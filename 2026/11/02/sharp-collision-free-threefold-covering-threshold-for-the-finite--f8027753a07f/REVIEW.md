# Scientific review: restricted cubic moment sums

## Correctness — PASS
For every finite field of characteristic at least five, the proof determines the unrestricted fiber by a quadratic-character quartic in the auxiliary sum \(u=x+y\), then removes precisely three pair-collision loci by inclusion-exclusion, restoring the all-equal locus twice. The cubic collision equation has at most three roots, so at most nine ordered representations are removed. Nonsingular quartics have genus one and two rational points at infinity: Hasse's bound gives at least \(q-2-2\sqrt q>9\) unrestricted representations for \(q\ge23\). The singular locus \(w=s^3/9\) factors and is handled explicitly; the diagonal locus \(w=s^3\) has a direct count. Complete finite enumeration certifies every smaller eligible field and all claimed absence sets. The code was executed for 6,371 complete target fibers including extension fields. Risk: finite checks alone would not prove the infinite statement; the proof's genus-one and singular-case arguments supply that step.

## Originality — PASS, with residual historical-priority risk
Moreland--Zieve, arXiv:1304.1442, Section 6, studies the *same pair of moments* but asks for infinitely many rational solutions to fixed Diophantine equations, using elliptic curves of positive rank; it does not state a collision-free finite-field universal threshold or classify missing targets for six small fields. Choudhry (2010), Sections 2 and 5, studies rational/integer equal-sum and equal-cubes parametrizations, not all target fibers over finite fields. The closest accessible published cubic-graph Fourier results concern twofold energy, a sharp \(L^4\) norm, or orthogonal character spectra, not pairwise-distinct threefold covering. An accessible historical result on *unrestricted* threefold cubic sums for \(q\ge11\) does not imply the restricted conclusion: the present \(q=19\) example has six forbidden targets. Searches were performed by exact moments, distinctness, finite-field aliases, elliptic reductions, sharp bounds, and numerical exceptions. Residual risks include an unlocated specialist result or a full-text table not surfaced by searches; the general elliptic method is not claimed as new.

## Mathematical value — PASS
This is an exact natural restricted-additive-basis classification for the cubic moment graph over **all** finite fields in the stated characteristics, rather than an isolated finite enumeration. It finds the optimal covering threshold \(23\), all smaller-field obstructions, and an exact formula for the number of ordered collision-free representations of *every* target. Distinctness is essential for additive configurations without repeated summands, and the difference between the unrestricted threshold and the restricted threshold is mathematically substantive. The answer combines the arithmetic structure of elliptic-curve point counts with exact local degeneracy correction.

## Closest literature and limitations
- Moreland--Zieve (2013), arXiv:1304.1442: same moment equations over \(\mathbb Q\), different quantifiers and objective.
- Choudhry (2010), DOI 10.46298/hrj.2010.171: integer/rational Diophantine parametrizations, not finite-field target coverage.
- Hasse bound: established tool, not claimed as new.
- Characteristics two and three excluded; residual historical-priority uncertainty remains.

Self-review: passed. Independent audit: not yet performed.
