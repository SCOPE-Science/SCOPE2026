"""Certify maximal-order unit norm sign for all 81 D via exact CF convergents.

Theory used (cited in DRAFT.md):
- l = period of sqrt(D). l odd  => conv[l-1] has norm -1 (integer unit, hence in O_K): N=-1.
- l even => no integer x^2-Dy^2=-1. A half-integer unit of norm -1 would give
  x^2-Dy^2=-4 with x,y both odd (D=1 mod 4). For D>16, Legendre's approximation
  theorem forces x/y to be a convergent of sqrt(D) (since |x/y-sqrtD|<1/2y^2);
  convergent norms repeat with period dividing 2l. So checking k<2l is COMPLETE:
  no odd-odd N_k=-4  =>  no norm -(-1) unit in O_K  =>  N=+1 certified.
Writes norms_cert.json.
"""
import json, math, os
HERE = os.path.dirname(os.path.abspath(__file__))

def cf_sqrt(D):
    a0 = int(math.isqrt(D))
    assert a0 * a0 != D
    m, den, a = 0, 1, a0
    per = []
    while True:
        m = den * a - m
        den = (D - m * m) // den
        a = (a0 + m) // den
        per.append(a)
        if a == 2 * a0:
            break
    return a0, per

def convergents(a0, per, n):
    seq = [a0] + (per * ((n) // len(per) + 1))[:n]
    out = []
    pm2, pm1 = 0, 1
    qm2, qm1 = 1, 0
    for a in seq:
        pm2, pm1 = pm1, a * pm1 + pm2
        qm2, qm1 = qm1, a * qm1 + qm2
        out.append((pm1, qm1))
    return out

rows = json.load(open(os.path.join(HERE, "census.json")))
cert = []
for r in rows:
    D = r["D"]
    assert D > 16
    a0, per = cf_sqrt(D)
    l = len(per)
    assert l == r["period"], (D, l, r["period"])
    if l % 2 == 1:
        convs = convergents(a0, per, l)
        x, y = convs[l - 1]
        assert x * x - D * y * y == -1, (D,)
        cert.append(dict(D=D, l=l, N=-1, how="integer convergent norm -1"))
    else:
        convs = convergents(a0, per, 2 * l)
        bad = [(k, x, y) for k, (x, y) in enumerate(convs)
               if x * x - D * y * y == -4 and (x & 1) and (y & 1)]
        assert not bad, (D, bad)
        # also confirm no integer -1 among convergents (consistency)
        assert not any(x * x - D * y * y == -1 for x, y in convs), (D,)
        cert.append(dict(D=D, l=l, N=1, how="no odd-odd N=-4 among first 2l convergents"))
    assert ({-1: -1, 1: 1}[cert[-1]["N"]] if False else cert[-1]["N"]) == r["N"], (D,)
print("fields certified:", len(cert))
print("N=-1:", sum(1 for c in cert if c["N"] == -1), " N=+1:", sum(1 for c in cert if c["N"] == 1))
json.dump(cert, open(os.path.join(HERE, "norms_cert.json"), "w"))
print("NORMS_CERT_OK")
