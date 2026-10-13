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

Run `python3 verify.py` in the directory containing `verify.c` and `certificate.json`.

The checker compiles the exact exhaustive enumerator and generates restricted-growth representatives, which are unique representatives of alphabet-permutation orbits. At each extension it uses the standard rich-word characterization via a unioccurrent palindromic suffix and directly compares Parikh vectors for every possible newly created abelian cube.

The exhaustive search returns exactly four canonical words at length \(180\) and zero at length \(181\). Since every length-\(180\) representative uses all three symbols, this gives \(4\cdot 6=24\) labeled extremizers.

For the four final words only, the verifier then performs a separate direct check that explicitly enumerates all palindromic factors and all possible abelian-cube factors. Finally it canonicalizes reversals and verifies the pairings \(1\leftrightarrow3\) and \(2\leftrightarrow4\), giving two orbits under relabeling and reversal.

The verification proves only the stated equality-case classification at the ternary maximum. Independent audit has not been performed.
