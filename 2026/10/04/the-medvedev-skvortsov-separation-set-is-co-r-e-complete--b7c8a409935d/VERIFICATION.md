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

The proof was checked at the level of exact logical equivalences.

For the upper bound:

\[
\mathrm{ML}\in\Pi^0_1
\]
because the primary source states that refutability in \(\mathrm{ML}\) is recursively enumerable.

Also,
\[
\mathrm{Form}\setminus\mathrm{Skvo}\in\Pi^0_1
\]
because \(\mathrm{Skvo}\) is recursively axiomatizable.

Their intersection is therefore \(\Pi^0_1\).

For the lower bound, fix a finite strongly aperiodic Wang tileset \(A\). The product construction uses ordered-pair edge colors. Projection and coordinatewise pairing prove
\[
W\otimes A\text{ tiles}
\iff
W\text{ tiles}.
\]
Projection of a periodic product tiling would be a periodic \(A\)-tiling, so
\[
W\otimes A
\]
never tiles periodically.

The primary source supplies the exact canonical-formula equivalences
\[
\alpha_U\notin\mathrm{ML}
\iff
U\text{ tiles periodically},
\]
and
\[
\alpha_U\notin\mathrm{Skvo}
\iff
U\text{ tiles}.
\]

Putting
\[
U=W\otimes A
\]
therefore gives
\[
W\text{ tiles}
\iff
\alpha_U\in\mathrm{ML}\setminus\mathrm{Skvo}.
\]

The tileset product and canonical-formula construction are effective. Since ordinary Wang tileability is \(\Pi^0_1\)-complete, this is a computable many-one hardness reduction.

## Limits

No bounded finite computation is used as evidence for the infinite tiling correspondences. The verification does not claim polynomial-time efficiency or a restricted-fragment completeness theorem.
