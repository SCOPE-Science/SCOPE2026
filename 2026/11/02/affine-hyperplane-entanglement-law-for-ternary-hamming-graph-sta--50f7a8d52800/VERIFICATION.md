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

# Reproduction and scope

Run `python3 artifacts/check.py` using Python 3 with NumPy installed. The script constructs all tested graph adjacencies from their definitions and checks exact binary ranks. It also constructs the full pure graph state and performs a numerical partial trace for the nine-qubit \(d=2\) case and the three-qubit \(d=1\) case. Its standard output is recorded as `artifacts/check_output.txt`.

The exhaustive affine test covers every nonzero normal and all three offsets in dimensions \(1\) through \(5\). For dimensions \(6\) and \(7\), it covers each support size with representative signed normals and all three offsets. The base hyperplane cut is tested through dimension \(8\). These are *finite* tests, while the all-dimensional proof is the finite-field calculation in the main result.

The direct partial-trace eigenspectra have respectively two eigenvalues of \(1/2\) and four eigenvalues of \(1/4\); the larger cases rely on exact rank tests plus proof, rather than constructing exponentially large complex state vectors. The code uses only NumPy and Python's standard library, and produces deterministic output. No external code downloads, inaccessible certificates, infinite enumeration or independent validation are implied.
