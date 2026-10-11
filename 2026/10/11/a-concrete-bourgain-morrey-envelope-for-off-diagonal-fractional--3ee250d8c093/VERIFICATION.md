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

The Bourgain–Morrey norm used in the proof was checked against the focal primary source. For every Calderón–Lozanovskiĭ factorization \(|F|\le |G|^{1-s}|H|^s\), the following three identities are the complete algebraic input:
\[
\frac1{p_s}=\frac{1-s}{p_1}+\frac{s}{p_2},\qquad
\frac1{u_s}-\frac1{p_s}=(1-s)\left(\frac1{u_1}-\frac1{p_1}\right)+s\left(\frac1{u_2}-\frac1{p_2}\right),
\]
\[
\frac1{r_s}=\frac{1-s}{r_1}+\frac{s}{r_2}.
\]
Local Hölder produces the first factorization estimate, multiplication by the exact cube power produces no residual scale factor, and sequence Hölder produces the \(\ell^{r_s}\) bound. Taking the defining infimum proves the inclusion with constant one.

The source was also checked for the lower generalized Boyd index \(p_{\mathcal M^u_{p,r}}=p\) and for Theorem 1.9(i). Therefore its hypothesis reduces exactly to
\[
n\left(\frac{1-s}{p_1}+\frac{s}{p_2}-\frac1q\right)<sk.
\]
The source’s Bourgain–Morrey subsection states that a general explicit Calderón-product description is unknown and retains the abstract product in its application table. The present verification establishes only a one-sided concrete envelope; it does not verify or assert equality of the spaces.

No numerical sampling, finite enumeration, or external certification is used. The principal residual literature risk is an equivalent unindexed one-sided lemma in older interpolation work, particularly the 2023 Calderón-product paper whose full text was not available in the inspected material.
