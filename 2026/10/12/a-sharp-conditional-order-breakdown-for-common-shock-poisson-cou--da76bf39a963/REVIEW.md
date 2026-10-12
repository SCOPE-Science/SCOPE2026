# Scientific review: common-shock Poisson conditional ordering

## Correctness — PASS

The theorem concerns independent \(Y_i\sim\operatorname{Pois}(a)\), \(Z\sim\operatorname{Pois}(b)\), \(a,b>0\), and \(X_i=Y_i+Z\) for every integer \(n\geq2\). The four claims were checked separately. For joint \(\mathrm{MTP}_2\), the Poisson mass sequence is log-concave, so each \((Z,X_i)\) conditional-mass factor is \(\mathrm{TP}_2\); products and marginalization give the full-vector result, using Fallat et al., Proposition 3.4(ii). For pairwise likelihood-ratio order, exact coefficient extraction of \(\mathbb E[u^{X_1}t^{X_1+X_2}]\) reduces every adjacent minor to two nonnegative log-concavity differences. Cauchy–Binet justifies closure of nonnegative interval-supported log-concave sequences under convolution. For \(S_n=n-1,n\), the possible latent values of \(Z\) are enumerated exhaustively and Poisson splitting yields the exact binomial mixture. This gives the sharp general-dimensional single-tail threshold and both exact trivariate likelihood-ratio and usual-stochastic-order thresholds. The support boundaries and equality cases are included.

The standalone exact-rational `VERIFY.py` passed 28 trivariate threshold cases, 90 general-dimensional transition cases, 676 adjacent bivariate \(\mathrm{TP}_2\) inequalities, and 104,328 finite-lattice \(\mathrm{MTP}_2\) comparisons. These finite checks do not prove all parameters/dimensions; universal quantifiers depend on the analytic arguments in RESULT.md. Independent external auditing remains outstanding.

## Originality — PASS, with residual priority risk

Pellerey and Navarro, *Stochastic monotonicity of dependent variables given their sum* (first public 11 October 2021, DOI 10.1007/s11749-021-00789-5), provide conditions and dependent examples for conditional-sum monotonicity. Their Section 3, Proposition 3.1 assumes a log-concave \(\mathrm{TP}_2\) distribution for \((X_i,\sum_{j\ne i}X_j)\), rather than mere full-vector \(\mathrm{MTP}_2\); neither their main results nor examples supply the proposed common-shock Poisson negative boundary or the thresholds. Schulz, Genest and Mesfioui, *A multivariate Poisson model based on comonotonic shocks* (DOI 10.1111/insr.12408), display the underlying classical common-shock model in Section 2.4, Eq. 6, but not the conditional-order phase boundaries. Ellis and Sijtsma (2023, DOI 10.1007/s11336-023-09905-w) treat manifest monotonicity given the rest score, explicitly excluding the observed coordinate, rather than the full sum here. Fallat et al., *Total positivity in Markov structures* (arXiv:1510.01290, Section 3), prove the needed positive-dependence closure, which the theorem **uses** as established mathematics. Searches of synonyms involving common shocks, conditional-on-total laws, \(\mathrm{MTP}_2\), Efron monotonicity, likelihood-ratio ordering, and trivariate Poisson laws identified no statement implying both the positive pair-sum property and the negative full-sum threshold.

Absence of a matching search result cannot establish priority. A possible earlier equivalent counterexample in a differently parameterized actuarial model remains a genuine residual risk; no claim of independent validation is made.

## Value — PASS

The motivating question is whether positive dependence and favorable pairwise conditional ordering are enough for Efron-style stochastic monotonicity after conditioning on the **entire** observed count. The theorem gives a substantive negative answer in the standard, infinitely supported, positively correlated common-shock Poisson model, and strengthens the hypothesis to \(\mathrm{MTP}_2\). It pinpoints the first problematic dimension, gives an exact general-dimensional tail transition, and distinguishes sharp likelihood-ratio and usual-stochastic thresholds in dimension three. These are structural ordering boundaries, not arbitrary finite values or known-table recomputations. The result does not assert an unrestricted multivariate classification.

## Remaining scientific limits

The statements treat equal idiosyncratic Poisson intensities and a common Poisson shock; they do not characterize general latent-shock count vectors. The cutoffs compare specified neighboring totals rather than every pair of conditioning levels. The computational certificate is bounded, and priority remains subject to independent literature assessment.

Self-review: passed. Independent audit: not yet performed.
