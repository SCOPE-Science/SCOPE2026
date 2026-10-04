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

The verifier implements the Gödel-chain operations
\[
x\odot y=\min(x,y),
\qquad
x\to y=
\begin{cases}
1,&x\le y,\\
y,&x>y,
\end{cases}
\]
and checks the FARL and monadic axiom systems independently.

For
\[
2\le n\le4,
\]
it exhaustively enumerates every pair of unary maps
\[
f,g:G_n\to G_n.
\]
The set of FARL pairs and the set of monadic Gödel pairs are exactly equal.

For
\[
2\le n\le6,
\]
it exhaustively enumerates candidate right adjoints \(f\), reconstructs the unique possible left adjoint \(g\), and verifies that the FARL survivors are exactly the rounding pairs arising from endpoint-containing subsets.

For
\[
2\le n\le12,
\]
it constructs every subset
\[
F
\quad\text{with}\quad
\{0,1\}\subseteq F
\]
and verifies both axiom systems directly. The number of distinct expansions is
\[
2^{n-2}
\]
at every checked size.

To test the general theorem away from chains, the verifier also exhaustively enumerates every pair of unary maps on the four-element product Gödel algebra
\[
G_2\times G_2.
\]
Again the FARL and monadic Gödel survivor sets coincide exactly.

The script prints `VERIFY_OK`.

## Limits

Finite enumeration is corroborative. The theorem for arbitrary Gödel algebras follows from the symbolic axiom comparison and the established monadic Gödel common-image approximation theorem. No inference from finite cases to the general theorem is used.
