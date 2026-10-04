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
# Verification

`verify.py` is a standalone standard-library verifier for the finite six-state claim. It rebuilds the published five transition maps and performs two exact calculations.

The first uses bit-mask subsets. Breadth-first search reaches all \(63\) nonempty subsets and proves that the first singleton distance is \(20\). For each letter \(x\), exact polynomial dynamic programming on the distance-tight shortest-path DAG computes \(P_x(z)\), the number of shortest words at every \(x\)-count.

The second uses `frozenset` subsets and separate first-arrival layers, without the bit-mask distance table. It independently propagates integer histograms until the first singleton layer. It reproduces every coefficient and confirms that all shortest mass ends at state \(3\).

Finally, the verifier expands the four displayed factor forms by its own integer polynomial multiplication and compares those coefficients exactly with both computations. It checks the total \(452{,}984{,}832\) for every marginal and checks that the \(b\)-marginal is constant, which is equivalent to universal absence of \(b\) from shortest reset words.

The proof is exhaustive for this finite power automaton. It does not infer an infinite-family formula. A successful run prints `VERIFY_OK length=20 total=452984832 target=3 reachable_subsets=63`.
