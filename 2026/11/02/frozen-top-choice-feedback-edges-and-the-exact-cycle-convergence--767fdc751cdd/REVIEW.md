# Scientific review

## Correctness — PASS

The assumptions are explicit: finite simple undirected graph, strict rankings of all neighbors over unmatched, and one blocking edge per transition. The independent forest argument follows an involuntary-breakup dependency backward through a hypothetical periodic orbit and constructs a forbidden infinite nonbacktracking walk. A mutual first-choice edge, once formed, is immutable; a feedback set of such edges splits any trajectory into at most \(|F|+1\) forest stages. The published forest move bound then gives \((|F|+1)\lfloor n^3/8\rfloor+|F|\). For a simple cycle, the absence of a \(+\) to \(-\) sign change is equivalent to constant orientation; the explicit one-edge orbit proves that both coherent orientations do cycle. Both odd/even static-stability cases were checked by direct argument. Every strict profile on cycles of order 3 through 10 was independently enumerated in `verify_cycles.py` with 824,616 valid improving transitions. Finite checks are corroboration, not a substitute for the universal proof.

## Originality — PASS, with literature risk

Fanelli--Moscardelli (DOI: 10.3233/FAIA251234), fully inspected in the HTML edition, already prove convergence on forests (Theorem 4) and provide one nonconvergent four-cycle (Figure 1). They do not in the inspected theorem/figure/results provide the present mutual-top feedback condition or the if-and-only-if classification of all strict profiles on cycles of arbitrary order. Bredereck--Chen--Finnendahl--Niedermeier (DOI: 10.1007/s10458-020-09470-x) exhibit cyclic top-choice obstructions to *existence* of stable matchings; the odd-cycle nonexistence observation is acknowledged as previously known rather than promoted to a standalone novelty claim. Diamantoudi--Miyagawa--Xue (DOI: 10.1016/j.geb.2003.05.003) guarantee the existence of some convergent path for solvable instances, not termination of all improvement paths. Available published research records and prior accessible claim ledgers were compared by implication, including the four-person stable-roommates census record 2026/10/4/…0bfa73dccf63, which is a static complete-preference census rather than cycle-graph dynamics. No stronger covering statement was identified. Novelty is not certified; differently worded prior dynamic criteria may remain unindexed.

## Value — PASS

The motivating paper explicitly identifies graph topologies between trees and complete graphs as an important research direction. A simple cycle is the first fundamental departure from forests. The exact \(2\)-profile failure classification valid for all cycle lengths, the uniform-random prevalence \(2^{1-n}\), and the feedback-edge sufficient theorem for arbitrary graphs explain precisely when a potentially destabilizing cycle is neutralized by first-choice preferences. The result distinguishes mere stable-matching existence from guaranteed convergence under every blocking-pair selection rule. Although the proof is compact, the structural classification is natural and quantitative rather than an arbitrary finite slice.

## Residual limitations

The published forest bound is used only for the optional explicit polynomial move-count estimate; the qualitative theorem is proven directly. The theorem does not characterize graphs with several cycles when the feedback-edge condition fails. Ties and alternative deviations are outside scope. Different nomenclature or inaccessible literature could affect priority.

Self-review: passed. Independent audit: not yet performed.
