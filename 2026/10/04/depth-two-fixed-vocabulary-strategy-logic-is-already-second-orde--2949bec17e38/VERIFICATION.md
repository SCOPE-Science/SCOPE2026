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

The proof was verified directly from the primary reduction.

The fixed vocabulary appears before the reduction:
\[
\mathrm{Ag}=\{a_1,a_2,a_3,b,c\},
\qquad
\mathrm{AP}=\{p_b,p_c,p_S,p_A,p_M\}.
\]

The auxiliary testing formulas use one \(X\); the independence formulas and the outer test \(L\) use at most \(XX\).

Membership is
\[
\mathrm{Mem}(Y,x)=B(x,e,e,Y,e)XXp_b.
\]

The three arithmetic relation encodings use
\[
Xp_S,\quad Xp_A,\quad Xp_M.
\]

Equality is obtained by quantifying over membership tests, and the second-order arithmetic translation introduces only strategy quantifiers and Boolean connectives. Therefore it does not increase temporal depth.

The final Boolean-goal prenex conversion changes only strategy-quantifier placement. The injectivizing padding uses the propositional tautology
\[
p_c\leftrightarrow p_c.
\]

Hence every lower-reduction output has temporal depth at most \(2\) and remains in the fixed five-agent/five-proposition vocabulary.

The source's Proposition 3.1 supplies an injective upper translation for all Strategy Logic formulas; restricting its domain preserves injectivity. Myhill's theorem therefore applies to the restricted satisfiability set.

## Limits

The verification establishes an upper bound of \(2\) on temporal depth for the hard reduction. It does not prove that depth \(1\) is easier.

No claim is made about fixing the action set to a finite size or about reducing the number of agents or propositions.
