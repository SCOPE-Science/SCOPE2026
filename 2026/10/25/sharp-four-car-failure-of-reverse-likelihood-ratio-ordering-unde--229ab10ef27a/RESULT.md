# Sharp four-car failure of reverse likelihood-ratio ordering under biased parking preferences

## Finding
For the classical forward linear-probing model, let \(L\) count lucky cars and \(D\) total displacement. At every size \(1\le n\le3\), for **every** strictly positive distribution of independent parking preferences, the conditional joint law of \((L,D)\) is reverse totally positive of order two (reverse-TP2): its \(2\times2\) minors on increasing row and column indices are nonpositive. This universal ordering first fails at \(n=4\). In particular, the iid preference probabilities \((1/3,1/6,1/3,1/6)\) yield a strictly **positive** minor of size \(1024\) in unnormalized integer weights, corresponding to a conditional odds reversal.

## Assumptions and scope
There are \(n\) ordered cars, \(n\) ordered sites, and independent identically distributed preferences \(A_i\in\{1,\ldots,n\}\), with \(\Pr(A_i=j)=p_j>0\). Cars arrive in index order. Each car occupies the first free site at or beyond its chosen site, or fails if none exists. Condition throughout on the positive-probability event that all cars park. Let \(B_i\) be car \(i\)'s occupied site, \(L=\sum_i\mathbf1\{B_i=A_i\}\), and \(D=\sum_i(B_i-A_i)=n(n+1)/2-\sum_iA_i\). Define \(P_{\ell,d}=\Pr(L=\ell,D=d\mid\text{all park})\), with zero outside the support. Reverse-TP2 means, for all \(\ell<\ell'\) and \(d<d'\),
\[
P_{\ell,d}P_{\ell',d'}-P_{\ell,d'}P_{\ell',d}\le0.
\]
It is a likelihood-ratio ordering condition, stronger than mere negative covariance or ordinary stochastic ordering. No claim is made for these weaker properties.

## Proof
For \(n=1\), the support is \(\{(1,0)\}\). For \(n=2\), it is \(\{(1,1),(2,0)\}\). For \(n=3\), exhaustive inspection of the \(3^3=27\) preference words by the explicit parking rule gives precisely
\[
\{(1,2),(1,3),(2,1),(2,2),(3,0)\}.
\]
Every strictly positive preference law gives positive mass to each of these cells. In each size \(n\le3\), higher lucky-count rows have displacement support entirely to the left of lower lucky-count rows, possibly touching at a single displacement value; thus every reverse-TP2 determinant is either zero or negative. This proves the universal small-size assertion without assuming uniform preferences.

For \(n=4\), assign preference weights \(w=(2,1,2,1)\), so that \(p=w/6\). For each successful preference word \(a=(a_1,a_2,a_3,a_4)\), assign multiplicative weight \(\omega(a)=\prod_iw_{a_i}\). Let \(W_{\ell,d}\) be the total weight of words with the indicated luck and displacement. Write the preference histogram as \((c_1,c_2,c_3,c_4)\). The following lists give the COMPLETE word multiplicities contributing to each of four required cells:

| Cell \((\ell,d)\) | Histogram : multiplicity | Weighted mass |
|---|---|---:|
| \((2,2)\) | \((1,2,1,0):4\); \((2,0,2,0):6\); \((2,1,0,1):4\) | \(4\cdot4+6\cdot16+4\cdot4=128\) |
| \((2,3)\) | \((1,3,0,0):4\); \((2,1,1,0):5\); \((3,0,0,1):4\) | \(4\cdot2+5\cdot8+4\cdot8=80\) |
| \((3,2)\) | \((1,2,1,0):8\); \((2,1,0,1):8\) | \(8\cdot4+8\cdot4=64\) |
| \((3,3)\) | \((2,1,1,0):6\) | \(6\cdot8=48\) |

The histogram multiplicities can be reproduced by looping over all \(4^4=256\) words and applying the explicit deterministic parking rule (see `verify.py`); each multiset-class multiplicity is strictly a count of parking-success words with both specified statistics, not a multinomial coefficient. As \(\omega(a)=2^{c_1+c_3}\), these totals are exact integers. The purported reverse-TP2 determinant for luck levels 2 and 3 and displacements 2 and 3 equals
\[
128\cdot48-80\cdot64=1024>0.
\]
Normalizing by the common positive success-weight total \(776\) multiplies this determinant by \(776^{-2}\), retaining its sign. The corresponding conditional likelihood ratios increase with displacement:
\[
\frac{P_{3,3}}{P_{2,3}}=\frac35>\frac12=\frac{P_{3,2}}{P_{2,2}}.
\]
This contradicts reverse-TP2. Together with the universal support argument for \(n\le3\), the first possible counterexample size is exactly four. \(\square\)

## Verification
The standalone `verify.py` enumerates every preference word for all sizes \(1\le n\le4\), independently uses a set-of-free-sites parking simulator, checks the exact small-size supports, tabulates the four weighted cells and contributing histograms, verifies the success-weight total and determinant, and checks every reverse-TP2 inequality for \(n\le3\) for several positive weight profiles. The universal \(n\le3\) claim follows analytically from the complete support lists, not from tests on selected weights. The finite \(n=4\) witness has an exhaustive exact certificate, with no floating-point approximation.

## Relationship to prior work
Gessel and Seo's 2005 preprint (Section 10, Theorem 10.1) enumerates the **unweighted luck marginal**, not the weighted luck-displacement likelihood-ratio minors. Stanley and Yin (2023, Theorem 2.1) give a joint unweighted enumerator for unluckiness and displacement together with additional statistics; their coefficients correspond to equal preference weights and do not give the four preference-histogram-sensitive weighted cells here. Kenyon and Yin (2021, Section 2.3) treat a joint enumerator for **critical left-to-right maxima** and displacement; critical left-to-right maxima are not the event that a car parks in its preferred site. Colmenarejo et al. (2024) study lucky counts and displacement on the restricted Stirling-permutation family, whose total displacement is constant, and hence their result cannot settle biased four-car conditional minors. These distinctions do not establish absolute historical priority; the result is a concrete sharp boundary for a natural likelihood-ratio hypothesis.

## Limitations
The positive minor disproves universal reverse-TP2 only. It does not refute negative correlation or stochastic monotonicity of luck against displacement, establish a sign characterization for all four-car probability vectors, or show the first possible failure under *uniform* preferences. It conditions on successful completion and assumes iid strictly positive site preferences. Historical novelty is subject to further independent evaluation.

## References
1. Gessel–Seo, *A Refinement of Cayley's Formula for Trees*, arXiv:math/0507497v1, first posted 2005-07-24, Section 10, Theorem 10.1. https://arxiv.org/pdf/math/0507497.
2. Stanley–Yin, *Some Enumerative Properties of Parking Functions*, arXiv:2306.08681v1, Theorem 2.1. https://arxiv.org/pdf/2306.08681.
3. Kenyon–Yin, *Parking Functions: From Combinatorics to Probability*, arXiv:2103.17180v1, Section 2.3. https://arxiv.org/pdf/2103.17180.
4. Colmenarejo et al., *On the Lucky and Displacement Statistics of Stirling Permutations*, arXiv:2403.03280v1, Sections 1 and 5. https://arxiv.org/pdf/2403.03280.
