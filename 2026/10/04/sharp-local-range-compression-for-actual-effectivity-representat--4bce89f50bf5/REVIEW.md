# Review

## Correctness

PASS. The source construction uses an auxiliary group coordinate only to synthesize a desired outcome \(u\) lying in the common range. Every prescribed neighborhood is already a subset of
\[
O(w)=\bigcup\Sigma_a(w),
\]
and uniform range guarantees that each other agent has some neighborhood containing \(u\). A cyclic group on \(O(w)\) therefore supplies the same cancellation step as the source's group on \(W\). The output remains in the selected intersection, and every \(u\in s\) is realized, so each action's exact output set is \(s\).

For the lower bound, in the two-agent frame with one neighborhood \(O\) per agent, a fixed action of one agent participates in only as many profiles as the other agent has actions. Determinism gives at most one outcome per profile, so realizing all \(r=|O|\) outcomes forces at least \(r\) actions on the other side, and symmetrically.

## Originality

PASS. The primary source gives the exact representation conditions and an explicit construction with auxiliary coordinate \(v\in W\), but it does not replace \(W\) by the local common range, discuss action-set cardinality, or prove a matching worst-case lower bound.

The closest same-year paper on actual-power representations treats two-agent generalized concurrent game frames and coalition powers. Its checked statements and construction discussion do not give this deterministic local-range compression or action-count optimality result. Earlier basic-power representation work likewise gives representability conditions rather than this local cardinality refinement.

Targeted published-finding and web searches for minimal action counts, local outcome-range compression, and action cardinality in actual-effectivity representations did not locate an equivalent statement.

## Value

PASS. The representation theorem is the semantic bridge used to pass between action-based concurrent-game models and neighborhood semantics in the new inquisitive action logic. On finite models, replacing \(|W|\) by \(|O(w)|\) can reduce the constructed action space substantially at worlds whose reachable outcomes occupy only a small part of the carrier. The matching lower bound shows that the local-range factor is not merely an artifact of the proof: it is unavoidable in the worst case.

## Closest literature and limitations

Ciardelli (2026), Theorem 2.2 and its constructive proof, are the direct source. Chen--Ju--Ågotnes (2026) is the closest contemporary representation-theorem literature, while van Benthem--Bezhanishvili--Enqvist gives the earlier basic-power background.

The result does not compute the exact minimum action count for every representable frame and does not address generalized nondeterministic outcome functions.

Same-model review: passed. Independent audit: not yet performed.
