# Scientific assessment: Erlang immunization stages and vaccination depth

## Correctness: PASS

The one-target expected-descendant reward follows by multiplying the exact race probability for an Erlang maturation clock versus an independent Erlang depth-infection clock by the number of strict descendants. The proof derives the race probability by event order, establishes strict depth log-concavity using coefficient-ratio monotonicity and exact complete-tree descendant counts, proves the monotonicity and endpoint values of every adjacent-depth ratio, and handles all transition endpoints. The sharp two-stage boundary and the exact binary-tree witness are rational consequences of the general theorem. The included `verify.py` checks \(1{,}920\) exact-rational families and independently reconstructs each race probability by finite-state dynamic recursion; this corroborates, but does not replace, the infinite-parameter proof. No unproved asymptotic claims are used.

## Originality: PASS, subject to ordinary literature uncertainty

Li–Huang–Lee–Eun (2023) supply the stochastic SI-with-delayed-immunization tree model and the general one-vaccine reward formula. Their accessible complete preprint was inspected through its model, theorems, proofs, numerical experiments, and references. Their result implies that any particular depth can be scored; the source does not state this exact all-branching/all-height/all-Erlang-stage sequence of strict log-concavity, ordered transitions, or the sharp one-versus-two-stage switch. The closest multistage-vaccine paper by DeLegge and collaborators concerns population-level compartment dynamics and does not have the same rooted-tree target objective; only its abstract was accessible in this check. Nguyen–Carlson's accessible description concerns a stochastic two-city SIR allocation model, not the same finite-tree race. Searches of related published mathematical findings identified delay-distribution and vaccination-threshold results but no implication of the ordered depth classification. A search is not a proof of publication priority; full verification of all possible literature is outside this review.

## Value: PASS

The model addresses a genuine allocation tradeoff: vaccinating close to an infected root protects more descendants but has less time to mature. The theorem completely solves this tradeoff on an analytically natural symmetric tree class for any positive infection/maturation rates and every integer stage count, including degenerate tie boundaries. It proves that a memoryless maturation assumption structurally prevents deeper targeting, whereas two maturation stages can reverse the preferred level without changing mean maturation time. This is an exact, reusable benchmark for allocation with noninstant immunity, rather than a numerically optimized arbitrary tree or a restatement of the source's expected-reward formula.

## Closest literature and limitations

The 2023 IFIP Networking paper is the precise model source and is credited for its baseline formula and algorithm. The 2015 multistage vaccine study and 2016 two-city vaccination study concern substantively different disease-population models. Published delay-comparison work is not a tree-depth optimization classification. The mathematical scope is one vaccinated vertex, one infected root, homogeneous independent exponential infection times, complete rooted trees, and Erlang maturation. The reward excludes the vaccinated vertex itself, following the source formulation; including it changes finite-height cutoffs. Multiple targets, recovery, other graphs, general phase-type distributions, and empirical effectiveness are not addressed.

Self-review: passed. Independent audit: not yet performed.
