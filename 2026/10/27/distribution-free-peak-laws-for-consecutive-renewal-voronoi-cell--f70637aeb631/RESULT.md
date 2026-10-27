# Distribution-free peak laws for consecutive renewal Voronoi cells

## Finding
For a two-sided renewal configuration with identically distributed independent positive atomless gaps, count the cells that are strictly longer than both neighboring cells. Their peak indicators have a universal probability \(1/4\), a four-term covariance profile
\[
\operatorname{Cov}(M_0,M_h)=
\begin{cases}
-1/16,&h=1,\\
-5/144,&h=2,\\
1/48,&h=3,\\
0,&h\ge4,
\end{cases}
\]
and a distribution-free finite-window variance. In particular, there is a surprising *positive* lag-three covariance after two negative lags. The long-run variance per indexed cell equals \(5/144\), only \(5/27\) of the variance calculated by incorrectly treating successive peak indicators as independent.

## Assumptions and scope
Let \((G_i)_{i\in\mathbb Z}\) be i.i.d. random variables with an atomless probability distribution on \((0,\infty)\). Define an increasing two-sided point configuration by \(T_0=0\) and \(T_{i+1}-T_i=G_i\) for all integer \(i\). With finite mean gaps, this describes the Palm version of a stationary renewal point process; finite moments are not needed for the indexed peak statements themselves. The Voronoi cell surrounding \(T_i\) has length \(V_i=(G_{i-1}+G_i)/2\). Set \(M_i=\mathbf1\{V_i>V_{i-1},\;V_i>V_{i+1}\}\) and \(S_n=\sum_{i=1}^{n}M_i\), for every integer \(n\ge1\). Strict inequalities are almost sure: a difference of independent atomless gaps vanishes with probability zero.

The precise statements are
\[
\begin{aligned}
\mathbb EM_i&=1/4,\\
\mathbb E[M_iM_{i+h}]&=0,\;1/36,\;1/12,\;1/16 \quad\text{for }h=1,2,3,\text{ and }h\ge4,\\
\operatorname{Var}(S_n)&=
\begin{cases}3/16,&n=1,\\1/4,&n=2,\\35/144,&n=3,\\5(n+4)/144,&n\ge4.\end{cases}
\end{aligned}
\]
Moreover \(n^{-1/2}(S_n-n/4)\Rightarrow N(0,5/144)\). Here \(N(0,5/144)\) denotes a centered Gaussian law with variance \(5/144\).

## Proof
The fundamental cancellation is
\[
V_i-V_{i-1}=\frac{G_i-G_{i-2}}2,
\qquad V_i-V_{i+1}=\frac{G_{i-1}-G_{i+1}}2.
\]
Consequently
\[
M_i=\mathbf1\{G_i>G_{i-2}\}\mathbf1\{G_{i-1}>G_{i+1}\}.
\]
The two comparisons concern four distinct i.i.d. gaps and are independent, with probabilities \(1/2\) each. Therefore \(\mathbb EM_i=1/4\).

At lag one, both indicators cannot be one: \(M_i=1\) requires \(V_i>V_{i+1}\), whereas \(M_{i+1}=1\) requires \(V_{i+1}>V_i\). Thus \(\mathbb E[M_iM_{i+1}]=0\).

At lag two, the four requirements separate by parity into two independent strict three-term chains:
\(G_{i+2}>G_i>G_{i-2}\) and \(G_{i-1}>G_{i+1}>G_{i+3}\). Every one of the six orders of three i.i.d. atomless gaps is equally likely, hence the joint probability is \((1/6)^2=1/36\).

At lag three, the simultaneous event is the intersection of \(G_i>G_{i-2}\), \(G_{i-1}>G_{i+1}\), \(G_{i+3}>G_{i+1}\), and \(G_{i+2}>G_{i+4}\). The two outside comparisons each have probability \(1/2\) and are independent of the shared-gap triple. In the triple, \(G_{i+1}\) must be the smallest of three i.i.d. atomless gaps, probability \(1/3\). Hence \(\mathbb E[M_iM_{i+3}]=1/12\).

For \(h\ge4\), the gap sets \(\{G_{i-2},G_{i-1},G_i,G_{i+1}\}\) and \(\{G_{i+h-2},G_{i+h-1},G_{i+h},G_{i+h+1}\}\) are disjoint. Thus the indicators are independent, so their joint probability is \(1/16\). Subtracting \((1/4)^2\) proves all covariance values. In particular, the indicators form a stationary *3-dependent* process, not a 2-dependent one.

Writing \(\gamma_h=\operatorname{Cov}(M_0,M_h)\), the variance of the sum is
\[
\operatorname{Var}(S_n)=n\gamma_0+2\sum_{h=1}^{\min(3,n-1)}(n-h)\gamma_h,
\qquad \gamma_0=3/16.
\]
Substitution yields \(3/16,1/4,35/144\) for \(n=1,2,3\). For \(n\ge4\) it simplifies to
\[
\frac{3n}{16}-\frac{n-1}{8}-\frac{5(n-2)}{72}+\frac{n-3}{24}=\frac{5(n+4)}{144}.
\]
Finally, the bounded stationary 3-dependent sequence satisfies a central limit theorem with nonzero long-run variance
\[
\gamma_0+2\gamma_1+2\gamma_2+2\gamma_3=\frac5{144}.
\]
For completeness, one can partition the indices into length \(b_n=\lfloor n^{1/3}\rfloor\) blocks separated by three discarded indices. The retained block sums are independent. The number of discarded indices is \(O(n/b_n)\), whose centered contribution has variance \(O(n/b_n)=o(n)\), by 3-dependence. The retained centered block sums have total variance asymptotic to \(5n/144\). Each block is bounded in absolute deviation by \(b_n\), so its third absolute centered moment is at most \(b_n\) times its second moment; summed over blocks this is \(O(nb_n)=o(n^{3/2})\). The Lyapunov central limit theorem applies. Adding the negligible discarded contribution proves the stated Gaussian limit.

## Verification
The standalone standard-library program `verify_peak_law.py` independently enumerates all orderings of the relevant gap variables. It reproduces the one-point and pairwise probabilities for lags one through four and enumerates complete peak-count windows for sizes one through six. There are 28 exact-rational comparisons, including independent calculations of both means and variances. The analytic proof, not the finite enumeration, establishes the all-size statement and limit law. Run `python3 verify_peak_law.py` from the directory containing the packaged file.

## Relationship to prior work
Járai-Szabó and Néda (public preprint 2004) derive the one-dimensional *marginal* Poisson–Voronoi cell-length density from two exponential neighbor gaps. Their formula supplies the geometric setting but does not compute consecutive-cell peak counts, their lag covariance, or a distribution-free renewal theorem. Gabrielli and Torquato (public preprint May 2004), in a different one-dimensional superhomogeneous model, give exact two-cell length statistics and correlation-sum identities, not strict local peak-indicator covariances. The classical peak-count problem is also addressed by Ku and Seneta (1994), whose accessible description emphasizes stationary **Gaussian** ARMA models, particularly MA(1), and by Bandt and Shiha (2007), who develop ordinal-pattern formulas for Gaussian and ARMA models. These are relevant partially overlapping formulations; the present statement concerns **every atomless i.i.d. gap law** and gives its exact four-lag profile and finite-window variance. The full texts of the latter two articles were not available for a decisive all-formulation exclusion; an earlier distribution-free equivalent remains a priority risk.

## Limitations
The theorem concerns indexed consecutive cells under i.i.d. atomless gaps. It does not assert corresponding formulas for a fixed Euclidean observation window, dependent gaps, ties, multidimensional Voronoi tessellations, peak heights, or joint distributions beyond the stated moments and Gaussian limit. The results give no independent audit or proof of historical priority.

## References
1. F. Járai-Szabó and Z. Néda, *On the size-distribution of Poisson Voronoi cells*, arXiv:cond-mat/0406116 (first public 4 June 2004), https://arxiv.org/abs/cond-mat/0406116.
2. A. Gabrielli and S. Torquato, *Voronoi and Voids Statistics for Super-homogeneous Point Processes*, arXiv:cond-mat/0405115 (first public 6 May 2004), https://arxiv.org/abs/cond-mat/0405115.
3. S. Ku and E. Seneta, *The number of peaks in a stationary sample and orthant probabilities*, J. Time Series Anal. 15 (1994), 385–403, doi:10.1111/j.1467-9892.1994.tb00201.x.
4. C. Bandt and F. Shiha, *Order Patterns in Time Series*, J. Time Series Anal. 28 (2007), 646–665, doi:10.1111/j.1467-9892.2007.00528.x.
5. W. I. Newman, D. L. Turcotte and B. D. Malamud, *Emergence of patterns in random processes*, Phys. Rev. E 86 (2012), 026103, doi:10.1103/PhysRevE.86.026103.
