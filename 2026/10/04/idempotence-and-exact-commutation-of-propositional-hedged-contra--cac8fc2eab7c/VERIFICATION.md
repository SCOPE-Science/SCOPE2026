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

For propositional content with truth set \(P\), the published update acts on every accessibility row as
\[
c_P(S)=
\begin{cases}
S\cup(W\setminus P),&S\subseteq P,\\
S,&S\not\subseteq P.
\end{cases}
\]

The bundled checker exhaustively enumerates all subsets \(P,Q,S\subseteq W\) for carrier sizes through six. It verifies
\[
c_P(c_P(S))=c_P(S)
\]
for every row and verifies the exact universal criterion
\[
\forall S\subseteq W\;
 c_P(c_Q(S))=c_Q(c_P(S))
\quad\Longleftrightarrow\quad
P=Q\text{ or }P\cup Q=W.
\]

Whenever the right-hand condition fails, the checker confirms that the empty row is already a witness and that the two orders finish at the distinct sets \(P^c\) and \(Q^c\).

It also enumerates every pair of Boolean truth functions on up to two atoms and confirms that the universal set condition holds on every collection of propositional valuations exactly when the functions are equivalent or their disjunction is tautological.

The script prints `VERIFY_OK`.

## Limits

The finite replay corroborates the proof. The arbitrary-set theorem is proved directly. Modal contraction contents are not covered because their truth sets can change under the relation update.
