---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-03.md",
      "INDEPENDENT_AUDIT_2026-11-03.json"
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

The cited Xu modal-ordering theorem identifies Gamma_{3,q}=(2π)^3(I_0(q)^{2/q}−I_1(q)^{2/q}) for q>3. At ν=1/2 the Bessel modes are c sin r/r and c(sin r−r cos r)/r², c=√(2/π). The first has unique absolute maximum at boundary r=0 with log profile −r²/6, producing I0=c^q C0 q^-3/2(1+O(1/q)); the second has unique interior absolute maximum r*≈2.08157598 where N(r)=(r²−2)sin r+2r cos r=0 and v''=−(1−2/r*²)v*, producing I1=(cv*)^q C1 q^-1/2(1+O(1/q)). Exact tails show no other peaks dominate. Taking 2/q powers and subtracting yields log rate 16π²(3−v*²) and full constant term. Independent root solving found r*=2.0815759778181007, Gamma∞≈127.86987173622556, rate≈443.69721257108506, and numerical quadrature at q=64,128,256 approached the claimed two-term asymptotic. Published finite-q modal premise is not established by numerics.

## originality

PASS

Xu 2026 supplies the exact finite-q coefficient and endpoint Bessel spectral reduction, rather than the new q→infinity logarithmic asymptotic. Carneiro–Oliveira e Silva–Sousa 2019 and Ciccone–Sousa 2025 address mode ordering/exact extremizers, not this quantified endpoint transition in inspected statements. The classical endpoint/interior Laplace method is standard, but applying it to the exact stability gap yields a new sharp rate; possible implicit prior derivation and inaccessible Xu full text are residual priority risks.

## value

PASS

A quantitative sharp stability constant is a natural spectral invariant for spherical Fourier extension. Its approach to the endpoint controls stability degradation at high mixed-norm exponent. The two distinct concentration codimensions create a non-obvious exact logarithmic rate and full next-order term; useful even though modal ordering itself is established prior work.

The dated certificate retains the supplied scientific assessment, sources and limitations.
