# Scientific review of the cyclic binary three-gram profile theorem

## Correctness

**PASS.** A cyclic word corresponds exactly to an Eulerian closed walk in the order-two binary de Bruijn digraph. The key extra condition beyond balanced nonnegative edge counts is connected positive support. The proof partitions by the positive occurrence of the two bridge types and accounts separately for the otherwise disconnected loops and alternating two-cycle. The partition gives a rational generating function by direct geometric sums, and exact coefficient extraction yields the all-length period-twelve quasipolynomial. Its small-length conventions include lengths one and two. A standalone, dependency-free checker compares actual length-three profile sets of every binary word to the independently enumerated parameter cases for lengths one through eighteen and checks the coefficient formula through length forty-six. Finite verification is corroboration, not the infinite proof.

## Originality

**PASS at the level of the available evidence, with residual literature risk.** Kiah–Puleo–Milenkovic's profile theory implies polynomial-order growth and gives the asymptotic constant \(1/288\) at binary three-grams, but its relevant sections and table do not state the exact cyclic finite-length count, rational series, or least quasipolynomial period. Jacquet–Knessl–Szpankowski count first-order, rather than second-order, Markov types. Yehezkeally et al. study distinct read/reconstruction constraints. The closest related published two-multispectrum record counts cyclic bigram profiles, not trigram profiles. No explicit equivalent rational series or degree-four period-twelve formula was located. A high-order Markov-type specialization in other literature remains the principal uncertainty; this is not a claim of globally established priority.

## Mathematical value

**PASS.** The exact number of distinguishable outcomes of a natural noiseless read-multiset channel is a directly motivated information-theoretic invariant. The result sharpens the known asymptotic leading constant to a complete all-length formula, distinguishes connected realizable profiles from balanced but disconnected pseudoprofiles, and identifies the minimal period-twelve arithmetic variation. It gives a sharp zero-error code cardinality for every block length, including small lengths for which asymptotics provide no exact answer.

## Boundaries and validation status

No alphabet size larger than two, read length other than three, fiber cardinality classification, or efficient optimal encoder is claimed. The proof is mathematical; computational checks cover only stated finite ranges. The self-review is not an independent scientific audit.

Self-review: passed. Independent audit: not yet performed.
