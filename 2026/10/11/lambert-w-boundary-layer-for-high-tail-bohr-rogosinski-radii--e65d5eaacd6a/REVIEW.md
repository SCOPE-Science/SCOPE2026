# Review of Lambert-W boundary layer for high-tail Bohr–Rogosinski radii

## Correctness

PASS. The source theorem supplies the exact sharp-root equation
\[
p\frac{1-r^m}{1+r^m}
=
\frac{2r^N}{1-r}.
\]
The root function is strictly decreasing in \(r\), and increasing \(N\) strictly raises it at every fixed \(r\), proving strict monotonicity of the roots.

The limit must be \(1\): a limit below \(1\) would make the right-hand side tend to zero while the left-hand side tends to a positive constant.

Writing
\[
\varepsilon=1-r,
\qquad
x=N\varepsilon,
\]
the exact equation first gives
\[
N[-\log(1-\varepsilon)]
=
2\log(1/\varepsilon)+O(1).
\]
This proves
\[
x\to\infty,
\qquad
x=O(\log N),
\]
and therefore
\[
N\varepsilon^2\to0.
\]
Only after this control is established is
\[
(1-\varepsilon)^N=e^{-x}(1+o(1))
\]
used. The resulting relation
\[
x^2e^x
=
\frac{4N^2}{pm}(1+o(1))
\]
is inverted by the principal Lambert function, yielding
\[
x
=
2W\!\left(\frac{N}{\sqrt{pm}}\right)+o(1).
\]
The expanded logarithmic formula follows from the standard large-argument expansion of \(W\).

## Originality

PASS. The 2025 lead article was inspected throughout. It proves the sharp root equation but does not state a large-tail rate. Its explicit limiting remark concerns a different parameter direction.

The 2021 scalar predecessor states only the qualitative limit
\[
R_{m,N}\to1
\]
as \(N\to\infty\). It supplies no Lambert-\(W\) scale, log-log correction, or powered-\(p\) version.

The closely related 2026 refinement was also inspected in full. Its improved functional fixes the coefficient tail at the first index and does not contain a large-\(N\) theorem for the source family.

Targeted searches for the exact equation, Lambert-\(W\) inversion, high-tail asymptotics, and equivalent sharp-radius formulations did not locate an implication-equivalent published result. The main residual risk is older literature using substantially different notation.

## Value

PASS. The tail index \(N\) is an intrinsic parameter of the Bohr–Rogosinski functional: it determines where the coefficient tail begins. The scalar predecessor records that the sharp radius tends to \(1\) as \(N\) grows, leaving the natural quantitative question of how fast this happens.

The answer is structurally nontrivial. The sharp radius lies in a singular boundary layer where the small geometric deficit
\[
1-r^m
\]
balances the exponentially small tail factor
\[
r^N.
\]
This competition produces the Lambert-\(W\) law and the universal \(-2\log\log N\) correction. The result therefore resolves a natural asymptotic gap in a sharp radius theorem and identifies the exact scale needed for quantitative high-tail estimates.

Same-model review: passed. Independent audit: not yet performed.
