# Review of three positive-step bands for Radau IIA diffusion on stars

## Correctness — PASS

The three-projector decomposition of the star Laplacian gives every completed-step matrix entry exactly, with positive denominators. Hub and leaf signs reduce to a quadratic and a quartic. The quadratic changes sign twice exactly at eleven or more leaves. For the quartic, a coefficientwise positivity argument on \(0\le h\le3\), endpoint concavity for \(2\le m\le10\), a strictly negative evaluation at \(h=m\) for \(m\ge11\), and Descartes' rule jointly establish all roots and sign ranges. The intervals are disjoint. A standalone exact-rational matrix check passed 176 cases; finite testing is corroboration, not the proof.

## Originality — PASS, with residual risk

Relevant published work on implicit SSP conditions, Radau IIA A-stability/maximal parabolic regularity, and other semi-implicit sign-preserving methods was inspected in substantive original-text portions. The closest recoverable specialized Radau results on balanced multipartite and rook graphs give different graph families and a single forbidden interval. A broader reversible-Markov per-state diagonal result already explains the positive-diagonal eleven-vertex boundary, but does not imply the exact star diagonal polynomials or two separated forbidden step intervals. Actual published-finding corpus searches using method and graph aliases revealed no matching exact classification. Specialized unindexed prior art remains possible, and a failed search alone does not establish novelty.

## Mathematical value — PASS

The result identifies a sharp integer-size transition in numerical monotonicity for a natural high-degree junction model: a negative hub-diagonal window, a restored positive middle interval, a separate negative leaf-diagonal window, then eventual recovery. It establishes exact conditions for physically meaningful nonnegative completed values even though the method remains spectrally stable and mass preserving throughout. The infinite family and two distinct negativity mechanisms make it a structural classification rather than a routine particular-matrix calculation.

## Limitations

The graph must be an unweighted star, the integrator must be the two-stage order-three Radau IIA scheme, and only completed-step entrywise positivity is addressed. The statement does not guarantee accuracy for large steps or internal-stage positivity. The proof has not undergone independent audit; the remaining novelty risk is possible specialized prior literature not returned in the searches.

Self-review: passed. Independent audit: not yet performed.
