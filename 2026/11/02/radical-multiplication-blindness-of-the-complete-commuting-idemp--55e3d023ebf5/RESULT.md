# Radical-multiplication blindness of the complete commuting-idempotent clique polynomial

## Finding
Let \(K=\mathbb F_q\) be any finite field, and let \(A\) be any finite-dimensional unital *split basic* associative \(K\)-algebra. Write \(J=\operatorname{rad}A\), assume \(A/J\simeq K^n\), and choose pairwise orthogonal primitive idempotents \(e_1,\ldots,e_n\) with sum \(1\). Set
\[
 d_{ij}=\dim_K(e_iJe_j),\qquad w_{ij}=d_{ij}+d_{ji}\quad(1\le i<j\le n).
\]
For each integer \(k\ge0\), let \(T_k(A)\) denote the number of ordered pairwise commuting \(k\)-tuples of idempotents of \(A\), permitting repetitions and taking \(T_0(A)=1\). Then
\[
\boxed{T_k(A)=\sum_{c:[n]\to\{0,1\}^k}q^{D(c)},\quad D(c)=\sum_{1\le i<j\le n}w_{ij}\,\mathbf1_{c(i)\ne c(j)}.}
\]
For each finite set of distinct idempotents, make it a clique when its members commute pairwise. If \(C_A(z)=\sum_{r\ge0}c_r(A)z^r\) is the ordinary clique polynomial (including the empty clique), then
\[
 c_r(A)=\frac{1}{r!}\sum_{j=0}^{r}s(r,j)T_j(A),
\]
where \(s(r,j)\) is the signed Stirling number of the first kind. In particular, **the complete clique polynomial is insensitive to radical multiplication and to the separate orientations \(d_{ij},d_{ji}\)**; only the symmetric off-diagonal dimensions \(w_{ij}\) enter. There are precisely
\[
\boxed{q^{\sum_{i<j}w_{ij}}}\qquad\text{maximal cliques, each of size}\qquad\boxed{2^n}.
\]

This insensitivity is genuine, not just formal. Let \(A_1=KQ_1\) for the path \(Q_1:1\to2\to3\), and let \(A_2=KQ_2/(\operatorname{rad}KQ_2)^2\) where \(Q_2\) has three arrows \(1\to2\), \(2\to3\), and \(1\to3\). Both algebras are six-dimensional and have \(w_{12}=w_{23}=w_{13}=1\), so for \(m=2^k\),
\[
 T_k(A_1)=T_k(A_2)=m+3m(m-1)q^2+m(m-1)(m-2)q^3,
\]
and their **complete** clique polynomials coincide:
\[
\boxed{C_{A_1}(z)=C_{A_2}(z)=q^3(1+z)^8+3q^2(1-q)(1+z)^4+(1-3q^2+2q^3)(1+z)^2.}
\]
Nevertheless \(\operatorname{rad}(A_1)^2\ne0\) while \(\operatorname{rad}(A_2)^2=0\). Therefore these nonisomorphic algebras cannot be distinguished by any commuting-idempotent clique count.

## Assumptions and scope
All algebras are associative, finite-dimensional, unital, and split basic over \(K=\mathbb F_q\), where \(q\) is any prime power; no assumption on characteristic, quiver acyclicity, or radical nilpotence *index* beyond finite-dimensionality is needed. The radical \(J\) is nilpotent. The graph includes **all** idempotents, including \(0\) and \(1\), and its edges join distinct commuting idempotents. The formula counts tuples with repeated entries; the clique polynomial counts subsets with no repetitions. Primitive idempotents are chosen modulo the ordered distinct simple factors of \(A/J\); permuting them does not change the invariant. We do not assert graph isomorphism for the two example algebras, only identical clique polynomials and maximal-clique data.

## Proof
**Step 1 (simultaneous Boolean decomposition).** Given commuting idempotents \(f_1,\ldots,f_k\), write their images in \(A/J\simeq K^n\) as binary labels \(c(i)=(c_1(i),\ldots,c_k(i))\in\{0,1\}^k\). For each binary word \(a\in\{0,1\}^k\), put
\[
 p_a=\prod_{\ell=1}^k \bigl(a_\ell f_\ell+(1-a_\ell)(1-f_\ell)\bigr),\quad E_a=\sum_{i:c(i)=a}e_i.
\]
(The displayed product uses integers \(0,1\) as scalars.) The \(p_a\) are mutually orthogonal idempotents summing to \(1\); their residue classes equal those of \(E_a\). Consequently
\[
 u=\sum_a p_aE_a\in1+J
\]
is a unit. Orthogonality gives \(p_a u=uE_a\), whence \(p_a=uE_a u^{-1}\) and \(f_\ell=u(\sum_{i:c_\ell(i)=1}e_i)u^{-1}\). Conversely, any such conjugates are commuting idempotents. Thus for each fixed color function \(c\), the conjugation action of \(U=1+J\) is transitive on all corresponding tuples.

**Step 2 (orbit-stabilizer count).** A unit \(1+x\) with \(x\in J\) fixes the standard tuple precisely when it commutes with all \(\sum_{i:c_\ell(i)=1}e_i\), or equivalently all \(E_a\). Decomposing \(x=\sum_{i,j}e_i x e_j\) proves that the stabilizing radical subspace is exactly
\[
 J_c=\bigoplus_{i,j:c(i)=c(j)}e_iJe_j.
\]
The group \(U\) has \(q^{\dim J}\) elements, and its stabilizer \(1+J_c\) has \(q^{\dim J_c}\) elements. Therefore the number of tuples with color function \(c\) is \(q^{\dim J-\dim J_c}=q^{D(c)}\). Summing over all colorings proves the boxed tuple formula, including \(k=0\).

**Step 3 (clique inversion).** For each \(k\), an ordered commuting tuple has a distinct-value support which is a clique. If its support has size \(r\), the number of surjections from the \(k\) ordered positions onto that fixed support is \(r!S(k,r)\), with \(S\) a Stirling number of the second kind. Hence \(T_k=\sum_{r\le k}r!S(k,r)c_r\). Inverting this triangular transform gives \(c_r=(1/r!)\sum_{j\le r}s(r,j)T_j\). The graph has only finitely many vertices, so the whole clique polynomial follows.

**Step 4 (all maximal cliques).** By Step 1 any commuting set lies in a conjugate of the Boolean family \(\{\sum_{i\in I}e_i:I\subseteq[n]\}\), and every such family has \(2^n\) distinct members. It is maximal because an idempotent commuting with all its members must lie in \(\bigoplus_i e_iAe_i\); each corner \(e_iAe_i\) is local and has only idempotents \(0,e_i\), so there are no additional idempotents in this commutant. Distinct full Boolean families are the orbit of this standard family under \(1+J\); since every member is fixed by the stabilizer, the stabilizer of the family has precisely the block-diagonal radical \(\bigoplus_i e_iJe_i\), and the count is \(q^{\sum_{i\ne j}d_{ij}}=q^{\sum_{i<j}w_{ij}}\).

**Step 5 (nonisomorphic witnesses).** The three nontrivial off-diagonal Peirce spaces in each example have dimension one and the diagonal radical spaces vanish. The color sum with \(m=2^k\) counts assignments of three positions to colors: all equal (\(m\) choices, weight \(1\)); exactly two equal (\(3m(m-1)\) choices, weight \(q^2\)); all distinct (\(m(m-1)(m-2)\) choices, weight \(q^3\)). Expanding this as a combination of \(2^k,4^k,8^k\) and applying Step 3 yields the displayed clique polynomial. The path algebra contains the nonzero length-two path and has \(J^2\ne0\), while the bound quiver explicitly kills all length-two paths and has \(J^2=0\), proving nonisomorphism.

## Verification
The standalone \(\texttt{verify.py}\) enumerates the two six-dimensional algebras directly, constructs products from their basis multiplication tables, tests every idempotent, independently tests every commuting pair and triple, and enumerates maximal cliques by a graph backtracking routine. For \(q=2\), both algebras give \(T_0,T_1,T_2,T_3=(1,26,340,3368)\) and exactly eight maximal cliques, all of size eight. For \(q=3\), they give \((1,56,976,10592)\) and exactly 27 maximal cliques, all of size eight. The checker returned \(\texttt{VERIFY_OK}\). These checks cover finite fields of orders two and three only and are not relied upon as a proof for arbitrary \(q,n,k\); the argument above supplies that proof.

## Relationship to prior work
Classical results on lifting idempotents modulo nilpotent radicals and conjugation by radical units underlie Steps 1–2. André–Dias (2019) supplies split-basic-algebra and radical-unit context; its main subject is representation theory of unit groups. Dolžan (2021) studies bounds and reductions for numbers of idempotents in finite rings, not a complete all-arity clique distribution. Wright (2020) classifies/counts *individual* triangular idempotent matrices; its full text was not accessible for inspection here, so no unqualified noncoverage claim is made about its entire contents. Closely related specialized upper-triangular and incidence-algebra tuple counts exist and are not claimed here as new. The present statement concerns **every finite-dimensional split basic algebra**, identifies exactly the symmetric radical Peirce data controlling all tuple/clique counts, and exhibits relation-distinct algebras with the same invariant. No exhaustive publication-priority claim is made.

## Limitations
The algebra is required to be split basic; no formula is asserted for nonsplit simples or matrix simple factors. The clique polynomial is not the full graph isomorphism type. The argument proves relation-insensitivity within this class but does not classify which different symmetric dimension matrices yield equal clique polynomials. Historical priority beyond the inspected primary sources and indexed research results remains an open literature risk; a plausible related triangular-matrix article had abstract-level access only. Independent mathematical validation has not been performed.

## References
1. C. A. M. André and J. Dias, “Smooth representations of unit groups of split basic algebras over non-Archimedean local fields,” arXiv:1910.14639v1, first publicly posted October 31, 2019. https://arxiv.org/abs/1910.14639 .
2. D. Dolžan, “Bounds for the number of idempotents in finite rings,” *Communications in Algebra* 49 (2021), 4800–4807, published online May 28, 2021, https://doi.org/10.1080/00927872.2021.1929277 . Primary MSC2020 16P10.
3. S. E. Wright, “Triangular idempotent matrices over a general ring,” *Linear and Multilinear Algebra* 70 (2022), 1717–1731, first published online June 1, 2020, https://doi.org/10.1080/03081087.2020.1773377 .
