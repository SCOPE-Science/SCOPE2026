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
# Verification evidence and limits

The complete proof, including all-distance derivative signs, is in `RESULT.md`. The accompanying `verify.py` is a standalone reproducibility test needing Python, NumPy, and SciPy; run `python verify.py`.

The checker carries out **129 finite checks**: exact quadrature and derivative roots for seven initial positions, reciprocal-difference identities on 25 position/coupling pairs, non-Hermitian finite-volume propagation with 420 sites through time 140 on six cases, and three large-distance root comparisons to the two-term expansion. Every assertion passed on the supplied run. Selected optimized ratios were \(\eta_2\approx1.128036558506\), \(\eta_3\approx1.035875451023\), \(\eta_4\approx1.014695527529\).

The finite-time capture estimate is strictly below its infinite-time analytic value because some surviving probability remains at the observation time. These checks cannot prove that the half-line spectrum or its all-time absorption is exhaustively represented by a finite truncation; the exact input integral and the analytic proof supply that scope. The original closed absorption formula is attributed rather than recertified here. No independent audit or external certification was performed.
