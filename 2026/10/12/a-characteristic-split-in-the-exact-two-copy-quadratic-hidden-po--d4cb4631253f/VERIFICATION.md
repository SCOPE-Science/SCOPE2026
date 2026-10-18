---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

PASS: Reconstructed the actual two-copy quadratic polynomial map (b,c)->(xb+yc,xb²+yc²). For every xy(x+y)≠0, (x+y)w−v²=xy(b−c)². For odd q, with each fixed v, the square map has one zero and (q−1)/2 double preimages: exactly q fibers of cardinality 1 and q(q−1)/2 of cardinality 2. In characteristic 2 squaring is a bijection of every finite field, yielding q² singleton fibers. There are (q−1)(q−2) good (x,y). Substitution into the actual source Eq. (16), including its q^(−6) normalization, gives the claimed finite-q formulas and limiting 1/2 and 1. Separate independently written enumeration checked odd primes 3,5,7 and F4, while the symbolic argument covers all prime powers; it does not claim optimal discrimination or q=2 success.

## originality

PASS

The sharp two-case exact success law is absent from the explicitly inspected 2007 measurement construction, which gives the fiber map and constant lower-bound analysis; the prior implication is nontrivial in that it needs the exact singleton/doubleton distributions before the nonlinear squared root sum can be evaluated. The construction and normalization themselves are not new.

## value

PASS

PASS: The numerical size of success in a specific standard quantum procedure is a natural benchmark. The same 2007 scheme is near-certain for characteristic-two extensions and approaches only 1/2 in odd characteristic; this precise field-arithmetic bifurcation is not conveyed by the original constant lower bound. It is independently useful to researchers choosing finite-field implementations even though the proof uses elementary finite-field algebra. The result does not claim a stronger general quantum-algorithm theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
