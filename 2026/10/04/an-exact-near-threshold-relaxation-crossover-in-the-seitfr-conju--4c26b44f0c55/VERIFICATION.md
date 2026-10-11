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

The total-population equation gives the exact full-system eigenvalue \(-\mu\). Eliminating the total-population direction yields the displayed five-dimensional tangent Jacobian. An independent exact-rational replay of the inspected verifier reproduced the affine polynomial \(\det(J_{\mathrm{tan}}+\mu I)\) and its unique root \(\mathcal R_\times=386467087274709075099662209/386355335676178838352248250=1.0002892456456818\ldots\). For \(1<\mathcal R_0<\mathcal R_\times\), positivity of this nonzero determinant in odd real dimension contradicts all shifted eigenvalues lying in the closed left half-plane, so some tangent eigenvalue has real part greater than \(-\mu\). At the root, \(-\mu\) is a tangent eigenvalue. The argument does not claim stability on the whole interval or dominance above the crossing.

## originality

PASS

The primary article's numerical spectral study begins at \(\mathcal R_0=1.01\) and reports the demographic mode as dominant only on that sampled range, while its bifurcation analysis gives only the qualitative forward transcritical crossing at one. General reproduction-number/center-manifold theory explains a critical eigenvalue approaching zero but does not determine this model-specific collision with the separate demographic eigenvalue. Current published-finding searches under model, dominant-mode, critical-slowing and crossover aliases found no earlier exact collision value or equivalent theorem.

## value

PASS

The exact collision identifies a genuine boundary in the interpretation of a published model's relaxation spectrum that the source's coarse grid necessarily misses. It is a motivated source-specific stability refinement with an exact certificate, not an arbitrary parameter sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
