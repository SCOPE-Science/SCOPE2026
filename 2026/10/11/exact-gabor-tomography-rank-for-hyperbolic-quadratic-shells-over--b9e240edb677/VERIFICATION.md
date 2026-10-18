---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-12.md",
      "INDEPENDENT_AUDIT_2026-10-12.json"
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

For odd prime power q and r>=2 on V=F_q^r+F_q^r, derive the level-set Fourier transform from orthogonality and completion of the square. On even nondegenerate sections at nonzero level, a sum of q-1 characteristic-p roots of unity cannot vanish (p does not divide q-1); on odd sections the Salié Fourier identity gives exact χ(cQ(w))=-1 zeros, or nonzero isotropic w when c=0. Intersect Q(x)=Q(x-a)=1: a=0 all coefficients survive; a nonzero isotropic yields B(a,b)=0 filter by free Witt coordinate; anisotropic t yields section a-perp with c=1-t/4 and w=b-(B(a,b)/2t)a. Reconstruct quadratic norm-fiber counts and sum χ(t(t-4))=-1 to obtain N+I q^(m-1)+J[C4+(q-2)C*-(q-1)q^r/2]. Weyl orbit conjugation diagonalizes complex-matrix lifting, making its rank ambiguity-support count and its kernel span zero-support Weyl matrices. Independent exhaustive mod3 residue-count implementation enumerated 6561 (q=3,r=2) coefficient pairs, exactly rank3393/nullity3168, including every shift/frequency; supports but does not prove all prime powers. All q odd and m>=4 boundaries accounted for; not a pure-state phase-retrieval theorem.

## originality

PASS

Best-of-knowledge original specific exact claim after theorem-level comparisons; detailed four checks and non-fabricated primary-source inspections follow. Search absence is not proof of priority, and significant prior-specialization risks are recorded.

## value

PASS

Exact complex operator lifting rank and every kernel direction for a canonical finite-field hyperbolic shell give a complete natural measurement-tomography classification over all odd prime powers and unbounded even dimension. The zero-strata arithmetic and nontrivial limit (q-1)(q+2)/(2q^2) are reusable and not merely numerical small-field tables.

The dated certificate retains the supplied scientific assessment, sources and limitations.
