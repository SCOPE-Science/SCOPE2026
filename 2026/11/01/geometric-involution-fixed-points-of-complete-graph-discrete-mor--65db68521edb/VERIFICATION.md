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

# Reproducibility and evidence limits

Run `python3 verify.py` from this directory. It uses Python's standard library, exhaustively constructs involution arrow orbits of the **original** complete directed graph, checks incoming-degree and cycle conditions, enumerates all admissible orbit faces, computes exact mod-two boundary ranks, and compares the resulting reduced Betti numbers and Euler characteristics with the theorem's formulas for ten finite parameter pairs. It separately tests the \((f,t)=(0,1)\) empty-fixed-space exception. The observed successful output terminates with `VERIFY_OK`.

The tested nonempty pairs are \((0,2),(0,3),(1,1),(1,2),(1,3),(2,1),(2,2),(3,1),(3,2),(4,1)\). These checks do not certify the unrestricted theorem; that conclusion rests on the general orbit-lifting argument and the complete-source shellability, expansion-shellability, and directed matrix--forest theorems cited in `RESULT.md`. The exact homotopy classification beyond tested sizes has not received independent review. Ordinary Morse, rather than the distinct strong Morse complex, is the mathematical object.
