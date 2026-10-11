# Review of Square-root saturation of the affine-balanced pre-Schwarzian shadow

## Correctness

PASS. The source gives the exact formulas
\[
x_k=
\frac{3-k^2-\sqrt{(1-k^2)(9-k^2)}}2,
\qquad
C(k)=\frac{2x_k^{3/2}}{k(1+x_k)},
\]
and identifies
\[
r_k=\sqrt{x_k}/k
\]
in its sharp Schwarz-Pick model. It also gives
\[
K_{\mathrm{aff}}=(1+k)/(1-k).
\]

Writing
\[
u=K_{\mathrm{aff}}^{-1/2}
\]
makes
\[
k=(1-u^2)/(1+u^2)
\]
exact. Direct substitution gives an algebraic function analytic at
\[
u=0,
\]
and its Taylor coefficients yield the claimed expansions. The expansion of
\[
x_k
\]
was separately checked in the source critical equation
\[
x^2+(k^2-3)x+k^2=0.
\]
No finite sampling is used to infer the endpoint theorem.

## Originality

PASS. The full source was inspected at the affine-invariant definitions, Theorem 1.5, Lemma 9.2, Proposition 9.4, and the sharpness argument. It gives the exact constant, proves monotonicity, states only the qualitative limit
\[
C(k)\to1
\]
at
\[
k\to1^-,
\]
and derives a small-\(k\) expansion. The inspected text contains no high-distortion expansion and no boundary-layer asymptotic for the maximizing radius.

Searches using the source identifier, high-distortion language, the pre-Schwarzian constant, the affine radius, and square-root endpoint formulations did not locate an implication-equivalent published result.

A previously recorded finding based on the same source concerns a Schwarzian shadow functional as
\[
k\to0.
\]
It neither contains nor implies the present
\[
k\to1
\]
pre-Schwarzian saturation law.

## Value

PASS. The source's principal affine invariant is the minimal quasiconformal distortion
\[
K_{\mathrm{aff}}.
\]
Its sharp pre-Schwarzian estimate becomes weakest as this invariant grows, but the source only records convergence of the sharp constant to
\[
1.
\]

The new result quantifies that degeneration on the intrinsic distortion scale and shows that it is governed by a square-root law rather than by
\[
K_{\mathrm{aff}}^{-1}.
\]
Tracking the maximizing disk radius at the same time identifies the geometric mechanism: sharpness migrates toward the unit circle on exactly half the constant-deficit scale. This gives a concrete high-distortion boundary layer complementary to the source's low-distortion quadratic theory.

Same-model review: passed. Independent audit: not yet performed.
