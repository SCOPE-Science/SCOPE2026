# Sharp cyclic-variation stability of two-cell conditional expectations

## Finding
Fix an integer \(n\ge 3\). Color every vertex of a cyclically ordered \(n\)-point set either \(A\) or \(B\), with both colors present. Give each vertex a strictly positive mass \(m_i\). Let \(P_m\) replace every signal value by the mass-weighted mean of its color class. Write
\[
V(x)=\sum_{i=0}^{n-1}|x_{i+1}-x_i|,
\]
with indices modulo \(n\). Let \(r\) be the number of maximal cyclic runs of color \(A\), equivalently of color \(B\). Put \(a=\sum_{i\in A}m_i\), \(b=\sum_{i\in B}m_i\), and
\[
c_i=\begin{cases}m_i/a,&i\in A,\\-m_i/b,&i\in B.\end{cases}
\qquad S_{-1}=0,\qquad S_j=\sum_{i=0}^{j}c_i\quad(0\le j<n).
\]
In particular \(S_{n-1}=0\). Then the **exact** variation-seminorm operator norm is
\[
\boxed{\displaystyle K(P_m)=\sup_{V(x)>0}\frac{V(P_mx)}{V(x)}
=r\left(\max_{-1\le j<n}S_j-\min_{-1\le j<n}S_j\right).}
\]
The supremum is attained by the indicator of a proper cyclic interval; hence the same constant is the sharp two-data Lipschitz modulus \(\sup_{V(x-y)>0}V(P_mx-P_my)/V(x-y)\).

**Complete contraction classification.** The following are equivalent:

1. \(V(P_mx)\le V(x)\) for every real signal \(x\).
2. \(K(P_m)=1\).
3. Every maximal \(A\)-run carries exactly \(a/r\) of the \(A\)-mass, and every maximal \(B\)-run carries exactly \(b/r\) of the \(B\)-mass.

With uniform vertex masses, the third condition says that all \(A\)-runs have the same length and all \(B\)-runs have the same length, i.e. the cyclic color word is a repetition of one \(A^s B^t\) block (up to rotation).

**Sharp achievable amplification range.** For a fixed cyclic two-color word having \(r\) runs of each color, allow all strictly positive vertex masses to vary. If \(r=1\), its variation norm is always \(1\). If \(r\ge2\), the attainable constants are **exactly** \([1,r)\). The upper endpoint \(r\) is a nonattained supremum as masses become concentrated in one adjacent pair of opposite-color runs. The lower endpoint is attained precisely by the run-mass balance above. These conclusions hold despite \(P_m\) being an idempotent positive averaging operator that contracts the supremum norm and the ordinary oscillation seminorm.

## Assumptions and scope
Signals are real vectors indexed by a finite *simple* cycle of length \(n\ge3\). Both color classes are nonempty, masses are strictly positive, and the input and output use the same unweighted cyclic edge-total-variation seminorm. The means are normalized separately within their respective classes; vertex masses affect the averaging operator but not the edge-variation weights. The underlying two-cell conditional expectation is
\[
(P_mx)_i=\begin{cases}
\frac1a\sum_{j\in A}m_jx_j,&i\in A,\\
\frac1b\sum_{j\in B}m_jx_j,&i\in B.
\end{cases}
\]
There is no assumption that each color class is connected. The result classifies *all* such two-cell partitions and positive masses, not general partitions into three or more classes.

## Proof
**1. Rank-one reduction.** Define \(\ell(x)=\sum_i c_ix_i\), the difference between the two color-class means. The output alternates between these two means exactly \(2r\) times as one traverses the cycle. Therefore
\[
V(P_mx)=2r|\ell(x)|.
\]
The coefficient vector has zero total sum: \(\sum_i c_i=1-1=0\).

**2. Exact dual variation norm.** Write \(d_i=x_{i+1}-x_i\), with cyclic indices. Then \(\sum_i d_i=0\). Summation by parts, including the endpoint identity \(S_{n-1}=0\), yields
\[
\ell(x)=-\sum_{i=0}^{n-1}S_i d_i.
\]
Let \(S_{\max}\) and \(S_{\min}\) be the largest and smallest prefix sums. Subtracting their midpoint from every \(S_i\) does not change the right side because \(\sum_i d_i=0\). Consequently
\[
|\ell(x)|\le\frac{S_{\max}-S_{\min}}2\sum_i|d_i|
=\frac{S_{\max}-S_{\min}}2 V(x).
\]
This bound is exact. Choose two distinct edges at which the prefix sums achieve their maximum and minimum, put gradient \(+1\) at one edge, gradient \(-1\) at the other, and zero gradients elsewhere. The resulting cyclic vector is, up to a constant and a sign, the indicator of a nonempty proper cyclic interval. Its variation equals \(2\), and \(|\ell(x)|=S_{\max}-S_{\min}\). Combining this equality with step 1 gives the displayed exact norm and its attainment. Since \(P_m\) is linear, this also proves the two-input assertion.

**3. Rigidity at norm one.** Moving around any maximal \(A\)-run increases the prefix sum by its mass divided by \(a\). The \(r\) positive increments sum to \(1\). Each increment is bounded above by the overall range \(\Delta=S_{\max}-S_{\min}\), so \(\Delta\ge1/r\), and \(K(P_m)=r\Delta\ge1\). If \(K(P_m)=1\), every one of the \(r\) positive increments must be exactly \(1/r\). The same argument applied to the \(r\) negative \(B\)-run increments shows that every \(B\)-run has normalized mass \(1/r\). Conversely, these equal alternating increments and decrements force the prefix sums to oscillate between two levels separated by exactly \(1/r\), even if the chosen starting index splits a cyclic run. Thus \(\Delta=1/r\) and \(K(P_m)=1\). The uniform-mass word classification follows by converting equal run masses to equal run lengths.

**4. Full mass-design range.** Every normalized proper cyclic interval contains some but not all positive mass of at least one color when \(r\ge2\). As a result, its normalized class-mass discrepancy has absolute value strictly below \(1\); there are finitely many intervals, so \(\Delta<1\) and \(K(P_m)<r\). For each fixed color word, select an adjacent \(A\)-run and \(B\)-run. Give a chosen vertex in each run mass \(1\), and every other vertex mass \(\varepsilon>0\). As \(\varepsilon\downarrow0\), the positive increment in the chosen \(A\)-run and the following negative increment in the chosen \(B\)-run both tend to \(1\), whence \(\Delta\to1\) and \(K(P_m)\to r\). Balanced strictly positive weights exist by assigning equal total mass to each run of each color. Finally, the map from positive mass vectors to \(K(P_m)\) is continuous (a finite maximum of rational continuous functions with positive denominators), and the positive mass domain is path connected. The intermediate value theorem yields every constant in \([1,r)\). When \(r=1\), the formulas force \(\Delta=1\) for any positive masses, giving constant \(1\).

## Verification
The accompanying standalone `check.py` uses exact rational arithmetic. It compares the prefix-sum norm against a direct enumeration of all proper cyclic-interval extremizers for \(2010\) combinations of colorings and positive mass vectors; it independently checks the run-balance equivalence, the \(r\)-bound, nonuniform examples, and positive-weight approaches to the nonattained upper endpoint. The code tests every anchored binary color word of lengths \(3\) through \(9\) under two mass profiles, plus reproducible randomly generated longer words. This is a finite diagnostic only; steps 1–4 are the proof for all \(n\) and all real positive masses.

For instance, on six positions with cyclic colors \(A,A,B,A,B,B\) and unit masses, the prefix range is \(2/3\), with \(r=2\), so the sharp constant is \(4/3\). The input \((1,1,0,0,0,0)\) attains it. Keeping the same coloring but choosing masses \((1,1,2,2,1,1)\) balances the normalized mass of every run and reduces the exact constant to \(1\). A single pass of prefix-sum extrema computes the norm in \(O(n)\) arithmetic operations and identifies an attaining interval.

## Relationship to prior work
Variation-diminishing interpolation on periodic Cartesian grids is established by Nochetto and Salgado (2012, Theorem 3.7), using a distinct continuous finite-element operator. Their contraction theorem does not classify the two-cell conditional expectations on arbitrary interlaced color sets or the full mass-dependent stability range here. Sandryhaila and Moura (2013, Section III) describe discrete cyclic total variation and graph filtering; their spectral-frequency analysis does not give the present operator norm and run-balance rigidity. Gaubert and Qu (2013, Theorem 1.1) analyze Markov-operator contraction in the *oscillation* seminorm and its dual, whereas this result uses the sum of absolute differences across adjacent cyclic sites. In particular, every \(P_m\) above is nonexpansive in ordinary oscillation while its cyclic-variation norm may be arbitrarily close to \(r\). The new claim does not assert novelty for the elementary definitions of conditional expectation, total variation, or generic dual-norm principles. An equivalent specialized binary-partition formula hidden in older literature cannot be excluded.

## Limitations
The classification requires exactly two output classes, strictly positive input masses, unweighted cyclic variation, and a real finite signal. It does not identify the sharp modulus for multiple output classes, arbitrary connected graphs, continuous function spaces, or independently weighted variation edges. The upper endpoint \(r\) is a supremum over different positive mass choices, not a finite-mass equality for \(r\ge2\). Exhaustive tests of bounded dimensions are not a replacement for the infinite-family proof. Independent scientific validation has not been performed.

## References
1. R. H. Nochetto and A. J. Salgado, *A Total Variation Diminishing Interpolation Operator and Applications*, arXiv:1211.1069 (first posted 2012-11-05). Original Theorem 3.7 and construction, pp. 3–4. https://arxiv.org/abs/1211.1069
2. A. Sandryhaila and J. M. F. Moura, *Discrete Signal Processing on Graphs: Frequency Analysis*, arXiv:1307.0468 (first posted 2013-07-01). Section III, pp. 3–4. https://arxiv.org/abs/1307.0468
3. S. Gaubert and Z. Qu, *Dobrushin's Ergodicity Coefficient for Markov Operators on Cones*, arXiv:1307.4649 (first posted 2013-07-17). Theorem 1.1 and introduction, pp. 1–3. https://arxiv.org/abs/1307.4649
