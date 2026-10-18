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

# Verification of the Gaussian hiccup-complement theorem

Run `python3 certify.py` in the same directory. Standard-library Python 3 is sufficient. Expected exact output:

```
PASS: 32 exact complete-tree and prefix-discrepancy checks
PASS: 27 direct sequence/complement comparisons
NOTE: weak convergence is justified by the analytic block-coupling proof
```

For every checked tree, the code constructs the entire word and checks every prefix rather than sampling prefixes. For nine parameter pairs, it constructs the self-referential increasing sequence separately from the word recursion, and it compares the first \(100\), \(2048\), and \(10000\) binary symbols. No randomness is used in these tests.

The asymptotic proof does not rely on finite enumeration: it establishes a coupling of uniformly chosen complete-tree positions to sums of independent uniform child indices with failure probability \(O_k(k^{-r})\), with \(r=\lfloor h^{1/3}\rfloor\), and handles a uniform index in a truncated concatenated word by discarding a vanishing fraction of positions. The external fact needed to identify the word with the original hiccup sequence is Cloitre's published Proposition 4.3 (arXiv:2610.13908v1). The validity of the limit for all \(N\) and fixed parameters depends on those mathematical arguments, not on the finite script.

Only a self-review has been carried out; an independent audit remains unperformed.
