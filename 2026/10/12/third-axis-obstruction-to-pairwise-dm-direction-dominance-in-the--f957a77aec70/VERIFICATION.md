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

Substitute Jx=0,Jy=-a,Jz=a and equal one-axis DM strengths a>0 into Li–Cao Wootters weights. Dx has duplicated eigenweights exp(2x),exp(-2x),exp(-2x),exp(2x), x=a/T, and zero concurrence for all T>0. Dy has weights 1,exp(2x),exp((sqrt5-1)x),exp(-(sqrt5+1)x); its concurrence is max(0,N(x))/sum(weights). After positive scaling, N has sign of H(x)=exp((3-sqrt5)x)-exp((1-sqrt5)x)-1-exp(-2sqrt5 x), with H(0)=-2, H(+infty)>0, H'(x)>0 for x>0. Hence unique x*=0.58258195... and Cy>0 iff 0<T<a/x*. Independently diagonalized spin-1/2 Hamiltonians and computed Wootters concurrence at T=a: Cx=0,Cy≈0.244952; checked root and open-neighborhood continuity. The source claim is the pairwise Jx>Jy heuristic, not the restrictive maximum-of-all-three claim.

## originality

PASS

The 2009 Li–Cao primary paper supplies general formulas and expressly states pairwise Dx-over-Dy dominance when Jx>Jy; the exhibited family contradicts that specific implication. Park 2019 includes general mixed-sign thermal thresholds but no inspected statement of this exact directional comparison/correction. Formula novelty is disclaimed; novelty is the concrete robust correction and unique interval, with explicit risk of an unlocated later correction.

## value

PASS

A mathematically explicit open set of parameter counterexamples to a directional entanglement control heuristic, exhibiting the structural role of third exchange coupling and a rigorous full temperature window, rather than an isolated numeric case. Does not overclaim all-parameter phase diagram.

The dated certificate retains the supplied scientific assessment, sources and limitations.
