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

# Reproducible verification
Run `python3 verification/verify_ultrametric.py` using Python's standard library. The program independently enumerates Hamiltonian-path weights with subset dynamic programming and reduces filtered boundary columns over \(\mathbb F_2\) to obtain the complete barcode. It tests 48 finite examples, including cluster sizes \(1\) through \(5\) where applicable, and \(u,v\ge2\) in the theorem's domain, with two pairs of edge lengths. The literal success marker is `VERIFY_OK`.

The program only tests finite cases and one coefficient field. The arbitrary-size integral homotopy claim and all-field persistence assertion rest on the mathematical proof (explicit pure/mixed face weights, a split inclusion in Mayer–Vietoris, connectivity and cellular homotopy arguments, and the behavior of filtration maps). These tests are independent code checks, **not** an external or independent scientific audit.
