# Isolated Segre cones on the Fano toric varieties of even cycle symmetric-edge polytopes

## Finding

For each integer \(n\ge 3\), let \(C_n\) be the simple cycle on \(n\) vertices. In the root lattice
\[
N=\{(a_1,\ldots,a_n)\in\mathbb Z^n:\textstyle\sum_i a_i=0\},
\]
put \(v_i=e_i-e_{i+1}\), with indices taken cyclically, and define the symmetric-edge polytope \(P_n=\operatorname{conv}\{\pm v_i:1\le i\le n\}\). Let \(X_n=X_{\Sigma(P_n)}\) be the normal projective toric Fano variety of the fan of cones over the proper faces of \(P_n\). (This is the **face fan**, not the normal fan of \(P_n\).) Work over any algebraically closed field \(k\).

**Theorem.** If \(n=2r\) with \(r\ge2\), the reduced singular locus of \(X_n\) consists of exactly
\[
\binom{2r}{r}
\]
**isolated torus-fixed points**. At each point, the entire affine toric chart (not merely its tangent cone) is isomorphic to the affine rank-at-most-one determinantal variety
\[
D_r=\operatorname{Spec}\left(k[z_{ij}:1\le i,j\le r]/I_2(z_{ij})\right),
\]
where \(I_2\) is the ideal of all \(2\times2\) minors. In particular, every singular point has local embedding dimension \(r^2\), Hilbert–Samuel multiplicity \(\binom{2r-2}{r-1}\), and local divisor class group \(\mathbb Z\); its completed local ring is normal, Cohen–Macaulay and Gorenstein. The non-\(\mathbb Q\)-factorial locus consists of these same isolated points. All other points are smooth. If \(n\) is odd, \(X_n\) is smooth (a previously known parity criterion, included solely for contrast).

For \(n=4,6,8\), the even-cycle singular point counts are respectively \(6,20,70\), and their multiplicities are respectively \(2,6,20\). Thus the six singularities for \(n=4\) are ordinary threefold conifolds, whereas for \(n=6\) the twenty singularities are rank-one \(3\times3\) determinantal cones.

## Assumptions and scope

The toric lattice is the **root lattice** \(N\), not the ambient \(\mathbb Z^n\) nor the vertex lattice of a normal-fan construction. The edges are oriented only to specify \(v_i\), and the symmetric polytope makes their orientation irrelevant. As \(v_1,\ldots,v_{n-1}\) form a \(\mathbb Z\)-basis and \(v_n=-\sum_{i=1}^{n-1}v_i\), \(\dim X_n=n-1\). The projective fan is complete since \(0\) lies in the interior of \(P_n\). All assertions are characteristic-independent. The claim of new geometric content is the **complete even-cycle singular-support and local determinantal classification**, not the previously published odd/even smoothness dichotomy.

## Proof

**1. All facets and maximal cones.** Fix the basis \(v_1,\ldots,v_{d}\) of \(N\), where \(d=n-1\). In dual coordinates, the polar polytope is
\[
Q_n=P_n^\circ=\{u\in\mathbb R^d:|u_i|\le1\ (1\le i\le d),\ |u_1+\cdots+u_d|\le1\}.
\]
Because at any vertex of \(Q_n\) at least \(d\) independent bounding hyperplanes meet, each vertex has either all \(d\) coordinates in \(\{\pm1\}\), or at least \(d-1\) in \(\{\pm1\}\) and the final coordinate determined by a hyperplane \(\sum u_i=\pm1\). In the latter case that coordinate is an integer of parity opposite to \(d-1\); if it is strictly between \(-1\) and \(1\), it must equal \(0\).

When \(n=2r\) is even, \(d=2r-1\) is odd. The remaining-coordinate candidate above is an odd integer, hence cannot be strictly interior to its interval. Consequently every vertex of \(Q_n\) is a cube corner \(u_i\in\{\pm1\}\) satisfying \(\sum_i u_i=\pm1\). There are
\[
2\binom{2r-1}{r-1}=\binom{2r}{r}
\]
such vertices, which correspond bijectively to facets of \(P_n\) and maximal cones of its face fan.

Choose one such \(u\). For each \(1\le i\le d\), set \(\epsilon_i=u_i\), and set \(\epsilon_n=-\sum_{i=1}^d u_i\). Then \(\epsilon_i\in\{\pm1\}\) for all \(i\), and \(\sum_{i=1}^n\epsilon_i=0\). The facet dual to \(u\) has precisely the \(n\) vertices \(w_i=\epsilon_i v_i\), since \(\langle u,w_i\rangle=1\) for each \(i\). All are distinct and primitive. Its cone \(\sigma_u\) has dimension \(n-1\), with \(n\) rays, so is nonsimplicial. Each maximal cone therefore gives a non-\(\mathbb Q\)-factorial singular torus-fixed point.

**2. Every proper cone is smooth.** The only integral dependence among the \(n\) cycle vectors is \(\sum_{i=1}^n v_i=0\). It has full support; equivalently,
\[
\sum_{i=1}^n\epsilon_i w_i=0.
\]
Deleting any one \(w_i\) leaves a \(\mathbb Z\)-basis of \(N\): the vectors \(v_1,\ldots,v_{n-1}\) are a root-lattice basis, and replacing a deleted \(v_j\) by \(v_n=-\sum_{i<n}v_i\) changes the determinant only by a sign. Every **proper face** of \(\sigma_u\) omits at least one of its rays, so its primitive generators extend to a lattice basis. It is therefore smooth. Every nonmaximal cone belongs to some maximal cone; hence all nonmaximal cones of \(\Sigma(P_n)\) are smooth. Toric orbit–cone smoothness now shows the singular locus is exactly the fixed points of the \(\binom{2r}{r}\) maximal cones. These points are mutually distinct and isolated.

**3. Exact affine charts.** Let \(\sigma_u=\mathbb R_{\ge0}\langle w_1,\ldots,w_n\rangle\). The map \(\pi:\mathbb Z^n\to N\), \(e_i\mapsto w_i\), is surjective, and its kernel is the primitive rank-one lattice generated by \((\epsilon_1,\ldots,\epsilon_n)\). Therefore the dual semigroup is
\[
\sigma_u^\vee\cap M\ \cong\ \bigl\{a\in\mathbb Z_{\ge0}^n:\sum_{\epsilon_i=+1}a_i=\sum_{\epsilon_i=-1}a_i\bigr\}.
\]
There are \(r\) indices of each sign. Each nonnegative balanced vector can be written as a sum of vectors \(e_i+e_j\) with \(\epsilon_i=+1\), \(\epsilon_j=-1\), simply by pairing its positive-side and negative-side occurrences. These \(r^2\) elements generate the semigroup. The corresponding monomial homomorphism is \(z_{ij}\mapsto s_it_j\); its kernel is the ideal generated by the \(2\times2\) minors, since pairings with fixed row and column multisets are related by transposing two paired partners, a single minor move. Consequently the entire affine chart \(U_{\sigma_u}\) is isomorphic to \(D_r\).

For \(r\ge2\), the rank-one matrix cone is singular only at the zero matrix (its nonzero rank-one stratum is smooth); its dimension is \(2r-1\), and its tangent space at zero has dimension \(r^2\). The projectivized cone is the Segre embedding \(\mathbb P^{r-1}\times\mathbb P^{r-1}\) under \(\mathcal O(1,1)\), so the vertex multiplicity equals its degree
\[
\int_{\mathbb P^{r-1}\times\mathbb P^{r-1}}(H_1+H_2)^{2r-2}=\binom{2r-2}{r-1}.
\]
The determinant presentation gives a normal Cohen–Macaulay semigroup ring. Its canonical module is principal since the two Segre factors have equal dimension (or, equivalently, the semigroup's interior lattice points are a translate of the semigroup by the all-ones vector); hence it is Gorenstein. Its local class group is \(\operatorname{Pic}(\mathbb P^{r-1}\times\mathbb P^{r-1})/\mathbb Z[\mathcal O(1,1)]\cong\mathbb Z\) at the cone vertex. This proves all even-cycle assertions.

**4. Odd-cycle contrast.** For odd \(n\), \(d=n-1\) is even. The polar vertices are (i) cube corners with \(\sum_i u_i=0\), and (ii) points with exactly one zero coordinate, all other coordinates \(\pm1\), and \(\sum_i u_i=\pm1\). Type (i) activates exactly \(d\) signed \(v_i\) rays; type (ii) activates \(d-1\) such coordinate rays and the signed \(v_n\) ray, altogether \(d\). Every selected \(d\)-tuple is a signed subset of \(d\) of the \(n\) cycle vectors and hence a lattice basis. The fan is smooth. This recovers the known parity statement, independently of any finite experiment.

## Verification

`check.py` is standalone Python 3 (standard library only). Run `python3 check.py` after extracting this result's embedded file. It enumerates polar vertices by exact integer coordinates, checks facet activity, all relevant maximal minors and balanced primitive relations for \(3\le n\le10\), and checks balanced-semigroup generation to small degree. Its successful output ends in `VERIFY_OK`. The finite checker corroborates examples and integral calculations; the complete infinite result is proved in the preceding four steps, not inferred from that enumeration. The rank-one-minor argument and Segre degree formula are independent symbolic ingredients.

## Relationship to prior work

Matsui–Higashitani–Nagazawa–Ohsugi–Hibi introduced and studied symmetric edge polytopes, including their reflexive structure and Ehrhart invariants [1]. Higashitani's smoothness criterion for symmetric directed graphs [2, Corollary 2.3] **already proves** that a graph without an even cycle gives a smooth Fano polytope and that an even cycle obstructs global smoothness. Ohsugi–Shibata [3] explicitly describe odd-cycle symmetric-edge polytopes as known smooth Fano examples. Those statements are not claimed as discoveries here. The present result adds the exact count of *all* singular points in an even cycle and the explicit isomorphism type, embedding dimension, multiplicity and local class group of *every* such singularity. The comparisons concern toric varieties of the **face fan**; normal-fan toric varieties have a different construction.

## Limitations

No classification for graphs other than simple cycles is asserted. The odd-cycle parity criterion is recalled, not original. The rank-one-chart classification is supported by a complete elementary proof and finite reproducibility checks, but a differently phrased or unindexed published treatment of even-cycle singularities may exist. Independent validation has not been performed. The scientific statements do not depend on any particular finite-field test or on generic characteristic assumptions.

## References

1. T. Matsui, A. Higashitani, Y. Nagazawa, H. Ohsugi, T. Hibi, *Roots of Ehrhart polynomials arising from graphs* (first public 2010-03-29), arXiv:1003.5444, https://arxiv.org/abs/1003.5444.
2. A. Higashitani, *Smooth Fano polytopes arising from finite directed graphs* (first public 2011-03-11), arXiv:1103.2202, particularly Theorem 2.2 and Corollary 2.3, https://arxiv.org/abs/1103.2202.
3. H. Ohsugi, K. Shibata, *Smooth Fano polytopes whose Ehrhart polynomial has a root with large real part* (first public 2011-09-05), arXiv:1109.0791, https://arxiv.org/abs/1109.0791.
