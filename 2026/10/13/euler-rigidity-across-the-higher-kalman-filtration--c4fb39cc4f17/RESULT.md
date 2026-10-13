# Euler rigidity across the higher Kalman filtration
## Finding
Let \(V\cong\mathbb C^n\), and let \(L\subsetneq V\) be a \(d\)-dimensional linear subspace. For
\[
1\le s\le d,
\]
write
\[
\mathcal K_{s,d,n}(L)
=
\left\{
[A]\in\mathbb P\operatorname{End}(V):
\text{there exists }U\subseteq L,\ \dim U=s,\ A(U)\subseteq U
\right\}.
\]
These are the higher Kalman varieties, with
\[
\mathcal K_{d,d,n}(L)\subseteq
\mathcal K_{d-1,d,n}(L)\subseteq\cdots\subseteq
\mathcal K_{1,d,n}(L).
\]

Their ordinary topological Euler characteristics are
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathcal K_{s,d,n}(L)\right)=n^2
\qquad(1\le s<d),
}
\]
and
\[
\boxed{
\chi_{\mathrm{top}}\!\left(\mathcal K_{d,d,n}(L)\right)
=
n^2-d(n-d).
}
\]

Thus every proper nonlinear member of the Kalman singularity filtration has the same Euler characteristic as the ambient projective matrix space:
\[
\chi_{\mathrm{top}}\!\left(\mathbb P\operatorname{End}(V)\right)=n^2.
\]

By additivity, the locally closed layers satisfy
\[
\boxed{
\chi_c\!\left(
\mathcal K_{s,d,n}(L)\setminus\mathcal K_{s+1,d,n}(L)
\right)=0
\qquad(1\le s\le d-2),
}
\]
whereas
\[
\boxed{
\chi_c\!\left(
\mathcal K_{d-1,d,n}(L)\setminus\mathcal K_{d,d,n}(L)
\right)=d(n-d).
}
\]

## Assumptions and scope
The base field is \(\mathbb C\). We assume
\[
1\le d<n.
\]
The varieties are projectivized inside
\[
\mathbb P\operatorname{End}(V)\cong\mathbb P^{n^2-1}.
\]

No normality, Cohen--Macaulayness, smoothness, or genericity assumption is imposed. In fact, the archival literature identifies the successive higher Kalman varieties as the iterated singular loci.

The statement concerns ordinary topological Euler characteristic of the projective varieties and compactly supported Euler characteristic of the open layers. It does not determine Betti numbers or intersection cohomology.

## Proof
Choose coordinates so that
\[
L=\langle e_1,\ldots,e_d\rangle.
\]
Let a one-parameter subgroup act on \(V\) diagonally with integer weights
\[
w_1,\ldots,w_n
\]
chosen so that every difference
\[
w_i-w_j\qquad(i\ne j)
\]
is distinct. Conjugation then gives an algebraic \(\mathbb C^*\)-action on
\[
\mathbb P\operatorname{End}(V)
\]
which preserves every \(\mathcal K_{s,d,n}(L)\).

The fixed locus in the ambient projective space consists of two types.

First, the zero-weight subspace is the diagonal matrix space, so it contributes
\[
\mathbb P^{n-1}.
\]
Every diagonal matrix preserves every coordinate \(s\)-plane in \(L\), hence the whole diagonal projective space lies in every higher Kalman variety.

Second, every off-diagonal weight space is one-dimensional and gives a matrix-unit fixed point
\[
[E_{ij}],\qquad i\ne j,
\]
where \(E_{ij}(e_j)=e_i\).

Fix such a matrix unit. If \(j>d\), then \(E_{ij}\) vanishes on \(L\), so every \(s\)-plane in \(L\) is invariant. If \(j\le d\) and \(s<d\), then
\[
L\cap\ker(E_{ij})
\]
has dimension \(d-1\), so it contains an \(s\)-plane \(U\), and this \(U\) is annihilated by \(E_{ij}\). Therefore every off-diagonal matrix unit belongs to every \(\mathcal K_{s,d,n}(L)\) with \(s<d\).

For \(s=d\), the only possible invariant \(d\)-plane contained in \(L\) is \(L\) itself. The matrix unit \(E_{ij}\) preserves \(L\) unless
\[
j\le d<i.
\]
There are exactly
\[
d(n-d)
\]
excluded matrix units.

Hence, for \(s<d\), the fixed locus has Euler characteristic
\[
\chi_{\mathrm{top}}(\mathbb P^{n-1})+n(n-1)
=
n+n(n-1)
=
n^2.
\]
For \(s=d\), it has Euler characteristic
\[
n+n(n-1)-d(n-d)
=
n^2-d(n-d).
\]

For a complex algebraic variety with an algebraic \(\mathbb C^*\)-action,
\[
\chi_c(X)=\chi_c(X^{\mathbb C^*}).
\]
One proof stratifies the nonfixed locus into constructible pieces admitting a finite quotient by \(\mathbb C^*\); every such piece has compactly supported Euler characteristic zero because
\[
\chi_c(\mathbb C^*)=0.
\]
Since every \(\mathcal K_{s,d,n}(L)\) is projective,
\[
\chi_{\mathrm{top}}=\chi_c,
\]
so the fixed-locus counts prove the two formulas.

Finally, the archival nesting
\[
\mathcal K_{d,d,n}\subseteq\cdots\subseteq\mathcal K_{1,d,n}
\]
and additivity of \(\chi_c\) give the formulas for the locally closed layers.

## Verification
The bundled checker independently enumerates the projective torus-fixed pieces for every
\[
2\le n\le30,\qquad 1\le d<n,\qquad 1\le s\le d.
\]
For each triple it classifies every ordered off-diagonal matrix unit by the invariant-subspace criterion above and verifies
\[
\chi_{\mathrm{fixed}}=
\begin{cases}
n^2,&s<d,\\
n^2-d(n-d),&s=d.
\end{cases}
\]

It also checks that powers-of-two diagonal weights separate all ordered off-diagonal conjugation weights for
\[
2\le n\le20,
\]
and verifies the compactly supported Euler differences between adjacent filtration levels.

These finite calculations are regression evidence only. The all-parameter proof is the fixed-locus argument above.

## Relationship to prior work
Ottaviani and Sturmfels define the higher Kalman varieties as matrices possessing an invariant \(s\)-plane inside a fixed \(d\)-plane. They prove the nested singularity filtration, its codimensions, determinantal equations, desingularizations, and degree formulas. Their full text does not state an Euler-characteristic or Poincaré-polynomial formula for these projective varieties.

Sam studies the same higher Kalman varieties using their normalizations and syzygies. His archival preprint lists MSC \(14M12\) first and supplies an algebraic-geometry source for the family used here. Its full text likewise contains no Euler- or Poincaré-type calculation.

Targeted searches for the aliases “higher Kalman variety,” “Kalman singular strata,” “matrices with invariant subspace in a given subspace,” and combinations with Euler characteristic, topology, Poincaré polynomial, and torus fixed points did not locate the displayed formulas.

The literature does mention homotopy groups of spaces of observable pairs, but those are complements in a different parameter space in which the observation matrix varies. They do not imply the Euler characteristic of a fixed-\(L\) projective Kalman variety or its full higher singularity filtration.

## Limitations
Euler characteristic is a coarse invariant. Equality with the ambient Euler characteristic does not imply equality of homology, motive, Hodge structure, or singularity type.

The proof relies on complex-algebraic \(\mathbb C^*\)-localization; no analogous statement over arbitrary base fields is claimed.

The argument is short after the fixed loci are isolated, so an unindexed or folklore observation remains a residual originality risk.

## References
Steven V. Sam, *Equations and syzygies of some Kalman varieties*, arXiv:1105.5756, first submitted 29 May 2011; *Proceedings of the American Mathematical Society* 140 (2012), 4153--4166, DOI 10.1090/S0002-9939-2012-11593-X.

Giorgio Ottaviani and Bernd Sturmfels, *Matrices with Eigenvectors in a Given Subspace*, arXiv:1012.1016, first submitted 5 December 2010; *Proceedings of the American Mathematical Society* 141 (2013), 1219--1232, DOI 10.1090/S0002-9939-2012-11404-2.
