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

The all-parameter argument is in `RESULT.md`, with explicit cross-intersection normal forms, atom-based symmetry recovery, and sound Horn-rule saturation plus lower bounds. Independently executable finite corroboration is in `artifacts/verify.py` (standard Python 3, no nonstandard dependencies). Run:

```sh
python3 artifacts/verify.py
```

The program constructs each Galois closure directly from the \(mn\) incidence crosses; compares all subset closures with the predicted finite closed-set family on boards \((2,2)\), \((2,3)\), \((2,4)\), \((3,3)\), \((3,4)\), and \((4,4)\); checks full forward-chaining saturation on all subsets in the first five cases; tests the four-corner and three-matching lower-bound witnesses for thick boards; and checks all independent permutations of two rows, and their interchange, when the long side has length three or four.

The completed run reported:

```text
CASE 2 2 concepts 16 subsets 16 iterative 0 PASS
CASE 2 3 concepts 25 subsets 64 iterative 2 PASS
CASE 2 4 concepts 36 subsets 256 iterative 2 PASS
CASE 3 3 concepts 44 subsets 512 iterative 3 PASS
CASE 3 4 concepts 69 subsets 4096 iterative 3 PASS
CASE 4 4 concepts 114 subsets 65536 iterative 3 PASS
THIN_WREATH 3 elements 72 PASS
THIN_WREATH 4 elements 1152 PASS
VERIFY_OK closure_family=PASS concept_counts=PASS arity_bounds=PASS thin_symmetry=PASS
```

The forward-chaining calculation was not exhaustively run on all subsets for the \((4,4)\) board; closure sets were. The program does not enumerate the entire generic automorphism groups: their upper bounds and realization are proved mathematically. No infinite theorem is inferred from finite observations, and independent external validation has not been performed.
