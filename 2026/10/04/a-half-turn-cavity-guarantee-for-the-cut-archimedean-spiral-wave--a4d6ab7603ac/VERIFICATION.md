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

Run `python3 artifacts/verify.py`.

The checker has three logically separate tasks. First, exact rational arithmetic shows that the order-six partial sum of the Bessel series for \(J_0(481/200)\) is negative while the remaining alternating terms decrease, proving \(j_{0,1}<481/200\). Second, outward interval arithmetic covers \([3.1415,7]\), which contains \([\pi,7]\), and certifies the squared-distance inequality for the explicit shifted disk on every box. Third, a rational reverse-triangle bound handles every \(\theta\ge7\).

The interval pass is a proof enclosure of a continuum inequality, not finite point sampling. The scientific limitation is that this verifies one explicit comparison disk only; it does not optimize the disk center or determine the true spectral critical angle.
