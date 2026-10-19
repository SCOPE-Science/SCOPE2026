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

# Finite verification and proof scope

The standalone Python 3 checker `checker.py` enumerates every cyclic rotation class with one doubled symbol and all other letters unique for alphabet sizes \(2\le q\le7\). A canonical representative starts at singleton symbol `1`, guaranteeing each rotation class occurs once.

For each period, the code directly compares pairs of adjacent blocks from the periodic sequence, searches all nonidentity rotations of the first block, and records the first match. It tests all starts and half-lengths \(2\le h\le2(q+1)\). The detector deliberately does not use the Parikh-vector lemma or adjacent-repeat classification.

Observed class table:

| \(q\) | All circular classes | First mesosome at length \(2q\) | No mesosome in tested window |
| ---: | ---: | ---: | ---: |
| 2 | 1 | 1 | 0 |
| 3 | 3 | 2 | 1 |
| 4 | 12 | 6 | 6 |
| 5 | 60 | 24 | 36 |
| 6 | 360 | 120 | 240 |
| 7 | 2520 | 720 | 1800 |

Terminal output: `NEAR_PERMUTATION_MESOSOME_PASS`. Run `python3 checker.py` with no dependencies. The infinitely many possible half-lengths beyond the check are handled by the structural residue/Parikh proof in `RESULT.md`, not by extrapolating the table. The proof assumes exactly the stated letter content, with cyclic adjacency including the period boundary.
