---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-26.md",
      "INDEPENDENT_AUDIT_2026-10-26.json"
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

PASS. Any rectangle is parametrized by center c, orthonormal axes u,v and positive half-lengths a,b; containment is five support inequalities n_j·c+a|n_j·u|+b|n_j·v|≤r. Dihedral/axis-swap symmetry reduces orientation to θ∈[0,π/10]. The exact positive normal dependencies n0+n1+φn3=0 and φn1+n3+n4=0, together with trigonometric signs, give a cos(t+3π/20)+b cos(t−3π/20)≤sqrt(5)/2 with t=θ−π/20. AM–GM implies area 4ab≤5/[4cos(t+3π/20)cos(t−3π/20)]≤5/[4cos(π/5)cos(π/10)]. Equality forces θ a symmetry boundary, unique half-lengths and support-equality center; five rotations give precisely five optimizers. Independently checked both normal identities to ≈2×10⁻¹⁶, five candidate support slacks near machine zero and numerical constrained optimization over nine orientations peaking at the predicted endpoints. The analytic support inequalities establish all orientation cases, not sampling.

## originality

PASS

PASS qualified best-of-knowledge, not certified historical priority. Cabello et al., arXiv:1405.1223 Theorem 4, provides a general exact algorithm, not this closed-form evaluated pentagon result and complete equality classes. A 2017 Math StackExchange answer treats the same side-aligned candidate but explicitly assumes optimal orientation, so the numerical candidate is known. Resultary published exact rectangle area for even regular polygons does not include odd n=5. No inspected predecessor provides the positive-circuit orientation-free proof and all five maximizing rectangles. Residual risk: Unindexed elementary geometry proof of the regular-pentagon optimum may already exist.

## value

PASS

PASS. Completes the unrestricted maximum-area rectangle geometry of the regular pentagon, giving an elegant sharp support-functional certificate and rigid classification of all five maximizers. Its construction and approximate area were previously anticipated conditionally; mathematical value is the missing unconditional optimization and uniqueness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
