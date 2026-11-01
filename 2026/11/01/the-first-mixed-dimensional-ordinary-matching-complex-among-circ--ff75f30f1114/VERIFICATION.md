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

# Reproducible verification

Run `python3 verify_circular_ladders.py` using Python 3 standard library. The standalone program has all graph definitions, data and algorithms built in. It regenerates all nonempty matchings independently by backtracking and exhaustive bitmasks, verifies their equality, checks every matched pair, performs a complete directed-Hasse acyclicity sort, reconstructs integral signed Morse differentials, and verifies rank/unit-minor certificates over exact arithmetic. Separately, it reduces ordinary simplicial boundaries over \(\mathbb F_2\) and checks the Euler characteristic.

| Graph width | Nonempty faces | Morse pairs | Critical dimensions | Integral upper differential | Mod-two Betti, including \(\beta_0\) |
| --- | ---: | ---: | --- | --- | --- |
| 3 | 31 | 12 | \(0:1,1:6\) | none | \((1,6,0)\) |
| 4 | 107 | 51 | \(0:1,2:4\) | none | \((1,0,4,0)\) |
| 5 | 341 | 165 | \(0:1,2:5,3:5\) | rank three with a maximal minor of determinant \(-1\) | \((1,0,2,2,0)\) |
| 6 | 1103 | 544 | \(0:1,3:13,4:1\) | rank one with a unit entry | \((1,0,0,12,0,0)\) |

The actual program output is `verification_output.txt`, ending in `CYCLIC_LADDER_MATCHING_INTEGRAL_MORSE_VERIFIED`. This is an exhaustive finite check for the stated graph sizes, not an infinite theorem and not independent expert validation. The integer degree argument in RESULT.md is needed to upgrade homology to the asserted homotopy wedge; mod-two checks alone cannot do that.
