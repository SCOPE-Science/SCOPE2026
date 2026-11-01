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

The Zak transform Z_a g(x,theta)=sqrt(a) sum_{j in Z}g(x+aj)e^{-ijtheta}, with torus measure dx/a dtheta/(2pi), is unitary at lattice (a,1/a). The causal exponential-mixture assumption gives Z/sqrt(a)=int e^{-sx}/(1-e^{-as}e^{-i theta}) dmu(s). For each r in (0,1), Re[1/(1-r e^{-i theta})]>=1/(1+r), with exact equality theta=pi, and monotonic x yields essential minimum at x->a-. The magnitude upper bound from triangle inequality is sharp at x->0+, theta=0. Hence A=a[int e^{-as}/(1+e^{-as})dmu]^2 and B=a[int 1/(1-e^{-as})dmu]^2, equivalent to stated sample sums; both are finite/positive by int s^-1 dmu finite. For g_p=(1+t)^-p the inverse-moment condition iff p>1, giving A=(1-eta(p))^2 and B=zeta(p)^2. For 1/2<p<=1 the positive non-summable coefficients of a typical Zak fiber force unbounded essential amplitude via uniformly bounded Fejer convolutions contradiction; p<=1/2 is not L2. The independent finite exponential-mixture Zak values agree with boundary constants; infinite conclusions are analytical.

## originality

PASS

Belov--Kulikov 2025 full primary paper proves critical/subcritical frame existence for stably decreasing causal functions, including exponential windows. Definition 1 requires a uniform relative decay factor q(t)<1 for each t>0, which excludes polynomial tails g_p. Their theorem does not give the sharp two-sided frame bounds for all positive Laplace mixtures. Janssen 1996 Theorem C gives known exact special-window frame-set results but its full paper was inaccessible, so novelty is qualified.

## value

PASS

The two simultaneously sharp frame bounds for every causal positive Laplace mixture form a natural exact spectral classification rather than a generic frame-existence criterion. The power-tail Riesz/Bessel/non-L2 trichotomy locates a meaningful Hilbert-space threshold not accessible from exponentially decaying stable-decrease hypotheses.

The dated certificate retains the supplied scientific assessment, sources and limitations.
