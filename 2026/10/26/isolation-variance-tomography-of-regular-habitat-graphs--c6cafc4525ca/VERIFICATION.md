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

A retained isolated indicator has mean pq^r. For adjacent endpoints the joint event is impossible, while nonadjacent endpoints with s common neighbors impose absence on a union of 2r−s sites disjoint from the endpoints. Summing diagonal, nr/2 adjacent and nonadjacent pair terms produces the stated factors, with codegree zero canceling. The normalized variance residual divides by 2p³q^r, nonzero at every permitted sample, and the geometric series gives triangular coefficients b_j=∑_{s≥r−j}N_s. Adjacent coefficient differences and exact interpolation at r distinct points prove inversion, including r=1 and the complete graph. The wedge count partitions into ∑sN_s open and 3T closed wedges. At cubic order the variance coefficient before substitution is n binom(r,2)+2nr(r+1)+2∑sN_s, which simplifies as claimed. The two cycle examples have ten distance-two pairs of codegree one and none of codegree two; disconnectedness is permitted. The uploaded certificate and checker were inspected, not executed. A separate exact retained-set enumeration and three-point interpolation for K3,3 and the triangular prism gave triangle counts 0 and 2 and the expected distinct normalized curves (python /workspace/review-evidence/independent_checks.py). The independent check is finite and numerical stability is not asserted.

## originality

PASS

The supported distinct claim is the exact equivalence between the scalar site-isolation variance curve and the nonedge-codegree histogram for known regular parameters, with uniform exact sample sufficiency and derived triangle census. Pair probabilities and interpolation are not claimed as new techniques. No earlier exact recovery or stronger same-observable inversion was established by the inspected sources.

## value

PASS

This identifies exactly which overlap invariant is retained by an accessible idealized aggregate, turns it into a finite exact reconstruction, and distinguishes triangle identifiability from graph or connectivity identifiability. The interpretation is mathematical, not a claim of robust ecological inference from noisy observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
