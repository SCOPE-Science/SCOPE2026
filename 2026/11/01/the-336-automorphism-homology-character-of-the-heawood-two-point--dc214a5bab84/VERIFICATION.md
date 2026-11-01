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
# Reproducible finite verification

Execute `python heawood_verify.py` with `heawood_cycles.json` in the same directory. No external Python packages are needed. The expected record is `heawood_verify_output.txt`; the program prints `HEAWOOD_VERIFY_OK` on completion.

The verifier constructs the fourteen point/line graph vertices by testing the dot product over \(\mathbb F_2\); it enumerates all twenty-one graph edges and the complete unordered two-point cubical chain complex, with cells in the exact reproducible lexicographic order stated in the source. It checks every signed two-boundary against the signed one-boundary. The 14 integral top cycles in the JSON certificate are **all** checked for zero boundary and have rank 14 modulo three. The two-boundary has rank 154 modulo three; therefore its exact rational rank is 154, by the matching upper bound from independent cycles. The one-boundary has rational rank 90. The top integral homology is free of rank 14 because there are no three-dimensional cells. Extra finite-field rank modulo two is reported only as a consistency test for the known torsion phenomenon, not as a substitute for an integer Smith decomposition.

The verifier checks that eight graph fundamental cycles have length at most seven in a depth-three breadth-first spanning tree. Thus they admit a stationary second particle and map onto a basis of graph first homology. Dimension equality makes this a rational representation isomorphism. Finally, all 168 invertible three-by-three binary matrices and 168 incidence dualities are enumerated, their action on each cubical cell and edge orientation is checked, and the exact Lefschetz character is evaluated and counted at all 336 symmetries. The eight class sizes, orders, traces, zero invariant average and character inner product two are checked.

These checks certify finite combinatorics and the exact claimed calculations; they do not claim external or independent validation. The published graph-braid rank formula is used only for context, not to generate the newly calculated group-character table.
