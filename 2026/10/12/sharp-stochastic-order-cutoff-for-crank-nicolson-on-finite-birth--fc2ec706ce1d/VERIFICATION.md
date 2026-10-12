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
The theorem is proved for every finite irreducible birth–death chain in `RESULT.md` using an exact adjacent-difference intertwining and a spectral representation of the edge resolvent; no finite test substitutes for those analytical steps.

The standalone Python/SymPy checker constructs both three-state generators with exact rational entries, verifies \(DQ=HD\) and the Crank–Nicolson edge transfer, and checks the closed-form rational transitions at the witness times. It verifies \(T_{3/2}(0,1,1)^{\mathsf T}=(60,49,73)^{\mathsf T}/91\) for the symmetric chain, and the negative central transition diagonal \(-1/11\) alongside an entrywise nonnegative edge propagator for the second chain. A four-state nonuniform chain also verifies the gradient indexing. The checker explicitly tests spectral discriminants giving \(h_{\mathrm{ord}}=2/\sqrt3\) and \(2/\sqrt7\).

Unproved by the finite checker are all-rate and all-dimension claims; they follow from the stated generator/edge/resolvent proof. The interval endpoints are exact arithmetic thresholds, and no guarantee about finite-precision rounding near them is asserted.
