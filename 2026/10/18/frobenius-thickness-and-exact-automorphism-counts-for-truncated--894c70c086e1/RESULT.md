# Frobenius thickness and exact automorphism counts for truncated polynomial rectangles

## Finding
Fix a prime \(p\), a field \(k\) of characteristic \(p\), an integer \(d\geq1\), and ordered positive integers \(a_1\leq\cdots\leq a_d\). Consider the finite local complete-intersection algebra
\[
A=k[x_1,\ldots,x_d]/(x_1^{p^{a_1}},\ldots,x_d^{p^{a_d}}).
\]
Let \(B=\{\nu\in\mathbb Z_{\geq0}^d:0\leq\nu_j<p^{a_j}\}\), \(N=\#B=p^{\sum_i a_i}\), and
\[
S_i=\{\nu\in B:p^{a_i}\nu_j<p^{a_j}\text{ for every }j\},\quad
u_i=\# S_i=\prod_{j:a_j>a_i}p^{a_j-a_i}.
\]
For each exponent value \(e\), put \(m_e=\#\{i:a_i=e\}\), and define
\[
M=\sum_{i=1}^{d}(N-u_i)-\sum_e m_e^2.
\]
Then the **automorphism group scheme**, considered solely as a \(k\)-scheme, has the explicit product decomposition
\[
\operatorname{Aut}_{k\text{-alg}}(A)\simeq
\mathbb A_k^{M}\times\prod_e\operatorname{GL}_{m_e,k}
\times\prod_{i=1}^{d}(\alpha_{p^{a_i}})^{u_i},
\qquad
\alpha_{p^a}:=\operatorname{Spec} k[z]/(z^{p^a}).
\]
**This is a scheme isomorphism, not an assertion about its noncommutative group law.** The reduction is the first two factors, a smooth geometrically connected variety of dimension \(\sum_i(N-u_i)\). The infinitesimal neighborhood has locally free rank \(p^{\sum_i a_i u_i}\) over this reduced variety, and the Zariski tangent dimension at the identity is \(dN\). Thus this automorphism group scheme is nonsmooth for every admissible \(A\), with tangent excess \(\sum_i u_i\).

For any finite field \(k=\mathbb F_q\) with characteristic \(p\), its exact number of rational automorphisms is
\[
\boxed{\#\operatorname{Aut}_{\mathbb F_q\text{-alg}}(A)
=q^M\prod_{e}\prod_{j=0}^{m_e-1}(q^{m_e}-q^j).}
\]
For example, at \(p=2\), \((a_1,a_2)=(1,2)\), one has \(N=8\), \((u_1,u_2)=(2,1)\), \(M=11\); hence the automorphism group has \(2048\) rational points over \(\mathbb F_2\), its reduced variety has dimension \(13\), its identity tangent space has dimension \(16\), and its infinitesimal thickening rank is \(16\).

## Assumptions and scope
Automorphisms mean unital automorphisms of the indicated commutative algebra, functorially over every commutative \(k\)-algebra \(R\). All base fields of characteristic \(p>0\) are included: no perfection or algebraic-closedness assumption. Exponents must be positive integral \(p\)-powers, with repetitions allowed. The group scheme is represented by a finite-type affine scheme, and its scheme isomorphism does not claim a direct-product decomposition of groups. Dimensions and tangent spaces are geometric dimensions over \(k\). The finite-field formula concerns actual \(\mathbb F_q\)-automorphisms, not the cardinality of a nonreduced scheme in a fictitious set-theoretic sense.

## Proof
**1. Functorial coordinates and Frobenius equations.** Every \(R\)-algebra endomorphism of \(A\otimes_kR\) is specified by \(d\) polynomials
\[
f_i=\sum_{\nu\in B}c_{i,\nu}x^\nu,
\quad c_{i,\nu}\in R,
\]
subject to \(f_i^{p^{a_i}}=0\). The characteristic-\(p\) Frobenius identity gives
\[
f_i^{p^{a_i}}=\sum_{\nu\in S_i}c_{i,\nu}^{p^{a_i}}x^{p^{a_i}\nu}.
\]
Distinct surviving multiindices give distinct basis monomials; therefore these equations are equivalent, coefficient by coefficient, to
\[
c_{i,\nu}^{p^{a_i}}=0\qquad(\nu\in S_i).
\]
The number of such equations for generator \(i\) is exactly \(u_i\), by independent coordinate choices with \(\nu_j=0\) when \(a_j\leq a_i\), and \(0\leq\nu_j<p^{a_j-a_i}\) otherwise.

**2. Exact automorphism condition, including nonreduced coefficient rings.** Let \(L=(c_{i,\mathbf e_j})_{i,j}\), the linear coefficient matrix, and \(\Delta=\det L\). On any geometric fiber of \(\operatorname{Spec}R\), each \(f_i\) is nilpotent, so its constant term vanishes and the induced map preserves the unique maximal ideal of the fiber algebra. In that fiber the algebra homomorphism is an automorphism exactly when its map on \(\mathfrak m/\mathfrak m^2\) is invertible, by Nakayama's lemma and finite dimension; this map is \(L\). Thus a homomorphism is an automorphism on each residue-field fiber exactly when \(\Delta\) is a unit in \(R\). Because the associated \(R\)-linear endomorphism acts on the finite free module \(A\otimes_k R\), fiberwise invertibility is equivalent to its determinant being a unit, and its linear inverse is automatically multiplicative. Conversely, any algebra automorphism restricts on each fiber to an automorphism and therefore has \(\Delta\) invertible. Hence the representing coordinate ring is exactly
\[
k[c_{i,\nu}:1\leq i\leq d,\nu\in B,\Delta^{-1}]
/\big(c_{i,\nu}^{p^{a_i}}:\nu\in S_i\big).
\]

**3. Reduced structure and infinitesimal coordinates.** The variables \(c_{i,\nu}\) for \(\nu\in S_i\) are individually nilpotent. Modulo their ideal, the remaining linear entries are zero precisely when \(a_j>a_i\). With the exponents ordered, the reduced matrix \(L\) is block lower triangular, its diagonal blocks having sizes \(m_e\); consequently
\[
\Delta\equiv\prod_e\det L_e\pmod{(c_{i,\nu}:\nu\in S_i)}.
\]
An element is invertible if and only if its reduction modulo a nilpotent ideal is invertible; hence localizing at \(\Delta\) is equivalent to localizing at the product of the block determinants. After separating the \(\sum_i u_i\) truncated variables, the \(\sum_i(N-u_i)\) ordinary polynomial coordinates consist of \(\sum_e m_e^2\) entries in these square diagonal blocks, and \(M\) unrestricted affine entries. This proves the announced scheme decomposition. The nilradical is precisely the truncated-variable ideal, since its quotient is a geometrically reduced affine-times-general-linear coordinate ring. The resulting finite free thickening rank is \(\prod_i(p^{a_i})^{u_i}\).

**4. Tangent space and finite-field points.** All defining relations \(c_{i,\nu}^{p^{a_i}}=0\) have zero differentials in characteristic \(p\), including at the identity; the open determinant condition imposes no linear tangent equations. Thus the tangent dimension is \(dN\), whereas the reduced variety dimension is \(\sum_i(N-u_i)\). Since each \(u_i\geq1\), the group scheme is always nonsmooth. For \(k=\mathbb F_q\), each nilpotent coordinate has the unique field value zero. The \(M\) affine coordinates contribute \(q^M\) points, while the independent diagonal blocks contribute \(\prod_{j=0}^{m_e-1}(q^{m_e}-q^j)\) for each \(e\), proving the finite-field count.

## Verification
The accompanying self-contained `verify.py` independently constructs each finite quotient as a multiplication table and enumerates all candidate images in the indicated small prime fields. It tests the defining nilpotency relations by actual products and checks invertibility by the rank of the full induced linear endomorphism, rather than relying on the displayed coordinate formula. Exhaustive actual counts equal the predicted values for \((p;(a_i))=(2;(1)),(2;(2)),(3;(1)),(2;(1,1)),(2;(1,2))\); the last case has \(2048\) actual automorphisms. It additionally verifies the surviving-monomial count for \((2;(1,1,2))\). Run `python3 verify.py`; expected final output is `VERIFY_OK`. These finite tests are sanity checks, not substitutes for the proof over arbitrary fields and sizes.

## Relationship to prior work
Díaz, Lucchini Arteche and Manzano-Flores's 2026 paper [1] analyzes automorphism groups of general zero-dimensional monomial algebras under its stated **algebraically closed characteristic-zero** assumption. Its reductive factors and unipotent-root constructions are different in scope from an explicit functor-of-points description over arbitrary positive-characteristic rings, including nilpotent coordinates and nonsmooth thickness. The related 2024 monomial-automorphism study [2] likewise assumes characteristic zero; the 2024 reconstruction paper [3] addresses recovering monomial quotients from their automorphism groups rather than counting points or infinitesimal layers of positive-characteristic rectangular quotients. These publications motivate the question, not a claim that the present argument is a characteristic-free consequence of their theorems. Standard finite-field \(\mathrm{GL}\)-cardinality and Frobenius identities are used as established facts.

## Limitations
This theorem concerns the special, but dimension-unbounded, **Frobenius rectangular** monomial ideals; it is not a classification for all monomial ideals. The displayed splitting is not a splitting of the group law. The proof gives no direct presentation of that group law beyond the substitution formula. Finite computations test only the stated small prime-field cases and cannot certify unrestricted theorem instances. Comparison with all past literature is not exhaustive; an equivalent group-scheme formulation under different terminology remains possible. No independent external mathematical audit is claimed.

## References
1. R. Díaz, G. Lucchini Arteche, G. Manzano-Flores, *The structure of automorphism groups of zero-dimensional monomial algebras*, arXiv:2609.13741 (first posted 2026-09-12), https://arxiv.org/abs/2609.13741.
2. R. Díaz, A. Liendo, G. Manzano-Flores, A. Regeta, *The Automorphism groups of zero-dimensional monomial algebras*, arXiv:2408.02197 (first posted 2024-08-05), https://arxiv.org/abs/2408.02197.
3. R. Díaz, G. Lucchini Arteche, *Finite monomial algebras are determined by their automorphism group*, arXiv:2409.15081 (first posted 2024-09-23), https://arxiv.org/abs/2409.15081.
