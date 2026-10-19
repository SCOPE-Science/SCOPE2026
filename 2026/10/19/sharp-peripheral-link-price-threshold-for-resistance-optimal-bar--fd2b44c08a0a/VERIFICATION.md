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

# Verification procedures and limits

The `verify.py` file requires Python 3 and SymPy. The script reconstructs exact weighted Laplacians for four balanced barbells, including cases with vanishing peripheral--peripheral conductance, and matches the pseudoinverse trace with the claimed resistance formula. It then verifies budget identities, claimed optimum values, interior stationarity equations, boundary KKT signs, and threshold equality over exact rational/radical parameter grids. Running it should print `VERIFY_OK 628 exact Kirchhoff/feasibility/KKT/equality certificates; m=2..12`.

These exact finite tests are auxiliary; the all-integer-size and all-positive-price theorem uses the separate symbolic, Cauchy--Schwarz and convexity/KKT proof in `RESULT.md`. Neither a numerical optimizer nor the script establishes bibliographic novelty or independent external validation. The stated review was a self-review; no independent audit has been performed.
