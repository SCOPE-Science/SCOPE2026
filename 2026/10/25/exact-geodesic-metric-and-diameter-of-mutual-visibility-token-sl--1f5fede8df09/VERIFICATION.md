---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For all m,n>=3 and connected layers k<=m+n-3 (also k=m+n-2 when min(m,n)=3), visibility condition is (a<=1 or b<n) and (b<=1 or a<m). Feasible A-population levels form an interval. Every slide alters one selected status per side, giving max of the two partwise symmetric differences as lower bound. Correct cross-part wrong tokens directly while staying in interval, then relay each residual same-part swap in two slides via adjacent feasible level; attains bound. Sharp diameter for k<=N-3 is min(2k,2(N-k-1),max(m,n)); connected top layer has diameter 3. If m,n>=4 top layer has mn isolated configurations. Independent all-pairs BFS on K3,3 K3,4 K4,4 corroborated all layers and boundary.

## originality

PASS

Original Fresán-Figueroa–Goldfeder–Lozano-Piña 2026 paper gives feasibility, connectivity and a loose upper bound, not exact all-pairs geodesics or sharp diameter. For disjoint balanced size-4 sets in K4,4 its bound is 8 versus exact distance 4. Unrestricted token graph results omit visibility restrictions.

## value

PASS

Mutual visibility token-slide layers are a recently introduced natural reconfiguration graph class. The exact isometric embedding into the ordinary token graph and all-pairs distance reduce optimization to a closed expression; sharp diameters and disconnected top boundary give a full natural layer classification rather than a routine restatement of connectivity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
