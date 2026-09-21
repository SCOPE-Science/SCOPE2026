# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.

The classification has two logically separate parts. Necessity first forces `a=b-1/2` and `c>=log sqrt(2pi)` from the leading Stirling term. The next digamma term gives

\[
f'(x)=\frac{b^2-b+1/6}{2x^2}+O(x^{-3}),
\]

so `f'<=0` excludes every `b<1/2-sqrt(3)/6`; the small-`x` behavior of `f'` excludes `b>1/2`. This leaves exactly the interval appearing in Guo's 2015 sufficiency theorem.

A direct sufficiency proof was also checked. The derivative is the Laplace transform of

\[
K_b(t)=\frac1t+\frac12-b-\frac{e^{-bt}}{1-e^{-t}}.
\]

After `t=2y` and `r=1-2b`, kernel positivity reduces to

\[
(1+ry)\sinh y>y e^{ry},\qquad 0\le r\le1/\sqrt3.
\]

The logarithm of the ratio decreases with `r`, and at `r=1/sqrt(3)` its derivative is positive on `(0,2]` by the partial-fraction lower bound for `coth y-1/y`, and on `[2,infinity)` by `coth y>1`. Hence `K_b(t)>0` for every `t>0`. The resulting Laplace representation yields strict complete monotonicity, including the case `c=log sqrt(2pi)`.

The endpoint algebra was independently recomputed: the roots of `b^2-b+1/6` are `1/2 +/- sqrt(3)/6`, and the kernel endpoint corresponds to `r=1/sqrt(3)`.

## Originality

PASS, to the best of our knowledge.

Guo (2015) was checked at Theorems 1 and 2 and its logarithmic-complete-monotonicity lemmas. It proves the coarse necessary condition `0<b<=1/2` and proves sufficiency on `[1/2-sqrt(3)/6,1/2]`, but does not state that the lower endpoint is necessary for the full family.

Searches covered the exact function, the source title and DOI, the threshold `1/2-sqrt(3)/6`, the polynomial `b^2-b+1/6`, and synonymous gamma/logarithmic-complete-monotonicity formulations. Guo's 2016 review and a 2019 survey of gamma-ratio complete monotonicity were checked as later status sources; no statement equivalent to the global classification was located.

Residual risk remains because specialized gamma-function results can be phrased in substantially different notation, and not every citing source was available or exhaustively inspected.

## Value

PASS.

The result converts a one-sided necessary condition plus a restricted sufficient theorem into a complete if-and-only-if parameter classification. The missing lower boundary is algebraic and sharp, and the proof identifies why it is forced: the sign of the first nonzero asymptotic term of `f'`. The positive Laplace kernel also gives a self-contained analytic mechanism for the sufficient range and shows strictness.

## Limitations

- The classification is specific to the stated gamma remainder family.
- Standard asymptotics and the partial-fraction expansion of `coth` are used and are not new.
- Equivalent prior coverage under different notation remains a residual originality risk.
- Independent audit has not been performed.
