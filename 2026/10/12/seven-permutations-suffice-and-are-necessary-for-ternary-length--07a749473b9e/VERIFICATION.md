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

# Reproducibility

Execute `python3 verify.py` using a standard Python 3 installation. There are no third-party packages, external downloads, external files, or random inputs. The checker enumerates all length-eight words over three letters, filters even multiplicities, and independently verifies that first-occurrence relabeling yields 274 classes.

For each word and permutation, the predicate tests all \(\binom84=70\) ways of choosing increasing positions for one subsequence; the other subsequence is the complement. It checks both orientations of permutation similarity. Exact neighborhoods of the seven explicit lower-bound words are recomputed over all 17 inverse-pair representatives and compared with the displayed certificate. Seven pairwise disjoint neighborhoods force the lower bound. The seven chosen permutations are checked against all 274 normalized classes and separately against all 1641 labeled even words, proving the upper bound.

Expected output:

```text
VERIFY_OK k=3 n=4 m=7 even_words=1641 canonical=274 inversion_classes=17 lower_witnesses=7
```

The checker verifies a finite complete claim, not infinite behavior. All claimed result parameters are the fixed alphabet size three and half-length four. The script's completion is supplemental to the transparent exhaustive proof; it does not constitute independent external validation.
