# Independent mathematical audit

## correctness

PASS

The frozen formulas are correct. The reduced successors are U(i), U(H(i)); finiteness makes a closed set jointly invariant under U,H, so irreducibility is transitivity. Cyclic classes in an irreducible doubly stochastic chain have equal size, and U takes each to the next bijectively, forcing H to preserve each. One class is odd and the others even, which rules out nontrivial periods. The fine and reduced normalized Markov matrices share the nonzero spectrum and hence the primitivity criterion. In the revised proof, rotation U and pairing H describe a map with one extra leg. Deleting the leg and rooting at its successor is reversible for k>=1 (the leg is not a vertex on its own in a connected map). The H-centralizer permutes reflection pairs and swaps their elements, and an element commuting with both U and H fixes the leg and then every dart by transitivity, proving freeness and class size 2^k k!. The orbit recurrence is disjoint and the normalization gives A000698 with n=k+1. For the asymptotic re-audit, Borinsky Theorem 32 on the zero-constant-term series D-1 applies with (alpha,beta)=(2,1/2); the derivative of 2-1/(1+u) yields D^(-2)=1-2z-3z^2-16z^3+O(z^4). Dividing the shifted double factorials by (2n-1)!! gives coefficients 2, 3 and 22 in inverse powers of N, with a fourth-order remainder. Read the original RESULT.md and VERIFICATION.md and inspected verify.py without executing it; replay is the unchanged python3 verify.py as described in the repaired VERIFICATION.md. Its 5,166 finite graph comparisons corroborate primitivity, not the revised all-grid correspondence or asymptotic.

## originality

PASS

The frozen claim fails as an original enumeration and rarity-law result: both headline formulas are covered after identifying the exact known sequence, and the third coefficient is a direct application of an existing analytic-composition theorem. This is substantive re-scoping, not passing the old claim with a citation. In repairs/3/RESULT.md the retained finding is the dynamical classification: irreducibility suffices for each odd-grid shuffle, and a rooted map indexes each class under reflection-preserving relabeling, with a uniform lift. The numerical formulas are credited as corollaries. Neither the inspected shuffled-map paper nor the known combinatorial results establish this dynamical identification.

## value

PASS

Recomputing a known sequence and a covered expansion alone would not carry scientific value as new exact results. The revised finding has a motivated structural use: for this old dynamical family the period test is unnecessary once connectedness is known, and the label quotient preserves reduced-matrix similarity and identifies the conditional uniform shuffle ensemble with the uniform rooted-map ensemble. It classifies all allowed odd-grid shuffles modulo explicit symmetries and lets researchers import refined map counts instead of enumerating dynamics. This is independent of claiming novelty for the resulting numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
