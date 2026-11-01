# Review of complete dyadic-parabola exponential spectra

## Correctness — PASS

The claim is quantified over every integer \(k\ge1\). The proof gives the exact zero criterion for each quadratic character sum modulo \(2^k\): at the final binary level cancellation occurs for the two-bit Hamming edges, while at every earlier level it requires a difference in the first frequency coordinate. The only nontrivial noncancellation case is proved by a two-point evaluation of the squared magnitude, which is \(2^{m+1}\). Capacity induction on low-bit frequency cells proves the necessity of every branch, and the same criterion proves sufficiency. The count is exact because both lower 1-Lipschitz maps and terminal edge assignments are recovered uniquely from an unordered frequency set. The \(k=1\) boundary case is explicit. Exact cyclotomic code confirms all character zeros for \(1\le k\le6\) and exhaustively enumerates small spectra, but the proof does not rely on those finite checks.

## Originality — PASS under bounded prior-work comparison

The closest published result, *Complete exponential spectra of the parabola over odd prime-power rings*, was read in full. It proves only the odd-prime version using strict contractions and explicitly excludes characteristic two. Its argument requires invertibility of two, and does not imply the dyadic Hamming-edge last-level condition or this dyadic count. The full text of Fan–Fan–Shi on one-dimensional cyclic prime-power spectral sets and the relevant portions of Iosevich–Koh on finite-field quadratic extension were inspected; their conclusions differ in ambient object and invariant. published-finding corpus searches for dyadic parabola spectra, orthogonal-frequency partners, polynomial graphs over even prime-power rings, and general spectral sets returned no direct covering theorem. Other available mathematical statements were compared for equivalent objects and implications; none of the inspected ones states the all-level dyadic characterization. Historical equivalent characterizations under Butson/Hadamard terminology remain a residual risk; nonappearance in a search cannot establish priority.

## Mathematical value — PASS

This is the natural characteristic-two counterpart of the complete spectral-partner problem previously solved at odd prime powers, and the structural answer changes materially. In particular, every dyadic level supports both horizontal and vertical terminal choices, so a graph-only classification is false. The new theorem supplies an unrestricted-level classification, a closed exact basis count, and an explicit generation algorithm; it is not a restatement of a Gauss-sum identity or a finite table. The count deliberately distinguishes ambient-frequency sets even when some restricted characters coincide.

## Limits

No assertion is made for arbitrary graph polynomials or equivalence-class counts. Exact finite verification is not independent validation, and independently conducted mathematical audit has not been performed. Historical priority outside the inspected literature remains uncertain.

Self-review: passed. Independent audit: not yet performed.
