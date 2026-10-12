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

# Verification and reproducibility

Run `python3 verify.py` using Python 3.10 or later. No non-standard dependencies are needed.

The replayed output of the bundled program is:

```text
VERIFY_OK language_cases 42 cross_model_bisimulations 27 bisimulation_worlds 4176 direct_term_closures 8 orientation_example (256, 64)
```

The program conducts three genuinely different finite checks. First it exhausts assignments to selected cluster vectors and compares the resulting rooted reduced words with an independently enumerated subsequence-capacity language. Second it builds the disjoint union of every model valuation for small cases, performs ordinary finite modal-bisimulation refinement, and tests its equivalence classes against the proposed normal forms. Third it enumerates the entire Boolean/modal closure of the projection functions on the full r-input operation truth tables for eight small frames, comparing each closure size with the predicted power of two. It separately tests the explicit three-world orientation difference.

These calculations cannot prove the theorem for arbitrary lengths and capacities. The general result follows from the bounded-morphism deletion lemma, the explicit suffix-isolating formulas, the uniqueness of finite reachable bisimulation-minimal quotients, and the constructive realizability of exactly the listed palette words. The code is a finite consistency check and an independently repeatable calculation, not an independent mathematical audit.
