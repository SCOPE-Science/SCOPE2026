---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

Parity splits the signed hemisphere compression into off-diagonal even/odd blocks; its gap-product is the squared determinant of the block. The block Gram ratio is H_m(0,beta)^2/[H_m(-1/2,beta)H_m(1/2,beta)]; Jacobi beta-moment/Selberg determinant evaluation yields the exact gamma product. Independently re-evaluated all three Hankel determinants with 60-digit mpmath and compared the gamma product in 15 cases m=1,2,3 and beta=-3/4,0,1/4,1,3 (relative error <1e-47). Analytically, log-gamma second differences yield monotonicity, while the t=m+j+beta+1>=m positivity and u(t)=1/(4t)+O(t^-2) give a beta-uniform O(1/m) sum-of-errors bound, including beta growing faster than m; Barnes ratio supplies the m^-1/4 constant. The finite checks are corroboration, not the all-parameter argument.

## originality

PASS

The beta=+infty Hermite degeneration and the classical fixed-symbol Hankel/Selberg identities overlap the building blocks, not the precise beta-uniform dimension/bandwidth crossover. Primary Simons-Dahlen-Wieczorek provides spherical Slepian operator theory and cap numerics, not an all-gap product. Deift-Its-Krasovsky Theorem 1.20 concerns fixed FH data and endpoint cases; it does not assert uniformity when the Jacobi weight exponent itself grows with the matrix size. Related published Hermite result has beta-independent low-pass product and limiting constant, not the interpolating regime. Best-of-knowledge originality survives, without claiming the classical determinant identity or Barnes constant as new.

## value

PASS

The dimension-versus-bandwidth joint limit creates a real noncommuting-limits question for a natural zonal hemispherical spectral invariant; the exact crossover unifies fixed dimension and Hermite/high-dimension behavior, with a quantitatively uniform error rather than a finite sample or a parameter substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
