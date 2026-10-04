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

The central symbolic check is self-contained in `verify.py`. Running it with SymPy returns `VERIFY_OK` only after verifying
\[
\frac{d}{dt}\left(x_3+\frac{x_1^2}{2a}\right)=b-x_1^2
\]
and the component identities used to derive the stationary moments.

The remaining deductions are analytic. For bounded forward trajectories, boundedness of \(H\) makes the endpoint correction divided by \(T\) vanish. For recurrence at \(b=0\), continuity of \(H\) along a returning subsequence combines with monotonicity to force the nonnegative integral of \(x_1^2\) to vanish. For compactly supported invariant measures, all observables and Lie derivatives used are bounded on the support, so invariance permits integration of their Lie derivatives with mean zero.

The verification proves only the stated identities and their logical consequences. It does not establish existence of any compact invariant set, numerical chaos, Lyapunov exponents, or basin properties.
