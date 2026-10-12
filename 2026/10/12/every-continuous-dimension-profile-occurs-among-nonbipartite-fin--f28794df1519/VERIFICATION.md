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

For
\[
\mathcal H_d
=
\{H:F(2^{\mathbb Z^d})\longrightarrow_c H\},
\]
the primary source states
\[
\mathcal H_j\subseteq\mathcal H_i
\qquad(i<j).
\]

Therefore, for every fixed finite target \(H\), the set
\[
\mathcal D_c(H)=\{d\ge2:H\in\mathcal H_d\}
\]
is downward closed. A downward-closed subset of
\[
\{2,3,\ldots\}
\]
is empty, a finite initial segment, or the whole set.

The three realization checks are exact:

\[
K_3\notin\mathcal H_2,
\]
so nestedness gives
\[
\mathcal D_c(K_3)=\varnothing.
\]

For every
\[
D\ge2,\qquad L\ge4,
\]
Proposition 7.7 gives
\[
M_{D,L}\in\mathcal H_D\setminus\mathcal H_{D+1}.
\]
Nestedness gives membership in every earlier class and nonmembership in every later class, hence
\[
\mathcal D_c(M_{D,L})=\{2,\ldots,D\}.
\]

Theorem 1.4 applies to \(K_4\), giving
\[
K_4\in\mathcal H_d
\]
for every \(d\), hence the full profile.

Finally, in dimensions greater than one, the finite targets admitting Borel homomorphisms are exactly the nonbipartite graphs. The graphs \(K_3\) and \(K_4\) are nonbipartite, and every \(M_{D,L}\) with \(D\ge2\) is nonbipartite because it already receives a continuous, hence Borel, homomorphism in dimension \(D\).

No computation is used.

## Limits

The argument classifies possible profile shapes and realizes them, but does not decide the profile of an arbitrary input graph.

No minimal-order claim is made for the witnesses \(M_{D,L}\).

The Borel comparison is stated only for dimensions at least two.
