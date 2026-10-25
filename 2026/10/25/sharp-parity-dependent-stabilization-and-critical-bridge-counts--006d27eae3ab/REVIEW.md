# Scientific review: sharp majority stabilization on bridged cliques

## Correctness — PASS

For each side, the majority update has an explicit three-case rule determined by the clique's total one-count and a single bridge bit. Odd cliques reach irreversible consensus by time two; even cliques can persist at half occupancy only while the two bridge bits disagree. These exact cases prove all dynamical and counting claims. The sharp terminal populations follow from binomial choices for half-filled nondistinguished vertices and, in the both-even case, strict binomial tail sums. The proof includes boundary sizes \(a=3\) and \(b=4\); every claimed count is corroborated by the standalone labelled-state simulation of \(254016\) configurations over 36 graph instances.

## Originality — PASS (bounded)

Goles and Olivos' period-two theorem is known prior work. Kaaser–Mallmann-Trenn–Natale (2015) explicitly address dense clique modules and give general convergence-time bounds, but their full-text main results do not imply an exact bridge-critical phase diagram or central-binomial terminal count. Benjamini–Chan–O'Donnell–Tamuz–Tan (2014) discuss general, infinite and random-graph majority convergence, not this graph family's exact basin boundary. Existing majority counts for split graphs and clique windmills involve different graph adjacency; the named published bridge-barbell zero-forcing formula concerns a different local rule. The underlying 1980 full text remains unchecked and historical duplication cannot be ruled out.

## Mathematical value — PASS

Joining dense communities by a single edge naturally models weakly coupled opinion blocks. The theorem identifies a sharp, size-independent stabilization bound that changes from \(2\) to \(4\) to \(5\) with clique parity, and computes the exact configurations realizing each bound. In particular, a mixed-parity graph has a thin but quantifiable class of five-step delays and their frequency decays as \(1/(\pi\sqrt{ab})\) when both cliques grow. The result also settles the entire recurrent-state population and all primitive two-cycles. This provides a structural characterization and a reusable boundary-counting mechanism, not merely finite computation.

## Scope and risks

The theorem applies only to labelled simple bridge barbells with clique sizes at least three, synchronous open-neighbour binary majority and ties retained. Intermediate basin strata and fixed-point basin sizes are not classified. The finite checker is corroboration of the general proof. Historical overlap assessment is not equivalent to an exhaustive literature certification, and the 1980 original full text remains a risk.

Self-review: passed. Independent audit: not yet performed.
