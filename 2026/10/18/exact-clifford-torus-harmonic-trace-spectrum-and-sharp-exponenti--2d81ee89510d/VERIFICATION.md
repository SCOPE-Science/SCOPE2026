---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-24.md",
      "INDEPENDENT_AUDIT_2026-10-24.json"
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

Reconstructed S³ probability-normalized Hopf measure, scalar Jacobi harmonic orthogonality, degree k=a+b+2j multiplicities (k+1)², and Fourier block restriction to the theta=pi/4 Clifford torus. Each torus weight (m,n) with s=|m|+|n|<L gives exactly one positive eigenvalue sum of squared Jacobi evaluation coefficients; j=0 is nonzero, proving the diamond range and rank 2L²−2L+1. j=0 term is (s+1)2^(−s)binom(s,a)≥(s+1)/2^s≥L/2^(L−1); only four axial s=L−1 modes attain equality for L≥3 (all five at L=2). This establishes optimal pseudoinverse norm sqrt(2^(L−1)/L). Independently calculated exact rational Jacobi sums and Chebyshev Laurent coefficients for every frequency L=1..7 (L7 rank85, least 7/64), including normalized trace/rank identities; finite checks supplement all-L analytic proof.

## originality

PASS

Classical Hopf harmonic eigenmodes and Jacobi normalization are not original; the reviewed theorem evaluates the entire bandlimited scalar restriction operator to the fixed Clifford torus, including all positive eigenvalues, exact range/kernel and sharp minimum over every band. Prior SU(2)/S³ harmonic-basis references and SO(3) global sampling results inspected concern different operators or incomplete trace extrema. Best-of-knowledge PASS, with risk of a general trace theorem implicitly giving identical block spectrum.

## value

PASS

Restriction to the canonical Clifford torus is a natural inverse harmonic-measurement problem. Exact attainable Fourier data, nullspace dimensions, and exponentially worsening sharp minimal-norm inverse give both algebraic identifiability and precise noise amplification for every cutoff, unlike an unmotivated finite spectral experiment.

The dated certificate retains the supplied scientific assessment, sources and limitations.
