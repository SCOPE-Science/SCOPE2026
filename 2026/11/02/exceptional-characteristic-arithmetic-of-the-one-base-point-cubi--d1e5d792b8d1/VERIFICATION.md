---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Resultant_y(F,G)=x^9 and F_y(0,0,1)=1 prove the unique length-nine base point. Gröbner reductions of the full finite Jacobian ideal in char2 give (x,y+t,t³+1), and char3 (x−y²,y³−1,t); homogeneous derivatives exclude singular support at infinity. The char2 tangent cone x²+txv+t²v² has branch directions governed by u²+u+1, split over F_{2^r} iff r even; at t=∞ the tangent is xy and split. In char3 at (1,1,1), the exact local equation w²+w v²−v³=0 is A2 cusp; the other singularity is a split node. Normalization P1 gives q+2/q/q+1 point counts. Hasse invariants are t (char2) and t² (char3); the discriminant of the projection quartic is −256(t³+27), I=t(t³+24), implying j(C_t)=−t^9 in char3. Independent exact resultants, Jacobian systems over F2/F3, Hasse coefficient, quartic discriminant, and prime-field projective singular sets corroborated.

## originality

PASS

Moschetti–Pirola–Stoppino (2024 original, expanded 2025) use the exact same integral generators but prove four nodal fibers over C; this does not imply their bad-characteristic plane singularity splitting, point counts or inseparable characteristic-three modular map. The cusp of F at characteristic three is already known from 2020 and not claimed independently original. Classical elliptic surface Kodaira and extremal classifications may constrain resolved surface types, but do not fix these marked plane-node and rational-branch data from the stated formulas. Qualified.

## value

PASS

Bad reduction of a distinguished integral elliptic pencil is a natural arithmetic-geometric invariant. The complete char2/char3 singular-fiber and rational branch count, Hasse ordinarity and purely inseparable ninth-power j map quantify exactly where the characteristic-zero geometry fails; specific useful mathematical data, not a parameter renaming.

The dated certificate retains the supplied scientific assessment, sources and limitations.
