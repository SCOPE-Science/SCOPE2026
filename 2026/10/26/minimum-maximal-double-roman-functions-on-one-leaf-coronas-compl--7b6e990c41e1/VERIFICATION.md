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
# Reproducibility and scope

Execute `python verify.py` in the directory holding these files. The script independently encodes the original double Roman neighborhood conditions, the additional requirement that the zero-labeled set not dominate, and the counting formula for eligible \((D,S)\) pairs. It exhausts all simple graphs on up to four **labeled** vertices, adds five representative five-vertex bases, and tests cycles through order 15. Observed output is preserved verbatim in `verification_output.txt`.

The run traversed 80 base graphs and 2,696,420 candidate labelings (those not exceeding the constructive minimum weight). The claims for arbitrary finite \(G\) and every cycle length depend on the independent, complete mathematical proof in RESULT.md. A finite enumeration does not establish those claims on its own. No external or independent validation has been performed.
