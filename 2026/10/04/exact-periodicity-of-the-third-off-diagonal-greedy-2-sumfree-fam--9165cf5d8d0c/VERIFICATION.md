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

The theorem is proved symbolically in `RESULT.md`. The exact-integer program `verify.py` provides corroborative checks from an independent implementation of the greedy definition.

Running

`python3 verify.py`

produces exactly:

`VERIFY_OK f_cases=195 range=6..200 periods=20`

For every tested \(f\), the program compares the complete greedy set with the stated closed form through twenty modulus lengths. It additionally checks the modular identity \((E+R)\bmod M=R^{\mathrm c}\), the disjointness \((R+R)\cap R=\varnothing\), the exceptional-residue disjointness, and \(|R|=f+4\).

Finite checking does not certify the theorem for untested \(f\). The infinite quantifier is justified by the interval identities and induction in `RESULT.md`. The verification does not address bibliographic originality beyond the source comparisons recorded in `AUDIT.json`.
