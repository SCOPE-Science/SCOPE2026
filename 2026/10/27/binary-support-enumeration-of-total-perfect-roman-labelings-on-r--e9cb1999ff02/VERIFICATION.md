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

The standalone verifier `verify.py` uses the original adjacency relation and literal definition of a total perfect Roman function to enumerate all \(3^{pq}\) functions on the boards \((2,2),(2,3),(2,4),(2,5),(3,3),(3,4)\). It compares every coefficient with a separate enumerator that loops over binary defender supports and uses the proved support classification. The resulting sample contains \(617544\) ternary assignments. Further support enumerations include \(2^{16}\) and \(2^{20}\) masks on \((4,4)\) and \((4,5)\). The test also compares minimum weight and minimum-function counts for every board in its sample. Results are recorded verbatim in `verification_output.txt`.

Run `python verify.py` in a directory containing the two files. No external packages or data are required.

Limitations: these tests do not establish an infinite theorem, and the binary-support checks for larger boards are not independent of the binary-support formula. The exhaustive original-definition checks are restricted to the six named boards. The theorem is supported by its general proof separately.
