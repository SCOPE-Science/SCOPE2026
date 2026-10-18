# Intrinsic-volume fragmentation of cycle graphical zonotopes: Dirichlet and tilted laws

## Finding

Let \(C_n\) be the simple cycle on \(n\ge3\) vertices, with indices interpreted modulo \(n\). Let
\[
Z_n=\sum_{i=1}^{n}[0,e_i-e_{i+1}]\subset H_n:=\{x\in\mathbb R^n:\sum_i x_i=0\}.
\]
The intrinsic Euclidean dimension is \(n-1\). Define \(F(z)=\sum_{s\ge1}\sqrt{s}\,z^s\). For **every** pair of integers \(n\ge3\), \(1\le k\le n\), its intrinsic volumes, with Steiner normalization \(V_0=1\), satisfy the exact identity
\[
\boxed{V_{n-k}(Z_n)=\frac nk[z^n]F(z)^k
=\frac nk\sum_{\substack{s_1+\cdots+s_k=n\\s_i\ge1}}\prod_{i=1}^k\sqrt{s_i}.}\tag{1}
\]
In particular, \(V_{n-1}(Z_n)=n\sqrt n\), \(V_1(Z_n)=n\sqrt2\), and
\[
V_{n-2}(Z_n)=\frac n2\sum_{s=1}^{n-1}\sqrt{s(n-s)}\sim\frac\pi{16}n^3.
\tag{2}
\]
Thus the Euclidean surface area in dimension \(n-1\) is asymptotic to \(\pi n^3/8\).

The coefficient identity has two sharply different geometric fragmentation regimes.

**Fixed number of deleted edges.** For each fixed integer \(k\ge1\),
\[
\boxed{V_{n-k}(Z_n)\sim\frac{\Gamma(3/2)^k}{k\Gamma(3k/2)}n^{3k/2}.}\tag{3}
\]
Select a \(k\)-edge deletion set from \(C_n\) with probability proportional to the \((n-k)\)-dimensional Euclidean parallelotope volume of its surviving edge roots. Independently mark one of the \(k\) deleted edges uniformly, and read the \(k\) positive cyclic gap sizes \((S_1,\ldots,S_k)\) starting there. For fixed \(k\ge2\),
\[
(S_1/n,\ldots,S_k/n)\ \Longrightarrow\ \operatorname{Dirichlet}(3/2,\ldots,3/2).
\tag{4}
\]
The geometric determinant weight changes the ordinary uniform-cut Dirichlet parameter from \(1\) to \(3/2\).

**A positive density of deleted edges.** Let \(k=k(n)\) be integers such that \(k/n\to\alpha\in(0,1)\). Define \(\theta=\theta_{n,k}\in(0,1)\) uniquely by
\[
\mu(\theta):=\frac{\theta F'(\theta)}{F(\theta)}=\frac nk,
\qquad\sigma^2(\theta):=\theta\mu'(\theta)>0.
\]
Then the **sharp** coefficient asymptotic is
\[
\boxed{V_{n-k}(Z_n)=\frac nk\frac{F(\theta)^k\theta^{-n}}{\sqrt{2\pi k\sigma^2(\theta)}}(1+o(1)).}\tag{5}
\]
Moreover \(\theta\to\theta_\alpha\), where \(\mu(\theta_\alpha)=1/\alpha\). For any fixed \(r\ge1\), the first \(r\) cyclic gap sizes converge jointly in distribution to independent positive integer variables with law
\[
\Pr(Y_\alpha=s)=\frac{\sqrt{s}\,\theta_\alpha^s}{F(\theta_\alpha)},\qquad s\in\{1,2,\ldots\}.
\tag{6}
\]
Writing \(M_{n,k}=\max_i S_i\), the largest component in this regime obeys
\[
\boxed{\frac{M_{n,k}}{\log n}\ \xrightarrow{\Pr}\ \frac1{-\log\theta_\alpha}.}\tag{7}
\]
Consequently the volume-biased forest components are macroscopic at every fixed \(k\ge2\), but only logarithmic at every positive deletion density.

## Assumptions and scope

The graph is exactly the unweighted simple cycle \(C_n\), with one oriented generator \(e_i-e_{i+1}\) per undirected edge, and the zonotope uses **segments of length \(\sqrt2\)**, not normalized unit-length edge roots. All intrinsic volumes use the induced metric on \(H_n\) and the standard Steiner convention
\[
\operatorname{vol}_{n-1}(Z_n+tB_{n-1})=\sum_{j=0}^{n-1}\kappa_{n-1-j}V_j(Z_n)t^{n-1-j}.
\]
Here \(\kappa_d\) is the Euclidean unit \(d\)-ball volume, \(\kappa_0=1\). The law on deleted-edge subsets is explicitly **determinant weighted** and is not uniform deletion of edges. The positive-density results require \(0<\alpha<1\) fixed; they do not assert a uniform transition theorem as \(\alpha\downarrow0\) or \(\alpha\uparrow1\).

## Proof

**1. Exact Euclidean forest Gram determinant.** For an edge subset \(A\subseteq E(C_n)\) of size \(j\le n-1\), the surviving graph \(F_A\) is a forest, with component sizes \(s_1,\ldots,s_{n-j}\). Let \(B_A\) be the matrix whose columns are the selected oriented edge roots. For each tree component of size \(s\), the nonzero eigenvalues of its Laplacian \(B_AB_A^{\mathsf T}\) have product \(s\), by the matrix-tree theorem (the component is a tree with one spanning tree). The positive eigenvalues of \(B_A^{\mathsf T}B_A\) coincide with these. Hence
\[
\det(B_A^{\mathsf T}B_A)=\prod_{i=1}^{n-j}s_i,
\quad \operatorname{vol}_j\!\left(\sum_{a\in A}[0,b_a]\right)=\prod_{i=1}^{n-j}\sqrt{s_i}.
\tag{8}
\]
For the empty edge set this determinant is the empty product, equal to one. The established zonotope intrinsic-volume decomposition states that \(V_j\) is the sum of these parallelotope volumes over all \(j\)-element generator subsets. Thus for \(j=n-k\) every term is the indicated product over the \(k\) components after deleting \(k\) cycle edges.

**2. Exact cyclic enumeration.** Mark one of the \(k\) deleted edges and traverse the labelled cycle clockwise. The positive distances between successive deleted edges form a composition \((s_1,\ldots,s_k)\) of \(n\). For each such composition there are exactly \(n\) choices of the marked starting edge. Each unmarked deletion set is counted exactly \(k\) times. The determinant weight in (8) depends only on these distances. Consequently the weighted subset sum is exactly \(n/k\) times the sum over ordered compositions, proving (1) even for \(k=1\) and \(k=n\). The displayed special cases follow by elementary evaluation. For \(k=2\), (2) follows from a Riemann sum and
\[\int_0^1\sqrt{t(1-t)}\,dt=B(3/2,3/2)=\pi/8.\]

**3. Fixed-deletion asymptotic and component law.** For fixed \(k\), divide the summands of (1) by \(n^{k/2}\) and view the positive compositions as a mesh of step \(1/n\) on the standard \((k-1)\)-simplex. The weight \(\prod\sqrt{t_i}\) extends continuously to the closed simplex and vanishes on its proper boundary (when \(k\ge2\)); standard Riemann-sum convergence gives
\[
\sum_{s_1+\cdots+s_k=n}\prod\sqrt{s_i}
\sim n^{3k/2-1}\int_{\substack{t_i\ge0\\\sum t_i=1}}\prod_i t_i^{1/2}\,dt_1\cdots dt_{k-1}
=n^{3k/2-1}\frac{\Gamma(3/2)^k}{\Gamma(3k/2)}.
\]
For \(k=1\) the identity is exact. For \(k\ge2\), the same weighted Riemann sums, tested against any bounded continuous function of the normalized gap vector, yield precisely the Dirichlet density claimed in (4). The marking operation makes the probability of a composition proportional to \(\prod\sqrt{s_i}\); there is no additional size-bias factor.

**4. Positive-density saddle point.** The series \(F\) is absolutely analytic for \(0<z<1\). Define \(p_\theta(s)=\sqrt{s}\theta^s/F(\theta)\). Its mean is \(\mu(\theta)\) and its variance is \(\sigma^2(\theta)\), since \(\theta\mu'(\theta)=\operatorname{Var}_\theta Y>0\). Its mean rises continuously from \(1\) to infinity as \(\theta\) rises from zero to one, so the stated \(\theta_{n,k}\) exists uniquely when \(1\le k<n\). With independent \(Y_i\sim p_\theta\), coefficient extraction gives the **exact** identity
\[
[z^n]F(z)^k=F(\theta)^k\theta^{-n}\Pr_\theta(Y_1+\cdots+Y_k=n).
\tag{9}
\]
If \(k/n\to\alpha\in(0,1)\), the corresponding \(\theta\) remains in a compact subinterval of \((0,1)\). This lattice law has span one (all positive integers occur) and uniformly bounded exponential moments in a neighborhood of the origin. The lattice local central limit theorem at its exact mean \(n=k\mu(\theta)\) yields
\[
\Pr_\theta\!\left(\sum_{i=1}^kY_i=n\right)
=\frac{1+o(1)}{\sqrt{2\pi k\sigma^2(\theta)}}.
\]
Substituting in (9) proves (5). For any fixed \(r\), conditioning on \(\sum_iY_i=n\) changes the joint law of \((Y_1,\ldots,Y_r)\) by the multiplicative factor
\[
\frac{\Pr_\theta(\sum_{i=r+1}^kY_i=n-\sum_{i=1}^r s_i)}{\Pr_\theta(\sum_{i=1}^kY_i=n)},
\]
which tends to one for fixed \(s_1,\ldots,s_r\) by the same local theorem. Tightness and domination then imply (6), since \(\theta\to\theta_\alpha\).

**5. Maximum component at positive density.** Write \(a=-\log\theta_\alpha>0\) and \(N_t=\sum_i\mathbf1_{\{S_i\ge t\}}\). The tilted-law tail satisfies \(\Pr_\theta(Y\ge t)=\Theta(t^{1/2}\theta^t)\), uniformly for \(\theta\) in the above compact interval. The local theorem used in step 4 also shows that the conditioning ratio displayed above is \(1+o(1)\), uniformly when at most two specified gap sizes are \(O(\log k)\). Terms with larger specified sizes can be discarded: the unconditional tail is exponentially small and the unconditional probability of the conditioning event is of order \(k^{-1/2}\). For \(t_+=(1+\varepsilon)\log k/a\), the first moment of \(N_{t_+}\) therefore tends to zero. For \(t_-=(1-\varepsilon)\log k/a\), its first moment diverges, and the two-coordinate conditioning estimate yields \(\mathbb E[N_{t_-}(N_{t_-}-1)]/(\mathbb E N_{t_-})^2\to1\); hence \(\Pr(N_{t_-}=0)\to0\) by the second moment method. Letting \(\varepsilon\downarrow0\) proves (7), since \(\log k/\log n\to1\).

## Verification

A standalone checker `verify_cycle.py` enumerates every edge subset of labelled cycles of orders \(3\) through \(9\), computes the intrinsic parallelotope contribution directly from the Gram determinant of the **actual edge-root vectors**, and compares its sum with the independently computed coefficient in (1) for every \(k\). This gives \(42\) complete finite \((n,k)\) comparisons. It also checks the exact \(C_4\) value and numerical convergence in the fixed-\(k\) and positive-density regimes. The recorded test output includes `VERIFY_OK`; no finite computation is used as a proof of the limiting laws.

Reproduce with `python verify_cycle.py` using Python 3, NumPy and SciPy. The checker is a standalone finite diagnostic and contains no dependency on external package files.

## Relationship to prior work

The all-zonotope intrinsic-volume sum over generator subdeterminants is classical and explicitly available in Joós and Lángi, *Isoperimetric problems for zonotopes* (2022), Corollary 1; Brazitikos and McIntyre, *Vector-Valued Maclaurin Inequalities* (2021), discuss the related wedge-volume and intrinsic-volume identity. Pešović and Stojadinović, *Between graphical zonotope and graph-associahedron* (2022), study the graph-polytopal framework and weighted **face** enumerators, not this Euclidean intrinsic-volume spectrum. All these starting facts are credited, not claimed new.

The assessed finding is the cycle-specific all-rank exact evaluation together with its two distinct **determinant-weighted forest fragmentation laws**, sharp asymptotic constants, positive-density saddle point and logarithmic-largest-component law. The general intrinsic-volume sum does not itself state these cycle-specific evaluated coefficients or limiting probability laws. Previously published cycle-zonotope skeleton spectra and published random-Cayley-tree intrinsic-volume expectations address different invariants and/or different graph ensembles. No claim is made that a failed search constitutes proof of uniqueness across all literature.

## Limitations

This statement concerns unweighted simple cycles with their unscaled type-A edge vectors. Applying length-normalized generators multiplies \(V_j\) by \(2^{-j/2}\); silently switching that normalization is incorrect. The fixed-\(k\) and positive-density limits do not establish uniform asymptotics for every intermediate growth regime. The exact coefficient identity is derived from an established general zonotope formula; its standalone novelty is in the explicit cycle calculation and geometric fragmentation asymptotics, rather than a new general intrinsic-volume decomposition. Independent mathematical validation and comprehensive bibliographic uniqueness assessment have not been performed.

## References

1. S. Brazitikos and F. McIntyre, *Vector-Valued Maclaurin Inequalities*, first public version 2021-02-11, arXiv:2102.05900. https://arxiv.org/abs/2102.05900
2. A. Joós and Z. Lángi, *Isoperimetric problems for zonotopes*, first public version 2022-06-07, arXiv:2206.03204; especially Corollary 1. https://arxiv.org/abs/2206.03204
3. M. Pešović and T. Stojadinović, *Between graphical zonotope and graph-associahedron*, first public version 2022-09-24, arXiv:2209.12053. https://arxiv.org/abs/2209.12053
4. Matrix-tree theorem and the lattice local central limit theorem (classical standard tools); the proofs specify their exact applications.
