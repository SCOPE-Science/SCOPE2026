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

For rim points the only competitive routes are along the rim or via the hub; the latter has length 2s plus the two nearest-rim-vertex offsets. At even order opposite midpoints simultaneously attain the two separate bounds. At odd order the midpoint triangle inequality gives d_C+δ(x)+δ(y)≤floor(n/2)+1, and one midpoint paired with a point moving from the opposite edge midpoint to its endpoint attains the three branches. A rim–spoke pair similarly has distance min(t+s+δ,s−t+r) for hub coordinate t and rim distance r from the spoke base. The bound r+δ≤ceil(n/2) is attained at a farthest edge midpoint, and balancing or clipping t gives B_n. Same-spoke distance is at most s; distinct spokes give at most min(2s,s+floor(n/2)/2) by the hub/rim alternatives. Maximizing each normalized branch gives the unique even and odd optima claimed, since in each n≥4 case B_n has strictly smaller normalized maximum than A_n; direct substitution gives D_3(s)=1+s for all s>0. The independent exact-rational edge-pair envelope checker found agreement in 75 parameter cases at n=3,…,11, including breakpoints and their neighborhoods, and recovered the normalized optima at the claimed s. No frozen script was run.

## originality

PASS

The available comparisons cover general all-edge-point diameter methods, nearby extremal problems and different invariants of wheels, but did not establish this parity-sensitive law or its normalized equality cases for the fixed symmetric family. The result passes on the distinct formulas, not on the general diameter notion or finite-candidate method. The most plausible older source is only partly accessible; that remains a historical risk.

## value

PASS

The wheel is a canonical two-route network and its vertex diameter misses the edge-interior bottlenecks. The result resolves the full parameter range, including the extra odd-order rim constraint, the takeover by a rim–spoke pair at large s, and the sharp and differently attained efficiency of worst distance per total length. The explicit witnesses and equality cases make this useful as an exact comparison family for metric-graph diameter; it is not merely a computed value at one length.

The dated certificate retains the supplied scientific assessment, sources and limitations.
