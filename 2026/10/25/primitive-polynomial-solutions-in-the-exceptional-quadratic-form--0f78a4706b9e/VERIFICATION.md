---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-28.md",
      "INDEPENDENT_AUDIT_2026-10-28.json"
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

Set U=u+1, A=2Uv, B=U²−2nv² and C=U²+2nv²; expand C²−B²=8nU²v²=2nA². For c!=0, x=−cnA²,y=−cB²,z=C² gives F_c(x,y,z)=c²n²A⁴ and t=c²n²A³BC squares nxyzF. For c=0, x=nA²,y=B²,z=C²,t=nABC(nA²+B²) likewise solves. In Q[u,v], A and B are coprime because B has nonzero U² coefficient and nonzero v² term for n≠0, so x and y share no nonconstant factor. Since z=C² has u⁴ coefficient 1, no common integer prime content exists. Symbolic independent polynomial checks validate both branches for arbitrary formal n,c, beyond finite parameter substitution.

## originality

PASS

Gawron–Ulas 2015 already prove polynomial-coprimality at n=1 (Corollary 2.2) and nonexceptional forms for general n, and primitive integer solutions for exceptional forms. Their Remark 2.3 and Conjecture 2.4 explicitly separate the unsettled integer-polynomial-coprimality case when n is arbitrary in the exceptional family. Thus the n=1 subcase and integer solutions are prior; the new uniform explicit exceptional polynomial family for every n!=0 is the assessed remainder. Searches found no stronger covered solution; unindexed preexisting parametrizations remain a risk.

## value

PASS

Supplies a compact explicit parametric construction resolving a named and algebraically natural exceptional coefficient locus left outside the prior theorem. Primitive content over Z[u,v] is essential: identity-only or Q[u,v]-coprimality alone would not address the stated question.

The dated certificate retains the supplied scientific assessment, sources and limitations.
