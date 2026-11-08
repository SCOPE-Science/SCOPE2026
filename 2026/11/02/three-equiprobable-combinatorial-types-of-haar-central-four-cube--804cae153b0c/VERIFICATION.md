---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-05.md",
      "INDEPENDENT_AUDIT_2026-11-05.json"
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

PASS: A generic central section vertex corresponds one-to-one to a crossed 4-cube edge, with crossing criterion abs(sum remaining signed coordinates)<u_i. After sorting four positive normal coordinates a<b<c<d, the two possible signed-sum changes X=d-a-b-c and Y=d+a-b-c partition the parameter cone into three types with facet inventories 4^6, 3^2 5^6, 4^6 6^2. Independently re-enumerated exact cube-edge crossings at (1,2,3,7),(1,2,3,5),(6,8,10,11), giving 8,12,12 vertices and the stated facets. A prescribed edge has crossing probability P(|N(0,1)|>sqrt3 |N(0,1)|)=1/3, so expected count 32/3 and dominant type probability 1/3. Reflection T(u)=u-(Y/2)(1,-1,-1,1) is orthogonal, involutive, and preserves the ordered non-dominant cone while swapping the remaining two types; Gaussian radial density is invariant, forcing their conditional 1:1 split. Boundary hyperplanes have Haar probability zero. Exact geometry, not simulation, proves the masses.

## originality

PASS

PASS: Best-of-knowledge supported by direct statement/implication comparisons, not claimed absolute priority. The exact 1/3 conditional split refines, rather than repeats, classifications and the coarser face-vector distribution. Expectation plus support {3 types} is insufficient for all three probabilities because two share vertex count 12; the orthogonal involution supplies a distinct extra equation. Neither result implies equality of the two nondominant chamber masses. The explicit measure-preserving cone reflection supplies the missing implication.

## value

PASS

PASS: Equal Haar probabilities for three different natural face-incidence types refine an already known two-valued face-vector law. The explicit cone reflection is a structural explanation, and the conditional split provides an exact distribution for a canonical random polytope, not a mere recount of a known type list.

The dated certificate retains the supplied scientific assessment, sources and limitations.
