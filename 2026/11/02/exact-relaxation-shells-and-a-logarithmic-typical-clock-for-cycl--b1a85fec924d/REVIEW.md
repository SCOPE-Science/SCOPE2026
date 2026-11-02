# Review of exact relaxation shells for cyclic Rule 178

## Correctness — PASS

The Boolean update is independently equivalent to the standard Rule 178 lookup table; differences of consecutive updated symbols give a monotone wall map. Each intervening zero-wall run shrinks from both ends by one cell per side, yielding the exact first-periodic-entry time, including odd residual singleton gaps. Even wall parity and the factor-two lifting from wall strings to configurations are explicitly accounted for. Marking each of the \(k\) walls gives the exact cyclic gap coefficient and the factor \(n/k\); the terminal-shell parity cases require exactly two walls. The transfer-matrix trace at fugacities plus and minus one gives the Lucas-formula primitive orbit count. For the random-time assertion, any \(n-1\) wall coordinates really are independent; both union and disjoint-window bounds tend to their required limits. An independently implemented local-rule trajectory checker exhaustively verified 262,136 configurations across \(3\le n\le17\). No finite test is used as an infinite proof.

## Originality — PASS, qualified

The closest published antecedents include Inokuchi–Sato's fixed-boundary Rule 232 transient theorem, Kuhlman et al.'s general synchronous two-period theorem, Betel's even-size two-step Rule 178/232 conjugacy, Fukś's Rule 178 iteration description, Donoso Leiva et al.'s relative-wall lemma and parallel-period-two theorem, and a separate domain-wall discussion that explicitly states wall persistence and gap invasion. All these antecedent facts are credited. The inspected statements do not enumerate the exact labelled first-periodic-entry shells on *all cyclic rings*, the parity-dependent terminal shell, and the logarithmic typical clock. Closest mathematical-record results address different local rules, threshold systems or boundary conditions. The literature search does not establish absolute uniqueness, and further historical combinatorial equivalents remain possible.

## Mathematical value — PASS

Exact basin entry-time counts for all ring sizes distinguish configurations with equal eventual period but very different relaxation duration. The identified logarithmic typical time versus linear maximal time is a precise structural and probabilistic difference; the parity-dependent terminal-shell cardinality is a finite-size extremal invariant. A recurrence, coefficient formula, and transfer-matrix interpretation permit independent extensions to nonuniform initial laws, finite-size fluctuation questions and perturbations, without assuming those extensions are proved here.

## Boundaries

The comparison does not claim as new the Rule 178 wall update, the two-cycle bound, or the even-ring Rule 232 conjugacy. No claim is made for asynchronous schedules, open boundaries, other elementary rules or limiting extreme-value distributions. Historical equivalence is a residual risk. Independent checking is outside this review.

Self-review: passed. Independent audit: not yet performed.
