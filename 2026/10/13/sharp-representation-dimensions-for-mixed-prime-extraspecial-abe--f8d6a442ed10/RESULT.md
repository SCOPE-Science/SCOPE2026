# Sharp representation dimensions for mixed-prime extraspecial–abelian products

## Finding
Let \(\delta(G)\) denote the least dimension of a faithful complex representation of a nontrivial finite group \(G\). For the family defined below,
\[
\boxed{\delta(G)=\sum_{i=1}^{t}p_i^{n_i}+\max\{0,R-t\}.}
\]
The formula is exact, including all boundary cases involving abelian Sylow factors, and an optimal representation is constructed explicitly.

## Assumptions and scope
Fix an integer \(t\geq1\). Choose pairwise distinct primes \(p_1,\ldots,p_t\), positive integers \(n_1,\ldots,n_t\), and any finite abelian group \(A\), possibly trivial. Each \(E_i\) is an extraspecial group of order \(p_i^{2n_i+1}\): its center, derived subgroup, and Frattini subgroup coincide and have order \(p_i\). Both extraspecial isomorphism types are allowed. Set
\[
G=E_1\times\cdots\times E_t\times A,\quad w_i=p_i^{n_i},\quad
r_\ell=\dim_{\mathbb F_\ell}A[\ell],\quad
R=\max_\ell\bigl(r_\ell+\mathbf1_{\ell\in\{p_1,\ldots,p_t\}}\bigr).
\]
Here \(A[\ell]=\{a\in A:\ell a=0\}\). The maximum is finite, and \(R\geq1\). All representations are complex and completely reducible.

## Proof
**Central detection.** Every nontrivial normal subgroup of a finite nilpotent group intersects its center nontrivially. Hence a representation of \(G\) is faithful exactly when its restriction to \(Z(G)\) is faithful. As each irreducible constituent has a scalar central character, a direct sum of \(N\) irreducibles can be faithful only if \(N\geq R\): the \(\ell\)-torsion in \(Z(G)\) has dimension \(r_\ell+\mathbf1_{\ell\in\{p_1,\ldots,p_t\}}\) and each constituent contributes at most one linear functional on this vector space.

**Nonlinear weights.** The character theory of an extraspecial group of order \(p_i^{2n_i+1}\) says that its irreducibles have degree \(1\) or \(w_i\), and exactly the degree-\(w_i\) irreducibles are nontrivial on the center. Thus for each \(i\), at least one constituent of any faithful representation must have an \(E_i\)-factor of degree \(w_i\). Each irreducible constituent is a tensor product of irreducibles of all factors. If \(S\) is the subset of indices carrying nonlinear factors, that constituent has degree \(\prod_{i\in S}w_i\), with empty product one.

For all integers \(w_i\geq2\) one has
\[
\prod_{i\in S}w_i\geq1+\sum_{i\in S}(w_i-1)
\quad\text{and}\quad
\prod_{i\in S}w_i\geq\sum_{i\in S}w_i\quad(S\ne\varnothing).
\]
The first follows inductively from \(ab\geq a+b-1\); the second from \(ab\geq a+b\) for \(a,b\geq2\). Summing the first inequality across \(N\) constituents, and using central detection of every \(E_i\), gives
\[\dim\rho\geq N+\sum_i(w_i-1)\geq R+\sum_i(w_i-1).\]
Summing the second, with empty-index constituents contributing positively, gives independently \(\dim\rho\geq\sum_i w_i\). Therefore
\[\dim\rho\geq\sum_iw_i+\max\{0,R-t\}.\]

**Attainment.** Let \(N=\max(t,R)\). For each \(i\), select one degree-\(w_i\) irreducible of \(E_i\) with nontrivial central character; use this alone (with other extraspecial factors acting trivially) as the \(i\)-th summand. Add \(N-t\) one-dimensional summands. These \(N\) summands can all be tensored by linear characters of \(A\) without changing their dimensions. For each prime \(\ell\notin\{p_i\}\), choose \(r_\ell\) rows to carry independent central characters on \(A[\ell]\). For \(\ell=p_i\), make the \(i\)-th row trivial on \(A[p_i]\), and choose \(r_{p_i}\) of the other \(N-1\) rows to carry independent characters there. This is possible because \(N\geq R\). Every character on \(A[\ell]\) chosen from a basis can be extended to a linear character of \(A\); choices for different primes combine multiplicatively. Hence for every \(\ell\), the central characters of the resulting irreducible summands span the dual of \(Z(G)[\ell]\). The representation is faithful, and its degree is \(\sum_i w_i+N-t\), matching the lower bound.

**Illustrations.** With \(E_1=\mathrm D_8\), \(A=C_3\), one gets \(R=t=1\) and \(\delta(G)=2\). Multiplying the standard faithful two-dimensional representation of \(\mathrm D_8\) by a primitive third-root character of \(C_3\) gives a faithful representation, since nontrivial scalars from the two factors have coprime orders. For \(A=C_3^2\), the theorem gives \(\delta(G)=3\). With \(E_1=\mathrm D_8\) and an extraspecial \(E_2\) of order \(27\), the formula gives \(\delta(E_1\times E_2)=2+3=5\).

## Verification
Run `python3 verify.py` with a standard Python 3 interpreter. The script checks 896 finite weighted-support optimization instances and exactly enumerates the matrix images of \(\mathrm D_8\times C_3\) (24 distinct two-dimensional matrices) and an explicit faithful three-dimensional representation of \(\mathrm D_8\times C_3^2\) (72 distinct images). Its terminal line is `OPTIMIZATION_CASES 896 EXACT_D8_x_C3^2_ELEMENTS 72 VERIFY_OK`. These finite checks do not replace the proof for unbounded primes, ranks, or extraspecial orders.

## Relationship to prior work
Kaur, Kulshrestha, and Udeep (2026), arXiv:2608.18814v1, establish same-prime additivity and give \(\delta(\mathrm D_8\times C_3^2)=3\) as an illustrative cross-prime failure of additivity (Example 2). The present exact formula extends that isolated example to arbitrary abelian Sylow ranks and arbitrarily many extraspecial factors at distinct primes. The same preprint's Theorem 3 makes a broader cyclic-factor additivity assertion; in the coprime cyclic case it conflicts with the explicit faithful two-dimensional construction above, and therefore does not establish the present formula.

Kaur, Kulshrestha, and Singh (2023, arXiv:2308.01612v2) treat faithful degrees of certain groups with cyclic center and give additive statements for mixed-prime products (Theorem 4.1 and Corollary 4.2). Their noncyclic-factor theorem covers some of our subfamilies, notably two extraspecial groups with distinct primes and no abelian factor, but not the full arbitrary-rank formula. The corollary's unrestricted cyclic-Sylow reading also conflicts with the explicit \(\mathrm D_8\times C_3\) construction. Moretó (2021) gives general bounds but not this exact rank-sensitive formula.

## Limitations
The formula is established for pairwise distinct primes of the extraspecial factors; multiple extraspecial factors at the same prime require a different allocation argument and are not claimed here. It concerns complex representations, not modular or real representations. The explicitly exposed comparison with two published cyclic-factor assertions shows a genuine discrepancy rather than an independent referee resolution. An equivalent older exact formula in the broader character-theoretic literature remains possible.

## References
1. G. Kaur, A. Kulshrestha, and A. Udeep, *On the representation dimension of finite \(p\)-groups*, arXiv:2608.18814v1 (first public 2026-08-19), Sections 2–3 and Example 2. https://arxiv.org/html/2608.18814v1
2. G. Kaur, A. Kulshrestha, and A. Singh, *Representation dimension of some finite groups*, arXiv:2308.01612v2 (originally public 2023-08-03), Section 4 and Corollary 4.2. https://arxiv.org/pdf/2308.01612
3. A. Moretó, *On the minimal dimension of a faithful linear representation of a finite group*, arXiv:2102.01463v3 (originally public 2021-02-02), Sections 1–3. https://arxiv.org/html/2102.01463v3
