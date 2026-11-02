# Strict positive site association in the weak-Langmuir limit of driven exclusion networks

## Finding

For an exclusion system whose stationary state at each conserved particle number is a positive, inhomogeneous product weight conditioned on that number, arbitrarily weak *uniform* Langmuir attachment and detachment reverse the sign of correlations between occupied sites. Conditional on any nontrivial fixed particle number, every distinct pair has **strictly negative covariance**. In the stationary zero-Langmuir-rate limit with fixed nonzero attachment-to-detachment ratio, the covariance of every distinct pair is instead **strictly positive** if the site weights are nonconstant, regardless of distance. More strongly, that limiting law is log-supermodular (MTP2) and all coordinatewise nondecreasing observables are positively associated. All pair covariances vanish exactly when all site weights coincide.

This holds on finite connected, nontrivially driven, multi-lane asymmetric simple exclusion networks with a closed coordinate and a periodic transverse coordinate, including lane-dependent hopping rates and stationary circulating currents. For each such fixed finite system with unequal weights, the pair covariances remain positive at all sufficiently small **strictly positive** Langmuir rates. No uniform infinite-volume claim is made.

## Assumptions and scope

Let \(V\) contain \(L\ge2\) distinguishable sites, and let \(w_i>0\) for all \(i\in V\). Occupancy configurations are subsets \(S\subseteq V\), with \(\eta_i(S)=\mathbf1_{\{i\in S\}}\). Define elementary symmetric polynomials and the canonical measures by
\[
e_k(w)=\sum_{|S|=k}\prod_{i\in S}w_i,\qquad
\pi_k(S)=\mathbf1_{\{|S|=k\}}\frac{\prod_{i\in S}w_i}{e_k(w)},\qquad 0\le k\le L.
\]
Assume a finite-state irreducible exclusion hopping generator \(H\) preserves the particle number and has the unique stationary law \(\pi_k\) in every \(k\)-particle sector. Add independent, uniform particle insertion at an empty site at rate \(\epsilon a\) and removal at an occupied site at rate \(\epsilon b\), where \(a,b>0\) and \(\epsilon>0\). Set \(q=a/(a+b)\in(0,1)\), and denote the unique perturbed stationary law by \(\mu_\epsilon\).

Its weak-exchange limit is
\[
\mu_0(S)=\binom{L}{|S|}q^{|S|}(1-q)^{L-|S|}
\frac{\prod_{i\in S}w_i}{e_{|S|}(w)}.
\tag{1}
\]
The particle-number marginal is exactly \(\operatorname{Bin}(L,q)\) already for every \(\epsilon>0\). Formula (1), including the form for multi-dimensional ASEP, is prior work; the claims here concern its previously unclassified dependence structure and the strict finite-rate consequence.

A concrete non-equilibrium class takes \(L=L_xL_y\), \(L_x\ge2\), \(L_y\ge3\), a reflecting/closed horizontal coordinate \(x\) and periodic vertical coordinate \(y\). Horizontal nearest-neighbor hops have positive rates \(p_x\) right and \(q_x\) left, while vertical hops on each horizontal layer have positive \(p_y(x)\) forward and \(q_y(x)\) backward, independently of \(y\). The canonical weight is \(w_{x,y}=(p_x/q_x)^x\), with \(x\in\{0,\ldots,L_x-1\}\). If \(p_x\ne q_x\), these weights are nonconstant; when some \(p_y(x)\ne q_y(x)\), there is nonzero stationary vertical particle current. This model is an explicitly verified subclass rather than a claim about arbitrary driven exclusion generators.

## Proof

**1. The weak-exchange stationary law.** At every positive \(\epsilon\), the total particle count \(N\) is an autonomous birth–death chain with rates \(\epsilon a(L-k)\) from \(k\) to \(k+1\) and \(\epsilon bk\) from \(k\) to \(k-1\). Its unique equilibrium is \(\operatorname{Bin}(L,q)\), independent of the hopping rates. Since the state space is finite, any subsequential limit of \(\mu_\epsilon\) as \(\epsilon\downarrow0\) is stationary for \(H\); sector uniqueness forces its conditional law at \(N=k\) to be \(\pi_k\). The already-fixed binomial sector masses identify the limit uniquely, proving (1) without an interchange of thermodynamic limits.

**2. The log-supermodular lattice inequality.** Put \(a_k=e_k(w)/\binom{L}{k}\), the normalized elementary symmetric means. The sharp form of Newton's inequalities states
\[
a_{k+1}^2\ge a_ka_{k+2},\quad 0\le k\le L-2,
\]
with strict inequality for every indicated \(k\) if the positive weights are not all equal. Writing (1) as \(\mu_0(S)=c_{|S|}\prod_{i\in S}w_i\), one has \(c_k=q^k(1-q)^{L-k}/a_k\). For any \(S\) not containing distinct \(i,j\), with \(|S|=k\),
\[
\frac{\mu_0(S)\mu_0(S\cup\{i,j\})}
{\mu_0(S\cup\{i\})\mu_0(S\cup\{j\})}
=\frac{a_{k+1}^2}{a_ka_{k+2}}\ge1.
\tag{2}
\]
Elementary squares generate the distributive Boolean lattice; hence (2) gives \(\mu_0(A\cup B)\mu_0(A\cap B)\ge\mu_0(A)\mu_0(B)\) for arbitrary configurations \(A,B\). As every configuration has positive mass, the finite FKG inequality establishes nonnegative covariance of all nondecreasing observables.

**3. Strict positive covariance for every pair.** Suppose the weights are not all equal. Then every elementary-square inequality in (2) is strict. Fix two sites \(i\ne j\) and condition on the full occupancy configuration \(T\) of the remaining \(L-2\) sites. The resulting positive \(2\times2\) conditional probability table has cross-product odds ratio strictly above one by (2), so \(\operatorname{Cov}(\eta_i,\eta_j\mid T)>0\) for *every* \(T\). MTP2 is preserved by marginalization, and its monotone-regression property makes each conditional mean \(\mathbb E[\eta_i\mid T]\) and \(\mathbb E[\eta_j\mid T]\) nondecreasing in the coordinates of \(T\). Applying FKG to the marginal of \(T\) shows that the covariance of these two conditional means is nonnegative. The law of total covariance therefore gives \(\operatorname{Cov}_{\mu_0}(\eta_i,\eta_j)>0\), for every pair. If all \(w_i\) coincide, (1) is exactly the independent Bernoulli product law and every pair covariance is zero. (Alternatively, the finite four-functions inequality and strict local minors give the same conclusion.)

**4. Opposite sign in each fixed-size sector.** For \(1\le k\le L-1\), remove the two site weights \(w_i,w_j\), calling the remainder \(u\) (length \(L-2\)); use \(e_{-1}(u)=e_{L-1}(u)=0\). Elementary inclusion/exclusion gives
\[
\operatorname{Cov}_{\pi_k}(\eta_i,\eta_j)
=-\frac{w_iw_j}{e_k(w)^2}
\left[e_{k-1}(u)^2-e_{k-2}(u)e_k(u)\right]<0.
\tag{3}
\]
The last strict inequality follows from the strict (unnormalized) log-concavity of the elementary symmetric coefficient sequence for positive weights, including the endpoint cases; for \(L=2\) it follows directly from \(e_0(u)=1\). This is the genuine canonical-versus-Langmuir sign reversal.

For \(L=2\), formula (1) also gives the nontrivial exact identity
\[
\operatorname{Cov}_{\mu_0}(\eta_1,\eta_2)
=q^2(1-q)^2\left(\frac{w_1-w_2}{w_1+w_2}\right)^2.
\tag{4}
\]
Thus the sharp equality condition is visible already in the smallest system.

**5. Driven multi-lane realization and finite-rate consequence.** For the stated strip, horizontal moves satisfy pairwise detailed balance with respect to \(\prod w_{x,y}^{\eta_{x,y}}\) because \(w_{x+1,y}/w_{x,y}=p_x/q_x\). For each periodic vertical ring, all site weights agree, and its asymmetric inflow/outflow sums cancel by cyclic telescoping, even when its two rates depend on \(x\). These facts verify stationarity of each \(\pi_k\); positivity of all hopping rates on the connected grid gives sector irreducibility. Nonzero vertical asymmetry produces a persistent current because the probability of an occupied–empty oriented vertical bond is positive and orientation-reversal symmetric under the \(y\)-translation-invariant \(\pi_k\) for \(1\le k\le L-1\) and under \(\mu_0\). By finite-state stationary continuity \(\mu_\epsilon\to\mu_0\), and there are finitely many site pairs, so strict limiting positivity persists simultaneously for all pairs for each sufficiently small \(\epsilon>0\). The smallness threshold may depend on the geometry, rates and parameters.

## Verification

Run `python verify.py` with Python 3 and NumPy. The standalone script reconstructs (1) and tests every elementary-square inequality and all pair signs in 240 independent weighted-subset examples at sizes two through seven. It separately checks the exact two-site identity and negative fixed-size covariances. For a six-site driven strip with two horizontal layers, three periodic vertical sites, horizontal rates \((p_x,q_x)=(3,1)\), layer-dependent vertical rate pairs \((2.2,0.8)\) and \((1.5,0.65)\), and \((a,b)=(2,3)\), it constructs an independent 64-state hopping-plus-exchange generator. It verifies the hopping-only invariant distribution, exact binomial number marginal at four positive exchange strengths, convergence to the theoretical weak-limit vector and positive pair covariance at the smallest tested rate. Exact symbolic inequalities and finite-state arguments above, not finite experiments, prove the unlimited-parameter statements.

## Relationship to prior work

Ishiguro and Sato (arXiv:2405.09261v1, 2024) gave the canonical-sector mixture as the proposed weak-Langmuir state in two dimensions, reported numerical verification for closed and multi-lane boundaries, and analyzed densities and currents. Their earlier arXiv:2403.01934v1 provided the sectorwise product-weight stationary measures beyond one dimension, including nonuniform periodic lanes. Sato and Nishinari (arXiv:1711.06949, first public 2017) established the one-dimensional closed-system weak-Langmuir construction. The FKG implication, MTP2 marginal/regression closure (Karlin–Rinott), and Newton inequalities are standard prior mathematical tools, not new lemmas claimed here. The contribution is the *strict all-pairs positive association versus canonical negative covariance*, its equality classification, and rigorous finite-rate persistence in an explicitly driven multi-lane subclass. None of the inspected primary-source results directly states this dependence-phase classification; that literature comparison is not an absolute priority guarantee.

## Limitations

Only finite connected exclusion systems with the specified canonical product-weight structure and uniform attachment/detachment are covered. Positive covariance at fixed strictly positive Langmuir rate requires a parameter-dependent sufficiently small rate; monotonicity in that rate is neither proved nor claimed. There is no thermodynamic-limit lower bound, uniform-in-volume perturbation theorem, nonlinear reaction generalization, or extension to hopping models whose conserved sectors do not have the stated weights. External independent scientific review and exhaustive publication-priority verification have not been performed.

## References

1. Y. Ishiguro and J. Sato, *Exact analysis of the two-dimensional asymmetric simple exclusion process with attachment and detachment of particles* (2024), arXiv:2405.09261v1, https://arxiv.org/html/2405.09261v1.
2. Y. Ishiguro and J. Sato, *Exact steady states in the asymmetric simple exclusion process beyond one dimension* (2024), arXiv:2403.01934v1, https://arxiv.org/html/2403.01934v1.
3. J. Sato and K. Nishinari, *Relaxation dynamics of closed diffusive systems with infinitesimal Langmuir kinetics* (2017), arXiv:1711.06949, https://arxiv.org/abs/1711.06949.
4. C. M. Fortuin, P. W. Kasteleyn and J. Ginibre, *Correlation inequalities on some partially ordered sets*, Communications in Mathematical Physics 22 (1971), 89–103, https://doi.org/10.1007/BF01651330.
5. S. Karlin and Y. Rinott, *Classes of orderings of measures and related correlation inequalities. I. Multivariate totally positive distributions*, Journal of Multivariate Analysis 10 (1980), 467–498, https://doi.org/10.1016/0047-259X(80)90065-2.
6. Classical Newton inequalities for elementary symmetric polynomials, https://en.wikipedia.org/wiki/Newton%27s_inequalities.
