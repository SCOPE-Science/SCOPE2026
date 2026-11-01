# Quarter-cycle delay and exact heat-Lipschitz decay on finite cycles

## Finding
For every integer \(n\ge7\), let \(C_n\) be the unit-edge cycle, let \(L=D-A\) be its combinatorial graph Laplacian, and let \(H_t=e^{-tL}\). Write \(p_t(j)=H_t(0,j)\), \(d(j)=\min\{j,n-j\}\), and \(R_k(t)=\sum_{d(j)>k}p_t(j)\). The **attained sharp graph-Lipschitz operator seminorm** \(\Lambda_n(t)\), for every \(t\ge0\), is

\[
\Lambda_n(t)=W_1(H_t(0,\cdot),H_t(1,\cdot))
=\min_{c\in\mathbb R}\sum_{j=0}^{n-1}|p_t(j)-c|.
\]

Here \(W_1\) uses the original cycle shortest-path metric. If \(n=4r+a\), with \(a\in\{0,1,2,3\}\), then the exact closed profile is

\[
\Lambda_n(t)=\begin{cases}
1-2p_t(r)-2R_r(t),&a=0,\\
1-p_t(r)-2R_r(t),&a=1,\\
1-2R_r(t),&a=2,\\
1-3p_t(r+1)-2R_{r+1}(t),&a=3.
\end{cases}
\]

The heat kernel has the explicit finite spectral formula

\[
p_t(j)=\frac1n\sum_{\ell=0}^{n-1}
\exp\!\left(-4t\sin^2\!\frac{\pi\ell}{n}\right)
\cos\!\frac{2\pi\ell j}{n}.
\]

These expressions are valid at \(t=0\) by continuity and are strictly between zero and one for every \(t>0\). In particular, \(\Lambda_n(0)=1\) and \(\Lambda_n(t)<1\) at every positive time. Its first nonzero short-time contraction term has the **quarter-cycle order**

\[
1-\Lambda_n(t)=\frac{b_a}{k_n!}t^{k_n}+O_n(t^{k_n+1}),\qquad
k_n=\left\lfloor\frac{n+2}{4}\right\rfloor,
\qquad (b_0,b_1,b_2,b_3)=(2,1,4,3).
\]

Thus the contraction is genuinely flat to every order below \(k_n\), even though the norm is strictly contracting at every positive time. Let \(\lambda_1=4\sin^2(\pi/n)\) and \(\lambda_2=4\sin^2(2\pi/n)\). At large times,

\[
\Lambda_n(t)=c_n e^{-\lambda_1t}+O_n(e^{-\lambda_2t}),
\qquad
c_n=\begin{cases}
\frac4n\cot(\pi/n),&n\equiv0\pmod4,\\
\frac2n\bigl[\csc(\pi/(2n))-\sin(\pi/(2n))\bigr],&n\text{ odd},\\
\frac4{n\sin(\pi/n)},&n\equiv2\pmod4.
\end{cases}
\]

In all residue classes \(c_n\to4/\pi\) as \(n\to\infty\). The full-time profile, four-residue higher-order onset, and spectral amplitude are asserted as a single theorem; the general median-flow identity itself is earlier literature, not claimed new.

## Assumptions and scope
The graph has precisely \(n\ge7\) vertices labeled by \(\mathbb Z/n\mathbb Z\), each edge has length and conductance one, and the positive Laplacian is \(Lf(j)=2f(j)-f(j-1)-f(j+1)\). The seminorm is \(\operatorname{Lip}(f)=\max_j|f(j)-f(j+1)|\) on real functions modulo constants. The operator norm is the supremum of \(\operatorname{Lip}(H_tf)/\operatorname{Lip}(f)\) over nonconstant real \(f\). Time is any real \(t\ge0\); no degree normalization is used.

## Proof
**1. Exact operator–transport duality.** For a finite graph, the Kantorovich–Rubinstein dual expresses the transport distance between two probability rows as the supremum of their integral difference against \(1\)-Lipschitz functions. The graph-Lipschitz seminorm is the maximum over edges, so exchanging a finite edge maximum with a supremum gives the operator norm as the maximum neighbor-row \(W_1\) distance. Cycle rotations make all neighbor distances identical. The maximum is attained since the Lipschitz unit ball modulo constants is compact.

**2. Circular circulation.** For the adjacent rows \(\mu_j=p_t(j)\) and \(\nu_j=p_t(j-1)\), their difference is \(p_t(j)-p_t(j-1)\). A signed flow along the oriented edge \(j\to j+1\) with this divergence necessarily has the form \(g_j=p_t(j)-c\) for one real \(c\). The minimum total absolute flow is the graph-metric \(W_1\) distance: any transport path yields a feasible edge flow of no larger cost, while decomposing a feasible signed flow into paths and deleting circulation yields a transport plan of no greater cost. Equivalently, finite-dimensional linear-programming duality gives the same equality. Hence \(W_1=\min_c\sum_j|p_t(j)-c|\). An optimal \(c\) is a median of the \(n\) kernel entries. The circular median formula is also the established result of Delon–Rabin–Gousseau, equation (12) in the cited paper; it is not independently claimed here.

**3. Strict radial ordering.** Put \(m=\lfloor n/2\rfloor\) and \(q_d(t)=p_t(d)\) for \(0\le d\le m\). The heat equation gives \(q_0'=2(q_1-q_0)\), \(q_d'=q_{d-1}+q_{d+1}-2q_d\) for interior radial indices, and \(q_m'=q_{m-1}-q_m\) when \(n\) is odd or \(q_m'=2(q_{m-1}-q_m)\) when even. For \(z_d=q_d-q_{d+1}\), the first equation is \(z_0'=-3z_0+z_1\); all intermediate equations are \(z_d'=z_{d-1}-2z_d+z_{d+1}\); the final equation is \(z_{m-1}'=z_{m-2}-2z_{m-1}\) (odd) or \(z_{m-1}'=z_{m-2}-3z_{m-1}\) (even). This is an irreducible cooperative tridiagonal linear system, initialized at \(z_0(0)=1\) and all other \(z_d(0)=0\). Its exponential is strictly positive for positive times by the path expansion with a sufficiently large positive diagonal shift. Thus \(q_0(t)>q_1(t)>\cdots>q_m(t)>0\) for \(t>0\).

**4. The four median cuts.** The radial values have multiplicities one at zero, two at each intermediate distance, and (only when \(n\) is even) one at the antipode. For \(n=4r\), a median is \(q_r\), with \(2r-1\) strictly larger and \(2r-1\) strictly smaller entries. For \(n=4r+1\), a median is \(q_r\), with \(2r-1\) larger and \(2r\) smaller entries. For \(n=4r+2\), any value between \(q_r\) and \(q_{r+1}\) is a median, with \(2r+1\) entries on each side. For \(n=4r+3\), a median is \(q_{r+1}\), with \(2r+1\) larger and \(2r\) smaller entries. Expanding the absolute values, using \(\sum_jp_t(j)=1\), gives the displayed four expressions. They are sharp since median minimization is exact. Every contraction deficit is positive for \(t>0\), as all kernel entries are positive.

**5. Exact first nonzero Taylor term.** The continuous-time walk is generated by \(Q=-L\). For any distance \(1\le d< n/2\), the first nonzero coefficient of \(p_t(d)=\sum_{h\ge0}t^h(Q^h)_{0d}/h!\) occurs at order \(d\): a shortest walk uses precisely \(d\) forward hops, so \(p_t(d)=t^d/d!+O_n(t^{d+1})\). The relevant cut radii \(r\) or \(r+1\) are less than \(n/2\) for \(n\ge7\). Their more distant tails start one order later. The four formulas therefore yield respectively \(2t^r/r!\), \(t^r/r!\), \(4t^{r+1}/(r+1)!\) (two vertices at that distance, each with coefficient one), and \(3t^{r+1}/(r+1)!\), plus higher orders. The coefficients are nonzero, proving the exact order \(k_n\) and excluding any lower-order term.

**6. Exact long-time coefficient.** The cycle Fourier characters diagonalize \(L\), with eigenvalues \(4\sin^2(\pi\ell/n)\). The two lowest nonconstant modes contribute \((2/n)e^{-\lambda_1t}\cos(2\pi j/n)\) to the kernel, and all remaining modes decay at least as \(e^{-\lambda_2t}\). Because the radial order is fixed, the median formula is a fixed linear functional of the kernel, so its leading coefficient is \((2/n)\min_c\sum_j|\cos(2\pi j/n)-c|\). For clarity, set \(\theta=\pi/n\), and write \(S\) for the sum of the cosine values strictly greater than a median (counting multiplicity). If \(n=4r\), the total median absolute deviation is \(2[1+2\sum_{j=1}^{r-1}\cos(2j\theta)]=2\cot\theta\). If \(n=4r+2\), it is \(2[1+2\sum_{j=1}^{r}\cos(2j\theta)]=2\csc\theta\). For \(n=4r+1\), the median is \(\sin(\theta/2)\), \(S=1+2\sum_{j=1}^{r-1}\cos(2j\theta)\), and the deviation is \(2S+3\sin(\theta/2)=\csc(\theta/2)-\sin(\theta/2)\). For \(n=4r+3\), the median is \(-\sin(\theta/2)\), \(S=1+2\sum_{j=1}^{r}\cos(2j\theta)\), and the deviation is \(2S-\sin(\theta/2)=\csc(\theta/2)-\sin(\theta/2)\). The equalities use \(1+2\sum_{j=1}^{h}\cos(2j\theta)=\sin((2h+1)\theta)/\sin\theta\). Multiplication by \(2/n\) gives precisely the three displayed amplitudes; small-angle expansions give the common limit \(4/\pi\). This proves the claimed all-time and asymptotic statements.

## Verification
The standalone `verify_cycle.py` uses only the Python standard library. It independently optimizes the Lipschitz dual through dynamic programming over integral edge slopes (without using the median) for 132 heat-kernel instances on cycles from three through twenty-four vertices, then compares the result with both the median formula and four-residue formula. It verifies 78 long-time spectral amplitudes directly from the first Fourier mode, and 897 exact integer Taylor-coefficient conditions for sizes three through eighty. Successful execution prints `CHECK_OK cycle_sizes=78 spectral_coefficients=78 heat_dual_instances=132 exact_Taylor_coefficients=897`. These finite computations do not establish the unrestricted theorem; the preceding proof does.

## Relationship to prior work
Ollivier's coarse Ricci curvature framework (first publicly posted 30 January 2007) treats contraction of Markov kernels in graph-metric \(W_1\). Delon, Rabin, and Gousseau (first publicly posted 30 June 2009) give the general circular histogram median formula; that identity is a prior result and the present proof explicitly relies on it. Münch and Wojciechowski (2017) establish a general equivalence between graph curvature bounds and heat-semigroup Lipschitz estimates, but their semigroup characterization gives exponential bounds rather than this cycle-specific exact profile, high-order four-residue short-time law, and explicit long-time constants. Previously catalogued sharp heat transport on the six-cycle is a boundary case, not part of the novelty claim restricted to \(n\ge7\). The claimed contribution is this combined all-size exact heat-semigroup theorem and its high-order and spectral deductions, not circular transport duality or Fourier diagonalization separately.

## Limitations
No formula is claimed for edge-weighted cycles, degree-normalized generators on irregular graphs, graphs other than simple cycles, or Wasserstein orders different from one. The eigenmode asymptotic concerns fixed \(n\) followed by large time; the limit \(n\to\infty\) applies only to its leading coefficient, not to a joint time–size scaling limit. Prior general circular-transport formulas make the median identity known; an unindexed direct calculation of the combined heat-profile or order law remains a publication-priority possibility. No independent audit has been performed.

## References
1. Yann Ollivier, *Ricci curvature of Markov chains on metric spaces*, arXiv:math/0701886, first version 30 January 2007, Journal of Functional Analysis 256 (2009), 810–864. https://arxiv.org/abs/math/0701886
2. Julie Delon, Julien Rabin, Yann Gousseau, *Transportation Distances on the Circle and Applications*, arXiv:0906.5499, first version 30 June 2009, especially Section 2.2.3, equation (12). https://arxiv.org/abs/0906.5499
3. Florentin Münch and Radosław K. Wojciechowski, *Ollivier Ricci curvature for general graph Laplacians: Heat equation, Laplacian comparison, non-explosion and diameter bounds*, arXiv:1712.00875, first version 4 December 2017, especially Theorem 3.8. https://arxiv.org/abs/1712.00875
