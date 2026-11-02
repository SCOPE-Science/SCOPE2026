# Two-scale price crossover for optimal second-order coherence on weighted stars

## Finding

For an undirected star with \(m\ge 3\) leaves and positive spoke conductances \(w_1,\ldots,w_m\), consider the inverse-square Laplacian objective
\[
\mathcal F(w)=\sum_{k=2}^{m+1}\lambda_k(L(w))^{-2}.
\]
For arbitrary strictly positive prices \(p_1,\ldots,p_m\) and budget \(B>0\), the unique positive allocation minimizing \(\mathcal F\) subject to \(\sum_i p_iw_i\le B\) satisfies the strict universal price-compression law: whenever \(p_i>p_j\),
\[
\left(\frac{p_j}{p_i}\right)^{1/2}
<\frac{w_i^*}{w_j^*}
<\left(\frac{p_j}{p_i}\right)^{1/3}.
\tag{1}
\]
If one spoke has price \(Q>0\) and the other \(m-1\) spokes have price \(1\), write \(t_m(Q)\) for the unique positive root of
\[
Q\left((m-1)(m+2)t^3+t^2\right)=(m-1)t+m^2.
\tag{2}
\]
The unique optimum gives conductance \(B/(m-1+Qt_m(Q))\) to each ordinary spoke and \(Bt_m(Q)/(m-1+Qt_m(Q))\) to the distinguished spoke. In particular, \(t_m(Q)<1\) exactly for \(Q>1\), with equality at \(Q=1\).

The root displays two distinct, exact many-spoke price scales. First, if \(Q=\kappa m^{3/2}\) with fixed \(\kappa>0\), the fraction of total budget assigned to the distinguished spoke tends to
\[
\frac{\kappa^{2/3}}{1+\kappa^{2/3}}.
\tag{3}
\]
Second, if \(Q=\tau m^6\) with fixed \(\tau>0\), then
\[
m^2t_m(\tau m^6)\longrightarrow s_\tau,
\qquad \tau s_\tau^2(1+s_\tau)=1,
\tag{4}
\]
where \(s_\tau>0\) is uniquely determined. The outer regimes are
\[
\lim_{m\to\infty}t_m(Q)=Q^{-1/3}\quad(Q>0\text{ fixed}),
\qquad
\lim_{Q\to\infty}\sqrt Q\,t_m(Q)=m\quad(m\text{ fixed}).
\tag{5}
\]
The \(m^{3/2}\) budget-concentration scale and \(m^6\) conductance-ratio crossover are different phenomena.

## Assumptions and scope

The network is the simple star \(K_{1,m}\). Edge conductance is continuously and independently adjustable and strictly positive; there are no upper bounds other than the linear price budget. \(L(w)\) is the symmetric weighted graph Laplacian with eigenvalues \(0=\lambda_1<\lambda_2\le\cdots\le\lambda_{m+1}\). The normalized second-order coherence of the standard double-integrator model
\[
\dot x=v,\qquad \dot v=-\beta L(w)x-\beta L(w)v+\xi
\]
with independent unit-covariance white noise \(\xi\), fixed \(\beta>0\), and the mean position removed is \(\mathcal H_{\mathrm{SO}}=\mathcal F/(2\beta^2(m+1))\). Therefore minimizing this coherence is exactly the claimed \(\mathcal F\)-minimization. All claims concern continuous edge conductances and this particular common-gain second-order model, not discrete-time mixing rates or general feedback systems.

## Proof

**1. Exact spectral trace identity.** Put \(n=m+1\), let \(e_0\) be the hub coordinate, let \(e_i\) denote leaf \(i\), and define \(z_i=e_i-n^{-1}\mathbf 1\), \(r_i=w_i^{-1}\). The graph incidence matrix has columns \(e_i-e_0\). Since \((e_j-e_0)^Tz_i=\delta_{ij}\) and \(\sum_i(e_i-e_0)z_i^T=I-n^{-1}\mathbf1\mathbf1^T\), one has
\[
L^\dagger=\sum_{i=1}^m r_i z_i z_i^T.
\]
Here \(L^\dagger\) is the Moore--Penrose pseudoinverse. Because \(z_i^Tz_j=\delta_{ij}-1/n\), taking the square trace yields the exact identity
\[
\mathcal F(w)=a_m\sum_{i=1}^m w_i^{-2}
+d_m\left(\sum_{i=1}^m w_i^{-1}\right)^2,
\quad
a_m=\frac{m-1}{m+1}>0,\quad d_m=\frac1{(m+1)^2}>0.
\tag{6}
\]
The coherence normalization is the standard second-order modal Lyapunov calculation: each positive Laplacian eigenvalue \(\lambda\) contributes positional variance \((2\beta^2\lambda^2)^{-1}\); the zero mode is removed.

**2. Global existence, uniqueness and price ratios.** Each function \(w_i\mapsto w_i^{-2}\) is strictly convex. The function \(S(w)=\sum_iw_i^{-1}\) is positive convex on the positive orthant, hence \(S(w)^2\) is convex; (6) is strictly convex. It diverges when any coordinate tends to zero with the budget bounded, and scaling every coordinate upward decreases it. Thus the unique minimizer exists in the positive orthant and exhausts the budget. Stationarity with multiplier \(\Lambda>0\) gives
\[
\Lambda p_i=2a_mw_i^{-3}+2d_mS(w)w_i^{-2}.
\tag{7}
\]
At the same \(S(w)\), the right side decreases strictly with \(w_i\), so \(p_i>p_j\) implies \(t=w_i/w_j\in(0,1)\). Dividing the equations gives
\[
\frac{p_i}{p_j}=t^{-3}
\frac{a_m+d_mS(w)w_i}{a_m+d_mS(w)w_j}.
\]
Since \(a_m,d_m,S(w)>0\), the final fraction lies strictly between \(t\) and \(1\). Therefore \(t^{-2}<p_i/p_j<t^{-3}\), proving (1). The inequalities are strict and apply to unrestricted, unequal price vectors.

**3. Exact one-premium-spoke solution.** Uniqueness and permutations of the ordinary spokes imply that their optimal conductances coincide, say \(u\), while the distinguished spoke has conductance \(v=tu\). Budget equality gives \(u=B/(m-1+Qt)\). Dividing its stationarity equation by an ordinary spoke's equation and clearing denominators yields (2). Its polynomial has coefficient-sign sequence \(+,+,-,-\), hence exactly one positive root by Descartes' rule and continuity (alternatively, it has one positive minimum and one positive zero). At \(t=1\), the polynomial equals \((Q-1)(m^2+m-1)\), proving the price ordering. Strict convexity proves this stationary point is the unique global minimizer.

**4. Large-network limits and their distinct scales.** Divide (2) by \(m^2\) and use \((m-1)(m+2)/m^2\to1\). If \(Q>0\) is fixed, the unique positive root stays bounded above and below, and its only possible limit satisfies \(Qt^3=1\). Hence the first limit of (5). If \(m\) is fixed and \(Q\to\infty\), substitute \(t=y/\sqrt Q\) in (2). The unique positive limiting solution is \(y=m\), giving the second limit of (5).

For \(Q=\kappa m^{3/2}\), substitute \(t=u/\sqrt m\) and divide (2) by \(m^2\). The unique positive limit is determined by \(\kappa u^3=1\), hence \(u\to\kappa^{-1/3}\). The premium-spoke budget fraction is \(Qt/(m-1+Qt)\), whose limit is (3). For \(Q=\tau m^6\), substitute \(t=s/m^2\) and divide by \(m^2\); the limiting equation is \(\tau(s^3+s^2)=1\), with a unique positive root. Positivity and the one-root property bound the rescaled roots away from zero and infinity in each scaling, making these limiting arguments rigorous. This proves (4) and completes the claim.

## Verification

The standalone script `verify.py` checks the pseudoinverse trace identity with exact rational arithmetic on small stars, tests the Laplacian eigenvalue identity numerically, verifies the scalar KKT equations and strict price-ratio bounds, compares the proposed optimizers with thousands of asymmetric feasible allocations, solves general-price nonlinear programs, and checks convergence predictions in all four asymptotic regimes. Its successful replay reported 3,342 assertions. Finite tests are diagnostic only; the infinite and unrestricted claims are proved in the preceding four steps.

Run from a directory containing the provided script with `python verify.py`; dependencies are Python 3, NumPy, SciPy and SymPy.

## Relationship to prior work

Bamieh, Jovanović, Mitra and Patterson (2011) establish spectral coherence formulas and limits of locality for first- and second-order network dynamics on regular lattices. Patterson and Bamieh (2013) explicitly give the inverse-square eigenvalue sum for second-order noisy consensus, and analyze fractal graph scaling. Neither source treats positive-price edge allocation on weighted stars or the two distinct scales (3)--(4). Xiao, Boyd and Kim (2006) optimize a discrete-time first-order stochastic averaging objective, not the present continuous-time second-order trace square. Hassan-Moghaddam and Jovanović (2015) optimize sparsity-promoting first-order undirected network designs with a reciprocal-eigenvalue objective, rather than second-order inverse-square coherence. These distinctions are mathematical objective and domain differences, not merely different terminology. Related spectral-gap star allocation concerns the smallest positive eigenvalue, which alone cannot determine the inverse-square trace.

## Limitations

No claim is made for non-star topologies, negative/zero conductances, edge capacity constraints, heterogeneous position and velocity feedback, or time-discretized stochastic consensus. A zero-priced or unavailable edge is excluded. The formula optimizes stationary mean-square position disagreement, not the fastest transient convergence rate. Exact source novelty cannot be proved by search; unlocated specialist formulations or applications of more general graph-design methods may imply parts of the result. The model is not independently audited, and finite tests do not replace the mathematical proof.

## References

- B. Bamieh, M. R. Jovanović, P. Mitra and S. Patterson, *Coherence in Large-Scale Networks: Dimension-Dependent Limitations of Local Feedback*, arXiv:1112.4011v1 (first public 2011-12-17), https://arxiv.org/abs/1112.4011, especially the second-order transfer-variance formula and Sections II--V.
- S. Patterson and B. Bamieh, *Consensus and Coherence in Fractal Networks*, arXiv:1310.2592v1 (2013-10-09), https://arxiv.org/abs/1310.2592, Section II-B and Eq. (6).
- L. Xiao, S. Boyd and S.-J. Kim, *Distributed Average Consensus with Least-Mean-Square Deviation*, MTNS proceedings, 2006-07-24 to 2006-07-28, https://web.stanford.edu/~boyd/papers/pdf/lmsc_mtns06.pdf.
- S. Hassan-Moghaddam and M. R. Jovanović, *Topology design for stochastically-forced consensus networks*, arXiv:1506.03437 (first posted 2015, revised 2016), https://arxiv.org/abs/1506.03437, especially Section II.
