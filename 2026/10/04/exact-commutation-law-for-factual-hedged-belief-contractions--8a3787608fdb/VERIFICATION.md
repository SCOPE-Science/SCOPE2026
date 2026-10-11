---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

For a fixed factual truth set X, one row is updated by C_X(S)=S union X^c when S is contained in X and is otherwise fixed. Idempotence follows immediately. If X=Y or X union Y=W, a complete rowwise case split gives commutation. Conversely, if X differs from Y and their union is not W, the empty row yields X^c in one order and Y^c in the other. The propositional universal criterion follows by combining a valuation where the formulas differ with one where both are false. Inclusion-exclusion counts equal pairs and covering pairs as 2^N+3^N-1 for N=2^n. A fresh independent exhaustive check through five-world carriers reproduced the iff law.

## originality

PASS

Belardinelli--Zhang introduce the row-expansion contraction and study its one-step logical properties and event composition, but the checked public full-text material/searches did not surface the exact factual pairwise commutation theorem or census. The audited theorem reduces the operator to an exact set map and classifies its semigroup interaction; no stronger checked contraction theorem implied the iff condition.

## value

PASS

Commutation and idempotence are natural structural questions for iterated belief change. The exact universal criterion sharply separates compatible factual contractions and the census quantifies how rare noninteraction becomes over finite propositional vocabularies; this is a reusable algebraic property of the new operator rather than a cosmetic reformulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
