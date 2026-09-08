"""Lane 260 FINAL BUILD — canonical committed artifacts.
S3 := x^14 EXACTLY as the commitment string states (literal, auditable).
S3supp := x^30, the true Galois inverse on GF(2^5)*, as documented supplement.
"""
import hashlib, json

def sha_words(seed, need):
    out, c = [], 0
    while len(out) < need:
        d = hashlib.sha256(seed.encode() + b':' + c.to_bytes(4, 'big')).digest()
        for i in range(0, 32, 4):
            out.append(int.from_bytes(d[i:i+4], 'big'))
        c += 1
    return out

def fisher_yates(n, seed):
    a = list(range(n)); w = sha_words(seed, n); k = 0
    for i in range(n - 1, 0, -1):
        j = w[k] % (i + 1); k += 1
        a[i], a[j] = a[j], a[i]
    return a

def gmul(a, b, mod, n):
    r = 0
    while b:
        if b & 1: r ^= a
        a <<= 1
        if a >> n: a ^= mod
        b >>= 1
    return r

def gpow(a, e, mod, n):
    r = 1
    while e:
        if e & 1: r = gmul(r, a, mod, n)
        a = gmul(a, a, mod, n); e >>= 1
    return r

M5 = int('100101', 2); M6 = int('1000011', 2)
S1 = [0xC,0x5,0x6,0xB,0x9,0x0,0xA,0xD,0x3,0xE,0xF,0x8,0x4,0x7,0x1,0x2]
S2 = [gpow(x, 3, M5, 5) for x in range(32)]
S3 = [gpow(x, 14, M5, 5) for x in range(32)]                       # literal commitment
S3supp = [0 if x == 0 else gpow(x, 30, M5, 5) for x in range(32)]  # true inverse
S4 = [gpow(x, 3, M6, 6) for x in range(64)]
S5 = [0 if x == 0 else gpow(x, 62, M6, 6) for x in range(64)]
S6 = fisher_yates(32, 'SCOPE-260-n5-v1')
S7 = fisher_yates(64, 'SCOPE-260-n6-v1')
B  = [(((v & 1) * ((v >> 3) & 1) + (((v >> 1) & 1) * ((v >> 4) & 1)) +
        (((v >> 2) & 1) * ((v >> 5) & 1))) & 1) for v in range(64)]

tt = {'S1': S1, 'S2': S2, 'S3': S3, 'S3supp': S3supp, 'S4': S4,
      'S5': S5, 'S6': S6, 'S7': S7, 'B': B}
with open('output/artifacts/truth_tables.json', 'w') as f:
    json.dump(tt, f)
defs = {
  'S1': 'PRESENT nibble sBox C536B90AD3EF84712 (list index = input)',
  'field5': 'GF(2^5) = GF(2)[t]/(t^5+t^2+1), elements as ints 0..31 (bit i = coeff of t^i)',
  'field6': 'GF(2^6) = GF(2)[t]/(t^6+t+1), elements as ints 0..63',
  'S2': 'x -> x^3 on GF(2^5)',
  'S3': 'x -> x^14 on GF(2^5) (0 -> 0); LITERAL commitment string; NOT the Galois inverse',
  'S3supp': 'x -> x^30 (0 -> 0), the TRUE multiplicative inverse on GF(2^5)*; supplement',
  'S4': 'x -> x^3 on GF(2^6) (a general map, not a permutation: gcd(3,63)=3)',
  'S5': 'x -> x^62 (0 -> 0), the TRUE multiplicative inverse on GF(2^6)*',
  'S6': "SHA256('SCOPE-260-n5-v1':uint32be counter) word stream, Fisher-Yates of 0..31",
  'S7': "SHA256('SCOPE-260-n6-v1':uint32be counter) word stream, Fisher-Yates of 0..63",
  'B': 'Maiorana-McFarland f(v)=x0*y0+x1*y1+x2*y2, x=bits0-2, y=bits3-5',
}
with open('output/artifacts/definitions.json', 'w') as f:
    json.dump(defs, f, indent=1)
print('wrote truth_tables + definitions')
