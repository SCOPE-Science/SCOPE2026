# Parity spectrum of maximal commuting rank-one symmetric idempotents in characteristic two

## Finding
Let \(q=2^e\) with \(e\ge1\), \(n\ge2\), and let \(\Gamma_{n,q}\) have as vertices the rank-one matrices \(P\in M_n(\mathbb F_q)\) satisfying \(P^T=P=P^2\). Distinct vertices are adjacent when they commute. Define
\[
H_{2a}(q)=q^{a^2}\prod_{i=1}^{a}(q^{2i}-1),\quad H_0(q)=1,
\]
and, for \(d\ge1\),
\[
G_d(q)=\begin{cases}H_{d-1}(q),&d\text{ odd},\\ q^{d-1}H_{d-2}(q),&d\text{ even}.\end{cases}
\]
The **complete clique polynomial**, including the empty clique, is \(C_{n,q}(z)=\sum_{k=0}^n c_kz^k\) with \(c_0=1\) and, for \(1\le k\le n\) and \(d=n-k\),
\[
 c_k=\frac{G_n(q)}{k!}\left(\mathbf 1_{d\ge1}\frac{1}{G_d(q)}+\mathbf 1_{2\mid d}\frac{1}{H_d(q)}\right).
\]
The number of **inclusion-maximal** cliques of size \(k\) is
\[
 m_k=\begin{cases}\dfrac{G_n(q)}{k!H_{n-k}(q)},&1\le k\le n,\quad n-k\text{ even},\\0,&\text{otherwise}.\end{cases}
\]
In particular, the possible maximal-clique sizes are **exactly** \(n,n-2,n-4,\ldots\) down to \(1\) for odd \(n\) or \(2\) for even \(n\). The clique number is \(n\), whereas the smallest maximal clique has size one for odd \(n\) and two for even \(n\). For odd \(n\) there is exactly one isolated vertex. For even \(n\), precisely \(q^{n-1}/2\) maximal cliques have size two. These assertions hold for all \(q\), including \(q=2\).

## Assumptions and scope
All vector spaces and matrices are over the specified finite field of characteristic two; \(T\) denotes ordinary transpose, not an involution on the field. A clique is an unordered **set of distinct** matrices; the empty clique contributes one to \(C_{n,q}\). Matrix commutation is ordinary matrix multiplication. The form is \(b(u,v)=u^Tv\) on \(V=\mathbb F_q^n\), not the polar form of a characteristic-two quadratic form. The quantity \(H_{2a}(q)\) is the cardinality of the symplectic group in even dimension; no \(H_d\) is used for odd \(d\). The integer factorials divide the indicated ordered-frame counts.

## Proof
**1. Projections and orthonormal vectors.** Any symmetric rank-one matrix is \(\lambda vv^T\) for a nonzero vector \(v\) and a scalar \(\lambda\ne0\). Idempotence gives \(\lambda(v^Tv)=1\). In characteristic two, \(v^Tv=(\sum_i v_i)^2\). Thus its normalized representative \(u=v/(\sum_i v_i)\) exists, is unique, has \(\sum_i u_i=1\), and \(P=uu^T\). Conversely every such \(u\) gives a vertex. For two distinct normalized vectors \(u,w\), the rank-one products are \((u^Tw)uw^T\) and \((u^Tw)wu^T\). Their equality forces \(u^Tw=0\): otherwise their image lines coincide, hence the two normalized vectors are equal. Therefore cliques are precisely unordered families of pairwise orthogonal vectors of norm one. They are linearly independent, and every clique has size at most \(n\).

**2. The canonical vector and terminal frames.** Put \(\omega=(1,\ldots,1)^T\). The perfectness of \(\mathbb F_q\) gives
\[
 b(x,x)=b(x,\omega)^2.
\]
For an ordered orthonormal \(k\)-frame \(u_1,\ldots,u_k\), let \(U\) be its span and \(W=U^\perp\). The restriction \(b|_W\) is nonsingular, and it is alternating precisely when \(b(w,\omega)=0\) for all \(w\in W\), namely when \(\omega\in U\). Its orthogonal projection onto \(U\) is \(\sum_i u_i\); hence in the alternating case \(\omega=\sum_i u_i\). A clique can be enlarged by one more vertex precisely when \(W\) contains a norm-one vector. A nonsingular symmetric bilinear form over a perfect characteristic-two field contains such a vector exactly when it is nonalternating. Therefore a clique is maximal precisely when \(W\) is alternating, equivalently \(\omega\in U\). Every such \(W\) has even dimension. For every \(1\le k\le n\) with \(n-k\) even, such a frame exists: the nonalternating form \(I_k\perp H^{(n-k)/2}\) is isometric to \(I_n\), as shown in the next step. This also proves the stated parity spectrum and the isolated vertex in odd dimension, represented by \(\omega\).

**3. Isometry types and orders.** Over a perfect characteristic-two field, all nonsingular alternating forms in dimension \(2a\) are symplectic and have isometry-group order \(H_{2a}(q)\). Every nonsingular **nonalternating** symmetric form in dimension \(d\ge1\) is isometric to \(I_d\). To see this without assuming an unproved classification, split off a normalized anisotropic line. Repeat if its orthogonal complement is nonalternating; if an alternating complement remains, use \([1]\perp H\cong I_3\) (an explicit orthonormal basis in the left-hand space is \(a+b,a+c,a+b+c\) for \(b(a,a)=b(b,c)=1\) and other pairings zero). This eliminates symplectic planes one by one. Consequently there are exactly two possible complement types for a \(k\)-frame when \(d=n-k\) is even and positive (alternating or nonalternating), only the nonalternating type when \(d\) is odd, and only the zero alternating type when \(d=0\).

Write \(\mathcal O_d\) for the isometry group of \(I_d\). Every isometry fixes its canonical vector \(\omega\), because \(b(x,\omega)^2=b(x,x)\) and the square map is injective. For odd \(d\), \(b(\omega,\omega)=1\), so \(I_d=\langle\omega\rangle\perp\omega^\perp\), the latter alternating of dimension \(d-1\). Restriction yields \(\mathcal O_d\cong\operatorname{Sp}_{d-1}(q)\) and order \(G_d=H_{d-1}\). For even \(d\), \(\omega\) is isotropic. Choose \(h\) with \(b(h,\omega)=1\), set \(Z=\langle h,\omega\rangle^\perp\); its form is alternating of dimension \(d-2\). The action on \(\omega^\perp/\langle\omega\rangle\cong Z\) maps \(\mathcal O_d\) onto \(\operatorname{Sp}(Z)\). For the kernel, given \(a\in Z\), \(c\in\mathbb F_q\), fix \(\omega\), send \(z\in Z\) to \(z+b(z,a)\omega\), and send \(h\) to \(h+a+c\omega\). These and only these are kernel elements (check pairings with \(h,Z,\omega\)), so the kernel has \(q^{d-1}\) members. Thus \(|\mathcal O_d|=G_d=q^{d-1}H_{d-2}\). The case \(d=2\) uses \(Z=0\) and is included.

**4. Orbit–stabilizer and all clique sizes.** A full ordered orthonormal frame is an isometry of \(I_n\); there are \(G_n\) of them. More generally, the isometry group acts transitively on ordered \(k\)-frames with a specified isometry type of residual form: map the frames to each other and extend by any isometry of their nonsingular complements. The stabilizer fixes each frame vector and acts by the entire isometry group of the complement. Therefore the ordered-frame count is \(G_n/G_d\) for nonalternating complements and \(G_n/H_d\) for alternating complements. For \(k=0\) only the empty frame exists. For each \(k\ge1\), add the available complementary-type counts and divide by \(k!\) to obtain \(c_k\). Keeping only alternating complements gives \(m_k\). Since full frames exist, maximum clique size \(n\) occurs. For odd \(n\), \(m_1=G_n/H_{n-1}=1\); for even \(n\), \(m_2=G_n/(2H_{n-2})=q^{n-1}/2\). All statements follow.

## Verification
Run `python verify.py` with Python 3 (no external dependencies). It constructs actual finite fields of orders \(2,4,8\), enumerates normalized vectors and literal rank-one matrices, compares actual matrix products with the claimed adjacency, then enumerates **all** cliques and maximal cliques in ten \((q,n)\) configurations. It independently checks every coefficient against the isometry-group formulas, not just the maximum. In particular the full clique polynomials are
\[
C_{4,2}(z)=1+8z+16z^2+8z^3+2z^4,
\]
\[
C_{4,4}(z)=1+64z+512z^2+640z^3+160z^4.
\]
The all-size maximal-clique counts for \((n,q)=(6,2)\) are \(m_2=16,m_4=160,m_6=32\), with all others zero. The verifier prints `VERIFY_OK_SYMMETRIC_IDEMPOTENT_PARITY_CLIQUES`. The proof applies to arbitrary \(e,n\); finite enumeration is supplementary evidence only.

## Relationship to prior work
The equivalence of self-adjoint idempotents with orthogonal projections onto nondegenerate subspaces is classical; Murray's Lemma 3.5 proves a module-theoretic version in characteristic two. The isometry groups of nonalternating symmetric bilinear forms are studied by Kramer and Stroppel. Their structural isometry-group analysis is background, not newly claimed here. Iosevich–Senger count mutually orthogonal tuples asymptotically in arbitrary large finite-field subsets, rather than exact orthonormal partial frames and their nonextendible families. The characteristic-two orthogonal graph literature (Zhou, Gu, Wan) studies subconstituents of singular orthogonal graphs; those adjacency parameters have not been found to imply the complete maximal-clique parity spectrum for the **nonalternating bilinear** projection graph here. A recent treatment of cliques in **representation graphs of quadratic forms** (DOI 10.1007/s10801-025-01493-5) uses edges from \(Q(x-y)=a\); in characteristic two its polar bilinear form is alternating, so it does not specialize to this nonalternating dot-product graph, and its maximum-clique formulas do not imply the all-size terminal-frame enumeration. The contribution assessed here is the precise partial-frame terminal criterion and the resulting complete clique and maximal-clique spectra, not the classical forms or symplectic group orders.

## Limitations
The result concerns rank-one **symmetric idempotents** with ordinary transpose over finite fields of characteristic two; it is not a claim for higher-rank projections, odd characteristic, Hermitian adjoints, or graphs defined from quadratic-form polarization. The published-literature overlap check is necessarily bounded; an earlier equivalent description of partial orthonormal-frame maximality or orbit counts under different graph terminology remains possible. The exact frame count is proved for finite fields only; no claim is made for imperfect fields of characteristic two.

## References
- *Cliques in representation graphs of quadratic forms*, Journal of Algebraic Combinatorics, doi:10.1007/s10801-025-01493-5; Definitions 1.1 and 4.1, Lemma 4.4 and section 5.2, defining a different distance-based graph. https://doi.org/10.1007/s10801-025-01493-5
- A. Iosevich and S. Senger, *Orthogonal systems in vector spaces over finite fields*, Electronic Journal of Combinatorics **15** (2008), R151, published 9 December 2008; Theorem 1.1 counts orthogonal tuples asymptotically in large subsets. https://www.combinatorics.org/ojs/index.php/eljc/article/download/v15i1r151/pdf/
- J. C. Murray, *Symmetric bilinear forms and vertices in characteristic 2*, arXiv:1501.00862, initial public version 5 January 2015; especially Lemma 3.5 (orthogonal projection). https://arxiv.org/abs/1501.00862
- L. Kramer and M. J. Stroppel, *Hodge operators and groups of isometries of diagonalizable symmetric bilinear forms in characteristic two*, arXiv:2208.11326, initial version 24 August 2022; Section 1 and the dimension-four isometry computations. https://arxiv.org/abs/2208.11326
- K. Zhou, Z. Gu, Z.-X. Wan, *Subconstituents of orthogonal graphs of characteristic 2*, Linear Algebra Appl. 507 (2016), 251–266, doi:10.1016/j.laa.2016.05.036 (abstract and bibliographic details checked). https://doi.org/10.1016/j.laa.2016.05.036
