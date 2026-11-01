---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

With x=R^β>=1, F(x)=wλx/(1+λx)+(1-w)λ/(λ+x) and F prime=λ[w/(1+λx)^2−(1−w)/(x+λ)^2]. For 0<w<1, the sign is that of sqrt(w/(1-w))−(1+λx)/(x+λ). The latter ratio strictly increases from 1 at x=1 to λ as x→∞ since λ>1, giving the claimed decreasing regime w<=1/2, single strict global maximum when 1/2<w<λ²/(1+λ²), and increasing regime above. Endpoint w=0,1 handled directly; equality conditions have strict monotonicity for every finite β>0. Setting derivative zero gives x*=(λ√w−√(1−w))/(λ√(1−w)−√w)>1 and peak λ(λ−2√(w(1−w)))/(λ²−1); endpoints F(1)=λ/(1+λ), lim_{x→∞}F=w. Hence each share strictly between max{F(1),w} and the peak has exactly two positive β inverse solutions. The explicit λ=R=2,w=3/5,share=27/40 has polynomial 6x²−25x+22=0 and roots (25±sqrt97)/12>1; independently verified symbolically. The argument is exhaustive for exactly two mirrored-distance districts, not general geographies.

## originality

PASS

Huff 1963 supplies the probabilistic choice law; Nakanishi-Cooper 1974 develops MCI least-squares fitting, and Griffith 1982 generalizes the model for price elasticity. Fully inspected Griffith 10-page mathematical article and Wieland 2017 retail analysis do not state the exact mirrored two-zone λ,w response classification or the two admissible positive exponents; source techniques are acknowledged. A general theorem for rational mixtures of two opposed logistic curves might imply this elementary special case but was not established in searched primary literature. Huff 1963 and Nakanishi-Cooper full texts remain inaccessible after authorized institutional retrieval reported disconnected VPN; their abstracts do not prove noncoverage. The surviving priority is only the sharp specialization and explicit inverse ambiguity.

## value

PASS

One aggregate market share is a natural and often-used datum for fitting the Huff distance exponent. Even with attraction ratio and district distances known, the model can be noninjective; the exact parameter interval, closed peak, and two distinct admissible fitted exponents give a complete minimal counterexample and directly identify when a single aggregate observation cannot resolve β. The mirrored two-district geometry is the smallest actual spatial competition configuration with opposing distance effects and demand imbalance. This is a motivated complete response classification, not a random fitted polynomial.

The dated certificate retains the supplied scientific assessment, sources and limitations.
