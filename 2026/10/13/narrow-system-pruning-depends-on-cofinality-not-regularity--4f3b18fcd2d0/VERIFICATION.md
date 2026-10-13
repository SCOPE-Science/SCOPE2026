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

The proof was checked from the definitions rather than by treating the regular theorem as a black box.

Define transfinite prunes \(T^\xi\) by retaining, at each successor stage, exactly those nodes whose cone in the current prune reaches every higher level. The sequence stabilizes before \(|T|^+\). If a nonempty stable prune existed, it would be a well-pruned subtree. Therefore, under the contrary assumption, every node has a least successor removal rank \(r(x)\).

For each node \(x\), removal at a successor stage gives a level \(\delta_x<\kappa\) such that every descendant \(y\) above that level satisfies
\[
r(y)<r(x).
\]

Let
\[
\theta=\operatorname{width}(S),
\qquad
\lambda_\theta=\max(\omega,\theta^+).
\]
The hypothesis
\[
\lambda_\theta<\operatorname{cf}(\kappa)
\]
is used exactly twice: first to keep the \(\lambda_\theta\)-stage recursion of indexed subsystem levels below \(\kappa\), and second to choose one indexed level above all of the resulting bounds.

At that common level, a node cannot lie above selected cones from infinitely many recursion stages, since that would give an infinite strictly descending sequence of ordinal removal ranks. Hence each node accounts for only finitely many stages. A subsystem level contains at most \(\theta\) nodes, so it accounts for fewer than \(\lambda_\theta\) stages, contradicting coverage of all \(\lambda_\theta\) stages.

Finally, applying the resulting escape property to the actual subsystem level \(S_\alpha\) contradicts the defining coherence of a subsystem.

## Limits

No claim is made when
\[
\operatorname{cf}(\kappa)\le\max(\omega,\theta^+).
\]

The sufficient cofinality threshold is not claimed optimal.

The argument concerns one-cardinal trees and does not automatically transfer to the source's two-cardinal setting.
