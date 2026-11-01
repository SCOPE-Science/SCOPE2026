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

# Reproduction and proof boundary

Run `python3 paley7_multipath_verify.py`, requiring only Python 3 standard-library modules. The source reconstructs the quadratic-residue digraph, enumerates every arc subset allowed by the multipath condition, computes all oriented simplicial boundaries, verifies the complete acyclic Morse matching, checks exact integer unit Smith reduction, and computes mod-two cup-one squares on fifteen independent degree-three cohomology generators.

Expected face vector: `(21,168,630,1113,819,189)`. Expected critical cells: `{0:1,3:22,4:45,5:24}`. Expected Morse integer unit factors: `7`, remaining nonunit factors: `0`. Expected top Morse boundary: zero. Expected \(Sq^2\) rank: `0`. Expected terminal marker: `PALEY7_MULTIPATH_INTEGRAL_HOMOTOPY_VERIFIED`. The actual execution output is `verification_output.txt`.

The code establishes finite assertions exhaustively; the general homotopy-theoretic deduction from the unit cellular cancellations and vanishing Steenrod square is explained in `RESULT.md`. It does not verify any broader parameter family or determine independent external validation.
