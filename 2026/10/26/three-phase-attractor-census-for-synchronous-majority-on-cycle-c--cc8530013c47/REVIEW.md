# Scientific review

## Correctness — PASS

The finite-graph period-two property follows from a symmetric matrix sign-Lyapunov argument with a small diagonal tie-retaining weight, so it applies without imposing regularity. Periodic-state representation by two core/leaf phase words is bijective. The one-leaf case is a cyclic double-cover count; the two-leaf case has explicit local reversible transition conditions and a verified sixteen-state transfer polynomial; the three-or-more case is controlled by a strict private-vote majority after one step. The exact algebraic and all-labelled-state checks in `VERIFY.py` match the theorem for the stated finite ranges. No finite simulation is used as an infinite proof.

## Originality — PASS, bounded historical comparison

The exact ring word count \(Q_n\) and the general convergence-to-period-two theorem are known and are attributed, respectively, to Agur–Fraenkel–Klein (1988) and Goles–Olivos (1980). Primary manuscript inspection of Benjamini et al. (2014) and Turau (2022) finds general or tree-specific dynamical classifications, not the complete three-regime cycle-corona census. A cyclic majority rule with its *own* past bit is not equivalent to the private-leaf majority system by changing notation. Separate exact results on XOR dynamics of sunlet graphs, and majority dynamics on a circular prism, also have different local maps or graph degree structures. No inspected source yields the new \(r=2\) quartic trace formula and the \(r\ge3\) \(4^n\) recurrent-state/one-step law simultaneously. Unindexed prior work might contain an equivalent calculation; the scope of search is not a proof of novelty.

## Mathematical value — PASS

The natural operation of attaching more private leaves to every cycle site induces three distinct exponential recurrent-state growth rates while the local rule remains fixed. A complete infinite graph-family attractor census, explicit phase-bijection, sharp one-step bound in the third regime, and exact rational transfer presentation for the middle regime give usable structural information beyond textbook counting.

## Closest work and limitations

The 1988 majority-ring fixed-word sequence is prior art. The deterministic corona state-space census is not inferred from the general finite-graph period-two theorem. The related noisy majority transfer study by Lemoy, Mozeika and Seki (2014) was compared using accessible abstract/metadata, without a full-text conclusion. Basin cardinalities and sharp entry times in the first two regimes are not determined. A qualified historical-overlap risk remains; none of this constitutes independent verification.

Self-review: passed. Independent audit: not yet performed.
