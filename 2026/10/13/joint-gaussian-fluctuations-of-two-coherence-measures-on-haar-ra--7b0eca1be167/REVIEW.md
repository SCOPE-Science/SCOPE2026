# Scientific review

## Correctness — PASS
The result uses exact Dirichlet moments and their logarithmic derivatives, then applies the multivariate i.i.d. central limit theorem and the delta method to normalized exponential samples. The crucial mixed covariance is \(\pi(d-1)(3\log2-2)/(2(d+1))\), and the asymptotic covariance matrix has positive determinant because the two influence functions are not proportional on the exponential support. Means, second moments, the cross-covariance, boundary \(d=2\), centering and all normalizations have been reconstructed from explicit formulas. Finite simulations support but do not establish weak convergence. Supporting source: the Dirichlet mixed-moment identity in Puchała–Pawela–Życzkowski, arXiv:1507.05123, Eq. (61). No nonstandard unverified lemma is used.

## Originality — PASS (qualified)
The published Dirichlet formula and exact \(\ell_1\)-coherence mean are credited. Singh–Zhang–Pati (arXiv:1509.08939) establish typicality for relative entropy but do not state the joint Gaussian law or its cross-fluctuation. Cheng–Hall (arXiv:1508.03240) study distinct basis-averaged quantities. The comparison covers equivalent Shannon and order-one-half Rényi formulations, higher-level general Dirichlet identities and a search for exact published covariance tables. A general Dirichlet functional central limit theorem could subsume the bivariate law, and this is a remaining priority risk. The assessment is based on inspected accessible literature and searches, not proof of global uniqueness.

## Value — PASS
Two canonical, operationally motivated coherence measures have very different scales of finite-dimensional fluctuation. Their full bivariate Gaussian covariance is a natural calibration law: strong correlation does not imply that the second observable is asymptotically determined by the first. The strictly positive conditional-variance constant identifies independent residual information and can inform statistical uncertainty quantification in Haar-typical coherence measurements. This goes beyond means and single-measure concentration, without presuming a new general limit theorem or a major downstream application.

## Residual limits
Complex Haar pure states and natural logarithms only. No uniform rate, rare-event bounds or mixed-state statement. Generic Dirichlet functional-CLT literature could contain an equivalent corollary; independence or priority has not been certified.

Self-review: passed. Independent audit: not yet performed.
