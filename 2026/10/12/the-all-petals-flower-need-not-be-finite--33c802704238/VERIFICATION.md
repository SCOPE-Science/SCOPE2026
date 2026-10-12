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

The source-dependent checks were made against arXiv:2609.27078v2.

Definition 3.4 makes every sprout finite but defines its height and width using strict modal chains and incomparable immediate successors. Neither parameter counts the number of points inside one reflexive modal cluster.

Definition 7.1 permits a canonical sprout homomorphism to map multiple sprout points to one canonical world.

Definition 8.2 extends the notation for grafting a family only when that family is finite.

Definition 12.1 imposes bounded height and width on an \(n\)-petal.

Proposition 12.3 sets
\[
\mathcal G=
\{\text{all \(n\)-petals over \(w\), up to isomorphism}\}
\]
and then writes
\[
A'=A\sqcup_w\mathcal G.
\]

The explicit family used for verification is
\[
B_m=
\text{an \(m\)-point reflexive modal cluster mapped constantly to \(\Psi\)}
\qquad(m\ge1).
\]

For every \(m\),
\[
\operatorname{hgt}(B_m)=
\operatorname{wdt}(B_m)=0,
\]
and all petal conditions are unchanged by increasing \(m\). Ordinary isomorphism nevertheless preserves
\[
|B_m|=m.
\]
Hence infinitely many isomorphism types occur.

Theorem 14.2's Kruskal encoding labels a modal cluster by the **set** of labels that occur in it. This can collapse repeated copies under the simulation order, but it is not a proof that the repeated-copy sprouts are ordinarily isomorphic.

## Limits

This verifies failure of the stated all-petals finiteness step.

It does not verify failure of Proposition 12.3 as a theorem, does not rule out a finite repair, and does not challenge the separate finite-model proof of \(\mathsf{IK4}\).
