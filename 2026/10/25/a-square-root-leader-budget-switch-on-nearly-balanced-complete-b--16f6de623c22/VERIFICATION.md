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

# Verification record

The standalone `verify.py` (Python standard library) was executed from the delivered package source. It returned the exact output contained in `verification_output.txt`:

```
VERIFY_OK exact_allocation_cases=353496 strict_chord_cases=166650 direct_orbit_inversions=220 full_subset_inversions=666 integer_tie_cases=6
```

The checker independently assembles full grounded Laplacian matrices and inverts them using exact rational Gauss–Jordan elimination, then compares the traces with the proved two-part formula. All possible labeled leader sets were examined for \(2\le m\le4\). The full feasible allocation range for \(2\le m\le100\) was checked, including perfect-square ties and high-budget boundaries. The analytic proof establishes all integer parameters and is separate from these finite computations.

No probabilistic simulations or numerical tolerance arguments enter the theorem. Independent mathematical audit has not been performed.
