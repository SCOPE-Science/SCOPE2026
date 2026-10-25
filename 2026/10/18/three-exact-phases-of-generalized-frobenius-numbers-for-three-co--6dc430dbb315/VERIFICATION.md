---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-21.md",
      "INDEPENDENT_AUDIT_2026-10-21.json"
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

Reconstructed ordered nonnegative representation count using n=aq+r, s=x+y+z=q-t, and u=r+at=y+2z. At fixed t the exact count is floor(u/2)-max(0,u-(q-t))+1 for 0<=u<=2(q-t); zero otherwise. The injection (x,y,z)->(x+1,y,z) implies d(n+a)>=d(n), so checking the displayed candidate g_p has exactly p representations and each of its a immediate successors >p proves the infinite bound. Algebraic residue subcases in RESULT.md establish this in three regimes 0<=p<=floor(a/2), floor(a/2)+1<=p<=a+1, a+2<=p<=2a for all a>=3. An independent coin-change DP independently checked g_p and all larger values within the computed range for all 4,347 pairs (a,p), 3<=a<=65.

## originality

PASS

The first regime was published by Komatsu–Ying; the exact uniform next two regimes through p=2a are the assessed extension. Primary full-text Theorem 1 restricts its p-range, whereas other cited triple formula imposes a nonapplicable divisibility condition as a uniform theorem. Best-of-knowledge, not exhaustive historical priority.

## value

PASS

The extension determines precise linear-to-alternating phase transitions in a natural numerical semigroup invariant beyond an explicit range left open by the original theorem. Uniform all-a formulas are more informative than an arbitrary finite table, with transparent application to generalized Frobenius questions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
