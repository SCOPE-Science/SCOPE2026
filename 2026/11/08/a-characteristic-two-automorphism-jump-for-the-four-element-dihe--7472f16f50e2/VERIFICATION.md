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

# Verification

`CHECK.py` tests the defining bilinear multiplication \(e_i e_j=e_{2j-i\bmod4}\) directly for each candidate transformation, independently of the symbolic block-proof.

For \(\mathbb F_2\), all \(20,160\) invertible four-by-four matrices are enumerated and the exact set of automorphisms (\(32\) matrices) is compared with the predicted normal form. For \(\mathbb F_3\) and \(\mathbb F_5\), each predicted matrix and thousands of seeded random nonmembers are tested. For \(\mathbb F_4\), the checker uses polynomial-basis multiplication modulo the irreducible polynomial \(z^2+z+1\), tests all \(512\) predicted automorphisms, and also tests random nonmembers.

Run `python3 CHECK.py` in the directory containing this file. The expected terminal output is embedded separately as `CHECK_OUTPUT.txt`. These checks are finite experiments; they cannot prove the theorem for all fields. The unrestricted conclusion follows from the normal-form argument in `RESULT.md`.
