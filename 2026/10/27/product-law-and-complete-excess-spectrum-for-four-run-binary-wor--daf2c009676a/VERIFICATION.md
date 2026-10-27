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

# Verification record

The claim concerns every four-run binary word of positive run lengths, and not only the finite checked cases. The proof in `RESULT.md` classifies closed factors by run count and then derives the complete excess spectrum for all lengths at least four. No open lemma or computational enumeration is needed to infer the infinite-parameter theorem.

Run the standalone script `python3 verify.py` using the Python 3 standard library. It explicitly constructs every distinct contiguous factor and checks every proper nonempty border's occurrence positions, independently of the proposed closed-factor family. For all \(1\leq a,b,c,d\leq6\), the observed **set** of closed factors equals the proposed union exactly, and for every \(4\leq n\leq18\) the entire set of attainable four-run excess values and its maximum agree with the formulas. The actual output was:

```
CHECK_OK families=1296 run_lengths=1..6 max_length=24 exact_sets=matched
CHECK_OK exact_excess_spectra=lengths_4_through_18 maxima=matched
```

Finite enumeration does not prove the formula for larger parameters. The proof gives that extension. The originality comparison was limited to the documented full-text sources and scientific searches; it does not rule out unindexed prior results. Independent audit has not been performed.
