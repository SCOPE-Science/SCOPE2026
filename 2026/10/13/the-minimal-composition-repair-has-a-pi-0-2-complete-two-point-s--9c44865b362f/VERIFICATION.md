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

For each program index \(e\), set
\[
T_e
=
\mathrm{PA}
+
\{\exists s\,T_1(\bar e,\bar n,s):n\in\omega\}.
\]

The added sentence for \(n\) is true exactly when
\[
\varphi_e(n)\downarrow.
\]

If
\[
e\in\mathrm{TOT},
\]
every added axiom is true. Hence every theorem of \(T_e\) is true in the standard natural numbers, so \(T_e\) is \(\Sigma^0_1\)-sound. Lengyel's Theorem 4 yields
\[
\sim_e=\{(a,b):\varphi_a=\varphi_b\}.
\]

If
\[
e\notin\mathrm{TOT},
\]
some added axiom is a false \(\Sigma^0_1\) sentence. Thus \(T_e\) is not \(\Sigma^0_1\)-sound, and the same theorem yields
\[
\sim_e=\omega\times\omega.
\]

Therefore the repair endpoint is extensional exactly on
\[
\mathrm{TOT}.
\]

For the complexity statement,
\[
e\in\mathrm{TOT}
\Longleftrightarrow
(\forall n)(\exists s)\,T_1(e,n,s),
\]
which is \(\Pi^0_2\). Given any computable \(R\) and predicate
\[
k\in P
\Longleftrightarrow
(\forall n)(\exists s)\,R(k,n,s),
\]
uniformly construct a program that on input \(n\) searches for an \(s\) satisfying \(R(k,n,s)\). It is total exactly when \(k\in P\). Hence the extensional endpoint is \(\Pi^0_2\)-complete and the collapsed endpoint is \(\Sigma^0_2\)-complete.

## Limits

No consistency hypothesis is used.

No finite experiment is used to infer an infinite statement.

The conclusion concerns the generated unary composition congruence and the displayed uniform family only.
