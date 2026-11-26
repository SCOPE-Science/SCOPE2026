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

Column products decouple. For inputs (t,b) and (s,c), the witness equations are (t-s)u=0, (1-s)z=c-bu and (t-s)v=0, (1-t)w=b-cv. When neither scalar is 1, take u=v=0 and solve by division. When both are 1, the equations require reciprocal scalar multiples, equivalent to equal nonzero lines or two zero vectors. In the mixed case the diagonal-1 vector must vanish, which is also sufficient. All choices assemble into allowed witnesses. Thus the one-column star and line fibers have sizes 1+(q-1)q^d and q-1 respectively; line count is (q^d-1)/(q-1), and products give every class multiplicity. Squaring yields precisely t=0 with arbitrary b or (t,b)=(1,0) as idempotents. For q=2 this equals the star fiber; over any larger field diag(I,aI) for a not 0 or 1 disproves equality. As a bounded cross-check from actual block multiplication, K_{1,1} over F_3 has a seven-element star class (six t≠1 plus the identity) and one two-element class, with four idempotents. The counterexample X(0,2) and the identity are mutually intertwined by X(0,0). This check is additional to the universal algebraic argument; uploaded code was inspected but not executed.

## originality

PASS

The exact prior question and three strong nearby formulations were compared against the all-column partition with restricted witnesses. The evidence supports the specific star/projective-line classification and the idempotent-class answer for the stated family, not priority for Otto conjugacy itself or a solution of the other questions in Open Problem 7.5.

## value

PASS

The open problem asks for more than idempotents being mutually conjugate: the result identifies their full containing class, produces a counterexample over the original complex base, distinguishes the F_2 exception, and gives a uniform classification with class sizes for noncomplete as well as complete bipartite graphs. Dependence on the witness monoid makes this useful beyond a conjugacy calculation by units.

The dated certificate retains the supplied scientific assessment, sources and limitations.
