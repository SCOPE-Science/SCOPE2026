# Spectral-scale stationary fluctuations of hub-seeded SIS dynamics on stars

## Finding

Fix real parameters \(\beta>0\) and \(\eta>0\). On the star with one hub and \(m\ge2\) leaves, every infected vertex recovers at rate one; each infected vertex infects each susceptible neighbor at rate \(\lambda_m=\beta/\sqrt m\). Independently, only a susceptible hub receives external infections, at rate \(\eta\), including when every vertex is susceptible. Denote the stationary hub infection indicator by \(H_m\), the number of infected leaves by \(K_m\), and \(U_m=K_m/(\beta\sqrt m)\).

The finite-state chain has a unique invariant law, and its stationary joint law satisfies
\[
 (U_m,H_m)\ \Longrightarrow\ (U,H),\qquad m\longrightarrow\infty.
\]
The first coordinate is supported on \((0,1)\) with density
\[
 f_{\beta,\eta}(u)=\frac{u^{\eta-1}e^{\beta^2u}}{Z_{\beta,\eta}},\quad
 Z_{\beta,\eta}=\int_0^1 u^{\eta-1}e^{\beta^2u}\,du,
 \quad 0<u<1,
\]
and its joint law with the hub indicator is specified by
\[
 \Pr(H=1\mid U=u)=u. 
\]
Every nonnegative integer moment of \(U_m\) converges to the corresponding moment of \(U\). In particular, \(\operatorname{Var}(U)>0\) and
\[
 \lim_{m\to\infty}\frac{\operatorname{Var}(K_m)}m
 =\beta^2\operatorname{Var}(U)>0.
\]
Writing \(X_{m,i}\in\{0,1\}\) for the indicator that leaf \(i\) is infected, for any two distinct leaves \(i\ne j\),
\[
 \lim_{m\to\infty}\sqrt m\,\operatorname{Cov}(H_m,X_{m,i})
  =\beta\operatorname{Var}(U),\qquad
 \lim_{m\to\infty}m\,\operatorname{Cov}(X_{m,i},X_{m,j})
  =\beta^2\operatorname{Var}(U).
\]
The moments have the exact integral representation
\[
 \mathbb E[U^r]=
 \frac{\int_0^1 u^{\eta+r-1}e^{\beta^2u}\,du}
 {\int_0^1 u^{\eta-1}e^{\beta^2u}\,du},\qquad r\in\{0,1,2,\ldots\}.
\]
The limiting density also has an exact profile change: if \(0<\eta<1\), it is decreasing throughout \((0,1)\) when \(\beta^2\le1-\eta\); when \(\beta^2>1-\eta\), it decreases to a unique interior minimum at \(u=(1-\eta)/\beta^2\) and subsequently increases toward the right endpoint. For \(\eta\ge1\), it is strictly increasing.

## Assumptions and scope

The graph is the simple star \(K_{1,m}\) with labelled leaves. Infection clocks on edges, recovery clocks, and external hub infection clocks are independent exponentials with the rates stated above. The parameters \(\beta,\eta\) are fixed as \(m\to\infty\); the external infection is present even in the all-susceptible configuration. Thus this is an irreducible, permanently seeded SIS/contact process, **not** the usual absorbing contact process or its quasistationary law. No infection is externally introduced directly to leaves. All expectations, limits, and covariances in the theorem refer to the unique finite-size stationary law.

## Proof

**1. Exact reduced chain.** The pair \((H_m,K_m)\) is a continuous-time Markov chain. Its only nonzero off-diagonal rates, for \(0\le k\le m\), are
\[
 (0,k)\to(1,k):\ \eta+\beta k/\sqrt m,\qquad
 (1,k)\to(0,k):\ 1,
\]
\[
 (1,k)\to(1,k+1):\ \beta(m-k)/\sqrt m\quad(k<m),
 \qquad (z,k)\to(z,k-1):\ k\quad(k>0).
\]
External hub activation and the positive infection/recovery rates make this finite chain irreducible. Exchangeability of leaves shows its stationary law determines all one- and two-leaf marginals.

**2. Stationary tightness, including moments.** Applying stationary generator balance to \(K_m\) yields
\[
 \mathbb E[K_m]
 =\frac\beta{\sqrt m}\mathbb E[H_m(m-K_m)]\le\beta\sqrt m.
\]
For every integer \(r\ge2\), use the inequalities
\[
 k\bigl((k-1)^r-k^r\bigr)\le-rk^r+C_r k^{r-1},
\]
\[
 \frac\beta{\sqrt m}(m-k)\bigl((k+1)^r-k^r\bigr)
 \le C_r\beta\sqrt m\bigl(1+k^{r-1}\bigr)
\]
for \(0\le k\le m\), with the first inequality interpreted as zero at \(k=0\). Stationarity and induction give \(\sup_{m\ge2}\mathbb E[U_m^r]<\infty\) for every fixed \(r\). In particular, the stationary laws are tight and are uniformly integrable in every polynomial degree.

**3. Limiting generator.** For a smooth test function \(g(u,z)\), the rescaled finite generator converges, uniformly in \(u\) on bounded sets, to
\[
 \mathcal Ag(u,z)
 =(z-u)\partial_u g(u,z)
 +q_z(u)\bigl[g(u,1-z)-g(u,z)\bigr],
\]
where \(q_0(u)=\eta+\beta^2u\) and \(q_1(u)=1\). Indeed the rescaled leaf birth and death drifts are \(z(1-\beta u/\sqrt m)\) and \(-u\), and their quadratic jump corrections are uniformly \(O(m^{-1/2})\) on compact subsets. The standard martingale-problem compactness argument, using the preceding moment bounds and the Lipschitz deterministic flows between hub switches, implies that every subsequential stationary weak limit is invariant for this well-posed piecewise-deterministic Markov process (PDMP).

**4. Support and uniqueness of the limiting invariant law.** Between hub switches, \(dU_t/dt=H_t-U_t\). Since the switching does not jump \(U_t\),
\[
 (U_t-1)_+\le e^{-t}(U_0-1)_+.
\]
The invariant law therefore has support within \([0,1]\). Every hub-switching rate is at least \(c=\min\{\eta,1\}>0\). Conditional on one or more switches before time \(t\), the final position has an absolutely continuous law: conditional on preceding switch times and the number of switches, the final switching time has a density, and its effect on the position at time \(t\) has a nonzero derivative. The probability of no switch is at most \(e^{-ct}\). Invariance, followed by \(t\to\infty\), therefore implies that the stationary joint law has Lebesgue densities \(f_0,f_1\) on \((0,1)\) and no atoms at endpoints.

Adding the stationary forward equations gives a constant probability current
\[
 J=-uf_0(u)+(1-u)f_1(u).
\]
Integrability and nonnegativity force \(J=0\): if \(J>0\), then \(f_1(u)\ge J/(1-u)\) is not integrable near one; if \(J<0\), then \(f_0(u)\ge(-J)/u\) is not integrable near zero. Hence \((1-u)f_1=uf_0\). Substitution in the \(z=0\) stationary equation,
\[
 0=\frac{d}{du}(uf_0)-(\eta+\beta^2u)f_0+f_1,
\]
gives the unique integrable solution (up to a scalar)
\[
 f_0(u)=Cu^{\eta-1}(1-u)e^{\beta^2u},\qquad
 f_1(u)=Cu^\eta e^{\beta^2u}.
\]
Normalization fixes \(C=Z_{\beta,\eta}^{-1}\). The two displayed densities directly satisfy both forward equations, proving existence and uniqueness. Thus all subsequential limits coincide, proving joint weak convergence.

**5. Polynomial moments and correlations.** The uniform moment bounds in Step 2 imply convergence of all polynomial moments of \((U_m,H_m)\). The limit densities give \(\mathbb E[H\mid U]=U\), so \(\operatorname{Cov}(H,U)=\operatorname{Var}(U)\). Exchangeability implies
\[
 \mathbb E[X_{m,i}]=\frac{\mathbb E[K_m]}m,\quad
 \mathbb E[X_{m,i}X_{m,j}]=\frac{\mathbb E[K_m(K_m-1)]}{m(m-1)},\quad
 \mathbb E[H_mX_{m,i}]=\frac{\mathbb E[H_mK_m]}m.
\]
Substituting \(K_m=\beta\sqrt m\,U_m\) proves both covariance limits. The variance limit follows directly. Finally, differentiating \(\log f_{\beta,\eta}\) gives \(\beta^2+(\eta-1)/u\), establishing the stated density-profile classification.

## Verification

The accompanying `verify.py` is executable with Python 3, NumPy, SciPy, and SymPy, as specified in `requirements.txt`. Execute `python verify.py` from the directory containing both files. It checks the two stationary forward equations symbolically, normalization and moment identities numerically, and the exact finite stationary generators for four sizes at three parameter choices. The script also compares the finite-size scaled hub–leaf and leaf–leaf covariances with their limiting formulas. All checks were run against the packaged code. Finite enumeration checks do not prove the weak-convergence theorem; the argument is in Steps 2–5.

## Relationship to prior work

Chatterjee and Durrett derived star-graph survival results for the ordinary absorbing contact process, notably in the strong-survival regime with a diverging product of star degree and squared infection rate. Banerjee, Chatterjee, and Shakkottai treated externally aided epidemics, including strategies concentrating their infection budget at a star's hub, but stipulated that external infection ceases upon extinction and studied extinction-time bounds. Neither statement gives a permanently seeded stationary joint law in the fixed spectral-scale window here.

Cator and Van Mieghem studied exact stationary distributions for star-graph variants of SIS dynamics, including uniform nodal self-infection and a modification preventing absorption. Their work is closely related and should be consulted when applying or extending the present theorem. The accessible abstract does not establish the hub-only stationary limit above, but the full text could not be inspected; consequently, its precise implications remain a literature-priority risk. The resulting two-regime PDMP is also related to telegraph/promoter-switching models in which stationary distributions can be beta-like. The novelty assessed here is the original star-process scaling limit and its graph-level covariance consequences, not the general definition of a PDMP.

## Limitations

The theorem applies to fixed positive \(\beta,\eta\), recovery rate one, one exogenously seeded hub, and homogeneous star-edge rates of order \(m^{-1/2}\). It does not describe the absorbing model's quasistationary law, extinction times after immigration is switched off, simultaneous limits \(\eta\to0\) or \(\beta\to\infty\), non-star graphs, or arbitrary infection-rate heterogeneity. No rate of stationary weak convergence is asserted. Mathematical originality has only been assessed against identified published material; a comprehensive historical priority determination and independent scientific audit remain outstanding.

## References

1. S. Banerjee, A. Chatterjee and S. Shakkottai, *Epidemic Thresholds with External Agents*, arXiv:1312.0938v1, publicly posted 2013-12-03. Relevant material: introduction, definition of finite-lifetime external seeding, Theorem 3, and Appendix B star proof.
2. S. Chatterjee and R. Durrett, *Contact Processes on Random Graphs with Power Law Degree Distributions Have Critical Value 0*, arXiv:0912.1699, Annals of Probability 37 (2009). Relevant material: Lemma 1.1 and star survival bounds.
3. E. Cator and P. Van Mieghem, *Susceptible-infected-susceptible epidemics on the complete graph and the star graph: Exact analysis*, Physical Review E 87, 012811 (2013), DOI: 10.1103/PhysRevE.87.012811. Full text not inspected; accessible publisher abstract and author-hosted search excerpts considered.
4. P. Van Mieghem and E. Cator, *Epidemics in networks with nodal self-infection and the epidemic threshold*, Physical Review E 86, 016116 (2012), DOI: 10.1103/PhysRevE.86.016116. Accessible abstract compared.
5. U. Herbach, *Stochastic Gene Expression with a Multistate Promoter: Breaking Down Exact Distributions*, SIAM Journal on Applied Mathematics 79 (2019), DOI: 10.1137/18M1181006. Related stationary PDMP framework; accessible abstract considered.
