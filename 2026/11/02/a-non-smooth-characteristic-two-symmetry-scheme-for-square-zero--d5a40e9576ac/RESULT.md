# A non-smooth characteristic-two symmetry scheme for square-zero complete intersections

## Finding
For any field \(k\) and integer \(d\ge 2\), set
\[
A_d(k)=k[x_1,\ldots,x_d]/(x_1^2,\ldots,x_d^2),\qquad \mathfrak m=(x_1,\ldots,x_d).
\]
Let \(G_d=\operatorname{Aut}_k(A_d)\) be the affine automorphism group scheme of the underlying **ungraded unital** algebra. The following characteristic boundary holds.

**Characteristic two.** As a scheme (not as a direct product of group schemes),
\[
G_d\simeq (\alpha_2)^d\times\operatorname{GL}_d\times\mathbb A^{d(2^d-d-1)},
\qquad \alpha_2=\operatorname{Spec}k[u]/(u^2).
\]
Thus its geometric reduction is smooth, connected, rational, and has dimension \(d(2^d-1)\), but \(G_d\) itself is not smooth: its tangent space at the identity has dimension \(d2^d\), an excess of exactly \(d\). Its ordinary field-valued automorphisms are precisely the substitutions
\[
x_i\mapsto \sum_{j=1}^{d}L_{ji}x_j+h_i,
\quad L\in \operatorname{GL}_d(k),\quad h_i\in\mathfrak m^2.
\]

**Characteristic different from two.** Every field-valued automorphism has exactly one description
\[
x_i\mapsto x_{\sigma(i)}u_i,
\qquad \sigma\in S_d,
\quad u_i\in\left(k[x_j:j\ne\sigma(i)]/(x_j^2:j\ne\sigma(i))\right)^\times.
\]
Its automorphism group scheme is smooth, and its geometric underlying variety consists of \(d!\) connected components, each isomorphic to
\[
(\mathbb G_m)^d\times\mathbb A^{d(2^{d-1}-1)}.
\]
Each component has dimension \(d2^{d-1}\), equal to its identity tangent dimension.

Consequently, for every finite field \(\mathbb F_q\),
\[
\#\operatorname{Aut}_{\mathbb F_q}(A_d)=
\begin{cases}
\displaystyle |\operatorname{GL}_d(\mathbb F_q)|q^{d(2^d-d-1)},&q\text{ even},\\[2pt]
\displaystyle d!(q-1)^d q^{d(2^{d-1}-1)},&q\text{ odd},
\end{cases}
\]
where \(|\operatorname{GL}_d(\mathbb F_q)|=\prod_{j=0}^{d-1}(q^d-q^j)\).

## Assumptions and scope
The algebra is the **commutative** square-zero-variable complete intersection, not the radical-square-zero algebra obtained by also imposing \(x_ix_j=0\) for distinct indices. The full ungraded automorphism functor, including nonreduced test-algebra points, is used in the characteristic-two scheme statement. Other statements about points hold over arbitrary fields; geometric component assertions mean after algebraic closure. The equality for field-valued maps does not by itself imply scheme smoothness; the tangent comparison is separate. No group-scheme product decomposition is asserted.

## Proof
The squarefree monomials \(x_S=\prod_{i\in S}x_i\), for \(S\subseteq\{1,\ldots,d\}\), are a basis. Thus \(\dim_k A_d=2^d\), the algebra is local, \(\mathfrak m/\mathfrak m^2\) has dimension \(d\), and every endomorphism inducing an invertible linear map on this cotangent space is an automorphism (successive powers of the nilpotent maximal ideal and Nakayama, or an explicit filtered inverse).

**Characteristic two: the whole scheme.** For every commutative \(k\)-algebra \(R\), a unital \(R\)-algebra map \(A_d\otimes_kR\to A_d\otimes_kR\) is specified by images
\[
f_i=a_i+\sum_jL_{ji}x_j+\sum_{|S|\ge2}c_{Si}x_S.
\]
In characteristic two the square of every positive-degree squarefree monomial is zero, and the Frobenius square is additive, even with nonreduced coefficients. Hence \(f_i^2=a_i^2\), and the defining relations are **exactly** \(a_i^2=0\), with no other polynomial equations on the displayed coefficients. The ideal \((a_1,\ldots,a_d)\) in the universal coefficient ring is nilpotent (every square vanishes). Modulo it, the substitution respects \(\mathfrak m\) and is invertible exactly when \(\det L\) is a unit, by the cotangent criterion. A map of finite free modules is invertible across a nilpotent ideal if and only if its reduction is invertible; therefore the same condition \(\det L\in R^\times\) characterizes the original substitution. This proves the claimed scheme coordinate description.

Setting every \(a_i=0\) gives the reduction \(\operatorname{GL}_d\times\mathbb A^{d(2^d-d-1)}\) as a variety; it is connected and rational of dimension \(d^2+d(2^d-d-1)=d(2^d-1)\). Differentiation of \(a_i^2=0\) imposes no linear constraint in characteristic two. Hence the tangent dimension is \(d2^d\), larger by \(d\), and the scheme is not smooth. Equivalently, infinitesimal translations \(x_i\mapsto x_i+\varepsilon b_i\) over \(k[\varepsilon]/(\varepsilon^2)\) account for the extra tangent directions.

**Characteristic not two: all field-valued maps.** For a field-valued automorphism, its generator images \(f_i\) lie in \(\mathfrak m\) and obey \(f_i^2=0\). Write the linear form of \(f_i\) as \(\sum_jL_{ji}x_j\). Comparing coefficients of the distinct quadratic monomials \(x_rx_s\), with \(r<s\), gives \(2L_{ri}L_{si}=0\). Therefore each column of the invertible matrix \(L\) contains exactly one nonzero entry and the supports of distinct columns are disjoint. There is a unique \(\sigma\in S_d\) for which its column \(i\) is supported on row \(\sigma(i)\).

Fix a generator with principal variable \(x=x_{\sigma(i)}\), and put \(B=k[x_j:j\ne\sigma(i)]/(x_j^2:j\ne\sigma(i))\). There is a direct vector-space decomposition \(A_d=B\oplus xB\). Write \(f_i=xu+v\) with \(u,v\in B\), where \(u\) is a unit because the coefficient of \(x\) is nonzero. Its square is \(v^2+2xuv\). The direct decomposition and invertibility of \(2u\) imply \(v=0\). Thus \(f_i=xu\), and \(u\) is uniquely determined and is an arbitrary unit of \(B\). Conversely, these substitutions preserve all square relations and induce an invertible monomial cotangent map, so they are all automorphisms. Units of \(B\) have one nonzero constant coefficient and \(2^{d-1}-1\) arbitrary remaining coefficients. Hence each permutation component has the displayed variety, dimension, and finite-field count.

For smoothness in characteristic different from two, the identity tangent space of \(G_d\) is \(\operatorname{Der}_k(A_d)\). A derivation is determined by arbitrary \(g_i=D(x_i)\) subject to \(0=D(x_i^2)=2x_i g_i\). As \(2\) is invertible, \(g_i\in\operatorname{Ann}(x_i)=(x_i)\), a vector space of dimension \(2^{d-1}\). Thus \(\dim\operatorname{Lie}(G_d)=d2^{d-1}\), the geometric dimension of every component. The finite-type group scheme becomes regular at its identity over an algebraic closure, so it is smooth there and hence smooth everywhere by group translations. The same derivation calculation in characteristic two gives dimension \(d2^d\), as above. Multiplying the independent coefficient counts and the \(d!\) permutation choices proves the finite-field formulas.

## Verification
The standalone `verify.py` uses explicit squarefree-monomial multiplication and finite-field arithmetic, including the nonprime field \(\mathbb F_4\). For each tested \((d,q)\), it enumerates **all** generator images satisfying \(f^2=0\), organizes them by cotangent linear form, tests invertibility by Gaussian elimination, sums all possible automorphism tuples, and compares with the theorem. Independently it calculates the tangent derivation dimension by linear equations derived from \(D(x_i^2)=0\). The complete configurations are \((d,q)=(2,2),(2,3),(2,4),(2,5),(3,2),(3,3)\). The resulting automorphism counts are respectively \(24,72,2880,800,688128,944784\). The corresponding tangent dimensions are \(8,4,8,4,24,12\). The final verification marker is `SQUARE_ZERO_COMPLETE_INTERSECTION_AUT_OK`. These computations are finite tests; the general proof is symbolic and holds for all stated \(d\) and fields.

## Relationship to prior work
Angeltveit, Gerhardt, Hill and Lindenstrauss (arXiv:1206.0247, originally posted 2012-06-01) study several-variable truncated polynomial complete intersections in algebraic \(K\)-theory; their theorems do not describe full automorphism schemes. Deo and Maitra (1997) study **graded** automorphisms of truncated polynomial algebras over characteristic-zero fields; imposing degree preservation is a different problem from the full ungraded automorphism functor here. Díaz, Liendo, Manzano-Flores and Regeta (arXiv:2408.02197) determine general automorphism groups of zero-dimensional monomial algebras under a characteristic-zero assumption. Their Theorem 4.21 and Example 4.24 already cover important characteristic-zero structural consequences for the algebra with two generators. No novelty is asserted for the characteristic-zero consequences implied by that theory.

The main contribution assessed here is the characteristic-two **nonreduced automorphism scheme**, its exact infinitesimal excess in arbitrary embedding dimension, the associated jump from monomial linear parts to full general linear groups, and the unified field-unrestricted finite-field formula. A published description of automorphisms of truncated *coordinate-cross* algebras concerns the distinct quotient in which cross products of distinct variables vanish, and does not cover the present family. Classical descriptions of modular elementary-abelian group algebras may still implicitly contain the characteristic-two point-count portion; the scheme-theoretic assertion is kept separate from that possible overlap.

## Limitations
These are automorphisms of labelled algebras, not isomorphism classes of all finite-dimensional complete intersections. The coordinate-chart description of the characteristic-two automorphism scheme is a **scheme** isomorphism, not an isomorphism of product group structures. The characteristic-zero automorphism structure is substantially covered by the general monomial-algebra literature, and no priority claim is made for that slice. Finite searches cannot establish historical uniqueness; implicit coverage in the theory of modular group algebras or automorphism group schemes remains a residual novelty risk. No independent audit has been performed.

## References
1. V. Angeltveit, T. Gerhardt, M. A. Hill, A. Lindenstrauss, *On the algebraic K-theory of truncated polynomial algebras in several variables*, arXiv:1206.0247v1 (2012-06-01), especially introduction and statements of Theorems 1.2–1.4.
2. S. Deo, J. K. Maitra, *Automorphism groups of truncated polynomial algebras*, National Academy Science Letters 20 (1997), nos. 5–6, pp. 74–80; accessible scanned paper at `https://www.researchgate.net/publication/266354814_Automorphism_groups_of_truncated_polynomial_algebras`.
3. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197, Theorem 4.21 and Example 4.24 (the characteristic-zero general theory).
4. *Automorphisms of truncated coordinate-cross algebras over arbitrary fields*, published mathematical record, `https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-automorphisms-of-truncated-coordinate-cross-algebras-over-arbitr--625ba30274cb` (a different monomial quotient).
