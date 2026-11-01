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

The base K_{p,q} Laplacian has four elementary invariant subspaces; for the 2-layer prism, L_G^+=L_base^+⊗P_+ +(L_base+2I)^−1⊗P_−. Direct currents for vertical edge sources yield exactly A,B and cycle values U,V=1+A/B−2R_eff. Horizontal sources fall into four base-edge incidence types with multiplicities 1,q−1,p−1,(p−1)(q−1); absolute cut and cycle sums are max(H₀,H₁) and max(1+H₀−2R_H,1+H₁−2R_H). I read the actual pinned verify_prism.py polynomial-region certificates and independently re-derived/recomputed 24 rational identities and nonnegative-coefficient polynomial witnesses plus all 31 finite pairs of the midrange; all passed. Separately built incidence matrices and orthogonal pseudoinverse projections for 10 (p,q) graphs, verifying every one of 410 edge columns, including exceptional (3,3) horizontal 73/30 and (3,7) phase disagreement. The polynomial certificates extend comparisons to all p≤q≥2, not finite extrapolation. Symbolically factored B−A and V−U to establish both switching thresholds.

## originality

PASS

The inspected Dilworth–Kutzarova–Ostrovskii primary paper develops canonical cut/cycle projections and computes norms for Hamming graphs/cubes and tori, not the p,q-asymmetric K_{p,q}□K₂ prism family with two different switching curves and the isolated (3,3) horizontal exception. General electrical transfer-current formulas are background and could implicitly specialize to these formulas, a recorded residual priority risk.

## value

PASS

The two distinct sharp extremizer-switching curves and a genuine exceptional balanced prism give a complete natural two-parameter spectral and Banach-operator invariant classification, not a trivial substitution into a single graph norm. It identifies when edge-orbit geometry controls cut versus cycle projections differently.

The dated certificate retains the supplied scientific assessment, sources and limitations.
