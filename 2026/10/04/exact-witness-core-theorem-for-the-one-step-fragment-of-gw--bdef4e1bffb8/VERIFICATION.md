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

The verifier uses the truth-value set

\[
Q=\left\{0,\frac12,1\right\}
\]

with Gödel implication.

For carriers of size at most three, it exhaustively enumerates every root accessibility vector

\[
R(w,-)\in Q^W
\]

and every one-step propositional-scope value vector

\[
v\in Q^W.
\]

Each modal specification is marked as either box or diamond. For every pair of such specifications, the verifier computes the original modal extrema and their complete witness sets.

It then checks every subset \(S\) containing the designated root and verifies the equivalence

\[
\text{all restricted modal values equal their originals}
\iff
S\text{ hits every witness set}.
\]

Because arbitrary atom valuations can realize every tested scope-value vector, this directly checks the semantic step used by the proof without assuming a special propositional formula shape.

The sharp family is checked separately for every

\[
1\le m\le12.
\]

For each \(m\), the verifier constructs a crisp root with \(m\) distinct successor witnesses and confirms that:

\[
E_{\Diamond p_i}=\{u_i\}
\]

for every \(i\);

\[
e(w,\bigwedge_i\Diamond p_i)=1;
\]

and deleting any \(u_i\) changes the conjunction value to \(0\).

The script prints `VERIFY_OK`.

## Limits

The exhaustive replay is corroborative only. The arbitrary finite-family theorem follows from the exact minimum/maximum argument for witnessed extrema. The checker does not test nested modalities, which are explicitly outside the theorem.
