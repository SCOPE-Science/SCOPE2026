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

For every finite tree T, write C_T(t)=sum_{selected S with no isolated selected vertex}t^|S|; conditioning on nonempty survival multiplies C_T(t)-1 by (1-p)^n/[1-(1-p)^n] with t=p/(1-p)>0. An independent unlabeled-tree enumeration using graph isomorphism checked all tree orders 1..8: 1,1,1,2,3,6,11,23 types and 0,0,0,0,0,1,5,23 equal-degree unordered pairs. Full exact enumeration of 2^n selected sets showed 22 of the 23 eight-tree pairs coefficientwise ordered and exactly one mixed-sign pair; for smaller n none mixed. Independently matched the labeled witness T edges {01,05,07,12,14,23,56} and H {01,04,06,12,13,45,67} with C_T-C_H=t^5-t^7. Algebra gives p^5(1-p)(1-2p)/[1-(1-p)^8] and the unique strict reversal at 1/2. Degree matching gives equal expected isolated survivor count p sum_v(1-p)^degree(v). Exhaustiveness is justified by leaf deletion and canonical tree isomorphism, and n>8 is explicitly outside the claim.

## originality

PASS

The complete minimal order/equal-degree reversal classification is not an instance of ordinary node reliability (which requires surviving vertices to induce one connected graph). Tittmann–Averbouch–Makowsky enumerate induced subgraphs by total component count; that is broader polynomial information in a different marginal, not a theorem specifying singleton-free induced subgraphs or the degree-matched risk crossings. Earlier ecological graph connectivity motivates the model, not the 29-pair exact census. Could a preexisting complete induced-subgraph table permit mechanical extraction of these finite facts? Yes; no such complete matching table was identified in inspected texts. Priority risk explicit.

## value

PASS

The property "every surviving patch has a surviving neighbor" is a natural isolation-free site-percolation event, distinct from connected-retained-set node reliability. The minimal order eight and unique same-degree pair with an exact reversal show that degree sequence and expected number of isolated survivors do not determine a reliability ordering. A complete small-tree cutoff is a mathematically motivated structural result despite finite scope; no claims of ecological calibration or all-order extremality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
