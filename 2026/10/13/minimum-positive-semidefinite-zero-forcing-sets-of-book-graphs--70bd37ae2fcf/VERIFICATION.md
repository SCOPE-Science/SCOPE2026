---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Removing any single vertex leaves the book connected, and the sole blue vertex has at least two neighbors in that component; no first PSD force is possible. From both spine vertices blue, each white page is a separate edge and can be forced from an endpoint. From a same-page pair, the two blue page vertices can force the spine. From {a,x_i} use x_i→y_i→b, and from {a,y_i} first force the isolated white x_i from a, then force b from y_i. Exchanging sides covers the other spine–page pairs. From two different pages, the white spine edge remains and every residual white page fragment attaches to it; each blue page vertex has both neighbors in that one white component. Thus neither can start a force. The categories are exhaustive and disjoint, giving 1+n+4n minima after excluding both the empty set and singletons. The argument also covers n=1: the four-cycle has all six pairs as minima, and there are no different-page pairs.

## originality

PASS

Pass for the classification and 5n+1 count of all minimum PSD forcing sets, not for Z_+(B_n)=2, which follows from a prior theorem about partial 2-trees. The inspected reductions and other graph-family formulas do not give the all-pairs classification. Full-text limitations on two relevant further sources are noted separately.

## value

PASS

The classification resolves a location-sensitive question that the known minimum size cannot answer on a standard graph product: putting both vertices on different pages fails completely, whereas a spine vertex can be partnered with any other vertex. Together the cases give the leading PSD forcing-polynomial coefficient and a labeled census useful for testing structural guesses about minimum sets. This is a natural complete classification with a cone-of-pairs obstruction, not a finite recomputation of the scalar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
