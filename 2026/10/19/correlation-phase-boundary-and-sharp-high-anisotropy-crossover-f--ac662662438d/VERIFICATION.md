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

# Reproducibility and limitations

The package contains \(\texttt{verify.py}\), a standalone deterministic Python 3 script using only the standard library, and the matching \(\texttt{verification_output.txt}\). Run it with \(\texttt{python3 verify.py}\).

The program performs 935 assertions. These encompass exact Fraction-arithmetic differentiation and geometric bounds over multiple parameter choices; independent polar-angle midpoint integration of the literal sketch error (not the proposed closed formula); correlation direction and balanced-marginal checks; the special equal-variance algebraic decomposition; and high-anisotropy double-scaling checks. The recorded execution passed all assertions.

The analytic proof of the Gaussian angular integral, the all-parameter monotonicity and equality alternatives, and the infinite asymptotics appears in \(\texttt{RESULT.md}\). Numerical integration is not an infinite proof and the finite tested parameter grid does not certify arbitrary parameters. No independent scientific audit or external formal certification is claimed.
