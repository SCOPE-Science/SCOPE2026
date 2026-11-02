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

# Reproducibility and limits

The files `verify.py` and `verify_output.txt` provide an exact-arithmetic finite check of the theorem's combinatorial inputs. Running `python3 verify.py` prints `PASS: 178630 exact-arithmetic assertions`. The program enumerates independent binary configurations through seven coordinates at three rational biases, checks binomial witness probabilities and the exact BK-gap decomposition, verifies symmetric-disjoint-pivot equivalence under direct coordinate modification through six coordinates, and checks finite overlap covariance and binomial likelihood ratios.

The analytical proof in `RESULT.md` establishes the Gaussian windows, pivot asymptotics, conditional overlap law and sharp large-deviation prefactor. No finite experiment certifies those limits, novelty or mathematical value. Independent mathematical audit remains not performed.
