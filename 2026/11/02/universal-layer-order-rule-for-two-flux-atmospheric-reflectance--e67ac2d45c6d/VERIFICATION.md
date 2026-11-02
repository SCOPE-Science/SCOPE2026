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

Run `python3 verify.py` using Python standard library only. The program computes layer maps and all cross-checks from exact rational arithmetic, independently of floating approximations. The resulting test lines include the three-layer exact fractions, 4,800 exact pairwise commutator/sign checks, 10,944 exhaustive-permutation comparisons across sampled stacks and conservative-layer commutativity.

The logical all-parameter proof is the matrix-commutator and adjacent-swap argument of `RESULT.md`. The finite verification set cannot prove the infinitely quantified theorem, uniqueness in untested cases, or historical priority. The optical reduction itself assumes hemispheric two-flux symmetry, passivity, positive finite transmission, and fixed layer optical properties.
