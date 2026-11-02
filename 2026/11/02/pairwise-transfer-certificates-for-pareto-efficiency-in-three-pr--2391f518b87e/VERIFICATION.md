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

Run `python verify.py` with Python 3.10+ and no external dependencies. The program uses exact `fractions.Fraction` arithmetic, checks 49,927 three-project rational profile/outcome cases through denominator five by comparing six local transfers with an independently derived global feasibility threshold, constructs a valid strictly improving transfer whenever predicted, and verifies the four-project counterexample. Its printed `PASS` line is a finite test report, not a proof of the infinitely many real-input cases.

In a separate check, a SciPy linear program for a global weak-improvement polytope independently matched the transfer condition for 12,736 profile/outcome cases through grid denominator four. This optional separate check is not needed to execute the supplied script or establish the theorem.

The proof's decisive non-computational ingredients are the exact three-coordinate zero-sum norm identity, the one-or-two active-coordinate classification, and selection of a box-feasible elementary transfer that moves every active coordinate of a strictly improved agent toward its report. At four projects these conditions no longer force a dominating elementary transfer. No independent external audit has been performed.
