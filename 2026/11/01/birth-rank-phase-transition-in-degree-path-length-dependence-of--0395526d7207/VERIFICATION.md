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

# Reproduction and limits

Run `python3 verify.py` in the directory containing this file and the companion verifier. It enumerates the independent-parent representations of uniform random recursive trees for every size from three through eight and checks exact joint mixed moments. It checks a separate algebraic identity and the single sign transition over a larger bounded range (sizes three through five hundred).

The proof for every finite order and for the asymptotic transition scale is in `RESULT.md`. Enumeration and executable checks alone cannot establish the unbounded theorem. Reproducing this script does not amount to independent auditing of the manuscript.
