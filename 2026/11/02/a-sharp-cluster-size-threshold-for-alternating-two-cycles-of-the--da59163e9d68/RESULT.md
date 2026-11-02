# A sharp cluster-size threshold for alternating two-cycles of the discrete Kuramoto map

## Finding
For each integer \(N\ge2\) and coupling \(2<\kappa<\pi\), the identical-frequency, zero-phase-lag, all-to-all discrete Kuramoto map possesses an explicit alternating period-two solution for every nontrivial partition of its oscillators into two internally synchronized groups. The exact transverse Floquet spectrum depends only on the group sizes and the unique \(u\in(0,\pi/2)\) satisfying \(\kappa\sin u=2u\). The orbit is exponentially attracting modulo common phase rotation precisely when
\[
\frac{\max(m,N-m)}{N}<p_*(\kappa),\qquad
p_*(\kappa)=\frac{\sin u-u\cos u}{u(1-\cos u)}.
\]
It has a transverse unstable direction when this inequality is reversed, and a unit-modulus transverse multiplier at equality. The sharp threshold decreases strictly from \(2/3\) toward \(2/\pi\) as \(\kappa\) varies from \(2\) toward \(\pi\). Thus three oscillators uniquely lack an attracting two-block member of this family, while for two oscillators and every size at least four, a balanced partition generates an attracting member throughout \(2<\kappa<\pi\).

## Assumptions and scope
Let \(N\ge2\) be an integer and let \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). The map is
\[
F_\kappa(\theta)_i=\theta_i+\frac{\kappa}{N}\sum_{j=1}^N\sin(\theta_j-\theta_i)\pmod{2\pi},
\qquad i=1,\ldots,N.
\]
It is the identical-frequency, zero-phase-lag specialization of the discrete Kuramoto network; changing a common natural frequency only adds a common phase drift and is not included in the literal period-two claim. Fix \(2<\kappa<\pi\), and a partition of index set into nonempty blocks \(A,B\) with \(|A|=m\), \(|B|=n=N-m\). Put \(p=m/N\) and \(q=n/N\). There exists precisely one \(u\in(0,\pi/2)\) such that \(\kappa=2u/\sin u\). For arbitrary \(\phi\in\mathbb T\), define
\[
\theta^{(0)}_i=\begin{cases}\phi+qu&i\in A,\\\phi-pu&i\in B,\end{cases}\qquad
\theta^{(1)}_i=\begin{cases}\phi-qu&i\in A,\\\phi+pu&i\in B.\end{cases}
\]
The claim concerns the two-cycle \(\theta^{(0)}\leftrightarrow\theta^{(1)}\), its complete linear spectrum, and normal exponential attraction or instability relative to the common-rotation circle. No assertion is made for \(\kappa\notin(2,\pi)\), nonidentical frequencies, nonzero lag, or other dynamical attractors.

## Proof
**Existence and uniqueness.** For \(0<u<\pi/2\), the function \(2u/\sin u\) increases strictly from \(2\) to \(\pi\), since its derivative has numerator \(2(\sin u-u\cos u)>0\). Hence there is a unique solution for each stated coupling. At the first configuration, the map moves every oscillator in \(A\) by \(-\kappa q\sin u=-2qu\) and every oscillator in \(B\) by \(+\kappa p\sin u=+2pu\). It therefore exchanges the two configurations exactly. At the second configuration the updates have opposite signs, so the map exchanges them back. The relative group phase difference is \(+u\) then \(-u\), which are distinct modulo \(2\pi\). Thus the orbit has least period two, not merely relative period two.

**All Floquet multipliers.** At either configuration the Jacobian has entries \((\kappa/N)\cos(\theta_j-\theta_i)\) off diagonal and diagonal entries equal to one minus the sum of the off-diagonal entries of that row. Intra-block phase differences vanish, inter-block phase differences are \(\pm u\), and cosine is even; consequently both Jacobian matrices are exactly the same symmetric matrix \(J\). Its invariant orthogonal decomposition comprises the common-rotation direction, the inter-block-constant zero-mean direction, and the two spaces of zero-sum internal block perturbations. Direct row summation gives eigenvalues respectively
\[
1,\quad 1-\kappa\cos u,\quad
1-\kappa(p+q\cos u)\text{ (multiplicity }m-1\text{)},\quad
1-\kappa(q+p\cos u)\text{ (multiplicity }n-1\text{)}.
\]
The period-two monodromy is \(J^2\), so the corresponding four multipliers are the squares of these quantities, with the stated multiplicities. When a block has size one its internal perturbation space has dimension zero.

**Sharp stability criterion.** From \(\kappa=2u/\sin u\),
\[
0<\kappa\cos u=2u\cot u<2,
\]
so the inter-block multiplier has modulus strictly below one. Since \(0<\cos u<1\), both internal-mode exponents lie below one (before squaring) and exceed \(-1\) if and only if
\[
p<\frac{2/\kappa-\cos u}{1-\cos u}=p_*(\kappa),\qquad
q<p_*(\kappa),
\]
for whichever internal modes exist. The missing-mode caveat cannot invalidate the combined criterion: \(p_*(\kappa)>2/\pi>1/2\), proved below, whereas the proportion of a singleton block is at most one half. Thus normal exponential attraction is equivalent to \(\max(p,q)<p_*\). When the maximum exceeds \(p_*\), the associated block necessarily has at least two members, and its internal Jacobian eigenvalue is smaller than \(-1\), yielding an expanding Floquet direction. Equality gives the real Jacobian eigenvalue \(-1\) and Floquet multiplier \(+1\), hence nonhyperbolicity. Smoothness and the invariant rotation symmetry imply local exponential attraction modulo the rotational circle whenever all nontrivial multipliers lie strictly inside the unit circle.

**Monotone threshold and size gap.** A useful exact integral representation is
\[
p_*(u)=\frac{\int_0^1 s\sin(us)\,ds}{\int_0^1\sin(us)\,ds},\quad 0<u<\pi/2.
\]
With respect to the strictly positive probability density proportional to \(\sin(us)\) on \((0,1)\), differentiation gives
\[
\frac{d p_*}{du}=\operatorname{Cov}\bigl(s,s\cot(us)\bigr)<0.
\]
Indeed, \(s\) is increasing while \(s\cot(us)\) is strictly decreasing, because its derivative has numerator \(\sin(us)\cos(us)-us<0\). The strict reversed covariance inequality follows by integrating the product of differences over two independent points. Dominated convergence at the endpoints yields
\[
\lim_{u\downarrow0}p_*(u)=\frac23,
\qquad \lim_{u\uparrow\pi/2}p_*(u)=\frac2\pi.
\]
Therefore \(2/\pi<p_*<2/3\). For \(N=3\), every bipartition has majority proportion \(2/3\), hence is transversely unstable. For \(N=2\), a bipartition contains two singletons and the sole nontrivial inter-block multiplier is contracting. For every \(N\ge4\), choose a balanced bipartition: its maximum fraction is at most \(3/5<2/\pi\), so its orbit is normally exponentially attracting for every stated coupling.

## Verification
The companion `check_clusters.py` directly iterates the original vector map, constructs its actual full Jacobian matrices, and compares the directly computed two-step eigenvalues with the claimed closed-form spectrum for several integer sizes, partitions, and couplings. It also checks the strict stability criterion against the full computed transverse spectral radius. Run with `python check_clusters.py` using Python 3, NumPy and SciPy. These finite computations are cross-checks, not the proof of the all-size statement; that proof is the block decomposition and analytic covariance argument above.

## Relationship to prior work
Zhai, Xiao and Zheng (2023) examine sinusoidally coupled discrete circle maps, explicitly analyze the two-oscillator sine-circle reduction, and describe period doubling and two-phase-cluster formation near the loss of synchronization using numerical simulations. These phenomena, the onset of period doubling, and the basic sine-circle reduction are therefore not claimed as new. Gade and Gupta (2026) formulate a globally coupled phase-lag discrete Kuramoto model and analyze onset of synchronization and finite-system dynamics. The present statement isolates the zero-lag equal-frequency finite-system slice and supplies an exact bipartition-dependent **full transverse Floquet classification**, a strictly monotone sharp partition threshold, and the exceptional three-oscillator outcome. The 2026 paper's full text was not obtainable for direct comparison; its accessible abstract emphasizes incoherent-state linear stability rather than this particular finite-cluster theorem, so historical priority remains a residual uncertainty.

## Limitations
The theorem is local to the explicit alternating two-cluster branch and excludes other orbits, other couplings, phase lags, and heterogeneous frequency distributions. At equality of the threshold it proves nonhyperbolicity, not nonlinear stability or instability. Near \(\kappa=2\) and \(\kappa=\pi\) the open-interval conclusion is not extended to either endpoint. A full-text comparison with the 2026 motivating paper and independent mathematical review remain outstanding.

## References
1. P. M. Gade and S. Gupta, *Discrete-time Kuramoto model with phase lag: Linear stability analysis and onset of synchronization*, arXiv:2609.22715v1 (first posted September 19, 2026), https://arxiv.org/abs/2609.22715.
2. Y. Zhai, J. Xiao and Z. Zheng, *Synchronization–desynchronization transitions in networks of circle maps with sinusoidal coupling*, Chinese Physics B 32 (2023), 060505, DOI:10.1088/1674-1056/acc062, https://www.cpsjournals.cn/en/article/doi/10.1088/1674-1056/acc062.
