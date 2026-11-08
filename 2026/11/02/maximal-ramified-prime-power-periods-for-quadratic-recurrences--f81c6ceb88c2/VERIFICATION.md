---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-07.md",
      "INDEPENDENT_AUDIT_2026-11-07.json"
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

Companion matrix A is cyclic on e1, so sequence period equals matrix order. Mod p the nonscalar repeated-root A=alpha I+J yields ord(A)=m p. B=A^m−I has B nonzero, B²=0 mod p; (I+B)^p=I+pB mod p² since p>=5 gives B^p=0 mod p². This forces exact first and higher lifts by binomial induction. Under Y=X−1, any monic factorization of X^p−1 with both degrees >=2 has linear coefficient divisible by p², whereas target has coefficient p. The p=3 cyclotomic factor is an explicit exception. Independent modular companion powers checked 108 cases p=5,7,11,13 for k=1..3; finite checks are not proof.

## originality

PASS

Best-of-knowledge statement/implication comparison finds no inspected stronger result covering the full final claim; known components and related earlier theorems are credited. This is not a novelty certificate.

## value

PASS

The repeated-root branch of a current prime-period construction is a canonical arithmetic case; a complete prime-power answer and failed non-coprime Hensel lift are mathematically useful, with a sharp characteristic-three boundary. It corrects a specific proposed coding-theory construction rather than a randomly chosen case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
