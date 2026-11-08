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

For volume-uniform B_3, strict exclusion y outside z+tB gives limiting minimal center distance D=t-r. Intersection volume of radii 1 and t decreases with separation. Splitting circular slices at x0=(t^2-1-D^2)/(2D), integrating and dividing by 4π/3 yields L. Direct exact-rational algebra gives 1-L-(2-3r+r^3)/4=3(1-r²)^2/[16(t-r)]. The derivative has sign of 3r²-4tr+1, giving a single interior radial maximizer r_t=1/(2t+sqrt(4t²-3)); at t=1 its error is 2/9, and the full uniform asymptotic begins 3/(16t)+3/(128t³). At r>=1, both depth functions vanish, and the removable t=r=1 endpoint is zero. This reconstructs all t>=1 and all ambient y; finite rational sampling does not establish it alone.

## originality

PASS

Best-of-knowledge PASS after comparing the exact claim with its closest known general theorem and special cases. Novelty refers only to the stated full result, not common definitions, known subcases or routine ingredients.

## value

PASS

The canonical uniform three-ball is the natural sharp-order test model for convergence of ball-translate depth to halfspace depth. The full finite-scale pointwise error, unique off-center maximizing locus, sharp leading coefficient and next asymptotic correction answer a quantitative question not determined by the general O(1/t) rate. The exact equality geometry is independently useful; no universal higher-dimensional or distribution-free conclusion is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
