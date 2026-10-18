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

# Verification details

Run `python3 code/reproduce.py` from the package root with Python 3, SymPy and a C++17 compiler. This procedure was run from the public source directory and passed, reproducing the 141 nonzero coefficient-space orbits by transvections, the 142 orbits including zero by Burnside, and all 36 geometrically smooth projective orbits. The unit-ideal Gröbner checks certify smoothness on all four charts. A separate symbolic tangent-plane calculation checks every rational point of every smooth representative and an independent line-containment test verifies all 258 rational points in those representatives. Regenerated data agree with stored orbit, point-contact, and weighted 21-stratum tables.

These are finite-field exact computational checks supplemented by the symplectic-matrix proof of the 28 smooth 15-point cubics; no numerical extension-field cutoff is taken for geometric smoothness. The classification is limited to equations over F2 modulo PGL4(F2), and its historical priority has not been independently audited.
