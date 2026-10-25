---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-22.md",
      "INDEPENDENT_AUDIT_2026-10-22.json"
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

For nonerasing Psi on finite nonempty Sigma+, Phi(a_i)=a_i^{N_i}, commuting generator identity Phi(w_i)=w_i^{N_i} and preservation of maximal constant-letter runs force a monomial image when N_i>1, with target letter at the same exponent level. For N_i=1, length positivity forces an arbitrary word solely in exponent-one letters. If Psi^k=Phi, Psi commutes with Phi; the exponent-one block images must have length one by nonerasing monotonicity. Thus all images are weighted letters, the finite letter map f obeys f^k=id and is a permutation with cycles d|k; each cycle has weight-product p with p^(k/d)=m. Ordered factorization count D_d(p)=prod_{prime^v||p} binom(v+d-1,d-1) and labelled exponential cycle-index provide exact formula. Tested small two-letter profiles independently by enumerating nonerasing compositions; (2,2),k=2 has two roots and (4,4),k=2 has four, in agreement with the classification. Universal proof is textual, not inferred from finite tests.

## originality

PASS

Best-of-knowledge statement-and-implication comparison; not a priority certificate. A full paper and targeted Resultary search were inspected as described below.

## value

PASS

Complete centralizer classification for an infinite family of free-semigroup endomorphisms and a finite exact count of k-th roots inside an infinite endomorphism monoid. The exponent-one free-morphism block and weighted permutation cycle constraints expose genuinely structural behavior. The theorem answers naturally motivated composition and factorization questions, unlike a routine evaluation of a pre-known numerical table.

The dated certificate retains the supplied scientific assessment, sources and limitations.
