---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification
The analytic proof reduces play on each bipartition shore to color capacities. For a shore of size \(s\), each color may be used at most \(\lfloor s/2\rfloor\) times. A nonfull dead state can occur exactly when every color is saturated before \(s\) vertices are colored, equivalently when \(k\lfloor s/2\rfloor<s\).

The bundled `verify.py` independently enumerates every reachable occupancy vector for shore sizes \(2\) through \(12\) and palette sizes \(1\) through \(5\), tests the dead-state criterion directly, and checks the resulting game-number formula for all \(2\le m,n\le100\).

Replay output:

`ALL CHECKS PASSED; shore_cases=55; reachable_state_checks=19450; pair_cases=9801; shore_range=2..12; palette_range=1..5; parameter_range=2<=m,n<=100`

The enumeration is a finite stress test. The unbounded parameter ranges are justified by the analytic capacity argument, not by computation. No claim is made for graphs with a shore of size \(1\) or for arbitrary bipartite graphs.
