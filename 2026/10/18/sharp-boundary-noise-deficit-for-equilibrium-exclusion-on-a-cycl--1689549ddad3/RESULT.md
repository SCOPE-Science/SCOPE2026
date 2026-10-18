# Sharp boundary-noise deficit for equilibrium exclusion on a cycle

## Finding
Consider the symmetric simple exclusion process on a periodic ring with \(n\ge3\) sites, exactly \(1\le k<n\) particles, and each allowed nearest-neighbor particle hop occurring at rate \(r>0\). Start the process in its uniform fixed-particle-number equilibrium. For any contiguous block \(B=\{0,\ldots,m-1\}\), \(1\le m<n\), write \(N_B(t)=\sum_{i\in B}\eta_i(t)\), and define the centered integrated occupation
\[
A_t=\int_0^t \bigl[N_B(s)-km/n\bigr] \,ds.
\]
The exact long-time variance rate is
\[
\boxed{\lim_{t\to\infty}\frac{\operatorname{Var}(A_t)}{t}=\frac{k(n-k)m(n-m)\,[m(n-m)+2]}{6r\,n^2(n-1)}.}\tag{1}
\]
There is a canonical decomposition of this rate into the stationary quadratic-variation rates of the martingale obtained from the Poisson corrector, one nonnegative contribution \(w_i\) per undirected spatial bond \(\{i,i+1\}\). Put \(a=m\), \(b=n-m\) and
\[
d_i=\begin{cases}
\dfrac{b(a-2i-2)}{2n},&0\le i<a,\\[4pt]
\dfrac{a(2i-n-a+2)}{2n},&a\le i<n.
\end{cases}\tag{2}
\]
Then
\[
\boxed{w_i=\frac{2k(n-k)}{r\,n(n-1)}d_i^2},\qquad \sum_{i=0}^{n-1}w_i=\lim_{t\to\infty}\frac{\operatorname{Var}(A_t)}t.\tag{3}
\]
The two observable-boundary bonds \(\{a-1,a\}\) and \(\{n-1,0\}\) are the **unique two bonds of maximal individual importance**, but their **combined** fraction of (1) is only
\[
\boxed{R_{n,m}=\frac{6m(n-m)}{n\,[m(n-m)+2]}=\frac6n-\frac{12}{n\,[m(n-m)+2]}.}\tag{4}
\]
This fraction does not depend on the particle count or hop rate, and it tends to zero uniformly over all nontrivial block sizes as \(n\to\infty\). More generally, the best \(K\)-bond selection captures at most \(3K/n\) of the variance, for each \(1\le K\le n\); the explicit stronger bound is \(3K m(n-m)/(n[m(n-m)+2])\). For every \(n\ge12\), even the optimal two bonds account for strictly **less than half** of the integrated-occupation variance, and \(n=12\) is the smallest all-larger-sizes threshold: at \(n=11\), \(m=5\), their fraction equals \(45/88>1/2\).

The normalized stationary correlation time is also exact and independent of particle number:
\[
\frac{\lim_{t\to\infty}\operatorname{Var}(A_t)/t}{2\operatorname{Var}_{\pi}(N_B)}=\frac{m(n-m)+2}{12r},\qquad \operatorname{Var}_{\pi}(N_B)=\frac{k(n-k)m(n-m)}{n^2(n-1)}.\tag{5}
\]

## Assumptions and scope
The state is \(\eta\in\{0,1\}^n\) with \(\sum_i\eta_i=k\), using cyclic indices. Every bond \(\{i,i+1\}\) exchanges an occupied/empty pair at rate \(r\); equal occupancies do nothing. The finite process is irreducible and reversible under the uniform measure \(\pi\) on \(\binom nk\) configurations. All formulas hold for every integer \(n\ge3\), \(1\le k,m<n\), and real \(r>0\), without a large-system approximation. An edge contribution here is defined through the **Poisson-corrector martingale quadratic variation** of the **long-time integrated observable**; it is not the static covariance contribution or the variance obtained by literally removing transition mechanisms from the nonlinear exclusion chain.

## Proof
Set \(f(\eta)=N_B-km/n\). Let \(L_0u(i)=u(i+1)+u(i-1)-2u(i)\). Solve \(-L_0u(i)=\mathbf1_{\{i\in B\}}-m/n\), which is solvable uniquely up to an additive constant because the right side sums to zero. Taking differences \(d_i=u(i+1)-u(i)\), the equations give \(d_i-d_{i-1}=m/n-\mathbf1_{\{i\in B\}}\), and periodicity imposes \(\sum_i d_i=0\). These two requirements yield (2), including the boundary values \(d_{m-1}=-m(n-m)/(2n)\) and \(d_{n-1}=m(n-m)/(2n)\).

For the full interacting exclusion generator \(\mathcal L\), define the linear corrector
\[
U(\eta)=r^{-1}\sum_{i=0}^{n-1}u(i)\eta_i.
\]
In an exclusion exchange the increment of \(U\) is \((u(i+1)-u(i))(\eta_i-\eta_{i+1})/r\). Summing allowed exchanges gives \(\mathcal L U=r^{-1}\sum_i\eta_i(r L_0u)(i)=-f\): exclusion factors cancel in the generator acting on a linear occupation observable. Consequently
\[
M_t=U(\eta_t)-U(\eta_0)+A_t
\]
is a square-integrable martingale. The corrector is bounded because the state space is finite. In stationarity \(\operatorname{Var}(A_t)/t\) and \(\mathbb E[M_t^2]/t\) have the same limit (the cross term is \(o(t)\) by Cauchy--Schwarz). Under the uniform \(k\)-particle measure,
\[
\mathbb E_\pi[(\eta_i-\eta_{i+1})^2]=\frac{2k(n-k)}{n(n-1)},
\]
so the expected predictable martingale quadratic variation of bond \(i\) per unit time equals (3).

For \(s\ge1\), the elementary exact identity \(\sum_{h=1}^{s-1}(s-2h)^2=s(s-1)(s-2)/3\) gives, after applying (2) separately to the two arcs,
\[
\sum_i d_i^2=\frac{m(n-m)[m(n-m)+2]}{12n}.
\]
Combining this with (3) proves (1). Hypergeometric sampling of the uniform \(k\)-particle configuration gives the stationary variance in (5), hence its correlation-time formula.

Every nonboundary difference in (2) has magnitude strictly less than \(m(n-m)/(2n)\), while both boundary differences attain that magnitude. Thus the two boundary edges are the unique maximum-weight edges. Their two contributions divided by (1) give (4). Each edge weight is no larger than a boundary weight, so any \(K\) edge weights total at most \(K/2\) times the sum of the two boundary weights: its variance fraction is at most \(3K m(n-m)/(n[m(n-m)+2])<3K/n\). In particular, (4) is strictly less than \(6/n\), hence less than \(1/2\) for every \(n\ge12\). For \(n=11,m=5\), direct substitution into (4) yields \(45/88\), proving sharpness of the all-larger-sizes cutoff. Because \(m(n-m)\ge n-1\), (4) differs from \(6/n\) by at most \(12/[n(n+1)]\), uniformly over \(m\).

## Verification
Run \(\texttt{python3 verify_cycle_shielding.py}\); the program uses only the Python standard library and exact rational arithmetic. It independently solves the one-walker Poisson equations for every \(3\le n\le20\) and each block length, verifies the explicit edge gradients, variance and selection identities, and checks larger cycles through \(n=1024\). Crucially, it constructs the **full interacting \(\binom nk\)-state exclusion generator**, independently solves the configuration-space Poisson equation, and checks (1), (3), and (4) in **94** small-system settings (including nonunit hopping rates), covering **1,374** configuration appearances. The one-walker portion checks 219 parameter settings and 10,098 rational edge weights. These are finite corroborations of the general argument, not substitutes for its arbitrary-\(n\) proof.

## Relationship to prior work
Schmandt and Galán (2012) introduced stochastic shielding of unobserved transitions. Schmidt and Thomas (2013) introduced graph-edge importance measures and optimal noise-source selection for stationary Ornstein--Uhlenbeck reductions; Schmidt, Galán and Thomas (2018) further derived power-spectral edge decompositions and documented exceptions in which hidden transitions dominate. Thus neither the *general edge-decomposition idea* nor the *possibility of important hidden transitions* is claimed as new. The explicit formulas (1)--(5) instead concern finite **interacting** canonical-density exclusion, the **zero-frequency** integrated block-occupation observable, the exact sharp two-boundary fraction, and its uniform geometric cutoff. Appert-Rolland et al. (2008) compute current and activity cumulants for periodic SSEP, distinct observables from the integrated residence-time fluctuation treated here. General projection/resolvent methods provide related theoretical machinery, but the inspected works do not evaluate this particular all-size interacting bond allocation. Equivalence to an unlocated historical result remains possible.

## Limitations
The result is about stationary continuous-time homogeneous nearest-neighbor SSEP on a finite cycle and a single contiguous block, with fixed positive particle count strictly below the number of sites. It is not a general impossibility theorem for all noise-reduction algorithms: the canonical Poisson-corrector edge allocation characterizes long-time zero-frequency variance, not full finite-time pathwise accuracy or stationary instantaneous variance. No conclusion for asymmetric hopping, open boundaries, inhomogeneous rates, multiple disjoint blocks, or infinite-volume fluctuation fields is proved. The 2012 source was inspectable at abstract level but not in complete text, leaving a specific bibliographic coverage risk.

## References
- C. Appert-Rolland, B. Derrida, V. Lecomte, and F. van Wijland, *Universal cumulants of the current in diffusive systems on a ring*, arXiv:0804.2590v1 (public 2008-04-16), https://arxiv.org/abs/0804.2590 .
- N. T. Schmandt and R. F. Galán, *Stochastic-Shielding Approximation of Markov Chains and its Application to Efficiently Simulate Random Ion-Channel Gating*, Phys. Rev. Lett. 109, 118101 (online 2012-09-11), https://doi.org/10.1103/PhysRevLett.109.118101 .
- D. R. Schmidt and P. J. Thomas, *Measuring edge importance: a quantitative analysis of the stochastic shielding approximation for random processes on graphs*, arXiv:1308.5179v1 (public 2013-08-23), https://arxiv.org/abs/1308.5179 .
- D. R. Schmidt, R. F. Galán, and P. J. Thomas, *Stochastic shielding and edge importance for Markov chains with timescale separation*, PLOS Computational Biology 14, e1006206 (2018), https://doi.org/10.1371/journal.pcbi.1006206 .
