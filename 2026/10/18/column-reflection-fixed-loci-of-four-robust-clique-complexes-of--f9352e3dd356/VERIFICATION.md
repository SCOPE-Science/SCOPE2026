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
# Verification of column-reflection fixed loci

Run `python3 verify_fixed.py` using Python 3 without external packages. The checker independently constructs the graph and reflection orbits and enumerates orbit subsets containing at most six original graph vertices. It tests whether every four-vertex subset has a graph edge; this is exactly the definition of the four-robust clique complex. For even widths it compares every orbit-complex simplex with the folded combinatorial model specified in the proof. For odd widths it checks that adjoining the central middle-row singleton preserves every face. It also builds all boundary matrices over \(\mathbb F_2\), performs exact pivot elimination, and compares the reduced Betti numbers for every integer \(3\le n\le40\).

The recorded stdout is in `verification_output.txt`. Finite computations verify the combinatorial model on those widths and detect errors; they neither establish the theorem for arbitrarily large grids nor replace the written all-width matching and collapse argument. No independent scientific audit has been performed.
