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

For C_n^2 the shortest path distance is ceil(min(k,n-k)/2)=(delta(k)+delta(k) mod 2)/2. Discrete Fourier diagonalization of the circulant distance matrix yields an explicit nonconstant spectrum. For even n, the parity term contributes a single alternating frequency and every nonconstant eigenvalue is nonpositive. For odd n=2N+1, the parity Dirichlet sum yields lambda_j=-1/4(1/(1+(-1)^j cos(pi j/n))+(-1)^(N+j)/cos(pi j/n)); sign cases exclude odd n>=7 congruent 3 mod 4, and among n congruent 1 mod 4 admit only 5,9. At n=9 the frequencies 3,6 vanish; there are no positive modes. Finite Schoenberg negative-type equivalence and strict PD of distinct-point Gaussian kernels prove the claimed universal t>0 statement, with converse small-t failure from positive distance eigenmodes. Independent FFT checks of all n=3..128 matched formulas and admissibility including zero modes at nine.

## originality

PASS

Atik–Panigrahi 2016 Theorem 2.2 already establishes the full distance spectrum of even square cycles. That component must not be called new. The candidate distinctive theorem supplies a complete odd-n spectrum and Gaussian negative-type classification, with unique odd nine-vertex exception. Other graph-distance spectral and circulant papers cited do not directly state the odd spectrum in inspected material. Priority for a differently titled historical odd-square-cycle result remains uncertain.

## value

PASS

Universal Gaussian-kernel positivity and squared-Euclidean embeddability are canonical finite metric invariants. A complete infinite-family classification with a surprising isolated odd exception and exact minimum embedding dimensions has independent mathematical use and is not an arbitrary small-n check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
