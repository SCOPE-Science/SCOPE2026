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

The claim is the sharp best-approximation inequality for \(\overline z^{\,2}f\) in power-weighted Bergman Hilbert spaces, including all weight thresholds and equality spaces. The precise definitions and proof appear in `RESULT.md`.

`python verify.py` completed successfully using SymPy. The recorded output in `verify_output.txt` reports 1650 counted assertion groups. The script verifies the moment-ratio rational identity, the exact difference polynomial and its threshold roots, positivity of the mode variances, several direct polynomial projection calculations, and comparisons across sample weights. The proof in `RESULT.md` establishes the infinite-dimensional and continuum-of-weights assertions independently of those samples.

Critical checks: the mode-zero exception is handled explicitly; all denominator factors in the difference are positive for \(\alpha>-1\); the sign polynomial has one admissible root for each positive integer degree; each root lies strictly between its even and odd integer barriers; the residual modes are pairwise orthogonal, and equality requires support only in the maximizer eigenspace.

Limitations: finite test ranges do not certify unseen indices or parameters; the full text of a materially relevant 1988 source was unavailable for priority comparison; no independent scientific audit has been performed. This document contains only the actual performed checks and their limitations.
