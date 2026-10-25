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

# Verification

Use Python 3 (standard library only) to run `python3 composite_resolution_verify.py` from the directory containing that program. Its stored output is `verification_output.txt` and begins with `VERIFY_OK`.

The program generates the composite alphabet as integer four-tuples of sum \(k\); independently counts admissible short strings and compares them with the weighted transfer recurrence. It checks the exact bin sums and both tail inclusions for every resolution \(2\leq k\leq60\) and multiple rational tolerances. It also checks the complete four-bin graph at tolerance \(1/k\), and approximates its spectral radius against the analytic radical. No probabilistic Monte Carlo argument is used.

The infinite statements are established by the analytic inequalities, the limiting logarithm argument, and the four-vertex characteristic polynomial in `RESULT.md`; no finite checker or stored output certifies those statements on its own. No external or independent audit has been performed.
