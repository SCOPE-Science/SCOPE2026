---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-31.md",
      "INDEPENDENT_AUDIT_2026-10-31.json"
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

For all finite connected undirected positive-weight graphs, p>0, positive convictions and stubbornness, the coercive potential has a positive minimizer (nonzero constant perturbation; connectedness excludes boundary zeros). At a positive equilibrium the max-coordinate ratio rules out two solutions. Writing H=κL+diag[σ_i((p+1)x_i^p-u_i)], the exact equilibrium identity gives Hx=pσ_i x_i^(p+1)>0. diag(x)Hdiag(x) has nonpositive off-diagonals and positive row sums pσ_i x_i^(p+2), proving H positive definite. Implicit differentiation yields D′=−(Lx)^T H^{-1}(Lx), strictly negative unless all u_i equal; at κ=0 H_0=diag(pσ_i u_i) gives the claimed right slope. Boundedness of x between min and max convictions and κLx=f(x) imply x→c1 with c=(Σσu/Σσ)^(1/p), and the EXACT identity D=(2κ²)^−1 f(x)^T L†f(x) yields the stated strictly positive resistance coefficient and exact inverse-square decay for nonconstant u. The one-sided κ=0 and constant-u cases were checked; no inference from finite tests substitutes for this derivation.

## originality

PASS

Originality is limited to uniform-coupling comparative statics and the sharp graph-pseudoinverse coefficient. Reynolds–Tudisco (2023 preprint, 2025 journal publication) already provide precisely this nonlinear equilibrium model, positive equilibrium uniqueness, smoothness and potential (equation (15), Theorem 1.2, equation (57)), so those inputs are not novel. Their inspected full text does not state the negative quadratic-form derivative or κ² asymptotic coefficient. Linear directed-network optimization and edge-changing linear opinion results concern different models. The monotone derivative is relatively direct from the known potential and IFT, and generic singular perturbation theory could entail the strong expansion: best-of-knowledge PASS retains this limitation, not priority certification.

## value

PASS

The unscaled graph Dirichlet disagreement is a natural measurable observable in nonlinear equilibrium opinion dynamics. Strict all-κ monotonicity supplies a global design comparison; the sharp large-coupling coefficient expresses heterogeneous conviction forcing through effective resistance and is meaningful even when individual pairwise differences are not individually monotone. This is an all-parameter structural asymptotic, not a renaming of equilibrium existence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
