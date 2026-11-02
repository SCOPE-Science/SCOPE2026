# Commuting-tuple varieties of rectangular-band semigroup algebras

## Finding

Let \(a,b\ge 2\), let \(k\) be a field, and let \(A_{a,b}(k)=k[S_{a,b}]\) be the semigroup algebra of the rectangular band with basis \(e_{ij}\), \(1\le i\le a\), \(1\le j\le b\), and multiplication \(e_{ij}e_{h\ell}=e_{i\ell}\). Put \(d=(a-1)(b-1)\). For each integer \(m\ge0\), the number of ordered, pairwise-commuting \(m\)-tuples over \(\mathbb F_q\), with one empty tuple at \(m=0\), is

\[
C_{a,b}(m;q)=q^{dm}\left[q^{m(a-1)}+q^{m(b-1)}-1+\frac{q^{a+b-1}-q^{a-1}-q^{b-1}+1}{q-1}(q^m-1)\right].
\]

For \(m\ge2\), the reduced commuting-tuple variety over every algebraically closed field has exactly \(1+\mathbf 1_{a\ge3}+\mathbf 1_{b\ge3}\) irreducible components, all descending to the coefficient field. One is a rank-at-most-one determinantal variety times an affine \(dm\)-space, of dimension \(dm+a+b+m-2\). If \(a\ge3\), a second component is a linear space of dimension \(dm+m(a-1)\); if \(b\ge3\), a third is a linear space of dimension \(dm+m(b-1)\). In particular, the transition from one to two or three components occurs sharply when either side of the band reaches size three.

The tuple-length-two specialization and the individual-element centralizer sizes are already available from an earlier commutator-rank census of this family; neither is claimed as a new contribution. The new content is the higher-arity formula together with the complete reduced component decomposition and its sharp thresholds.

## Assumptions and scope

All fields are allowed for the geometric assertion, including fields of characteristic two. For the point count, \(q\) ranges over all prime powers and \(m\) over all nonnegative integers. No unit is adjoined to the semigroup algebra. The geometric claim is about the underlying **reduced** affine commuting variety, not about the scheme cut out with its potentially nonreduced structure. A component stated to descend to the ground field is defined by equations with coefficients in that field.

For \(x=\sum_{ij}x_{ij}e_{ij}\), define its row-sum vector \(r(x)\in k^a\) and column-sum vector \(c(x)\in k^b\) by \(r_i(x)=\sum_jx_{ij}\) and \(c_j(x)=\sum_ix_{ij}\). Let

\[
W=\{(u,v)\in k^a\oplus k^b:\sum_i u_i=\sum_j v_j\},\quad
\Phi(x)=(r(x),c(x)).
\]

Thus \(\dim W=a+b-1\) and \(\dim\ker\Phi=d\). The notation \(m\) always refers to tuple length, never to a band-side size.

## Proof

**1. Exact multiplication and the margin quotient.** By bilinearity of the band multiplication,

\[
(xy)_{i\ell}=\left(\sum_jx_{ij}\right)\left(\sum_hy_{h\ell}\right)=r_i(x)c_\ell(y).
\]

Hence \(xy=yx\) if and only if \(r(x)c(y)^{\mathsf T}=r(y)c(x)^{\mathsf T}\). The map \(\Phi\) is surjective: for prescribed margins \((u,v)\in W\), take \(x_{i1}=u_i\) for \(i\ge2\), \(x_{1j}=v_j\) for \(j\ge2\), \(x_{11}=u_1-\sum_{j\ge2}v_j\), and all other entries zero. Its kernel has dimension \(ab-(a+b-1)=d\), and any linear splitting identifies the space of all tuples with \(W^m\times k^{dm}\). Commutativity depends only on the \(W^m\) coordinate.

**2. Three closed families, without omitted boundary cases.** Write each margin pair as \(w_s=(u_s,v_s)\in W\). If all \(u_s\) vanish, the tuple commutes; likewise if all \(v_s\) vanish. Otherwise, if a commuting tuple has both some nonzero \(u_i\) and some nonzero \(v_j\), then the equality \(u_i v_j^{\mathsf T}=u_j v_i^{\mathsf T}\) forces at least one \(w_s\) to have both coordinates nonzero. Fix such an \(s\). For each \(t\), equality of the rank-one outer products \(u_s v_t^{\mathsf T}=u_t v_s^{\mathsf T}\) forces \((u_t,v_t)=\lambda_t(u_s,v_s)\) for a unique scalar \(\lambda_t\). This also handles \(w_t=0\). Thus the commuting locus in \(W^m\) is exactly

\[
\mathcal R_m\ \cup\ \mathcal U_m\ \cup\ \mathcal V_m,
\]

where \(\mathcal R_m\) is the determinantal locus of rank-at-most-one \(m\times(a+b-1)\) matrices (the rows are the \(w_s\)), \(\mathcal U_m=\{u_1=\cdots=u_m=0\}\), and \(\mathcal V_m=\{v_1=\cdots=v_m=0\}\). This is a set-theoretic equality over every field, including every algebraic closure.

**3. Irreducible components.** The rank-one determinantal locus is irreducible: its nonzero matrices are scalar products of a column and row, and its closure also contains zero. It has dimension \(m+(a+b-1)-1=a+b+m-2\). The two linear loci have respective dimensions \(m(b-1)\) and \(m(a-1)\). For \(m\ge2\), \(\mathcal U_m\subseteq\mathcal R_m\) precisely when \(b=2\), since then \(\mathcal U_m\) corresponds to matrices with one available independent column; when \(b\ge3\), two independent elements of \(\ker(\sum:k^b\to k)\) supply a tuple in \(\mathcal U_m\setminus\mathcal R_m\). Symmetrically, \(\mathcal V_m\subseteq\mathcal R_m\) precisely when \(a=2\). The determinantal locus contains points with both nonzero margin coordinates, so it is contained in neither linear locus. The two linear loci are not contained in one another. Therefore the components and dimensions are exactly as claimed. Taking their product with the affine kernel space adds \(dm\) to each dimension.

**4. Finite-field enumeration.** In \(W(\mathbb F_q)\), the number of vectors with both margins nonzero is

\[
N=q^{a+b-1}-q^{a-1}-q^{b-1}+1.
\]

Indeed, the zero-first-margin locus has \(q^{b-1}\) points, the zero-second-margin locus has \(q^{a-1}\), and their intersection is the origin. There are exactly \(N/(q-1)\) one-dimensional lines containing a vector with both margins nonzero. Each such line contributes \(q^m-1\) nonzero ordered tuples; lines do not overlap away from zero. Tuples with all first margins zero contribute \(q^{m(b-1)}\); tuples with all second margins zero contribute \(q^{m(a-1)}\); these two counts share exactly the zero tuple. These three disjoint cases yield the bracketed formula. Each tuple has \(q^{dm}\) lifts through \(\Phi^m\). When \(m=0\), the bracket is one, as required.

**5. Previously known centralizer check.** Set \(d=(a-1)(b-1)\). For an element with margin pair \((u,v)\), the vector-space dimension of its element centralizer is exactly

\[
\begin{array}{c|c|c}
(u,v)&\dim C_{A_{a,b}}(x)&\#\{x\text{ of this type over }\mathbb F_q\}\\\hline
(0,0)&ab&q^d\\
u=0,\ v\ne0&d+b-1&q^d(q^{b-1}-1)\\
u\ne0,\ v=0&d+a-1&q^d(q^{a-1}-1)\\
u\ne0,\ v\ne0&d+1&q^d N
\end{array}
\]

Here distinct rows of the table may yield the same numerical dimension. The first case is central because both products vanish. In the second case, a commuting element must have first margin zero; the third case is symmetric; and in the fourth case the margin pair must lie on the one-dimensional span of \((u,v)\). Add the free \(d\)-dimensional kernel in each case. This recovers the known centralizer spectrum and provides a consistency check on the previously established pair case. It is not part of the novelty claim.

## Verification

The accompanying `checker.py` constructs the full semigroup-algebra multiplication from the original basis products, not from the margin quotient. It enumerates all commuting pairs and selected commuting triples, checks the four centralizer-size cases element by element, and verifies the three-set decomposition for every enumerated commuting pair. Arithmetic includes prime fields and \(\mathbb F_4\) represented as \(\mathbb F_2[z]/(z^2+z+1)\). The script runs with Python 3 and no external packages:

`python checker.py`

The recorded run passed all 11 configurations. Among the directly obtained counts are \(C_{2,2}(2;2)=88\), \(C_{2,3}(3;2)=9472\), \(C_{3,3}(2;2)=27136\), and \(C_{2,2}(2;4)=5056\). Enumeration is finite corroboration, not a proof of the arbitrary-parameter statements.

## Relationship to prior work

The rectangular-band product and the concept of a semigroup algebra are classical. A prior commutator-rank census of this same rectangular-band algebra already derives the exact ordered commuting-*pair* count and the centralizer-size classification. Those results are expressly treated as existing coverage, and the claim here is restricted to all-arity enumeration beyond pairs and to the newly established component decomposition. Guo, Rosenkranz and Zheng, arXiv:1402.3702 (first submitted 2014-02-15), study Rota–Baxter operators on two- and three-element semigroup algebras; their Section 2 gives multiplication-table methods, not the present commuting-tuple arithmetic or component geometry. Nagy and Zubor, arXiv:1511.08671 (2015-11-27), study ideal congruences in semigroup algebras of rectangular bands, including a detailed treatment of the two-by-two band; their Theorem 2 addresses congruence permutability, not ordered commuting tuples. General determinantal geometry provides the standard irreducibility of \(\mathcal R_m\); the novelty claim concerns its exact placement alongside the two linear branches in this algebra and the resulting complete all-arity count. An analogous count for a different associative algebra does not imply this formula without an algebra isomorphism or the margin reduction.

## Limitations

The classification applies to rectangular bands, not arbitrary bands or finite semigroups. It gives the **reduced** component decomposition and rational-point counts, not nilpotent thickenings, automorphism-orbit counts or a complete description of component intersections as schemes. The existing literature may contain an equivalent formulation under another name; a database search is not a proof of publication priority. The computation checks finitely many parameters only. Independent validation has not been performed.

## References

1. L. Guo, M. Rosenkranz, S. Zheng, *Classification of Rota-Baxter operators on semigroup algebras of order two and three*, arXiv:1402.3702, originally submitted 2014-02-15. https://arxiv.org/abs/1402.3702
2. A. Nagy, M. Zubor, *A Note on Semigroup Algebras of Permutable Semigroups*, arXiv:1511.08671, originally submitted 2015-11-27. https://arxiv.org/abs/1511.08671
3. J. R. Britnell, M. Wildon, *On types and classes of commuting matrices over finite fields*, Journal of the London Mathematical Society 83 (2011), 470–492, DOI 10.1112/jlms/jdq088. This concerns full matrix similarity classes rather than the semigroup algebras treated here.
