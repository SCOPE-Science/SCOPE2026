# The first double peak of sample-incidence singletons occurs at fifteen sites

## Finding
Consider a finite ecological incidence survey with exactly two distinct species and \(N\) sites. If \(k\) sites are drawn uniformly without replacement, let \(U_k\) count species recorded in **exactly one** of those \(k\) sites, and put \(u_k=\mathbb E[U_k]\). For strictly positive species occupancies, **two strict interior local maxima** of the sequence \((u_1,\ldots,u_N)\) are impossible when \(2\le N\le14\). At \(N=15\) they occur for exactly one unordered occupancy pair, \(\{2,9\}\), with maxima at \(k=2\) and \(k=7\). This holds irrespective of overlap between the two species' occupied-site sets. One species by itself always gives a unimodal expected singleton curve, so two species are also the smallest richness capable of the phenomenon.

The raw count and its per-site normalization differ qualitatively: for any fixed finite incidence matrix with any species count, \(u_k/k\) is nonincreasing in \(k\), even when \(u_k\) has two strict local maxima. The normalized monotonicity is a known complementary property, not claimed as a novel theorem.

## Assumptions and scope
Let \(N\) be an integer with \(2\le N\le15\), and let each of two labeled species occur at a nonempty fixed subset of \(\{1,\ldots,N\}\). Their occupancy sizes, after ordering, are integers \(1\le a\le b\le N\); the occupied subsets may intersect in any permitted way. Each of the \(\binom Nk\) site subsets of size \(k\) is sampled with equal probability. Observations are perfect, and sampling has no effect on the underlying incidences. Define a **strict interior local maximum** at an integer \(k\) with \(2\le k\le N-1\) by \(u_{k-1}<u_k>u_{k+1}\). Tied plateaus are not counted as strict maxima. Set \(\binom mr=0\) when \(r<0\) or \(r>m\).

## Proof
**1. Hypergeometric reduction.** A species occupying \(d\) sites occurs in exactly one selected site in precisely \(d\binom{N-d}{k-1}\) of the \(\binom Nk\) possible samples: choose its single occupied site, then the remaining \(k-1\) sites outside its occupancy set. By linearity of expectation, without assuming independence of the two species,
\[
u_k=\frac{a\binom{N-a}{k-1}+b\binom{N-b}{k-1}}{\binom Nk},\qquad 1\le k\le N.
\]
Consequently every occupancy arrangement with the same \(N,a,b\) has the same curve.

**2. A species alone cannot produce two peaks.** Let \(g_d(k)=d\binom{N-d}{k-1}/\binom Nk\). On its positive range and for \(k<N\),
\[
\frac{g_d(k+1)}{g_d(k)}=\frac{(k+1)(N-d-k+1)}{k(N-k)}.
\]
The sign of \(g_d(k+1)-g_d(k)\) agrees with the sign of \(N+1-d(k+1)\), until the sequence becomes identically zero. That expression decreases strictly with \(k\); therefore the sequence is unimodal (allowing a tie at the mode), and it has at most one strict interior local maximum.

**3. Exhaustive sharp finite classification.** The accompanying standalone `verify.py` implements the displayed hypergeometric formula with exact integer binomial coefficients and reduced rational numbers. It loops over **every** \(N\in\{2,\ldots,15\}\), every \(1\le a\le b\le N\), and every integer sample depth \(1\le k\le N\). For each exact profile, it tests all \(2\le k\le N-1\) strict-peak inequalities using exact rational comparisons. This is a finite proof because the formula already reduces arbitrary incidence matrices to these exhaustive integer parameter triples. There are
\[
\sum_{N=2}^{15}\frac{N(N+1)}2=679
\]
parameter triples. The complete class counts of profiles with at least two strict interior maxima are zero at every \(N=2,\ldots,14\), and exactly one at \(N=15\), namely \((a,b)=(2,9)\). The program asserts these outcomes, rather than merely printing exploratory diagnostics.

**4. Exact witness.** For \((N,a,b)=(15,2,9)\), the exact values at the relevant depths are
\[
\begin{array}{c|rrrrrrrr}
k&1&2&3&4&5&6&7&8\\\hline
u_k&11/15&16/21&291/455&752/1365&1565/3003&2628/5005&1147/2145&8/15
\end{array}
\]
(with subsequent values listed in the executable witness certificate). Direct fraction comparison yields \(u_1<u_2>u_3\), \(u_4>u_5<u_6<u_7>u_8\), and thus two strict interior maxima. The same executable independently enumerates all \(2^{15}\) labeled site subsets for each of a disjoint and a nested occupancy arrangement, recomputes \(u_k\) from actual observed counts, and verifies equality with the formula at all fifteen sample sizes. Thus the sharp witness does not depend on species co-occurrence assumptions.

**5. Contrast with normalization.** For any species of occupancy \(d\), using \(k\binom Nk=N\binom{N-1}{k-1}\),
\[
\frac{g_d(k)}k=\frac dN\frac{\binom{N-d}{k-1}}{\binom{N-1}{k-1}}.
\]
The ratio of binomial coefficients is the probability that a uniform \((k-1)\)-subset of the other \(N-1\) sites avoids the \(d-1\) other occupied sites, so it is nonincreasing with \(k\). Summing over species proves the stated normalization contrast for any fixed incidence matrix.

## Verification
Run `python3 verify.py` with Python 3 and no third-party dependencies. It performs all \(679\) exact occupancy-profile comparisons through fifteen sites, verifies the normalized monotonicity inequality for each, and independently checks \(65{,}536\) site subsets across disjoint and nested realizations of the witness. Expected output begins `VERIFY_OK census_pairs=679 scaled_profiles=679 direct_subsets=65536`. These are complete finite enumerations for the specified finite domain; they provide no inference about untested site counts.

## Relationship to prior work
Patil and Taillie (2001) derived the general hypergeometric linear relation between the population range distribution and expected sample-incidence frequencies. Specializing that known framework to sample frequency one gives the displayed expectation formula; **the formula is not claimed as new**. Ugland, Gray and Ellingsen (2003) developed exact sample-based species-accumulation expressions for the different statistic of species appearing at least once. Hui and McGeoch (2014) linked singleton incidences \(F_{1,k}\) and the normalized novelty rate \(F_{1,k}/k\) to zeta-diversity partitioning; the present classification concerns the raw expected singleton count \(\mathbb E[F_{1,k}]\), rather than normalized discovery rate or cumulative richness. The sharp minimum \(N=15\) and uniqueness of the occupancy pair \(\{2,9\}\) are not stated in these inspected sources. The new finite enumeration is a classification within those established incidence models, not a new sampling distribution.

## Limitations
The complete assertion is restricted to two species and at most fifteen sites; no claim is made about the number or locations of maxima for arbitrary larger surveys. The two peaks have different heights, and the secondary increase is small: \(u_7-u_5=1147/2145-1565/3003\). Such a difference may be swamped by finite field-survey noise; the result is an exact information/design boundary, not evidence that ecological field data will visibly exhibit two peaks. Sampling is assumed uniform without replacement with perfect detection and fixed incidences. Although the full parameter set is exhausted, published sources not found by the literature searches might have established the same cutoff; independent scholarly validation has not been performed.

## References
1. Patil, G. P. and Taillie, C. (2001). *Estimation of species richness based on species range*. Community Ecology **2**, 209–211. https://doi.org/10.1556/ComEc.2.2001.2.8 . Online publication recorded as 30 December 2001.
2. Ugland, K. I., Gray, J. S. and Ellingsen, K. E. (2003). *The species–accumulation curve and estimation of species richness*. Journal of Animal Ecology **72**, 888–897. https://doi.org/10.1046/j.1365-2656.2003.00748.x . First published 15 August 2003.
3. Hui, C. and McGeoch, M. A. (2014). *Zeta diversity as a concept and metric that unifies incidence-based biodiversity patterns*. The American Naturalist **184**. https://doi.org/10.1086/678125 . Published 24 September 2014.
