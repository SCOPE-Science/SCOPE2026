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

Run `python3 verify.py` in the directory containing the extracted package. The script uses Python's standard library only and has no downloads, dependencies, or external state.

The first verifier independently constructs an Euler tour from the undirected multigraph, expands traversals, and checks every required palindrome, exact cyclic length, and the complete unordered-adjacency multiplicity profile for \(2\le q\le30\). The second verifier performs a separate breadth-first state search over all possible cyclic words modulo rotation through compulsory `000`, checking all masks of achieved palindrome triples and the two wraparound windows. The minimum values are \(8\) at \(q=2\), \(15\) at \(q=3\), and \(28\) at \(q=4\).

Successful execution reports `VERIFY_OK alphabet_sizes=2..30 required_triplets=9454 complete_constructive_covers=True brute_force_q=2..4` along with three exact BFS results. The search is finite corroboration, not an all-alphabet proof. The infinite argument is the lower bound by pair-label runs and parity followed by matching-augmented Eulerian construction. Scientific literature overlap is evaluated separately and is not certified by code.
