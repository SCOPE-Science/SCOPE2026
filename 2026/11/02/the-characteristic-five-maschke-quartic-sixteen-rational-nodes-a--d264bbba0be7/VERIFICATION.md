---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

In characteristic five, the partials are x_i(x_i²−2S), S=Σx_i². If all vanish, S cannot be zero at a projective point; the number of nonzero coordinates satisfies 2r=1 in F5, so r=3. This gives precisely the sixteen rational sign patterns up to overall scale. The affine Hessian at [1:1:1:0] has determinant 2 and sign/permutation symmetry transfers this to every point, giving A1 singularities. Isolated singularities exclude repeated factors and distinct components (two projective surface components meet in positive dimension); the hypersurface is normal by R1 and S2. Adjunction and rational double points give trivial canonical bundle and H^1(O)=0 on the minimal resolution, hence a K3. Each rational node is replaced by a smooth conic over F5, hence by P1 over F5. My own replay /workspace/review_replay.py uses a distinct chart ordering and θ²=2 for F25; it checks the Hessian from the original form and exhausts the charts over F5 and F25, getting totals 16 and 776. Adding 16q gives 96 and 1176. The K3 trace formula gives H² traces 70 and 550, and purity gives |α_i|=5. Equality in the triangle inequality at the second trace forces every α_i²=25, and the first trace then gives multiplicities 18 and 4. This proves all extension counts and both zeta functions; the two counts are exact inputs, not extrapolation. No Frobenius semisimplicity assumption is needed for the trace or zeta assertions.

## originality

PASS

The supported distinct result is the arithmetic of this specified Maschke reduction and its resolution, not the general Kummer degeneration or the existence of a characteristic-five K3 with this spectrum. The strongest indexed results with the same spectrum count different projective models. The inspected classical sources identify the integral equation and general Kummer loci, but do not settle the arithmetic of this fiber. No exact matching theorem or implication from those sources was established in the bounded comparison.

## value

PASS

This characteristic-five reduction fixes a historically distinguished equation and a field where it acquires the extremal sixteen-node geometry. Its rational exceptional configuration, attainment of the sharp K3 bound over F25, and precise descent over F5, including the four minus signs, are meaningful model-specific arithmetic. The result determines the singular-model and resolution zeta functions; the former differs from those of the matching Hessian examples. This is useful exact information about a natural model, not a claim to have discovered a new numerical spectrum or new Kummer geometry.

The dated certificate retains the supplied scientific assessment, sources and limitations.
