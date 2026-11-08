# A Dirichlet law and Gaussian welfare scaling for gap-product facility selection

## Finding

Fix an integer \(k\ge 2\). Let \(X_1,\ldots,X_n\) be independent \(\operatorname{Uniform}[0,1]\) agent positions, where \(n>k\). Truthfully reported positions are used by the **gap-product selection rule**: for each set of \(k\) distinct agents whose sorted positions are \(u_1<\cdots<u_k\), choose that set with probability proportional to
\[
w(u_1,\ldots,u_k)=\prod_{j=1}^{k-1}(u_{j+1}-u_j).
\]
Open facilities at the chosen locations. Write \(Y_{n,1}<\cdots<Y_{n,k}\) for the random facilities; write \(C_{n,k}\) for total realized nearest-facility distance, and \(\mathrm{OPT}_{n,k}\) for the minimum total distance achievable by \(k\) arbitrary facility sites on the line.

As \(n\to\infty\) with \(k\) fixed, the \(k+1\) spacings
\[
(Y_{n,1},\;Y_{n,2}-Y_{n,1},\ldots,Y_{n,k}-Y_{n,k-1},\;1-Y_{n,k})
\]
converge in distribution to
\[
(G_0,\ldots,G_k)\sim\operatorname{Dirichlet}(1,\underbrace{2,\ldots,2}_{k-1},1).
\]
Moreover, with
\[
T_k=\frac{G_0^2+G_k^2}{2}+\frac14\sum_{j=1}^{k-1}G_j^2,
\]
we have the joint convergence
\[
\left(\frac{C_{n,k}}n,\frac{C_{n,k}}{\mathrm{OPT}_{n,k}}\right)
\xrightarrow{d}(T_k,4kT_k),\qquad
\frac{\mathrm{OPT}_{n,k}}n\longrightarrow\frac1{4k}\quad\text{almost surely}.
\]
The exact first two cost moments are
\[
\boxed{\mathbb E T_k=\frac{3k+1}{4k(2k+1)}},\qquad
\boxed{\operatorname{Var}(T_k)=\frac{6k^3+8k^2-3k-3}{16k^2(k+1)(2k+1)^2(2k+3)}}>0.
\]
Consequently, conditional on almost every sequence of sampled locations, the mechanism's **expected** approximation ratio converges to
\[
\boxed{\rho_k=\frac{3k+1}{2k+1}}.
\]
The unconditional mean ratio also converges to \(\rho_k\). For comparison, uniformly selecting \(k\) distinct agents has limiting mean approximation ratio \(2k(k+3)/[(k+1)(k+2)]\), strictly larger by
\[
\frac{(k-1)(k^2+5k+2)}{(k+1)(k+2)(2k+1)}.
\]
Finally, in the **iterated** regime (population first, facility count second),
\[
\boxed{\sqrt{k}\left(4kT_k-\frac32\right)\xrightarrow[k\to\infty]{d}N\!\left(0,\frac34\right)}.
\]
In particular \(\rho_2=7/5\), \(\rho_3=10/7\), and \(\rho_k\uparrow3/2\). For each fixed \(k\), the realized ratio remains random even in an arbitrarily large population; concentration occurs only in the subsequent \(k\to\infty\) limit.

## Assumptions and scope

All random locations are independent and exactly uniform on the compact interval \([0,1]\). Reports are truthful; the result does **not** claim incentive compatibility beyond values already established in the cited work. Agents are labeled, so subsets refer to distinct agent labels, but ties have probability zero. The number of facilities is fixed during the population limit. The ratio uses total realized social cost for an actual randomized draw, not the cost averaged over the rule; its conditional mean is treated separately. The second limit is iterated, not a joint rate result for growing \(k=k(n)\).

## Proof

**1. Weak limit of weighted sampling.** Let \(\mu_n=n^{-1}\sum_{i=1}^n\delta_{X_i}\). Almost surely, \(\mu_n\) converges weakly to Lebesgue measure \(\lambda\) on \([0,1]\). For any bounded continuous function \(h\) on ordered \(k\)-tuples, define the symmetric bounded continuous kernel
\[
H_h(x_1,\ldots,x_k)=w(x_{(1)},\ldots,x_{(k)})\,h(x_{(1)},\ldots,x_{(k)}).
\]
The weight vanishes when any adjacent positions coincide, so it is continuous across ordering collisions. The average of \(H_h\) over all distinct ordered \(k\)-tuples of indices differs from its \(\mu_n^{\otimes k}\)-integral by \(O_k(1/n)\), since repeated-index tuples have proportion \(O_k(1/n)\). Weak convergence of product measures therefore makes both the weighted numerator and its corresponding denominator converge to their \(\lambda^{\otimes k}\)-integrals. The limiting denominator is strictly positive. Dividing establishes conditional weak convergence, almost surely, of the selected sorted locations to the measure on \(0<u_1<\cdots<u_k<1\) with density proportional to \(\prod_{j=1}^{k-1}(u_{j+1}-u_j)\).

**2. Exact Dirichlet normalization.** Make the unit-Jacobian substitution \(g_0=u_1\), \(g_j=u_{j+1}-u_j\) for \(1\le j<k\), and \(g_k=1-u_k\). The new variables are nonnegative and sum to one. Their density is proportional to \(\prod_{j=1}^{k-1}g_j\). Its normalization is \(\Gamma(2k)\), because the simplex integral equals \(\Gamma(1)^2\Gamma(2)^{k-1}/\Gamma(2k)=1/\Gamma(2k)\). This is the claimed Dirichlet law.

**3. Cost and empirical optimum.** For arbitrary ordered facilities \(0\le u_1<\cdots<u_k\le1\), integration over their Voronoi cells yields
\[
\int_0^1\min_j|x-u_j|\,dx
=\frac{u_1^2+(1-u_k)^2}{2}+\frac14\sum_{j=1}^{k-1}(u_{j+1}-u_j)^2.
\]
For every facility vector, the integrand is a 1-Lipschitz function of \(x\). Hence the difference between its empirical and continuum average, uniformly over facility vectors, is at most \(W_1(\mu_n,\lambda)\to0\) almost surely. This proves convergence of realized normalized cost by the continuous mapping theorem. For the population optimum, partition \([0,1]\) into \(k\) Voronoi intervals of lengths \(\ell_j\). On each, its best possible one-site uniform transportation cost is \(\ell_j^2/4\). Thus the continuum cost is at least \(\sum_j\ell_j^2/4\ge1/(4k)\), with equality at the midpoints of \(k\) equal intervals. The preceding uniform empirical approximation gives \(\mathrm{OPT}_{n,k}/n\to1/(4k)\), even if the finite optimum is restricted to reported locations, because those reports become dense almost surely. The joint limit and ratio follow.

**4. Dirichlet moments.** For a Dirichlet vector with parameters \(\alpha_i\), total \(a=\sum_i\alpha_i\), and nonnegative integer exponents \(r_i\),
\[
\mathbb E\prod_iG_i^{r_i}=\frac{\prod_i(\alpha_i)_{r_i}}{(a)_{\sum_i r_i}},
\qquad (b)_r=b(b+1)\cdots(b+r-1).
\]
Here \(a=2k\), the endpoint parameters are \(1\), and the interior parameters are \(2\). Inserting second and fourth moments into the quadratic expression for \(T_k\) gives
\[
\mathbb E T_k=\frac{3k+1}{4k(2k+1)},\qquad
\mathbb E T_k^2=\frac{9k^2+27k+20}{16k(k+1)(2k+1)(2k+3)}.
\]
Subtracting the squared mean yields the displayed variance, strictly positive for every \(k\ge2\). For unweighted uniform selection, the gaps instead have \(\operatorname{Dirichlet}(1,\ldots,1)\), giving mean cost \((k+3)/[2(k+1)(k+2)]\) and the displayed positive difference of expected ratios.

**5. Convergence of expected ratio.** Almost surely, the conditional mean \(\mathbb E[C_{n,k}/n\mid X_1,\ldots,X_n]\) converges to \(\mathbb ET_k\), and \(\mathrm{OPT}_{n,k}/n\to1/(4k)\). Their quotient converges to \(\rho_k\). To pass to unconditional expected approximation ratios, use the published worst-case expected-cost bound \(\mathbb E[C_{n,k}\mid X_1,\ldots,X_n]\le2k\,\mathrm{OPT}_{n,k}\) for this exact mechanism [2, Lemma 5]. The nonnegative conditional ratios are uniformly bounded by \(2k\), allowing dominated convergence. This use of the published inequality is explicit; the new distributional theorem does not assert a deterministic \(2k\) bound on each randomly realized ratio.

**6. High-facility Gaussian transition.** Represent the Dirichlet spacings as independent gamma variables divided by their sum: the two endpoints have \(\operatorname{Gamma}(1,1)\) laws, and the \(k-1\) interior variables \(B_j\) have \(\operatorname{Gamma}(2,1)\) laws. Writing the scaled cost \(R_k=4kT_k\), the endpoint contributions are \(O_p(1/k)\) in the numerator and denominator of
\[
R_k=\frac{k^{-1}\sum_{j=1}^{k-1}B_j^2+2k^{-1}(A_0^2+A_k^2)}{\bigl(k^{-1}\sum_{j=1}^{k-1}B_j+k^{-1}(A_0+A_k)\bigr)^2}.
\]
The gamma moments give \(\mathbb EB_j=2\), \(\mathbb EB_j^2=6\), \(\operatorname{Var}(B_j)=2\), \(\operatorname{Cov}(B_j^2,B_j)=12\), and \(\operatorname{Var}(B_j^2)=84\). The bivariate central limit theorem and the delta method applied to \((u,v)\mapsto u/v^2\) at \((6,2)\), with gradient \((1/4,-3/2)\), give asymptotic variance
\[
(1/4,-3/2)\begin{pmatrix}84&12\\12&2\end{pmatrix}
\begin{pmatrix}1/4\\-3/2\end{pmatrix}=3/4.
\]
The endpoint terms vanish on the \(k^{-1/2}\) scale, yielding the claimed normal limit.

## Verification

The standalone `verify_gap_product.py` performs 277 deterministic algebraic, exact-enumeration, and seeded Monte Carlo checks. In particular, for each integer \(2\le k\le64\), it checks the two exact moment identities, strict variance positivity, and the positive difference from uniform selection using rational arithmetic. It also enumerates all weighted \(k\)-subsets on deterministic grids for \(k=2,3,4\), and independently samples the normalized gamma representation for \(k=2,3,6,12\). Execute using `python3 verify_gap_product.py`; its summary ends `PASS 277 checks; analytic proof remains necessary`.

The numerical tests do **not** prove convergence in \(n\) or \(k\), nor do they establish strategyproofness or publication priority. Those analytical conclusions follow from the preceding arguments and cited primary mechanism definitions.

## Relationship to prior work

The product-of-consecutive-gaps selection law and the sharp worst-case \(2k\) expected approximation bound were introduced in Jia [1] and independently in Chan, Lin, and Wang [2]. For \(k=2\), the same distance-weighted pair selection appeared earlier as Global Pair in Ma and Peng [3]. The cited works analyze strategic incentives and worst-case approximation. The present statement instead identifies the **stochastic population law** for uniform i.i.d. locations, its full spacings distribution, exact average-case ratios and variances, and the iterated high-facility central limit theorem. Nothing here claims the known \(2k\) bound or the known incentive boundary as new. The known rule is not strategyproof when \(k\ge4\); our probabilistic conclusions apply to truthful inputs without claiming strategic robustness in that regime.

## Limitations

The population density is uniform; the Dirichlet identification and rational formulas need not hold for nonuniform locations. The limit takes \(n\to\infty\) **before** \(k\to\infty\) and supplies no simultaneous growth theorem. The individual realized ratio need not be bounded by the published worst-case guarantee for expected cost. A related earlier full manuscript [1] was not accessible for a complete direct full-text comparison; the available abstract and substantial synopsis were checked, and publication priority remains conditional on unindexed or inaccessible results. No independent scientific audit is claimed.

## References

[1] Jianhao Jia, *Product Gap Mechanisms for Multi-Facility Location*, first public August 20, 2026, arXiv:2608.19633, https://arxiv.org/abs/2608.19633.

[2] Hau Chan, Jianan Lin, and Chenhao Wang, *Randomized Strategyproof Facility Location: Two Facilities and Beyond*, first public August 23, 2026, arXiv:2608.22484, https://arxiv.org/abs/2608.22484. Public full text: https://www.researchgate.net/publication/413593510_Randomized_Strategyproof_Facility_Location_Two_Facilities_and_Beyond.

[3] Mengfan Ma and Bo Peng, *Breaking the 4-Approximation Barrier in Strategyproof Two-Facility Location*, first public August 10, 2026, arXiv:2608.09061, https://arxiv.org/abs/2608.09061.
