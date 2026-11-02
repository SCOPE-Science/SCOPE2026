---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-27.md",
      "INDEPENDENT_AUDIT_2026-10-27.json"
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

For any epsilon>0 and finite m, select an arbitrarily high-dimensional E orthogonal to finite prefixes of all tested bases. Parseval gives sum_{k>N}||P_E b_k^(j)||²=d. With Gaussian g on E, union bounds using exp(-C/a)<=a exp(-C) for C>=1 and a∈(0,1] give P(||g||<sqrt(d/2) or some tested coefficient>epsilon sqrt(d/2))<=e^(-d/16)+2md e^(-epsilon²d/4)<1 for large d. Thus unit vectors u_n have simultaneously sup_j,k |<u_n,b_k^(j)>|<=1/n. Rank-one T_n x=<x,u_n>e_n have norm 1 and each tested image union is contained in bounded finite initial line segments plus a uniformly shrinking tail, hence relatively compact. The full unit-ball images contain e_n and coordinate delta_n∈(c0)*=l1 are weak-star-null but give supremum one. No finite-dimensional experiment substitutes for these universal quantifiers.

## originality

PASS

PASS best of knowledge. Mathematical statements and implication directions were compared to inspected primary literature, not merely titles or identical parameter names; residual risks explicitly retained.

## value

PASS

Gorokhova’s universal orthonormal-sequence criterion raises a natural exact question whether finitely many predetermined bases can certify collective limitedness. The constructed counterfamily rules out every such finite test simultaneously, even for rank-one operators and with the stronger relatively compact tested images; this pinpoints a genuine limitation of the universal quantifier.

The dated certificate retains the supplied scientific assessment, sources and limitations.
