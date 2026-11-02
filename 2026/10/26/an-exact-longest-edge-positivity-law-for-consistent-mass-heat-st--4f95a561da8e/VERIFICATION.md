---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

Reconstructed assembled consistent P1 mass/stiffness on a finite metric tree, n>=3, all Neumann/Kirchhoff unknowns retained: each edge has beta=h/6-t/h in H=M+tK. For every t>0 the positive branch inverse g obeys 1/g>=h/3+t/h, so Schur complement gives 0<P_bb<1 and P_ab=g[(h/6)(1-P_bb)+(t/h)P_bb]>0 for adjacent vertices. For t<h_uv^2/6 choose w adjacent to u distinct from v: P_vw=-beta_uv*g_v*P_uw<0 at distance two. For t>=max h_e^2/6 H is positive definite Stieltjes, hence H^{-1}M>=0, and P(0)=I; with exactly two vertices no distance-two witness and all entries remain positive. Independently computed nine exact rational 3-vertex path matrix-step checks, including thresholds and strict witnesses. Finite tests do not establish the general theorem.

## originality

PASS

Existing FEM positivity theory establishes the Stieltjes sufficient mechanism and discusses nonpositivity of consistent-mass discretization at small times, typically on Euclidean-domain meshes. The sharp necessary-and-sufficient longest-edge law for arbitrary graded metric trees with Neumann/Kirchhoff coupling and a distance-two negative certificate was not established in the reviewed primary sources. General M-matrix sufficiency is not claimed as new.

## value

PASS

Positivity preservation is essential for monotone parabolic numerical schemes. The exact longest-edge cutoff for any finite graded metric tree and edge-specific negative witnesses are informative for choosing backward-Euler step sizes on networks, beyond generic sufficient conditions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
