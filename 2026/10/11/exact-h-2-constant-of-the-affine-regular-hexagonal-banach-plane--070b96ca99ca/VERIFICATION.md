---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For N(s,t)=max(|s|,|t|,|s-t|), I independently re-enumerated all six signed norm facets against six possible y edges after edge-transitivity fixes x=(1,u): solving N(x+y)=N(x-y) as piecewise affine equality with exact rational inequalities returns exactly eight nonempty segments (two each on y-edges 1,2,4,5). The repository's exact facet certificate additionally supplies explicit dihedral matrices identifying the two canonical families y=±((1-u)/2,1), 0<=u<=1/3. For lambda>=1 the facet lower envelopes cross at 2(1-u)/(1+u) and 2/(1-u); their derivative signs reduce the global infimum to crossings. The plus family is strictly above 32/45. For the minus family the sharp R(u)>=(32/45) reduces exactly to (3u-1)(15u^3-25u^2+56u-20)>=0 on [0,1/3]. The explicit unit isosceles pair x=(1,1/3), y=(-1/3,-1), lambda=3 attains N(x+3y)=8/3 and H2=3sqrt(10)/8. The lambda<1 case is obtained by interchanging the ordered unit pair and inverting lambda. This establishes the continuum theorem, not merely a finite sample; original audit and verifier scripts were inspected, not blindly executed.

## originality

PASS

The source DOI introduces the exact Baronti–Bertella H_p objective and ordered-pair symmetry and analyzes Hilbert/square cases and general bounds, but its examined mathematical sections have no formula for H_2 of the hexagonal norm. Searches for the exact hexagon/constant and dual presentations did not reveal a dominating published computation. H_4 in a different hexagon and other von Neumann–Jordan/Banach–Mazur hexagon invariants change the objective, so they do not imply this H_2 optimization. This is a best-of-knowledge judgment, not novelty certification; Resultary failed and names of equivalent pointwise mu_2 formulations remain a priority risk.

## value

PASS

A canonical affine-regular hexagonal nonsmooth Banach plane is a natural test space for a recently introduced Hilbert-deviation constant. The exact nonboundary maximizing lambda=3, exhaustive two-family classification and sharp universal norm ratio give a reusable polygonal-facet method, not a renamed general bound or arbitrary parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
