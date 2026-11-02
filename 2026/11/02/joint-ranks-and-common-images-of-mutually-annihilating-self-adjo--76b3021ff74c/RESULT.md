# Joint ranks and common images of mutually annihilating self-adjoint square-zero operators

## Finding
Let \(q\) be an odd prime power; let \(V\) be an \(n\)-dimensional vector space over \(\mathbb F_q\), \(n\ge 2\), equipped with a nondegenerate symmetric bilinear form \(B\). Write \(T^\sharp\) for its adjoint. For each integer \(m\ge 1\), consider ordered tuples \((T_1,\ldots,T_m)\) satisfying
\[
T_i^\sharp=T_i,\qquad T_iT_j=0\quad(1\le i,j\le m).
\]
In particular, all entries are square-zero and commute, although commuting square-zero tuples not satisfying the zero-product condition are **not** counted. Define \(W=\sum_i\operatorname{im}T_i\), \(t=\dim W\), and \(r_i=\operatorname{rank}T_i\).

The following expression gives **the exact number \(N_{t;r_1,\ldots,r_m}\) for every simultaneous image-span dimension and individual rank vector**:
\[
\boxed{N_{t;r_1,\ldots,r_m}=I_t\sum_{j=0}^{t}{t\brack j}_q(-1)^{t-j}q^{\binom{t-j}{2}}\prod_{i=1}^m {j\brack r_i}_q S_{r_i}.}
\]
Here \({a\brack b}_q=\prod_{h=0}^{b-1}(q^{a-h}-1)/(q^{b-h}-1)\) for \(0\le b\le a\), zero otherwise; \(S_0=1\), and, for \(h\ge0\),
\[
S_{2h}=q^{h(h+1)}\prod_{a=1}^h(q^{2a-1}-1),\qquad S_{2h+1}=q^{h(h+1)}\prod_{a=0}^h(q^{2a+1}-1).
\]
Thus \(S_r\) is the number of nonsingular symmetric \(r\)-by-\(r\) matrices, and the count of symmetric \(j\)-by-\(j\) matrices of rank \(r\) is \({j\brack r}_q S_r\).

Write \(w\) for the Witt index of \(B\). For odd \(n\), \(w=(n-1)/2\). For \(n=2a\), set \(\epsilon=\chi((-1)^a\det B)\), where \(\chi\) is the quadratic character; then \(w=a\) if \(\epsilon=1\) and \(w=a-1\) otherwise. For \(0\le t\le w\), define
\[
p_q(d,\epsilon)=\begin{cases}
(q^{d-1}-1)/(q-1),&d\text{ odd},\\
(q^{d-1}-1)/(q-1)+\epsilon q^{d/2-1},&d\text{ even},
\end{cases}
\qquad
I_t=\frac{\prod_{a=0}^{t-1}p_q(n-2a,\epsilon)}{\prod_{a=0}^{t-1}(q^{t-a}-1)/(q-1)}.
\]
Empty products equal one. The sign is irrelevant in odd dimension; the even-dimensional quotient forms retain the same \(\epsilon\). For \(t>w\), set \(I_t=0\). Then \(I_t\) is the exact number of totally isotropic \(t\)-dimensional subspaces.

The complete multivariate rank and image-span enumerator is
\[
\mathcal R_{B,m}(u,z_1,\ldots,z_m)=\sum_{t=0}^w\sum_{r_1,\ldots,r_m=0}^{t}N_{t;r_1,\ldots,r_m}\,u^t\prod_{i=1}^m z_i^{r_i}.
\]
In particular, the number of ordered mutually annihilating tuples, including the zero tuple, is
\[
\boxed{C_m(B)=\sum_{t=0}^w I_t\sum_{j=0}^t{t\brack j}_q(-1)^{t-j}q^{\binom{t-j}{2}+m\binom{j+1}{2}}.}
\]

**Maximal-subspace classification.** The inclusion-maximal linear subspaces \(L\subseteq\operatorname{End}(V)\) consisting of \(B\)-self-adjoint, pairwise-zero-product maps are exactly
\[
E_U=\{T:T^\sharp=T,\ \operatorname{im}T\subseteq U\}
\]
for maximal totally isotropic \(U\). They all have dimension \(\binom{w+1}{2}\), and there are exactly \(I_w\) of them over \(\mathbb F_q\). Over an algebraic closure, the reduced tuple variety has one irreducible component in odd ambient dimension, two in even dimension; these geometric observations use established orthogonal-isotropic incidence geometry rather than constituting the arithmetic novelty claim.

For \(q=3,n=4\), the split form has \(177\) individual square-zero self-adjoint maps and \(5697\) ordered zero-product pairs, whereas the nonsplit form has respectively \(21\) and \(81\). The exact split pair rank matrix (ranks \(0,1,2\), in that order) is
\[
\begin{pmatrix}1&32&144\\32&448&1152\\144&1152&2592\end{pmatrix},
\]
whereas the nonsplit matrix (ranks \(0,1\)) is \(\begin{pmatrix}1&20\\20&40\end{pmatrix}\). The numbers of maximal annihilating linear spaces are respectively \(8\) and \(10\), with dimensions \(3\) and \(1\).

## Assumptions and scope
All fields have odd characteristic, \(n\ge2\), \(m\ge1\), and \(B\) is nondegenerate symmetric. The operators are actual linear endomorphisms, not conjugacy classes. Their mutual products, including the diagonal products, must be zero. No claim is made for arbitrary merely commuting square-zero tuples or for characteristic two. The geometric statements concern reduced geometric points, not potentially nonreduced defining schemes.

## Proof
**Step 1: common isotropic image criterion.** By self-adjointness, for all \(v,w\in V\), \(B(T_iv,T_jw)=B(v,T_iT_jw)\). Hence all pairwise products vanish if and only if \(W=\sum_i\operatorname{im}T_i\) is totally isotropic: the converse follows from the nondegeneracy of \(B\), because \(B(v,T_iT_jw)=0\) for every \(v,w\) when all images are mutually orthogonal.

**Step 2: symmetric forms on an isotropic subspace.** Fix an isotropic \(U\) of dimension \(j\). If \(T=T^\sharp\) and \(\operatorname{im}T\subseteq U\), then \(T\) kills \(U^\perp\): indeed \(B(Tv,u')=B(v,Tu')=0\) for \(u'\in U^\perp\), so \(Tu'=0\) by symmetry and nondegeneracy. Thus \(T\) factors through \(V/U^\perp\cong U^*\), giving a linear map \(U^*\to U\). Self-adjointness is exactly symmetry of the associated tensor in \(\operatorname{Sym}^2U\). Conversely each symmetric tensor defines such a \(T\). This is an isomorphism, preserving rank, between \(E_U\) and the \(j\)-by-\(j\) symmetric matrices. It also proves \(E_U\) consists entirely of mutually annihilating elements.

**Step 3: symmetric-matrix rank lemma.** Every rank-\(r\) symmetric matrix has a radical of dimension \(j-r\) and induces a nonsingular symmetric form on the quotient. Choosing its radical gives \({j\brack r}_q S_r\). To verify \(S_r\), apply the two nondegenerate-form congruence classes and finite orthogonal-group orders. In odd dimension \(r=2h+1\), both orthogonal orders are \(2q^{h^2}\prod_{a=1}^h(q^{2a}-1)\). Summing \(|\mathrm{GL}_{2h+1}(q)|/|O|\) for the two determinant classes gives \(q^{h(h+1)}\prod_{a=0}^h(q^{2a+1}-1)\). In even dimension \(r=2h\), the orders are \(2q^{h(h-1)}(q^h\mp1)\prod_{a=1}^{h-1}(q^{2a}-1)\). Summing their two orbit sizes similarly gives \(q^{h(h+1)}\prod_{a=1}^h(q^{2a-1}-1)\). The \(r=0\) formula is immediate.

**Step 4: exact common image by Möbius inversion.** For fixed isotropic \(U\) of dimension \(t\), the number of tuples with \(\sum\operatorname{im}T_i\subseteq X\) for a \(j\)-subspace \(X\subseteq U\), and individual ranks \(r_i\), equals \(\prod_i {j\brack r_i}_q S_{r_i}\) by Step 2. The subspace lattice Möbius function is \(\mu(X,U)=(-1)^{t-j}q^{\binom{t-j}{2}}\). Summing over all \({t\brack j}_q\) subspaces \(X\) gives precisely the inner sum in the theorem; its tuples have image span exactly \(U\). Distinct exact spans are disjoint, so multiply by \(I_t\).

**Step 5: isotropic-subspace counts.** Let \(I_t\) count totally isotropic \(t\)-subspaces. A fixed isotropic \((t-1)\)-subspace extends along isotropic lines of its nondegenerate orthogonal quotient of dimension \(n-2(t-1)\). The number of those lines is \(p_q(n-2t+2,\epsilon)\), by the elementary quadratic-form zero count: in odd dimension \(d\), nonzero isotropic vectors number \(q^{d-1}-1\); in even dimension they number \(q^{d-1}-1+\epsilon(q-1)q^{d/2-1}\). Each isotropic \(t\)-subspace contains \((q^t-1)/(q-1)\) hyperplanes. Double-counting incidences gives \(I_t=I_{t-1}p_q(n-2t+2,\epsilon)/((q^t-1)/(q-1))\), with \(I_0=1\), proving the product formula and its Witt-index boundary.

**Step 6: maximal linear spaces.** If \(L\) is a linear space of mutually zero-product self-adjoint operators, its summed image \(U=\sum_{T\in L}\operatorname{im}T\) is isotropic by Step 1, and \(L\subseteq E_U\). If \(U\) is not maximal isotropic, enlarge it. Conversely, for any maximal isotropic \(U\), the images of elements of \(E_U\cong\operatorname{Sym}^2U\) span \(U\) (rank-one symmetric tensors suffice). An additional self-adjoint operator annihilating all elements of \(E_U\) and squaring to zero must therefore have its image in the maximal isotropic \(U\), so already belongs to \(E_U\). This proves the exact maximal-space classification and counts.

**Geometric note.** Over an algebraic closure, put \(\bar w=\lfloor n/2\rfloor\); a tuple is obtained from a maximal geometric isotropic \(U\) of dimension \(\bar w\) and \(m\) symmetric tensors in \(\operatorname{Sym}^2U\). The total space of this vector bundle maps properly onto the affine tuple variety; generic tuples have common image \(U\), making the map generically one-to-one. The maximal-isotropic Grassmannian has one connected component for odd \(n\) and two for even \(n\), yielding the claimed reduced component count. This invokes classical orthogonal-Grassmannian geometry; it does not assert novelty of those geometrical facts.

## Verification
Run `python checker.py` with Python 3 and the standard library, then compare its complete output with `checker_output.txt`. The independent brute-force program enumerates every self-adjoint endomorphism in seven small finite-field configurations, checks original matrix squares and pair products, computes genuine matrix ranks and common image-span ranks, then compares the full coefficients \(N_{t;r_1,\ldots,r_m}\) for \(m=1,2\). It uses \(\mathbb F_9=\mathbb F_3[\alpha]/(\alpha^2+1)\), not integer arithmetic modulo nine. Its marker is `SELFADJOINT_ZERO_PRODUCT_RANK_CENSUS_OK 7_EXHAUSTIVE_CONFIGURATIONS`. Finite tests are not proofs in unbounded dimension or arity; Steps 1–6 supply the general proof.

## Relationship to prior work
Wang's 2000 orthogonal-nullcone article develops incidence resolutions using isotropic images and classifies components of vector-matrix null cones. Those vector-tuple null cones are mathematically related but not the same space as the present tuples of symmetric-tensor endomorphisms. The orthogonal Grassmannian component description here is therefore contextual, not asserted as independent novelty. Fulman and Goldstein's 2012 symmetric-matrix rank distributions, building on older finite-field quadratic-form counts, supply the known single symmetric-tensor rank counts. Brouwer, Gow and Sheekey's 2014 work determines counts of individual symmetric nilpotent matrices, including rank-sensitive variants. The present claim concerns simultaneous mutual-zero-product constraints, the entire joint rank vector and **exact common-image-span** distribution for all tuple lengths, as well as the resulting maximal linear annihilating spaces. These are not stated in the inspected sections of those papers. An unidentified general polar-space enumeration may still subsume some or all of the formulas; no claim of certified historical priority is made.

## Limitations
Only odd characteristic and nondegenerate symmetric forms are treated. The zero-product condition is stronger than commuting. Counts distinguish ranks and combined image dimension but not orthogonal-conjugacy orbits, quadratic-form class of each induced symmetric tensor, or nonreduced structures. The geometric component descriptions use classical incidence geometry. A comprehensive external priority determination and independent verification remain outstanding.

## References
1. W. Wang, *Resolution of singularities of null cones*, arXiv:math/0005078 (first public preprint 2000-05-08), https://arxiv.org/abs/math/0005078. See §§1.1–1.3 and 1.4.
2. J. Fulman and L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504 (first public 2012-11-02), https://arxiv.org/abs/1211.0504. See §4.
3. A. E. Brouwer, R. Gow and J. Sheekey, *Counting symmetric nilpotent matrices*, Electronic Journal of Combinatorics 21(2) (2014), #P2.4, doi:10.37236/3810. See especially §7.
