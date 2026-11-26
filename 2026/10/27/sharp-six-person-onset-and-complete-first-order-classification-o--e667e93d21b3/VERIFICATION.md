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

An unserved nonbuyer can profitably buy, and a buyer nominated by another buyer can drop its purchase and save the cost. These are exactly the profitable deviations once quotas are fixed, because choosing nominations does not affect the buyer's own access. Thus equilibrium buyer sets are precisely the feasible exact-quota cut covers. Independent replay used lower-bounded circulation: exact inflow at each buyer, unit arcs to eligible nonbuyers, and required inflow at least one per nonbuyer; integral feasible flows correspond to legal nomination sets. The replay covered all labeled connected graphs of orders 2–6 (1, 4, 38, 728, 26704) and every capacity 1 through n−1; larger capacities are identical to n−1. It found no reversal below six and exactly 1330 at six, each with only m2=2<m3=3. Minimizing each mask over all 720 relabelings gave code:count 121:90, 693:360, 127:180, 954:180, 639:60, 703:360, 1759:90, 4060:10. Only 121 has five edges (01,04,05,12,13), the double-star. The independent replay was written separately from the frozen nomination-union checker. The frozen checker's Python 3.9 compatibility note should say 3.10+ because it uses int.bit_count(); this is not a census defect.

## originality

PASS

Credit only the first possible order, exhaustive eight-class boundary, multiplicities and unique sparsest class. The game, DP-Nash characterization, double-star reversal, and the K3,3 reversal are already given or implied by the inspected sources. Those sources do not settle the full boundary.

## value

PASS

The first possible size is a natural question forced by a known sharing-capacity paradox, not an arbitrary graph-size slice. The full boundary makes the phenomenon independently usable: it separates one sparse tree obstruction from seven cyclic types, identifies the only increasing capacity step, and lets later work test proposed structural explanations against the full onset layer rather than just one example. The value is not the already-known example or a general welfare claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.
