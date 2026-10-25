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

# Verification and reproducibility

The mathematical evidence is in `RESULT.md`, especially the exact completed-square identity for \(g_Q\), the exhaustive interval \([t,\sqrt2t]\), the inspected published planar plank reduction, and the independent convolution formula that proves all single-strip equality cases. For \(0<W<2\) these prove the two branches and the angular classification. The critical published reference is E. Bakaev and A. Polyanskii, arXiv:2607.27483, Corollary 7, Lemma 11, Theorem 12; the statement is cited rather than independently reproved.

Execute `python3 check_square.py` from this directory with Python 3. The script uses only the standard library and reconstructs intersection polygons by a separate exact-rational half-plane clipping method. It confirms the rational optimizing witness at \(W=10/7\) with area \(148/49\), compares strictly worse noncentral placements, checks six further exact rational cases, and conducts ten sampled angular sweeps and transition-gain comparisons. Sampling supports the algebraic proof but cannot establish an infinite optimum.

Known limits: widths \(W=0\) and \(W\ge2\) are excluded from the main statement; no rotations, arbitrary rectangles or higher-dimensional cubes, and no uniqueness claim for multi-plank families are addressed. No independent audit has been performed.
