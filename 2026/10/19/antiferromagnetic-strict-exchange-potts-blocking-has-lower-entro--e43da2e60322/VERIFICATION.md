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

# Reproducibility
Run `python verify.py` with the Python and SymPy versions specified in `requirements.txt`. The program implements the four-site condition and independently computes whole-ring energy changes after swaps. It checks the two symbolic five-state quotient characteristic polynomials for variable \(q\), equality-pattern lumpability and strong connectivity for \(q=3,4,5,6,7\), the full \(q=3\) characteristic polynomial, and exact finite-ring counts for \(q=3, N=4\ldots9\), \(q=4, N=4\ldots7\), and \(q=5, N=4\ldots6\) for both energy signs. It checks additional antiferromagnetic \(q=3\) transfer counts through \(N=12\). These experiments are finite and do not prove the infinite statements; the proof is in `RESULT.md`. No external independent audit was performed.
