---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Normalize u by 2a+b=1 and use the positive Plucker relation r^2+t^2=s^2 on the stated symmetric x slice. Parameter r=s cos(theta), t=s sin(theta), theta∈(0,pi/2), and v=sin theta+cos theta∈(1,sqrt2]. The scale cancels and reduced log likelihood is g_b(v)=a log(v-1)+(a-1)log(v+1), giving exact derivative (1-bv)/(v^2-1). Sign analysis proves one symmetric strict maximum for b<=1/sqrt2 (quartic flat at equality) and two off-symmetric maxima for b>1/sqrt2; symmetric point then a strict local minimum. Solving (1+q)^2/(1+q^2)=1/b^2 gives the two exact reciprocal ratios. Independent SymPy verified derivative, exact quadratic roots, b=3/4 witness, and the quartic Taylor loss coefficient -1/(4 sqrt2). The argument makes no assertion about nonsymmetric full Grassmannian critical points.

## originality

PASS

The original positive Grassmannian paper supplies the model and computational/numerical multimodality discussion, but the inspected metadata/available abstract and follow-up searches did not locate the closed 1/sqrt2 critical ratio or reciprocal maximizing q values. Earlier squared-Grassmannian statements use probabilities proportional to squared Plucker coordinates and cannot cover the unsquared positive model. This is a conditional best-of-knowledge PASS: full Friedman v2 text was inaccessible, so an unindexed exact slice analysis in it remains material residual risk.

## value

PASS

The symmetric reflection slice is a geometrically motivated one-parameter family inside the source's model; a sharp bifurcation, exact optimizers, and quartic degeneration convert a qualitative/numerical multimodality into a precise theorem. A future researcher studying positive-Grassmannian likelihood can use these exact transition data without any claim to the full model.

The dated certificate retains the supplied scientific assessment, sources and limitations.
