# A seven-vertex reversal in optimal two-anchor Kuramoto-ring coherence

## Finding

For every integer \(N\ge4\), pin two distinct vertices of the unweighted cycle \(C_N\) at phase zero. The remaining \(M=N-2\) oscillators have nearest-neighbor Kuramoto coupling \(g>0\) and independent static natural-frequency offsets \(\epsilon\xi_i\), where the \(\xi_i\) are bounded, independent, mean-zero, unit-variance real variables. For each fixed \(N\), let \(\theta^*(\epsilon,\xi)\) denote the locally unique, stable, phase-locked equilibrium near zero, and define the *unpinned-subpopulation* coherence
\[
R_{\mathcal M}(\epsilon,\xi)=\left|\frac1M\sum_{i\in\mathcal M}e^{\mathrm i\theta_i^*(\epsilon,\xi)}\right|.
\]
Let \(\ell\in\{0,\ldots,M\}\) be the number of unpinned vertices on one of the two arcs between the anchors; the other arc has \(M-\ell\) vertices. Then
\[
1-\mathbb E R_{\mathcal M}(\epsilon,\xi)
=\frac{\epsilon^2}{2Mg^2}\,\mathcal C_M(\ell)+O_N(\epsilon^4),
\]
where, with \(y=\ell(M-\ell)\),
\[
\boxed{\;
\mathcal C_M(\ell)=
\frac{(M-1)(M+2)(M^2+6)}{360}
+\frac{-M^3+12M^2+22M+60}{360M}\,y
-\frac{7M+30}{360M}\,y^2.
\;}
\]
This exact coefficient has a complete global minimizer classification:

- For \(N=4,5,6\), precisely *adjacent* anchors (\(\ell=0\) or \(M\)) maximize weak-disorder coherence to leading order.
- For every \(N\ge7\), precisely the anchors splitting the two unpinned arcs as equally as possible (\(\ell=\lfloor M/2\rfloor\) or \(\lceil M/2\rceil\)) do so.

"Precisely" is modulo cycle rotation and reversal. Since there are finitely many arrangements for fixed \(N\), and the leading minimizer is strict against every inequivalent placement, the same maximizing arrangements also hold for the *actual expected nonlinear order parameter* for all sufficiently small nonzero \(|\epsilon|\) (with the permitted threshold depending on \(N\), \(g\), and the frequency distribution). No assertion is made for arbitrary disorder strength. The change occurs sharply between six and seven vertices: at \(N=6\), clustered and balanced coefficients are \(11/10\) and \(11/9\), respectively; at \(N=7\), they are \(217/90\) and \(407/180\). In contrast, the fixed-reference tracking coefficient \(\mathbb E\|\theta^*\|^2\) is minimized by balanced anchors for *all* \(N\ge4\).

## Assumptions and scope

The graph is the simple undirected cycle with \(N\ge4\) vertices and unit edge weights. Exactly two vertices are pinned at phase zero, modeling the strictly infinite-reset-rate (permanently grounded) limit. The free phases satisfy the *nonlinear* deterministic Kuramoto equations
\[
\dot\theta_i=\epsilon\xi_i+g\sum_{j\sim i}\sin(\theta_j-\theta_i),
\qquad i\in\mathcal M,
\]
with pinned neighbor phases identically zero. The coupling \(g>0\) is the per-edge coupling; it equals \(K/N\) under the normalization used in the motivating network-resetting model. The frequency variables are quenched (sampled once and then held fixed), not time-dependent white-noise forcing. Their distributions need not be symmetric, but they have bounded support, zero mean, unit variance, and independence. The asymptotic takes \(\epsilon\to0\) at fixed \(N\) and \(g\). No uniformity in \(N\), finite reset rate, or arbitrary locked branches is asserted.

When \(\ell=0\), the corresponding Dirichlet block is empty; all trace and quadratic contributions from it are defined to be zero. Coherence is measured *only among the unpinned vertices* and subtracts their collective phase through the complex modulus. It is not the tracking error to the pinned phase and not the all-vertex order parameter.

## Proof

**1. Small-frequency stationary branch.** Delete the two pinned vertices from the cycle Laplacian and call the resulting positive-definite grounded Laplacian \(L_g\). The derivative of the stationary Kuramoto force at zero is \(-gL_g\), which is strictly negative definite. The analytic implicit-function theorem gives a unique real-analytic equilibrium branch near zero, stable by continuity. The sine force is odd, so
\[
\theta^*(\epsilon,\xi)=\frac{\epsilon}{g}L_g^{-1}\xi+O_N(\epsilon^3),
\qquad
\theta^*(-\epsilon,\xi)=-\theta^*(\epsilon,\xi).
\]
Bounded frequency support and finiteness of the graph give uniform expansions over all allowed \(\xi\), for sufficiently small \(|\epsilon|\).

**2. The centered phase observable.** For \(\theta\) close to zero, with \(\bar\theta=M^{-1}\sum_i\theta_i\) and \(P=I_M-\boldsymbol1\boldsymbol1^{\mathsf T}/M\), direct Taylor expansion of the complex modulus gives
\[
\left|M^{-1}\sum_i e^{\mathrm i\theta_i}\right|
=1-\frac{1}{2M}\theta^{\mathsf T}P\theta+O(\|\theta\|^4).
\]
The modulus and the stationary branch are even under simultaneous sign reversal of \(\epsilon\); consequently the integrated remainder in the weak-disorder expansion is \(O_N(\epsilon^4)\). Independence, zero means and unit variances imply \(\mathbb E[\xi\xi^{\mathsf T}]=I_M\), whence
\[
\mathcal C_M(\ell)=\operatorname{tr}(L_g^{-1}PL_g^{-1})
=\operatorname{tr}(L_g^{-2})
-\frac1M\boldsymbol1^{\mathsf T}L_g^{-2}\boldsymbol1.
\]

**3. Exact Green functions on the two arcs.** The grounded matrix decomposes as \(L_g=T_\ell\oplus T_{M-\ell}\), where \(T_n\) is the \(n\)-by-\(n\) Dirichlet tridiagonal matrix with diagonal \(2\), nearest off-diagonal \(-1\), and \(T_0\) the empty block. For \(n\ge1\), its inverse is
\[
(T_n^{-1})_{ij}=\frac{\min(i,j)(n+1-\max(i,j))}{n+1},
\quad 1\le i,j\le n.
\]
In particular \((T_n^{-1}\boldsymbol1)_i=i(n+1-i)/2\). Elementary sums of powers, including the double sum of squares of the displayed inverse kernel, yield
\[
F(n):=\operatorname{tr}(T_n^{-2})
=\frac{n(n+2)(2n^2+4n+9)}{180},
\]
\[
H(n):=\boldsymbol1^{\mathsf T}T_n^{-2}\boldsymbol1
=\frac{n(n+1)(n+2)(n^2+2n+2)}{120},
\]
also valid at \(n=0\). Therefore
\[
\mathcal C_M(\ell)
=F(\ell)+F(M-\ell)
-\frac{H(\ell)+H(M-\ell)}M.
\]
Expansion in the elementary symmetric variable \(y=\ell(M-\ell)\) gives precisely the polynomial displayed under Finding.

**4. Exhaustive global optimization, not a finite search.** Since \(0\le y\le Y_M:=\lfloor M^2/4\rfloor\), the coefficient of \(y^2\) in \(\mathcal C_M(y)\) is \(-(7M+30)/(360M)<0\). Hence this is *strictly concave* in \(y\). Every interior value strictly exceeds the chord joining the endpoint values, so the global minimum over all integer arc partitions is attained only at either \(y=0\) (adjacent pins) or \(y=Y_M\) (balanced pins). No intermediate geometry can tie.

For even \(M\), subtraction of the balanced value from the adjacent value gives
\[
\mathcal C_M(0)-\mathcal C_M(Y_M)
=\frac{M(11M^3-18M^2-88M-240)}{5760}.
\]
For odd \(M\), the corresponding difference is
\[
\frac{(M-1)(M+1)(11M^3-18M^2-95M-270)}{5760M}.
\]
The relevant cubic is negative at \(M=2,3,4\) and positive at every integer \(M\ge5\) of the corresponding parity. Indeed both cubics are strictly increasing for \(M\ge3\), and their signs at the last small integer and first large integer establish the stated partition without missing a root or equality. Thus adjacent anchors uniquely minimize for \(N=4,5,6\), while balanced anchors uniquely minimize for \(N\ge7\). Since the order-\(\epsilon^4\) remainder is uniform over the finitely many placements at each fixed \(N\), strict coefficient gaps imply this ordering for the actual expected order parameter at sufficiently small nonzero \(\epsilon\).

**5. The observable matters.** If instead the squared stationary phase is measured from the fixed pin reference, the leading coefficient is \(F(\ell)+F(M-\ell)\). Its second centered integer difference equals
\[
F(n+1)-2F(n)+F(n-1)=\frac{12n^2+24n+19}{90}>0
\quad(n\ge1),
\]
so balancing minimizes that different quantity for all \(N\ge4\). In particular, the small-cycle reversal is caused by the collective-mean subtraction in the physical subpopulation order parameter, not by an alternative convention for edge coupling.

## Verification

The standalone `verify.py` implements independent exact rational matrix inverses for Dirichlet chains, checks both polynomial Green sums, and symbolically verifies the reduction to a strictly concave quadratic in \(y\). It exhausts all distinct two-pin placements for \(4\le N\le30\) using the full grounded matrix and centered projection; it also compares fixed-reference tracking and, when SciPy is installed, solves sample nonlinear sine-coupled stationary equations at two small disorder amplitudes. The script prints `PASS: 355 deterministic algebraic, graph, and local-equilibrium tests` in the checked Python environment. Finite checks are not the proof for arbitrary \(N\); the Green identity and polynomial-concavity argument establish that part.

Reproduce from the supplied files with `python verify.py`. The exact tests require SymPy; numerical regression checks additionally use NumPy and SciPy and are skipped if these are not installed.

## Relationship to prior work

Paramero-Arias and Riascos, arXiv:2610.21842 (first posted 2026-10-15), derive the pinned-subsystem grounded-Laplacian linearization of network Kuramoto synchronization and the general mean-centered quadratic order-parameter expression. Both reductions are prior work. The added conclusion is the *complete two-anchor cycle optimization for the unpinned-only nonlinear local order parameter* and its unexpected exact size threshold \(N=7\).

Fitch and Leonard, arXiv:1407.1569, and Patterson, McGlohon and Dyagilev, arXiv:1412.6595, obtain uniform leader-spacing conclusions for a different noise-driven fixed-reference tracking criterion involving \(\operatorname{tr}(L_g^{-1})\). Patterson, Yi and Zhang, arXiv:1708.06873, similarly study resistance-distance performance of noisy leader-follower systems. None of those inspected fixed-reference results gives this mean-centered, static-frequency \(\operatorname{tr}(L_g^{-1}PL_g^{-1})\) optimum. The fixed-reference contrast in the present proof explains why the earlier optimal-placement conclusion cannot simply be carried over to the current observable.

## Limitations

The result is for two permanent pins on an unweighted cycle, independent bounded quenched frequency disorder, and the locally stable synchronized branch at sufficiently small disorder for each fixed \(N\). It does not determine global equilibrium selection, arbitrary disorder strength, finite-rate stochastic resetting, arbitrary graph families, or coherence when the pinned vertices are included in the order parameter. A generic prior grounded-Laplacian formula supplies an important starting reduction; the claim is the additional exact finite-size optimization and sign change, not invention of that reduction. Independent mathematical and publication-priority review remain to be performed.

## References

1. K. Paramero-Arias and A. P. Riascos, *Synchronization induced by stochastic subsystem resetting in complex networks*, arXiv:2610.21842 (first public 2026-10-15), https://arxiv.org/abs/2610.21842.
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569 (2014), https://arxiv.org/abs/1407.1569.
3. S. Patterson, N. McGlohon and K. Dyagilev, *Efficient, Optimal \(k\)-Leader Selection for Coherent, One-Dimensional Formations*, arXiv:1412.6595 (2014), https://arxiv.org/abs/1412.6595.
4. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873 (2017), https://arxiv.org/abs/1708.06873.
