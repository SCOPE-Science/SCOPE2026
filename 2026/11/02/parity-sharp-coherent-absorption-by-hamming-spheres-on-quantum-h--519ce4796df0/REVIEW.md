# Scientific review

## Correctness — PASS

The final claim is a single all-radius hypercube Hamming-sphere absorption theorem, including exact energy-resolved Walsh-shell restriction ranks and the odd/even minimum number of full Hamming layers needed for total capture. All symbols, ranges, boundary dimensions and positive loss assumptions are explicit in `RESULT.md`. The proof first reduces the dark projector to adjacency energy eigenspaces whose Walsh expansions vanish at the traps. The Boolean inclusion up/down commutator gives a complete orthogonal harmonic decomposition; computing the signed intersection transform of each harmonic lift gives the precise scalar \((-2)^i K_{n-2i,w-i}(r-i)\). Its vanishing criterion proves the rank formula and the central odd/even assertions. A finite-dimensional dissipative spectral argument turns rank into actual no-jump asymptotic norm loss. The supplied checker was executed successfully from the scientific package, with 284 signed-shell ranks, 30 direct adjacency observability ranks, 8 parity checks and 24 paired-shell tests. The infinite-family result is analytic and does not depend on extrapolation of finite tests.

## Originality — PASS on examined sources, historical priority provisional

The closest previously examined results include Moore–Russell's hypercube Fourier diagonalization, Varbanov–Krovi–Brun's continuous-time quantum hitting framework, Srinivasan's binary Hamming Terwilliger harmonic decomposition, and Filmus's Boolean-slice harmonic basis. Those mechanisms are credited and not claimed as new. Published mathematical findings on all-degree **nonbinary** Fourier-shell sampling and on binary **low-degree** Walsh-band shell concentration do not provide the all-exact-energy shell ranks or the global-loss physical parity theorem as stated. Existing corner-start shell absorption determines survival from one initial vector, not from all initial states; Hamming-ball trapping has a different support. A newer spin-coupled Grover-walk preprint has a related parity theme but different dynamics. The remaining risk is that general pre-existing harmonic/association-scheme identities could have been explicitly specialized in an older source not recovered by the targeted full-text comparisons.

## Mathematical value — PASS

The problem asks when a geometrically thin, highly symmetric set of absorbers eliminates all coherent dark states in a quantum network. The theorem gives the exact answer for every single Hamming sphere, its entire energy-resolved rank profile, a sharp parity obstruction, and an optimal two-layer repair in even dimensions. In odd dimension, a vanishing fraction \(\Theta(n^{-1/2})\) of trap vertices captures **every** initial state, a quantitatively distinct assertion from capture of one chosen corner state or eventual trapping on a Hamming ball. These provide nontrivial structured network design benchmarks, not a routine standalone binomial evaluation.

## Evidence and limitations

Primary literature inspected includes the full available texts of Moore–Russell, Varbanov–Krovi–Brun, Srinivasan and Filmus, together with two closely related published Fourier-shell results. An additional relevant 2026 preprint was available through its abstract but its full text could not be accessed during comparison. Such access uncertainty is retained as a risk, not represented as proof of novelty. The exact minimum is over unions of complete shells, not unrestricted vertex subsets. Site-dependent trap rates may change convergence speed. The theorem does not treat dephasing, arbitrary disorder, or finite-time optimum capture.

Self-review: passed. Independent audit: not yet performed.
