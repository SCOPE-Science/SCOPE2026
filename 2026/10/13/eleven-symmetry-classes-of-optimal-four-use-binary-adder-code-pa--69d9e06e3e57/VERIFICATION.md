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
# Finite verification

Compile each C++17 source from this directory, e.g. `c++ -std=c++17 -O2 adder4.cpp -o adder4`, and likewise the two other programs. Run `./adder4`, `./adder4census`, then `./adder4orbits` from the directory containing the `adder4_root_pairs.txt` file. The census program generates the normalized-pair data, which is already provided; `adder4orbits` reads those pairs. Results: max=36, normalized ordered pairs=966, all ordered labeled pairs=2448; orbit count=11, histogram 48:1, 96:3, 192:3, 384:4. These are exhaustive finite enumerations, not infinite generalizations.

The two count methods differ materially: the upper bound is an independent-set recurrence for every normalized first codebook, whereas the census tests every cardinality-compatible second codebook directly. The independent-set recurrence and the masks have their mathematical meaning defined in `RESULT.md`. No independent external review or certification is asserted.
