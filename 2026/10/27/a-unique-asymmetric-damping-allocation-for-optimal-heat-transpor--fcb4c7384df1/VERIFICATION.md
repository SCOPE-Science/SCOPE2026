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

For the stated unit-mass Itô system with positive springs and frictions, the positive definite mechanical energy dissipates as −g v₁²−h v₂²; the only invariant zero-dissipation trajectory is the origin. The linear drift is thus Hurwitz and the stationary Gaussian covariance is unique. Write K=(a,−k;−k,b), Γ=diag(g,h), S=E[xxᵀ], R=E[xvᵀ]=(0,C;−C,0), H=E[vvᵀ]. The stationary equations are H=SK+RΓ and ΓH+HΓ=RK−KR+2diag(gT₁,hT₂). The latter gives H₁₁=T₁−kC/g, H₂₂=T₂+kC/h, H₁₂=(b−a)C/G. Symmetry of S gives KH−HK=KRΓ+ΓRK. Its off-diagonal entry yields kΔT=C[(a−b)²/G+k²(1/g+1/h)+ah+bg]. The energy input current is kC; substituting g=Gp, h=G(1−p) yields the displayed formula. Its positive numerator is independent of p, and the denominator has second derivative 2k²[p^−3+(1−p)^−3]>0 and first derivative limits of opposite infinite signs. This proves the unique interior optimum and the side of 1/2 follows from F′(1/2)=G²(v−u). With unequal traps, the critical equation gives δ=min(p*,1−p*)→0 and Gδ→k/√|u−v|. The reciprocal term is then O(G), and the leading denominator is G²[min(u,v)+k], whereas balance gives G²[(u+v)/2+k]. For small G, the odd part of F′ about 1/2 has leading coefficient 32k² and cubic remainder; the shift is G²(u−v)/(32k²)+O(G⁶), which implies the stated O(G⁴). For equal traps balance holds exactly; the zero-temperature-difference degeneracy is not within scope.

## originality

PASS

Credit Henkel for the broader forward heat law: the classical white-noise, Ohmic, unit-mass specialization determines the current before doing the frozen covariance calculation. Do not credit the current model or the existence/direction of current as new. What survives comparison is the fixed-sum allocation theorem, including its exact unique optimizer, which oscillator gets more damping, the nonzero limiting smaller friction, and the enhancement factor. The inspected heat-current and damping-allocation comparisons optimize different variables or objectives, or use different dynamics. The conclusion is limited to the inspected sources, not a claim of priority.

## value

PASS

A fixed damping budget poses a natural design problem distinct from predicting current at given bath contacts. For detuned traps the allocation direction and the finite nonzero weak-contact limit quantify a singular optimum: increasing budget mainly strengthens the stiffer contact but must not turn off the other bath. The asymptotic improvement over balanced damping is explicit. Those conclusions, rather than the already-covered forward law or convexity in isolation, are independently useful.

The dated certificate retains the supplied scientific assessment, sources and limitations.
