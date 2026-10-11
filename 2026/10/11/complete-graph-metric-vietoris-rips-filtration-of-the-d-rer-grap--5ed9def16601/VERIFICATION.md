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

`verify.py` reconstructs the Dürer graph from the edge formula, performs breadth-first all-pairs shortest-path computation, and verifies graph diameter \(4\). It then enumerates all \(2^{12}-1\) nonempty vertex subsets and retains those of diameter at most each threshold.

At threshold \(1\), the verifier obtains face vector \((12,18,2)\), checks all \(42\) Hasse covers, verifies \(13\) matching pairs, proves the oriented Hasse graph acyclic, and leaves one critical \(0\)-cell and five critical \(1\)-cells.

At threshold \(2\), it obtains face vector \((12,48,82,60,18,2)\), checks all \(684\) Hasse covers, verifies \(110\) matching pairs, proves acyclicity, and leaves one critical \(0\)-cell and one critical \(2\)-cell.

At threshold \(3\), it obtains face vector \((12,63,190,363,456,377,198,60,8)\), checks all \(8628\) Hasse covers, verifies \(863\) matching pairs, proves acyclicity, and leaves one critical \(0\)-cell only.

Euler characteristics from full face counts and from critical cells agree at every checked threshold. Threshold \(0\) has exactly \(12\) singleton faces, and threshold \(4\) is the full nonempty simplex. No claim is made about a family beyond this graph.
