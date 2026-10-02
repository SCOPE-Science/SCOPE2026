---
{
  "schema_version": 1,
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-09-30.md",
      "INDEPENDENT_AUDIT_2026-09-30.json"
    ]
  },
  "lean_verification": {
    "status": "unknown",
    "evidence": null
  },
  "expert_attestation": {
    "status": "unknown",
    "evidence": null
  }
}
---

# Independent mathematical audit

## correctness

PASS

Independent direct pattern enumeration of all permutations at n=6 and n=7 reproduced (U,C1,C2)=(394,393,393) and (1806,1781,1785), and the two-sided n=7 differences (21,25), which alone proves the Wilf split and minimal separating index. Source-level inspection of enum.c verifies that max insertion is exhaustive: a newly created 2413/3142 occurrence must contain the new maximum in the unique max position tested by sep_ok, and a newly created 123654/321654 occurrence exists exactly when an increasing/decreasing pre-max triple has maximum below the minimum of a decreasing post-max pair, which is exactly the thit predicate. The logged n=8..12 counts therefore follow from the inspected exhaustive recursion; the decisive n=7 theorem does not depend on those higher terms.

## originality

PASS

Exact searches for the two basis patterns found the current SCOPE record but no prior source stating this pairwise split. General separable-permutation literature supplies the universe and structural methods, not these two finite counts.

## value

PASS

A first-separation index for two naturally defined principal subclasses of the separable permutations is a concrete classification datum: it conclusively resolves one Wilf-equivalence cell, supplies minimal two-sided witnesses, and can be used in subsequent classification or generating-function work. The result is finite but not arbitrary in the sense of the value bar because Wilf classification of pattern classes is itself a natural invariant problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
