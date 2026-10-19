# Scientific review

## Correctness — PASS
The exact four-transition jump chain follows from independent edge priorities, and its fluid equations have the displayed scalar solution. The stopped-martingale central limit theorem is not inferred from simulations: the proof supplies a uniform terminal cutoff, with a generator-bound Lyapunov argument and a parity-based identification of terminal vacancies. The variance is the explicitly evaluated martingale bracket. The small-instance exact graph and count-chain calculations, generator inequalities, and numerical integral pass using `verify.py`. The only asymptotic normalization is \(\sqrt N\), with class densities tending to fixed positive limits.

## Originality — PASS, with limitations
The closest directly examined full primary text is Gamarnik–Goldberg (arXiv:0807.1277v1), whose theorems concern bounded-degree and/or large-girth graphs; these cannot establish the present dense, three-type, balanced-terminal folded Gaussian law. Dyer–Frieze (1991) and Pippenger (1989) provide classical greedy-matching/adsorption context, but their full text was unavailable. An earlier complete-split calculation yields a positive limiting vacancy density and an ordinary Gaussian about its nonzero mean. An earlier complete multipartite law with a *fixed* number of parts yields a zero limiting density under tied maxima, but neither its asserted statement nor the fixed-part quantifiers determine the \(\sqrt N\)-scale distribution here. An undiscovered special dense-graph central limit theorem could overlap; the lack of a matching search result is not proof of uniqueness.

## Mathematical value — PASS
A physically natural substrate has two competing adsorption reservoirs and a third reservoir permitting within-class dimers. Perfect matching is possible for every finite even graph; nevertheless, a random irreversible process has a diverging jammed population of order \(\sqrt N\), whose law is folded normal. This is a finite-size critical fluctuation theorem at a zero-density boundary, not a small numerical correction or a change of notation in a macroscopic law.

## Limitations
Independent audit has not been performed. The theorem requires equally sized independent reservoirs and a fixed positive clique fraction. There is no generalization here to unequal reservoirs on the critical \(\sqrt N\) scale. The inaccessible older source is an unresolved bibliographic risk, not a claim of noncoverage. Finite exact checks and simulations do not prove the infinite-volume theorem.

Self-review: passed. Independent audit: not yet performed.
