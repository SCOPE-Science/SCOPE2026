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

The normalized projective-harmonic Jacobi kernel R_{d,k} on projective space has three inner-product values on a union of m MUB:1 within a point,0 within each basis,1/d across bases. Gram decomposes into within-basis zero-sum W, between-basis zero-sum B, total constant C, with eigenvalues 1-u,1+(d-1)u-dv,1+(d-1)u+d(m-1)v. Independently computed exact rational u_k,v_k for k=0,1,2,3 via terminating hypergeometric sum; deduced ranks 1,m(d-1), md-1_{m=d+1},md. Quadratic for m=d has condition number d+1; cubic for m=d+1 has max 9/2 at d=3, formula d(d+4)/((d-2)(d+2)) thereafter. Exact rational checks independently evaluated all k and eigenspaces d=3..17; proof uses algebraic positivity for all allowed d,m, not experiments.

## originality

PASS

Complete mutually unbiased bases are known complex projective 2-designs (Klappenecker–Rötteler), so quadratic linear dependence of complete collections and standard Jacobi/harmonic kernels are prior. Roy–Scott extend weighted projective 2-designs. The joint exact-degree rank/conditioning threshold for incomplete versus complete MUB and sharp cubic 9/2 uniform bound were not identified in inspected prior theorems. Strong residual association-scheme and quantum tomography re-expression risk; best-of-knowledge PASS restricted to full spectral classification.

## value

PASS

A natural stability/solvability discontinuity when adjoining the final unbiased basis: one quadratic interpolation direction is lost exactly while cubic restores full rank with dimension-uniform conditioning. Sharp Gram spectra and interpolation thresholds useful in design sampling and projective harmonics.

The dated certificate retains the supplied scientific assessment, sources and limitations.
