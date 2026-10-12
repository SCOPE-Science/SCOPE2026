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

The ordinary-moment part is checked directly from the Cauchy tail: for every positive integer order, the absolute-moment integrand is asymptotic to a nonzero constant times \(|x|^{r-2}\), so the integral diverges.

The proof defect is checked by exact algebra:
\[
\frac{1}{\pi\sigma f_X(x)}-1=\frac{(x-\mu)^2}{\sigma^2}.
\]
Consequently the nonnegative square root is \(|x-\mu|/\sigma\). A plus-only inverse therefore maps both points \(\mu-t\) and \(\mu+t\) to \(\mu+t\), so it cannot equal the original random variable on the whole support.

For the replacement identity, the Cauchy density is decomposed into its two simple poles and integrated against the principal complex power in the upper half-plane. The large semicircle vanishes for \(\operatorname{Re}z<1\), the indentation at zero vanishes for \(\operatorname{Re}z>-1\), and the only enclosed pole is \(\mu+i\sigma\). This gives \(\mathbb E[X^z]=(\mu+i\sigma)^z\). Local behavior at zero and at infinity proves that no larger vertical strip can be an absolute-expectation domain.

The source theorem and its proof equation were read in the full publisher PDF. The closest fractional-moment predecessor was also inspected in full-text form. No numerical experiment is needed for the proof, and no statement about principal-value or finite-part moments is inferred.
