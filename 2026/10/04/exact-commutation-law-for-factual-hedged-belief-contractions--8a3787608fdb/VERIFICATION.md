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

For a factual truth set \(X\subseteq W\), the update on one accessibility row is
\[
C_X(S)=
\begin{cases}
S\cup X^c,&S\subseteq X,\\
S,&S\not\subseteq X.
\end{cases}
\]

The proof checks idempotence directly and establishes
\[
C_XC_Y=C_YC_X
\quad\Longleftrightarrow\quad
X=Y\ \text{or}\ X\cup Y=W
\]
as an identity of maps on \(\mathcal P(W)\). The noncommuting direction is witnessed by the empty row.

The bundled `verify.py` exhaustively tests all triples \((X,Y,S)\) for carriers of sizes \(1\) through \(7\). It separately counts commuting ordered pairs through carrier size \(8\) and checks the closed form \(2^N+3^N-1\). It also confirms the propositional counts \(12,96,6816\) for one, two, and three variables.

## Limits

The checker is corroborative. The proof, not the finite enumeration, establishes the general set-map theorem. The result does not cover modal contraction inputs.
