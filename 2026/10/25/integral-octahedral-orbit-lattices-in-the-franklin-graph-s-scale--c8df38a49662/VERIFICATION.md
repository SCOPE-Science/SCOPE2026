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

The included `verify_franklin.py` reconstructs the twelve-vertex graph and the complete scale-two flag complex. Its actual executed checks include the \((12,48,76,45,12,2)\) face vector; modular ranks \(37\) and \(35\); \(35\) exactly generated signed third boundaries; a determinant \(-1\) integral minor from those boundaries and four independent octahedral cycles; exact lattice coordinates for twenty primitive octahedra; \(48\) graph automorphisms; octahedron orbits of \(8\) and \(12\); orbit Smith factors \((1,1,1,1)\) and \((1,1,1)\); and all induced mod-two second homology checks on vertex sets of size at most six. The script checks all chain identities in the **full** chain groups, not only projected minors.

The verifier uses `networkx` and `sympy` as specified in `requirements.txt`; the original successful output is embedded separately as `verification_output.txt`. These are exact finite calculations. The flag-minimal-support argument in `RESULT.md` justifies why six is a sharp geometric lower bound over arbitrary coefficient fields. No assertion about infinite families or independent external verification is made.
