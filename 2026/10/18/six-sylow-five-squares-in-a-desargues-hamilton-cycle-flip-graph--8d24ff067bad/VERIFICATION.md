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

# Verification instructions

Execute `python3 verify_subsets.py` and `python3 verify_cycles.py` in the same directory as these files. Both use only the Python standard library. Their standard outputs are captured in `verify_subsets.txt` and `verify_cycles.txt`, respectively. The final line `VERIFY_OK` is reached only if all exhaustive assertions pass.

The first program enumerates all perfect matchings by branching on every partner of the first free vertex, verifies complementary two-factors, enumerates every pair of Hamilton-complement matchings, and checks the graph distance spectrum, intrinsic triangle-free flip edges, cross-component matchings, transitive \(S_5\) action, Sylow-five fibre identity and equivariant neighbour rule. The second program independently enumerates Hamilton tours by depth-first search in \(GP(10,3)\), fixes starting point and orientation, then constructs and checks all alternating-cycle difference types and resulting transition graphs.

These are exhaustive finite computations on a graph with twenty vertices, not a probabilistic sample, a computational timeout certificate or a claim about infinite families. For a human-checkable proof of the equivalence between the finite loops and the mathematical result, see `RESULT.md`, particularly the matching-complement bijection, exhaustive branch partition, symmetric-difference degree/tour test, and the finite \(S_5\)-action argument.

Independent audit status: not performed.
