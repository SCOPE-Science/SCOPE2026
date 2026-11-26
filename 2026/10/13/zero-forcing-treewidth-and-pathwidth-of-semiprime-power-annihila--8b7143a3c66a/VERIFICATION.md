---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

The 2a nonzero proper divisor ideals are precisely A_i=(p^i), 1≤i≤a, and B_j=(p^j q), 0≤j<a; each has a nonzero annihilator. Products give no A−A edges and the threshold i+j≥a for A−B or B−B edges (on distinct vertices). From A_1,...,A_{a−1}, the chronological forces A_i→B_{a−i} are legal because B_j with j>a−i are already blue, after which B_1→A_a→B_0 clears the graph. Writing U_i=A_i and V_i=B_{a−i}, the disjoint edges U_iV_i form K_a branch sets since U_jV_i is an edge for i<j. Independently, a width-(a−1) path decomposition consists of the a−1 bags {V_1,...,V_i,U_i,...,U_{a−1}} for 1≤i≤a−1, then {V_1,...,V_{a−1},U_a} and {U_a,V_a}. Vertex occurrences are consecutive; the bags cover U_iV_j iff j≤i and all V−V edges, as V_a has no V-neighbors. The minor lower bound, this path-decomposition upper bound and the forcing/width inequality establish equality; at a=1 the graph is K_2. A fresh finite enumeration from ideal-product divisibility for n=3·2^a, 1≤a≤7, gave Z=1,1,2,3,4,5,6 and minimum-set counts 2,2,6,23,63,207,559. This only corroborates Z for those rings. The packaged verify.py was read but not executed; its recorded finite checks are not the all-exponent proof.

## originality

PASS

The structural description of the arithmetic graph is prior background, as are general width/forcing inequalities. The supported distinct claim is the exact three parameters with matching explicit certificates for p^a q,  a≥2. Neither a same-family independence result nor a same-day equality for p²q² gives this claim.

## value

PASS

The exact equality joins a forcing process to a width obstruction in a natural family of ideal-product graphs. The matching explicit sequence, minor and boundary case provide usable sharp test instances of the general inequalities. The value is the structural equality and certificates; merely recovering a from the graph is not new information because its vertex count is 2a.

The dated certificate retains the supplied scientific assessment, sources and limitations.
