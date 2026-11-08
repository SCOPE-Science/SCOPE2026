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

Starting from the two exact recurrence equations, W Delta q +tK q=0 with nonsymmetric W=[[1+a/2,0],[(1-omega)c/2,1]]. For temporal mode z, x=2-z-z^-1, det(tK-xW)=p x²-Sx+R. The discriminant decomposes into the square (a-pb+(1-omega)c²/2)² plus (4+2a omega)c², proving two real positive spatial roots; the smaller root is <a/p<2 for C≠0, and the C=0 decoupled case is explicit. A positive spatial root has power-bounded temporal solutions precisely for x<4; x=4 gives repeated -1 with linearly growing n(-1)^n and x>4 an exponentially growing mode. Thus the larger root must be below four, equivalent to det(tK-4W)=16+4(A-B)t-[AB+(2omega-1)C²]t²>0, a strictly concave quadratic with exactly one positive root. Solving gives the stated T*(omega), monotone decreasing with omega if C≠0 and separator 4/B at omega=1/2. For A=B, C²↑AB, ratio of omega0 to midpoint ceilings diverges within SPD domain. Independently verified determinant/discriminant symbolic identities and 36 SPD modal cases; numerical checks alone are not proof for all matrices.

## originality

PASS

PASS, qualified: Chung–Efendiev–Leung–Vabishchevich introduce precisely the weighted partially explicit split and analyze omega=1 and omega=0 with sufficient energy conditions. The explicit necessary-and-sufficient 2D power-boundedness frontier, its all-omega dependence and sign-reversal phase were not found in that primary source. Generic von Neumann methods may make the computation short but do not constitute an already stated boundary formula.

## value

PASS

The coupling sign switches the effect of off-diagonal stiffness on allowable time steps across the weight omega=1/2; this isolates a meaningful stability mechanism and provides sharp boundary design guidance, rather than just a special-case normalization. Arbitrarily large near-singular gain strengthens the significance, while no accuracy claim is made.

The dated certificate retains the supplied scientific assessment, sources and limitations.
