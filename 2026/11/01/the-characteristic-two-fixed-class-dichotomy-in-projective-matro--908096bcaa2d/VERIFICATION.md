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

The proof is a universal chain-level argument: transitive top simplices, an orientation-reversing facet stabilizer, and the exact extension multiplicity of each independent codimension-one face. There are no top-dimensional boundaries from higher simplices. No finite sample substitutes for any of these deductions.

Execute `python3 verify_pg_fixed.py` in a directory containing the program. It uses only the Python standard library and tests seven \((q,r)\) instances over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\); it checks all projective bases and their codimension-one incidences, and a representative orientation-reversing coordinate transposition. The recorded expected output is `VERIFIER_OUTPUT.txt`. The samples do not check all group elements in large dimensions, which is unnecessary for the general argument.

Self-review: passed. Independent audit: not yet performed.
