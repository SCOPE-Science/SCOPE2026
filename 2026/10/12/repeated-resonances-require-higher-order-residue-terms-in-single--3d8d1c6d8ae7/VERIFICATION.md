---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

The submitted 4×4 U_α is unitary for |α|=1 because its 3×3 active block is real orthogonal, with outgoing mapped to α incoming. Exact characteristic polynomial is z²(z−r)²−α(1−rz)² for r=−1/√6. U_0 has a nonzero double resonance with a size-two Jordan chain. The source's S=−g/f then has a genuine order-two pole at r; its w=z^{-1} Laurent series gives h[n]=6δ_{n2}+(5(5n−17)/36)r^{n−4} for n≥2 and zero earlier. Independently checked unitarity, Jordan dimensions and 12 coefficients with symbolic algebra. The general residue derivative for multiplicity m is standard contour calculus and yields polynomial×exponential terms, demonstrating failure of the source's unqualified pure-exponential formula.

## originality

PASS

Cottrell Theorem 2.10 uses denominators η_j−η_k with no distinct-root hypothesis and asserts a pure exponential sum. The same paper discusses higher-degree eigenvalue roots for nonunit closures in Theorem 2.5 but does not implement their higher-order impulse residues. Standard DSP repeated-pole formulas do not supply the explicit permissible graph closure matrix or source-specific correction.

## value

PASS

A mathematically admissible explicit double-resonance counterexample identifies a missing simplicity hypothesis in a published quantum-graph impulse-response theorem, and supplies the correct finite-dimensional replacement. The generic repeated-pole rule is routine, but demonstrating its necessity in this specific physical closure model is a substantively motivated correction.

The dated certificate retains the supplied scientific assessment, sources and limitations.
