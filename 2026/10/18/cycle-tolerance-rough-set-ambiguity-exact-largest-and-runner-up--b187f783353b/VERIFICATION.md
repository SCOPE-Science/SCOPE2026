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

For the same reflexive closed-neighborhood relation in both approximations, the two-bit de Bruijn states give a bijection from labeled inputs to indexed closed walks, including on the triangle. The three observation matrices count all fibers by trace. On complement-symmetric states the uncertain transition has characteristic polynomial t^2-t-1, and on antisymmetric states t^2+t+1, yielding the Lucas plus period-three central count. The endpoint generating functions, obtained by projecting onto these same two subspaces, give a_t+b_t=F_{t-1} (t>=1) and a_t-b_t=delta(t). The maximum endpoint entry f_t is supermultiplicative by concatenation and complement symmetry. Inserting the rank-one definite projectors factors any noncentral fiber into endpoint entries with total gap length n-r for r definite symbols. For n>=7, monotonicity after t=2 and f_0=1 bound every r>=2 fiber by f_{n-2}<a_{n-1}; the difference is positive at n=7,8,9 and the Fibonacci term dominates thereafter. Exactly the 2n one-definite observations realize a_{n-1}, below the central trace. For n<=6 the r=1 endpoint counts through t=5 and the r>=2 bounds through t=4 are at most one. Binet asymptotics give the stated ratio. Separate direct aggregation by cyclic triple for n=3..16 (131064 inputs, 37596 realized outputs) reproduced both rankings and all equality patterns. At the endpoints n=7 and 16 the runner-up counts are 3 and 189 with respectively 14 and 32 attaining outputs. Frozen replay reference: verify.py beside RESULT.md, inspected but not executed; the independent enumeration counts input subsets by observed bit-pair and does not stand in for the unbounded proof. The Finding's prose 'four fixed ... matrices' is an editorial slip: the displayed valid formula uses three fixed matrices of size four.

## originality

PASS

Pass for the exact ranked multiplicity theorem, especially the runner-up value, strict gap and equality class on labeled cycles. The central cyclic-word enumeration and the rough-approximation formalism are ingredients, not separate originality claims. No inspected precedent supplies the ranking on this observation map.

## value

PASS

A closed-neighborhood rough observation deliberately forgets local membership. The exact worst and second-worst inverse ambiguities, the strict separation from every multi-definite output, and the complete equality class give sharp uncertainty benchmarks on a natural graph family. This goes beyond counting familiar restricted binary words: the endpoint analysis identifies which noncentral observations are hardest to resolve.

The dated certificate retains the supplied scientific assessment, sources and limitations.
