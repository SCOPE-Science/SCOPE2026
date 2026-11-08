---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For connected simple undirected G of order <=4 and uniformly chosen single mutant, derived the fourteen-state harmonic system with gain rates r/d_i and loss rates 1/d_j and absorbing boundary values 0,1. The six connected order-four types and six one-edge insertions are exhaustive by canonical labeled-graph enumeration. Exact rational functions give negative star→paw, path→C4, paw→diamond, diamond→K4, positive C4→diamond, and path→paw sign equal to P(r)=12780r^9+14805r^8-177144r^7-665280r^6-1193573r^5-1412701r^4-1179232r^3-667896r^2-206727r-19404 for every r>1. Positive denominator factor shifts, one Descartes coefficient sign change, P(1)<0 and positive leading coefficient give exactly one crossing, 4.887<r_c<4.888. P3→K3 is negative for r>1; K2 has no edge insertion. Independently rebuilt the finite harmonic matrices with rational arithmetic: at r=2 path→paw = -35293/6486192; at r=5 it is +10823483975/182762925076026; also tested noncrossover signs. These samples corroborate, not replace, polynomial and enumeration arguments.

## originality

PASS

Prior Broom–Rychtář–Stadler (2009) already reports the qualitative path/paw ranking reversal for a finite fitness grid, and Broom–Rychtář (2008) supplies exact star and line processes. The tested novelty is the exact ninth-degree crossover threshold and its uniqueness over all r>1 together with the six-type all-fitness sign classification; neither the 2008 nor 2009 full paper provides this stated complete comparison. General Moran isothermal theorem is accepted prior theory. Best-of-knowledge priority remains provisional.

## value

PASS

Mathematical value is a smallest-order complete parametric phase diagram for a natural graph modification in a widely used evolutionary process. The sharp four-vertex minimum and one-root crossover strengthen already observed qualitative reversal, without claiming new qualitative phenomenon or extension to larger graphs.

The dated certificate retains the supplied scientific assessment, sources and limitations.
