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

# Verification details

The proof is an exact counting argument on the signed simplex face lattice, with no numerical approximation in the theorem. `check_cross_sections.py` separately enumerates all eligible signed crossing edges, checks straddling signed faces for generic sections, and computes geometric convex hulls of representatives in small dimensions using NumPy and SciPy. The observed output from this source program is:

```
EXACT_SECTION_COMBINATORICS_OK 252 parameter cases
GEOMETRIC_SECTION_CHECK_OK 70 nontrivial polytope sections
```

These bounded computations support the formulas but do not establish the infinite-dimensional quantifiers. The central and supporting cases and excluded vertex counts are derived explicitly in the proof. Historical originality is based on comparison with identified accessible literature and remains subject to additional review. No independent audit has been performed.
