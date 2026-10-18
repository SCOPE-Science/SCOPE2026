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

# Reproducibility and limits

Run `python3 verify_coronene.py` with Python 3 and no third-party packages. The source code and `verification_output.txt` are included in the same complete package.

The program enumerates the seven fused hexagons from integer coordinates, constructs the twenty-four-vertex graph and all 62,506 nonempty independent faces, and verifies the entire acyclic face-poset matching (31,251 pairs and 392,364 oriented cover relations), retaining one critical zero-cell, one five-cell and two seven-cells. The critical face bitmasks are 1, 1376424, 12629012 and 12751380. The 62,506-face directed topological order has SHA-256 digest `35cbe1f8681194f7f0b3322ad71f349e7e696b8a4dd938e88720c7aeb1ec80b1` using little-endian unsigned 32-bit face bitmasks. The program separately computes all twelve signed reduced Lefschetz traces and all sixteen dihedral-subgroup character averages.

The mathematical proof supplements these finite checks with the discrete-Morse CW theorem, the simplicial Hopf trace formula, representation theory of finite dihedral groups, and rational transfer. The executable certificate proves the integral homology groups of this single finite complex, but does not compute higher-cell attaching maps, integral quotient torsion, or similar invariants for other patches. No external audit is represented as complete.
