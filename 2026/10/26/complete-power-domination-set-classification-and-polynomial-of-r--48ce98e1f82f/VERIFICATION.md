---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For the finite rook graph K_p square K_q (2<=p<=q), the initially unobserved region is exactly I x J where I,J are unused rows and columns. If both |I|,|J|>=2, each observed neighbor has zero or at least two unobserved neighbors, preventing any force. If either |I|<=1 or |J|<=1, any remaining unobserved vertex has a forcing neighbor, so all are reached. This proves r(S)>=p-1 OR c(S)>=q-1, including p=2 and empty set. Counting failing sets by their exact occupied row/column supports gives the stated bipartite edge-cover inclusion-exclusion polynomial. Minimal size p-1 and coefficients p*q^(p-1) when p<q, or 2*p*p^(p-1)-p^2*(p-1)! when p=q, follow by overlapping row/column transversals. Maximal failing sets are full (p-2)x(q-2) rectangles, giving the sharp degree cutoff. Independent forcing simulation versus support criterion found n subsets 256 (2x4), 512 (3x3), 4096 (3x4), 65536 (4x4), with failing counts 1,10,31,317, matching all coefficients.

## originality

PASS

The published numerical minimum p-1 (Soh and Koh) is prior work. General power domination polynomial (Brimkov et al) and ordinary domination rook-graph edge-cover inclusion-exclusion (Mertens) are also prior. Their inspected content did not supply the all-subset forcing criterion, full rook-graph power-domination polynomial, minimal-set multiplicities or maximal failure rectangles. This is a concrete new result subject to possible specialized enumeration elsewhere.

## value

PASS

For a natural graph product K_p square K_q, the result classifies every feasible power dominating set and exact polynomial at all sizes, rather than merely restating minimum cardinality. Full obstruction rectangles and the sharp cutoff give useful structural information for propagation and sensor placement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
