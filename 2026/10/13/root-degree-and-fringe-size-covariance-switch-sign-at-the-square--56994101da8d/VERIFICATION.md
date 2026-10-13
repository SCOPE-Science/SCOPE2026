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

`CHECK.py` requires Python 3 and only its standard library. Run `python CHECK.py`. The program exhaustively enumerates all recursive parent vectors for \(2\le n\le9\), which gives exactly 46,233 labelled trees. It tests the per-vertex fringe-size probability and conditional mean, the fringe-count expectation and covariance with the root degree, and exact sum identities; it reports 412 exact enumeration comparisons. It also checks the strict sign-threshold formula and monotonicity for each integer \(3\le n\le500\), giving 376,239 additional rational checks, and reports large-size numerical threshold diagnostics at three sizes. The terminal marker is `CHECK_OK`.

The proof in `RESULT.md` covers all admissible sample sizes through conditional uniform attachments, two factorial-binomial sum identities, a strict monotonicity inequality, and a uniform harmonic-tail expansion. None of the finite checks alone establishes universal correctness or absolute originality. No independent scientific audit or external proof certification has been performed.
