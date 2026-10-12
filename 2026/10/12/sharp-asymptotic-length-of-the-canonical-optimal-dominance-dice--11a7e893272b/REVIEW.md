# Review: Sharp asymptotic length of the canonical optimal-dominance dice subcycle

## Correctness
PASS. The canonical comparison probability gives an exact one-step product constraint, and monotonicity makes the farthest admissible successor greedy-optimal. After centering, both parity recurrences have exact increments whose fixed-height bands have total width \(2\sqrt m(\sqrt{r+1}-\sqrt r)+O_r(1)\). Dividing each band width by its constant step \(r+1\) yields the series, while a dyadic estimate makes the outer bands negligible after division by \(\sqrt m\). The unrestricted lower bound follows exactly from \(3/4-a_n=\tan^2(\pi/(n+2))/4\). The regression checker reproduces every shortest-canonical-subcycle length quoted by the source.

## Originality
PASS. Full-text comparison with the motivating paper shows that it proves only square-root-order bounds for the unrestricted minimum and lists several shortest canonical-subcycle lengths without deriving their asymptotic constant. Candidate-specific database searches under the subcycle, recurrence, numerical-constant, and \(n(N)\) formulations found no covering statement. Later balanced-dice work concerns three-cycle attainable probabilities and side counts, not the sharp-dominance cycle-length asymptotics studied here. The main residual risk is an equivalent analysis of the same integer recurrence under different terminology.

## Value
PASS. The source explicitly highlights the gap between its easy shortened subcycle and the shortest one and reports values through \(N=10^8\). The theorem explains those data with an exact lattice-sensitive constant, improves the canonical upper constant from a coarse value below \(5\) to \(2.630472693388697\ldots\), and simultaneously sharpens the source's universal lower constant to \(\pi/\sqrt2\). This is a structural asymptotic answer to a natural invariant introduced by the source, not a finite extension of its table.

## Closest literature and limitations
The closest literature is Komisarski's 2021 paper, especially Theorem 2 and the paragraph listing shortest canonical subcycles. The 2024 balanced-nontransitive-dice classification studies a different fixed-three-dice problem. The exact constant here is not claimed for the unrestricted minimum; the gap between \(\pi/\sqrt2\) and \(C\) remains.

Self-review: passed. Independent audit: not yet performed.
