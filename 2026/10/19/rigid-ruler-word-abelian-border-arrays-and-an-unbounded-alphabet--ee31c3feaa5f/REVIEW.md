# Scientific review: ruler-word Abelian-border-array rigidity

## Correctness — PASS

The proposition concerns every finite length and every possible realizing alphabet; the proof specifies the complete array and recovers all equalities among letter positions by induction. The key positive-border step cancels the known length-\((d-1)\) blocks in the Parikh equality for the shortest border \(d\), forcing the next letter. At a power of two, appending any previous letter yields a forbidden exact border, so a new letter is necessary. This excludes arbitrary third-symbol alternatives rather than relying on finite enumeration. The separate direct Parikh comparison and restricted-growth-word census through length \(16\) independently test the invariant and uniqueness; they are not substituted for the proof.

## Originality — PASS, subject to the stated literature risk

Habib–Shamil–Rahman (arXiv:2111.00259v1, Sections 3–4) established binary-array uniqueness and the elementary shortest/longest border duality, both acknowledged. Their explicit higher-alphabet nonuniqueness example does not resolve existence of **special rigid arrays**, nor does their Bell-number upper bound imply a minimum alphabet lower bound. Goč–Rampersad–Rigo–Salimov (2014) enumerate unbordered words; Berera et al. (2023) use ruler words for square-free words; Duval–Lecroq–Lefebvre (2005) address ordinary rather than Abelian border arrays. These statements do not imply rigidity under a weaker (Abelian) equality relation. Literature and published-record searches using the exact array, ruler/Zimin aliases, and alphabet-size formulations located no mathematical equivalent. A result embedded in classical word combinatorics or unindexed work remains possible, especially given the Zimin construction's familiarity.

## Mathematical value — PASS

The result addresses the higher-alphabet reconstruction difficulty identified by Habib–Shamil–Rahman, showing that notwithstanding general noninjectivity, an explicitly structured infinite family is uniquely reconstructible over **all** alphabets. The alphabet threshold is exact for that family and forces unbounded alphabet requirements for the general inverse problem, quantitatively \(M(n)\) at least logarithmic. This is not the same as trivially counting labels in a particular witness: uniqueness rules out all lower-alphabet realizations with the same numerical observation. It neither gives the optimal global maximum nor a general verification algorithm.

## Remaining limitations

Published ordinary-border-array alphabet bounds are analogous but impose stronger equality constraints; the inspected summaries cannot be treated as an Abelian-equivalence result. No independent audit has been completed. The exact general alphabet threshold and total array counts remain open beyond this family.

Self-review: passed. Independent audit: not yet performed.
