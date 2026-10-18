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
# Reproduction and exact-check limits

The self-contained `verify.py` uses only the Python standard library. Run `python verify.py` with Python 3. It builds the once-subdivided graph directly, takes a breadth-first-search spanning tree, assigns independent \(\pm1\) differences on its tree edges, and rejects assignments violating a single non-tree edge. This enumerates every all-edge-tight normalized integer potential without using the closed-form count.

The program compares the computed facet totals for orders two through six against the independently evaluated binomial formula, returning \(4,20,152,1984,50176\). At orders four and five it independently constructs every vertex permutation on the graph and global sign reversal, partitions the actual facet set into orbits, and verifies the predicted \(13\) and \(37\) orbits. It separately constructs all simple-graph isomorphism types and complement classes for the orbit-formula comparison. The terminal line observed was `ALL EXACT CHECKS PASSED`.

No random sampling, floating point, or heuristic optimization is used. The finite checks do not prove the general statements; the analytic proof in `RESULT.md` gives the quantified conclusion. No external or independent scientific audit has been performed.
