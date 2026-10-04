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

The proof is algebraic. The key checks are:

1. Specializing the cited L-ADMM update gives the displayed scalar formulas, and the exact \(w\)-optimality relation implies \(y_{k+1}=mw_{k+1}\) after every completed update.
2. Substitution of \(y=mw\) yields the stated \(2\times2\) recurrence matrix.
3. Its characteristic trace and determinant are
\[
T=\frac{hr+2h+r^2-r-1}{(h+r)(r+1)},\qquad
D=\frac{h-1}{(h+r)(r+1)}.
\]
4. The discriminant numerator has quadratic-in-\(h\) discriminant \(-32r^2(r-1)(r+1)\), producing the two repeated-root boundaries only when \(0<r<1\).
5. With \(c=(r+1)/(3r+1)\), the identity
\[
p(c)=-\frac{2r^2(r-1)}{(r+1)(3r+1)^2}
\]
controls the derivative sign of the real roots and proves the three parameter regimes.
6. At \(r=1\), the eigenvalues factor exactly as \(1/2\) and \((h-1)/(h+1)\), giving the full optimal plateau \([1/3,3]\).

`verify.py` uses only the Python standard library. It checks the recurrence identities in exact rational arithmetic at several rational parameter points, checks the balanced factorization, evaluates every closed-form branch, and performs deterministic grid/perturbation regression tests. These finite tests are supplementary; the global minimization is established by the analytic sign argument in `RESULT.md`.

Run:

`python3 verify.py`

Expected output:

`VERIFY_OK`
