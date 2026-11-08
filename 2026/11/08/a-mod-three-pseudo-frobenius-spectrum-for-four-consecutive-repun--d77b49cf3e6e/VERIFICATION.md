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

Run `python3 verify_repunit_truncation.py` with any standard Python 3 installation. The program uses only `heapq` and exact integers. It constructs minimum Apéry representatives by independent Dijkstra shortest paths on the residue graph and verifies membership for every pseudo-Frobenius candidate. It separately checks the greedy representatives and the predicted boundary formulas. Actual output is recorded in `verify_repunit_truncation_output.txt`.

The checked domain contains 330 generic cases with \(a=(b^2+b+1)Q+r\), \(2\le b\le12\), \(1\le Q\le10\), \(r\in\{0,1,b+1\}\), subject to \(a\le13000\), and 31 true four-term repunit cases with \(n\ge5\) and \(a\le40000\). There are no randomized tests, approximations, floating point calculations, or external data dependencies.

For the universal statement, the proof relies instead on: (1) greedy minimal coin counts proved by exact exchanges; (2) increasing Apéry representatives; (3) the one-step maximality criterion including its no-wrap inequality; (4) an exhaustive symbolic analysis of all indices in the terminal slab. These four items have been reconstructed and checked for their stated quantifiers and boundary cases. Finite tests are not an infinite certificate, and no independent audit has been carried out.
