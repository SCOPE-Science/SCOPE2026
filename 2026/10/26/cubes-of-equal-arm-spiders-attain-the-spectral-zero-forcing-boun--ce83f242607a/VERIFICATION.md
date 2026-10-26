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

The attached `verify.py` uses only the Python standard library. Execute `python3 verify.py` in the directory containing it. The included `verify_output.txt` records a successful run with 40 upper-seed checks, 40 cubic-support and eigenspace checks, and eight exhaustive smaller-start-set cases. The computation is finite and only corroborates the unrestricted proof in `RESULT.md`.

The proof's noncomputational checks are: the three distinct eigenvalues \(2\cos(j\pi/(\ell+1))\), for \(1\le j\le3\), of the arm-path adjacency matrix; each produces an \((m-1)\)-dimensional eigenfamily of the whole tree; and the polynomial \(\prod_{j=1}^{3}(A-\lambda_j I)\) has nonzero off-diagonal entries at every graph distance one, two, or three and zeros at larger distances. The case \(\ell=4\) is handled separately to ensure that no distance-one cancellation occurs. The explicit forced-vertex order in the proof supplies the upper bound.

Independent audit and independent mathematical validation have not been performed. Searches can miss unindexed or inaccessible prior art; the scientific result should not be treated as independently certified.
