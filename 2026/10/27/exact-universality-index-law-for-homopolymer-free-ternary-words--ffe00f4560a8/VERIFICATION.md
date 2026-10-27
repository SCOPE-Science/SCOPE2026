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

The proof gives a general greedy-arch equivalence, a stochastic independent-geometric renewal representation, and formal bivariate generating functions. The standalone verifier `verify.py` uses two numerically independent finite methods: (i) a last-letter/seen-symbol mask dynamic program for all lengths through \(80\); (ii) exhaustive enumeration of all adjacent-distinct ternary words through length \(11\), checking every candidate scattered subsequence directly. It validates the exact coefficient formula and prints `TERNARY_NO_REPEAT_UNIVERSALITY_PASS dynamic_n=1..80 direct_spectra_n=1..11`. Only the mathematical derivations, not finite experiments, establish all-length identities and limiting laws.

Independent audit has not been performed.
