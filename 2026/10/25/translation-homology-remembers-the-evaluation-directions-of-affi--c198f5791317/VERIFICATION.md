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

Run `python3 verify.py` with Python 3 and standard library only. Success terminates with `VERIFY_OK`.

The script tests prime-field arrays at \((q,n)=(3,4),(5,4),(5,5),(5,6),(7,8)\). Across those examples it enumerates the actual row facets and subfaces, proves all pair projections are bijective by exhaustive enumeration, verifies every complete simplex-collapse pair against the then-active complex, and checks the terminal graph independently. Translation trace checks enumerate all fixed simplices at every group element, rather than assuming the graph trace formula, and a complex discrete Fourier transform checks all irreducible multiplicities. The first four cases also compare against an independent exhaustive partial-assignment enumerator.

Acyclicity follows from explicit elementary free-face removals; no discrete-Morse matching or infinite computational certification is assumed. Fourier computations are numerical with a tolerance of \(10^{-7}\), while the theorem's algebraic character proof is exact. Prime-power fields of nonprime order are covered by the general linear-algebra proof, not the finite checker. This review is not an independent audit.
