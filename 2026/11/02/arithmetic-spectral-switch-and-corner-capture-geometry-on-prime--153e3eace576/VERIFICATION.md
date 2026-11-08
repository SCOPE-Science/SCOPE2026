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

For Hermitian finite grid adjacency H with absorbing diagonal local loss of strictly positive rates, orthogonal complement of the absorber Krylov cyclic subspace is completely dark; any hypothetical real eigenvalue of the effective Hamiltonian inside the cyclic subspace forces vanishing absorber components, contradiction. Thus maximally mixed eventual capture is cyclic rank divided by (p-1)(q-1). Endpoint sine eigenvectors are nonzero at a corner; one-corner rank equals number of distinct a lambda_i^(p)+b lambda_j^(q). Cyclotomic elements u_r=zeta^r+zeta^(-r) have trace Gram matrix pI-2J, strictly positive eigenvalues 1 and p, hence rational independence; intersections of distinct-prime real cyclotomic fields are Q and for p>=7 differences between distinct path eigenvalues cannot be rational. Rational a/b therefore yields simple spectrum when primes differ. For equal primes the signed-basis representation gives simple spectrum for positive rational a/b !=1 and precisely 2d^2+1 energies when a=b. Endpoint parity makes opposite-corner projections collinear on each eigenspace while adjacent corner adds d^2-d+1 directions, giving 3d^2-d+2. Independent exact SymPy Krylov ranks on 4x4 and 4x6 agreed; original integer modular checker and CHECKS.txt were inspected. General-prime proof is cyclotomic, not numerical.

## originality

PASS

Best-of-knowledge originality qualified by primary literature, prior methods and named residual priority risks; the final evaluated theorem is not established or logically implied by the cited comparator statements.

## value

PASS

Determines exact asymptotic absorption for a natural whole family of prime-denominator product paths, revealing a sharp isotropic/equal-side dark-state obstruction, rational anisotropy full capture, and a striking difference between opposite and adjacent trap placement. The irrational sqrt5 resonance gives a meaningful boundary showing exactly why the theorem does not assume unrestricted real weights.

The dated certificate retains the supplied scientific assessment, sources and limitations.
