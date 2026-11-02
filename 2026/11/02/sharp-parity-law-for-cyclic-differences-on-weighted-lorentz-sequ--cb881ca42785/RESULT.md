# Sharp parity law for cyclic differences on weighted Lorentz sequences

## Finding
Fix an integer \(n\ge2\) and positive nonincreasing real weights \(w_1\ge\cdots\ge w_n>0\). Write \(W_0=0\) and \(W_k=\sum_{j=1}^k w_j\). The norm on real vectors is \(\|x\|_w=\sum_{j=1}^n w_j x_j^*\), where \(x^*\) is the decreasing rearrangement of the absolute coordinate values. Set \((Sx)_j=x_{j-1\pmod n}\) and \(D=I-S\). Then
\[
\|D\|_w=\begin{cases}
2,&n\text{ even},\\
\max\left\{\displaystyle\max_{1\le k<n}\frac{W_{k-1}+W_{k+1}}{W_k},\ \frac{2W_{n-1}}{W_n}\right\},&n\text{ odd}.
\end{cases}
\]
For odd \(n\), \(\|D\|_w<2\) if and only if \(w_1>w_2>\cdots>w_n\). As a special case, for \(1<p<\infty\) and \(w_j=j^{1/p}-(j-1)^{1/p}\), the odd-dimensional norm is
\[
\|D\|_w=\left(1-\frac1{n-1}\right)^{1/p}+\left(1+\frac1{n-1}\right)^{1/p},
\]
and its defect is \(2-\|D\|_w=(p-1)/(p^2(n-1)^2)+O_p((n-1)^{-4})\) along odd dimensions.

## Assumptions and scope
All scalars are real. The cycle is the directed cyclic permutation on \(n\) coordinates, and the operator norm uses the **same** rearrangement-invariant norm in domain and codomain. Zero weights and increasing weights are excluded; strict positivity ensures a genuine norm, and decreasing weights make the Lorentz gauge subadditive. The dimensions and weights are otherwise arbitrary; the power-weight corollary assumes \(1<p<\infty\). In particular, this is not a result about a one-sided difference on infinite sequences, nor does it identify the spectrum or the numerical radius.

## Proof
**1. Reduction to ternary step vectors.** Let the absolute values of the entries of any nonzero \(x\) be \(a_1\ge\cdots\ge a_n\ge0\), with \(a_{n+1}=0\). For \(1\le k\le n\), define \(s^{(k)}\) to have on the positions of the \(k\) largest entries of \(x\) the corresponding signs and to vanish elsewhere. Then exactly
\[
x=\sum_{k=1}^n (a_k-a_{k+1})s^{(k)},\qquad
\|x\|_w=\sum_{k=1}^n(a_k-a_{k+1})W_k.
\]
By linearity and the triangle inequality, \(\|Dx\|_w/\|x\|_w\) is at most the largest of the ratios \(\|Ds^{(k)}\|_w/W_k\) for those \(k\) with nonzero coefficient. Conversely every nonzero signed support indicator is a vector in the space. Thus it suffices to maximize over all vectors with coordinates in \(\{-1,0,1\}\), not just a numerical sampling of such vectors.

**2. Proper supports.** Let \(s\) have \(1\le k<n\) nonzero entries. Its support splits into \(q\ge1\) nonempty connected arcs of the cyclic graph. Each arc contributes exactly two boundary edges of magnitude \(1\) to \(Ds\). Among its \(k-q\) internal edges, let \(b\le k-q\) connect opposite signs and hence contribute magnitude \(2\); the remaining internal edges contribute zero. Therefore the decreasing rearrangement of \(|Ds|\) consists of \(b\) copies of \(2\), then \(2q\) copies of \(1\), then zeros, so
\[
\|Ds\|_w=W_b+W_{b+2q}\le W_{k-q}+W_{k+q}\le W_{k-1}+W_{k+1}.
\]
The first inequality follows from the monotonicity of \(W\). For the second, the discrete increments \(w_j\) are nonincreasing, so \(W_{k-q}+W_{k+q}\) decreases as the integer spread \(q\ge1\) increases. Note \(k+q\le n\), because distinct support arcs are separated by distinct zero positions. Equality in both inequalities is attained for one contiguous arc of \(k\) active coordinates with alternating signs, giving \(b=k-1\) and \(q=1\). Hence, for each \(k<n\), the exact maximum is \((W_{k-1}+W_{k+1})/W_k\).

**3. Full supports.** If \(k=n\), every cyclic neighbor difference is either \(0\) or of absolute value \(2\). For even \(n\), alternating signs all around the cycle produce \(n\) changes and \(\|Ds\|_w/W_n=2\). For odd \(n\), there must be at least one unchanged edge (odd cycles cannot be properly two-colored); alternating signs except at one edge produce exactly \(n-1\) changes. Thus the sharp full-support ratio in odd dimensions is \(2W_{n-1}/W_n\). The step-vector reduction proves the full operator-norm formula.

**4. Characterization of the strict deficit.** For \(1\le k<n\),
\[
2W_k-(W_{k-1}+W_{k+1})=w_k-w_{k+1}\ge0.
\]
Also \(2W_n-2W_{n-1}=2w_n>0\). In odd dimensions the formula is therefore strictly less than \(2\) exactly when every consecutive weight inequality is strict. If some equality occurs, its corresponding proper-support ratio is exactly \(2\). Even dimensions attain \(2\) regardless of weights.

**5. Power weights.** Put \(\alpha=1/p\in(0,1)\); then \(W_k=k^\alpha\). For \(1\le k<n\), the proper-support ratio becomes \((1-1/k)^\alpha+(1+1/k)^\alpha\), which increases strictly with \(k\) by strict concavity and the decrease of the spread \(1/k\). The greatest proper-support ratio is at \(k=n-1\). By arithmetic-geometric mean, for every \(n\ge3\),
\[
\left(1-\frac1{n-1}\right)^\alpha+\left(1+\frac1{n-1}\right)^\alpha
\ge2\left(1-\frac1{(n-1)^2}\right)^{\alpha/2}
\ge2\left(\frac{n-1}{n}\right)^\alpha.
\]
The final comparison follows by squaring positive terms and checking \(1-1/(n-1)^2\ge(1-1/n)^2\). Hence the full-support branch cannot dominate. The Taylor expansion of \((1-t)^\alpha+(1+t)^\alpha\) at \(t=0\) has leading correction \(-\alpha(1-\alpha)t^2\) and remainder \(O_\alpha(t^4)\), establishing the stated asymptotic.

## Verification
The proof is valid for all admissible \(n\) and weights, independently of computation. A standalone exact rational checker enumerates every nonzero signed ternary vector in dimensions \(2\) through \(9\) for 39 nonincreasing rational-weight cases, verifying equality with the closed formula in all cases. The finite tests independently exercise boundary, plateau, and strict-weight regimes but do **not** constitute an infinite-dimensional or all-parameter proof. Run \(\texttt{python3 checker.py}\) from the extracted artifact directory to reproduce them.

## Relationship to prior work
Agarwal, Rabie and Saker (2023) examine discrete weighted Lorentz norms and Hardy-type operators, supplying a modern natural context for these rearrangement gauges. Roopaei and Foroutannia (2018) compute norms of noncyclic higher backward differences from \(\ell_p\) to matrix-domain sequence spaces; their operator, ambient spaces and boundary conditions differ. Sağır and Oğur (2014) treat vector-valued infinite generalized Lorentz difference sequence spaces and inclusion relations rather than finite cyclic operator norms. Jameson and Lashkaripour (2002) determine norms of Hilbert, Copson and averaging maps on weighted and Lorentz sequence spaces, a different operator family. The present claim is the exact **finite cyclic difference norm** for *every* decreasing positive weight vector and the resulting parity/strictness law. No equivalence with those published assertions is asserted.

## Limitations
Novelty is based on the inspected primary material and available mathematical indexing, not an exhaustive search of every historical treatment of Lorentz difference norms. The main formula is finite-dimensional and real; the special power-weight case is not claimed for \(p=1\), \(p=\infty\) or general complex sequences. A finite checker alone never verifies the universal quantifiers; the analytical argument supplies them. The published work cited for motivation contains broader or adjacent themes, and the exact present finite-cyclic formula has not been independently audited.

## References
- R. P. Agarwal, S. S. Rabie and S. H. Saker, *On Discrete Weighted Lorentz Spaces and Equivalent Relations between Discrete \(\ell_p\)-Classes*, Fractal Fract. **7** (2023), 261. DOI: 10.3390/fractalfract7030261. Published 14 March 2023.
- H. Roopaei and D. Foroutannia, *The norm of backward difference operator \(\Delta^{(n)}\) on certain sequence spaces*, Operators and Matrices **12** (2018), 867–880. DOI: 10.7153/oam-2018-12-52.
- B. Sağır and O. Oğur, *On Vector-Valued Generalized Lorentz Difference Sequence Space*, Journal of Operators (2014), article 545346. DOI: 10.1155/2014/545346.
- G. J. O. Jameson and R. Lashkaripour, *Norms of Certain Operators on Weighted \(\ell_p\) Spaces and Lorentz Sequence Spaces*, J. Inequal. Pure Appl. Math. **3** (2002), article 6.
