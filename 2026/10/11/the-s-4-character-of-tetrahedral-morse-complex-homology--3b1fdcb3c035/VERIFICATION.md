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

`verify.py` uses only the Python standard library. It reconstructs the closed tetrahedron from four abstract vertices and forms all 28 primitive regular pairs in its Hasse diagram. Backtracking enumerates every acyclic collection of disjoint regular pairs, giving 12,820 nonempty simplices and face vector \((28,300,1544,3932,4632,2128,256)\).

A deterministic element matching on this enumerated Morse complex is then checked against every one of its 58,680 Hasse covers. A topological sort verifies that the reversed matched-cover orientation is acyclic. The critical vector is \((1,0,0,2,101,0,0)\). Signed gradient reduction constructs the integral Morse boundary from the 101 critical \(4\)-cells to the two critical \(3\)-cells. A full-rank \(2\times2\) minor has determinant \(-1\), forcing Smith invariants \((1,1)\) and hence reduced homology \(\mathbb Z^{99}\) only in degree \(4\).

For representatives of all five \(S_4\) conjugacy classes, the program applies the induced permutation of the 28 primitive regular pairs and computes signed traces on every simplicial chain group. Equivariant Euler--Poincaré gives fourth-homology character \((99,1,-1,0,-1)\). Exact inner products with the rational irreducible character table of \(S_4\) produce multiplicities \((4,13,8,12,4)\).

A successful replay ends with `TETRA_S4_VERIFY_OK`. The computation is finite and exhaustive for \(\Delta^3\); no extrapolation to higher simplices is made.
