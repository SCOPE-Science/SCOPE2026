# Scientific assessment

## Correctness: PASS

The physical local update uses the current closed-neighborhood population with thresholds \((1,3)\). The proof's recurrence is checked against both possible current states and both possible values of the next-neighbor bit. Its inductive set-inclusion proves every sweep output satisfies \(y_n=y_1\); the calculation on that invariant subset is an explicit invertible rotation, not an observed pattern. A first-input-transition decomposition proves all one-step predecessor multiplicities, which sum over the rotations of a primitive word to give the triangular cyclic-run basin formula. The extremal statement follows from convexity, with its equality family exhibiting every divisor period. Separate direct-update programs exhaust all bitstrings through \(n=12\) and \(n=18\), respectively; finite checks are corroboration, not the argument for arbitrary \(n\).

## Originality: PASS, with residual risk

The closest same-object source is Kuhlman et al., arXiv:1108.2974: Example 2.1 and Figure 1 give the small full phase space at \(n=4\), and Proposition 3.6 constructs one orbit of length \(n-1\) for general \(n\), under the identical rule and cyclic scan. Existence of that orbit does not imply an exact one-step image, a conjugacy for every periodic state, a complete necklace multiplicity census, or the attraction-basin formula. Section 4 of that paper develops existence constructions on trees rather than the missing cycle-wide basin classification. Macauley–Mortveit, arXiv:0802.4412, concerns equivalence of sequential update orders, and Defant, arXiv:1509.03907, concerns arbitrary rules on complete graphs and period-two orbits. Searches for bi-threshold cycle attractor enumeration, one-sweep state rotation, and necklace/basin equivalences did not identify a dominating theorem. The possibility of an unindexed equivalent treatment remains; a negative search is not a proof of uniqueness.

## Mathematical value: PASS

The original literature establishes existence of arbitrarily long sequential bi-threshold cycles, but leaves the phase-space organization and basin distribution unexplained for its basic cyclic example. Here the entire family of size \(2^n\) is reduced exactly to an \((n-1)\)-bit rotation with a one-step transient layer. Binary necklaces enumerate every attractor, while cyclic run lengths—not just orbit period—determine its basin. The sharp basin extremizers make the concentration of initial conditions on different attractors quantitatively testable. This is an all-sizes structural and dynamical classification, not merely a special finite computation or a renamed enumeration.

## Scientific limitations

The theorem does not classify different scan orders, thresholds, stochastic variants or continuous dynamics. General cycle-equivalence results do not transfer its individual basin formulas. No independently performed mathematical audit is claimed; literature coverage is bounded by accessible published sources and queries.

Self-review: passed. Independent audit: not yet performed.
