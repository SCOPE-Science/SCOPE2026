# Review of the vertex-geodesic online-shattering classification

**Correctness — PASS.** The upper bound is deduced from the exact version-space recurrence, support-bound lemma, four query-shape reductions and explicit center-degree refinement. Separate depth-three and depth-four certificates provide constructive lower bounds; the verifier replays every binary label sequence from endpoint pairs. The 128 canonical diameter-four trees of orders five through twelve were also exhaustively checked. The finite check does not replace the infinite proof.

**Originality — PASS with priority risk.** The inspected full-text sections of Ghazi et al. (2020 preprint; 2021 ALT proceedings) give generic closure inequalities, not the diameter-four branching criterion. Abraham et al. analyze VC dimension of the same shortest-path vertex sets (Theorem 2), not online shattering. The directly related earlier analyses of paths on chains and rooted descendant cones concern strictly narrower or different concept classes. Searches using geodesic-path, thicket, online mistake bound and diameter-four terminology located no dominating exact classification. The absence of a search hit is not a proof of absolute priority.

**Mathematical value — PASS.** This completes the first four nonzero diameter layers of online path learning for trees and isolates the first branching-sensitive threshold. Even with an unbounded number of endpoint-pair hypotheses, diameter-four trees have optimal worst-case realizable mistake bound at most four, with the exact three-versus-four transition controlled solely by center degree. Known VC dimension two does not imply this adaptive classification. The six-vertex minimal obstruction is an explicit reproducible structural witness.

**Closest literature and remaining limits.** See RESULT.md references to Ghazi et al. and Abraham et al.; the latter already proves the classical static VC upper bound and is credited. Historical priority beyond those inspected texts remains open. Diameter-five and larger trees are unclassified here.

Self-review: passed. Independent audit: not yet performed.
