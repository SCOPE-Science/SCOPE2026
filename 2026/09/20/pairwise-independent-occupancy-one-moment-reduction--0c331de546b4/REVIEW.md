# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The central reduction is exact. Averaging any admissible law over coordinate permutations and common alphabet relabelings preserves uniform pairwise marginals and preserves every occupancy-invariant objective. The resulting invariant laws are precisely mixtures of uniform occupancy-orbit laws.

For an orbit with collision count \(c\), coordinate symmetry forces a fixed coordinate pair to agree with probability \(c/\binom n2\). Common-label symmetry then forces every diagonal ordered pair \((a,a)\) to have probability \(c/(\binom n2 q)\), while every off-diagonal ordered pair \((a,b)\), \(a\ne b\), has probability \((1-c/\binom n2)/(q(q-1))\). Hence a symmetric mixture has pairwise-uniform two-coordinate marginals if and only if its mean collision count is \(\binom n2/q\). This proves both directions of the one-moment characterization.

The collision-free corollary follows from \(1\le C\le\binom n2\) on the collision event and from the fixed mean \(\mathbb EC=\binom n2/q\). The three orbit types \((1^n)\), \((2,1^{n-2})\), and \((n)\) realize the endpoint mixtures for every \(2\le n\le q\). Convex mixtures of endpoint laws retain the same pairwise-uniform marginals, proving attainability of the entire interval.

A standalone exact-arithmetic verification enumerates all vectors for \(2\le q\le6\), constructs both endpoint laws, checks every two-coordinate cell probability against \(1/q^2\), and confirms the stated all-distinct probabilities.

No hidden prime-power or divisibility assumption is used: the constructions are probability mixtures of complete symmetry orbits and therefore work for every integer \(q\ge n\ge2\).

## Originality

The literature check began from classical pairwise-independent hashing. Carter--Wegman introduced universal hashing, and Luby--Wigderson's treatment explicitly computes the expected number of pair collisions under pairwise-independent hashing and derives a one-to-one guarantee by the first-moment method. Those sources support the fixed mean-collision identity but do not state the sharp reverse inequality or the general occupancy-statistic reduction found here.

Strength-two orthogonal arrays encode the equal-weight finite-sample version of pairwise-uniform two-coordinate marginals. Recent orthogonal-array work and the 2025 review by Lin--Stufken were checked for nearby formulations; their emphasis is on definitions, constructions, classification, design optimality, and applications rather than an extremal occupancy reduction of this form. Wiese--Boche study collision-flat universal hashing and design connections, while Harvey--Sahami study explicit orthogonal arrays and arbitrary-parameter universal hashing; neither inspected source supplied the stated all-distinct interval or the one-moment convex-envelope theorem.

Ramachandra--Natarajan give tight bounds for unions of pairwise-independent Bernoulli events. That is a different constraint: under pairwise independence of \(X_1,\ldots,X_n\), the collision indicators for different coordinate pairs need not themselves be pairwise independent, especially when the coordinate pairs overlap. Their result therefore does not directly subsume the collision event considered here.

Searches also included finite exchangeability, 2-exchangeability, weighted/strength-two orthogonal arrays, collision-free and injective hashing, birthday probabilities under 2-wise independence, and synonymous occupancy terminology. No exact statement matching either the general reduction or the sharp interval was located.

Originality is therefore assessed as PASS only to the best of our knowledge. The proof is elementary once the correct symmetry is imposed, so the main residual risk is an equivalent result stated in a different language in finite-exchangeability, design-theory, hashing, or extremal-probability literature.

## Value

The result identifies a reusable mechanism rather than a single example: every occupancy-invariant linear objective under uniform pairwise independence becomes a one-dimensional moment problem over integer partitions. The two-point-support conclusion immediately limits the complexity of extremizers and can be applied to other symmetric occupancy statistics without rebuilding the full pairwise-independence polytope.

The all-distinct corollary is a concrete consequence. It proves that the familiar first-moment collision guarantee is not merely convenient but globally sharp over all pairwise-independent uniform laws, and it adds the sharp universal lower collision probability \(1/q\). At \(n=q\), the contrast with the iid value \(q!/q^q\) quantifies how much higher-order occupancy behavior can vary while all one- and two-coordinate marginals remain identical.

## Scientific limitations and residual uncertainty

The reduction requires invariance under coordinate permutations and a common relabeling of the alphabet. It does not characterize general nonsymmetric objectives or all admissible nonsymmetric distributions. Nonuniform marginals and higher-order independence would leave more moment constraints and are not covered by the theorem.

The literature search cannot exclude an older equivalent theorem under substantially different terminology. In particular, general work on finite exchangeability, weighted orthogonal arrays, correlation polytopes, or sharp moment problems may contain a reformulation not surfaced by the inspected sources. This residual risk does not alter the mathematical proof, but it limits the originality claim to the best of our knowledge.
