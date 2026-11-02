# Two-local automorphism rigidity for every finite-dimensional perfect evolution algebra

## Finding
Let \(K\) be any field and \(E\) any finite-dimensional perfect evolution algebra over \(K\). Every two-local algebra automorphism \(T:E\to E\), **without any prior linearity assumption**, is an ordinary algebra automorphism. The result holds in all characteristics and over finite fields as well as infinite fields.

## Assumptions and scope
An evolution algebra admits a natural basis \(e_1,\ldots,e_n\) with \(e_i e_j=0\) whenever \(i\ne j\). Perfect means \(E^2=E\), equivalent in finite dimension to the linear independence of \(e_1^2,\ldots,e_n^2\). A map \(T:E\to E\) is **two-local automorphic** when, for every ordered pair \(x,y\in E\), there exists a single \(K\)-algebra automorphism \(g_{x,y}\) matching \(T\) simultaneously at both points. Neither additivity, homogeneity, continuity nor bijectivity is assumed of \(T\) a priori. The zero-dimensional case is trivial; the argument below covers every \(n\ge1\).

## Proof
**Step 1 (monomiality of actual automorphisms).** Write an automorphism \(g\) in the natural basis as \(g(e_i)=\sum_k a_{ki}e_k\). For \(i\ne j\),
\[
0=g(e_ie_j)=g(e_i)g(e_j)=\sum_{k=1}^{n}a_{ki}a_{kj}e_k^2.
\]
Perfection makes the \(e_k^2\) linearly independent, hence each row \(k\) of \((a_{ki})\) has at most one nonzero entry. Invertibility forces exactly one nonzero entry in every row and column. Thus \(g(e_i)=c_i e_{\sigma(i)}\), where \(c_i\ne0\) and \(\sigma\) is a permutation.

**Step 2 (two-locality forces global monomial linearity).** For each \(i\), choose an automorphism implementing \(T\) at \(e_i\). By Step 1, \(T(e_i)=c_i e_{\sigma(i)}\). Applying the two-local condition to each pair of distinct natural basis elements proves that the indices \(\sigma(i)\) are distinct, so \(\sigma\in S_n\). Now fix an arbitrary \(x=\sum_i x_i e_i\). For each \(i\), apply two-locality to \((e_i,x)\), obtaining a monomial automorphism \(g_i\) with \(g_i(e_i)=c_i e_{\sigma(i)}\) and \(g_i(x)=T(x)\). The coefficient of \(e_{\sigma(i)}\) in \(g_i(x)\) is necessarily \(c_i x_i\), since no other input basis vector maps into that output coordinate. Consequently,
\[
T(x)=\sum_{i=1}^n c_i x_i e_{\sigma(i)}.
\]
Thus \(T\) equals the invertible monomial linear map \(M\) specified by its basis images.

**Step 3 (product preservation).** For each \(i\), apply two-locality to \((e_i,e_i^2)\). The matching algebra automorphism \(h_i\) gives
\[
M(e_i^2)=T(e_i^2)=h_i(e_i^2)=h_i(e_i)^2=T(e_i)^2=M(e_i)^2.
\]
For distinct indices \(i\ne j\), monomiality yields \(M(e_i)M(e_j)=0=M(e_ie_j)\). Hence \(M\) preserves all basis products, and by \(K\)-bilinearity it preserves products of arbitrary vectors. It is already invertible by Step 2. Therefore \(T=M\in\operatorname{Aut}_K(E)\). \(\square\)

## Verification
The three steps constitute a symbolic proof, with no case split on the field. The accompanying `check.py` separately enumerates all six invertible \(2\times2\) structure matrices over \(\mathbb F_2\), computes their actual automorphism groups, and exhaustively tests **all** \(4^4=256\) set maps on each four-element algebra against the definition of two-local automorphism. It confirms equality of the two-local maps and automorphisms in every case. This finite check corroborates but does not establish the universal theorem.

## Relationship to prior work
The central input that actual automorphisms of perfect evolution algebras are monomial is classical, stated explicitly in Costoya–Mayorga–Viruel (2025, Theorem 2.4 and Corollary 2.5), tracing back to Elduque–Labra. Their paper studies permutation representations, not two-local automorphism rigidity. Mukhamedov–Khakimov–Omirov–Qaralleh (2018/2019) treat local automorphisms and two-local derivations for **nilpotent**, therefore nonperfect, evolution algebras, rather than the present all-perfect two-local automorphism theorem. The 2026 survey by Kaygorodov–Martín González–Viruel motivates renewed study of automorphism/derivation structure in evolution algebras. The novelty claim is restricted to the explicit universal two-local rigidity conclusion; no new monomiality theorem is asserted.

## Limitations
Perfection is essential to Step 1; this proof provides no theorem for nonperfect evolution algebras. The assertion concerns two-local **automorphisms**, not local automorphisms or two-local derivations. Historical priority beyond the inspected literature remains uncertain, especially general two-local results formulated using monomial group actions. No independent external mathematical audit has been performed.

## References
- I. Kaygorodov, C. Martín González and A. Viruel, *Evolution algebras: a survey of results and a list of open problems* (2026), arXiv:2610.22248; first posted 2026-10-15.
- C. Costoya, P. Mayorga and A. Viruel, *Permutation Representations and Automorphisms of Evolution Algebras*, Mediterranean Journal of Mathematics 22 (2025), article 149, DOI:10.1007/s00009-025-02924-0. Particularly Theorem 2.4 and Corollary 2.5.
- F. Mukhamedov, O. Khakimov, B. Omirov and I. Qaralleh, *Derivations and automorphisms of nilpotent evolution algebras with maximal nilindex*, arXiv:1805.10285 (2018); J. Algebra Appl. 18 (2019), article 1950233.
