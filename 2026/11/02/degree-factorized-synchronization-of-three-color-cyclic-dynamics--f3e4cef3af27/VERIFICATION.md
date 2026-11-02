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

The exact statement is proved in `RESULT.md`. The computations provide finite cross-checks only.

- `python3 verify/spot_checks.py` (Python 3 standard library): produces `PASS standalone_python labelled_graphs=383 states=65775 n_le_5` by enumerating all connected labelled trees and unicyclic simple graphs on 2–5 vertices and all labelled three-color initial configurations. Its own direct synchronous update, rather than the winding criterion, decides convergence.
- `c++ -std=c++17 -O2 verify/labelled_graphs.cpp -o /tmp/line_cycle_check && /tmp/line_cycle_check` (C++17): produces `PASS labelled_graphs=5339 unicyclic_graphs=3898 initial_states=3048843 n_le_6` for all such connected labelled graphs on 2–6 vertices. It enumerates all initial configurations and updates directly.
- The attached output files are `verify/spot_checks_output.txt` and `verify/labelled_graphs_output.txt`. A separate unlabelled-graph-atlas exploration of 78 tree/unicyclic graphs through seven vertices checked 92,838 initial configurations, but that extra calculation is not part of the standalone verification package and is not needed for the proof.

Each program computes the same declared formula and compares it to independently simulated trajectories. The limit on simulation steps exceeds the graph diameter, which suffices for a zero-winding initial state under the cited theorem. Non-synchronizing states may be periodic and need not be assigned an orbit type by these tests. No infinite-case result is inferred from the finite enumeration. These checks were executed against the actual packaged source paths and reported output captured verbatim.
