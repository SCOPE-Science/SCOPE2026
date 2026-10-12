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

# Exact certificate and limits

Run `python3 verify_node.py` with Python 3 (standard library only). The actual execution returned `NODE_CERTIFICATE_OK` and checked the incidence scheme over the exact finite field \(\mathbb F_{11}\), without numerical approximations.

The program verifies all fifteen dependent triples and all 150 basis triples at the stated cuspidal realization, constructs the six other points through twelve line-incidence equations, checks nonzero second coordinates for the six intersections, and proves three exact polynomial identities expressing the remaining incidence determinants as \(3G\), \((-2x+2z)G\), and \((-2x+5z-3)G\). It then verifies the full cubic expansion at the marked point and its split quadratic tangent cone.

The mathematical passage from the explicit localized incidence presentation to an ordinary node uses the invertibility of the eliminated line-intersection coefficients at the point and the standard formal criterion for plane nodal singularities in odd characteristic. The checker does not assert a global description of the realization scheme, an independently performed audit, or any unproved modular comparison in characteristic \(11\).
