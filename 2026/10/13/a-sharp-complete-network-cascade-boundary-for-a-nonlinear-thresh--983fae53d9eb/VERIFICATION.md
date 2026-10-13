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

# Reproducible finite checks and analytic scope

Execute `python3 verify.py` using a standard Python 3 interpreter. The script operates only on deterministic algebraic expressions: it tests the sharp polynomial factorization at criticality, verifies admissibility and threshold ordering across 33 exact-rational parameter grids, checks signs either side of the transition, and confirms saturation is inactive before opinion \(1/2\) at a discrete tie. Its floating-point check evaluates the closed-form arctangent expression at increasingly small coupling for four population sizes, and checks approach to the proved limit.

The tested computations do **not** establish the universal theorem: the full proof relies on scalar uniqueness and monotonicity, exact equilibrium classification, and a controlled improper-parameter limit. There is no external verification or independently audited certificate. A successful run reports `VERIFY_OK`; failures raise assertions.
