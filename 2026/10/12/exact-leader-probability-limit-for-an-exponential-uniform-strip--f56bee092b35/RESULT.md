# Exact leader-probability limit for an exponential–uniform strip law
## Finding
Let \(X\sim\operatorname{Exp}(1)\) and \(V\sim\operatorname{Unif}(0,1)\) be independent, and put
\[
Z=(X,X+V).
\]
For iid copies \(Z_1,\ldots,Z_n\), let \(a_n\) be the probability that the sample contains a leader, meaning one observed vector that is coordinatewise at least every other observed vector. Then
\[
\lim_{n\to\infty}a_n
=
L
:=
\int_0^1\frac{dw}{1+w(e^w-1)}
=
0.7323592996919\ldots .
\]
In particular,
\[
L<\frac{\pi}{4}<0.8.
\]

The motivating paper studies this exact dependent model, proves a positive lower bound, and reports computer simulations suggesting that the limiting leader probability is at least \(0.8\). The exact limit above shows that this numerical suggestion is false.

## Assumptions and scope
The exponential distribution has rate one. The variable \(V\) is uniform on \((0,1)\) and independent of \(X\). The order on \(\mathbb R^2\) is coordinatewise.

The joint law is absolutely continuous on the strip
\[
\{(x,y):x>0,\ x<y<x+1\},
\]
so a leader, if present, is unique almost surely. The result is specific to this strip law and does not classify leader probabilities for general dependent bivariate distributions.

## Proof
The joint density is
\[
p(x,y)=e^{-x}\mathbf 1_{\{x>0,\ x<y<x+1\}}.
\]
The published distribution function on the strip is
\[
F(x,y)
=
1-e^{-x}-(x+1-y)\left(e^{-(y-1)_+}-e^{-x}\right).
\tag{1}
\]

For an absolutely continuous bivariate law, symmetry and conditioning on a nominated sample point give
\[
a_n
=
n\,\mathbb E\!\left[F(Z)^{n-1}\right].
\tag{2}
\]
Indeed, conditional on \(Z_1=z\), all other \(n-1\) sample vectors lie coordinatewise below \(z\) with probability \(F(z)^{n-1}\), and the \(n\) possible leaders are disjoint almost surely.

Write
\[
y=x+v,\qquad 0<v<1,
\]
and set
\[
w=1-v.
\]
Split (2) according to \(x<1\) and \(x\ge1\).

For \(0<x<1\),
\[
F(x,x+v)\le \Pr\{X'\le x\}\le1-e^{-1}.
\]
Hence that part of (2) is bounded by
\[
n(1-e^{-1})^{n-1},
\]
and therefore tends to zero.

Now suppose \(x\ge1\). Then \(y=x+v\ge1\), so (1) simplifies to
\[
F(x,x+v)
=
1-e^{-x}\left[1+w(e^w-1)\right].
\]
Define
\[
A(w)=1+w(e^w-1).
\]
For \(0\le w\le1\),
\[
1\le A(w)\le e.
\]
The contribution from \(x\ge1\) is consequently
\[
n\int_0^1\int_1^\infty
e^{-x}\left(1-A(w)e^{-x}\right)^{n-1}\,dx\,dw.
\]
For each fixed \(w\), substitute \(u=e^{-x}\). This gives the exact identity
\[
n\int_1^\infty
e^{-x}\left(1-A(w)e^{-x}\right)^{n-1}\,dx
=
\frac{1-\left(1-A(w)e^{-1}\right)^n}{A(w)}.
\tag{3}
\]
The right-hand side lies in \([0,1]\) and converges pointwise to \(1/A(w)\). Dominated convergence and the negligible \(x<1\) contribution now yield
\[
\lim_{n\to\infty}a_n
=
\int_0^1\frac{dw}{A(w)}
=
\int_0^1\frac{dw}{1+w(e^w-1)}.
\]

Finally, for every \(0<w\le1\),
\[
e^w-1>w.
\]
Therefore
\[
1+w(e^w-1)>1+w^2,
\]
and hence
\[
L
<
\int_0^1\frac{dw}{1+w^2}
=
\frac{\pi}{4}
<
0.8.
\]
This also proves analytically that the published simulation suggestion cannot be correct.

## Verification
The standalone script `verify.py` evaluates the limiting integral by composite Simpson quadrature using only the Python standard library. It independently checks the strict comparison with \(\pi/4\), the range \(1\le A(w)\le e\) on a deterministic grid, and the finite-\(n\) upper-strip formula (3) against direct numerical integration.

A successful run ends with
`VERIFY_OK limit=0.732359299692 pi_over_4=0.785398163397`.

The numerical calculation is a reproducibility check only. Existence of the limit and the bound below \(0.8\) are proved analytically above.

## Relationship to prior work
Răducan, Rădulescu, Rădulescu, and Zbăganu introduced and studied leader probabilities for random vector samples. Their Section 5.2 treats exactly
\[
X\sim\operatorname{Exp}(1),\qquad
V\sim\operatorname{Unif}(0,1),\qquad
Y=X+V,
\]
with \(X\) independent of \(V\). It records the density and the distribution function used in (1), obtains a positive lower bound \(e^{-1}\), and states that computer simulations suggest a limiting value at least \(0.8\). The inspected section does not evaluate the limit.

A later same-author paper studies quasi-unidimensional samples of the form \(Z=f(U)\), with support on a one-dimensional image, and does not cover this absolutely continuous two-dimensional strip model in the inspected full text.

Previously checked leader-probability results concern product laws, maximum-tie criteria, and discrete infinite-support constructions. They assume independent coordinates or different support geometry and do not imply the present dependent-strip calculation.

Targeted searches using the source DOI, the exact model, the integral, and the numerical value did not locate a published statement of the displayed limit.

## Limitations
The theorem resolves one explicit dependent bivariate model. It does not give a general criterion for leader probabilities or leader-property limits.

The decimal value is only a numerical evaluation of the proved integral. Literature searches cannot exclude an equivalent calculation under unrelated terminology, although the direct source and the most plausible same-author follow-up were inspected.

## References
1. A. M. Răducan, C. Z. Rădulescu, M. Rădulescu, and G. Zbăganu, “On the Probability of Finding Extremes in a Random Set,” *Mathematics* 10 (2022), 1623. DOI: 10.3390/math10101623. Published 10 May 2022.
2. G. Zbăganu, A. M. Răducan, and M. Rădulescu, “Computing Probabilities of Finding Extremes in a Random Set,” *Mathematics* 13 (2025), 3074. DOI: 10.3390/math13193074.
