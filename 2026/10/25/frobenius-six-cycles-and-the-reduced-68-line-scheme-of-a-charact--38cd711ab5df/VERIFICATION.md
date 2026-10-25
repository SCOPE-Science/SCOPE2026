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
# Reproducible exact checks

A self-contained Python 3 checker `verify.py` reads the 68 explicit Grassmannian representatives in `lines.txt`. It first verifies irreducibility of the degree-six field polynomial, then the five coefficients of the full quartic restriction at each representative, reduced-row-echelon uniqueness, all tangent-space ranks, Frobenius closure, and orbit lengths. It was run against the included files and returned `VERIFY_OK`, with orbit multiplicities \(1^4 2^2 3^2 6^9\), four cuspidal-plane lines, and tangent dimension zero at every point.

An independent C++ enumerator `enumerate.cpp`, compiled using `g++ -O3 -std=c++17`, was run as `./enumerate 64 0x43`. It visited all \(17,047,617\) \(\mathbb F_{64}\)-rational line representatives in the six Grassmannian echelon charts, found exactly \(68\) contained lines, and produced a file exactly matching the included `lines.txt`. The five-point test is mathematically equivalent to the five homogeneous binary-quartic coefficient equations over this field.

The global upper bound of 68 geometric lines is Veniani's Theorem 1.1, applicable because the model lies in the cited \(A_3\) family. A finite search by itself would not exclude lines over larger fields; it is the published upper bound plus 68 explicit witnesses that does so. Likewise, the checked full-rank tangent Jacobians at all geometric points establish reducedness but do not assert any cohomological invariants of the surface. No independent audit has been performed.
