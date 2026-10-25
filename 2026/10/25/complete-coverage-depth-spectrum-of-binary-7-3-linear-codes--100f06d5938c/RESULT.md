# Complete coverage-depth spectrum of binary \([7,3]\) linear codes

## Finding

Let \(\mathcal C\) run over all distinct binary \([7,3]\) linear codes with **fixed, labeled coordinates**, and let \(\mu(\mathcal C)\) be the expected number of independent uniformly sampled coordinate positions, with replacement, needed for the sampled generator-matrix columns to span \(\mathbb F_2^3\). There are exactly \(11811\) such codes. **The multiset of values of \(\mu(\mathcal C)\) has precisely \(42\) distinct rational levels.** Its complete exact probability mass function is in `coverage_depth_spectrum.csv`: for each level, the number in `binary_linear_codes` divided by \(11811\) is its probability under a uniformly selected code.

For this uniform code ensemble, the exact mean and variance **across code designs**, not the variance of the waiting time inside a fixed code, are
\[
\mathbb E_{\mathcal C}\,\mu(\mathcal C)=\frac{509611}{78740},\qquad
\operatorname{Var}_{\mathcal C}(\mu(\mathcal C))=\frac{759156664}{232499535}.
\]

A structural refinement identifies the entire second level. The minimum value \(47/12\) is attained by the known simplex construction, on \(30\) labeled codes. The next value is \(17/4\), attained by exactly \(630\) labeled codes. Every code at that second level has a generator matrix whose seven columns consist of all but one of the seven nonzero vectors in \(\mathbb F_2^3\), with a different one of the six retained vectors repeated once. Conversely, every such matrix attains \(17/4\). All these second-level codes are equivalent under coordinate permutations; there are \(42\) distinct column-multiplicity profiles before quotienting by invertible row operations. The values \(47/12\) and the lower bound \(17/4\) were already reported in the originating paper; the new result is the complete distribution, its code-level multiplicities and variance, and the exhaustive equality classification at the second level.

## Assumptions and scope

A binary \([7,3]\) code means a three-dimensional subspace of \(\mathbb F_2^7\). Fix any rank-three \(3\times7\) generator matrix \(G\) of the code. In one trial, choose one of its seven **column positions** uniformly; positions are sampled independently with replacement. Stop as soon as the selected columns span the entire \(\mathbb F_2^3\). The expectation \(\mu(G)\) depends only on the row space of \(G\), so \(\mu(\mathcal C)\) is well defined. Generator matrices with zero or repeated columns are allowed, but the rank must be three. The outer distribution chooses a code uniformly from the \(11811\) distinct labeled binary \([7,3]\) codes; it is not a distribution over equivalence classes or over only zero-free codes.

Vectors in \(\mathbb F_2^3\) are represented by integers \(0,1,\ldots,7\), with bitwise exclusive-or for addition. Let \(c_v\) count occurrences of vector \(v\) among the seven columns. Thus \(\sum_{v=0}^{7}c_v=7\). For each nonzero normal vector \(a\), write \(L_a=\{v\ne0:a\cdot v=0\}\); each \(L_a\) has three elements.

## Proof

**Step 1: an exact formula for every column profile.** Set \(m_a=c_0+\sum_{v\in L_a}c_v\). The event that the span after \(t\) samples is proper has, by subspace-lattice Möbius inversion,
\[
\Pr(T>t)=\sum_{a=1}^{7}\left(\frac{m_a}{7}\right)^t
-2\sum_{v=1}^{7}\left(\frac{c_0+c_v}{7}\right)^t
+8\left(\frac{c_0}{7}\right)^t.
\]
This holds even for \(t=0\), with all zero powers interpreted as one. Indeed, the Möbius coefficients from dimensions two, one, zero to the ambient three-space are respectively \(1,-2,8\). For rank three every proper-subspace mass is strictly smaller than one. Summing the geometric series over all \(t\ge0\) therefore proves
\[
\boxed{\displaystyle
\mu(c)=\sum_{a=1}^{7}\frac{7}{7-m_a}
-2\sum_{v=1}^{7}\frac{7}{7-c_0-c_v}
+\frac{56}{7-c_0}.}
\]
Consequently this is an exact rational formula with no simulation or approximation.

**Step 2: exhaustive, finite reduction.** Two matrices differing only by reordering their columns share the profile \(c\), and every nonnegative integer profile of total seven corresponds to one unique nondecreasing seven-tuple of values in \(\{0,\ldots,7\}\). Their number is exactly \(\binom{14}{7}=3432\). The rank-three condition can be checked by closing the selected vectors under binary exclusive-or and asking whether the resulting set contains eight vectors. The complete census finds exactly \(2696\) full-rank profiles. On each one, the expression above produces a rational number; sorting and aggregating them yields exactly the \(42\) levels and the `profile_count` column of the supplied CSV. All \(3432\) possible profiles are examined, not merely sampled. The finite certificate is the complete `verify.py` program with no third-party dependencies.

**Step 3: counting labeled matrices and codes.** For each profile \(c\), exactly \(7!/\prod_{v=0}^{7}c_v!\) ordered matrices realize it. Aggregating these weights at each rational level produces the `ordered_full_rank_matrices` column. Its entries sum to
\[
(2^7-1)(2^7-2)(2^7-4)=1984248,
\]
the exact number of ordered rank-three \(3\times7\) binary matrices. Each labeled code has exactly \(|\operatorname{GL}_3(\mathbb F_2)|=168\) ordered generator matrices, since row bases are arbitrary and the action is free. Dividing each ordered-matrix count by \(168\) produces the code distribution and gives \(1984248/168=11811\) codes. Weighting the rational levels by their code counts and subtracting the squared mean gives the displayed exact variance. All divisions are exact.

**Step 4: equality geometry.** The rational comparison across the exhaustive profile census identifies exactly one profile at \(47/12\), with each nonzero vector appearing once, and exactly \(42\) profiles at \(17/4\). The latter are precisely the profiles obtained by choosing a missing nonzero vector \(u\), then a distinct duplicated nonzero vector \(v\): \(7\cdot6=42\) choices. Every full-rank profile outside those \(42\) and the simplex profile gives a larger expectation. Each second-level profile represents \(7!/2=2520\) ordered matrices, hence \(42\cdot2520/168=630\) labeled codes. The group \(\operatorname{GL}_3(\mathbb F_2)\) acts transitively on ordered pairs of distinct nonzero vectors (they are linearly independent), and column reordering removes remaining order, so all second-level codes form one coordinate-permutation equivalence class. Their sharp difference from the simplex expectation is \(17/4-47/12=1/3\), a numerical threshold known previously, not claimed as new here.

**Step 5: independent computation of every expectation.** For each ordered matrix, let \(\alpha_s\) be the number of its \(s\)-subsets of column positions that span \(\mathbb F_2^3\). The coupon-order identity
\[
\mu(G)=7H_7-\sum_{s=3}^{6}\frac{\alpha_s}{\binom6s}
\]
is evaluated independently from direct subset-rank calculations, for each of the \(2696\) profiles, and checked equal to the subspace Möbius formula. A separate enumeration of all \(8^7=2097152\) ordered matrices reproduces the multiplicities obtained by multinomial weighting. This checks both the mathematical reductions and every table entry, not just aggregate totals.

## Verification

Run `python3 verify.py` in a directory containing that program. It creates `coverage_depth_spectrum.csv` and prints the exact enumeration summary. The delivered CSV and `verification_output.txt` were generated by that same program. The output includes `FULL_RANK 2696`, `DISTINCT_BINARY_LINEAR_CODES 11811`, `DISTINCT_EXPECTATIONS 42`, `SECOND_BINARY_LINEAR_CODES 630`, the exact ensemble moments, and terminates with `VERIFY_OK`. The program is deterministic, uses only standard-library integer arithmetic and `Fraction`, and independently compares the two exact expectation formulas. A fresh extraction and replay is described in `VERIFICATION.md`.

## Relationship to prior work

Bertuzzo, Ravagnani and Yaakobi (2025), Section III, Example 1, already computed that the binary simplex \([7,3]\) code has expectation \(47/12\) and that other binary \([7,3]\) codes have expectation at least \(17/4\). These two **numerical values and the resulting gap are explicitly prior results**. Their subsequent general information-set formula is also prior and is used as an independent check here. Kong, Elishco, Wang and Duman (2026) and Gross, Grunbaum, Bertuzzo, Yaakobi and Ravagnani (2026) independently established general simplex optimality and its equality condition, which are not claimed as new. The latter paper also develops random-code **mean** coverage depth. The present finite-geometry contribution is the complete exact **distribution across all labeled codes**, its code-ensemble **variance** and the complete structural enumeration of second-level codes; these are not established in the inspected source statements.

## Limitations

This is a computer-assisted but mathematically finite and exhaustive classification at **binary dimension three and length seven only**. It does not imply corresponding code-level variance formulas or second-minimizer classifications for larger lengths, higher dimensions or larger alphabets. Uniform sampling assumes error-free reads and seven equiprobable strand positions; nonuniform synthesis or sampling and physical sequencing noise are excluded. Variance across randomly selected code designs must not be confused with the waiting-time variance for a fixed code. The historical published bound \(17/4\) and simplex optimality are credited. Equivalent unpublished tables or unindexed classifications are an originality risk. The supplied verifier is not an independent external audit.

## References

1. M. Bertuzzo, A. Ravagnani and E. Yaakobi, *The Coverage Depth Problem in DNA Storage Over Small Alphabets*, arXiv:2507.20639, first public 28 July 2025; especially Section III, Example 1, and Proposition 2. https://arxiv.org/abs/2507.20639
2. X. Kong, O. Elishco, C. Wang and T. M. Duman, *The Coverage Depth Problem in Distributed DNA Data Storage*, arXiv:2610.02931, first public 2 October 2026. https://arxiv.org/abs/2610.02931
3. R. Gross, Y. Grunbaum, M. Bertuzzo, E. Yaakobi and A. Ravagnani, *Optimal Codes for the Coverage Depth Problem and the Performance of Random Codes*, arXiv:2610.07370, first public 5 October 2026; Sections IV and VII. https://arxiv.org/abs/2610.07370
