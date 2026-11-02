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

# Reproduction and proof-boundary checks

Use Python 3.9 or later, and a C++17 compiler. No additional Python dependencies are required.

From the directory containing the packaged files, run `python3 verify_symbolic.py` and compare its output with `symbolic_results.txt`. The script enumerates every one of the 676 capped initial-color signature pairs, detects the true full-representative recurrence, checks the complete first-entry/least-period histogram and proves exact formal polynomial equality in four independent indeterminates using integer-coefficient polynomial arithmetic. It also verifies the all-parameter formulas at 121 illustrative size pairs. The formal identity, rather than those 121 instances, establishes validity for every integer shore size.

Compile the independent labelled-state implementation with `g++ -O2 -std=c++17 -Wall -Wextra -pedantic verify_direct.cpp -o verify_direct`, then run `./verify_direct` and compare with `direct_results.txt`. That implementation updates every labelled vertex using opposing-shore neighbor counts and exhaustively evolves all 1,185,921 labelled configurations for the 25 graphs \(K_{a,b}\) with \(2\le a,b\le6\). It compares entry bounds, all three eventual-period counts, and two individual period-four entry layers.

The finite-representative reduction is exact because vertices sharing an initial color within one shore have identical neighbor sets, remain synchronized, and never split. Replacing each cohort size by its truncation at two preserves every threshold-two decision indefinitely. This is the critical size-independent lemma. The formal polynomial identities produced from all 676 representatives and the exponential generating-function substitutions supply the infinite family proof. An exhaustive calculation for finitely many labelled graphs alone would not establish the theorem.

Limitations: the code does not establish historical uniqueness or publication priority; no independent audit has been performed. The rule assumes three colors, synchronous updating, and threshold two on complete bipartite graphs of part sizes at least two. No larger class of graphs or threshold rules is certified.
