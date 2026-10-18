# Exact second-moment law and nonconcentration of shortest absent binary subsequences

## Finding
Fix the ambient alphabet \(\{0,1\}\), including when the source word uses only one letter. For a finite binary word \(w\), let \(S(w)\) be the number of *distinct shortest absent subsequences*: binary words of minimum length not obtainable by deleting positions from \(w\) while maintaining order. The empty source has \(S(\varepsilon)=2\).

For nonnegative integers \(a,b\), define the first and second raw totals
\[
 A_{a,b}=\sum_{\substack{|w|_0=a\\|w|_1=b}}S(w),\qquad
 B_{a,b}=\sum_{\substack{|w|_0=a\\|w|_1=b}}S(w)^2.
\]
The complete bivariate generating functions are
\[
 \begin{aligned}
 F_1(x,y)&=\sum_{a,b\ge0}A_{a,b}x^ay^b
 =\frac{2-x-y}{1-x-y-2xy+2x^2y+2xy^2-x^2y^2},\\[2mm]
 F_2(x,y)&=\sum_{a,b\ge0}B_{a,b}x^ay^b
 =\frac{4-3x-3y+2x^2y+2xy^2-2x^2y^2}
 {1-x-y-4xy+4x^2y+4xy^2-x^2y^2-2x^3y^2-2x^2y^3+2x^3y^3}.
 \end{aligned}
\]
Consequently, for a uniformly random binary word \(W_{n,k}\) of length \(n\) with exactly \(k\) ones, for every \(n\ge0\) and \(0\le k\le n\),
\[
 \operatorname{Var} S(W_{n,k})=
 \frac{B_{n-k,k}}{\binom nk}-
 \left(\frac{A_{n-k,k}}{\binom nk}\right)^2.
\]
This is an exact all-length, all-composition variance formula with coefficients specified by explicit rational functions. For example, at length \(10\) and weight \(5\), the mean is \(185/42\) and the variance is \(12331/588\).

There is also a sharp nonconcentration phenomenon for an independent, uniformly random binary word \(W_n\). Define the polynomials
\[
 P_1(z)=1-z-3z^2+z^3,\qquad
 P_2(z)=1-z-5z^2+3z^3+2z^4-2z^5,
\]
and let \(r_1\in(0.460811,0.460812)\) and \(r_2\in(0.406865,0.406866)\) be their respective smallest-modulus roots. Each is positive, real and simple. Then
\[
 \begin{aligned}
 \mathbb E S(W_n)&\sim C_1(2r_1)^{-n},\\
 \mathbb E S(W_n)^2&\sim C_2(2r_2)^{-n},\\
 \operatorname{Var}S(W_n)&\sim C_2(2r_2)^{-n},
 \end{aligned}
\]
where
\[
 C_1=\frac{2}{-r_1P_1'(r_1)}\approx1.38760048,
 \qquad C_2=\frac{2(2+r_2-r_2^2-r_2^3)}{-r_2P_2'(r_2)}\approx3.22461941.
\]
In particular the coefficient of variation increases exponentially:
\[
 \frac{\sqrt{\operatorname{Var}S(W_n)}}{\mathbb E S(W_n)}
 \sim\frac{\sqrt{C_2}}{C_1}
 \left(\sqrt{\frac{2r_1^2}{r_2}}\right)^n
 \approx1.2941207\,(1.02167385)^n.
\]
Thus the number of shortest absent subsequences is not concentrated on the scale of its mean in the uniform binary model.

## Assumptions and scope
A subsequence means a scattered, order-preserving subsequence; multiplicities of different embeddings are ignored. The alphabet is always the *fixed binary alphabet*, not the support of the source. The variables \(x,y\) mark zeros and ones of the **source**, not the target. All generating-function equalities are identities of formal power series. The variance statement covers the boundary compositions \(k=0\), \(k=n\), and the empty word. The asymptotic statement uses the uniform source model only, not an arbitrary fixed-composition model.

## Proof
**Arch factorization.** Read a binary source from left to right and end each arch as soon as both symbols have appeared. Every complete arch has the unique form \(b^r\bar b\), with \(r\ge1\) and \(\bar b=1-b\); the remainder is empty or a constant-letter run. Suppose there are \(m\) complete arches. Every binary target of length at most \(m\) is a subsequence, because its next symbol can be matched within the next complete arch. At least one target of length \(m+1\) is absent: choose the last symbol of every arch, followed by the symbol missing from the remainder. Therefore the shortest absent length is exactly \(m+1\).

Match a fixed target \(t_1\cdots t_{m+1}\) greedily, always taking the leftmost possible source occurrence of the next letter. Since each complete arch contains both binary symbols, failure to match the target occurs **if and only if** each arch consumes precisely one target letter and the remainder avoids the final target letter. Indeed, consuming at least two letters in one arch would, together with at least one letter from each other arch if needed, finish the target. Conversely, one consumption per arch leaves its final letter unmatched, and the stated remainder condition prevents completion.

For a single arch \(b^r\bar b\), consumption of exactly one letter imposes the following complete local rule. If the current target letter is \(\bar b\), it matches at the end of the arch, and the next target letter is unrestricted. If the current letter is \(b\), then the run length must be \(r=1\) and the next target letter must also be \(b\); otherwise greedy matching consumes at least two letters in this arch. This also handles the first and final arches without exceptions.

**First moment transfer.** Let \(u=xy\), \(L_0=xy/(1-y)\), and \(L_1=xy/(1-x)\). With target-letter states ordered \(0,1\), the matrix summing allowed arch weights is
\[
 T_1=\begin{pmatrix}L_0+u&L_0\\L_1&L_1+u\end{pmatrix}.
\]
An absent terminal target letter \(0\) allows an empty remainder or a positive run of ones; letter \(1\) allows an empty remainder or a positive run of zeros. Accordingly, \(v_1=(1/(1-y),1/(1-x))^\mathsf T\). Every pair (source, absent target) is counted exactly once by its unique arch decomposition and target letters. Therefore
\[
 F_1=(1,1)(I-T_1)^{-1}v_1,
\]
which reduces by the two-by-two inverse formula to the first displayed rational function.

**Second moment transfer.** The square \(S(w)^2\) counts ordered pairs of shortest absent targets, which share the source arches. A pair has four possible current-letter states \(00,01,10,11\). The exchange of the two targets identifies the two *mixed* states for evaluating the same terminal function. Working in the resulting symmetric three-dimensional invariant subspace, with coordinates \(00\), mixed, \(11\), the arch transition matrix is
\[
 T_2=\begin{pmatrix}
 \frac{xy(2-y)}{1-y}&\frac{2xy}{1-y}&\frac{xy}{1-y}\\
 xy&2xy&xy\\
 \frac{xy}{1-x}&\frac{2xy}{1-x}&\frac{xy(2-x)}{1-x}
 \end{pmatrix}.
\]
For example, in state \(01\), an arch \(01\) allows next states \(00,01\), while an arch \(10\) allows \(01,11\); no longer arch is permitted. This yields the mixed-state row \((xy,2xy,xy)\). In state \(00\), long arches beginning with \(1\) are permitted, explaining the geometric factors \(1/(1-y)\). The terminal weights are \(v_2=(1/(1-y),1,1/(1-x))^\mathsf T\): a nonempty remainder can avoid both final target letters only when those letters coincide. Summation over all initial ordered pairs counts the mixed coordinate twice. Consequently
\[
 F_2=(1,2,1)(I-T_2)^{-1}v_2.
\]
Clearing denominators in this explicit three-by-three identity gives exactly the second displayed rational function. The finite-state formula proves the all-length identity; computation is not needed to extend a finite pattern.

**Variance and asymptotics.** At fixed composition \((a,b)\) there are exactly \(\binom{a+b}b\) equiprobable source words. Dividing the coefficient totals by that number proves the mean, second moment, and variance identities. Substitution \(x=y=z\) and cancellation of removable factors yield
\[
 F_1(z,z)=\frac{2}{P_1(z)},\qquad
 F_2(z,z)=\frac{2(2+z-z^2-z^3)}{P_2(z)}.
\]
The coefficients of \(F_j(z,z)\) are the sums of the corresponding powers of \(S(w)\) over all length-\(n\) binary sources; division by \(2^n\) gives the moments for \(W_n\).

For completeness, the positivity and aperiodicity needed for dominant-pole extraction hold directly in the displayed transfer matrices. For each positive \(z<1\), all their entries are strictly positive when \(x=y=z\). Their Perron eigenvalues are strictly increasing in \(z\), start at zero, and reach one before \(z=1\). Thus the first positive singularity is a simple pole. Furthermore at any \(z\) on the same modulus circle but not positive real, an arch-loop entry with both length-two and length-three terms has strictly smaller modulus than its positive-real value. Irreducibility then gives spectral radius strictly below one, so the dominant pole is unique. Rational-interval sign checks put the poles in the stated intervals; the positive residues produce \(C_1\) and \(C_2\). Finally \(r_2<0.406866<2(0.460811)^2<2r_1^2\), so \((2r_2)^{-1}>(2r_1)^{-2}\). The squared mean is exponentially negligible relative to the second moment, establishing the variance and coefficient-of-variation limits.

## Verification
Run `python3 check_moments.py`. The standalone standard-library checker independently enumerates every binary source of lengths \(0\) through \(14\), constructs each shortest absent-target set directly, and compares its first and second powers against coefficients of the two rational functions. It also directly enumerates allowed arch words and ordered target pairs, checking both transfer constructions for all total degrees through \(12\), verifies one fixed-composition example exactly, and isolates the asymptotic poles by rational sign tests. These finite checks are independent supporting tests, not substitutes for the formal arch bijection and matrix identities.

## Relationship to prior work
Kosche, Koß, Manea, and Siemer introduced and characterized shortest absent subsequences, including their arch structure, in *Absent Subsequences in Words* (first public version 2021). Adamson and coauthors' *Tight Bounds for the Number of Absent Subsequences* (first public version 2024) investigates extremal missing-subsequence counts at fixed universality index; Manea and coauthors (2025) investigate optimal enumeration algorithms. Those inspected papers supply the established framework but not the conditional second-moment rational function or the nonconcentration law above. A previously available length-only generating function for the **first** moment, \(2/P_1(z)\), is recovered by specialization, not claimed as new. It does not determine the second moment or variance, even without conditioning on composition. Exact simultaneous first-and-second composition moments and the exponential relative-fluctuation conclusion are the contribution here.

## Limitations
This theorem determines only the first two moments, not the complete probability distribution or its limiting law. No asymptotic at a moving fixed composition \(k/n\) is asserted. The transfer construction relies on the two-letter arch form and does not establish formulas for alphabets of size three or more. An equivalent formula may exist in literature not accessible through the inspected search sources; no independent review has been performed.

## References
1. M. Kosche, T. Koß, F. Manea, S. Siemer, *Absent Subsequences in Words*, arXiv:2108.13968 (first submitted 2021-08-31), Theorem 3.4 and the arch framework. https://arxiv.org/abs/2108.13968
2. D. Adamson, P. Fleischmann, A. Huch, F. Manea, P. Sarnighausen-Cahn, M. Wiedenhöft, *Tight Bounds for the Number of Absent Subsequences*, arXiv:2407.18599 (first submitted 2024-07-26), Sections 3–5. https://arxiv.org/abs/2407.18599
3. F. Manea, T. Ringleb, S. Siemer, M. Winkler, *Efficiently Finding All Minimal and Shortest Absent Subsequences in a String*, arXiv:2504.21471 (2025), Sections 1–6. https://arxiv.org/abs/2504.21471
