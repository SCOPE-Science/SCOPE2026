# Review of four-run self-shuffles

## Correctness (C): PASS

The finite derivative and parity-atom enumeration give a rigorous universal \(8\)-symbol atom bound. The certificate covers exactly \(2764\) even-Parikh smooth words at the four lengths \(38,40,42,44\); each supplied coloring is verified directly, with complete alternative enumeration of the finite domain. The negative residual-automaton checks exhaust all candidate bounded-run colorings, rather than relying on a timeout. The infinite argument uses only the proven atom bound, factoriality and the observation that swapping two colors within a completed self-shuffle preserves both induced subwords. No finite data is extrapolated to infinity without this argument.

## Originality (O): PASS, subject to stated priority risk

Kilpatrick, *Shuffle squares in smooth binary words and the Kolakoski sequence* (arXiv:2610.02262, first public 2026-10-01), establishes the even-Parikh smooth theorem and an explicit Kolakoski run bound of \(48\). Zwierzyński, *Shuffle Squares in Differentiable Words* (arXiv:2610.07828, first public 2026-10-06), establishes broader C3 existence results and exact unconstrained self-shuffle tests. Neither inspected primary text asserts a uniform bound \(4\) or the four-run exact finite window. published-finding corpus queries for color-run and Kolakoski equivalences returned no directly dominating statement. The older graph-based work of Grytczuk, Pawlik and Ruciński was examined at abstract level only; unindexed stronger statements remain possible. These limits prevent a claim of exhaustive publication priority.

## Value (V): PASS

The explicit bound for Kolakoski monochromatic runs drops from \(48\) to \(4\), while the theorem simultaneously extends to every smooth infinite binary word with infinitely many even-Parikh prefixes. This controlled-interleaving feature is strictly stronger than ordinary shuffle-square existence. The least compatible four-consecutive-even-length window \(38,40,42,44\) is a sharp and naturally motivated finite invariant: four even lengths cover every possible atom jump of size at most \(8\). Complete explicit positive and negative certificates make this useful for further investigation of stronger run limits.

## Limits

The bound \(4\) is not proved optimal for the infinite Kolakoski word. Exact finite-window optimality is a statement about a specific universal block-assembly criterion, not about every possible infinite coloring. Scientific priority remains provisional pending independent literature verification.

Self-review: passed. Independent audit: not yet performed.
