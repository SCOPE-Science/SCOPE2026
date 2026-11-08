---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-01.md",
      "INDEPENDENT_AUDIT_2026-11-01.json"
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

Every allowed cyclic triple a∈A,b∈B,c∈C has positive clockwise arc gaps p,q,r∈[1,m] summing a multiple of n=2m+1 but <=3m<2n, so sum=n and A,B,C occur in unique noninterlaced cyclic blocks. The first selected A after C is a unique anchor. Block widths u,v,w and gaps p,q,r satisfy all-to-all inequalities u+v+p<=m, v+w+q<=m, w+u+r<=m. Defining slacks i,j,k gives six nonnegative parameters u+v+w+i+j+k=m-1, and inverse positive gaps p=1+w+j+k etc; optional block interiors yield weight W(z,s)=s(1-z)/(1-(1+s)z). Three gap-slack factors (1-z)^-3 cancel W(z,s)^3 numerator, leaving n[z^(m-1)](1-(1+s)z)^-3=n C(m+1,2)(1+s)^(m-1). Rotation shifts the unique anchor, so cell stabilizer is trivial. Alternating sum zero for m>=2 implies noncontractibility of finite nonempty CW complex; m=1 is three vertices. Independently enumerated all ordered nonempty A,B,C satisfying actual arc constraints for target orders 3,5,7,9, reproducing e.g. R9 f=(90,270,270,90), not used to infer general m.

## originality

PASS

Best-of-knowledge universal exact all-dimensional cell polynomial for cyclic *nontransitive* target tournaments. Dochtermann–Singh defines directed Hom and proves transitive-target properties, not this all cyclic target f-polynomial. The closest complete Resultary R9 result gives precisely the m=4 vector (90,270,270,90) and even S1 homotopy for that *one* finite target, but expressly disclaims any all-order formula. The m=4 values are prior-covered numerical facts and are not counted as newly discovered. Directed flag/homology tournament results concern different constructions.

## value

PASS

An explicit binomial cell vector in every dimension for a canonical infinite family of directed Hom complexes provides useful exact invariants, dimension and Euler-zero/noncontractibility results, plus free cyclic cell-orbit census. The known finite R9 computation does not imply these symbolic formulas. The dimension is relevant to the oriented-triangle equivariant obstruction setting, so this is motivated all-order structural enumeration rather than table recomputation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
