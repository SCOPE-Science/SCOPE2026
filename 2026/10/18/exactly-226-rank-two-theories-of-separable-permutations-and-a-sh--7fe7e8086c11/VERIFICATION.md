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

# Verification instructions

From the same directory as the embedded certificate, run:

```sh
python3 verify_permutation_rank2.py
```

This uses only the standard Python library and verifies a **complete finite-state closure**, not an incomplete search at bounded permutation length. Every listed state is witnessed by a separable permutation; every ordered pair of states is closed under both direct sum and skew sum; and every proposed minimal length obeys the universal subadditivity inequalities and is attained by its witness. These checks prove all-size coverage and minimum-length optimality once the quadrant and rank-two composition lemmas in `RESULT.md` are established.

The verifier also independently enumerates all separable permutations through length ten and checks every resulting signature directly from ordered point pairs. It checks the special signature of the permutation \(2,5,3,1,4\), which is absent from the exhaustive separable-state list.

The exact completed stdout is included as `verification_output.txt`. Verification was performed on the certificate and verifier as embedded here. These computational and mathematical checks do not constitute an independent external audit or an assessment of literature priority.
