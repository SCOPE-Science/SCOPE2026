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

# Reproduction and limits

Run `python3 verify.py` from the directory containing this file and the standalone `verify.py`; Python 3.8 or newer is sufficient, with no nonstandard packages or downloads. All graph and threshold comparisons use arbitrary-size integers and rational breakpoints, not floating-point approximations. The script enumerates every labeled simple undirected graph up to five vertices, filters for connected graphs, enumerates every proper nonempty seed set and allowed one-edge rewiring, and checks every critical threshold and open-threshold cell representative.

Expected totals: 771 connected labeled graphs across orders two through five; 288,834 (graph, seeds, threshold) combinations; 213,990 admissible rewiring comparisons for baselines not already at full adoption. The program separately verifies the six-vertex tree, the unchanged seed set, both trees' connectedness and edge count, and the three-versus-six final adoption counts at threshold one third.

For every graph of order at most five, a threshold rule comparing integer neighbor counts against a fixed real fraction can change only at one of finitely many rationals \(k/d\) with \(1\leq d\leq4\). The program evaluates all such breakpoints and representatives between them. Therefore the verified finite enumeration establishes the universal real-threshold lower-order assertion, provided the explicitly stated model and enumeration algorithm are followed. The all-large-orders extension is proved algebraically by adjoining leaves to a permanent seed; finite tests are not used to extrapolate that statement.

No claim is made here about unconditional expectations under ongoing stochastic rewiring, heterogeneous thresholds, or noisy individual choices. Independent audit has not been performed.
