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

# Reproducibility and verification

Compile the included self-contained source file with `g++ -std=c++17 -O2 -Wall -Wextra -pedantic verify.cpp -o verify`, then run `./verify`.

The checker builds the graph \(P_3\square P_n\) directly from its coordinates. For \(2\le n\le9\), it enumerates subsets by cardinality up to \(n+2\), tests closed-neighborhood domination and tests whether every connected component of the selected induced subgraph contains at least one cycle. The latter is detected by the connected-component edge-versus-vertex inequality, not by importing the analytic column-run proof. It independently verifies the explicit middle-row-plus-two upper-bound witness.

For \(n=2,3\), it additionally enumerates *all directed orientations* and tests the directed definition: every vertex has positive indegree, and each vertex receives an arc from a member of the proposed total dominating set. The minimum over valid orientations equals the independently obtained undirected-criterion minimum. These cross-checks validate the orientation criterion in small orders without using its constructive proof.

Expected output is the nine lines `width n minimum n+2 checked` for widths two through nine, followed by `VERIFY_OK`. Actual output obtained from the embedded source before packaging was `VERIFY_OK` with each of the nine expected minima. All code uses only the C++17 standard library and compiler builtins for 64-bit bit counts. Tests are exhaustive only for the stated finite orders; the unrestricted proof is in RESULT.md. No external or independent mathematical audit has been performed.
