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

With Python 3.10 or newer, execute `python3 verify.py character.csv` in the directory containing `verify.py` and `character.csv`. The script uses only the standard library and checks all 65,536 vertex subsets without sampling. `verification_output.txt` records its deterministic expected console output.

The program checks (i) forest membership by a union-find cycle detector and independently by the Euler edge/vertex/component formula; (ii) the face vector; (iii) the entire augmented discrete-Morse matching and a full directed-Hasse topological sort; (iv) the exact signed integral Morse boundary by oriented face recursion and a determinant \(-1\) minor; (v) independent ordinary mod-two simplicial boundary ranks; and (vi) the character at every coordinate-permutation and bit-translation automorphism, by the signed Lefschetz fixed-face formula.

The exact critical face masks and integral differential appear in `RESULT.md`, making the calculation independently inspectable. The complete computed character table is `character.csv`. The script compares an existing table byte-independently to the complete recomputed rows; when the destination is absent, it creates the table. Verification output is not evidence of an independent audit and does not verify absolute priority against all possible literature.
