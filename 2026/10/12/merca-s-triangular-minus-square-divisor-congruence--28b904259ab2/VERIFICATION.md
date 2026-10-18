---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

Let N=8n+1. Since tau(N)=product(e_p+1), v_2(tau(N))<=1 implies either every exponent even, hence odd square N=(2m+1)^2 and n=T_m, or precisely one odd exponent, e_p≡1 mod4, and N=p^(4a+1)v². Modulo 8 forces p≡1 mod8. Quadratic reciprocity (2/p)=1 and the Euclidean norm property of Z[sqrt2] (nearest integer error norm <1) show p splits as p=A²−2C², with C even by mod8, hence p=A²−8B². Scaling by p^(2a)v yields N=X²−8Y² with odd X and desired n=T_m−Y²; signs normalized. Own factor/exponent checks for n<3000 and explicit small norm-prime witnesses corroborate both branches; no finite check used to prove all n.

## originality

PASS

Best-of-knowledge statement-level novelty of the surviving claim after crediting overlap in actual primary texts; not a universal priority certificate. Matching conjecture statement establishes relevance, not prior proven coverage; this proof is an answer to the original question. No inspected stronger theorem implies the exact τ(8n+1) representation implication. Closely titled papers need scientific content comparison, not title match. This nontrivial combination settles that stated conjecture; no source found with the implication already fully proved. The norm lemma is not itself novel.

## value

PASS

This resolves an explicitly published pointwise divisor-congruence conjecture in full generality using a structural prime-exponent classification and a quadratic norm bridge. The exact link between tau(8n+1) modulo 4 and triangular-minus-square representation is a natural nontrivial arithmetic problem, beyond finite OEIS observations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
