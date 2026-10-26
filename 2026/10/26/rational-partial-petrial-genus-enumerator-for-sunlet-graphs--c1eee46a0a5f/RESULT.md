# Rational partial Petrial genus enumerator for sunlet graphs

## Finding

For every integer \(n\geq3\), let the *sunlet* \(S_n=C_n\circ K_1\) consist of a simple cycle of length \(n\) with one pendant leaf at every cycle vertex. It has \(2n\) vertices. All matrices below have entries in \(\mathbb F_2\). For every finite simple graph \(G\), define its partial Petrial rank polynomial by
\[
P_G^{\times}(z)=\sum_{D\subseteq V(G)}z^{\operatorname{rank}(A(G)+I_D)},
\]
where \(I_D\) is diagonal with ones at \(D\) and zeros elsewhere. This is the matrix definition of the partial Petrial polynomial [1--4].

Define two rational functions in a length variable \(t\) and a nullity variable \(u\):
\[
H(t,u)=\frac{2t^2(1+u+2t)}{(1-2t)^2(1+t)},
\]
\[
C(t,u)=\frac{(2+u^2)t}{3(1-2t)}+\frac{(1-u^2)t}{3(1+t)}+\frac{ut}{1-2t}.
\]
**Theorem.** For every \(n\ge3\), set
\[
N_n(u)=[t^n]\left(\frac{2t}{1-2t}+\frac{t\,\partial_tH(t,u)}{1-H(t,u)}+C(t,u)\right).
\]
Then
\[
\boxed{P_{S_n}^{\times}(z)=z^{2n}N_n(z^{-1}).}
\]
Thus a **single explicit rational bivariate generating function** gives the number of diagonal choices at every rank and, equivalently, every Euler genus for this complete unicyclic family. In particular,
\[
\begin{aligned}
N_3(u)&=41+22u+u^2,\\
N_4(u)&=149+96u+11u^2,\\
N_5(u)&=553+406u+65u^2,\\
N_6(u)&=1997+1700u+383u^2+16u^3.
\end{aligned}
\]
The least exponent of \(P_{S_n}^{\times}(z)\) is \(4\) for \(n=3\), and \(2n-\lfloor n/2\rfloor\) for every \(n\ge4\). Every coefficient is a nonnegative integer, and \(N_n(1)=4^n\).

## Assumptions and scope

The cycle has labeled, pairwise distinct vertices \(0,\ldots,n-1\), with edges between consecutive indices modulo \(n\); its pendant vertices are \(0',\ldots,(n-1)'\). The labeled subsets \(D\) are counted once each, not modulo graph automorphisms. Coefficients \([t^n]\) refer to formal power series over \(\mathbb Q[u]\), so convergence is irrelevant. The theorem is **not** asserted for cycles of orders one or two; the formulas for the cyclic matrix use two distinct neighbors at every core vertex. The exponent \(\operatorname{rank}\) equals \(2n-\operatorname{nullity}\) throughout.

## Proof

**1. Elimination of all pendant vertices.** Fix a diagonal choice \(D\), and let \(a_i,b_i\in\{0,1\}\) be its cycle and pendant diagonal bits. Let \(B=\{i:b_i=1\}\). If \(b_i=0\), the block on cycle vertex \(i\) and its leaf is
\[
\begin{pmatrix}a_i&1\\1&0\end{pmatrix}.
\]
Its determinant is one; the cycle--cycle entry of its inverse is zero. A Schur complement therefore eliminates this pair without changing adjacencies or diagonals among the remaining vertices. If \(b_i=1\), elimination of the leaf alone adds one to the cycle diagonal \(a_i\). Iterating the two eliminations preserves nullity and leaves precisely
\[
A(C_n[B])+\operatorname{diag}(c_i:i\in B),\qquad c_i=a_i+1.
\]
For every fixed \(B\), its nullity polynomial receives the factor \(2^{n-|B|}\), since the eliminated cycle bits \(a_i\) with \(i\notin B\) are free. The cases \(B=\varnothing\), \(B=V(C_n)\), and \(\varnothing\subsetneq B\subsetneq V(C_n)\) will be counted separately.

**2. A path block.** For an induced path of \(\ell\ge1\) retained cycle vertices, write \(J_\ell\) for the number of choices of its diagonal giving a singular tridiagonal matrix. Every such matrix has nullity at most one: the kernel recurrence
\[
x_{i+1}=c_i x_i+x_{i-1}
\]
is determined by its first entry after the left boundary value zero is fixed. For determinants of leading principal blocks, set \(d_0=1\), \(d_1=c_1\), and \(d_j=c_jd_{j-1}+d_{j-2}\). Two consecutive determinants cannot both vanish. Consequently, among the \(2^{\ell-1}\) diagonal prefixes of length \(\ell-1\), precisely those with nonzero preceding determinant admit a unique final bit making the full determinant zero. Hence
\[
J_0=0,\qquad J_\ell=2^{\ell-1}-J_{\ell-1}
\quad(\ell\ge1),
\]
and therefore
\[
J_\ell=\frac{2^\ell-(-1)^\ell}{3}.
\]
This is also the established Jacobsthal path formula [2,3]. The path nullity polynomial is
\[
p_\ell(u)=(2^\ell-J_\ell)+J_\ell u,
\]
and its length generating series is
\[
F(t,u)=\sum_{\ell\ge1}p_\ell(u)t^\ell
=\frac{t(1+u+2t)}{(1-2t)(1+t)}.
\]

**3. Proper nonempty retained sets.** If \(B\) is nonempty and proper, \(C_n[B]\) consists of cyclically ordered vertex-disjoint path components, separated by one or more deleted cycle vertices. Each run of retained vertices of length \(\ell\) contributes \(p_\ell(u)t^\ell\); each run of deleted vertices of length \(h\ge1\) contributes \(2^ht^h\), with generating function \(G(t)=2t/(1-2t)\). Thus one consecutive retained/deleted run pair contributes \(H=FG\), exactly as displayed in the theorem.

For a cyclic binary word with \(k\) retained runs and \(k\) deleted runs, distinguish one retained-to-deleted boundary. Such distinguished labeled words are counted by \(n[t^n]H(t,u)^k\): choose the boundary's position among the \(n\) labeled positions and then the ordered positive run lengths. Each undistinguished labeled word is represented \(k\) times. Therefore the total contribution for all proper nonempty \(B\) is
\[
\sum_{k\ge1}\frac{n}{k}[t^n]H^k
=[t^n]t\,\partial_t\left(-\log(1-H)\right)
=[t^n]\frac{t\,\partial_tH}{1-H}.
\]
The identity is formal, and no assumption of aperiodicity is needed: boundaries, not rotational orbits, are marked.

**4. All retained cycle vertices.** For \(B=V(C_n)\), kernel vectors satisfy
\[
\begin{pmatrix}x_{i+1}\\x_i\end{pmatrix}
=T(c_i)\begin{pmatrix}x_i\\x_{i-1}\end{pmatrix},\qquad
T(0)=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad
T(1)=\begin{pmatrix}1&1\\1&0\end{pmatrix}.
\]
The matrices generate \(\mathrm{GL}(2,\mathbb F_2)\cong S_3\); the first is an element of order two and the second one of order three. For \(n\ge3\), the cycle's nullity is the fixed-space dimension of the product of these \(n\) matrices. It is two for the identity, one for a transposition, and zero for a nonidentity three-cycle.

Exactly \(2^{n-1}\) binary words contain an odd number of copies of \(T(0)\), hence give a transposition. Write \(e_n\) for the number with identity product. The standard two-dimensional character \(\chi\) of \(S_3\) has values \(2,0,-1\) on identity, transpositions and nonidentity three-cycles. In its real plane representation, the matrix \(\rho(T(0))+\rho(T(1))\) has eigenvalues zero and minus one. Thus
\[
\sum_{c\in\{0,1\}^n}\chi(T(c_n)\cdots T(c_1))
=\operatorname{tr}\left((\rho(T(0))+\rho(T(1)))^n\right)
=(-1)^n,
\]
while counting the three conjugacy types gives \(3e_n-2^{n-1}\). Therefore
\[
e_n=\frac{2^{n-1}+(-1)^n}{3},
\]
and the full retained-cycle nullity enumerator is
\[
C_n(u)=\frac{2^n-(-1)^n}{3}+2^{n-1}u+
\frac{2^{n-1}+(-1)^n}{3}u^2.
\]
The coefficient of \(t^n\) in \(C(t,u)\) equals precisely \(C_n(u)\), by geometric-series expansion.

**5. Completion and least rank.** The empty set \(B\) contributes \(2^n\) nonsingular outcomes, enumerated by \([t^n]2t/(1-2t)\). Adding this, step 3, and step 4 proves the boxed identity for all \(n\ge3\). For a proper \(B\), every path component contributes nullity at most one. Because each retained run must be separated from the next by a nonempty deleted run, the number of path components is at most \(\lfloor n/2\rfloor\). For \(B=V(C_n)\), the nullity is at most two, which is bounded by \(\lfloor n/2\rfloor\) if \(n\ge4\). The bound is attained by retaining \(\lfloor n/2\rfloor\) pairwise nonadjacent cycle vertices and choosing their diagonal bits to be zero. For \(n=3\), retaining all vertices with every diagonal bit one gives the rank-one all-ones matrix, of nullity two. This proves the least-rank assertion. Finally the evaluation \(u=1\) counts all \(2^{2n}=4^n\) diagonal assignments and gives the stated normalization.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. The script constructs the full \(2n\)-vertex adjacency matrix and enumerates **all** diagonal assignments for \(3\le n\le8\), independently compares the formula's coefficients against a Schur-reduced enumeration for \(3\le n\le10\), and verifies the normalization and least-rank statements through \(n=12\). Recorded deterministic output is in `verify_output.txt`. The direct enumeration covers \(87{,}360\) diagonal assignments. These finite tests are corroboration; the preceding proof is valid for all \(n\ge3\).

## Relationship to prior work

The definition, topological motivation, and Jacobsthal path polynomial are established in [1--4]. Deng and Zhang [3] classify trees with trinomial partial Petrial polynomials and provide complete formulas for T- and H-shaped trees, but their claims and cases do not evaluate this unicyclic sunlet family. Feng, Guo and Yan [4] prove a general edge-pivot/local-complementation recurrence and inequalities for extreme coefficients; applying a general recurrence to a graph is not itself the explicit uniform bivariate rational solution above. The matrix theory [5] supplies general pivot identities and leaf reductions, but no sunlet enumerator. The result here is the complete genus/rank profile over **every order** of the cycle corona, obtained through a cyclic-run and six-element monodromy decomposition. A generic recursion was not presented as an originality claim.

## Limitations

No independent audit has been performed. The literature comparison covers identified closely related accessible primary works; equivalent results in unindexed literature remain a priority risk. The formula is for simple sunlets with one leaf per cycle vertex and does not establish analogous expressions for general unicyclic graphs, other corona products, or other fields. A circle-graph/bouquet interpretation is conditional on selecting an appropriate orientable bouquet representation; the theorem itself only uses the unambiguous matrix polynomial. Computational enumeration is finite and is not the argument establishing all orders.

## References

[1] Q. Yan and Y. Li, *Partial Petrial polynomials for complete graphs and paths*, arXiv:2501.04186v1 (2025-01-07). https://arxiv.org/html/2501.04186v1

[2] Q. Deng, X. Jin and Q. Yan, *Partial-twuality polynomials of matrices*, arXiv:2604.12433v1 (2026-04-14). https://arxiv.org/html/2604.12433v1

[3] Q. Deng and C. Zhang, *A Characterization of Trees with Trinomial Partial Petrial Polynomials*, arXiv:2608.01748v1 (2026-08-03). https://arxiv.org/pdf/2608.01748v1

[4] R. Feng, X. Guo and Q. Yan, *Recurrence and coefficient inequality for the partial Petrial polynomial of graphs*, arXiv:2606.03166v1 (2026-06-02). https://arxiv.org/html/2606.03166

[5] X. Yu, R.-X. Hao, J. Liu and Z. Li, *Partial Petrial Polynomials of Ribbon Graphs*, arXiv:2604.21942v1 (2026-04-15). https://arxiv.org/html/2604.21942v1
