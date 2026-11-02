# Markov-correlated reset sites have a stationary-averaged Lévy escape law

## Finding
Fix \(0<\alpha<2\), \(c>0\), \(r>0\), and an integer \(m\ge2\). Let \(Y\) be a symmetric strictly \(\alpha\)-stable Lévy process whose characteristic function is \(\mathbb E e^{i\xi Y_t}=e^{-ct|\xi|^\alpha}\). In an interval \((-L,L)\), reset at independent rate-\(r\) exponential times. At a reset, select the new site \(L\lambda_j\) according to an irreducible row-stochastic matrix \(K=(K_{ij})_{i,j=1}^m\), where \(-1<\lambda_i<1\). The previous reset-site label is \(i\), and every excursion is a fresh independent copy of \(Y\). Start at any selected site \(L\lambda_i\). Let \(H_L\) be the first exit time and \(J_L\in\{-,+\}\) the exit side.

Write \(\pi K=\pi\), \(\sum_i\pi_i=1\), and define
\[
\eta_\alpha=\frac{c\,\Gamma(\alpha)\sin(\pi\alpha/2)}{\pi},\qquad
\kappa_i^+=\eta_\alpha(1-\lambda_i)^{-\alpha},\qquad
\kappa_i^-=\eta_\alpha(1+\lambda_i)^{-\alpha},
\]
\[
\bar\kappa_\pm=\sum_i\pi_i\kappa_i^\pm,\qquad
\bar\kappa=\bar\kappa_++\bar\kappa_->0.
\]
Then, as \(L\to\infty\), **for every initial reset site**,
\[
\left(L^{-\alpha}H_L,J_L\right)
\Longrightarrow (E,J),\qquad
E\sim\operatorname{Exp}(\bar\kappa),\qquad
\mathbb P(J=\pm)=\frac{\bar\kappa_\pm}{\bar\kappa},
\]
where \(E\) and \(J\) are independent. Moreover, for every integer \(k\ge1\),
\[
\lim_{L\to\infty}\frac{\mathbb E H_L^k}{L^{\alpha k}}=
\frac{k!}{\bar\kappa^k}.
\]
In particular, both the limiting completion-time law and the side bias depend on the reset-site chain only through its stationary weights \(\pi\); they are independent of the fixed positive reset rate \(r\) and of the remaining temporal correlations of the reset-site chain. The effective rate is the **stationary arithmetic average of exit hazards**, not an average of single-site mean passage times.

## Assumptions and scope
The stable process is one-dimensional, symmetric, strictly stable with generator symbol \(-c|\xi|^\alpha\), without a Gaussian component (\(\alpha<2\)); the interval is open and absorbing. There is one fixed finite set of sites \(\lambda_i\) strictly inside \((-1,1)\). The row-stochastic matrix \(K\) is irreducible (periodicity is allowed), and neither \(K\), the sites nor \(r\) varies with \(L\). Independent stable excursions and exponential resets restart the particle's state in full. No assertions are made for a vanishing reset rate, reset sites approaching the boundary, growing state counts, or the Brownian endpoint \(\alpha=2\).

## Proof
**1. One-excursion marked exit rates.** The Lévy measure of the specified stable process has density
\[
\nu(dz)=c\,\frac{\Gamma(1+\alpha)\sin(\pi\alpha/2)}{\pi}
|z|^{-1-\alpha}\,dz.
\]
At spatial fraction \(\lambda_i\), integration over jumps leaving the unit interval gives the rates \(\kappa_i^\pm\) above. The standard small-time exit theorem for Lévy processes in intervals, including the exit side, yields for the first unreset exit \(\tau_i\) of \((-1,1)\),
\[
\mathbb P(\tau_i\le t,J_i=\pm)=\kappa_i^\pm t+o(t)\quad(t\downarrow0).
\]
For fixed finitely many sites the remainders may be taken simultaneously. Exact self-similarity gives \(\tau_{L,i}\stackrel d=L^\alpha\tau_i\) with the same side. An integration-by-parts Abelian argument therefore yields, for every fixed \(u>0\),
\[
\mathbb E_i[e^{-u\tau_{L,i}}\mathbf1_{\{J_i=\pm\}}]
=\frac{\kappa_i^\pm}{uL^\alpha}+o(L^{-\alpha}).
\]
This uses actual first-exit probabilities, not just a terminal jump tail; exit-by-small-jump excursions are included in the cited small-time theorem.

**2. Exact correlated-reset renewal matrix.** For \(s\ge0\), define \(a_i^\pm(s)=\mathbb E_i[e^{-(r+s)\tau_{L,i}}\mathbf1_{\{J_i=\pm\}}]\), \(a_i=a_i^++a_i^-\), and \(b_i(s)=r(1-a_i(s))/(r+s)\). Conditioning on whether exit occurs before the next independent exponential reset gives the exact linear equation for the vector of marked Laplace transforms,
\[
F^\pm(s)=a^\pm(s)+\operatorname{diag}(b(s))K F^\pm(s).
\]
The term \(K\), rather than a rank-one resampling matrix, retains all correlations of successive destination labels.

**3. Singular resolvent limit.** Put \(\varepsilon=L^{-\alpha}\) and \(s=\theta\varepsilon\), \(\theta\ge0\). From step 1,
\[
a_i^\pm=\frac{\varepsilon\kappa_i^\pm}{r}+o(\varepsilon),\qquad
b_i=1-\frac{\varepsilon(\theta+\kappa_i^++\kappa_i^-)}r+o(\varepsilon).
\]
Every \(F_i^\pm\) is between zero and one. The renewal equation implies \((I-K)F^\pm=o(1)\); since \(K\) is finite irreducible, its right fixed space is spanned by the all-ones vector, even when \(K\) is periodic. Thus along any convergent subsequence \(F^\pm\to z_\pm\mathbf1\). Multiply the renewal equation by the stationary left eigenvector \(\pi\), insert the expansions and divide by \(\varepsilon\). The limiting scalar equation is
\[
(\theta+\bar\kappa)z_\pm=\bar\kappa_\pm.
\]
Its unique solution \(z_\pm=\bar\kappa_\pm/(\theta+\bar\kappa)\) proves convergence along the entire sequence, the independent exponential and side-mark law, and independence of the initial reset-site state.

**4. Moment convergence.** Choose \(0<\delta<\min_i(\kappa_i^++\kappa_i^-)/2\). At \(s=-\delta\varepsilon\) the same Abelian expansion holds, and for sufficiently large \(L\) all row sums of \(\operatorname{diag}(b(s))K\) are at most \(1-C\varepsilon\), while \(\max_i a_i(s)=O(\varepsilon)\). The positive Neumann series gives a uniform bound on \(\mathbb E_i e^{\delta H_L/L^\alpha}\). This furnishes uniform integrability of all polynomial moments. The limiting exponential moments then give \(k!/\bar\kappa^k\) for every fixed integer \(k\ge1\).

## Verification
The exact renewal matrix and its singular Perron-mode expansion were checked independently against the killed finite-state generator in `verification/markov_reset_check.py`, using a nonreversible three-state reset chain, four spatial scales, three Laplace parameters, first and second moments, and a different reset kernel with the same stationary law. The standalone check passes 30 assertions. Its killed finite-state model is an asymptotic big-jump analogue, **not** a simulation or proof of the infinite-activity stable process. The infinite-dimensional step relies on the cited Lévy small-time exit theorem and is proved analytically above.

## Relationship to prior work
Żbik and Palmowski (2026), arXiv:2610.20410, establish the large-interval **mean** for a single fixed reset location by combining the first-exit short-time law with a scalar reset formula. The present result addresses a different process: successively visited reset destinations follow an arbitrary finite irreducible Markov chain, and it proves the full marked limit with all moments. Figueroa-López and Tankov (2014) supply the underlying short-time Lévy exit theorem, not the correlated-reset limit. González, Riascos and Boyer (2021), arXiv:2104.00727, derive spectral formulas for **multiple reset destinations** on discrete networks, including Lévy-type network walks; their destination choice is memoryless rather than a retained finite-state reset label, and their framework does not explicitly give the present expanding continuous interval, stationary-averaged marked asymptotic. Żbik and Dybiec (2024), arXiv:2311.16014, examine resetting of Lévy flights and walks in bounded intervals without this correlated multisite scaling.

The comparison is at the level of hypotheses and implications; published general Markov-renewal rare-event theorems could provide an alternative proof and remain a priority risk. The contribution claimed is the explicit correlated multisite stable-exit law and its side-mark/moment consequence, not a new general Markov-renewal identity or a new Lévy small-time exit theorem.

## Limitations
No uniformity is claimed when \(r\), \(m\), \(K\), or \(\lambda_i\) varies with \(L\). The theorem does not apply to Brownian motion \(\alpha=2\); its one-large-jump coefficient disappears. It is a leading-order large-domain result and does not resolve the rate of convergence or finite-\(L\) optimal reset policies. Independent proof and priority reviews have not been performed.

## References
1. B. Żbik and Z. Palmowski, *Asymptotic behaviour for escaping an interval by Lévy flights under stochastic resetting*, arXiv:2610.20410 (first publicly submitted 2026-10-14), https://arxiv.org/abs/2610.20410.
2. J. E. Figueroa-López and P. Tankov, *Small-time asymptotics of stopped Lévy bridges and simulation schemes with controlled bias*, Bernoulli 20 (2014), 1126–1164, arXiv:1203.2355, https://arxiv.org/abs/1203.2355.
3. F. H. González, A. P. Riascos and D. Boyer, *Diffusive transport on networks with stochastic resetting to multiple nodes*, Physical Review E 103, 062126 (2021), arXiv:2104.00727, https://arxiv.org/abs/2104.00727.
4. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, Physical Review E 109, 044147 (2024), arXiv:2311.16014, https://arxiv.org/abs/2311.16014.
