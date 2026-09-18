# Same-model review

Same-model review: passed. Cross-model review: not yet performed.

## Correctness

**PASS.**

The FGM composite was differentiated directly:
\[
F_{m,\theta}
=
Uv+\theta(U-U^2)(v-v^2),\qquad U=\prod_i x_i.
\]
The identities
\[
\partial_{x_1}\cdots\partial_{x_m}U=1,\qquad
\partial_{x_1}\cdots\partial_{x_m}U^2=2^mU
\]
give
\[
g_{m,\theta}=1+\theta(1-2^mU)(1-2v).
\]
The factor multiplying \(\theta\) has exact range
\([-(2^m-1),2^m-1]\), so nonnegativity is equivalent to
\(|\theta|\le(2^m-1)^{-1}\). Groundedness and every one-dimensional uniform margin were checked from the copula boundary identities. Thus the density sign condition gives the claimed necessary and sufficient copula criterion.

The general differential identity was checked algebraically. With \(D=u\partial_u\),
\[
\partial_{x_1}\cdots\partial_{x_m}h(\prod_i x_i)
=
u^{-1}D^m h(u)
=
(1+D)^{m-1}h'(u).
\]
Taking \(h(u)=\partial_v C(u,v)\) yields
\((1+u\partial_u)^{m-1}c(u,v)\).

The entropy inequality uses only an exact mean-preserving-spread relation. Under Lebesgue measure on the cube,
\[
A_m=1-\prod_{i=1}^m(2X_i),\qquad
A_1=\mathbb E[A_m\mid X_1].
\]
For fixed \(B=1-2V\), the function
\[
(1+\theta Ba)\log(1+\theta Ba)
\]
is convex and, in the strict admissible range, has second derivative bounded below by
\[
\frac{\theta^2B^2}{1+|\theta|(2^m-1)}.
\]
The conditional variance and elementary second moments give the displayed quantitative gap. At \(m=2,\theta=1/4\), substitution gives exactly \(1/378\). This example lies strictly within the admissible threshold \(1/3\), so entropy nonadditivity is not a consequence of an invalid composite.

Boundary cases were checked: \(m=1\) reduces to ordinary FGM; \(\theta=0\) gives independence and equality; fixed nonzero \(\theta\) eventually violates the threshold as \(m\) increases.

## Originality

**PASS, to the best of our knowledge.**

Lu (arXiv:2609.20512, 2026) was inspected around the proposed blockwise substitution, closure statement, product-density formula and entropy-additivity claim. The present result is directly relevant to those statements, but it does not treat their general formulation as a new open problem: classical work already shows that ordinary scalar copulas do not universally combine prescribed non-overlapping multivariate marginals by naive substitution.

Brechmann (2014) was inspected through the article abstract and searchable text describing the motivation for hierarchical Kendall copulas. It explicitly uses the Kendall distribution function as the multivariate analog of the probability integral transform and records the classical obstruction to direct scalar-copula linking of arbitrary non-overlapping multivariate marginals.

Li, Scarsini and Shaked (1996) was identified as a primary older source on linkage functions for distributions with given non-overlapping multivariate marginals. Its abstract and bibliographic record were inspected, but its complete full text was not. Fan and Henry (2023) was inspected through its abstract and bibliographic record; it constructs vector copulas by measure transport and proves a vector Sklar theorem.

Searches for combinations of `FGM`, `Farlie Gumbel Morgenstern`, `product/independence block`, `multivariate marginal substitution`, `Sklar substitution`, `copula entropy`, the threshold forms `2^m-1` and `1/(2^m-1)`, and the Euler-operator form did not locate a prior statement of the exact FGM threshold, the displayed independence-block operator criterion, or the quantitative entropy defect.

The principal residual originality risk is the older literature on distributions with prescribed non-overlapping multivariate marginals, including linkage and related constructions. Some of that literature was accessible only through abstracts or secondary searchable excerpts. It may contain equivalent special-case differential conditions under different notation. Accordingly, no originality is claimed for the general fact that naive multivariate substitution can fail, nor for the fact that \(C(U)\) has a Kendall rather than a uniform distribution. The originality claim is restricted to the explicit sharp FGM phase boundary, the independence-block Euler-operator formula in this context, and the quantitative entropy defect.

## Value

**PASS.**

The result converts a qualitative obstruction into a sharp dimension-dependent phase diagram in a canonical copula family. It also separates two logically distinct failures: direct block substitution can cease to be a copula, while entropy additivity already fails by a controlled positive amount in a parameter region where the composite remains a bounded positive copula. The operator identity identifies the exact higher-chain-rule terms responsible for the discrepancy and provides a simple diagnostic for other smooth outer copulas with an independence block.

## Scientific limitations retained

The exact threshold is specialized to FGM with one independence-product block. The general operator criterion assumes smoothness and does not solve arbitrary multiblock substitution. The entropy lower bound is not asserted to be sharp. Older linkage/multivariate-marginal literature remains a residual originality risk.
