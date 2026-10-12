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

For a numerical semigroup \(H\), the strict upper cone in
\[
P_H(x,y)\iff x\le y\text{ and }y-x\in H
\]
is
\[
\operatorname{Up}_{<_{P_H}}(x)=x+H_+.
\]

If \(y<x\), let \(m\) be the least positive element of \(H\). Then \(y+m\) lies in the upper cone of \(y\), while its displacement from \(x\) is strictly below \(m\) and is therefore not in \(H_+\). Hence Jagiella's reverse upper-cone inclusion cannot hold.

If \(d=y-x\ge0\), then
\[
\operatorname{Up}(y)\subseteq\operatorname{Up}(x)
\quad\Longleftrightarrow\quad
 d+H_+\subseteq H_+.
\]
For \(d\in H\), this is additive closure. For a gap \(d\notin H\), it is exactly the pseudo-Frobenius condition. Thus
\[
(P_H)^+=P_{H\cup\operatorname{PF}(H)}.
\]

The checked numerical-semigroup source states that adjoining pseudo-Frobenius numbers preserves numerical-semigroup structure. Induction therefore identifies every subsequent preorder stage with the corresponding repeated pseudo-Frobenius saturation.

At any nonterminal stage, the Frobenius number is pseudo-Frobenius, so at least one gap disappears. The iteration therefore reaches \(\mathbb N\) in at most the initial genus. Since exactly \(t(H_i)\) gaps disappear in round \(i\), telescoping gives
\[
g(H)=\sum_{i<\ell(H)}t(H_i).
\]

## Limits

No finite experiment is used to infer an infinite statement.

The stagewise identity is verified only for exact translation-invariant representatives \(P_H\), not arbitrary finite perturbations.

The pseudo-Frobenius saturation here is not identified with MED closure or with the separate Apery-saturation process from the supporting semigroup paper.
