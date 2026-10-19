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

Execute `python verify.py` using Python 3.10 or later and only the standard library. It reconstructs labelled path embeddings independently, compares full vertex-state exact terminal distributions with the two-class Markov recursion on eleven small substrates, checks 564 rational drift identities, 6300 even-path remainder identities, and six critical-exponent normalizations. The expected output consists of four PASS lines.

The separate Monte Carlo values given in RESULT.md are reproducibility-oriented sanity checks, not exhaustive certificates. Finite enumeration cannot establish the infinitely many graph sizes or the Gaussian weak limit; these are proved via the exact martingale, quadratic-variation, and boundary arguments. No independent audit has been performed.
