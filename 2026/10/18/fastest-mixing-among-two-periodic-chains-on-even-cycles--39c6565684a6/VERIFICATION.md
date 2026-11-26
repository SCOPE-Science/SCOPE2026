---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Two-vertex Bloch cells give off-diagonal product Z=(c cos θ+2ir sin θ)^2+d^2 sin²θ at the first nonconstant mode, with c=a+b, d=a−b, θ=2π/N. For X=c² cos²θ and Y=(d²−4r²)sin²θ, |Z|²−(X−Y)²=4Xd²sin²θ, so the square root with nonnegative real part has real part at least c cos θ. The other spectral obstruction is the alternating eigenvector in the constant-cell block, with eigenvalue 1−2c. Their maximum bound has its unique minimum at c=2/(3−cos θ), and the homogeneous reversible spectrum attains it. For even N≥6, at this c the first bound is strict for d≠0 by the identity, and for d=0,r≠0 by the imaginary part. For N=4 the two nonconstant-cell eigenvalues are 1−c±√(d²−4r²), whose maximum modulus exceeds 1−c unless the discriminant is zero, whether it is real positive or negative. Balancing against |1−2c| yields exactly c=2/3 and d²=4r²; then |r|≤1/6. The example has nonconstant-cell block with diagonals 1/3 and off-diagonals 1/3,0, establishing geometric multiplicity one. The invariant mean-zero subspace counts extra eigenvalues 1 in reducible cases. The supplied SymPy identities and witness and 2275 finite grid iterations were inspected, not rerun; the grid does not prove an optimum on the continuous domain.

## originality

PASS

The optimal value itself is the known homogeneous benchmark. The distinct comparison is the global bound when alternating symmetric rates and constant circulation are simultaneously allowed, with the resulting rigidity for N≥6 and the defective equality family for N=4. No unrestricted global cycle optimum is asserted.

## value

PASS

Period two is the simplest nonconstant periodic symmetric environment in which circulation can interact with inhomogeneity. The sharp bound gives a tractable global case beyond the separate-perturbation and local comparisons. Its four-cycle exception provides a whole explicit family showing that even attainment of the optimal spectral modulus need not imply reversibility or diagonalizability; this distinction matters for finite-time behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
