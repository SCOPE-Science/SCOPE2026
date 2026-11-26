---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The primary source confirms the WNM and Nelson equations and both recovery definitions. On a chain, WNM forces product either zero or min, with the zero cut given by d(y)=y→0. Conversely weak negation gives the symmetric condition x≤d(y) iff y≤d(x), so a triple product is nonzero precisely when every pair passes the nonzero cut, and then equals the triple minimum. This verifies associativity and the displayed residuum follows by maximizing the allowed argument. For Nelson only x>y with x≤d(x) needs a check. If d(y)=d(x), the second conjunct is top and exceeds x→y=d(x); if d(y)>d(x), then d(d(y))≤d(d(x))≤d(x)<d(y), so the square of d(y) is d(y) and the conjunct equals d(x). Thus the stated consecutive strictness criterion suffices and is necessary. With r=d(1), if r<n−2 the penultimate point must map to zero and can be deleted (renaming top), preserving all interior inequalities. If r=n−2 and n≥4, d(n−2) must equal 1: a larger value would repeat r on the initial increasing-index segment x≤d(x), violating strictness. Restriction to [1,n−2] and subtraction of one then gives the n−2 case, with the inverse obtained by adjoining new outer bounds. Distinct negations cannot be identified by an order automorphism; the two branches give the Fibonacci recurrence with bases 1 and 2. The support of positive d on the nonzero elements ends at r, so exactly n−2−r interiors have defect. For fixed r>0 strip penultimate zeros until size r+2, then use the paired branch, with r=1 handled at size three; r=0 gives a single map. The limit follows from Fibonacci ratios and the stated moments are those of the limiting geometric distribution, not an assertion of moment convergence for the finite laws.

## originality

PASS

Existing representation theorems and chain recovery formulas are credited, not claimed new. The closest Resultary record has the very same Fibonacci coefficient profile under reindexing and the same limiting law for another chain class and another statistic, but no identified algebraic implication yielding the PQN census or recovery defect. The supported contribution is the structural PQN enumeration by recovery defect, not novelty of the Fibonacci or geometric laws as numerical patterns.

## value

PASS

The algebras and operators are fixed by an existing logic, and the prevalence of dual versus nondual recovery is a natural structural question. The finite classification is strong enough to predict how often every defect occurs, including the unique extreme defect and the bounded typical defect at large size. Its contribution is the intrinsic chain decomposition and exact census for these operations; the subsequent Fibonacci limit calculation, taken alone, would not meet the value bar.

The dated certificate retains the supplied scientific assessment, sources and limitations.
