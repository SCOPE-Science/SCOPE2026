# Review of Exact detachment crossover for Paley–Wiener concentration

## Correctness

PASS. The unshifted weighted discrepancy has the exact identity
\[
D_0(E_{\varepsilon,b})
=
\int_{r-\varepsilon}^{r}
\int_0^b
-u_s'(x+t)\,dt\,dx.
\]
When
\[
b\to0,
\qquad
\varepsilon\le b,
\]
the integration rectangle collapses uniformly to the endpoint \(r=s/2\), so this equals
\[
-u_s'(r)\varepsilon b(1+o(1)).
\]

The interval center is a unique strict maximizer and has curvature
\[
2u_s'(r)<0.
\]
The detached perturbation changes the first center derivative by only
\[
O(\varepsilon b),
\]
so the optimal center moves by
\[
O(\varepsilon b)
\]
and improves the mass by only
\[
O(\varepsilon^2b^2).
\]
The recent stability proof then supplies
\[
0\le\mathcal D(E)-\eta(E)\le A_s\mathcal D(E)^2,
\]
which preserves the same leading asymptotic.

## Originality

PASS. The October 2026 primary source introduces exactly the family
\[
E_{\varepsilon,b}
\]
and gives only two order comparisons: quadratic loss when \(b=\varepsilon\), and linear loss in \(\varepsilon\) for fixed positive \(b\). It does not calculate the leading coefficient or the joint regime in which \(b\) itself tends to zero.

The earlier optimal-concentration theorem establishes the interval extremizer but contains no stability expansion for a detached piece. Classical prolate theory supplies the endpoint slope and spectral gap but not the set-perturbation crossover.

Exact-source and implication-equivalent searches did not locate a published statement of the product law
\[
\eta\sim-u_s'(s/2)\varepsilon b.
\]

## Value

PASS. The source uses the detached-piece example to motivate why symmetric difference loses displacement information. The exact product law quantifies precisely the missing information: near the interval boundary the concentration deficit measures moved length times travel distance, with an intrinsic sharp coefficient supplied by the optimizer's boundary slope.

This unifies the source's adjacent-piece quadratic regime with the previously unstated mesoscopic regime and gives an exact leading constant rather than only an order estimate.

Same-model review: passed. Independent audit: not yet performed.
