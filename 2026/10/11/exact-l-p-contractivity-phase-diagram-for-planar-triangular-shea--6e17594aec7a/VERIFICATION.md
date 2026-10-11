---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

For \(1<p<\infty\), phase alignment in the exact norming-functional formula gives
\[
\omega_p(M_{a,b,c})=\sup_{r\ge0}\frac{-a+br-cr^p}{1+r^p}.
\]
The sign boundary is the unique minimum of \(a/r+c r^{p-1}\), attained at \(r_0=(a/(c(p-1)))^{1/p}\), which yields the stated \(\beta_p(a,c)\). Differentiating its logarithm gives the unique maximum at \(p=1+a/c\), with value \(a+c\).

The focal endpoint checks reproduce the source:
\[
\omega_1(M_{1,9,10})=-1,\qquad\omega_2(M_{1,9,10})=\frac{9\sqrt2-11}{2}>0.
\]
A supplementary numerical root calculation places the unique crossover near \(p=1.46417\); that decimal is not used in the proof.

For the semigroup, pointwise domination and constant-function witnesses identify the multiplication-operator norm with the matrix operator norm. The logarithmic-norm inequality gives the upper bound, and the defining right derivative at zero rules out any larger prefactor-one decay exponent.

The literature comparison inspected the focal preprint at the relevant semigroup section, compared the theorem with classical logarithmic-norm frameworks, and searched published mathematical findings using source identifiers, formula aliases, dissipativity language, matrix-measure language, and implication-level formulations. The main remaining risk is an older equivalent calculation under different terminology.
