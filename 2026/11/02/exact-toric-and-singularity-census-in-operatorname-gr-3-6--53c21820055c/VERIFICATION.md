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

# Reproduction instructions

Run `python3 verify.py` with the two bundled dependency files `compute.py` and `independent.py` in the same directory. No third-party Python packages, downloads, or external data are required. The program runs exact binary arithmetic, integers, and set operations and prints `VERIFY_OK` only when all assertions succeed.

The primary route enumerates decorated permutations, applies cyclic Gale-order tests, tests binary representability using a uniquely normalized candidate matrix, detects all \(U_{2,4}\) minors, and derives dimension and smoothness from basis exchanges. The second route enumerates all \(1395\) reduced-row-echelon binary three-planes, tests whether their supports are positroids, and separately derives the geometric classifications. The final program checks exact equality of *every* resulting support and its associated dimension/smoothness pair, as well as the eight count cells. Expected output includes \(883\) total labeled positroids, \(703\) toric, \(391\) smooth toric, and \(312\) singular toric.

The geometric interpretation relies on established cited theorems about positroids, regular matroids, toricity, tangent spaces and moment-polytopal dimension. The code does not prove these external theorems, does not establish counts in other Grassmannians, and does not constitute independent mathematical validation.
