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

# Reproducibility

Run `python verify.py` using Python 3. The checker is standalone for all graph, fort, forcing, and fort-packing operations; if SciPy is available, it additionally solves finite fractional-transversal linear programs. No external graph package is required.

The checker directly constructs every original crown-graph neighborhood, exhaustively enumerates vertex subsets for \(3\le n\le8\), and independently identifies inclusion-minimal forts by asking whether **any** proper subset is a fort. This stronger test is essential because a property may reappear after removing several vertices even when removing any single vertex invalidates it. It also replays every standard zero-forcing initial coloring for \(3\le n\le7\) and verifies all coefficients of the counting polynomial, computes optimal disjoint fort packings by subset dynamic programming, and tests the fractional linear program when an LP library is installed.

Recorded execution:

```text
FULL_SUBSET_MINIMALITY_OK 3 5
FULL_SUBSET_MINIMALITY_OK 4 14
FULL_SUBSET_MINIMALITY_OK 5 30
FULL_SUBSET_MINIMALITY_OK 6 55
FULL_SUBSET_MINIMALITY_OK 7 91
FULL_SUBSET_MINIMALITY_OK 8 140
DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK 3 6
DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK 4 30
DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK 5 90
DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK 6 210
DIRECT_ALL_ZERO_FORCING_SETS_AND_POLYNOMIAL_OK 7 420
EXACT_FORT_PACKING_DP_OK 3 2
EXACT_FORT_PACKING_DP_OK 4 2
EXACT_FORT_PACKING_DP_OK 5 3
EXACT_FORT_PACKING_DP_OK 6 4
EXACT_FORT_PACKING_DP_OK 7 4
INDEPENDENT_FRACTIONAL_LP_OK 3 2.0
INDEPENDENT_FRACTIONAL_LP_OK 4 2.66666667
INDEPENDENT_FRACTIONAL_LP_OK 5 3.33333333
INDEPENDENT_FRACTIONAL_LP_OK 6 4.0
INDEPENDENT_FRACTIONAL_LP_OK 7 4.66666667
VERIFY_OK
```

The exact proof, rather than finite computation or floating-point linear programming, establishes all parameters for every \(n\ge3\). The code does not certify historical priority or independent mathematical validation.
