# Derive closed form for BCD(k) = sum_e N_e 1[e in 2M ∪ M_odd], verify polynomial/floor expression, then Delta(k)<0.
def BCD(k):
    M = list(range(-k+1, k+1))
    twoM = set(2*m for m in M)
    Modd = set(m for m in M if m % 2 != 0)
    cond = twoM | Modd
    return sum((2*k - abs(e)) for e in range(-(2*k-1), 2*k) if e in cond)

vals = {k: BCD(k) for k in range(1, 15)}
print(vals)
# guess: BCD = 2k^2 + something. differences:
for k in range(1, 15):
    print(f"k={k} BCD={vals[k]} BCD-2k^2={vals[k]-2*k*k} k^2/2={(k*k)/2}")
# candidate: BCD = (5k^2+1)/2 for odd? k=1:3, k=3:31? (45+1)/2=23 no. try BCD = ceil/floor mixes; fit quadratic per parity:
# odd k=1,3,5: 3,31,87 → 7k^2+... k=1:3, k=3:31, k=5:87: 87/25... fit ak^2+bk+c: (9a+3b+c=31, a+b+c=3, 25a+5b+c=87) → 8a+2b=28, 16a+2b=56 → 8a=28 → a=3.5, b=0, c=-0.5 → (7k^2-1)/2. k=1:3 ✓ k=3:31 ✓ k=5:87 ✓ k=7: (343-1)/2=171?
# even k=2,4,6: 14,56,126 → 14=7*4/2, 56=7*16/2, 126=7*36/2 → 7k^2/2. k=2:14 ✓ k=4:56 ✓ k=6:126 ✓.
# so BCD = 7k^2/2 (even), (7k^2-1)/2 (odd).
for k in range(1, 15):
    pred = (7*k*k)//2 if k % 2 == 0 else (7*k*k-1)//2
    assert vals[k] == pred, (k, vals[k], pred)
print("BCD closed form CONFIRMED: 7k^2/2 even, (7k^2-1)/2 odd")
# full chi: deconed c2 = Sig = P2 - T3 + Q with P2=30k^2, ABC=ABD=3k^2, ACD=2k^2, Q=2k^2:
# Sig = 30k^2 - (6k^2+2k^2+BCD) + 2k^2 = 24k^2 - BCD = 24k^2 - 7k^2/2 = 41k^2/2 (even); odd: 24k^2-(7k^2-1)/2 = (41k^2+1)/2 ✓ matches brute S(k)!
# Delta = 81k^2 - 4*Sig = 81k^2-82k^2 = -k^2 (even); odd: 81k^2-82k^2-2 = -(k^2+2) ✓ matches!
for k in range(1, 15):
    BCDv = (7*k*k)//2 if k % 2 == 0 else (7*k*k-1)//2
    Sig = 30*k*k - (6*k*k + 2*k*k + BCDv) + 2*k*k
    D = 81*k*k - 4*Sig
    expD = -(k*k) if k % 2 == 0 else -(k*k+2)
    assert D == expD < 0, (k, D)
print("Delta(k)<0 for all k CONFIRMED: -k^2 (even), -(k^2+2) (odd)")
