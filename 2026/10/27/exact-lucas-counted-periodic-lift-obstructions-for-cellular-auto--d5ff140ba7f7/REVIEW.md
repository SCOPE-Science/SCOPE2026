# Scientific review: Exact Lucas-counted periodic-lift obstructions for cellular automaton rule 18

## Correctness — PASS
The rule-18 parity polynomial forces even output weight on every finite periodic ring. A pair of adjacent output ones forces the input marker `1001` and permits same-period splicing. For cyclically isolated output ones, the explicit XOR phase construction gives an exact preimage, period \(n\) if output weight is even and period dividing \(2n\) in all cases. These cases exhaust periodic points in the image. The weighted transfer-matrix trace yields the Lucas-minus-character formula and the rational generating function. Direct exact Boolean-matrix enumeration of every binary ring word through \(n=12\) checks all key cases, but is not used as an infinite proof.

## Originality — PASS, with residual priority risk
Wolfram (1984) describes the one-step symbolic image of rule 18, not the evaluated same-period failure census. Jiang–Xie (2002) study time evolution and defects. Shreim et al. (preprint 2006) study finite-ring cellular-automaton preimage networks, not the all-length parity-filtered image-point count. Salo (2022) treats the general weak periodic point condition and its decidability, so the simple existence of an obstructed periodic point is NOT claimed as novel. Sabrié–Törmä (2023 preprint) explicitly use marker-`11` parity arguments for limit dynamics, so the marker ingredient is also NOT claimed as novel. No inspected result states the combined complete exception language, closed Lucas/character count, and universal period-doubling bound. General decision procedures or unexamined early tables could implicitly cover the result; historical priority is not independently established.

## Mathematical value — PASS
The result quantifies exactly the failure of periodic-point lifting for a canonical elementary cellular automaton. It answers a natural invariant question with a complete all-period language classification, an explicit exponential census with period-six arithmetic fluctuation, and a sharp double-period repair for primitive output periods. This is more informative than a single witness of nonregularity and is not merely a count of arbitrary selected examples. It concerns the spatial image after one step, not the eventual attractor or temporal entropy.

Self-review: passed. Independent audit: not yet performed.
