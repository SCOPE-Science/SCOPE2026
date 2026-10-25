---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

PASS: At collinear configurations token-score first derivatives vanish along S1 tangents, since all base vectors are parallel to e and tangent perturbations are orthogonal to e. At C and B self-inclusive attention averages equal ±e and ±t e, t=tanh(alpha). The sign-flip conditions are eta*b>1 and eta*b*t>1 (equality is undefined). The one-step tangent Jacobians have plus eigenvalues (1+eta*a)/(eta*b-1) and (1+eta*a)/(eta*b*t-1); minus eigenvalues 1/(eta*b-1) and (1+eta*a*t)/(eta*b*t-1). Exact squared return-map multipliers establish C stability iff eta>2/(b-a) and B iff b*t>a, eta>2/(b*t-a). Consequently B stability implies C stability; for eta>2/(b-a) critical alpha=atanh((a+2/eta)/b). Independent direct full-softmax centered-tangent finite difference agrees within 1.9e-13 for an interior parameter choice. No claim made about nonlinear neutral-equality stability or other attractors.

## originality

PASS

PASS best-of-knowledge: inspected Altafini 2026 defines this full self-inclusive normalized map but its analyzed hyperbolic stationary equilibria are under step restrictions and do not establish two attracting sign-flip two-cycles. Gao/Yang/Chen repulsive attention uses diagonal-masked convention and a different value map; the complete text was not obtainable, so no wholesale NOT_COVERING judgment is inferred from its abstract. Continuous-time normalized-attention flow cannot directly contain this finite-discrete-time alternating orbit. The precise large-step alpha/eta coexistence boundary was not found among Resultary hits.

## value

PASS

PASS: Exhibits and exactly classifies an unusual coexistence of two distinct open basins of period-two attraction in the smallest full self-attention network, with an explicit sharp temperature onset. It is a diagnostic finite-step bifurcation distinct from a trivial fixed-point Jacobian exercise, and clarifies a phase omitted by small-step analyses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
