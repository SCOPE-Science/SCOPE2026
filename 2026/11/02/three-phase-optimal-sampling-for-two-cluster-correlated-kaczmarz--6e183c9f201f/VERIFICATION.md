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

Run `python verify.py` in the package directory. It requires Python 3, NumPy, SciPy and SymPy. The script uses deterministic random generation and exits nonzero if an asserted check fails. `verification_output.txt` is the captured successful local result of this actual packaged script.

The symbolic certificate expands and simplifies \(\det(H(t)-L_0 I)=-\kappa(t-t_0)^2\), including precise \(a,b,d\) normalization. Four exact-rational full Gram experiments verify the characteristic polynomials and rates in all branches. A scalar numerical optimizer cross-checks 560 independent parameter/grid cases. Another 13,440 feasible asymmetric row-probability allocations provide numerical comparisons with the optimum. Those tests do not establish the all-parameter theorem: the mathematical argument, including the matrix-inequality argument proving unrestricted uniqueness, is in RESULT.md. No infinite-state or independent verification is claimed.
