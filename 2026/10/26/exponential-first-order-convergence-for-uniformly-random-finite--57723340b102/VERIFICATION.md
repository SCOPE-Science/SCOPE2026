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

Finite enumerative checks: run `python check.py` in the package directory. The checker performs exhaustive labelled total-preorder enumeration through seven points, an independent block-composition histogram computation, the Fubini recurrence, exact edge-block counting identities, and comparison of the finite first-singleton probabilities with \(\log 2\). The successful run ends with `TOTAL_PREORDER_BLOCK_WORD_CHECK_OK`.

The complete all-sentence theorem is supported by the argument in `RESULT.md`, not by the finite checker. Its nontrivial infinite-size components are the bounded-quantifier-rank reduction to finite coloured words; aperiodicity of the word-type monoid; semisimplicity of the stochastic recurrent projection; and isolation of the unique simple pole at \(\rho=\log 2\). The checker neither certifies finite-dimensional spectral perturbation nor proves that unsearched literature cannot subsume the claim.

No independent audit or independent validation has been performed.
