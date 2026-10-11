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

The critical normalization check is
\[
\frac{2}{\pi}\cdot 2\pi\cdot\frac{p^2}{4}=p^2,
\]
which is the coefficient multiplying the radial integral after Poisson--Jensen and polar coordinates.

Freezing the decreasing factor at the outer radius gives
\[
p^2(a+bt)^{p-2}\int_0^t s\log\!\frac{t}{s}\,ds
=
\frac{p^2}{4}t^2(a+bt)^{p-2},
\]
so the new statement reproduces the recent published theorem exactly as a corollary.

For \(A=0\),
\[
p^2\int_0^t s(bs)^{p-2}\log\!\frac{t}{s}\,ds
=t^p b^{p-2}.
\]
When \(B\) has rank one, multiplying by \(\|B\|_2^2\) gives \(t^p\|B\|_p^p\), which is exactly the circular mean. This is an analytic equality check, not a numerical experiment.

For arbitrary Hilbert spaces, finite-rank compressions converge in \(S_p\) and hence in \(S_2\) for \(p\le2\); their operator norms do not exceed the original operator norms. This supplies the infinite-dimensional passage without an unproved compactness step.

No converse, upper bound, or complete equality classification has been verified or claimed.
