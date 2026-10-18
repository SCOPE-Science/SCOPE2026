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

For T a 3×3 matrix commuting with diag(1,λ,λ), solve [Tx,Ty]_λ=T([Tx,y]_λ) on all ordered basis pairs. λ=0 gives block a⊕M2 with q^5 points. For λ≠0,1 the remaining equations a(p−t)=p(t−a)=0, v²=0 give q(2q−1)+2q(q−1)=4q²−3q. For λ=1, u=v=0, bi=di=i(a−e)=0 and bd=a(e−i), which split into singular 2×2 A at i=0 and A=0 or iI at i≠0, yielding q^5+q^4+q^3−2q². Independently enumerated all 3×3 matrices and checked rank profiles over F2 and F3, including char2; all five (q,λ) cases match formulas. Rank and zeta identities follow from disjoint strata for all fields.

## originality

PASS

Same adjoint embedding-tensor axioms as Das–Makhlouf, but their inspected general paper does not provide this concrete Heisenberg/Yau-twist exceptional-fiber classification or finite-field rank distributions. The closest Heisenberg Hom-Lie article addresses current representations and extensions; 2025 averaging work classifies graded q-Witt instead.

## value

PASS

The Heisenberg algebra is the canonical smallest nonabelian nilpotent Lie algebra. Exact solution of all adjoint embedding tensors across the natural Yau parameter, two exceptional q^5-scale jumps, rank strata and zeta functions gives a complete motivated classification and arithmetic invariant, not just a renamed general tensor definition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
