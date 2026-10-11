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

# Verification of the permutahedral vertex-cofibration theorem

Run from the directory containing the package files:

```sh
python3 verification/verify_morse.py
python3 verification/check_polynomial.py
```

`verify_morse.py` independently builds all 24 vertices and 36 edges by adjacent-position transpositions. It enumerates the complete face sets including the empty face for the full graph, one vertex deletion and one closed-neighborhood deletion. The exact face totals are 37076, 27941 and 9135. It constructs the stagewise elementary matching, checks no face is used twice and that the empty face is matched once, then enumerates every Hasse incidence and topologically sorts the corresponding directed graph to certify no closed gradient path. Directed incidences: 219240, 162087, 48018; critical augmented dimensions: four 5-cells, three 5-cells, one 4-cell. The assertion-based verifier prints `PERMUTOHEDRON_LOCAL_GLOBAL_MORSE_OK` on completion.

`check_polynomial.py` independently reconstructs the same graph using value swaps and verifies its isomorphism to the position-swap presentation under permutation inversion. A memoized deletion recurrence computes all three complete independence polynomials, yielding values at negative one of 4, 3 and -1. The cross-check terminates with `INDEPENDENT_POLYNOMIAL_OK`.

The matching computation is exhaustive for the specified finite graph, with graph automorphisms transferring its local conclusions to all vertices. These programs do not establish any result for permutahedra of other orders and do not certify bibliographic priority or constitute independent scientific review.
