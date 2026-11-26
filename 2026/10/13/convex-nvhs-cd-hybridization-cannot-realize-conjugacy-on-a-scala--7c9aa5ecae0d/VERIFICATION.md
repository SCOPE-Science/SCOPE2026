---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

For the coefficient and clipping rule stated in the frozen record, the first-step obstruction holds exactly. The first iterate is rx0 with r=1-aα0, and y0=aα0 d0. Hence d0ᵀy0=aα0||d0||²>0. Dividing the two strong-Wolfe conditions by their positive scalar factors gives |r|≤σ and aα0≤2(1-δ). The latter is automatic on the curvature interval because δ<σ<1/3. Conjugacy in one dimension would require d1=0 since y0≠0, giving β=-r. The CD coefficient is r². Using the NVHS* scalar specialization r(r-|r|)/(1-r) in the record, for positive r the target is negative and both endpoints are nonnegative. For r=-s<0, 0<s≤σ<1 and s²<2s²/(1+s)<s; the target is again strictly outside the hull. The affine weight of CD is (β_conj-β_NVHS*)/(β_CD-β_NVHS*) and reduces to -1/r in the understep and -1/s in the overstep. The denominator is nonzero in both cases; clipping selects NVHS*. The exact step r=0 gives a zero gradient and is excluded, so no division at r=0 is needed. The finite rational artifact independently documents what scalar formulas were tested but is not evidence for the universal quantifier or for paper attribution.

## originality

PASS

A conjugacy-derived interpolation parameter leaving [0,1], subsequently clipped, is known in related hybrids and is not credited as new. The supported distinct finding is the strict all-nonexact-first-step convex-hull obstruction for the stated NVHS*–CD endpoints in the condition-one quadratic, including both under- and oversteps and the same clipped endpoint in both cases. The inspected close predecessor and catalog cases use different coefficient or clipping mechanisms; none of their actual statements supplies this obstruction by specialization. Access limits on the original 2026 paper and the 2017 LS–CD comparison remain explicit.

## value

PASS

A condition-one scalar quadratic is a baseline for a conjugacy-based update, not an ill-conditioned or exotic test. Under the stated blend, adjusting the weight cannot recover exact conjugacy on any nonterminal allowed first step, and clipping nullifies the hybrid on both sides of the line minimum. That universal local obstruction gives a substantive boundary on the method's design objective, without confusing that objective with descent or convergence.

The dated certificate retains the supplied scientific assessment, sources and limitations.
