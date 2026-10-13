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

Define \(\mathsf{PC}(\lambda)\) for regular uncountable \(\lambda\) by
\[
\mathsf{PC}(\lambda):
\quad
\text{every \(\le\!\lambda\)-generated \(\lambda\)-projective module over every ring \(R\) with \(|R|<\lambda\) is projective.}
\]

Assume \(V=L\) and let \(\kappa_*\) be the first weakly compact cardinal.

Calderoni--Yanowitz Theorem 1.1 gives
\[
\mathsf{PC}(\kappa_*).
\]

For a regular uncountable
\[
\lambda<\kappa_*,
\]
Shelah--Strüngmann construct an abelian group
\[
G=\bigcup_{\alpha<\lambda}G_\alpha
\]
of cardinality \(\lambda\), where the chain is increasing and continuous and every \(G_\alpha\) is free of cardinality below \(\lambda\). Their final group is indecomposable.

Hence the chain is a \(\lambda\)-filtration by projective \(\mathbb Z\)-modules. Calderoni--Yanowitz Proposition 2.7 gives
\[
G\text{ is }\lambda\text{-projective}.
\]

If \(G\) were projective over \(\mathbb Z\), then it would be free. An uncountable free abelian group has basis size greater than one and therefore splits nontrivially by partitioning its basis. This contradicts indecomposability. Thus
\[
G\text{ is not projective}.
\]

Because
\[
|\mathbb Z|=\aleph_0<\lambda,
\]
the group \(G\) is a counterexample to \(\mathsf{PC}(\lambda)\).

Therefore
\[
\kappa_*
=
\min\{\lambda:\lambda\text{ is regular uncountable and }\mathsf{PC}(\lambda)\}.
\]

## Limits

The lower-bound construction uses \(V=L\).

Only regular uncountable cardinals are classified.

No computation, enumeration, or experimental evidence is used.
