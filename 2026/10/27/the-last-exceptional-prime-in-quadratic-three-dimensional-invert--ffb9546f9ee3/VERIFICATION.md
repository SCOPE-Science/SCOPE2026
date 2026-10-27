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
# Verification record

Run the self-contained `verify_exception73.py` using the Python 3 standard library. The checker first computes \(a_k(4)\) and \(\lambda_k(4)\) as exact rational numbers through degree six, then independently reconstructs them modulo \(73\) and confirms the four required units and the vanished second coefficient. Next it constructs \(\mathbb F_{73^2}\) from \(u^2=5\) (with a verified nonsquare), enumerates all \(5328\) nonzero field elements, and verifies that the four-power-trace signature partitions them into precisely \(2700\) Frobenius orbits, including \(72\) singleton orbits. It checks the two Galois-stabilizer cardinalities \(4\) and \(8\), corresponding to degrees \(18\) and \(9\).

Expected terminal statements include `COEFFS_OK`, `TRACE_ORBITS_OK`, two `STABILIZER_OK` lines, and `CERTIFICATE_OK`. Arithmetic is exact. The finite check does **not** compute the inverted sums directly, prove the published p-adic trace-recovery proposition independently, or claim an exhaustive literature search. The general infinite family follows from the paper's theorem plus the self-contained exceptional-prime argument, not from an extrapolated finite experiment. Independent mathematical audit remains unperformed.
