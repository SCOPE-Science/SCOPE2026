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

Index factors with >=2 ones by first consecutive square gap 2k+1 and leading-zero budget B_0=0, B_k=2k-2; reverse pairs only occur among exactly-two-one factors with both outside zero budgets feasible. Counting N_k and reversals C_k yields even contribution min(m-k,2k-1), sum 2+floor((m+1)^2/3), and odd increment 1. All-zero/isolated-one classes and n=0,1 handled separately; ordinary factor asymptotic n²/8 gives limit 2/3. Independent direct finite-prefix factor/reversal census checked every n=2..100, corroboration not infinite proof.

## originality

PASS

Definition/theory of reflection complexity is established, but the exact periodicity-unrelated *perfect-square characteristic word* counting formula requires increasing unequal square gaps and a special reversal-pair census, not automatic-sequence reflection results.

## value

PASS

Reflection complexity is a natural recently studied invariant; obtaining a full-length explicit formula and a nontrivial 2/3 asymptotic ratio for the sparse squares word supplies a standalone exact example outside standard automatic-word classes.

The dated certificate retains the supplied scientific assessment, sources and limitations.
