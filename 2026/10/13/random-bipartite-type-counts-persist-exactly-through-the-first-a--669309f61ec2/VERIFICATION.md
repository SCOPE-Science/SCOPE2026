---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-18.md",
      "INDEPENDENT_AUDIT_2026-10-18.json"
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

In T_(m,n), complete types are classified by incidence-isomorphism of the algebraic closure of their marked tuple (Conant–Kruckman). At injective arity k=min(m,n), any mixed-sort tuple has fewer than m points and n lines and triggers no incidence closure. If m=k and the tuple consists of m points, exactly n-1 common lines are algebraically added; since n-1<n, no dual rule can trigger. The dual case applies if n=k; when m=n, both same-sort shapes are exceptional. Their unlabelled new common elements are unique up to marked incidence isomorphism, so the injective k-type count remains a_k=sum_p binom(k,p)2^[p(k-p)], while a_k-(1 or 2) types have trivial closure. Arbitrary equality patterns give sum_j Stirling2(k,j)a_j. Independent integer checks reproduced a_0..7, the Stirling transform, and the closure-size exception schema for all 49 pairs m,n in [2,8]. The finite checks are not a substitute for the model-theoretic closure theorem.

## originality

PASS

Conant–Kruckman establish the incidence-closure and marked-closure-isomorphism theory, including the exact m-point/n-1-common-line rule. They do not explicitly count complete types at k=min(m,n) in the inspected primary sections. The boundary enumeration follows simply but nontrivially from identifying a first algebraically nontrivial closure that nevertheless causes no type splitting. A related published extension-count result is a different finite-parameter problem, not coverage of the empty-parameter k-type count.

## value

PASS

The number of complete k-types and first nontrivial algebraic-closure threshold are natural invariants of this established family of generic K_mn-free incidence structures. The theorem gives a uniform exact count at the first arity where trivial-closure enumeration no longer applies, and a complete classification of the exceptional boundary type templates and their closure sizes. This is a useful first boundary in the finite-type census rather than an arbitrary finite slice. It does not pretend to solve all higher-arity types.

The dated certificate retains the supplied scientific assessment, sources and limitations.
