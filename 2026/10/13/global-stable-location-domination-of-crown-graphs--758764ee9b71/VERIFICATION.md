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

The verifier constructs each crown graph and its complement from adjacency sets and tests the definition directly. For a candidate set it checks locating-domination, then removes every selected vertex in turn and checks locating-domination again, in both graphs.

For every \(3\le n\le8\), every subset is checked against the claimed omitted-index classification. The boundary \(\operatorname{Cr}_2=C_4\) is checked separately. For \(n=9\), every subset through the claimed minimum size is scanned and the full minimum count is compared.

Recorded output:

```text
VERIFY_OK
n=3: gamma_glsL=4, minimum_sets=3, all_sets=10
n=4: gamma_glsL=6, minimum_sets=28, all_sets=37
n=5: gamma_glsL=6, minimum_sets=30, all_sets=166
n=6: gamma_glsL=6, minimum_sets=20, all_sets=619
n=7: gamma_glsL=7, minimum_sets=70, all_sets=2038
n=8: gamma_glsL=8, minimum_sets=182, all_sets=6367
n=2: gamma_glsL=4, minimum_sets=1 (boundary check)
n=9: gamma_glsL=9, minimum_sets=420
subsets_checked = 242758
all_set_classification_equivalence_checks = 87360
all classifications and minimum counts matched
```

The finite computation is an exhaustive regression check over the stated finite ranges. It does not replace the symbolic proof for arbitrary \(n\).
