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
The claim is proved symbolically; no finite experiment is used as an infinite certificate.

The critical nonstandard input is Radomskii's translate lemma from arXiv:2609.38408v1. The proof uses it only after verifying its three relevant hypotheses: the shifts are distinct, their count is at most \(\eta x\), and their absolute values are at most \(e^{3x}=X\).

The remaining scale checks are:
\[
|\mathcal P_{\mathcal A}(X)|=O_{\mathcal A}(\log X),\qquad
D\gg_{\mathcal A}\frac X{\log X},
\]
\[
Qe^x=X^{2/3+o(1)}=o(D),\qquad
\exp\!\left(\frac{x}{(\log x)^5}\right)=X^{o(1)}=o(D).
\]
These guarantee both that the constructed block stays inside one power-free gap and that every sieve divisor of a positive difference is proper.

The proof explicitly covers all exponents: powers larger than the block yield negative differences; powers at or below the block yield positive composite differences. Duplicate power values or duplicate shifts are removed before applying the translate lemma and do not affect coverage.
