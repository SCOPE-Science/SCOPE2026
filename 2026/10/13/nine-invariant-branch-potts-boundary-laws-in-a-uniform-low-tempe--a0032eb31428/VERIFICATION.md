---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

The invariant I1 equations from the primary Potts boundary-law construction are h=k f_theta(h), l=f_theta(h)+(k-1)f_theta(l), with f_theta(x)=log((theta exp x+2)/(theta+exp x+1)). Both t=exp(h/k)>0 and y=exp(l/(k-1))/t^(1/(k-1))>0 are bijective coordinate transformations. The first polynomial F=t^(k+1)-theta t^k+(theta+1)t-2 has ≤3 positive roots by Descartes, and the strict signs at 0,2/theta,1,theta/2,theta for k≥4 theta>24 locate roots t_-<1<t_+. For every such t, H_t(y)=t y^k-theta t y^(k-1)+(theta+1)y-2 has ≤3 positive roots; strict sign brackets (0,1,theta/2,∞) when t<1, (0,1/2,2,∞) at t=1, and (0,3/theta,1,∞) when t>1 supply 3 each. The uniform bound theta>24 makes all inequalities strict (including H_(t+)(3/theta)>1-24/theta>0), proving exactly nine distinct pairs for every k≥4. Independently checked rational F endpoint signs for all 4≤k≤8 and theta=25,30,50; these finite signs are corroboration, not the infinite proof.

## originality

PASS

Rahmatullaev–Dekhkonov full arXiv article explicitly supplies the same two-value I1 equations, says b=0 can yield more than three branch solutions, and proves at least seven Gibbs measures in another overall regime, but gives no exact nine-count for M=[[k,0],[1,k-1]] on I1 uniformly for theta>24. Earlier scalar translation-invariant classifications concern other symmetry classes. This is a real exact phase-count refinement of a natural coupled boundary-law branch, subject to the quoted restricted scope.

## value

PASS

Exact splitting-measure multiplicity in a model already known to admit complicated nontranslation-invariant boundary laws is a motivated structural phase-count question. This uniform nine-solution theorem closes the source’s explicit more-than-three possibility on the natural M=[[k,0],[1,k-1]] family for all k≥4 in an explicit low-temperature region, not an arbitrary single numeric experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
