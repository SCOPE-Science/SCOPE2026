# Independent mathematical audit

## correctness

PASS

The length-two scattered deck recovers relative order of all r distinct singleton marker symbols from their directed pair counts. For a fixed marker permutation, each a-prefix and b-prefix count before a marker recovers all r+1 weak gap compositions a_s,b_s. All other deck entries are determined except K=#ab. Its intergap contribution H=sum_{s<t}a_s b_t is forced, and its intragap values form every integer in [0,S], S=sum a_s b_s, since an adjacent ba→ab swap increments #ab by one. Therefore each marker permutation and gap-composition pair contributes exactly S+1 decks, each with a nonempty fiber and multiplicity [z^{K-H}]∏ GaussianBinom(a_s+b_s,a_s;z). Summing using symmetry and means A/(r+1),B/(r+1) yields D2=r! * binom(A+r,r)*binom(B+r,r) * (1+AB/(r+1)), an integer. Independent direct enumeration of all multiset words/decks for (A,B,r)=(1,1,1),(2,2,1),(2,2,2),(3,2,2) yielded respectively 6,27,168,360 decks, matching the formula. The general interval and coefficient proof, not the small samples, establish unrestricted A,B,r>=1.

## originality

PASS

Best-of-knowledge: familiar Parikh matrices, inversion distributions, and general binary two-binomial equivalence algorithms are reused, but the all-parameter distinguishable-singleton-marker spectrum with exact every-fiber Gaussian convolution was not identified as already covered. Recent broad bounds pose a specific access risk.

## value

PASS

A precise length-two subsequence-deck class count and all fiber sizes provide natural reconstructibility and zero-error code invariants for fixed-content words with distinguishable markers, a useful intermediate family between binary inversion statistics and fully general multisymbol deck enumeration. Arbitrary r and A,B are covered, not a single small census.

The dated certificate retains the supplied scientific assessment, sources and limitations.
