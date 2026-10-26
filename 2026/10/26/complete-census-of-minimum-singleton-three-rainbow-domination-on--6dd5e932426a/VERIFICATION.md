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

# Reproducibility and verification

The enclosed `verify.py` is a standalone Python 3 program using only the standard library. Run `python3 verify.py` and compare its complete output with `verify_output.txt`.

Three distinct finite verification routes are implemented. The first enumerates **every** assignment from \(\{0,1,2,3\}\) to vertices of \(C_n\square K_2\) at \(n=3,4,5\), constructs the graph's actual open neighborhoods, and directly evaluates the defining condition. The second enumerates supports with zero, one, or two fully colored rungs and counts three-colorings through the pairwise inequality graph induced by each uncolored vertex. This verifies all three predicted coefficients for every \(3\le n\le24\). The third independently enumerates internal and terminal colors for each one-run kernel of length one through eight.

The output ends in `VERIFY_OK` only if every equality has been checked. These are finite exact computations and therefore corroborative only. They do not assert any independent audit and do not replace the combinatorial proof in `RESULT.md`.

The source distinguishes named colors, labeled vertices, and all four symbols precisely. No external packages, downloaded datasets, or network access are needed to replay the checks.
