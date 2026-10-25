# Sharp magic-positivity threshold for complete-bipartite polar edge polytopes

## Finding

Let \(G_m=K_{2,m}\) for an integer \(m\ge1\), and let \(Q_m\) be the polar dual of its symmetric edge polytope, taken in the natural root lattice and its dual. The dimension of \(Q_m\) is \(d=m+1\). Write its Ehrhart polynomial in the magic basis as
\[
L_{Q_m}(n)=\sum_{i=0}^{m+1}\mu_{m,i}n^i(n+1)^{m+1-i}.
\]
**Then \(\mu_{m,i}\ge0\) for every \(i\) if and only if \(1\le m\le8\); in fact all these coefficients are strictly positive for \(m\le8\). Ordinary Ehrhart positivity holds if and only if \(1\le m\le19\).** Thus the whole interval \(9\le m\le19\) has positive monomial coefficients but fails magic positivity. For every \(9\le m\le19\), the middle magic coefficient \(\mu_{m,\lfloor(m+1)/2\rfloor}\) is negative. For every \(m\ge20\), the ordinary Ehrhart coefficient of \(n^{m-19}\) is negative, so magic positivity is impossible.

The exact counting polynomial, for every integer \(n\ge0\), is
\[
\boxed{L_{Q_m}(n)=(2n+1)^m+2\sum_{r=1}^{2n}r^m.}
\]
This classification extends the previously published finite table of magic signs for \(K_{2,m}\) through \(m=11\); it neither claims novelty for those tabulated cases nor asserts non-real-rootedness of the Ehrhart numerator.

## Assumptions and scope

Work in the rank-\((m+1)\) root lattice \(A_{m+1}=\{a\in\mathbb Z^{m+2}:\sum a_j=0\}\). The symmetric edge polytope is \(P_{G_m}=\operatorname{conv}\{\pm(e_u-e_v):uv\in E(G_m)\}\). Its polar \(Q_m=P_{G_m}^{\vee}\) lives in the dual lattice \(\mathbb Z^{m+2}/\mathbb Z\mathbf1\), represented by integer graph potentials after fixing one coordinate to zero. The graph is connected; its edge differences span the root space, so \(Q_m\) is bounded and full-dimensional. Its defining matrix is a graph-incidence matrix, hence totally unimodular; in particular \(Q_m\) is a lattice polytope. The origin lies in its interior, and its polar is integral, so \(Q_m\) is reflexive.

For a rational polynomial of degree \(d\), its magic coefficients are defined by the unique expansion in \(\{n^i(n+1)^{d-i}:0\le i\le d\}\). Magic positivity means all these coefficients are nonnegative. Ordinary Ehrhart positivity requires all monomial coefficients to be positive. Magic positivity implies ordinary positivity, since each magic-basis polynomial has nonnegative monomial coefficients.

## Proof

**1. Lattice-point enumeration.** Label the two vertices on the small side of \(G_m\) by \(u,v\), and the other vertices by \(w_1,\dots,w_m\). Fix the potential at \(u\) to zero and write \(t\) for the potential at \(v\). A point of \(nQ_m\) consists exactly of integer potentials satisfying \(|y_j|\le n\) and \(|t-y_j|\le n\) for every \(j\). Consequently \(-2n\le t\le2n\), and for fixed \(t\) there are \(2n+1-|t|\) independent choices for each \(y_j\). Summing proves the displayed Ehrhart formula, including \(n=0\).

**2. Coefficients.** Define \(B_k=B_k(1)\) by the generating series
\[
\frac{z e^z}{e^z-1}=\sum_{k\ge0}\frac{B_k}{k!}z^k,
\]
so that \(B_1=1/2\). Put \(L_{Q_m}(n)=\sum_{j=0}^{m+1}c_{m,j}n^j\). The Faulhaber identity, or its proof by telescoping the Bernoulli polynomials, gives
\[
\begin{aligned}
c_{m,0}&=1,\\
c_{m,j}&=2^j\binom mj\left(1+\frac{2B_{m+1-j}}{m+1-j}\right)\quad(1\le j\le m),\\
c_{m,m+1}&=\frac{2^{m+2}}{m+1}.
\end{aligned}
\]
The magic transformation gives an entirely explicit rational expression for *every* magic coefficient:
\[
\boxed{\mu_{m,i}=\sum_{j=0}^{i}(-1)^{i-j}\binom{m+1-j}{i-j}c_{m,j}\quad(0\le i\le m+1).}
\]
Indeed, \((1-z)^{m+1}L_{Q_m}(z/(1-z))=\sum_i\mu_{m,i}z^i\).

**3. Finite range.** The exact recurrence
\[
B_0=1,\qquad B_r=1-\frac1{r+1}\sum_{j=0}^{r-1}\binom{r+1}{j}B_j\quad(r\ge1)
\]
computes all required rationals with no approximations. Substitution into the preceding finite sums gives strictly positive magic coefficients for \(m=1,2,\dots,8\). Their respective smallest values are
\[
1,\ 1,\ 1,\ 1,\ 1,\ 1,\ 2/3,\ 2/15.
\]
For the eleven remaining parameters below twenty, the middle coefficients are the following exact negative witnesses:

| \(m\) | \(\mu_{m,\lfloor(m+1)/2\rfloor}\) |
| ---: | ---: |
| 9 | \(-144/5\) |
| 10 | \(-598/11\) |
| 11 | \(-892/3\) |
| 12 | \(-262324/455\) |
| 13 | \(-106896/35\) |
| 14 | \(-31729/5\) |
| 15 | \(-41178\) |
| 16 | \(-4767934/51\) |
| 17 | \(-7027360/9\) |
| 18 | \(-774064682/399\) |
| 19 | \(-2120599388/105\) |

This is an exhaustive finite check of the *parameter interval* \(1\le m\le19\), not a finite experiment extrapolated to infinitely many values. Its exact arithmetic is independently reconstructed in `verify.py` by interpolation from lattice counts.

Every ordinary coefficient is positive for \(m\le19\): in the displayed coefficient formula, the only negative nonzero Bernoulli values of index at most nineteen are \(B_4=-1/30\), \(B_8=-1/30\), \(B_{12}=-691/2730\), and \(B_{16}=-3617/510\), each satisfying \(2|B_k|<k\). All other relevant Bernoulli values are nonnegative, and the leading and constant coefficients are positive.

**4. All higher dimensions.** The known Bernoulli value \(B_{20}=-174611/330\) yields, for every \(m\ge20\),
\[
\boxed{c_{m,m-19}=2^{m-19}\binom{m}{m-19}\left(1-\frac{174611}{3300}\right)<0.}
\]
A nonnegative combination of magic-basis polynomials cannot have a negative monomial coefficient. Therefore none of these infinitely many polars is magic positive. In the first case \(m=20\) (dimension \(21\)), the linear Ehrhart coefficient is exactly \(-342622/165\). Together with Step 3 this proves both claimed sharp positivity thresholds and the gap between them.

## Verification

Run `python3 verify.py` from the directory containing this document. The standard-library checker calculates Bernoulli numbers as reduced rational fractions, forms both coefficient bases exactly, and compares the ordinary coefficients against an **independent Newton interpolation** from exact graph-potential lattice counts for every \(1\le m\le20\). It also enumerates small graph potentials directly, verifies the finite magic-sign cases and the Bernoulli index-twenty value, and checks reflexive symmetry of the magic coefficients. The full infinite-range implication in Step 4 is an algebraic proof, not a computational extrapolation.

## Relationship to prior work

Konoike's work on magic-positive Ehrhart polynomials tabulates the magic signs of these same polar duals for \(K_{2,m}\), \(2\le m\le11\), finding positivity through \(m=8\) and failures at \(m=9,10,11\). Those specific cases were already known; the present mathematical contribution is the **complete all-\(m\) classification** and the explicit structural explanation for the entire infinite tail. The October 2026 study by Ohsugi and Tsuchiya establishes magic positivity for polar duals of pseudo-symmetric simplicial reflexive polytopes and for symmetric-edge polars of cycles; its positive theorem does not cover the present nonpositive infinite family.

Liu and Tsuchiya's 2018 order-polytope result already identifies the Bernoulli-index-twenty sign obstruction for a different polytope family. Specifically, for the star-poset order-polytope enumerator \(F_m(n)=\sum_{r=1}^{n+1}r^m\), the present graph-polar enumerator obeys \(L_{Q_m}(n)=2F_m(2n)-(2n+1)^m\). The Bernoulli obstruction and the resulting negative ordinary coefficients are thus **not claimed as a newly discovered general sign pattern**. The additional magic-basis classification of the reflexive graph polars is the point of the finding. Liu's 2026 work concerns how positivity properties behave under standard operations on lattice polytopes, without this \(K_{2,m}\) classification.

## Limitations

This classification concerns \(K_{2,m}\) only, not general \(K_{a,b}\). It makes no claim that the Ehrhart numerator is or is not real-rooted when magic positivity fails: the converse of the magic-positivity implication does not hold. The universal negative coefficient argument does not identify every negative monomial coefficient for each \(m\). Equivalent computations might exist under a different graph, flow-polytope, order-polytope, or tension-polytope representation; historical priority is not independently certified.

## References

1. H. Ohsugi and A. Tsuchiya, *Magic positivity for polar duals of pseudo-symmetric smooth Fano polytopes*, arXiv:2610.06419 (first public October 5, 2026), especially the introduction and symmetric-edge-polar results.
2. M. Konoike, *A new class of magic positive Ehrhart polynomials of reflexive polytopes*, arXiv:2409.16648; Séminaire Lotharingien de Combinatoire 93B.148 (2025), Section 4 and Example 4.3, including the \(K_{a,b}\) table.
3. F. Liu and A. Tsuchiya, *Stanley's non-Ehrhart-positive order polytopes*, arXiv:1806.08403, Theorems 1.4–1.5.
4. F. Liu, *Ehrhart Properties under Operations on Lattice Polytopes*, arXiv:2610.06338 (first public October 5, 2026), introductory positivity definitions and preservation results.
