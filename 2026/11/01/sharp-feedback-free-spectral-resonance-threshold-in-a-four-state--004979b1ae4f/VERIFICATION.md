---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

Four-cycle Markov generator eigenvalues 0,-2a,-a±ia give Cov(1_{Z_t=0},1_{Z_0=0})=(1/8)e^{-a|t|}cos(a t)+(1/16)e^{-2a|t|}; its exact transform is S_H=a(w^4+3a^2w^2+6a^4)/(2(w^2+4a^2)(w^4+4a^4)). Conditional Poisson immigration/death gives S_Y=(beta/2+beta^2 S_H)/(gamma^2+w^2), retaining intrinsic shot noise. In x=(w/a)^2 the derivative is -b Q(x)/(2(g^2+x)^2(x+4)^2(x^2+4)^2); I symbolically and exactly recovered Q and Q(0)=256+96b-24b g^2. Every nonconstant Q coefficient is positive, hence the unique positive zero occurs iff gamma^2>4a^2+32a^3/(3beta). The explicit n=2,3 promoter spectra decrease; reversible generators have nonnegative Lorentzian sums. All boundary rates strictly positive; equality lies in the zero-peak branch. Finite rational derivative checks supplement exact proof.

## originality

PASS

Known general biochemical resolvent/spectrum methods and multistate-promoter mRNA filtering are credited. Full-text inspection of Rieckh–Tkačik identifies a three-state cycling information-transmission model, not this four-state mRNA peak phase boundary. Jia–Qian–Zhang treats feedback hybrid oscillations; Warren et al exact linear reaction networks. No retrieved result implies the stated iff four-state threshold and minimality, subject to older general-resolvent subsumption risk.

## value

PASS

An exact phase boundary for a measured stationary noise peak in a non-feedback four-state promoter is a motivated structural distinction from feedback-driven oscillations and from all reversible promoters. Unique peak and minimal equal-rate cycle size are more informative than a routine spectral rescaling; not a deterministic oscillation assertion.

The dated certificate retains the supplied scientific assessment, sources and limitations.
