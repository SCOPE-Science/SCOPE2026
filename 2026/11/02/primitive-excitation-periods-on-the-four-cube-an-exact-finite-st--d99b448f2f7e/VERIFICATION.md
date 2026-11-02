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

# Finite-state verification

The four included standalone C++17 programs all compile without third-party dependencies. Compile and run each on dimensions \(1\) through \(4\). `census.cpp` uses bit masks and a one-outdegree graph traversal; `independent.cpp` performs direct trit-level updates and independently traverses the graph; `basins.cpp` performs a further direct-step classification of entry times and limiting periods; `circulation.cpp` does **not** simulate trajectories but checks all square-face edge circulations, an independent method for counting the extinction basin based on the published arbitrary-graph theorem. These are complete finite enumerations for each dimension, not probabilistic tests.

The exact expected count rows, including the independent implementation, are in `data/observed_counts.txt`, with full captured executable output in `data/reproduction_output.txt`, and the complete first-entry table is in `data/entry_profile.txt`. The explicit ten-cycle trace is `data/period10_witness.txt`. Total states for the largest run are \(3^{16}=43046721\); the represented states are indexed consecutively from zero through \(43046720\). Full exploration identifies exactly one fixed point, \(292616\) period-three cycles, \(13190\) period-four cycles, and \(1344\) period-ten cycles. The sum of all Q4 basin counts equals \(43046721\). The square test finds exactly \(592641\) extinction states, which matches the trajectory-classification extinction basin.

The code and observed counts are attached for independent reproduction; no external assessor has reviewed these programs. The proof relies on complete enumeration only for \(d\le4\). No general assertion for larger \(d\) follows from the code.
