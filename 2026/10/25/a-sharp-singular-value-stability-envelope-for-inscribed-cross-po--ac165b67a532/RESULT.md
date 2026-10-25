# A sharp singular-value stability envelope for inscribed cross-polytopes

## Finding

For every integer \(d\ge2\), consider a convex \(d\)-polytope \(P\) inscribed in the unit sphere and combinatorially equivalent to a cross-polytope. Label its unique nonadjacent vertex pairs \((p_i^+,p_i^-)\), \(1\le i\le d\). Define the squared labelled distance to the family of regular cross-polytopes by
\[
D(P)=\min_{R\in O(d)}\sum_{i=1}^d\bigl(\|p_i^+-Re_i\|_2^2+\|p_i^-+Re_i\|_2^2\bigr).
\]
Then the following exact finite-deficit inequality holds:
\[
\boxed{\operatorname{vol}_d(P)\le \frac{2^d}{d!}\left(1-\frac{D(P)}{4d}\right)^d.}
\]
Equality occurs precisely when the \(d\) opposite-pair difference vectors are mutually orthogonal and have the same length. The bound is **attainably sharp at every squared distance**
\[
0\le D<4d\left(1-\frac{2}{\sqrt5}\right),
\]
not just asymptotically near a maximizer. Consequently the best possible quadratic stability coefficient at a regular inscribed cross-polytope is exactly \(2^d/(4d!)\):
\[
\frac{2^d}{d!}-\operatorname{vol}_d(P)
\ge \frac{2^d}{d!}\left(\frac{D(P)}4-\frac{d-1}{32d}D(P)^2+O(D(P)^3)\right).
\]
The inequality involving \(O(D^3)\) is a local expansion of the explicit nonnegative lower-bound function, not a uniform third-order bound for arbitrary \(D\).

In dimension four, \(\operatorname{vol}_4(P)\le\frac23(1-D(P)/16)^4\), attained for every \(0\le D(P)<16(1-2/\sqrt5)\). The sharp quadratic coefficient is \(1/6\).

## Assumptions and scope

A cross-polytope here means any convex polytope with the face lattice of \(\operatorname{conv}\{\pm e_1,\ldots,\pm e_d\}\); central symmetry is **not** assumed. Its graph determines the nonadjacent pairing uniquely. All vertex norms equal one. Labels of pairs and signs may be fixed arbitrarily: the distance is invariant under simultaneous permutation and sign changes, since the minimization is over the full orthogonal group. Volume is ordinary Euclidean \(d\)-volume. The bound holds globally within this combinatorial class. The explicit interval is a proved range of sharp attainability; it is not claimed maximal.

## Proof

**Step 1: the diagonal determinant identity.** Set \(C=[p_1^+-p_1^-\ \cdots\ p_d^+-p_d^-]\). The cross-polytope boundary has precisely the facets indexed by signs \(\epsilon\in\{\pm1\}^d\), each choosing \(p_i^{\epsilon_i}\). Orient the ordered facet \((p_1^{\epsilon_1},\ldots,p_d^{\epsilon_d})\) with the factor \(\prod_i\epsilon_i\). This is a coherent orientation of the simplicial boundary: across an adjacent pair of facets, exactly one sign changes, and the induced ridge orientations are opposite. The oriented boundary determinant formula (the standard signed-volume identity) therefore gives
\[
d!\operatorname{vol}_d(P)
=\left|\sum_{\epsilon\in\{\pm1\}^d}
\Bigl(\prod_i\epsilon_i\Bigr)
\det(p_1^{\epsilon_1},\ldots,p_d^{\epsilon_d})\right|
=|\det C|.
\]
The second equality is determinant multilinearity. The signed-volume formula is translation invariant, so the argument does not require the origin to lie inside \(P\).

**Step 2: matching distance and singular values.** If \(s_1,\ldots,s_d>0\) are the singular values of \(C\), orthogonal Procrustes optimization gives
\[
D(P)=4d-2\max_{R\in O(d)}\operatorname{tr}(R^{\mathsf T}C)
=4d-2\sum_{i=1}^d s_i.
\]
In particular \(0\le D(P)<4d\), since \(s_i>0\) and \(\sum_i s_i\le \sum_i\|p_i^+-p_i^-\|_2\le2d\). By the arithmetic-geometric mean inequality,
\[
|\det C|=\prod_i s_i\le\left(\frac1d\sum_i s_i\right)^d
=2^d\left(1-\frac{D(P)}{4d}\right)^d.
\]
Equality holds if and only if all singular values coincide, equivalently \(C=2rR\) for some \(R\in O(d)\) and \(r>0\); geometrically the opposite-pair difference vectors are orthogonal and equally long.

**Step 3: attainability on an explicit interval.** Fix \(2/\sqrt5<r\le1\), set \(t=\sqrt{1-r^2}\), let indices be cyclic, and define
\[
p_i^\pm=\pm r e_i+t e_{i+1},\qquad i=1,\ldots,d,\quad e_{d+1}=e_1.
\]
Each point lies on the unit sphere, and \(C=2rI_d\), so \(D(P)=4d(1-r)\). It remains to verify, rather than assume, that the configuration has the stated combinatorial type. Put \(q=t/r<1/2\). For each sign choice \(\epsilon\), the candidate facet through \(p_i^{\epsilon_i}\) is supported by the unique vector \(n\) satisfying \(r\epsilon_i n_i+t n_{i+1}=1\). Writing \(u_i=r\epsilon_i n_i\), these equations become \(u_i=1-q\epsilon_{i+1}u_{i+1}\). They have a unique solution by contraction in the maximum norm; \(\max_i|u_i|\le1/(1-q)\), hence \(u_i\ge(1-2q)/(1-q)>0\). The opposite point satisfies
\[
\langle n,p_i^{-\epsilon_i}\rangle=1-2u_i<1.
\]
Thus every one-from-each-pair choice is an exposed simplicial facet, and these \(2^d\) facets form the entire cross-polytopal boundary. The origin is interior: coefficients \((1-q)/(2d)\) for all \(p_i^+\), and \((1+q)/(2d)\) for all \(p_i^-\), are positive, sum to one and have barycenter zero. Consequently all these are genuine full-dimensional inscribed cross-polytopes, and they attain equality for every \(D=4d(1-r)\) in the specified interval. The expansion at \(D=0\) follows by binomial expansion. The displayed sharp coefficient cannot be increased because these equality shapes occur with arbitrarily small positive \(D\).

## Verification

The standalone `verify.py` uses exact rational arithmetic on three unit-circle Pythagorean choices \((r,t)=(12/13,5/13),(24/25,7/25),(40/41,9/41)\). For each \(d=2,3,4,5,6\), it checks all \(2^d\) supporting hyperplanes strictly exclude the unselected partners, the chosen facet matrices are nonsingular, strictly positive coefficients give the origin, and the determinant and equality formulas hold. It reports 15 configurations and 372 signed-facet certificates. These finite tests supplement, rather than establish, the unrestricted-dimensional proof.

## Relationship to prior work

Horváth and Lángi (2014), Corollary 3, established that a maximum-volume inscribed cross-polytope must be regular. Medgyes (2026), Theorem 5.1 and its corollary, established optimality and uniqueness of the regular four-dimensional cross-polytope among eight-vertex spherical polytopes, with a strict bound on other simplicial types. Neither of the checked results provides a sharp volume envelope conditioned on labelled squared vertex distance to the orthogonal orbit. The present theorem adds an exact dimension-uniform deficit profile, equality classification and a nontrivial interval of realized sharpness, while relying on standard determinant and singular-value inequalities.

## Limitations

The theorem is restricted to the combinatorial cross-polytope class. The explicit interval of sharpness need not exhaust all attainable distances. In four dimensions, no globally sharp distance-conditioned inequality is asserted for non-cross-polytopal eight-vertex configurations. The originality assessment cannot exclude an unindexed earlier derivation of the same singular-value profile. There has been no independent audit.

## References

1. C. Medgyes, *Inscribed 4-polytopes of maximal volume with seven and eight vertices*, arXiv:2610.26886v1, first public October 12, 2026; see Sections 2.4, 3.1, and 5. https://arxiv.org/abs/2610.26886
2. Á. G. Horváth and Z. Lángi, *Maximum volume polytopes inscribed in the unit sphere*, arXiv:1402.6496v3, first public February 26, 2014; see Corollary 3. https://arxiv.org/abs/1402.6496
