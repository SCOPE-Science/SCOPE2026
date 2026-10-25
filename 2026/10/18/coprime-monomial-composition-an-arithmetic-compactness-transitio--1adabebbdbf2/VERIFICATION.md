---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-19.md",
      "INDEPENDENT_AUDIT_2026-10-19.json"
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

Beta integration gives w_n=Gamma(alpha+2)n²Gamma(n)/Gamma(n+alpha+1), and monomial C_m maps e_n to sqrt(w_mn/w_n)e_mn. Noncoprime g=gcd(m,k)>1: choose n=(m/g)j with g not dividing j; m not divide n yet m divides kn, so infinitely many orthogonal columns have norms approaching (mk)^((1-alpha)/2)>0, obstructing compactness. For coprime degrees the sparse difference maps e_mj to Delta_j e_kj and vanishes elsewhere, with Delta_j=w_mkj/sqrt(w_mj w_kj)-sqrt(w_mj w_kj)/w_j. Gamma ratio expansion w_n=Gamma(alpha+2)n^(1-alpha)(1-alpha(alpha+1)/(2n)+O(n^-2)) yields Delta_j=-[alpha(alpha+1)/2](m-1)(k-1)/(mk)*(mk)^((1-alpha)/2)/j+O(j^-2). Orthogonality implies the singular multiset is |Delta_j|; rearrangement gives s_n~Lambda/n and summable perturbation of harmonic series gives log partial sums Lambda log N+O(1), Schatten p>1, normalized Dixmier trace Lambda. For alpha=0, w_n=n and coprime Delta=0 exactly. I independently computed Delta_j with exact rational w_n=2n/(n+1) at alpha=1,m=2,k=3 for j=10,100,1000,10000; j Delta_j tends to -1/3 as claimed.

## originality

PASS

Best-of-knowledge the full quantified final claim is not shown covered by the inspected primary statements, including aliases/stronger-theorem comparisons. The full 2011 Theorem 4.1 is a one-symbol self-commutator spectral law and does not entail the distinct-degree arithmetic compactness or weighted singular residue. Possible stronger material in unread full text remains a residual risk; its accessible statements do not logically imply the mixed-degree cancellation law. These spectral analogues involve different symbols/operators, not a database containing Lambda(alpha;m,k); search failure is not novelty proof. Setting m=k in this theorem yields NONcompactness rather than a weak-trace transition, so the earlier diagonal/self-commutator statements cannot imply the off-diagonal gcd dichotomy without additional work. Inaccessible relevant full text is explicitly a residual risk; absence from a database alone is not novelty proof.

## value

PASS

The exact gcd-driven compactness transition for mixed products of individually noncompact monomial composition operators and sharp weak-trace residue are natural operator-theoretic invariants. The alpha=0 cancellation identifies an exceptional Dirichlet normalization, and the 1/n tail resolves a meaningful trace-class boundary.

The dated certificate retains the supplied scientific assessment, sources and limitations.
