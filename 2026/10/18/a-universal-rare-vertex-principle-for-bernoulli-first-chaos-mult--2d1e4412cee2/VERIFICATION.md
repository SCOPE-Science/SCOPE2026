---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

The orthonormal biased first-chaos coordinates yield kernel K_c(x,y)=sum c_i chi_i(x)chi_i(y). Its complex L-infinity operator norm is max_x E|K_c(x,Y)| by phase selection. At rare input coordinate x_i=r_i, the factor chi_i(x_i)chi_i(Y) equals U=(Z-a)/a with endpoint values -1,(1-a)/a; at common input it equals V=-(Z-a)/(1-a), a centered variable contained in the same interval. The secant bound for every convex t→|s+c_i t| (including complex c_i) gives E|s+c_i V|<=E|s+c_i U|. Independent coordinate replacements therefore monotonically increase row norm and make the universal rare vertex optimal for every diagonal multiplier. Adjoint argument supplies L1 norm; binomial centered first absolute moment telescopes to 2n(1-a) P(B_(n-1)=floor na), Gaussian CLT and fixed c/n Poisson local limit are correctly scoped. Independently enumerated all rows n=1..5 for heterogeneous rational coefficients and 27 exact binomial norm cases.

## originality

PASS

Known uniform Boolean cube invariant Fourier projection norm formulas and biased-coordinate Fourier stability provide background/special cases, but the same rare vertex maximizing EVERY complex arbitrary diagonal first-chaos multiplier in an INHOMOGENEOUS Bernoulli product uses a new convex-order dominance. No cited stronger theorem found to provide this assertion verbatim or by transparent reduction.

## value

PASS

Sharp operator norm formulas for canonical first-chaos diagonal multipliers are natural projection constants. The all-dimensions, heterogeneous biases, arbitrary complex coefficients simultaneous row-max collapse avoids exponential row optimization and supplies the Gaussian-to-Poisson regime transition; it is a structural phenomenon beyond a textbook binomial moment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
