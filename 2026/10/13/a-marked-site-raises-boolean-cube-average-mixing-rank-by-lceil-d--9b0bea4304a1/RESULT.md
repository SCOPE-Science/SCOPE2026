# A marked site raises Boolean-cube average-mixing rank by \(\lceil d/2\rceil\)

## Finding

For each integer \(d\geq 1\), let \(Q_d\) be the graph on \(V=\{0,1\}^d\) whose edges flip one bit, let \(A\) be its ordinary real symmetric adjacency matrix, and let \(o=0^d\). For each real \(\tau\), set \(H_\tau=A+\tau e_o e_o^{\mathsf T}\), \(U_\tau(t)=e^{\mathrm i tH_\tau}\), and define the infinite-time average-mixing matrix entrywise by
\[
\widehat M_\tau=\lim_{T\longrightarrow\infty}\frac1T\int_0^T\bigl(U_\tau(t)\circ\overline{U_\tau(t)}\bigr)\,dt.
\]
(Here \(\circ\) denotes entrywise multiplication; the limit exists.) Then
\[
\operatorname{rank}\widehat M_\tau=\begin{cases}2^{d-1},&\tau=0,\\2^{d-1}+\lceil d/2\rceil,&\tau\ne 0.\end{cases}
\]
For a nonzero mark there is also an exact kernel description. Write \(\chi_S(x)=(-1)^{\sum_{i\in S}x_i}\) for subsets \(S\subseteq\{1,\dots,d\}\). Let \(\mathcal O=\operatorname{span}\{\chi_S:|S|\text{ odd}\}\) and let \(\mathcal R\) be the space of functions constant on every Hamming-weight shell \(\{x:|x|=k\}\). Then
\[
\ker\widehat M_\tau=\mathcal O\cap\mathcal R^\perp\quad(\tau\ne0).
\]
Consequently precisely \(\lceil d/2\rceil\) formerly dark, radial odd-Walsh directions become visible when a vertex is marked; all nonradial odd-Walsh directions remain in the kernel. The strength or sign of the nonzero mark does not affect the rank.

## Assumptions and scope

The graph is a finite, unweighted Boolean hypercube; only one vertex has a real diagonal potential. By vertex transitivity the choice of marked vertex is immaterial. The walk has the adjacency-plus-potential Hamiltonian shown above, not the normalized Laplacian or a discrete-time coined walk. The matrix is an all-starting-vertices/all-destinations Cesàro average, not a single-start search-success probability. Rank and orthogonality are taken over the reals, and spectral eigenspaces with repeated eigenvalues are kept intact. The result holds for every integer dimension \(d\ge1\), including \(d=1\), and all real \(\tau\).

## Proof

**1. Spectral projectors and radial/dark splitting.** Set \(N=2^d\). The normalized Walsh functions \(\chi_T/\sqrt N\), indexed by \(T\subseteq[d]\), are an orthonormal eigenbasis of \(A\), with eigenvalue \(\lambda_j=d-2j\) when \(|T|=j\). Let \(E_j\) be the projector onto their weight-\(j\) span, of rank \(m_j=\binom dj\), and define
\[
 w_j=\frac{E_je_o}{\sqrt{m_j/N}}=\frac1{\sqrt{m_jN}}\sum_{|T|=j}\chi_T,
 \qquad F_j=E_j-w_jw_j^{\mathsf T}.
\]
The vectors \(w_0,\ldots,w_d\) form an orthonormal basis of the Hamming-radial space \(\mathcal R\). Every \(F_j\) projects onto an orthogonal \((m_j-1)\)-dimensional space unaffected by \(\tau e_oe_o^{\mathsf T}\), because \(F_je_o=0\).

In the orthonormal **position-shell basis** \(u_k=\binom dk^{-1/2}\sum_{|x|=k}e_x\) of \(\mathcal R\), the Hamiltonian has the Jacobi form with off-diagonals \(\sqrt{(k+1)(d-k)}>0\), the root diagonal equal to \(\tau\), and other diagonals zero. Thus its \(d+1\) eigenvalues \(\mu_s\) are simple. They are disjoint from every \(\lambda_j\) when \(\tau\ne0\): the rank-one characteristic polynomial in the \(w_j\) basis equals
\[
 p_\tau(z)=\prod_{j=0}^d(z-\lambda_j)-\tau\sum_{j=0}^d\frac{m_j}{N}\prod_{\ell\ne j}(z-\lambda_\ell),
\]
so \(p_\tau(\lambda_j)=-\tau(m_j/N)\prod_{\ell\ne j}(\lambda_j-\lambda_\ell)\ne0\). Let \(B_s\) denote the rank-one projector onto the radial eigenvector of eigenvalue \(\mu_s\). Distinct-eigenvalue spectral averaging gives
\[
 \widehat M_\tau=M_{\mathrm{dark}}+M_{\mathrm{bright}},\quad
 M_{\mathrm{dark}}=\sum_{j=0}^dF_j\circ F_j,\quad
 M_{\mathrm{bright}}=\sum_{s=0}^dB_s\circ B_s\qquad(\tau\ne0).
\]
Both terms are positive semidefinite by the Schur product theorem. The coincidence issue is essential: this decomposition uses \(\tau\ne0\), not a limiting argument at zero.

**2. An exact kernel for the dark term.** For any real orthogonal projector \(F\) and real vector \(f\), setting \(D_f=\operatorname{diag}(f)\) gives
\[
 f^{\mathsf T}(F\circ F)f=\operatorname{tr}(FD_fFD_f)=\|FD_fF\|_F^2.
\]
Hence \(f\in\ker M_{\mathrm{dark}}\) exactly when \(F_jD_fF_j=0\) for all \(j\). If \(f\) is any odd-degree Walsh character, multiplication by \(f\) changes Fourier-weight parity, so \(F_jD_fF_j=0\). Thus \(\mathcal O\) lies in the dark kernel.

For the remaining even-Walsh part write \(f=\sum_{|S|\text{ even}}c_S\chi_S\). In the normalized weight-\(j\) Walsh basis \(\{\chi_T/\sqrt N:|T|=j\}\), the compression of \(D_f\) has entries \(C_j(T,U)=c_{T\triangle U}\). Removing the uniform direction \(w_j\) amounts to \(P_jC_jP_j\), where \(P_j=I-\mathbf1\mathbf1^{\mathsf T}/m_j\). Suppose inductively that \(c_S=c_\varnothing\) for all even \(|S|<2j\). The matrix \(D_j=C_j-c_\varnothing\mathbf1\mathbf1^{\mathsf T}\) is symmetric, has zero diagonal, and can be nonzero only for disjoint \(j\)-subsets \(T,U\), in which case \(D_j(T,U)=c_{T\triangle U}-c_\varnothing\). The dark-kernel condition yields \(P_jD_jP_j=0\). Any real symmetric matrix annihilated by this two-sided compression has the form \(\mathbf1a^{\mathsf T}+a\mathbf1^{\mathsf T}\). Since \(D_j(T,T)=0\), every coordinate of \(a\) is zero, hence \(D_j=0\). Every \(2j\)-subset splits into disjoint \(j\)-subsets, implying \(c_S=c_\varnothing\) for all \(|S|=2j\). Induction from \(j=1\) through \(\lfloor d/2\rfloor\) covers all even Fourier weights, also when \(d=1\) (vacuously). Conversely, equal coefficients on every even Walsh character give a matrix multiple of \(\mathbf1\mathbf1^{\mathsf T}\) in every weight space and hence satisfy every dark-kernel equation.

Writing \(h=\sum_{|S|\text{ even}}\chi_S=(N/2)(e_o+e_{(1,\ldots,1)})\), we conclude
\[
\ker M_{\mathrm{dark}}=\mathcal O\oplus\operatorname{span}\{h\},\quad
\operatorname{ran}M_{\mathrm{dark}}=\mathcal E\cap h^\perp,\quad
\operatorname{rank}M_{\mathrm{dark}}=N/2-1,
\]
where \(\mathcal E\) is the even-degree Walsh space. The last equality holds for all \(d\ge1\).

**3. Bright intensities span all radial functions.** Every \(B_s\) is rank one with a radial eigenvector. Therefore the vectors \(\operatorname{diag}B_s\) are radial and \(\operatorname{ran}M_{\mathrm{bright}}\subseteq\mathcal R\). To prove equality consider the odd diagonal moment vectors \(v_r(x)=(H_\tau^{2r+1})_{xx}\), \(r=0,\ldots,d\). A closed walk contributing to an odd diagonal moment must take an odd number of on-site-potential steps at the marked root, because ordinary cube edges form a bipartite graph. If \(|x|=k>r\), reaching the root, using a potential step, and returning requires at least \(2k+1>2r+1\) steps, hence \(v_r(x)=0\). If \(k=r\), there is precisely one potential step and exactly \(r\) shortest edge steps in each direction. Each leg has \(r!\) orderings, so
\[
 v_r(x)=\tau(r!)^2\quad\text{when }|x|=r.
\]
Consequently the \((d+1)\times(d+1)\) matrix of moments versus Hamming shells has a triangular shape with nonzero diagonal for \(\tau\ne0\), and these \(d+1\) vectors span \(\mathcal R\).

To see why they lie in the bright intensity span, let \(J=\operatorname{diag}((-1)^{|x|})\). On Walsh functions it exchanges weight \(j\) with weight \(d-j\), so \(JF_jJ=F_{d-j}\) while \(\lambda_{d-j}=-\lambda_j\). As conjugation by diagonal \(J\) fixes a matrix diagonal,
\[
 \sum_j\lambda_j^{2r+1}\operatorname{diag}F_j=0.
\]
The spectral expansion of \(H_\tau\) now yields \(v_r=\sum_s\mu_s^{2r+1}\operatorname{diag}B_s\). Since \(M_{\mathrm{bright}}=\sum_s(\operatorname{diag}B_s)(\operatorname{diag}B_s)^{\mathsf T}\), its range is exactly \(\mathcal R\) and its rank is \(d+1\).

**4. Dimension count and the exact marked kernel.** Within the radial space, the even Walsh space has basis \(\sum_{|S|=2j}\chi_S\), for \(0\le j\le\lfloor d/2\rfloor\). Hence \(\dim(\mathcal R\cap\mathcal E)=\lfloor d/2\rfloor+1\). Since \(0\ne h\in\mathcal R\cap\mathcal E\),
\[
 \dim\bigl(\operatorname{ran}M_{\mathrm{dark}}\cap\operatorname{ran}M_{\mathrm{bright}}\bigr)=\lfloor d/2\rfloor.
\]
For PSD matrices the range of their sum is the sum of their ranges, therefore
\[
 \operatorname{rank}\widehat M_\tau=(N/2-1)+(d+1)-\lfloor d/2\rfloor=N/2+\lceil d/2\rceil.
\]
The kernel is the intersection of the two kernels, namely \((\mathcal O\oplus\operatorname{span}\{h\})\cap\mathcal R^\perp=\mathcal O\cap\mathcal R^\perp\), using \(h\in\mathcal R\) and orthogonality of even and odd Walsh functions.

**5. Unmarked boundary.** For \(\tau=0\), the walk factors into one-bit evolutions, and its instantaneous probability matrix is the tensor power of
\[
\begin{pmatrix}\cos^2t&\sin^2t\\\sin^2t&\cos^2t\end{pmatrix}.
\]
The Walsh character \(\chi_S\) has instantaneous probability-matrix eigenvalue \(\cos(2t)^{|S|}\). Its infinite-time average is zero for odd \(|S|\) and equals \(2^{-|S|}\binom{|S|}{|S|/2}>0\) for even \(|S|\). Exactly half of the \(N\) Walsh characters have even weight, so the rank is \(N/2\). This separately resolves the \(\tau=0\) spectral collisions.

## Verification

The included `VERIFY.py` is a standalone Python 3 checker using NumPy and SymPy; run `python3 VERIFY.py`. Its reported output is:

```
VERIFY_OK exact_dark_profiles=5 moment_identities=54 spectral_profiles=30 matrix_entries=28664 cube_orders=1..6
```

It reconstructs the dark projectors with exact rational arithmetic in dimensions \(1\) through \(5\), checks the triangular odd-moment identities exactly in dimensions \(1\) through \(4\), and independently computes spectral projector sums for dimensions \(1\) through \(6\) and five zero/nonzero signed potentials. These are finite corroborations; the theorem for all dimensions and all nonzero real potentials follows from the proof above.

## Relationship to prior work

Coutinho, Baptista, Godsil, Spier and Werner develop exact average-mixing machinery for quantum walks in *Irrational quantum walks* [1], which motivates the Cesàro-matrix invariant used here. Coutinho, Godsil, Guo and Zhan relate average-mixing rank to commutant projections [2]; that is a general framework rather than this marked-hypercube rank and kernel law. Moore and Russell analyze unmarked continuous-time hypercube walks and their mixing phenomena [3]. Lugão, Portugal, Sabri and Tanaka provide methods for continuous-time search Hamiltonians with marked vertices [4], but study search performance rather than the rank of the all-start Cesàro mixing matrix. Mohan and Zhan analyze average vertex mixing under a discrete-time marked-vertex walk [5], with different evolution and Hilbert space. The present result combines the marked rank-one Hamiltonian with the complete dark/bright projector and Walsh-kernel classification.

## Limitations

This theorem does not cover two or more marked sites, nonuniform edge weights, arbitrary Hamming alphabets, or other Hamiltonians. It is an exact result for infinite-time averaged *probability matrices*, not a bound on finite-time convergence or a search-success probability. The supplied finite checks do not certify arbitrary dimensions. Originality remains subject to the possibility that a stronger previously published rank-one perturbation or association-scheme theorem implies the same rank and kernel classification; the inspected related papers did not yield such an implication. No independent mathematical audit has been performed.

## References

1. Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier, Reinhard Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (first public 2022-08-18), https://arxiv.org/abs/2208.08971.
2. Gabriel Coutinho, Chris Godsil, Krystal Guo, Hanmeng Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591v1 (2017), https://arxiv.org/abs/1709.03591.
3. Cristopher Moore, Alexander Russell, *Quantum Walks on the Hypercube*, arXiv:quant-ph/0104137 (2001), https://arxiv.org/abs/quant-ph/0104137.
4. Pedro H. G. Lugão, Renato Portugal, Mohamed Sabri, Hajime Tanaka, *Multimarked Spatial Search by Continuous-Time Quantum Walk*, arXiv:2203.14384 (2022), https://arxiv.org/abs/2203.14384.
5. Mohan and Zhan, *Discrete Quantum Walks with Marked Vertices and Their Average Vertex Mixing Matrices*, arXiv:2411.16676 (2024), https://arxiv.org/abs/2411.16676.
