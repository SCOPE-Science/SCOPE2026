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

# Reproducible mathematical verification

Execute `python3 verify_prism.py` with Python 3 and no external packages. The script generates the complete graph-edge matching complex for each integer \(3\le n\le10\), rather than loading a precomputed incidence list. All face masks and dimensions are rebuilt on each execution. The complete directed Hasse graphs after reversal of matched edges are topologically sorted; any directed cycle triggers an assertion.

The signed Morse boundary is calculated over integers using an acyclic, cached gradient-flow recursion with standard simplicial incidence signs. The two nonzero Morse boundary ranks are \(1\) at \(n=8\) and \(2\) at \(n=9\); the exact integer pivots are units, with the residual matrices checked to vanish. The values \(n=3\) through \(n=10\) have respectively \(32,108,342,1104,3544,11396,36626,117732\) total faces including the empty face. Their full directed face-incidence counts are \(48,252,1020,4002,15022,55272,199890,714010\).

As a separate test of the original simplicial complex, exact mod-two boundary eliminations directly recompute its reduced Betti ranks for all eight inputs, agreeing with the integral Morse classifications. Euler characteristics and complete critical-cell counts are also independently asserted against the homotopy table.

These checks are finite and exhaustive for each stated graph. They do **not** prove a conjecture for all circular ladders or provide an independent human or external audit. The research uses the integral cellular boundary and elementary homotopy cancellations; mod-two ranks alone would not establish integral homotopy.
