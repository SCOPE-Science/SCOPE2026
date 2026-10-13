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

The verification script uses exact integer/rational projective arithmetic. It reads no external data: the nine point coordinates are transcribed from the cited source and are stated explicitly in RESULT.md. It checks that projective dualization produces exactly the nine \(B_3\) line normals, exhaustively enumerates all pairwise line intersections and their multiplicities, and verifies \(t_2=6,t_3=4,t_4=3\). It also constructs the 24 projective signed-permutation transformations and checks that each preserves the line set.

The script is a certificate for these finite algebraic steps, not a substitute for the proof that the stabilizer is maximal. That proof is given in RESULT.md by using the three unique fourfold points to force monomial form and then forcing the diagonal ratios to be signs. The group-theoretic identification with the quartic automorphism action also uses the published statement \(\operatorname{Aut}(K)\cong S_4\) and the published quadruple-point–involution correspondence.

No claim of independent audit is made.
