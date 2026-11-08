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

For standard Gaussian surface measure of fixed axis-aligned finite-dimensional orthotope, facet Fubini factorization gives G(t)=C[φ(t-a)+φ(t+a)+Λ(Φ(t+a)-Φ(t-a))] with C=∏q_j and Λ=Σ(2φ(b_j)/q_j), q_j=2Φ(b_j)-1>0. Differentiate: Gʹ(t)=2Cφ(a)e^{-t²/2}cosh(at)[(a-Λ)tanh(at)-t]. If a−Λ≤0 bracket negative for t>0; otherwise its fʹ(0)=δ=a(a−Λ)−1 and fʺ(t)<0 for every t>0. Therefore δ≤0 gives unique centered global max and δ>0 exactly two global maxima ±t*, with t* unique positive root in (0,a−Λ); decay at infinity excludes others. Threshold a_c=(Λ+sqrt(Λ²+4))/2. Taylor expansion of tanh gives t*²=3δ/a_c²+O(δ²), positive gain 3Cφ(a_c)δ²/(2a_c²)+O(δ³), and critical negative quartic coefficient −Cφ(a_c)a_c²/6. Independently checked direct numerical derivative and local phase for multiple widths/dimensions.

## originality

PASS

Best-of-knowledge PASS after comparing the exact claim with its closest known general theorem and special cases. Novelty refers only to the stated full result, not common definitions, known subcases or routine ingredients.

## value

PASS

An exact all-dimensional translation phase diagram for a standard Gaussian geometric functional on a natural rigid family. It identifies when central symmetry of shape fails to produce centered perimeter maximizers, gives a sharp transverse-width threshold, uniqueness, square-root bifurcation and quartic critical flatness. Unlike broad order-of-magnitude maxima over arbitrary convex sets, this is a precise, motivated extremal classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
