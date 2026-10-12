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

The exact checker `verify_schur_galois.py` was replayed from the packaged file. It verifies:

1. for \(\alpha^4=-1\), the pullback of \(x_0^4-x_0x_1^3-x_2^4+x_2x_3^3\) under \((x_0,x_1,x_2,x_3)=(X,-Y,\alpha Z,-\alpha W)\) is exactly \(X^4+XY^3+Z^4+ZW^3\);
2. the eight Miura--Taki Galois points map exactly to the four points of \(L\cap S\) and four points of \(M\cap S\) used by Rojas--Lira;
3. all 16 joins \(\overline{p_iq_j}\) lie identically on the Schur quartic;
4. their Plücker coordinates give 16 distinct projective lines; and
5. their incidence degrees are four at each of the eight marked points, giving \(K_{4,4}\).

Fresh replay output:

`VERIFY_OK transform=S8_to_Schur galois_points=8 join_lines=16 incidence=K4,4 each_galois_point_on_join_lines=4`

## Literature-dependent global steps
The checker does **not** claim to enumerate all 64 lines. The proof separately uses Rojas--Lira, Lemma 3.1, for the theorem that these 16 joins are every Schur line meeting \(L\) or \(M\). It uses Nurowski's complete incidence census for the theorem that the full 64-line arrangement has exactly eight quadruple points and that its 16 distinguished lines are exactly those incident with two quadruple points. These are the precise boundaries between computation and cited global input.
