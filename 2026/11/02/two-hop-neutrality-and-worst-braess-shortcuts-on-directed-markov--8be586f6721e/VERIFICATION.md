---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-06.md",
      "INDEPENDENT_AUDIT_2026-11-06.json"
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

For L=-Q, the characteristic polynomial det(zI+L(0))=Π(z+r_i)-Πr_i; rank-one determinant lemma with the unique k→0 chain gives the cofactor difference. Expanding the linear and quadratic z coefficients gives a1=P[S+(t/r0)B], a2=P[E2+(t/r0)(e2(B)+AB)], and the irreducible CTMC guarantees eigenvalue 0 simple and all other eigenvalues Re>0, so H=Σ1/λ=a2/a1. Differentiation yields sign CS-BE2 independent of t. At equal rates, the difference is t(n-k)(k-2)/[2(n+t(n-k))]. Maximizing g_t(y)=y(n-2-y)/(n+ty), y=n-k, gives a unique positive real critical y_c and adjacent-difference sign n(n-2y-3)-t y(y+1), therefore exact discrete tie threshold and monotone worst-chord index. Independently built rational SymPy matrices and compared det(zI+L) coefficients for all n3..6, all chords, symmetric and nonuniform rates, t=0,1/2,3; every case matched exact formula. The unlimited-rates conclusion rests on the determinant and calculus proof.

## originality

PASS

Exact claims were contrasted with primary mathematical results, aliases, stronger scope, and published semantic records; no inspected source logically implies the final exact claim, subject to explicitly logged residual risks.

## value

PASS

Provides a complete all-rate sign criterion and a surprising exact two-hop neutrality/worst-chord transition for a simple natural continuous-time Markov graph. It distinguishes integrated relaxation from spectral gap and supplies a sharp analytically solvable Braess benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
