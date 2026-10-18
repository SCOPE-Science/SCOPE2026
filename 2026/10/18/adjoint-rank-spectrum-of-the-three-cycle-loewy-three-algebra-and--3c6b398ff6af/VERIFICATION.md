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

Run `python verify.py` with Python 3.9 or later; no third-party libraries are needed. The script defines the multiplication table directly from three oriented-cycle vertices and allowed paths of lengths zero, one and two. For each of the diagonal coincidence patterns it enumerates every six-tuple of radical coefficients over fields of orders two, three, four and five, and computes exact nine-by-nine commutator ranks by Gaussian elimination.

The degree-two extension for order four is implemented explicitly by the polynomial \(z^2+z+1\). The full proof applies to every finite field; the computational ranges are validation samples, not an infinite proof. The output `VERIFY_OK` is produced only if every conditional frequency is exactly as predicted. No numerical approximation, random sampling, or unstated dependency is used.
