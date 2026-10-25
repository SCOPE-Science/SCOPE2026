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

# Exact verification of the bidirected biclique calculation

Place `verify.py` and `morse_certificate.json` in one directory and run `python verify.py` using Python 3 with its standard library. The script recomputes simplices from arc sets, checks every collapse/critical operation in the 793-step certificate against the remaining face poset, checks acyclicity by topologically sorting the oriented Hasse graph, and checks exact mod-two boundary ranks for leaf counts one through six. The check was executed against the embedded artifacts; output included `ALL TESTS PASS`.

For six leaves, the face vector is \((24,192,600,600)\), 623 pairs use 1246 nonempty faces, and the critical cells use the other 170 faces: one zero-cell and 169 three-cells. No integral homology is inferred from a mod-two calculation: the complete acyclic Morse matching and the discrete-Morse CW theorem give the integral homotopy type.

For one through five leaves, independently computed nonzero reduced mod-two homology below degree three excludes two-connectedness, regardless of possible integral torsion. The result does not cover higher leaf counts, nor does this evidence constitute independent audit or external certification.
