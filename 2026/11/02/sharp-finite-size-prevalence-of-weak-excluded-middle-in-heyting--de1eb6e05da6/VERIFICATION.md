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

# Reproduction and limits

Run `python3 verify_wem.py` using Python 3; no external modules or downloaded data are needed. The code encodes a finite poset by a tuple of predecessor bitsets, enumerates its downsets, and evaluates pseudocomplement and double pseudocomplement directly from the definition. It separately computes the product formula from comparability components and counts join-irreducible-size extremizers.

Actual replay output from the packaged verifier:

```text
n=1 orders=1 failures=0 extremizers=0
n=2 orders=2 failures=0 extremizers=0
n=3 orders=7 failures=1 extremizers=1
n=4 orders=40 failures=15 extremizers=1
n=5 orders=357 failures=216 extremizers=1
n=6 orders=4824 failures=3741 extremizers=1
SAME_STRONG_DEGREES_DIFFERENT_WEAK_DEGREE_PASS 4/7 5/7
EXTREMAL_FAMILY_PASS n=3..16
WEAK_EXCLUDED_MIDDLE_EXACT_CHECKS_PASS
```

The naturally labeled enumeration represents every isomorphism class of finite posets up to six points, although it does not enumerate every arbitrary relabeling. All comparisons use exact integers and rational fractions. The independent direct evaluation confirms the all-size component expression in the tested range and the sharp upper bound and equality type there. The proof in `RESULT.md`, not this finite calculation, establishes the unrestricted theorem. This is not an independent human audit or an external mathematical certificate.
