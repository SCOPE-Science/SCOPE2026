# Hidden multi-particle tail hierarchy identifies random batch-reset laws for stable flights

## Finding
Consider \(N\ge2\) independent symmetric strictly \(\alpha\)-stable Lévy flights in one dimension, with \(0<\alpha<2\) and characteristic functions
\[
\mathbb E e^{i\xi L_i(t)}=\exp(-Dt|\xi|^\alpha),\qquad D>0.
\]
At the event times of an independent Poisson process of rate \(r>0\), draw a fresh size \(M\in\{1,\ldots,N\}\) with probabilities \(p_m\), uniformly choose one subset of that size, and reset exactly its coordinates to zero. Unselected coordinates continue their flights. Denote the unique stationary position law by \(\pi\). Let \(\binom ab=0\) for integers \(b>a\), and define the rate at which at least one of any specified \(j\) particles is reset:
\[
\lambda_j=r\left[1-\sum_{m=1}^N p_m\frac{\binom{N-j}{m}}{\binom Nm}\right],\qquad 1\le j\le N.
\]
All these rates are positive, and \(\lambda_N=r\). Let
\[
 c_\alpha=\frac{2\Gamma(\alpha)\sin(\pi\alpha/2)}{\pi}.
\]
For every \(1\le j\le N\) and every fixed \(t_1,\ldots,t_j>0\), the stationary simultaneous large-displacement probability satisfies the exact asymptotic
\[
\boxed{\lim_{x\to\infty}x^{j\alpha}
\pi\bigl(|X_1|>t_1x,\ldots,|X_j|>t_jx\bigr)
=(c_\alpha D)^j\frac{j!}{\prod_{\ell=1}^j\lambda_\ell}
\prod_{i=1}^j t_i^{-\alpha}.}
\]
In particular, the finite rare-event amplification factors
\[
H_0=H_1=1,\qquad
H_j=\lim_{x\to\infty}\frac{\pi(|X_1|>x,\ldots,|X_j|>x)}{\pi(|X_1|>x)^j}
=\frac{j!\lambda_1^j}{\prod_{\ell=1}^j\lambda_\ell}
\]
obey the sharp bounds \(1\le H_j\le j!\). For every \(j\ge2\), the lower equality holds precisely when batches have size one almost surely, and the upper equality holds precisely when they have size \(N\) almost surely.

More strongly, **the entire probability mass function of the random batch size is uniquely determined by the dimensionless rare-event factors \(H_2,\ldots,H_N\)**, without knowing \(r\), \(D\), or \(\alpha\). Indeed, put
\[
q_0=0,\qquad q_j=\frac{jH_{j-1}H_N}{NH_jH_{N-1}}
\quad(1\le j\le N),\qquad b_j=1-q_j.
\]
Then \(q_j=\lambda_j/r\) (hence \(q_N=1\)) and
\[
\boxed{p_m=\binom Nm\sum_{s=0}^{m}(-1)^{m-s}\binom ms b_{N-s},\qquad 1\le m\le N.}
\]
For fixed-size batches \(M=m\), the pair factor specializes to
\[
H_2=\frac{2}{2-(m-1)/(N-1)},
\qquad m=1+2(N-1)(1-H_2^{-1}).
\]
Thus even pairwise rare-event amplification recovers an unknown fixed batch size. Every fixed \(j\ge2\) has asymptotically vanishing conditional simultaneous-exceedance probability, despite \(H_j>1\) under nontrivial simultaneous resetting.

## Assumptions and scope
The system has a *fixed finite* number \(N\) of labeled particles, a state-independent homogeneous Poisson reset clock, independent fresh nonempty batch sizes and uniform conditional subset selection. The Lévy drivers are mutually independent, independent of the reset mechanism, and restarted only in the sense that the selected positions become zero; no other coordinate or noise source is reset. Rates, stable index, and batch law are fixed before the displacement threshold \(x\to\infty\). All probability statements refer to the stationary law, not a finite-time transient. The batch-size inversion assumes \(p_0=0\); allowing invisible empty events would destroy identification of their occurrence fraction from the stationary position law.

## Proof
**1. Stationary construction and uniqueness.** Mark a two-sided rate-\(r\) Poisson process by independent batches. Every given coordinate is selected with probability \(\mathbb E M/N>0\), so its resets form a thinned Poisson process of rate \(\lambda_1>0\). Let \(A_i\) be its age since the most recent reset before time zero. The vector \(A\) has finite joint moments because \(\Pr(\max_i A_i>t)\le N e^{-\lambda_1 t}\). Conditional on all reset marks, each stationary coordinate is its independent Lévy-driver increment over the last \(A_i\) units of time, and the joint conditional law is a product. This defines an invariant law. Any two processes coupled with the same marks and Lévy increments agree on every coordinate after its first subsequent reset; the finite union of coordinate reset times is almost surely finite. Thus the invariant law is unique.

**2. Exact age-product hierarchy.** For a fixed \(j\)-element set \(J\), let \(F_J(A)=\prod_{i\in J}A_i\). Between resets, every age grows at unit speed; a reset intersects \(J\) at rate \(\lambda_j\) and then makes \(F_J=0\). Therefore the stationary age-process generator gives
\[
0=\mathbb E\mathcal LF_J
=\sum_{i\in J}\mathbb E\prod_{h\in J\setminus\{i\}}A_h
-\lambda_j\mathbb E\prod_{i\in J}A_i.
\]
The generator identity is justified by truncation and the exponential tail bound above. Exchangeability implies that every term in the sum equals the same \((j-1)\)-fold product moment \(M_{j-1}\). With \(M_0=1\), it follows that \(M_j=jM_{j-1}/\lambda_j\), giving
\[
\mathbb E\prod_{i=1}^j A_i=M_j=\frac{j!}{\lambda_1\cdots\lambda_j}.
\]
An independent check follows by integrating the joint survival function. For ordered backward durations \(0<t_{(1)}<\cdots<t_{(j)}\), the probability of avoiding all relevant marked resets is
\[
\exp\left[-\lambda_j t_{(1)}
-\sum_{\ell=2}^j\lambda_{j-\ell+1}(t_{(\ell)}-t_{(\ell-1)})\right].
\]
Integrating across the \(j!\) orderings and using successive positive gaps reproduces \(j!/\prod_{\ell=1}^j\lambda_\ell\).

**3. Rare joint excursions.** The standard symmetric stable tail law with the stated Fourier normalization is
\[
\Pr(|L_i(a)|>tx)\sim c_\alpha Da\,(tx)^{-\alpha}
\quad(x\to\infty),\qquad a,t>0.
\]
By stable scaling and boundedness of \(y^\alpha\Pr(|L_i(1)|>y)\), the left side multiplied by \(x^\alpha\) is bounded by \(C_{\alpha,D,t}a\) uniformly for \(a\ge0\) and \(x>0\). Conditional independence given \(A\), the age-product formula, and dominated convergence now yield the first boxed limit. Dividing by the \(j\)-th power of the \(j=1\) marginal asymptotic yields \(H_j\). Since the simultaneous probability is of order \(x^{-j\alpha}\) while one marginal has order \(x^{-\alpha}\), the ordinary tail-dependence coefficient vanishes for \(j\ge2\).

**4. Sharp envelope.** The hit event for any fixed one of \(j\) coordinates is contained in the hit event for their union, so \(\lambda_1\le\lambda_j\). The union bound gives \(\lambda_j\le j\lambda_1\). Substitution in the product formula gives \(1\le H_j\le j!\). When \(j\ge2\), equality at the lower bound forces \(\lambda_2=2\lambda_1\), equivalently \(\mathbb E[M(M-1)]=0\), hence \(M=1\) almost surely. Equality at the upper bound forces \(\lambda_2=\lambda_1\), equivalently the event of resetting one specified coordinate without a second has probability zero, hence \(M=N\) almost surely. Both endpoints are attained.

**5. Exact identification.** The adjacent-factor identity \(H_j/H_{j-1}=j\lambda_1/\lambda_j\), together with \(\lambda_N=r\), proves \(q_j=\lambda_j/r\). The probability that a fresh batch misses a fixed set of size \(N-s\) is
\[
b_{N-s}=\sum_{m=1}^s p_m\frac{\binom{s}{m}}{\binom Nm},\qquad 0\le s\le N.
\]
This is a triangular binomial transform of \(p_m/\binom Nm\); binomial inversion gives the second boxed formula. All operations have positive denominators because \(M\ge1\) almost surely. For deterministic \(M=m\), the common-hit rate of a given pair is \(r m(m-1)/[N(N-1)]\); hence \(\lambda_2=2\lambda_1-rm(m-1)/[N(N-1)]\), yielding the displayed \(H_2\) and its inverse.

## Verification
The accompanying Python 3 script `verify.py` uses only the standard library. It enumerates reset-subset hit probabilities exactly using rational arithmetic, computes the moment hierarchy and rare-event factors, recovers complete deterministic and random batch laws by binomial inversion, and checks their sharp endpoints. It also compares two independent analytic expressions for the stationary joint-age moments and performs a Cauchy-flight tail sanity check. Run `python3 verify.py` in the package directory. These finite computations test formulas and implementation; the infinite-displacement limit, stationary uniqueness, and law identifiability are proved above, not inferred from enumeration.

## Relationship to prior work
De Mauro, Majumdar, and Schehr (arXiv:2601.20077, first posted 2026-01-27) introduced fixed-size uniform batch resetting for *Brownian* gases, proved an exact recursive closure for Fourier marginals, and analyzed two-particle correlations. Their discussion identifies *random batch sizes* as an interesting extension. Those results establish the reset-batch framework, not the present heavy-tailed stationary multi-exceedance hierarchy or recovery of an arbitrary batch-size law from normalized tail factors. De Mauro, Biroli, Majumdar, and Schehr (arXiv:2509.06658) analyze a *fully simultaneous* Brownian gas with non-Poissonian intervals; the common-age special case does not supply the mixed-batch inversion. Żbik and Dybiec (arXiv:2311.16014) study Lévy flight/walk *first-passage escape* with resetting, not multi-particle stationary joint extremes. The stable-tail asymptotic itself is classical and is used here as an input, not claimed as new. Generic Poisson common-shock inclusion-exclusion and binomial inversion are likewise known techniques; the claim is their combined exact realization and inverse identification for this nonequilibrium gas.

## Limitations
No claims are made for Brownian \(\alpha=2\) (which has Gaussian, not power-law, displacement tails), correlated Lévy drivers, infinite particle numbers in a joint threshold limit, history-dependent batch laws, nonuniform subset selection, reset durations, or state-dependent clocks. The observable joint exceedances can be extremely rare at high order; the theorem is asymptotic and gives no finite-sample inference accuracy. Allowing empty batches without knowing the physical event rate creates a thinning nonidentifiability. Published general multivariate shock or resetting results could contain broader implications not found in the inspected material; independent literature-wide priority and validation have not been completed.

## References
1. G. de Mauro, S. N. Majumdar, and G. Schehr, *Tuning the strength of emergent correlations in a Brownian gas via batch resetting*, arXiv:2601.20077 (first public version 2026-01-27), https://arxiv.org/abs/2601.20077.
2. G. de Mauro, M. Biroli, S. N. Majumdar, and G. Schehr, *Dynamically emergent correlations in Brownian particles subject to simultaneous non-Poissonian resetting protocols*, arXiv:2509.06658 (2025), https://arxiv.org/abs/2509.06658.
3. B. Żbik and B. Dybiec, *Lévy flights and Lévy walks under stochastic resetting*, Physical Review E 109, 044147 (2024), arXiv:2311.16014, https://arxiv.org/abs/2311.16014.
4. W. M. Bednorz, R. M. Łochowski, and R. Martynek, *On tails of symmetric and totally asymmetric stable distributions*, arXiv:1802.00612 (2018), https://arxiv.org/abs/1802.00612.
