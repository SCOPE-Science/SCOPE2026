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

`verify.py` is standalone Python 3 code using only the standard library. Run `python verify.py` from the extracted directory. It reconstructs the EGF using exact `fractions.Fraction` arithmetic and directly checks inclusion-minimal total domination using every open adjacency neighborhood of each vertex of \(L(K_n)\). Across \(3\le n\le7\), this covers precisely \(2{,}131{,}016\) subsets of \(E(K_n)\) and compares the complete degree-by-degree polynomial rather than only minimum sizes.

Expected output:
```
n= 3 actual= {2: 3} predicted= {2: 3}
n= 4 actual= {2: 12} predicted= {2: 12}
n= 5 actual= {3: 80} predicted= {3: 80}
n= 6 actual= {4: 840} predicted= {4: 840}
n= 7 actual= {4: 630, 5: 3402} predicted= {4: 630, 5: 3402}
VERIFY_OK n=3..7 all_subset_checks=2131016 minimal_set_coefficients_agree
```

Checks use exhaustive subsets for those orders, but no finite range proves the general theorem. The unrestricted proof is in RESULT.md; previous literature comparisons are separately qualified in REVIEW.md and AUDIT.json. The completed finite computation does not constitute an independent mathematical audit.
