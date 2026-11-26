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

Independently expand the fitness as −2ky+kyz+h(z+βxz+αz²). For ω³=1 with positive imaginary part and U=x+ωy+ω²z, cyclic Fourier summation gives KU+L·conj(U)², where K=k(−2ω²−1/3)+h[(1+2α/3)ω+β(1+ω)/3] and L=[k+h(βω²+αω)]/3. Squaring gives the stated positive gap |K|²−|L|²; since |U|≤1, no off-center interior equilibrium is possible. At equal frequency the linearized motion in U is multiplication by K/3, giving the stated trace threshold and positive determinant. On z=0 the strict fitness difference directs the flow from x to y; cycling gives the three boundary connections. The eigenvalue ratio at each corner is 2k/[h(1+α)]>1 exactly below a_partial. The local saddle passages, composed with regular edge passages, have return exponent equal to the cube of this ratio. Equivalently, bounding the logarithmic growth and decay rates on sufficiently small corner boxes yields an upper return bound C r^p for some p>1. The return map and saddle/edge flow then give an open attracting collar of the cycle. The sink and cycle basins are disjoint and open; the nonempty invariant frontier of the sink basin stays outside both a thin boundary collar and a neighborhood of the sink. Thus an omega-limit set of a frontier point is compact and contains no equilibrium; Poincaré–Bendixson gives an interior periodic orbit on the frontier. Its Jordan interior contains an equilibrium by the planar index of a periodic orbit, hence contains the sink. The connected boundary collar lies outside, and neither basin can cross the orbit. The two threshold formulas give the stated gap, and a_partial>0 guarantees nonempty admissible a even when a_*<0; at the rational witness the thresholds are 3/13 and 1/3. The source checker was inspected, not executed: the infinite-parameter and separation claims follow from the argument, not the recorded symbolic output.

## originality

PASS

Credit the original model, a_* and cycle phenomenon to Griffin–Wu, and a neighboring later Resultary record for a local Hopf theorem in the same model. The supported distinct claim is the explicit global sufficient interval at arbitrary admissible fixed b, with a basin-separating periodic orbit throughout, not discovery of cycles or calculation of a Hopf normal form.

## value

PASS

A rigorous, explicitly checkable condition uniform over the full fixed-b wedge turns a local/numerical observation in a studied model into a guarantee of two attractors with an intervening interior periodic orbit. The strict width and rational witness make the regime usable without simulation. This is a motivated sufficient region, not a claimed maximal characterization.

The dated certificate retains the supplied scientific assessment, sources and limitations.
