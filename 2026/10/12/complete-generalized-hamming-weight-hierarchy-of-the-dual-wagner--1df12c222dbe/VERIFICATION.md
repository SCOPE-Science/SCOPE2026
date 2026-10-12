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

The file `verify.cpp` is a standalone exact checker. It embeds the 14-by-23 binary generator matrix from the public CodeTables Wagner-code entry. For each nonempty coordinate subset it computes the column rank over \(\mathbb F_2\), then applies
\[
\dim D(X)=|X|-\operatorname{rank}_2(G_X).
\]
It examines all \(2^{23}-1\) nonempty subsets and checks the expected minima for every \(r=1,\ldots,9\).

Replay from the package directory with a standard C++17 compiler:

`g++ -O3 -std=c++17 verify.cpp -o verify && ./verify`

The run used for this package is preserved in `verification_output.txt` and ends with `VERIFY_OK`. The computation uses only integer bit operations and exact XOR elimination. It does not use randomness, floating point, heuristic pruning, timeout conclusions, or an external certification service.

The certificate proves only the hierarchy of the displayed code. Equivalence of linear codes preserves generalized Hamming weights; Simonis's uniqueness theorem is used only to identify this hierarchy with the Wagner equivalence class.
