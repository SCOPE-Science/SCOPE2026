---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The proof was checked in three layers. First, the lower bound was replayed as a quantifier-rank-preserving syntactic translation from the exact undirected-cycle theorem using \(E(x,y)\equiv S(x,y)\lor S(y,x)\). Second, the upper-bound source proof was inspected at the path-coordinate step: the replies preserve signed offsets from matched endpoints, so an oriented edge, characterized by positive coordinate difference \(1\), is preserved after cutting the cycles at the first matched point. The cases \(q=1\) and \(q=2\) were checked separately.

The accompanying `verify.py` exhaustively solves the finite EF game for every \(1\le q\le4\) and every \(3\le m\le n\le12\). It checks equality and the directed successor relation after every response. Running it prints:

`VERIFY_OK cases=220`

This computation is not used as an infinite proof. It only stress-tests the exact closed form in a finite window. No independent external audit has been performed.
