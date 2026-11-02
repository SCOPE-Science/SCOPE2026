---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-30.md",
      "INDEPENDENT_AUDIT_2026-10-30.json"
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

For normal real K=aI+bJ, exactly three restarted inner calls give P3(γK)=I−γK+(γK)^2−(γK)^3; because K is rotation-dilation, its squared norm is the scalar |(1−z^4)/(1+z)|². With r=γL,c=a/L, q−1=G/(1+r²+2rc), G=r^8−2r^4(8c^4−8c²+1)−r²−2rc. Both angular boundaries and all r<=1/2 are strictly negative. Any first nonnegative maximum at r<1 is interior and solves G=∂cG=0. Independently verified resultant 65536r^16(4r^6+4r^4+4r²+3)^2 H(r²), H(u)=16u^6−32u^5+48u^4−104u³+72u²−8u+3; Descartes substitution yields exactly one positive root u∈(0,1). Rational sample r=19/20,c=2/3 has q=1773279907/1728000000>1 (independent exact 2×2 matrix multiplication); a neutral scaled rotation occurs at unique r*=sqrt(u*)≈0.940521095740431. The universal result applies only to normal two-dimensional saddle K, not arbitrary nonlinear/non-normal models.

## originality

PASS

Best-of-knowledge exact statement and implication comparison: closest accessible primary papers and ranked published findings do not establish this precise claim under the stated parameters. This is not a historical-priority certificate; see source inspections and risks.

## value

PASS

Fixed-cost approximate proximal schemes need a sharp safe outer-iteration step bound; inner fixed-point contractivity alone is not sufficient. The exact radius, a normal strongly convex-concave divergence witness and the reentrant stable/unstable dependence on damping resolve a concrete finite-iteration stability question not answered by end-to-end guarantees for a growing inner budget.

The dated certificate retains the supplied scientific assessment, sources and limitations.
