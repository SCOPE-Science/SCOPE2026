---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

For t nonzero finite, at a singular point with all coordinates nonzero, the square-coordinate derivatives sum to −U²: summing the derivatives kills U and the differences, and sends V to 2U. The curve equation then forces a repeated square coordinate and U=0 makes all three equal. On each coordinate axis the restriction is −(b−1)(b²+tb−1); no coordinate vertex lies on a finite member, and the multiple roots for t nonzero occur exactly at b=t with t²=−1. Both transverse quadratic coefficients there are nonzero. At each blowup centre the quadratic jet is a double tangent and the cubic restricted to it is nonzero. Completing the square in the completed local ring gives a cusp (the cubic unit can be absorbed by a square root because 2 is invertible), and the single blowup resolves it. Finite nonzero members are reduced because their singular loci are finite. Bézout excludes a component meeting its complement only at cusps; with the six nodes, splitting off a degree 2 or 3 component costs at least eight intersections, whereas a line would need five nodes but contains at most three. The plane genus formula then gives normalization genus six or zero as claimed. At zero the conic has order-two contact with each line at its own centre, which becomes transverse after blowup, and the six line intersections remain. At infinity the triple points contribute four exceptional curves, with twelve contacts with line transforms and three line-line nodes; label E_i by {i,5} and the transform through i,j by the complement of {i,j} in {1,2,3,4} to obtain Petersen disjointness. This is a classification of pencil divisors as defined, not a claim of a base-point-free morphism on S. Independent checks of the jets, factorization, axis coefficient and arrangement counts can be replayed with python3 /workspace/review-evidence/checks.py 1 (SymPy); the frozen checker was read, not executed.

## originality

PASS

The distinct contribution supported by the inspected sources is the complete classification on the specified characteristic-three reduction, including the generic cusp germs and exact singular-parameter support. Reducibility of the isolated t=0 Wiman sextic and the classical Petersen and six-node structures are not new. This is a bounded coverage judgment, not an assertion of priority.

## value

PASS

This is a natural bad-characteristic specialization of a classical family. The exact support and all geometric types after the blowup are useful when distinguishing singularities of the plane models from actual singular pencil divisors in characteristic three. The new issue is not the graph of a known endpoint: the Hessian and derivative behavior changes in this characteristic, and a complete exclusion of extra parameters and extra components is needed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
