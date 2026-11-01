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

# Reproduction and evidence

For the ordinary synchronous degree-threshold chip-firing map, run `python3 verify_counts.py` from a directory containing all packaged standalone files. It evaluates the exact binomial sum using arbitrary-size integer arithmetic, evaluates the corresponding weighted cut count by a different procedure, and verifies direct construction of period-two chip phases for small graph sizes. The exact-count checks span all admissible matching sizes for orders three through ten; representative ratio values extend to order 120. Expected output is `counts_output.txt`.

Compile the independent vertex-neighbor direct simulator with `g++ -O2 -std=c++17 verify_direct.cpp -o verify_direct` and execute `./verify_direct`. It exhaustively checks all chip configurations in the finite sufficient range for graph orders three through six, for every allowed matching size. The program prints `ALL PASSED: 2375520 bounded labelled chip vectors tested` when the 2,375,520 states agree with the mathematical enumeration. Expected output is `direct_output.txt`.

The proof of the infinite-family law additionally requires the Laplacian-kernel reduction to cut weights, exponentially concentrated weighted shore sizes, exact split-pair first and second moments, and uniform logarithmic expansion. The proofs and explicit formulas are in `RESULT.md`. The finite computations do not establish the unbounded-parameter error bound by themselves. Independent mathematical audit has not been performed.
