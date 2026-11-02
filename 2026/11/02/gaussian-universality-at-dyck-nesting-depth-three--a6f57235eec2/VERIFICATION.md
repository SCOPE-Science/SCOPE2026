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

# Verification record

Execute `python3 verify.py` with Python 3 and SymPy. The program independently rebuilds the three exact formal matrix generating functions, checks their simplified forms symbolically, enumerates all bounded-height Dyck words through semilength ten, compares the distributions, compares greedy-arch counts to explicit binary scattered-subsequence coverage through semilength six, and verifies the dominant-root derivatives and strict positivity of the variance coefficient. The observed output is `VERIFY_OK`.

This computation does not replace the infinite proof or constitute independent external scientific auditing. Its finite enumeration covers no words beyond its stated bounds. The analytic Gaussian conclusion uses the exact rational generating function, uniform local pole separation and characteristic-function convergence; it is not inferred from numerical moments.
