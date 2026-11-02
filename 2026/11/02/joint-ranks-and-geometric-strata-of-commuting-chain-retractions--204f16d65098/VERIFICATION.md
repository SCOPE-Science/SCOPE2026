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

The direct checker `verify_chain_retractions.py` was executed against the final candidate source using the Python standard library. All eleven complete histograms of simultaneous chain, homology and boundary ranks agreed with independently calculated automorphism-group and multiplicity sums. Twelve additional closed-form tests passed. See `checker_output.txt` for the actual execution result.

Finite examples are not a proof for all complex lengths, all field sizes or all tuple lengths; the general argument is the direct-sum decomposition, endomorphism radical computation, conjugacy/stabilizer classification, and locally constant rank stratification in `RESULT.md`. The checker tests prime fields; extension fields and arbitrary characteristics are addressed by the field-independent algebraic proof, not by exhaustive computation.

No independent mathematical audit has been performed. Historical publication priority is subject to the originality limitations described in `REVIEW.md`.
