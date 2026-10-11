---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

The package starts from the exact line and conic of Calussi--Carlini--Fatabbi--Lorenzini Example 4.3 and reconstructs their Hadamard quartic. The residual intersection equation for two rulings yields an explicit binary-cubic parametrization of the proposed singular curve. Its four coordinate cubics have coefficient rank four, so the image is a projective linear re-embedding of the standard degree-three Veronese curve. For the quartic Jacobian ideal \(J\) and the three displayed quadrics \(I=(q_1,q_2,q_3)\), exact identities give \(J\subset I\), while Gröbner reduction gives \(q_i^3\in J\) for every generator. Since \(I\) is the prime twisted-cubic ideal, \(\sqrt J=I\). A fresh independent symbolic replay confirmed coefficient rank four and the vanishing of all three quadrics on the parametrization.

## originality

PASS

The exact primary example states that the Hadamard product is a singular quartic surface with one-dimensional singular locus but does not identify that curve. Classical ruled-quartic classifications contain families with twisted-cubic double curves, but they also contain other one-dimensional singular-locus types; the classification alone does not select the type for these particular Hadamard coefficients. The package supplies that missing identification by an exact radical computation. Current Resultary search returned the assigned result as the exact hit and no prior source-specific identification.

## value

PASS

The example is used to show sharpness of a singular-locus dimension bound, so identifying its actual singular curve is a natural geometric refinement. The twisted-cubic description supplies an intrinsic projective model and an exact radical certificate, rather than only another finite computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
