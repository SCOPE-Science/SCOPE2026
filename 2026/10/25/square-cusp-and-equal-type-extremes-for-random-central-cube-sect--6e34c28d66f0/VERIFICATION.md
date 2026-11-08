---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

For the side-two cube with U uniform on S², sort a≥b≥c≥0 and normalize (a,b,c)=(1+r,1,q). Independently derived/intersected 500 generic cube-edge hulls: the given quadrilateral perimeter 4[√((1+r)²+1)+√((1+r)²+q²)]/(1+r) (r≥q) and given three-term hexagon formula (r<q) agreed to at most 1.43×10⁻¹⁴; the section has six edges exactly when q>r. In symbolic two-ray expansions r=t,q=st and r=st,q=t for 0≤s≤1, both first derivatives are -2√2; the second coefficients are 2s²+5√2/2 and 3√2s²/2+√2s+2, uniformly bounded, including seam r=q. Hence P*-P=2√2 max(r,q)+O((r+q)²) uniformly at the 12 signed-permutation maximizers. König–Koldobsky supplies the strict global maximum P*=4(1+√2) (rescaled from side one), so compactness forces every sufficiently small deficit there. The ordered sign chamber map u=(1+r,1,q)/√((1+r)²+1+q²) has exact area density ((1+r)²+1+q²)^(-3/2)=1/(2√2)+O(r+q). With h=ε/(2√2), each of 48 chambers contributes h²/(2√2)+O(h³) area, divided by 4π: 3√2/(8π)ε²+O(ε³). The rescaled conditional (r/h,q/h) converges weakly to uniform [0,1]², the seam q=r has null limit, giving P(N=6|event)→1/2 and normalized deficit max(V,W)∼Beta(2,1). Each oriented maximizer gets four identical chambers, so 12 labels are uniform and independent of the marks. Independent midpoint integration over the *exact* perimeter formulas at ε=.12,.06,.03 gave tail-to-leading ratios 1.08955,1.04296,1.02100 and six-edge ratios .49897,.49915,.49932; these are finite corroborations only. The exact 7-blob Git tree was reconstructed as 38d1f66faa71157704f4f95bec95a4f3519dbf14.

## originality

PASS

Best-of-knowledge: the sharp maximizing normal and complete pointwise piecewise perimeter formula are previously known in König–Koldobsky (2018/2019; earlier three-dimensional extremal result due to Pełczyński). Lonke (1998/2000) and the published rectangular-box hexagon law provide unconditional face statistics; a published orthotope-projection paper supplies different projection perimeter moments. None of the inspected primary mathematical statements evaluates the joint conditional square-cusp law, its 3√2/(8π) Haar upper-tail constant and 1/2 marked split. This is a specific probabilistic consequence derived using known deterministic formulas, not an independent discovery of those formulas; possible historical coverage by unindexed stochastic-geometry tables is recorded.

## value

PASS

The perimeter maximum lies exactly on the natural transition between four-edge and six-edge central sections, so the leading loss is a nonsmooth two-coordinate ℓ∞ cusp rather than the usual quadratic isolated maximum. The exact rare-event probability, sharp ε² coefficient, full conditional orientation-defect law, shortfall Beta(2,1) and equal polygon-type split quantify a natural geometric statistic that neither the deterministic maximum nor unconditional hexagon probability alone supplies. The marked law is directly useful for near-extremal random-section sampling and comparison of area versus perimeter conditioning. It is a narrow but motivated exact stochastic-geometric boundary invariant, not a claim of a new global cube-section maximum, all-threshold distribution, or high-dimensional theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
