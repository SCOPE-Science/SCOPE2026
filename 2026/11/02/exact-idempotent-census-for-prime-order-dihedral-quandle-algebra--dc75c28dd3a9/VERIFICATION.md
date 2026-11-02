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
# Reproducibility and verification

Run `python3 verify.py` in the same directory. It enumerates each coefficient vector in the stated finite-field quandle algebra, independently computes all bilinear products from \(e_xe_y=e_{2y-x}\), and counts those satisfying \(u^2=u\). Checks include the entire \(2^{17}\)-element algebra at \((p,q)=(17,2)\), 177147 elements at \((11,3)\), 823543 at \((7,7)\), nonprime fields \(\mathbb F_4\) and \(\mathbb F_9\), and modular characteristics \(3,5,7\). The observed counts exactly match the respective explicit formulas.

The passing output ends with `VERIFY_OK all independent coefficient-table checks passed`; this was observed from the actual packaged script. Arithmetic-only evaluations beyond the exhaustively checked fields do not constitute enumeration certificates. Universal correctness is established by the separate Fourier/orbit and truncated-logarithm proofs in RESULT.md. No independent mathematical audit, formal proof certification, or experimental extrapolation is claimed.
