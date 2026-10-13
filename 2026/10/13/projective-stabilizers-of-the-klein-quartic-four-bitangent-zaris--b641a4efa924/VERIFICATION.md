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

Run `python verify.py` with the standard Python library. The script uses exact rational arithmetic in \(\mathbb Q(\zeta_7)\), where \(\zeta_7\) satisfies \(1+\zeta_7+\cdots+\zeta_7^6=0\).

It verifies the quartic-preservation identities for the three displayed generators symbolically, enumerates their projective closure and requires exactly \(168\) elements, reconstructs the \(28\) bitangent equations from the source, checks that every group element permutes those lines, and computes the three setwise stabilizers. It then requires stabilizer orders \(6,1,1\), the first stabilizer's order profile \(1:1,2:3,3:2\), its full permutation action on \(\{L_1,L_3,L_5\}\) while fixing \(L_2\), and orbit sizes \(28,168,168\).

The computation is exact but does not independently re-prove the source's theorem that the displayed lines are bitangents; it reconstructs their published equations. The identification of the generated \(168\)-element projective subgroup with the full group uses the classical Hurwitz bound for the source's smooth genus-\(3\) quartic.

Successful execution ends with `VERIFY_OK`.
