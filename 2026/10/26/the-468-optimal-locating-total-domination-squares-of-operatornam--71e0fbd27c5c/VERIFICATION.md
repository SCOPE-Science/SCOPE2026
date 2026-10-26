---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification details

The projective-coordinate model indexes the 13 normalized nonzero triples over \(\mathbb F_3\), regarding triples as point vectors and line normals. Incidence is zero dot product modulo three. The 13-by-13 relation has row and column degree four, and every pair of distinct lines shares exactly one point.

Run `python3 verify.py`. This enumerates all 4-, 5- and 6-point blocking sets and 4-, 5- and 6-line covers with combined cardinality at most ten, tests the open-neighborhood locating-total condition directly, and compares the resulting minimum sets with an independent constructive parameterization by \((\ell,q,x,p,t)\). It then enumerates every legal one-vertex replacement between minimum sets and checks the partition into exactly 468 disjoint four-cycles. Verified output:

```text
OPTIMUM_OK min_size=10 states=1872 split=5+5
CLASSIFICATION_OK parameters=468 blocks_of_four
EXCHANGE_OK graph=468*C4 vertices=1872 edges=1872 degree=2
ALL_VERIFY_OK
```

Run `g++ -O2 -std=c++17 verify_alt.cpp -o verify_alt` and `./verify_alt`. This separately enumerates all blocking point masks and covering line masks, evaluates all relevant signature constraints, constructs the exchange graph and checks the connected-component and degree spectra. Its relevant completed output was `min 10 states 1872`, `5+5=1872`, `edges 1872 deg 2:1872`, and `components 4:468`.

These computations are exhaustive for the stated finite domain but do not assert anything about higher-order projective planes, unexamined publication history or independent validation. The symbolic argument supplies the lower bound, equality classification and exchange isomorphism without relying on a numerical search timeout.
