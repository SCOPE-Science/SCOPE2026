# The divisor-and-root lattice of subalgebras of cyclic permutation evolution algebras

## Finding
Let \(K\) be any field and \(n\ge 2\). Let \(E_n(K)\) have basis \(e_0,\ldots,e_{n-1}\), with indices read modulo \(n\), and multiplication
\[
e_i e_j=0\quad(i\ne j),\qquad e_i^2=e_{i+1}.
\]
This is a nonassociative, commutative evolution algebra. **All** its multiplication-closed \(K\)-linear subspaces, not merely those with a basis extending a natural basis of the ambient algebra, form the following explicit lattice.

For each divisor \(d\mid n\), put
\[
M_d=\frac{2^n-1}{2^d-1},\qquad
\mu_{M_d}(K)=\{c\in K^\times:c^{M_d}=1\},
\qquad
f_d(i)=\frac{2^i-2^{i\bmod d}}{2^d-1}\quad(0\le i<n).
\]
The exponent \(f_d(i)\) is a nonnegative integer. For \(c\in\mu_{M_d}(K)\), define
\[
U(d,c)=\Big\{(x_0,\ldots,x_{n-1})\in K^n:
 x_{kd+j}=c^{f_d(kd+j)}t_j\ 
(0\le j<d,\ 0\le k<n/d),\quad t_0,\ldots,t_{d-1}\in K\Big\}.
\]
The subalgebras are **exactly** \(\{0\}\) and these \(U(d,c)\); the representation is unique, \(\dim_K U(d,c)=d\), and the partial order is
\[
U(d,c)\subseteq U(e,h)
\ \Longleftrightarrow\
 d\mid e\text{ and }h=c^{(2^e-1)/(2^d-1)}.
\]
Every nonzero subalgebra is itself a simple, perfect, \(d\)-dimensional cycle evolution algebra; in particular, no proper nonzero subalgebra is an ideal of \(E_n(K)\).

For every finite field \(K=\mathbb F_q\), the **complete embedded subalgebra-dimension polynomial** is
\[
\boxed{\mathcal S_{n,q}(T)=1+\sum_{d\mid n}
\gcd\!\left(q-1,\frac{2^n-1}{2^d-1}\right)T^d.}
\]
For example,
\[
\mathcal S_{6,8}(T)=1+7T+7T^2+T^3+T^6.
\]
Thus there are exactly \(17\) subalgebras in this example. The coefficient of \(T\) (idempotent lines) is a previously accessible invariant; the additional intermediate-dimensional families and their inclusion relations are the focus of the classification.

## Assumptions and scope
A subalgebra here means **any** \(K\)-linear subspace closed under the bilinear product, including \(0\) and \(E_n(K)\). No associativity, algebraic closure, perfectness of \(K\), or restriction on its characteristic is assumed. Coordinates always refer to the displayed natural basis; \(\mu_m(K)\) is a set of roots in \(K\), not in an algebraic closure. In the finite-field count \(q\) is an arbitrary prime power. The statement does not claim an enumeration for arbitrary weighted or multi-cycle structure matrices.

## Proof
**Step 1: full support.** Denote coordinatewise (Schur) product by \(u\ast v=(u_iv_i)_i\) and the cyclic shift by \((Pv)_{i+1}=v_i\). Then \(uv=P(u\ast v)\). For a nonzero subalgebra \(U\), let \(B=\operatorname{span}_K\{u\ast v:u,v\in U\}\). A coordinate belongs to \(\operatorname{supp}(B)\) if and only if it belongs to \(\operatorname{supp}(U)\): one direction is clear; for the other take a vector with nonzero coordinate and square it coordinatewise. Because \(P(B)\subseteq U\), \(P(\operatorname{supp}U)\subseteq\operatorname{supp}U\). The shift is transitive, so \(U\) has full coordinate support.

**Step 2: equality of Schur-square dimensions forces a weighted partition code.** Write \(r=\dim U\). Select \(r\) independent coordinate functionals \(\ell_1,\ldots,\ell_r\in U^*\). Their bilinear tensors \(\ell_j\otimes\ell_j\) are linearly independent; hence \(\dim B\ge r\). Product closure gives \(\dim B=\dim P(B)\le r\); thus equality holds. Every other coordinate functional \(\ell=\sum_j a_j\ell_j\) has \(\ell\otimes\ell\) in the span of \(\ell_j\otimes\ell_j\). Comparing off-diagonal tensors \(\ell_j\otimes\ell_k\) for \(j\ne k\) yields \(a_ja_k=0\) for every unequal pair. Thus \(\ell\) is a nonzero scalar multiple of **exactly one** \(\ell_j\). This comparison uses bilinear tensors, not merely diagonal quadratic functions, so it works even in characteristic two. Therefore the coordinate positions partition into \(r\) nonempty blocks, and \(U\) consists of one independently varying scalar per block multiplied by fixed, nonzero coordinate weights. The Schur square \(B\) has exactly the same blocks, but with the weights squared.

**Step 3: the partition is cyclic.** Since \(P(B)=U\), shifting the blocks of \(B\) gives the same partition as that of \(U\). A partition of \(\mathbb Z/n\mathbb Z\) invariant under translation by one is a system of cosets of a subgroup. Its blocks therefore have the form \(\{kd+j:0\le k<n/d\}\), \(0\le j<d\), for a unique divisor \(d\mid n\), and \(r=d\).

**Step 4: solve the weights without leaving any free normalization.** Let \(v_j\in U\) be supported on the block \(j\), and normalize its coordinate at \(j\) to one. Write \(w_i\) for the resulting nonzero weight at coordinate \(i\), so \(w_j=1\) for \(0\le j<d\). Because \(P(v_j\ast v_j)\) is a nonzero vector supported in block \(j+1\), it is a scalar multiple of \(v_{j+1}\). The distinguished coordinates force the scalar to be one for \(j<d-1\). Therefore \(w_{kd+j}=b_k^{2^j}\) for \(b_k=w_{kd}\), with \(b_0=1\). The final block transition gives one scalar \(c\in K^\times\) such that \(b_{k+1}=c\,b_k^{2^d}\) (the index \(k\) is cyclic modulo \(n/d\)). Consequently
\[
b_k=c^{1+2^d+\cdots+2^{(k-1)d}},\quad
w_{kd+j}=c^{2^j(2^{kd}-1)/(2^d-1)}=c^{f_d(kd+j)}.
\]
The wrap-around equation \(b_{n/d}=b_0=1\) is precisely \(c^{M_d}=1\). Conversely, these equations, including wrap-around, prove \(v_j^2=v_{j+1}\) for \(j<d-1\), \(v_{d-1}^2=c^{-1}v_0\), and \(v_iv_j=0\) for distinct \(i,j\). Hence every proposed \(U(d,c)\) is a subalgebra. The coordinate normalization makes \(d\) and \(c\) unique; the case \(d=n\) has \(M_n=1\) and only \(c=1\).

**Step 5: inclusion and simplicity.** If \(U(d,c)\subseteq U(e,h)\), each pair of coordinate functionals proportional on \(U(e,h)\) is proportional upon restriction to \(U(d,c)\); hence the congruence modulo \(e\) refines that modulo \(d\), giving \(d\mid e\). For \(i=ke+r\) with \(0\le r<e\), compare the normalized weights at \(i\) and \(r\). The identity
\[
f_d(ke+r)-f_d(r)=\frac{2^e-1}{2^d-1}\,f_e(ke+r)
\]
shows that membership of every normalized block vector is equivalent to \(h=c^{(2^e-1)/(2^d-1)}\). This proves both implications of the poset rule. Each \(U(d,c)\) has the displayed nonzero cyclic multiplication constants, so its products span it (perfectness), and multiplying any nonzero ideal element by a suitable block basis vector and iterating along the cycle generates the whole algebra (simplicity). In particular \(E_n(K)\) has no proper nonzero ideals.

**Step 6: count.** Over \(\mathbb F_q\), the multiplicative group is cyclic of order \(q-1\). Therefore \(|\mu_{M_d}(\mathbb F_q)|=\gcd(M_d,q-1)\). Uniqueness from Steps 3–4 yields the polynomial and the stated example.

## Verification
Run `python checker.py` with Python 3 and no third-party libraries. The checker independently enumerates all reduced-row-echelon subspaces, tests multiplication closure by basis products, and compares rank counts with the formula for 12 small \((n,q)\) cases: \((2,2),(2,3),(2,4),(3,2),(3,4),(3,8),(4,2),(4,3),(4,4),(4,5),(5,2),(6,2)\). It also constructs the proposed normalized subspaces and independently verifies closure, cardinality, and the inclusion rule (via matrix ranks) for \((n,q)=(4,4),(6,2),(6,8),(12,4),(12,8)\). Arithmetic for \(\mathbb F_4\) and \(\mathbb F_8\) uses explicit irreducible binary polynomials. Successful completion prints `VERIFY_OK`. No finite computation is used as a proof for all fields or dimensions; the proof above supplies the infinite argument.

## Relationship to prior work
Narkuziyev (arXiv:2005.05793, first posted 2020-05-09) studies evolution algebras corresponding to permutations and their idempotents. Boudi–Cabrera Casado–Siles Molina (arXiv:2006.14460) treat natural bases, extending natural families and basic ideals. Wei–Zou (arXiv:2310.12368) classify **ambient algebras up to isomorphism** through monomial group actions. More directly, Ladra–Pérez-Rodríguez (arXiv:2503.07187; DOI:10.5802/crmath.804), Theorem 2 and Corollary 4, **already prove** that every subalgebra of any regular evolution algebra has a natural basis with pairwise disjoint supports, and Proposition 5 gives a codimension-one criterion. That general disjoint-support conclusion, also obtained independently in Step 2 above, is credited as known and not claimed as an original theorem. Their full five-page article was read, including the statement and proof of the general theorem and its subalgebra characterizations; it does not state or imply without further cycle-specific classification the divisor/root parameterization, all-dimensional counts, or precise containment formula. The new statement specializes to a single-cycle permutation algebra and **solves the weighted partition constraints and incidence relations in all dimensions**, including proper nonextendable subalgebras. Its dimension-one idempotent coefficient is also already accessible in previous work and is not claimed as new. Full text of Boudi et al. and Wei–Zou was inspected at the relevant sections; the complete text of Narkuziyev's article could not be inspected, leaving residual risk of unrecognized equivalence.

## Limitations
Only a single unweighted cyclic permutation structure matrix is classified. The result does not enumerate all subalgebras of arbitrary weighted cycles, sums of several cycles, or arbitrary evolution algebras. It is an embedded-subalgebra classification, not a claim that different parameters give pairwise nonisomorphic abstract algebras. The sources and searches considered do not certify global mathematical novelty; independent evaluation remains necessary. The displayed computer checks cover only explicitly stated small cases.

## References
1. B. A. Narkuziyev, *Some remarks on evolution algebras corresponding to permutations*, arXiv:2005.05793 (2020); Journal of Algebra and Its Applications, DOI:10.1142/S0219498822501122.
2. N. Boudi, Y. Cabrera Casado, M. Siles Molina, *Natural families in evolution algebras*, arXiv:2006.14460 (2020); Publicacions Matemàtiques (2022).
3. Y. Wei, Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368 (2023); Linear Algebra and its Applications 675 (2023), 142–178.
4. M. Ladra, A. Pérez-Rodríguez, *Regular evolution algebras are closed under subalgebras*, arXiv:2503.07187 (first posted 2025-03-10); Comptes Rendus Mathématique 363 (2025), 1461–1465; DOI:10.5802/crmath.804.
