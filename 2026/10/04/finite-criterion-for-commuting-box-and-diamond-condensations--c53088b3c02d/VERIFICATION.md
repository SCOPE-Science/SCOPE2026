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

The proof reduces the interaction to relation composition:
\[
\beta(\delta(R))
=
R\circ\leq^{-1}\circ\leq,
\qquad
\delta(\beta(R))
=
R\circ\leq\circ\leq^{-1}.
\]

The two middle relations mean “has a common lower bound” and “has a common upper bound.” If they coincide, their common relation is proved directly to be transitive and hence an equivalence relation; its classes are exactly comparability components. Finiteness then upgrades pairwise common upper and lower bounds to a greatest and least element in every component.

The bundled `verify.py` exhaustively enumerates every labelled poset on at most four points and checks this criterion. For every labelled poset on at most three points it also enumerates every binary relation and checks universal commutation directly.

It verifies that, in the commuting cases, the common result is the component saturation \(R\circ E\), is fixed by both operators, and preserves both p-conditions whenever the input relation has both.

The script prints `VERIFY_OK`.

## Limits

The checker is corroborative. The arbitrary finite theorem follows from the relation-algebra proof. No full-bimodal truth-preservation theorem is claimed.
