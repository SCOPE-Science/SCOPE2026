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

The cost gap is x−t; the scalar logit residual grows at least linearly in t and has bounded integral term, giving one zero, with the same monotonicity for the hard-step residual. At t_0 the logistic-minus-step kernel has zero mass by oddness and first moment 2∫_0^∞ z/(1+e^z) dz=π²/6. Interior endpoint truncation is exponentially small, so the scalar residual at t_0 is O(σ²) and the shift is O(σ²); a uniform local expansion then gives −π²f′(t_0)/[6(1+f(t_0))]. After rescaling, the shift disappears relative to the logistic layer and the powers of the absolute difference have integrals 2 log 2 and 2 log 2−1; continuity supplies the factor ρ(t_0). The L² norm itself is of order σ^{1/2}, not σ. The interval between cutoffs gives the stated partition mass, which is o(σ²) if f′(t_0)=0. In the witness, the hard root solves 3t+t²/2=1. On a feasible rectangle based at p≡1/2 the cost-difference field has nonzero circulation, with antisymmetric cross-direction coefficient 3/64; this rules out an exact potential in the stated cost normalization, not a weighted potential. The residual is negative at −1/4 and positive at t_0 by pairing the logistic tails. At a cutoff 0<t<t_0<1/2, the positive noise derivative from x=t+z dominates its opposite at x=t−z because 2+x is increasing, with a positive unpaired interval to the right; for t≤0 it is directly positive. Implicit differentiation and the high-noise sigmoid limit give the strict all-noise decrease and endpoint −1/4. The frozen numerical script was inspected, not executed; the above arguments are uniform proofs in the specified regimes.

## originality

PASS

The earlier uniform, two-moment Resultary theorem already covers the sharp cutoff and L¹ leading constants of the explicit affine example; even its cutoff expansion implies that example's hard-partition coefficient. The classical kernel moment and general qualitative equilibrium limits are likewise not new. The supported distinct content is the joint quantitative soft/hard profile theorem for arbitrary smooth positive type densities and weights (including f′ of either sign or zero), the squared-L² coefficient, and the all-noise monotonicity/endpoint result in the example. The latter does not follow from a local expansion.

## value

PASS

The general weighted theorem quantifies a qualitative convergence gap: the residual diffusive choice layer is larger than the induced partition displacement, and the latter can lose its quadratic leading term. Both error measures are operationally distinct. Global strict cutoff decrease in the explicit non-exact-potential example connects the small-noise sign with the entire response, beyond the known local affine example asymptotic. No general monotonicity in the kernels or all-resource extension is assumed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
