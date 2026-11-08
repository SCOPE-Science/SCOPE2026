# A hidden co-occupation threshold below fitness condensation

## Finding

A continuous-fitness, locally reset zero-range mean-field model has a **sharp local pair-crowding threshold at \(\nu=1/2\)**, even though its stationary mean density remains finite for every \(0<\nu<1\). This concerns the diagonal (within-site) factorial second moment, not the full variance of the population summed over different sites.

For the definitions below, let \(\mathcal P_\zeta\) be the density-integrated ordered co-occupation pair intensity. Then
\[
\mathcal P_\zeta=2\int_0^1\frac{\ell[\ell+\beta\rho_\zeta q(\ell)]}{[\zeta+1-\ell+r(\ell)][2(\zeta+1-\ell)+r(\ell)]}\,d\ell.
\]
As \(\zeta\downarrow0\),
\[
\begin{array}{ll}
0<\nu<\tfrac12:&\displaystyle\mathcal P_\zeta\longrightarrow\mathcal P_0<\infty,\\[3pt]
\nu=\tfrac12:&\displaystyle\mathcal P_\zeta\sim\frac4{C^2}\log(1/\zeta),\\[3pt]
\tfrac12<\nu<1:&\displaystyle\mathcal P_\zeta\sim 2C^{-1/\nu}J_\nu\zeta^{1/\nu-2},
\end{array}
\]
where
\[
J_\nu=\int_0^\infty\frac{dy}{(1+y^\nu)(2+y^\nu)}
=\frac{\pi(2^{1/\nu-1}-1)}{\nu\sin(\pi(1/\nu-1))}>0.
\]
The intrinsic (diagonal) variance intensity \(\mathcal V_\zeta\) obeys the exact identity \(\mathcal V_\zeta=\rho_\zeta+\mathcal P_\zeta\), and therefore has the same singular threshold. In contrast, \(\rho_\zeta\to\rho_0<\infty\) throughout \(0<\nu<1\).

## Assumptions and scope

Let \(q:[0,1]\to[0,\infty)\) be continuous and strictly positive on \((0,1)\), normalized by \(\int_0^1q(\ell)d\ell=1\), and satisfy \(q(1-x)=O(x^\alpha)\) for some \(\alpha>0\). Let \(r:[0,1]\to[0,\infty)\) be continuous and satisfy \(r(1-x)\sim Cx^\nu\) as \(x\downarrow0\), for \(C>0\) and \(0<\nu<1\). Fix \(0<\beta<1\) with
\[
\beta\int_0^1\frac{q(\ell)}{1-\ell+r(\ell)}\,d\ell<1.
\]
For \(\zeta>0\), set \(\eta=1+\zeta=\beta+\delta\), so \(\delta=1+\zeta-\beta>0\). Write
\[
 d_\zeta(\ell)=\zeta+1-\ell,\quad
 \rho_\zeta=\frac{\displaystyle\int_0^1\frac{\ell\,d\ell}{d_\zeta(\ell)+r(\ell)}}{\displaystyle 1-\beta\int_0^1\frac{q(\ell)\,d\ell}{d_\zeta(\ell)+r(\ell)}},\quad
 b_\zeta(\ell)=\ell+\beta\rho_\zeta q(\ell).
\]
This is the positive self-consistent stationary density and site-input profile of the large-network mean-field equations of Grange (2023).

For every fitness \(\ell\in[0,1]\), cutoff \(\zeta>0\), and integer site multiplicity \(v\ge1\), define the continuous-time Markov chain \(N^{(v)}_{\ell,\zeta}\) on \(\mathbb N_0\) as follows: at occupation \(n\), birth to \(n+1\) has rate \(\ell n+b_\zeta(\ell)/v\), death to \(n-1\) has rate \(\eta n\), and independent total site clearing to zero has rate \(r(\ell)\). Its unique invariant law is \(\pi^{(v)}_{\ell,\zeta}\). The exact quantities studied are
\[
 \mathcal P_\zeta=\int_0^1\lim_{v\to\infty}v\,\mathbb E_{\pi^{(v)}_{\ell,\zeta}}[N(N-1)]\,d\ell,\qquad
 \mathcal V_\zeta=\int_0^1\lim_{v\to\infty}v\,\operatorname{Var}_{\pi^{(v)}_{\ell,\zeta}}(N)\,d\ell.
\]
In the motivating fully-connected model, \(v\) corresponds to the number of microscopic sites at one fitness; its divergence at any fixed interior fitness is the large-volume regime. The multiplicity limit is taken **before** the high-fitness/critical cutoff limit \(\zeta\downarrow0\). These are integrated *within-site* observables of the stationary mean-field marginal model, not cross-site correlations or a theorem about the variance of the entire finite network.

## Proof

**Stationarity and the first two moment equations.** Because \(\eta>\ell\), the linear birth-death chain is subcritical, and its zero-clearing extension has a unique stationary distribution with finite polynomial moments. Put \(a=b_\zeta(\ell)/v\), \(d=\eta-\ell=d_\zeta(\ell)>0\), and \(R=r(\ell)\). Applying the generator to \(n\) and \(n(n-1)\) gives the exact identities
\[
 0=a-(d+R)m_1,\qquad
 0=2(\ell+a)m_1-(2d+R)m_2,
\]
where \(m_1=\mathbb E N\) and \(m_2=\mathbb E[N(N-1)]\). Thus
\[
 m_1=\frac{a}{d+R},\qquad
 m_2=\frac{2(\ell+a)a}{(d+R)(2d+R)}.
\]
Consequently, for each \(\ell\) and \(\zeta>0\),
\[
 \lim_{v\to\infty}vm_2=\frac{2\ell b_\zeta(\ell)}{(d+R)(2d+R)},\qquad
 \lim_{v\to\infty}v\operatorname{Var}(N)=\frac{b_\zeta(\ell)}{d+R}+\frac{2\ell b_\zeta(\ell)}{(d+R)(2d+R)}.
\]
Integrating the first identity yields the formula for \(\mathcal P_\zeta\). Integrating the first term of the variance formula yields exactly \(\rho_\zeta\), by the displayed self-consistency equation, giving \(\mathcal V_\zeta=\rho_\zeta+\mathcal P_\zeta\). All integrals are finite for fixed positive \(\zeta\).

**Finite density below the condensation threshold.** Write \(x=1-\ell\). The assumptions imply \(x+r(1-x)\asymp x^\nu\) near zero. Because \(\nu<1\), both \(\int_0^1\ell/[x+r(1-x)]\,d\ell\) and \(\int_0^1q(\ell)/[x+r(\ell)]\,d\ell\) are finite. The strict constraint on \(\beta\) keeps the self-consistency denominator positive. Dominated convergence yields \(\rho_\zeta\to\rho_0<\infty\). In particular, \(b_\zeta(1-x)\to1\) uniformly as \((x,\zeta)\to(0,0)\), since \(q(1-x)\to0\) and \(\rho_\zeta\) is bounded.

**Threshold and constants.** The possible singularity of \(\mathcal P_\zeta\) is confined to \(x=0\). There, its integrand is asymptotically equivalent (in the joint critical scaling) to
\[
 \frac{2}{[\zeta+Cx^\nu][2\zeta+Cx^\nu]}.
\]
For \(\nu<1/2\), the zero-cutoff integrand is bounded by a constant times \(x^{-2\nu}\), which is integrable; dominated convergence gives \(\mathcal P_0<\infty\). For \(\nu=1/2\), the interval \(x\gg(\zeta/C)^2\) contributes \((2/C^2)\int dx/x\), with lower scale \((\zeta/C)^2\); the result is \((4/C^2)\log(1/\zeta)\). This logarithmic equivalence remains valid for general \(r(1-x)\sim C\sqrt{x}\) by two-sided comparison with \((C\pm\varepsilon)\sqrt{x}\), followed by \(\varepsilon\downarrow0\).

For \(1/2<\nu<1\), substitute \(x=(\zeta/C)^{1/\nu}y\). Since \(x/\zeta=O(\zeta^{1/\nu-1})\to0\) for fixed \(y\), and since the scaled integrand is dominated in its tail by a multiple of \(y^{-2\nu}\), dominated convergence after splitting at a fixed small \(x\) gives
\[
 \mathcal P_\zeta\sim2C^{-1/\nu}\zeta^{1/\nu-2}
 \int_0^\infty\frac{dy}{(1+y^\nu)(2+y^\nu)}.
\]
Finally, substitution \(t=y^\nu\), partial fractions, and the Euler beta integral (or its convergent difference for \(1<1/\nu<2\)) give the displayed expression for \(J_\nu\). The bounded \(\rho_\zeta\) cannot change any of the divergent asymptotic equivalents.

## Verification

The included \`CHECK.py\` checks the stationary factorial-moment equations exactly at rational parameters, verifies their independently integrated stationary truncated-chain values numerically, and numerically reproduces the logarithmic coefficient and the power-law amplitude for the explicitly admissible test family \(q(\ell)=2(1-\ell)\), \(r(\ell)=(1-\ell)^\nu\), \(\beta=1/4\). These finite computations support but do not replace the asymptotic proof. The proof requires no external computational certificate.

## Relationship to prior work

Grange (arXiv:2311.12414, first posted 2023-11-21) derives the site generating-function equation and stationary *first-moment* density for fitness-dependent local resetting, and classifies the onset of macroscopic condensation at \(\nu=1\). The paper does not state the integrated within-site factorial-second-moment threshold or its constants. Kapodistria, Phung-Duc and Resing (2015 preprint; journal 2016) obtain general factorial moments for linear birth/immigration-death processes with binomial catastrophes; their total-catastrophe limit provides the local moment calculation here, but does not contain the fitness-integrated self-consistent near-critical classification. Thus **the pointwise second-moment formula alone is not asserted to be novel**. Related classical zero-range condensation fluctuation theory concerns different rate/disorder mechanisms; no identical \(\nu=1/2\) local pair-crowding law was identified in the inspected works. This is a best-knowledge comparison, not a proof of publication priority.

## Limitations

The theorem concerns self-consistent stationary mean-field *single-site* distributions in the dilute-site multiplicity limit, with the order \(v\to\infty\) followed by \(\zeta\downarrow0\). It does not establish a joint finite-network limit, full-population variance, inter-site covariance, distributional convergence, or universality outside \(q(1-x)=O(x^\alpha)\) and \(r(1-x)\sim Cx^\nu\), \(0<\nu<1\). At finite \(v\), additional terms enter the factorial moment; no uniform finite-size error bound is claimed. The exact critical constants are asymptotic, not finite-cutoff equalities. Publication originality remains subject to independent literature review.

## References

1. P. Grange, *Local resetting in non-conserving zero-range processes with extensive rates*, arXiv:2311.12414v1 (2023-11-21), https://arxiv.org/abs/2311.12414 . See the stationary site generating-function equation (31), density formulas (41)–(44), and Section 5.2.
2. S. Kapodistria, T. Phung-Duc and J. Resing, *Linear birth/immigration-death process with binomial catastrophes*, Eurandom Preprint 2015-006 (2015); *Probability in the Engineering and Informational Sciences* 30 (2016), 79–111, https://doi.org/10.1017/S0269964815000297 . See Section 5.3, total-catastrophe factorial moments (5.2).
3. S. Grosskinsky, P. Chleboun and G. M. Schütz, *Instability of condensation in the zero-range process with random interaction*, *Physical Review E* 78 (2008), 030101(R), https://doi.org/10.1103/PhysRevE.78.030101 . Context for distinct disorder-induced condensation effects.
