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

The proof is analytic and does not depend on finite enumeration. A standalone checker exhausts every subset for the parameter pairs listed in its output, computes skew closure using the rule that any vertex with exactly one white neighbor may force, and compares the result against the blade-occupancy criterion. It then compares the observed size distribution with coefficients obtained from
\[
(1+x)\left(x^m+m x^{m-1}+\binom{m}{2}x^{m-2}\right)^k-\binom{m}{2}^k x^{k(m-2)}.
\]
It separately checks \(Z_-(W_{k,m})=k(m-2)+1\) and the minimum-set multiplicity \(\binom{m}{2}^{k-1}(\binom{m}{2}+km)\).

Finite exhaustive checks support implementation correctness only; they are not evidence for the infinite quantifiers. The infinite claim rests on the white-neighbor count proof in RESULT.md. No independent audit has been performed.
