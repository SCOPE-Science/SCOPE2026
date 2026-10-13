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
# Computational verification and logical boundaries

Run `python3 verify.py` with Python 3.8 or later; the file uses only the standard library. It recreates the prism graph from two cycle layers and vertical spokes, computes the graph of conflicting edges from its adjacency relation, and applies exact bitset maximum-independent-set recursion. It also checks all six construction residue families for 178 orders and independently enumerates equality packings by selecting one edge from each conflicting triple.

Observed output, stored in `verification_output.txt`: 178 checked witnesses; complete conflict-table agreement for orders five through fifteen; exact optima \(2,3,4,6,6,7,8,9\) at orders three through ten; upper-bound equality census \(0,6,0,6\) for orders three, six, nine and twelve. The checker ended with `VERIFY_OK`.

The finite checks are exhaustive only for the explicitly named finite order sets. The infinite result and uniqueness at every order divisible by six rely on the cyclic conflict-table argument, the two conflicting partitions, and the residue-periodic construction in `RESULT.md`. No independent audit or expert certification is asserted.
