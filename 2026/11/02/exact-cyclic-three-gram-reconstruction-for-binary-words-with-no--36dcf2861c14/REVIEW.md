# Scientific review

## Correctness — PASS

The sole finding is a complete classification of cyclic three-gram multiplicity fibers for binary circular words without the cyclic factor `010`, together with the corresponding profile and singleton generating functions. The proof reconstructs the complete run decomposition for every nonconstant admissible necklace. The resulting profile coordinates uniquely determine the four integers \(t,v,A,B\); the missing-long-gap boundary \(v=0\Rightarrow A=0\), the constant necklaces and lengths \(n=1,2\) are treated separately. Stars-and-bars and Burnside's lemma count cyclic orbits of run pairs, with the correct order-divisibility requirements for periodic configurations. Explicit alternate placements exclude every non-singleton case, and exact generating-function sums and pole analysis give the asymptotics and the least eventual period. The standalone program verifies the complete profile-to-fiber map by independent literal necklace enumeration for every length through \(18\), and compares exact generating-function coefficients through \(150\). These checks are corroboration; the proof supplies the infinite argument.

## Originality — PASS, with limitations

The main nearby published works differ at the statement level. The 2015 sequence-profile work of Kiah, Puleo and Milenkovic establishes general constrained-profile and de Bruijn graph frameworks and quasipolynomial-order bounds; its inspected relevant theorems do not supply the exact `010`-avoidance profile parameterization, every reconstruction fiber, singleton criterion, or the two rational generating functions. Chee and collaborators' 2024 run-length-limited de Bruijn work instead maximizes lengths of sequences with non-repeated windows, and counts such necklaces/words, not three-gram multiplicity reconstruction fibers. The Markov-type work of Jacquet, Knessl and Szpankowski deals with first-order empirical transition matrices. Ye and Elishco's 2022 reconstruction setting uses unordered substring compositions with different equivalences and data. Targeted title, alias, forbidden-factor, Eulerian-flow and formula searches did not identify equivalent all-parameter formulas.

The main residual scientific risk is that a special case of a broader older integer-flow or Markov-type enumeration might already give one of these expressions without using the phrase `010`-avoiding necklaces. The negative search result alone is not offered as a proof of absolute novelty. The comparison rests instead on the distinct channel definitions and the specific claims visibly established in the inspected relevant sections.

## Mathematical value — PASS

The forbidden local transition `010` imposes the natural minimum-one-run-length constraint, distinct from upper run-length bounds. The theorem solves the exact noiseless ordered three-read capacity and rotational reconstruction problem for the entire infinite family, not merely a short enumeration. The precise fiber formula, singleton boundary, least period twelve and vanishing unique-profile proportion identify which information is lost by unordered cyclic reads. These facts are usable as benchmarks for constrained reconstruction and code design, even though noisy-read and longer-window extensions remain open. The exact per-profile reconstruction answer is more informative than merely counting admissible words or specifying asymptotic profile growth.

## Source comparisons and limitations

- Chee et al., *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454 (first posted 2024-03-03), Introduction and Sections 2 and 4, including the weight-refined necklace formulas: maximum distinct-window constrained cycles, not ordered multiplicity profile fibers.
- Kiah, Puleo and Milenkovic, *Codes for DNA Sequence Profiles*, arXiv:1502.00517 (2015), especially Section 3, Theorem 3.3 and Section 4: broad Ehrhart and restricted graph bounds, but no exact theorem for the forbidden triple with rotational fibers.
- Jacquet, Knessl and Szpankowski, *Counting Markov Types* (2010), DOI:10.46298/dmtcs.2768: first-order Markov-type enumeration.
- Ye and Elishco, *Reconstruction of a Single String from a Part of its Composition Multiset*, arXiv:2208.14963 (2022), Introduction, definitions and reconstruction model: linear composition multisets and reversal, not ordered circular three-grams.

A complete independent literature search and independent mathematical audit have not been performed. The result does not assert that the finite test suite proves its infinite formulas.

Self-review: passed. Independent audit: not yet performed.
