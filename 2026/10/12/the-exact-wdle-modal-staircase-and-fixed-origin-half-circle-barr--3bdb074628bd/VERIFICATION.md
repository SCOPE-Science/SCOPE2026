---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Wrapping the actual source survival law S(x)=exp(-phi x)(1+phi x+phi³)/(1+phi³) gives a normalized positive mass f(r)=K q^r(b+r). Its ratio f(r+1)/f(r)=q(1+1/(b+r)) is strictly decreasing in r and f(r+1)>f(r) iff r<H_m(phi), with H_m=2/(e^phi-1)-m/(e^{m phi}-1)-1/phi-phi². The decomposition H_m=1/sinh(phi)-1/phi-phi² + [2/(e^{2phi}-1)-m/(e^{m phi}-1)] has strictly negative derivative by the stated sinh(t)/t monotonicity and elementary hyperbolic inequalities, including m=2. Limits H_m(0+)=m/2-1 and H_m(infty)=-infty imply exactly k_m=floor((m-1)/2) transitions and modes only 0..k_m. Exact equality yields exactly adjacent ties; no rotated-origin claim. Independently checked normalization and several transition/boundary cases by direct wrap and closed mass, not treated as an all-parameter proof.

## originality

PASS

Best-of-knowledge original complete modal phase map for the actual fixed-origin WDLE family; relevant published source defines the law but available material does not provide the all-parameter sharp crossings. Residual risk from uninspected full publisher PDF is recorded, not concealed.

## value

PASS

The mode of a named, genuinely studied wrapped discrete distribution determines modal angular sector and shape-sensitive inference. The full integer-m, real-shape staircase supplies a sharp structural restriction and unique transition points, not merely a graph, a renamed ratio test, or an unmotivated numerical slice; later users of the fixed-origin model can use these exact boundaries.

The dated certificate retains the supplied scientific assessment, sources and limitations.
