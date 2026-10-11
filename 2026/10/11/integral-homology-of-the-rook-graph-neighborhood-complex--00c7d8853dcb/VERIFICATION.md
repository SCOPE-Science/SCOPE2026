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

`verify.py` uses only the Python standard library.

It reconstructs the \(16\)-vertex graph \(H(2,4)\) from coordinates, verifies degree \(6\) and common-neighbor count \(2\) for every distinct pair, and generates the neighborhood complex exactly. The expected nonempty face vector is
\[
(16,120,320,240,96,16).
\]

The script regenerates the stagewise discrete-Morse matching from the archived vertex order. It checks every matching pair is a face-poset cover, orients every one of the \(2736\) nonempty Hasse covers in Forman orientation, and proves acyclicity by a complete topological sort. The critical-cell counts are
\[
(1,1,56).
\]

For integral \(H_1\), the script rebuilds the \(105\times320\) triangle-boundary relation matrix in a fundamental-cycle basis of the complete \(1\)-skeleton. It checks ranks \(104,105,105\) modulo \(2,3,5\), respectively. It then evaluates an explicit \(104\times104\) minor with determinant \(1\) and an explicit \(105\times105\) minor with determinant \(-2\) using fraction-free Bareiss elimination. Since the mod-\(2\) rank is \(104\), every full minor is even. These facts force Smith factors \(1\) repeated \(104\) times and \(2\) once.

The finite computations prove only the finite graph claim stated in the result. They are not extrapolated to larger Hamming graphs or general line graphs.
