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
The theorem was checked by a standalone direct implementation of ordinary color refinement.

For every nondecreasing tuple of path lengths with
\[
3\le d\le7,\qquad 2\le \ell_i\le10,
\]
the verifier constructs the simple subdivision of \(K_{2,d}\), runs refinement from the uniform coloring, and checks both the predicted stabilization depth
\[
\max\{\lfloor L/2\rfloor,S\}
\]
and the complete predicted partition at every round, where internal vertices are grouped by their unordered clipped branch-distance pairs.

The exhaustive run covers \(11{,}385\) graphs and \(77{,}660\) round-level partition comparisons. It additionally groups the data by fixed path count and order and checks \(45\) fixed-order extrema in a range where the length cutoff is automatically exhaustive.

The checker returns:

`VERIFY_OK depth_checks=11385 partition_checks=77660 order_checks=45 d=3..7 lengths=2..10`

The finite computation is corroborative only. The all-parameter statements rest on the induction and length-sum proof in `RESULT.md`.
