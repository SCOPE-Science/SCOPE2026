# A sharp two-thirds variability threshold for bias-efficient renewal transport

## Finding
Consider independently directed renewal rewards, with the direction bias freely controllable but the joint law of reward magnitudes and cycle durations fixed. A natural dimensionless cost-adjusted current precision has a unique optimum at **nonzero** direction bias if and only if the normalized cycle mismatch variance is strictly between zero and \(2/3\). At or above \(2/3\), progressively weaker bias gives higher efficiency; at zero mismatch, stronger bias gives arbitrarily high efficiency. The parameter distinguishing all three regimes is an exact ratio of two cycle-level second moments.

More precisely, let \((N_i,R_i)_{i\ge1}\) be independent identically distributed pairs with \(N_i\) a positive integer and \(R_i\) nonnegative; both are bounded and \(\mathbb E R_i>0\). The duration and reward *within* a cycle may be correlated. Independently of these pairs let \(X_i\in\{-1,+1\}\) be i.i.d., with \(\mathbb P(X_i=1)=(1+m)/2\), for control parameter \(0<m<1\). Put
\[
\mu_N=\mathbb E N,\quad \mu_R=\mathbb E R,\quad A=\mathbb E R^2,\quad
\rho=\mu_R/\mu_N,\quad B=\mathbb E[(R-\rho N)^2],\quad b=B/A.
\]
Let \(K(t)=\max\{k:\sum_{i\le k}N_i\le t\}\) and let the integrated completed-cycle current be \(J_m(t)=\sum_{i\le K(t)}X_iR_i\). Define \(j_m=\lim_{t\to\infty}\mathbb E[J_m(t)]/t\) and \(v_m=\lim_{t\to\infty}\operatorname{Var}(J_m(t))/t\). Define the **direction-selection reversal-information cost** per cycle by the *specific* Bernoulli divergence
\[
s(m)=D_{\rm KL}\!\left(\operatorname{Bern}\left(\frac{1+m}{2}\right)\middle\|\operatorname{Bern}\left(\frac{1-m}{2}\right)\right)=2m\operatorname{artanh}m,
\qquad \Sigma_m=s(m)/\mu_N.
\]
This cost is a well-defined informational cost. It is not asserted to equal the full physical entropy production of an unspecified microscopic apparatus. The dimensionless efficiency is
\[
\mathcal Q_b(m):=\frac{2j_m^2}{v_m\Sigma_m}
=\frac{\mu_R^2}{A}\frac{m}{[1-(1-b)m^2]\operatorname{artanh}m}.
\]
Its complete global classification is:

1. If \(b=0\), \(\mathcal Q_b\) is strictly increasing and diverges as \(m\uparrow1\).
2. If \(0<b<2/3\), \(\mathcal Q_b\) strictly increases on \((0,m_*)\) and strictly decreases on \((m_*,1)\), with exactly one global maximizer \(m_*\). It is characterized by
   \[
   \frac{1-t(m_*)}{m_*^2[1+t(m_*)]}=1-b,\qquad
   t(m)=\frac{(1-m^2)\operatorname{artanh}m}{m}.
   \]
   The maximum strictly exceeds the weak-bias value \(\mu_R^2/A\).
3. If \(b\ge2/3\), \(\mathcal Q_b\) is strictly decreasing throughout \((0,1)\), and its supremum \(\mu_R^2/A\) is approached only as \(m\downarrow0\).
4. For every \(b>0\), \(\mathcal Q_b(m)\to0\) as \(m\uparrow1\). These endpoint claims are limits, not achievable finite-cost states.

## Assumptions and scope
The cycle pair \((N,R)\) has an arbitrary bounded joint distribution with \(N\in\{1,2,\ldots\}\), \(R\ge0\) and \(\mathbb E R>0\); no independence between \(N\) and \(R\) is assumed. Across cycles all pairs are i.i.d. Each direction sign is independent of all cycle pairs and other signs. Only \(m\) is varied; the joint cycle law remains fixed. The current counts completed cycles only; the bounded unfinished-cycle contribution, if included, does not affect these long-time rates. In particular \(A>0\), \(B\ge0\), and \(\mu_N>0\). The case \(B=0\) means \(R=\rho N\) almost surely, not just vanishing raw reward variance.

## Proof
**1. Renewal current rates.** Let \(Y_i=X_iR_i-j_mN_i\) with \(j_m=m\mu_R/\mu_N=m\rho\). Then \(\mathbb EY_i=0\). Independence of \(X_i\) and \((N_i,R_i)\) gives the exact orthogonal decomposition
\[
Y_i=(X_i-m)R_i+m(R_i-\rho N_i),\qquad
\mathbb EY_i^2=(1-m^2)A+m^2B.
\]
For bounded i.i.d. renewal increments, the renewal-reward mean and variance rates are
\[
j_m=\frac{m\mu_R}{\mu_N},\qquad
v_m=\frac{(1-m^2)A+m^2B}{\mu_N}.
\]
For completeness, the variance rate can be obtained without presupposing the variance identity. Let \(H(t)=K(t)+1\) be the index of the first renewal crossing \(t\); this is a bounded stopping time for each fixed integer \(t\), and \(\mathbb EH(t)/t\to1/\mu_N\). The centered martingale \(M_h=\sum_{i\le h}Y_i\) satisfies by optional stopping \(\mathbb E M_{H(t)}=0\) and \(\mathbb E M_{H(t)}^2=\mathbb EY_1^2\,\mathbb EH(t)\). The difference between \(M_{H(t)}\) and the centered completed-cycle reward \(J_m(t)-j_mt\) consists of one omitted bounded \(Y\) and a bounded renewal undershoot; thus its second moment is bounded uniformly in \(t\), and its cross term with \(M_{H(t)}\) is \(O(\sqrt t)\). Their means differ by \(O(1)\), proving the claimed variance limit. It also proves the mean current limit. Substituting the explicitly defined Bernoulli KL cost yields the displayed efficiency formula.

**2. A monotone comparison function.** Write \(x=m^2\) and \(c=1-b\). Introduce
\[
t(m)=\frac{(1-m^2)\operatorname{artanh}m}{m}
=\int_0^1\frac{1-x}{1-xu^2}\,du,
\qquad
g(m)=\frac{1-t(m)}{x[1+t(m)]}.
\]
The integral representation follows by integrating \((1-xu^2)^{-1}\) from \(0\) to \(1\). Moreover
\[
\frac{1-t(m)}x=\int_0^1\frac{1-u^2}{1-xu^2}\,du=:I(x).
\]
For \(0<x<1\), the integrand of \(I\) is strictly increasing in \(x\) for \(0<u<1\), while the integrand of \(t\) is strictly decreasing in \(x\) for \(0\le u<1\). Hence \(I(x)\) is strictly increasing, \(t(x)\) strictly decreasing, and \(g=I/(1+t)\) is **strictly increasing**. Direct dominated convergence gives
\[
\lim_{m\downarrow0}g(m)=\frac{1}{3},\qquad
\lim_{m\uparrow1}g(m)=1.
\]
Indeed \(t\to1\) and \(I\to2/3\) at the first endpoint; at the second \(t\to0\) and \(I\to1\).

**3. Derivative sign and the classification.** Differentiating \(\mathcal Q_b\), and clearing factors that are strictly positive for \(0<m<1\), shows
\[
\operatorname{sgn}\mathcal Q_b'(m)
=\operatorname{sgn}\left((1+c m^2)t(m)-(1-cm^2)\right)
=\operatorname{sgn}\left(c-g(m)\right).
\]
The cancellation in the second equality uses \(1-t=x(1+t)g\). Because \(g\) increases bijectively from \(1/3\) to \(1\), if \(0<b<2/3\) then \(1/3<c<1\) and there is exactly one root. If \(b\ge2/3\), then \(c\le1/3\), so the derivative is strictly negative. If \(b=0\), then \(c=1>g(m)\), so the derivative is strictly positive. There are no other extrema.

**4. Endpoints and strict advantage.** As \(m\downarrow0\), \(\operatorname{artanh}m/m\to1\), so \(\mathcal Q_b\to\mu_R^2/A\). If \(b>0\), the factor \(1-(1-b)m^2\to b>0\), while \(\operatorname{artanh}m\to\infty\), giving \(\mathcal Q_b\to0\). If \(b=0\), \(\mathcal Q_0\sim(\mu_R^2/A)/[(1-m^2)\operatorname{artanh}m]\to\infty\). Strict increase from the weak-bias limit when \(0<b<2/3\) gives its strict advantage. Finally the local expansion is
\[
\frac{\mathcal Q_b(m)}{\mu_R^2/A}=1+(2/3-b)m^2+O(m^4).
\]
This proves the threshold and all stated boundaries.

## Verification
Run the self-contained Python standard-library script `verify.py` using `python3 verify.py`. It reconstructs the moment decomposition by direct finite-support enumeration, compares analytical derivative signs with finite differences, compares the unique-root formula with independent golden-section maximization, checks endpoint-side monotonicity in each regime, and performs a seeded bounded-cycle Monte Carlo sanity check. At preparation the script produced `PASS: 424 deterministic assertions; simulated ratio=1.0054558`. Its finite tests are reproducibility checks, not proofs of all-parameter uniqueness; the integral monotonicity argument above is the proof.

For the cycle law \(N=1\) and \(R\in\{1,3\}\) equally likely, \(A=5\), \(\mu_R=2\), \(B=1\), and \(b=1/5\). The optimal bias is \(m_*=0.963761792016\ldots\) and the efficiency gain over its weak-bias limit is \(1.87905138688\ldots\). For \(N=R=1\), \(b=0\). For \(N=1\) and \(R\in\{0,10\}\) with probabilities \(9/10\) and \(1/10\), \(b=9/10\), placing the optimum at the weak-bias boundary.

## Relationship to prior work
Karimi and Jafarpour (arXiv:2606.16339) establish the renewal-reward variance decomposition and the binary-direction entropy expression, with emphasis on universal uncertainty inequalities and weak-bias expansion. Shreshtha and Harris (arXiv:1903.01972) develop the renewal-reward approach to run-and-tumble uncertainty. Pietzonka and Coghi (arXiv:2305.15392) examine optimal cost–precision trade-offs for different counting observables and Markov-network mechanisms. Those foundational identities and broad trade-off questions are prior art. The finding assessed here is **not** a new renewal-variance formula or a general thermodynamic uncertainty inequality: it is the complete sharp global direction-control optimization at fixed cycle law, its strict monotonicity regimes, unique interior maximizer, and natural normalized-variability threshold. The comparison includes equivalent bias parametrizations and marginal reversal divergence; no inspected result states the same threshold classification. General optimization theory could imply aspects of the calculation, and an unlocated specialized treatment remains an originality risk.

## Limitations
The cost is the KL divergence of the chosen sign law against its sign-flipped law. It may coincide with a physical contribution to entropy production under a suitable microscopic local-detailed-balance implementation, but neither full physical entropy production nor a device-independent energetic optimization is established. Bias dependence of the duration/reward law, directional memory, correlated consecutive cycles, partially completed-cycle rewards with unbounded residuals, unbounded moments, and optimization of the apparatus jointly with bias are outside the theorem. No assertion is made that every prescribed cycle distribution is physically realizable by a particular motor. The numerical search result alone is not proof of novelty, and independent scientific audit has not been performed.

## References
1. F. Karimi and F. H. Jafarpour, *Thermodynamic Uncertainty Relation For a Multi-Phase Alternating Renewal Random Walk*, arXiv:2606.16339, first public version 15 June 2026, https://arxiv.org/abs/2606.16339 . Model, renewal variance and auxiliary sign entropy; Sections II–III and Appendix A of the accessible version.
2. M. Shreshtha and R. J. Harris, *Thermodynamic uncertainty for run-and-tumble type processes*, arXiv:1903.01972, https://arxiv.org/abs/1903.01972 . Related run-and-tumble renewal thermodynamics.
3. P. Pietzonka and F. Coghi, *Thermodynamic cost for precision of general counting observables*, arXiv:2305.15392, https://arxiv.org/abs/2305.15392 . Broader cost–precision bounds for counting observables.
