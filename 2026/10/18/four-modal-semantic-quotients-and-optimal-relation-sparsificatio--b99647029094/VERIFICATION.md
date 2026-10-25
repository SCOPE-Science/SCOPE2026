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

Every upset in W_n={0<...<n-1} is U_j={j,...,n-1}; empty upset j=n is included. For any R, define h_i=max row or -1 if empty and ell_i=min row or n if empty; membership and subset tests of each row in U_j reduce respectively to h_i>=j and ell_i>=j. The four modal clauses then reduce exactly to P_s=max_{i<=s}h_i, Q_s=min_{i>=s}h_i, E_s=max_{i<=s}ell_i, D_s=min_{i>=s}ell_i. Equality of all four profiles is necessary from one-step tests and sufficient by full structural induction for all formula nesting, both Heyting implications and same persistent valuation. The H_i,L_i boundary/jump constraints ensure one can independently select each extrema pair (empty sentinel (n,-1) or 0<=ell<=h<n) and reconstruct prefix/suffix sequences; independent minimal row costs are 0,1,2, giving sum_i min c and <=2n. Relation with each row {0,n-1} forces two arrows in every row for n>=2; n=1 maximum one. Independent raw enumeration of all 2^(n^2) relations for n=1..4 computed the four direct quantified modal truth tables, exactly 2,16,279,7171 semantic classes and sharp minima 1,4,6,8. Independent enumeration of all 16^5=1,048,576 endpoint row tuples for n=5 produced 235152 distinct classes with maximum minimum 10, not a claim to exhaust all 2^25 raw relations. These exhaustive finite checks corroborate but do not replace the general induction/rowwise reconstruction.

## originality

PASS

Best-of-knowledge PASS for a complete fixed-finite-chain pointwise quotient and exact 0/1/2 outgoing-edge minimization. Modal transformer clauses are prior work. Related published chain confluence normal forms restrict the accessibility relations and address different equivalences/counts; no direct implication of this unrestricted four-transformer signature found. Full initiating paper could not be accessed, preserved as explicit coverage risk rather than whole-document negative claim.

## value

PASS

Exact semantic compression of arbitrary accessibility relations on finite intuitionistic chains is an intrinsically motivated structural classification. A fully testable realization criterion and classwise optimal outgoing-arrow count reduce an n²-entry relation to at most 2n arrows without changing any formula truth; the universal bound and finite quotient enumeration are mathematically useful independent of further model theory.

The dated certificate retains the supplied scientific assessment, sources and limitations.
