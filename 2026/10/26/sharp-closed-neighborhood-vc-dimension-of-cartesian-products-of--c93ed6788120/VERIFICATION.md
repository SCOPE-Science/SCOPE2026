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

Execute the embedded `verify.py` with Python 3.10 or later. It constructs \(X\) as all coordinate tuples, forms every radius-one Hamming ball directly from the distance definition, tests every combination anchored at the first vertex of sizes one through four, and asserts the claimed piecewise VC dimension. Anchoring is justified by transitivity of the product of alphabet permutation groups. It also checks eight target traces for explicit three-point witnesses.

The executable was run after writing the file: nineteen parameter choices passed, with 14,580 anchored candidate subsets tested. In each finite instance, the checker found no shattered four-point subset and exactly the predicted largest shattered-set size. This is finite corroboration only. All-parameter correctness rests on the coordinate-star and rook-cross arguments in RESULT.md.

No independent third-party review or external proof certification has been performed.
