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

# Reproduction and scope

Run `python verify.py` with Python 3 and SymPy. The script must end with `VERIFY_OK`. The symbolic checks cover the exact two-state transfer matrix for every ordered pair of distinct length-two binary words; the four trace/determinant classes; generating functions; all three root-resultant identities; and the fair-switching eigen/rank-one certificates. Exhaustive finite checks over digit paths supplement the proof. Analytic claims for all \(n\) and for an open continuum of \(p\) are supported by the Cayley--Hamilton, rank-one and Perron--Frobenius arguments in `RESULT.md`, not by enumeration.

The claim is annealed. No independent audit was performed; bibliographic residual risks are recorded in the scientific review.
