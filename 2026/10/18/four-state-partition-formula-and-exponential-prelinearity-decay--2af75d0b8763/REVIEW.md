# Scientific assessment

## Correctness — PASS

The count of upsets of each incidence frame is \(Z(G)=\sum_{S\subseteq V}2^{|E(G[S])|}\), as an edge-world can be selected only with both endpoints. The two implications both fail at an edge-world precisely for opposed pure endpoint membership states; this gives the stated four-by-four matrix independently of optional lower memberships. The tree recursion follows by factorization, and the path recurrence and strict decay by elementary spectral computations and Perron comparison with a Kronecker product.

`verify.py` independently enumerated finite upsets and implication witnesses for 84 graph instances, totaling 2,490,828 ordered pairs, and checked defining-adjunction implication on 11 instances; it additionally checked tree recursion and path formulas. Finite checks are corroboration, not an exhaustive proof for all graph sizes.

## Originality — PASS, qualified

The inspected Bumpus–Kocsis paper supplies the satisfiability-degree framework and classical logical examples. The inspected Lewis-Smith prelinearity treatment concerns Gödel–Dummett linear-frame semantics rather than exact graph-incidence probabilities. The inspected Trotter–Wang paper uses the reverse incidence orientation and studies dimension of posets. The closest related weak-order prelinearity calculation covers ordinal sums of antichains; a related height-two negation-fiber result treats an entirely different invariant. None of these statements contains the full weighted four-state graph formula and path spectral limit. Graph-spin reformulations under other names remain an originality risk, and absolute publication priority is not certified.

## Mathematical value — PASS

The claim addresses a natural relative satisfiability degree, gives a uniform graph-indexed counting reduction and a fast forest algorithm, and reveals exact exponential loss of prelinearity even in height-two frames with two maximal successors per nonmaximal world. This identifies a mechanism and rate rather than a small numerical example.

## Limits

The strict decay assertion is about paths rather than all graph families. The linear bound counts integer arithmetic operations, not bit complexity. The proof and verifier use the dual incidence orientation. No external independent mathematical audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
