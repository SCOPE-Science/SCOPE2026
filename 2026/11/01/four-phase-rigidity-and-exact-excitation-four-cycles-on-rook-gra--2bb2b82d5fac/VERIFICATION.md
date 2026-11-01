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

# Reproducibility and limits

Compile the embedded `check_four_cycles.cpp` with a C++17 compiler, for example:

`g++ -O3 -std=c++17 check_four_cycles.cpp -o check_four_cycles`

Run `./check_four_cycles` and compare the result with `check_four_cycles_output.txt`. The program computes the synchronous three-state excitation transition from the explicit row-and-column adjacency masks. For each of nine board sizes it checks every \(3^{ab}\) configuration for \(F^4(x)=x\) and \(F^2(x)\ne x\). Independently it generates all four-phase rectangle states using every nonempty proper row cut, every nonempty proper column cut, four phase offsets and two orientations. It requires equality of the two sets, not just their cardinalities, then checks the expected orbit count. The exact tested population is \(20,280,861\) labelled initial configurations.

The computational domain consists of the nine boards \((2,2),(2,3),(2,4),(2,5),(2,6),(2,7),(3,3),(3,4),(3,5)\). This computation is not exhaustive for arbitrary board dimensions; the infinite-family proof is the two-condition phase lemma and rectangle-rigidity argument in RESULT.md. No independent audit or external mathematical certification has been performed.
