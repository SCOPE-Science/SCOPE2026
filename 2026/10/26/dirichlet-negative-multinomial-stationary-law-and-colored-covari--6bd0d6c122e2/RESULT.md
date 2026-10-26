# Dirichlet–negative-multinomial stationary law and colored covariance reversal in the boundary-driven harmonic chain

## Finding
Consider the integrable, reservoir-driven multispecies harmonic process defined in Casini–Frassek–Giardinà [1]. For its full stationary law on \(N\ge1\) sites and \(M\ge1\) colors we obtain an explicit Dirichlet mixture of independent negative-multinomial site distributions. A consequence is an exact finite-chain covariance tensor and a strict sign contrast: two different colors can be negatively correlated across separated sites when their reservoir fugacity gradients oppose each other, although their occupations at a common site have positive covariance. The source establishes the process and common absorbing/hidden-parameter dualities; the explicit multispecies stationary mixture and colored covariance classification are the claims assessed here.

Let \(t=2s>0\), \(L=N+1\), and let the reservoir injection parameters be \(\beta_{L,a},\beta_{R,a}>0\), with \(\sum_a\beta_{B,a}<1\) for \(B\in\{L,R\}\). Their fugacities are \(\rho_{B,a}=\beta_{B,a}/(1-\sum_b\beta_{B,b})\). Write \(\Delta_a=\rho_{L,a}-\rho_{R,a}\) and \(\mu_{i,a}=((L-i)\rho_{L,a}+i\rho_{R,a})/L\).

Take a positive Dirichlet random vector
\[ (H_1,\ldots,H_L)\sim\operatorname{Dirichlet}(t,\ldots,t),\qquad W_i=\sum_{k=i+1}^{L}H_k\quad (1\le i\le N). \]
Given it, put \(\Theta_{i,a}=\rho_{R,a}+\Delta_a W_i\). Independently over sites \(i\), draw the color occupation vector \(n_i=(n_i^1,\ldots,n_i^M)\) from the negative-multinomial law with probability generating function
\[
\mathbb E\left[\prod_{a=1}^M z_a^{n_i^a}\mid\Theta\right]
=\left(1+\sum_{a=1}^M\Theta_{i,a}(1-z_a)\right)^{-t}.
\]
**This mixture is the unique stationary law.** Consequently, with
\[
G_{ij}=\frac{\min(i,j)\,[L-\max(i,j)]}{L^2(Lt+1)},
\]
we have \(\mathbb E[n_i^a]=t\mu_{i,a}\) and
\[
\operatorname{Cov}(n_i^a,n_j^b)=
\begin{cases}
 t^2\Delta_a\Delta_b G_{ij},&i\ne j,\\
 t\mathbf1_{a=b}\mu_{i,a}+t\mu_{i,a}\mu_{i,b}
 +t(t+1)\Delta_a\Delta_bG_{ii},&i=j.
\end{cases}
\]
For \(N\ge2\), \(G_{ij}>0\) at distinct interior sites. Hence the separated-site color covariance has a rank-one color factor \(\Delta\Delta^\mathsf T\) and has negative off-diagonal color entries exactly for opposing nonzero reservoir gradients. The same-site covariance of different colors is **strictly positive** for positive reservoir fugacities.

For example, \(N=3\), \(t=2\), \(\rho_L=(4/5,1/5)\), \(\rho_R=(1/5,4/5)\) give the exact contrast
\[
\operatorname{Cov}(n_1^1,n_3^2)=-\frac1{100},\qquad
\operatorname{Cov}(n_2^1,n_2^2)=\frac{11}{25}.
\]

## Assumptions and scope
The state space consists of arbitrary nonnegative integer occupations \(n_i^a\), with nearest-neighbor symmetric colored batch jumps and reservoir removals/injections exactly as in [1], equations (2.6)–(2.13). There is a fixed number \(N\ge1\) of sites, fixed \(M\ge1\) colors, and \(t=2s>0\). Reservoir vectors obey the stated positivity and subunit total injection parameters; no equality of reservoir compositions is assumed. For all-site sign comparisons, a pair of distinct sites requires \(N\ge2\), two colors require \(M\ge2\), and strict sign contrast requires nonzero opposing gradients. The Dirichlet shape is \(t\) at **each** of the \(L\) spacings.

## Proof
**1. Reduction to a scalar hidden process.** In [1], equations (2.38)–(2.43), every hidden-parameter coordinate \(\theta_{i,a}\) is updated by the *same scalar fraction* \(u\in(0,1)\): a directed neighbor or reservoir update replaces \(\theta_{i,a}\) by \((1-u)\theta_{i,a}+u\theta_{j,a}\). The jump-intensity density is \((1-u)^{t-1}du/u\), with boundary values \(\rho_{L,a}\) and \(\rho_{R,a}\). Therefore the affine one-dimensional submanifold \(\theta_{i,a}=\rho_{R,a}+\Delta_a w_i\) is invariant, and \(w_0=1\), \(w_L=0\). Restricted to that submanifold, the generator is precisely the **scalar** harmonic hidden-parameter process with shape \(t\) and endpoint values 1 and 0. The scalar stationary distribution was established in [2,3]: its \(L\) successive nonnegative spacings have the \(\operatorname{Dirichlet}(t,\ldots,t)\) law. This crucial fact also has a direct detailed-balance check. Conditional on its two neighbors, an interior ordered Dirichlet coordinate, linearly rescaled between them, has the \(\operatorname{Beta}(t,t)\) density \(c x^{t-1}(1-x)^{t-1}\). For \(0<y<x<1\), the downward jump density at \(x\) to \(y\) is \((y/x)^{t-1}/(x-y)\), and the upward reverse jump density from \(y\) to \(x\) is \(((1-x)/(1-y))^{t-1}/(x-y)\). Multiplying by the respective Beta densities gives the identical detailed-balance weight \(c y^{t-1}(1-x)^{t-1}/(x-y)\). Therefore each site generator, conditionally on its neighbors, preserves the ordered Dirichlet distribution; summing generators proves stationarity of \(W\) for all \(N,t\), including the boundary sites with fixed neighbors 1 and 0. Only this stationary affine law, not a uniqueness assertion about the full vector hidden process, is needed in the next step.

**2. Transfer to the occupation law.** Theorem 5.3 and Proposition 5.8 of [1] establish duality of the original occupation process and the hidden-parameter process to the *same* absorbing-particle process, with normalized falling-factorial duality functions. Fix a multiindex \(k=(k_{i,a})\) of total finite degree. At interior sites the original duality monomial is
\[
 \prod_{i=1}^N\frac{\prod_a(n_i^a)_{\underline{k_{i,a}}}}{(t)_{\sum_a k_{i,a}}},
\]
where \((x)_{\underline r}\) is the falling factorial and \((t)_r\) is the rising factorial. The corresponding hidden monomial is \(\prod_{i,a}\theta_{i,a}^{k_{i,a}}\). Both dualities use matching reservoir factors \(\prod_a\rho_{B,a}^{k_{B,a}}\) on the two absorbing endpoints. Consequently the original and hidden stationary normalized factorial moments coincide after the finite dual system has been absorbed. Eventual absorption follows because the finite-particle dual is an irreducible finite interior jump system with reachable absorbing endpoints. More directly, initializing an occupation vector from the mixture described in the Finding, the conditional negative-multinomial identity
\[
 \mathbb E\!\left[\prod_a(n_i^a)_{\underline{k_{i,a}}}\mid\Theta\right]
 =(t)_{\sum_a k_{i,a}}\prod_a\Theta_{i,a}^{k_{i,a}}
\]
identifies all duality moments with the invariant hidden law, so they stay constant at every time. These moments determine the occupation law: the \(\Theta\)'s lie in a fixed compact positive rectangle, so the mixture has exponential moments near the origin, and the same duality bounds preserve an exponential-moment neighborhood under time evolution. Hence the candidate mixture is invariant. Irreducibility and positive recurrence ensure uniqueness: let \(g_i=i(L-i)>0\) and \(V=\sum_i g_i\sum_a n_i^a\). Using the first batch-removal moment \(\sum_k k_a\phi_s(k,n)=n_a/t\), the generator gives the strict Foster drift
\[
\mathcal LV =g_1\sum_a\rho_{L,a}+g_N\sum_a\rho_{R,a}-\frac2t\sum_{i,a}n_i^a.
\]
Finite positive boundary injections and reachable removals yield the required irreducibility on the countable state space. Therefore the invariant mixture is the unique stationary occupation law.

**3. Dirichlet covariances.** Since Dirichlet spacings each have parameter \(t\), their cumulative sums obey
\[
\mathbb EW_i=\frac{L-i}{L},\qquad
\operatorname{Cov}(W_i,W_j)=\frac{\min(i,j)[L-\max(i,j)]}{L^2(Lt+1)}=G_{ij}.
\]
For the negative-multinomial conditional law, \(\mathbb E[n_i^a\mid\Theta]=t\Theta_{i,a}\) and
\[
\operatorname{Cov}(n_i^a,n_i^b\mid\Theta)
=t\mathbf1_{a=b}\Theta_{i,a}+t\Theta_{i,a}\Theta_{i,b}.
\]
Distinct sites are conditionally independent. Applying total covariance proves every stated first and second moment and the color-rank-one structure.

**4. Strict local-versus-separated sign.** If \(a\ne b\), \(\Delta_a\Delta_b\ge0\), then the equal-site covariance is positive because \(\mu_{i,a}\mu_{i,b}>0\). Otherwise set \(q=-\Delta_a\Delta_b>0\) and \(w=(L-i)/L\); positivity of all reservoir fugacities gives \(\mu_{i,a}\mu_{i,b}\ge q w(1-w)\). Also
\[(t+1)G_{ii}=\frac{t+1}{Lt+1}w(1-w)<w(1-w)\]
for \(L\ge2\). Therefore the equal-site cross-color covariance is strictly positive. At separated sites, \(t^2G_{ij}>0\), so its sign is exactly that of \(\Delta_a\Delta_b\).

## Verification
The included standalone Python file `verify.py` checks the *original source transition generator*, not just the Dirichlet moment equations. It derives the first and second batch-jump moments and tests the claimed all-color second-moment formulas against every generator first- and second-monomial identity on finite chains with \(1\le N\le8\), \(1\le M\le4\), and four rational shape parameters. All **24,480** second-moment checks (and accompanying first-moment checks) pass in exact rational arithmetic. The same script checks the displayed two-color sign example and Dirichlet Green kernel identities. Finite checks corroborate, but do not replace, the analytic duality-and-Dirichlet proof, which applies to every admissible \(N,M,t\) and reservoir parameter vector.

## Relationship to prior work
[1] introduces exactly the colored batch-jump process, establishes its equilibrium negative-multinomial distribution, absorbing duality, hidden parameter process, and common dualities. Its Section 4.5 expressly leaves the nonequilibrium steady-state calculation to subsequent work, and does not state the Dirichlet-mixture occupation law or cross-color covariance formula. [2] proves the scalar harmonic hidden-parameter ordered-Dirichlet stationary law and mixture method. [3] establishes the scalar harmonic steady state and its large deviations. Neither [2] nor [3] treats color-resolved cross-species covariance for the colored batch-jump process of [1]. [4] computes multispecies SSEP correlations, but its exclusion dynamics (bounded site occupancy and single-particle transfers) cannot imply the unbounded negative-multinomial stationary law here. The present result combines [1]'s shared absorbing dual and vector affine hidden updates with the **known scalar** Dirichlet distribution to determine this explicitly colored steady state. Its broad underlying techniques and scalar special case are not claimed as new.

## Limitations
No transient colored law is asserted; the stationary result uses exactly the chain and boundary rules of [1], not asymmetric bulk rates, color-changing reactions, multiple reservoirs, or generic graph topologies. The rank-one property concerns spatial covariance at distinct sites, not the full same-site matrix. Because the source's dualities and the scalar Dirichlet invariant law were published previously, novelty lies in the new, specifically colored stationary classification and strict cross-species sign pattern, not in a new duality or scalar stationary theorem. Full independent scientific and priority validation is not performed. Broader general Markov-intertwining results may contain an implicit route to this formula; the cited sources and that residual risk are explicitly acknowledged.

## References
[1] F. Casini, R. Frassek, C. Giardinà, *The boundary-driven multispecies harmonic process*, arXiv:2607.26262v1 (first public July 28, 2026), https://arxiv.org/abs/2607.26262 ; especially equations (2.6)–(2.43), Theorem 5.3, Proposition 5.8, Corollary 5.9, and Section 4.5.

[2] C. Giardinà, F. Redig, B. van Tol, *Intertwining and Propagation of Mixtures for Generalized KMP Models and Harmonic Models*, Journal of Statistical Physics 192, article 21 (2025), https://doi.org/10.1007/s10955-025-03393-1 ; Section 3 and scalar ordered-Dirichlet stationary measure.

[3] G. Carinci, C. Franceschini, R. Frassek, C. Giardinà, F. Redig, *Large Deviations and Additivity Principle for the Open Harmonic Process*, Communications in Mathematical Physics 406, 103 (2025), https://doi.org/10.1007/s00220-025-05271-z .

[4] M. Vanicat, *Exact solution to integrable open multi-species SSEP and macroscopic fluctuation theory*, arXiv:1610.08388 (2016), https://arxiv.org/abs/1610.08388 .
