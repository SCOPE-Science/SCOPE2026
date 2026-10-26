# Sharp flux-curvature transition in the weakly deformed large-capacity exclusion gas

## Finding
For the periodic \((q,t)\) asymmetric \(K\)-exclusion gas with occupation \(\eta_i\in\{0,\ldots,K\}\), right-jump rate \([a]_t([K]_t-[b]_t)\), left-jump rate \(q[b]_t([K]_t-[a]_t)\), \(0\le q<1\), and \([a]_t=\sum_{j=0}^{a-1}t^j\), consider the stationary current at density \(\rho\). At fixed \(K\), after taking the ring length to infinity, it has the exact fugacity representation
\[
\rho=\sum_{j=-1}^{K-2}\frac{t^j y}{1+t^j y},\qquad J_{K,t,q}(\rho)=(1-q)[K]_t^2\frac{t y}{(t+y)^2},\qquad y>0.
\]
In particular, its unique current-maximizing density is \(\sum_{j=0}^{K-1}t^j/(1+t^j)\), and its maximal current equals \((1-q)[K]_t^2/4\).

Now take the **iterated limit** of ring length first, then capacity \(K\to\infty\), with \(t_K=e^{\lambda/K}\), \(\rho_K=Ku\), and fixed \(u\in(0,1)\), \(\lambda\in\mathbb R\). The capacity-normalized flux converges to
\[
\mathcal J_{\lambda,q}(u)=
\begin{cases}
\displaystyle\frac{1-q}{\lambda^2}\big(e^{\lambda u}-1\big)\big(e^{\lambda}-e^{\lambda u}\big),&\lambda\ne0,\\
(1-q)u(1-u),&\lambda=0.
\end{cases}
\]
The limiting flux is strictly concave throughout \(0<u<1\) **if and only if** \(|\lambda|\le\log3\). For \(|\lambda|>\log3\), it has exactly one interior inflection point
\[
u_{\mathrm{inf}}(\lambda)=\lambda^{-1}\log\frac{1+e^\lambda}{4}.
\]
For \(\lambda>\log3\), the flux is convex below this point and concave above it; for \(\lambda<-\log3\), the order reverses. For all real \(\lambda\), the flux has a unique maximum, at
\[
u_*(\lambda)=\begin{cases}\displaystyle\lambda^{-1}\log\frac{1+e^\lambda}{2},&\lambda\ne0,\\1/2,&\lambda=0.\end{cases}
\]
Thus the exactly factorized exclusion gas exhibits a sharp, nontrivial loss of global flux concavity when the scaled deformation crosses \(\pm\log3\).

## Assumptions and scope
Fix integer \(K\ge1\), ring length \(L\ge3\), deformation \(t>0\), and asymmetry \(0\le q<1\). The total particle number is conserved, with \(0\le n\le LK\). For each fixed \(K,t\), the thermodynamic current means the limit along canonical steady states with \(n/L\to\rho\in(0,K)\). The capacity limit is performed afterward, with \(\rho=Ku\), \(t=e^{\lambda/K}\), and fixed \(u\in(0,1)\), \(\lambda\in\mathbb R\). No interchange of these limits is asserted. At \(t=1\), define \([a]_1=a\) by continuity. Current is signed rightward minus leftward. For \(q=1\), it vanishes identically, so the strict statements require \(q<1\).

## Proof
**1. Stationarity and the fugacity law.** The source gives the canonical factorized weights
\[
w_a(t)=t^{(a-1)(a-2)/2}{K\brack a}_t,
\qquad F_{K,t}(y)=\sum_{a=0}^K w_a(t)y^a
=t\prod_{j=-1}^{K-2}(1+t^j y).
\]
All weights are positive. Here \({K\brack a}_t=\prod_{r=1}^a[K-r+1]_t/[r]_t\), and \(a=0\) has the empty product convention. A direct check of the stationary balance uses
\[
\frac{w_{a+1}}{w_a}=t^{a-1}\frac{[K-a]_t}{[a+1]_t},\qquad
[K]_t-[b]_t=t^b[K-b]_t.
\]
For a local pair \((a,b)\), the incoming right-jump rate weighted by the precursor configuration is \(w_aw_b\,u(b,a)\), while the incoming left-jump term is \(q w_aw_b\,u(a,b)\), where \(u(a,b)=[a]_t([K]_t-[b]_t)\); terms forbidden by an endpoint occupation vanish on both sides. The outgoing terms are \(w_aw_b(u(a,b)+q u(b,a))\). Their net difference on a bond equals \((1-q)w_aw_b[u(b,a)-u(a,b)]\), which sums to zero around a periodic ring because \(u(b,a)-u(a,b)=[K]_t([b]_t-[a]_t)\). Hence the canonical product-weight measure is stationary. The source's fixed-\(n\) law is recovered, without assuming detailed balance.

The grand-canonical one-site distribution \(P_y(a)=w_a(t)y^a/F_{K,t}(y)\) has mean \(\rho_K(y)=y\partial_y\log F_{K,t}(y)\), giving the displayed density formula. Moreover, for \(t\ne1\), the telescoping product yields
\[
\mathbb E_y(t^\eta)=\frac{F_{K,t}(ty)}{F_{K,t}(y)}
=\frac{1+t^{K-1}y}{1+y/t},\qquad
\mu:=\mathbb E_y[\eta]_t
=\frac{1-\mathbb E_y(t^\eta)}{1-t}=[K]_t\frac{y}{t+y}.
\]
Both identities extend continuously to \(t=1\). For each fixed \(K\), \(\rho_K(y)\) increases strictly from \(0\) to \(K\), so every interior density fixes a unique fugacity. The canonical distribution equals this grand-canonical product distribution conditioned on total occupancy \(n\). The finite-support span-one local central limit theorem implies convergence of every fixed-site marginal to \(P_y^{\otimes m}\) as \(L\to\infty\) and \(n/L\to\rho\in(0,K)\). Therefore the limiting right-minus-left bond current factorizes as \((1-q)\mu([K]_t-\mu)\), producing the first exact current formula. As a strictly positive multiple of \(y/(t+y)^2\), it is uniquely maximized at \(y=t\), where \(\rho_K(t)=\sum_{j=0}^{K-1}t^j/(1+t^j)\).

**2. Capacity scaling.** For each fixed \(y>0\), let \(t_K=e^{\lambda/K}\). The density is a Riemann sum:
\[
\frac{\rho_K(y)}{K}\longrightarrow U_\lambda(y)=\int_0^1\frac{ye^{\lambda s}}{1+ye^{\lambda s}}\,ds
=\begin{cases}\displaystyle\frac1\lambda\log\frac{1+ye^\lambda}{1+y},&\lambda\ne0,\\\displaystyle\frac{y}{1+y},&\lambda=0.\end{cases}
\]
The map \(U_\lambda:(0,\infty)\to(0,1)\) is continuous and strictly increasing. Consequently the fugacity at \(\rho_K=Ku\) converges to the unique solution \(y_\lambda(u)\), which for \(\lambda\ne0\) is
\[
y_\lambda(u)=\frac{e^{\lambda u}-1}{e^\lambda-e^{\lambda u}}.
\]
Also \([K]_{t_K}/K\to(e^\lambda-1)/\lambda\), with limit \(1\) at \(\lambda=0\), and \(t_K\to1\). Substituting into the exact fugacity current and simplifying gives the stated capacity-normalized flux, pointwise for every fixed interior \(u\).

**3. Sharp curvature transition.** Direct differentiation (with continuous interpretation at \(\lambda=0\)) gives
\[
\mathcal J_{\lambda,q}'(u)=\frac{1-q}{\lambda}e^{\lambda u}\big(1+e^\lambda-2e^{\lambda u}\big),\qquad
\mathcal J_{\lambda,q}''(u)=(1-q)e^{\lambda u}\big(1+e^\lambda-4e^{\lambda u}\big).
\]
The first expression has exactly one zero at \(e^{\lambda u}=(1+e^\lambda)/2\), yielding the stated maximizing density and maximum. The second changes sign exactly when \(e^{\lambda u}=(1+e^\lambda)/4\). For \(\lambda>0\), the range of \(e^{\lambda u}\) on \((0,1)\) is \((1,e^\lambda)\), so an interior zero exists iff \(e^\lambda>3\). For \(\lambda<0\), the range is \((e^\lambda,1)\), so an interior zero exists iff \(e^\lambda<1/3\). In the complementary parameter range the second derivative is negative throughout the open interval (including the endpoints of the parameter range \(|\lambda|=\log3\), where the possible zero lies at a boundary density). The stated sign pattern and the exact \(\pm\log3\) threshold follow.

## Verification
The accompanying \(check.py\) verifies, using exact rational arithmetic for multiple capacities/deformations/fugacities, the one-site factorization, the expected deformed occupation, and the optimizing flux. It checks exact finite-ring stationarity by enumerating all canonical configurations of selected small systems and balancing every incoming/outgoing Markov transition. It also compares capacity-dependent currents and maximizing densities with the analytical limits, and checks the limiting second-derivative formula by finite differences for deformations on and beyond the two threshold values. The infinite-volume and infinite-capacity statements are established by the proof above, not by these finite numerical checks.

## Relationship to prior work
Ayyer and Misra (first posted 2023-10-05, arXiv:2310.03343) introduced the \((q,t)\) \(K\)-exclusion process, proved the stationary factorization, and analyzed local occupation distributions. Their stationary generating function supplies the starting point; the present finding isolates the stationary signed-current diagram and its nonconcave weak-deformation, large-capacity regime. Generic misanthrope-process factorization and the use of stationary current–density relations in transport theory are known. The sharp model-specific curvature boundary \(|\lambda|=\log3\) and the accompanying closed limiting flux are not consequences of the qualitative factorization statement alone without the explicit new evaluation and scaling analysis. Comparisons include Evans and Waclaw on factorized mass transport and Chleboun, Grosskinsky, and Pizzoferrato on current large deviations in zero-range processes. Ayyer and Misra's later asymmetric **inclusion** process treats different unbounded-occupancy dynamics and does not identify this bounded-exclusion curvature transition.

## Limitations
The theorem identifies the stationary thermodynamic current and its iterated large-capacity limit; it does **not** prove a hydrodynamic limit, shock selection, KPZ exponents, current fluctuations, finite-ring spectral properties, or simultaneous scaling of \(L\) and \(K\). Results exclude \(q=1\) from strict maximizer and strict concavity assertions. Literature comparisons cannot establish absolute uniqueness; closely related, unindexed hydrodynamic notes may require independent follow-up. Finite computations are reproducibility checks only.

## References
1. A. Ayyer and S. Misra, *An exactly solvable asymmetric \(K\)-exclusion process*, arXiv:2310.03343, first public 2023-10-05. https://arxiv.org/abs/2310.03343.
2. M. R. Evans and B. Waclaw, *Condensation in stochastic mass transport models: beyond zero-range process*, arXiv:1312.5642 (2014). https://arxiv.org/abs/1312.5642.
3. P. Chleboun, S. Grosskinsky, and A. Pizzoferrato, *Lower Current Large Deviations for Zero-Range Processes on a Ring*, Journal of Statistical Physics (2017).
4. A. Ayyer and S. Misra, *An exactly solvable asymmetric simple inclusion process*, arXiv:2510.09191 (2025), distinct model. https://arxiv.org/abs/2510.09191.
