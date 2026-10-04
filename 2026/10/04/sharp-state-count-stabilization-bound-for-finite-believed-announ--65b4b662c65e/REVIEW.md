# Review

## Correctness

PASS. Under believed public announcement, every relation is intersected with the same target truth set. If an update is strict, at least one surviving arrow into a false target is deleted, and the update simultaneously deletes every incoming arrow to that target for every source and agent. That target therefore leaves the active-target set permanently. At most \(|T_0|\) strict updates are possible.

The sharpness construction is explicit. On the directed \(n\)-cycle, \(p\) is false only at one state and \(\neg\Box\bot\) says that the current state has a successor. The initially false target is removed first; its predecessor then becomes a sink, producing a one-state-per-round cascade. The final edge disappears at round \(n\), so the bound is attained.

## Originality

PASS. The primary 2026 paper proves general stabilization by counting labelled arrows and later gives a different finite-stabilization argument for single-agent \(K45\) generated models. It does not state a bound by active target states, a universal \(|W|\) finite-state bound independent of the agent set, or the sharp cycle family.

Targeted database and literature searches for finite stabilization bounds, active-target formulations, and sharp finite believed-announcement examples did not locate an equivalent theorem.

## Value

PASS. Transfinite stabilization is a central mechanism in the source paper. The theorem isolates the exact finite obstruction: on a finite carrier, the process cannot require transfinite stages and in fact has a sharp linear state-count bound even when the number of agents or labelled arrows is much larger. This gives a natural quantitative baseline for finite-model experimentation with iterated believed announcements.

## Closest literature and limitations

Yamada (2026), Definition 5 and Proposition 3, are the closest source. Proposition 3 uses the cardinality of the labelled-arrow set. Lemma 6 proves finite stabilization in a specific single-agent \(K45\) setting through propositional valuation types.

The sharp lower bound here is only for general models. A sharp \(K45\)-specific state bound is not claimed.

Same-model review: passed. Independent audit: not yet performed.
