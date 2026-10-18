---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-13.md",
      "INDEPENDENT_AUDIT_2026-10-13.json"
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

The final theorem conditions the Fu–Xie–Li unit-pair integrand Phi_X(x,y) on r=min(||x+y||,||x-y||)/max in (0,1]. After y↦−y assume a=||x+y||≥b=||x−y||=ra. The exact identity Phi=(a+b)/(2ab)||b(x+y)−a(x−y)|| and triangle inequality yield Phi≤(1+r)(2+a(1−r)/2)=(1+r)(2−r) after a≤2. For every 0<r≤1, x_r=(1,1−2r), y=(1,1) in real ℓ∞² realize a=2,b=2r and Phi=(1+r)(2−r), so the continuum of conditional suprema is attained. Tracing equality at the global 9/4 yields r=1/2,a=2,b=1 and ||3σy−x||=3 with sign σ; converse directly attains 9/4. The exact near-extremizer stability |r−1/2|≤sqrt(delta) follows from the polynomial gap and is sharp. Verified rational samples r=1/80,1/2,4/5,1 by a separate exact-norm implementation, supplementary to the continuum proof.

## originality

PASS

Best-of-knowledge original contribution scoped to the exact theorem, not its already-known ingredients. Originality comparisons explicitly distinguish full prior statements, their implications and residual access risks; inaccessible articles alone were not used as proof of novelty or as automatic rejection.

## value

PASS

The intrinsic ratio of two canonical chords is a natural geometric stratification of the isosceles Dunkl–Williams problem. Although the universal 9/4 bound and its upper polynomial were already known, exact attainability of each constrained value and a necessary/sufficient pairwise equality classification sharpen the result in an independently usable way. The full profile gives a sharp quantitative deficit and identifies the geometry of equality pairs without claiming global space classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
