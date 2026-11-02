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

The supplied `verify_gap_product.py` calculates the Product-Gap distribution directly from all \(k\)-report subsets of \(k+1\) distinct positions. It uses `fractions.Fraction` and independently evaluates each omitted agent's nearest-facility distance. It cross-checks the exact harmonic-gap expression for all 87,376 positive integer-gap profiles with \(2\le k\le8\) and every gap in \(\{1,2,3,4\}\); it also checks the universal \(k-\tfrac12\) inequality and the interior-minimum \(k-1\) inequality for each profile, and verifies the endpoint formula and interior-limit examples at several finite scales.

Command: `python3 verify_gap_product.py`.

Actual output: `VERIFY_OK exact_profiles=87376 k=2..8 integer_gaps=1..4 endpoint_and_interior_asymptotic_families=checked`.

The analytical derivation in `RESULT.md` covers arbitrary real positive gaps and arbitrary integers \(k\ge3\). Finite enumeration cannot establish that infinite statement. The program has no third-party dependencies and runs with ordinary Python 3.
