---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For zero trace c=1+b, map F(x,y)=(-b y+d sigma_h(x-y),x), 0<b<1, prescribed n-periodic ternary symbols yield a UNIQUE exact periodic response z_i=(Σ_{k=0}^{L-1}(-b)^k s_{i-1-2k})/(1-(-b)^L), L=n/gcd(n,2). This is a closed finite linear system since denominator !=0. Branch feasibility: active s_i u_i>0 and r=d/h>1/H strictly; neutral r<=1/Z inclusively. For b=1/4 independently enumerated exactly every 358 nonzero words of lengths 1..5 in rational arithmetic, mod cyclic rotations, obtaining precisely four feasible n=5 classes: (-1,-1,0,1,0),(-1,0,1,1,0), each r in (205/252,205/188], and (-1,-1,0,1,1),(-1,-1,1,1,0), each r in (41/16,41/4]. None for n<=4. Intersect 0<r<1 leaves exactly two primitive 5-orbits above threshold, none at equality because active threshold is strict and grazing point neutral. For 0<b<b* solving b+2b³=1, explicit five-word difference tuple and Q,Z bounds yield nonempty r interval Q/(1-b³)<r<min(1,Q/Z); odd symmetry gives distinct second orbit. Jacobian J²=-b I, so both strict-itinerary cycles locally attracting (five-step multipliers magnitude b^(5/2)); origin stable. Complete census only period<=5 and b=1/4; nonempty parameter open family not full phase diagram, no long-period exclusion.

## originality

PASS

PASS (best of knowledge). The model itself and overlapping periodicity are prior work by Gardini–Radi–Schmitt–Sushko–Westerhoff (2023) and 2025 continuation. Comparison of their actual parameter regimes and symbolic words shows their principal theorems use d>h or cycles with other neutral counts, whereas this finding proves sharp onset at d/h=205/252 in 0<d<h with two neutral visits and exhaustive primitive periods <=5. Research Resultary hits for two-zone maps or other piecewise-affine periods are not equivalent. Possible missed weak-forcing appendix or unindexed symbolic search remains residual risk.

## value

PASS

A precise threshold and complete short-period classification in the previously less-studied weak-sentiment regime is an independently motivated dynamical fact: grazing-boundary inclusion is mathematically decisive, the two distinct attracting 5-orbits coexist with a stable equilibrium, and finite exhaustive word space is exactly relevant to the period<=5 statement. No claim beyond period five or global dynamics is needed for value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
