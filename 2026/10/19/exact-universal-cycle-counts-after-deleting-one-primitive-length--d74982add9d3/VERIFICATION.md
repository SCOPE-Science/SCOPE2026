---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

A primitive three-letter orbit deletes three edges forming a directed cycle on three distinct two-letter vertices, so the residual graph is balanced with degrees q−1 at exactly those vertices. On the full de Bruijn graph A²=J; on the complement of constants the inverse of qI−A is given by truncating the nilpotent inverse series after A/q². Consequently det(L+J/q²)=q^(q²−1), the full cofactor is q^(q²−3), and the rank-three determinant lemma gives the stated tree factors. The 001 vertex adjacency restriction has rows (1,1,0),(0,0,1),(1,1,0); for 012 it has only the three cyclic-shift entries. Taking successive-row differences in these restrictions verifies the two compressed matrices and their determinants. The determinants are positive for q≥3, so a rooted tree exists and balance implies strong connectivity. BEST with a fixed first edge counts each cyclic edge list once; distinct triple labels give precisely the labeled-position-rotation convention. The factorial change is (q−1)^−3; (q−3)/q⁴ is the difference of tree ratios, not the difference of U_q/D_q without that factorial factor. Independent exact cofactor and tour enumeration (`python3 reproductions/1.py`) found ternary cofactors 189 and 12,096 circuits in each case; the binary 001 deletion leaves its 000 loop isolated and has zero circuits. The supplied script was inspected, not executed. The finite count is corroboration of the all-q determinant argument, not its substitute.

## originality

PASS

Pass is for the two explicit deletion counts and their comparison for labeled alphabets q≥3. The binary nonexistence is supplementary and is covered by the inspected binary-deficit record. None of the closest inspected statements provides the two evaluated factors in the general alphabet regime.

## value

PASS

A single rotation orbit is a natural balanced restriction of the full factor dictionary, and length three permits the first comparison of two primitive orbit types with identical removed-edge degree effects. The exact count resolves whether the overlap pattern affects cycle multiplicity: equality at three symbols and a strict ordering thereafter. These formulas give usable counts for the whole alphabet family, rather than merely a small-instance table or an instruction to evaluate a generic determinant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
