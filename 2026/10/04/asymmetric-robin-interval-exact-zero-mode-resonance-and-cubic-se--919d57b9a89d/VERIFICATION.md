---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

An affine zero mode gives a two-by-two boundary system whose determinant vanishes exactly when \(\lambda_0+\lambda_\ell-\lambda_0\lambda_\ell\ell=0\), and then the kernel is one-dimensional. Since both Robin parameters are nonzero, the zero-energy scattering matrix is \(-I_2\), giving scattering multiplicity one. Expanding the exact secular function gives a linear coefficient proportional to \(\ell-\lambda_0^{-1}-\lambda_\ell^{-1}\); on resonance the cubic coefficient is nonzero because \(\lambda_0^{-3}+\lambda_\ell^{-3}=\ell(\lambda_0^2-\lambda_0\lambda_\ell+\lambda_\ell^2)/(\lambda_0^2\lambda_\ell^2)>0\). The inspected exact formal-series checker was independently replayed across positive and mixed-sign cases and agrees with the symbolic proof.

## originality

PASS

Bolte--Egger--Steiner explicitly analyze the same one-edge Robin anomaly only on the symmetric diagonal \(L=\lambda I_2\), obtaining resonance \(\ell=2/\lambda\), secular order three there and order one otherwise, and scattering multiplicity one. The audited theorem classifies the full unequal-endpoint two-parameter family. Targeted searches found no published asymmetric version.

## value

PASS

The result gives the complete two-parameter continuation of the exact zero-energy multiplicity anomaly that motivated the source example, showing that it is a codimension-one resonance surface rather than an equal-parameter accident and that the trace-formula correction remains invariant. This is a natural complete classification even though its final algebra is elementary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
