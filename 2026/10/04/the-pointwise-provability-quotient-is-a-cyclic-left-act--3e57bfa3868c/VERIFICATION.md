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

The proof is symbolic and was checked against the source's exact arithmetized composition law.

The source defines
\[
e\equiv_T d
\iff
T\vdash\forall x\,E_{e,d}(x)
\]
and
\[
e\approx_T d
\iff
\forall n\in\omega,\ T\vdash E_{e,d}(\bar n).
\]

The first implication checked is
\[
\equiv_T\subseteq\approx_T.
\]

The formalized graph equation
\[
C_{f\bullet g}(x,z)
\leftrightarrow
\exists y\,
\bigl(C_g(x,y)\wedge C_f(y,z)\bigr)
\]
then permits a single universal equality proof to be substituted in either program position. This verifies that \(\equiv_T\) is a two-sided composition congruence.

The source separately proves the weaker pointwise implication
\[
g\approx_T h
\Longrightarrow
f\bullet g\approx_T f\bullet h.
\]
This is exactly the left-congruence law after quotienting by \(\equiv_T\).

Associativity and identity are checked at the uniform graph level, so the action law follows without choosing representatives.

For the recursively enumerable consistent case, the source's obstruction pair satisfies
\[
f\approx_T\mathrm{id}
\]
but
\[
f\bullet g\not\approx_T\mathrm{id}\bullet g.
\]
This simultaneously verifies that the induced left congruence is not right-compatible and that \(f\) cannot already be uniformly equal to the identity.

The nontriviality check uses the identity program and a program with provably empty graph.

The final boundary is exactly the source's Theorem 3: for consistent \(T\), full composition congruence is equivalent to proving every true \(\Pi^0_1\) sentence.

## Limits

No finite computation is offered as a substitute for the proof-theoretic argument. The verification does not establish faithfulness of the action and does not analyze higher-arity object types.
