---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For finite simple undirected G_{p,q,t}=K_{p,q} minus t disjoint edges, p,q>=3 and 1<=t<min(p,q), the shortest-path characterization is verified: every two same-part vertices have distance two, and their common neighbors exclude only the mates of at most two matched endpoints. Hence on each opposite side the omitted set must contain at least one unmatched vertex OR at least three vertices; conversely any such omitted sets expose an interior-free geodesic for all same-side pairs. For each deleted opposite-part pair a_i,b_i, the proof explicitly constructs a length-three geodesic through b_j in Y and a_k in X that avoids the missing middle edge; the stated side conditions guarantee the necessary nonmatched or distinct choices. The all-pairs criterion therefore factorizes by sides. The only forbidden omitted subsets in a side of order r are the matched-only subsets of sizes 0,1,2, giving F_{r,t}(z)=(1+z)^r-z^r-tz^{r-1}-C(t,2)z^{r-2}. Inclusion-maximal selections correspond to inclusion-minimal admissible omissions: one unmatched singleton or a three-matched-vertex set; the resulting product M gives layers p+q-2, p+q-4, p+q-6 when t>=3 and no lower layers for t<=2. The special (6,6,3) layers and count 3249 follow. This establishes all allowed p,q,t algebraically, independent of bounded computations. A separately written BFS shortest-geodesic-inspection checker enumerated every subset for 41 p,q<=5 parameter cases including boundary controls, plus (6,6,3),(6,7,4),(7,5,3); all exact coefficients, membership and inclusion maximality tests passed. Finite checks corroborate and are not the infinite proof.

## originality

PASS

Best-of-knowledge originality of the pair of COMPLETE bivariate enumerators and three-deletion lower-maximality transition for proper nonempty partial matching deletions from K_{p,q}. Earlier general distance-two/common-neighbor tests and basic parameter definitions are expressly prior; they imply a feasibility test after graph-specific specialization but do not supply the exact F_{p,t}(x)F_{q,t}(y), the inclusion-maximal polynomial, or the t=3 spectrum directly. Inspected primary source material and independently read nearest matching-deletion and visibility-polynomial research results did not logically cover the same claimed all-parameter census. Unindexed priority remains possible.

## value

PASS

Total mutual visibility and its lower inclusion-maximal variant are natural geodesic-avoidance parameters. Partial matching deletion is a canonical structured perturbation of K_{p,q} toward crown graphs, so the exact bipartition-weighted all-set count and maximal-set polynomial are motivated observables rather than arbitrary slices. The result determines every feasible placement by size in each part, a complete maximal-placement spectrum, and the sharp t=3 transition from equicardinal maximal sets to three size layers with a four-vertex lower-number drop while the maximum remains fixed. Those exact family-specific structural facts are not supplied by a scalar extremal parameter or by the known general common-neighbor test without specialization. The contribution is bounded to this natural family and does not claim a new graph-general criterion or an unrelated downstream theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
