# Self-review

## Correctness — PASS

The automorphism group is exactly the product of infinite symmetric groups on row and column coordinates. The pointwise stabilizer fixes precisely the used rows and columns, so its orbit count on arbitrary tuples factors into two distinguished-Bell polynomials. Applying invariant-set inclusion–exclusion removes the individually fixed parameter cells; signed Stirling inversion then removes collisions among tuple coordinates. The small-arity specialization recovers the unordered support pair from the product and sum of squares of its shifted coordinates. A direct bipartite-incidence classification establishes the sharp four-cell minimum, while a two-row degree-distribution argument establishes arbitrarily large collision fibers. Every statement is quantified over finite bases, and the limitations about fixed cardinality and ordered support are explicit. The standalone checker corroborates the independent analytic derivation on small cases; it is not offered as an infinite proof.

## Originality — PASS (qualified)

Cameron's *Sequences Realized by Oligomorphic Permutation Groups* (2000), in the full readable primary text, develops oligomorphic orbit/type counting, Bell and Stirling transforms and the infinite symmetric product action, including unlabelled bipartite-pattern orbits. These are pre-existing methods, not new ingredients. Applegate–Cameron's *Orbits on n-Tuples* (2009) develops general tuple-orbit inequalities, but not the finite-base grid stabilizer spectrum or its sharp collision fibers. Searches for pointwise-stabilizer finite-base type counts, bipartite incidence aliases, equality-of-spectra implications, and equivalence-class reduction did not identify a statement that covers the complete arity-two saturation and collision theorem. The closest comparison on random bipartite graph reduct groups concerns different edge-flip actions and is not a covering implication. The remaining risk is unindexed or implicitly equivalent material about product actions and orbit-growth invariants. Bibliographic search failure is not treated as proof of novelty.

## Mathematical value — PASS

The parameter-size-conditioned numerical type spectrum is a natural invariant of a classical homogeneous structure. The result completely determines when two finite bases have equal type counts in every arity, proves that arity two is sufficient to classify this numerical equivalence, and determines both its first genuinely nonisomorphic fixed-support collision and unbounded exact-size fibers. The theorem precisely distinguishes loss of structural incidence information from loss of numerical orbit-growth information; the sharp and unbounded features are not just a restatement of the basic Bell-number formula.

## Closest literature and limitations

P. J. Cameron, *Sequences Realized by Oligomorphic Permutation Groups*, J. Integer Sequences 3 (2000), Article 00.1.5, https://cs.uwaterloo.ca/journals/JIS/VOL3/groups.html (online 2000-01-25). R. Applegate and P. J. Cameron, *Orbits on n-Tuples*, Comm. Algebra 37 (2009), 269–275, https://webspace.maths.qmul.ac.uk/p.j.cameron/preprints/orbitpaper.pdf. Numerical types do not encode actual complete formulas, the two-count recovery presupposes equal known base sizes, and the four-cell minimality presupposes a fixed ordered pair of support sizes. Independent validation was not undertaken.

Self-review: passed. Independent audit: not yet performed.
