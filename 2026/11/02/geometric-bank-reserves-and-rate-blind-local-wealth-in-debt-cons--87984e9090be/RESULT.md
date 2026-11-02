# Geometric bank reserves and rate-blind local wealth in debt-constrained exchange

## Finding
Consider the symmetric-edge money-exchange chain of Sakagawa (2026) on any connected graph with \(N\ge2\) agents. Let the total net wealth be the nonnegative integer \(K_N\) and the bank's aggregate debt capacity be the positive integer \(L_N\). Fix \(0<p\le q\le1\) and use the transfer probability
\[
g(k)=\begin{cases}p,&k\ge1,\\q,&k\le0.\end{cases}
\]
Assume \(K_N/N\to\kappa>0\) and \(L_N/N\to\delta>0\). In the unique stationary law let \(X_{N,i}\in\mathbb Z\) be agent \(i\)'s net wealth and let \(S_N=L_N-\sum_{i=1}^N(-X_{N,i})_+\) be the bank's uncommitted credit, in integer coins.

Define
\[
R=\sqrt{1+4\delta(\kappa+\delta)},\qquad
 a=\frac{2(\kappa+\delta)+R-1}{2(\kappa+\delta)+R+1},\qquad
 b=\frac{2\delta+R-1}{2\delta+R+1},\qquad
 u=\frac pq\,ab.
\]
Then \(0<a,b,u<1\). For every fixed \(r\ge0\), the joint stationary law of \((S_N,X_{N,1},\ldots,X_{N,r})\) converges in total variation on the countable state space to independent \((S,Y_1,\ldots,Y_r)\), where \(S\) is geometric on the nonnegative integers and the \(Y_j\) are identically distributed with
\[
\Pr(S=s)=(1-u)u^s\quad(s\ge0),\qquad
\Pr(Y_j=k)=\frac1{\kappa+2\delta+R}
\begin{cases}a^k,&k\ge0,\\b^{-k},&k<0.\end{cases}
\]
In particular, the stationary probability that the bank has no remaining credit tends to \(1-u\), and \(\mathbb E S_N\to u/(1-u)\). The local account law depends only on \(\kappa,\delta\), whereas the microscopic reserve distribution also detects the ratio \(p/q\). The result is independent of graph topology within the stated reversible connected class.

At \(\kappa=\delta=1\), the parameters are \(a=3/4\), \(b=2/3\), so the bank is exactly empty with limiting probability \(1-p/(2q)\). For \(p/q=1/2\), the limit is \(3/4\), even though the limiting wealth marginal is the same as in the equal-rate model, for which the empty-bank probability is \(1/2\).

## Assumptions and scope
The graph at each \(N\) is finite, connected and undirected, with positive symmetric probabilities for selecting oriented edges; the choice can vary with \(N\). Each admissible move subtracts one coin from the transferring agent and adds one to the recipient. A move that would increase aggregate debt beyond \(L_N\) is canceled. All results refer to the unique stationary law, not to mixing times. The two positive densities and the fixed ratio \(p/q\) are held away from changing with \(N\); the integers \(K_N,L_N\) need only satisfy the stated limits. The case \(p=q\) is included for continuity and comparison, but the rate-sensitive conclusion is especially informative when \(p<q\).

## Proof
**1. Stationary reduction.** The known invariant product formula for Sakagawa's chain (2026, Proposition 1.1) gives weight \(G(k)=p^{-k}\) for \(k\ge0\) and \(G(-j)=q^j\) for \(j\ge1\). Alternatively, checking the ratio of weights before and after an allowed transfer gives detailed balance: \(G(k-1)/G(k)=g(k)\). For an admissible configuration \(x=(x_i)\) with \(\sum_i x_i=K\) and exact aggregate debt \(d=\sum_i(-x_i)_+\),
\[
 \prod_iG(x_i)=p^{-K}(q/p)^d.
\]
Irreducibility of the connected-graph chain and strict positivity establish uniqueness. In particular, conditioned on exact debt \(d\), the invariant configuration is uniform. Write \(Z_N(K,d)\) for the number of such configurations. Its known finite composition formula, included to make the normalization explicit, is
\[
Z_N(K,0)=\binom{K+N-1}{N-1},\qquad
Z_N(K,d)=\sum_{j=1}^{\min(d,N-1)}\binom Nj\binom{d-1}{j-1}\binom{K+d+N-j-1}{N-j-1}\quad(d\ge1).
\]
It follows by choosing the \(j\) debt-holding sites, distributing total debt \(d\) positively among them, and distributing \(K+d\) nonnegative coins among the others. This finite formula and stationarity are prior results, not the new assertion.

**2. Explicit saddle parameters.** Let \(\alpha=\kappa+\delta\), \(\beta=\delta\). The numbers \(a,b\) above are in \((0,1)\). Define an integer-valued two-sided geometric random variable \(Y\) by
\[
\Pr(Y=k)=c\,a^k\ (k\ge0),\quad \Pr(Y=-j)=c\,b^j\ (j\ge1),\qquad c=\frac{(1-a)(1-b)}{1-ab}.
\]
Its normalizing constant also equals \(c=1/(\kappa+2\delta+R)\). Direct geometric-series evaluation gives
\[
\mathbb EY^+=\frac{ca}{(1-a)^2}=\kappa+\delta,\quad
\mathbb EY^-=\frac{cb}{(1-b)^2}=\delta,\quad
\mathbb EY=\kappa.
\]
For clarity, set \(A=(1-a)^{-1}\), \(B=(1-b)^{-1}\). Then \(c^{-1}=A+B-1\), \(A-B=\kappa\), and \(B(B-1)=\delta(A+B-1)\). The unique solution with \(A,B>1\) is \(B=(1+2\delta+R)/2\), \(A=B+\kappa\), proving the displayed radical formulas. For every sufficiently large \(N\), make the same construction using \(\kappa_N=K_N/N\), \(\delta_N=L_N/N\), and denote the corresponding parameters \(a_N,b_N,c_N\) and \(u_N=(p/q)a_Nb_N\). They converge to interior limits and remain in a compact subset of \((0,1)\).

**3. Uniform local limit and reserve ratio.** Under the independent tilt law \(\nu_N\) with one-site masses \(c_N a_N^k\) for \(k\ge0\), and \(c_N b_N^{-k}\) for \(k<0\), put \(V_i=(Y_i,(-Y_i)_+)\). Its expectation is exactly \((\kappa_N,\delta_N)\). The support contains \((0,0),(1,0),(-1,1)\), hence has full lattice span \(\mathbb Z^2\); its covariance is positive definite. The family has uniformly bounded exponential moments in a neighborhood of zero. The standard two-dimensional lattice local central limit theorem, applied uniformly to this compact parameter family, yields for each fixed integer \(s\ge0\),
\[
\nu_N^{\otimes N}\!\left(\sum_iV_i=(K_N,L_N-s)\right)
=\frac{1+o(1)}{2\pi N\sqrt{\det\Sigma_N}},
\]
where \(\Sigma_N=\operatorname{Cov}_{\nu_N}(V_i)\to\Sigma\) is positive definite. Its characteristic-function inversion proof additionally gives a uniform point-mass bound \(\sup_z\nu_N^{\otimes N}(\sum_iV_i=z)\le C/N\), since the characteristic function has a uniform strict modulus gap off the origin and a uniform Gaussian bound near zero.

The coefficient identity for every feasible \(K,d\) is
\[
\nu_N^{\otimes N}\!\left(\sum_iV_i=(K,d)\right)=c_N^N a_N^K(a_Nb_N)^d Z_N(K,d).
\]
Combining it with Step 1, the ratio of stationary weights of debt levels \(L_N-s\) and \(L_N\) equals
\[
 u_N^s\,
\frac{\nu_N^{\otimes N}(\sum_iV_i=(K_N,L_N-s))}{\nu_N^{\otimes N}(\sum_iV_i=(K_N,L_N))}
\longrightarrow u^s
\]
for every fixed \(s\). The uniform point-mass upper bound and the local lower bound at \((K_N,L_N)\) dominate every ratio by \(C'\rho^s\) with some fixed \(\rho<1\). Summing in \(s\) therefore gives normalization \(\sum_{s=0}^{L_N}\operatorname{weight}(L_N-s)/\operatorname{weight}(L_N)\to(1-u)^{-1}\). This proves the geometric reserve law and, by the same exponential bound, convergence of its mean and every fixed polynomial moment.

**4. Joint tagged-coordinate law.** Fix \(r\) and particular integers \(x_1,\ldots,x_r\). By the same coefficient identity, the stationary mass of the event \(X_{N,j}=x_j\) for \(1\le j\le r\) and \(S_N=s\), divided by the stationary weight of debt \(L_N\), equals
\[
 u_N^s\prod_{j=1}^r\nu_N(Y=x_j)\,
\frac{\nu_N^{\otimes(N-r)}\bigl(\sum V_i=(K_N-\sum_{j=1}^r x_j,\ L_N-s-\sum_{j=1}^r(-x_j)_+)\bigr)}{\nu_N^{\otimes N}\bigl(\sum V_i=(K_N,L_N)\bigr)}.
\]
The same uniform lattice local limit theorem makes the final ratio converge to one (the omitted \(r\) means and fixed offsets are \(O(1)\)). Division by the reserve normalizer from Step 3 yields \((1-u)u^s\prod_j\Pr(Y=x_j)\). Since these pointwise limits sum to one over the entire discrete state space, convergence is in total variation and proves independence of reserve and any fixed collection of agent balances.

## Verification
The standalone `verify_reserve.py` independently enumerates small admissible states, checks exact finite debt-level counts, verifies reversibility both in the uniform and two-rate cases with exact rational weights, validates the radical parameter equations and compares finite reserve probabilities at \(N=50,100,300\) with the limit for three rate ratios. The recorded run reports 1,761 passing finite assertions. Neither finite enumeration nor numerical agreement replaces the analytical local-limit argument.

## Relationship to prior work
Lanchier and Reed (2018/2019) established uniform stationarity and exact finite composition counts in the equal-transfer-rate bank model. Their 2022 work treats multiple-bank extensions and large-money-temperature account marginals. Sakagawa (2026) supplies the transfer-dependent product stationary law and proves large-population, *diverging-money-temperature* one-site limits; his analysis distinguishes the positive-side and nonpositive-side transfer-rate regimes. The present result instead fixes positive *finite* wealth and credit densities and identifies the entire \(O(1)\) reserve law, its explicit rate-ratio sensitivity, and its asymptotic independence from any fixed finite set of accounts. The finite counting formulas and general local-limit technology are credited; only their specific joint reserve–wealth consequence is assessed here.

## Limitations
The theorem requires \(0<p\le q\le1\), strictly positive finite limits \(\kappa,\delta\), a symmetric connected interaction graph and stationary initialization. It does not cover the potentially nonsaturated \(p>q\) regime, capacities growing faster than \(N\), variable transfer rates beyond the specified two-level form, dynamical mixing, or a convergence-rate estimate. Historical priority may be affected by general boundary-ensemble theorems not located during the comparison; no independent validation is claimed.

## References
1. Hironobu Sakagawa, *Convergence of stationary distributions for a class of zero-range processes and its application to a wealth distribution model with debt*, arXiv:2610.00901v1, first posted 2026-10-01. https://arxiv.org/html/2610.00901v1 (Proposition 1.1, Theorem 1.4, Sections 2–3).
2. Nicolas Lanchier and Stephanie Reed, *Rigorous results for the distribution of money on connected graphs (models with debts)*, arXiv:1812.10359v1, first posted 2018-12-26; Journal of Statistical Physics 176 (2019), 1115–1137. https://arxiv.org/abs/1812.10359 (Theorem 2 and Lemma 10).
3. Nicolas Lanchier and Stephanie Reed, *Distribution of money on connected graphs with multiple banks*, arXiv:2201.11930, first posted 2022-01-28. https://arxiv.org/abs/2201.11930 (Theorems 1–2 and reversible stationary law).
