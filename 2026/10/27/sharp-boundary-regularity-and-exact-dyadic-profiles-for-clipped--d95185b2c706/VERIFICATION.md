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

The analytic verification reconstructs the escape event from the exact logarithmic-radius recurrence; proves atomlessness from uniform upper bounds on cylinder probabilities; checks both binary prefix factorizations with null boundary events; solves the clipped run recurrences and proves finite saturation; derives the identical endpoint profile by the digit-complement involution; and proves two-sided bounds with constants uniform over every allowed initial state.

The example \(\alpha=1/2\), \(\varepsilon=1/4\) is checked exactly: after the first zero digit, the state is \(3/8\), so \(\Pr(R\ge1/4)=3/4+(1/4)(3/8)=27/32\). Since \(\log_2(4/3)<1/2\) and \(\sqrt3/2>27/32\), the normalized limiting profiles at phase \(1\) and phase \(3/4\) differ. This is a rigorous witness of oscillation.

`python3 check.py` was executed and returned `CHECKS_PASS: 36 dyadic endpoint tests and 34 saturated u=3/4 tests; H(3/4)=27/32`. It uses Python standard-library rational arithmetic and enumerates finite binary words, checking the claimed identities on \(\alpha=1/2\), \(\varepsilon=1/4\), and initial states \(1/4,1/2,3/4\) for run lengths \(1\) through \(6\). Those checks do not by themselves establish the infinite-parameter theorem.

Primary-source comparison inspected Endo's complete arXiv paper with particular attention to Section 4 Example 4.2, where qualitative continuity, not the present exact boundary profile, is shown. Further inspected related de Rham function literature. Priority remains subject to broader independent literature examination; there is no independent audit evidence.
