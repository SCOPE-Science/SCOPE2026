---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

Natural order antisymmetry gives zerosumfreeness, while no zero divisors yields a Boolean support semiring homomorphism h(s)=1_{s!=0}. This inductively converts finite semiring truth support to ordinary FO satisfaction. Let phi_n be the finite classical extension-closed but not Sigma_n definable sentence from Dawar–Sankaran; psi_n is a disjunction of r copies. By uniform saturation, value(psi_n) is t if phi_n holds and 0 otherwise. Since each nonzero s<=t in natural order, 0<=t and extension-closed support makes psi_n semiring extension preserved. If semiring equivalent to a Sigma_n formula, testing canonical 0/1 annotations and applying h would make phi_n classically Sigma_n-definable, contradiction. For S_k operations a⊕b=min(k,a+b), a⊗b=min(k,ab), zero divisors are absent and k-fold positive sums equal k; S_2 is non-idempotent (1⊕1=2). Domain finiteness and nonemptiness are essential. Independently checked source proof steps and algebra, with no attempt to turn small finite source tests into the unbounded theorem.

## originality

PASS

Direct material from Brinke–Dawar–Grädel–Pago 2026 distinguishes a positive finite result for three-element min-max lattice semantics and failures on infinite N from the finite capped-counting semiring. Dawar–Sankaran proves only classical hierarchy input; semiring preservation requires the extra 0/t saturation argument. No prior source read gives this non-idempotent finite S_2 instance or all-level lifting. Best-of-knowledge with residual older support-semirings equivalence risk.

## value

PASS

The three-element capped-counting counterexample draws a sharp mathematical boundary between equal-sized semirings with different additive idempotence: min-max lattice has finite extension preservation, capped counting does not at any bounded prefix level. The uniform saturation-transfer lemma is a usable structural mechanism across a class of semirings, beyond a one-off numerical example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
