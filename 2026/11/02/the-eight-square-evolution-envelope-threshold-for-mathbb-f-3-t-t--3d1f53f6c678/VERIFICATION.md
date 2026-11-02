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

# Verification of the exact eight-square rank

Run `python verify.py` with Python 3 and no nonstandard packages. The expected final line is `VERIFY_OK`.

The script constructs all forty projective classes of nonzero four-variable linear forms over \(\mathbb F_3\), constructs the ten-dimensional coefficient space of quadratic forms, and derives the four-dimensional span \(W\) of the squaring map's components. It verifies a six-dimensional quotient with kernel \(W\). It then checks all \(\binom{40}{3}=9880\) triples, deduplicating the 4420 rank-three quotient spans, and certifies every preimage closure has intersection dimension at most three with \(W\). Any hypothetical seven-summand decomposition would have quotient rank at most three and hence belong to one of these checked closures. This exhausts the lower-bound cases, rather than sampling them.

The script verifies the eight displayed squares by exact equality of their ten quadratic monomial coefficients with each of the four target coordinate quadratics and checks independence of those eight squares. Its exact closure census is: \((4,1):3213\), \((5,1):243\), \((5,2):567\), \((6,2):243\), \((7,2):45\), \((7,3):27\), \((8,3):81\), \((13,3):1\).

These checks establish the finite-field rank calculation. The ideal-embedding equivalence is separately justified in `RESULT.md`; the code is not a general theorem prover. No independent external validation has been performed.
