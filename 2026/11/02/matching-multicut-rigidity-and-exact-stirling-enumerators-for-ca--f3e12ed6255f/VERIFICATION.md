---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

For a nontrivial Cartesian product of connected simple factors, a crossing edge in one coordinate uses the unique external-neighbor budget at both endpoints; every perpendicular edge becomes monochromatic, forcing parallel crossing through each square. Propagation across connected factors makes every fiber in other coordinates monochromatic and yields a unique active coordinate. A factor crossing edge lifts to N_i edges, so F_product(u,v)=sum_i F_factor_i(u,v^{N_i}). For P_n each matching of t crossing edges has binom(n-t,t) locations and yields t+1 consecutive constant runs; proper unordered k-partitions of the run path are Stirling S(t,k-1). For C_n cyclic matching locations are n/(n-t)*binom(n-t,t) and the proper run-cycle color partitions give the inclusion-exclusion chromatic polynomial q_t(k). Independent separate enumeration of restricted-growth partitions of P2..P7, C3..C7, and products P2 square P3, P3 square P3, C3 square P2 matched complete (k,t) distributions. Explicitly t>=2 for cycles and C3 has zero multicuts. Packaged check_matching_multicuts.py source inspected; finite cases do not establish arbitrary factors.

## originality

PASS

The substantive claimed result was compared at the level of mathematical objects, exact implications and limitations against same-family primary results, general theorems and Resultary; accepted as best-of-knowledge, with identified prior components and explicit residual risks, not an assertion of exhaustive historical priority.

## value

PASS

The unique-active-coordinate rigidity is an all-connected-factor structural theorem, and complete two-parameter enumerators for path/cycle Cartesian grids are natural exact counting information relevant to cut configurations and reconfiguration. Disconnected partition blocks make this more than trivial connected-component cutting, while preserving a sharp matching external-degree constraint.

The dated certificate retains the supplied scientific assessment, sources and limitations.
