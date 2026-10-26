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

The reproducibility program `verify.py` was executed with Python 3, `numpy` and `mpmath`. It passed 319 independent finite assertions: a three-by-three Laplacian eigendecomposition, comparison of 114 endpoint amplitudes against independent cosine formulas, 150 exact weighted-square identities evaluated to high precision, and seven Pell-recurrence checks with optimized and unshifted times. The computed dimensionless constant is \(\pi^4/144=0.6764520210694613696975\ldots\); for the example with \(M=12,k=1\), it is \(\pi^4/12=8.11742425283353643637\ldots\).

Execute `python verify.py`; Python package requirements are supplied in `requirements.txt`.

The exact global lower bound rests on the proof in `RESULT.md`: bounded normalized infidelity forces errors of order \(O(s^{-1})\) around odd/even phase multiples, after which a completed-square identity reduces the lower bound to the nonzero integer norm \(p^2-3q^2\). No finite computation can replace this quantifier argument. The asymptotic statement is confined to the reduced cosine-wave propagator. The weak-coupling limit in the underlying discrete walk is only invoked at fixed reduced observation times.
