# Sharp parity-dependent two-sample Kaczmarz contraction on planar harmonic frames

## Finding

Fix an integer \(m\ge 3\). Let \(u_j=(\cos(j\pi/m),\sin(j\pi/m))^{\mathsf T}\), for \(j=0,\ldots,m-1\), and consider the consistent equations \(u_j^{\mathsf T}x=b_j=u_j^{\mathsf T}x_*\). At each iteration draw an unordered pair of distinct row indices uniformly and project onto the equation with larger absolute residual among the two. Ties can be broken arbitrarily. For every nonzero error \(e=x-x_*\), the sharp conditional mean-square progress constant is

\[
\alpha_m:=\inf_{e\ne0}\frac{\mathbb E[\|e\|_2^2-\|e^+\|_2^2\mid e]}{\|e\|_2^2}
=\begin{cases}
\displaystyle \frac12+\frac{\cot^2(\pi/(2m))}{2m(m-1)},&m\text{ odd},\\[2mm]
\displaystyle \frac12+\frac{2\cos(\pi/m)}{m(m-1)\sin^2(\pi/m)},&m\text{ even}.
\end{cases}
\]

For odd \(m\), equality holds exactly for error directions whose angle \(\theta\) belongs to \((\pi/(2m))\mathbb Z\), modulo \(\pi\). For even \(m\), equality holds exactly when \(\theta\equiv \pi/(2m)\pmod{\pi/m}\) (bisectors between consecutive row directions). Among even \(m\), the alternative row-aligned orientation has strictly larger expected progress, by precisely

\[
\frac{\tan^2(\pi/(2m))}{m(m-1)}.
\]

Consequently, for independent pair drawings at consecutive iterations and every initial error, \(\mathbb E\|e_k\|_2^2\le(1-\alpha_m)^k\|e_0\|_2^2\). The coefficient is sharp for the conditional **single-step** inequality; no claim of sharpness for the multi-step bound is made. By comparison, selecting one row uniformly has exactly \(1/2\) expected progress for every nonzero error. Both parity branches obey \(\alpha_m\to 1/2+2/\pi^2\), while the even-parity orientation gap is asymptotic to \(\pi^2/(4m^4)\).

## Assumptions and scope

The rows are unit vectors in \(\mathbb R^2\), equally spaced modulo sign over a half-circle. The system is exactly consistent and the projection is an exact Euclidean orthogonal projection. Two **distinct** indices are sampled without replacement, uniformly among the \(\binom m2\) unordered pairs, afresh at every step; there is no relaxation factor. The state \(e\) is arbitrary and need not have arisen from an earlier iterate. Results concern expected squared Euclidean error, not residual norm or computational work per unit time.

## Proof

**One-step reduction.** Write \(e=\|e\|_2(\cos\theta,\sin\theta)\), and \(r_j(\theta)=\cos^2(\theta-j\pi/m)\). Projecting onto row \(j\) reduces squared error exactly by \(\|e\|_2^2r_j(\theta)\). Since the greedy rule chooses the larger of the two reductions, its normalized expected progress is

\[
F_m(\theta)=\frac{1}{\binom m2}\sum_{0\le i<j<m}\max\{r_i(\theta),r_j(\theta)\}
=\frac12+\frac{1}{m(m-1)}\sum_{i<j}|r_i(\theta)-r_j(\theta)|.
\tag{1}
\]

The last equality uses \(\sum_j r_j(\theta)=m/2\), which follows from the geometric sum \(\sum_j e^{2\mathrm i j\pi/m}=0\). Thus \(F_m\) is invariant under \(\theta\mapsto\theta+\pi/m\). It is also invariant under \(\theta\mapsto\theta+\pi/2\): this shift replaces every \(r_j\) by \(1-r_j\), while the average pairwise maximum plus the average pairwise minimum is \(1\).

**No unexamined minimizing directions.** For distinct indices, the equality \(r_i(\theta)=r_j(\theta)\) can occur only when

\[
\theta\equiv (i+j)\pi/(2m)\pmod{\pi/2}.
\]

Hence every crossing lies on the grid \((\pi/(2m))\mathbb Z\). Between consecutive grid points, signs of all the differences are fixed. The nonconstant part of (1) is then a linear combination of \(\sin(2\theta)\) and \(\cos(2\theta)\), so

\[
F_m''(\theta)=-4\bigl(F_m(\theta)-1/2\bigr)<0.
\]

The inequality is strict for \(m\ge3\), since the squared row correlations are not all equal for any \(\theta\). Therefore the minimum on each grid interval occurs only at one of its endpoints. Modulo the row-rotation symmetry there are only two candidate orientations, \(\theta=0\) and \(\theta=\pi/(2m)\).

**Even row count.** Let \(m=2n\) and \(\phi=\pi/m\). At \(\theta=0\), the ordered squared correlations consist of one \(0\), duplicate values \(\cos^2(j\phi)\) for \(1\le j\le n-1\), and one \(1\). At \(\theta=\phi/2\) they consist of duplicate values \(\cos^2((j+1/2)\phi)\), \(0\le j<n\). Using

\[
\sum_{i<j}\max\{r_i,r_j\}=\sum_{k=1}^m(k-1)r_{(k)}
\tag{2}
\]

for ascending order statistics, and the geometric-series sums of cosines and cosine-weighted indices, gives the exact evaluations

\[
F_m(0)=\frac12+\frac{2\csc^2\phi-1}{m(m-1)},\qquad
F_m(\phi/2)=\frac12+\frac{2\cos\phi\,\csc^2\phi}{m(m-1)}.
\tag{3}
\]

For completeness, the only nontrivial arithmetic sums needed for the first formula are \(\sum_{j=1}^{n-1}\cos(j\pi/n)=0\) and \(\sum_{j=1}^{n-1}j\cos(j\pi/n)=n/2-1/(2\sin^2(\pi/(2n)))\). For the second, \(\sum_{j=0}^{n-1}\cos((j+1/2)\pi/n)=0\) and \(\sum_{j=0}^{n-1}j\cos((j+1/2)\pi/n)=-\cos(\pi/(2n))/(2\sin^2(\pi/(2n)))\). These all follow by taking real parts of the finite geometric series and its derivative, noting that \(e^{\mathrm i\pi}=-1\). Subtraction in (3) yields

\[
F_m(0)-F_m(\phi/2)=\frac{1-\cos\phi}{(1+\cos\phi)m(m-1)}
=\frac{\tan^2(\phi/2)}{m(m-1)}>0.
\]

Thus precisely the bisector orientations minimize when \(m\) is even.

**Odd row count.** Let \(m=2n+1\) and \(\phi=\pi/m\). At \(\theta=0\), there is one correlation of \(1\) and two of each \(\cos^2(j\phi)\), \(1\le j\le n\). Applying (2), \(\sum_{j=1}^{n}\cos(2j\phi)=-1/2\), and \(\sum_{j=1}^{n}j\cos(2j\phi)=-1/[4(1-\cos\phi)]\) yields

\[
F_m(0)=\frac12+\frac{1+\cos\phi}{2(1-\cos\phi)m(m-1)}
=\frac12+\frac{\cot^2(\phi/2)}{2m(m-1)}.
\]

Since for odd \(m\), the perpendicular shift \(\pi/2\) is congruent to \(\phi/2\) modulo \(\phi\), the two candidate values are equal. Strict concavity between crossings excludes any other minimizers.

**Consequences.** The conditional estimate follows by substituting the minimum of \(F_m\) into the exact projection energy identity, and the multi-step upper bound follows from conditional expectation and induction. For singleton uniform row sampling the tight-frame identity gives progress exactly \(\sum_jr_j/m=1/2\). The large-\(m\) limits follow from \(\sin t\sim t\), \(\cot t\sim1/t\); the even gap uses \(\tan t\sim t\).

## Verification

Run `python verify_pairwise_skm.py` using Python 3.9+ (standard library only). The script checks direct enumeration over all unordered pairs against the closed formulas for \(3\le m\le74\), samples 7,200 angular test points, evaluates the even-parity gap and odd-parity tie, and tests the uniform single-row baseline. The numerical checks are reproducibility tests, not substitutes for the all-integer analytical argument above.

## Relationship to prior work

Sampling Kaczmarz--Motzkin (SKM) and its uniform-subset selection rule were introduced and analyzed in the work of De Loera, Haddock and Needell. Haddock and Ma subsequently developed residual-dependent convergence bounds, and Zhang and Li analyzed randomized block-subselection variants. Those results apply to broader matrices, but the inspected statements do not give the globally sharp one-step constant for the particular complete family of regular planar harmonic frames with pair sampling. Wright and Recht analyze **exactly the same harmonic frame** for ordinary uniform single-row randomized Kaczmarz, where the expected progress is \(1/2\); that analysis does not evaluate the best-of-two selection rule. The novelty claimed here is only the explicit pair-sampling sharp constant, parity-resolved minimizers, and quartic orientation gap, not the algorithm, the frame, or the general expectation identity.

## Limitations

This result is restricted to exact projections in two dimensions, consistent systems, equal-norm equally spaced rows and best-of-two selection **without replacement**. The coefficient is the optimal state-uniform one-step contraction; it need not be the exact asymptotic long-run decay factor and does not compare wall-clock runtimes. The nonexistence of a prior closed formula is not formally provable by literature search; an unlocated specialized computation could already contain the same trigonometric evaluation.

## References

- J. A. De Loera, J. Haddock and D. Needell, *A Sampling Kaczmarz--Motzkin Algorithm for Linear Feasibility*, arXiv:1605.01418 (first submitted 2016). https://arxiv.org/html/1605.01418v6
- J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz--Motzkin*, arXiv:1912.03544 (first submitted 2019-12-07), https://arxiv.org/html/1912.03544v2
- Y. Zhang and H. Li, *Randomized block subsampling Kaczmarz--Motzkin method*, arXiv:2211.16682 (first submitted 2022-11-30), https://arxiv.org/abs/2211.16682
- S. J. Wright and B. Recht, *Optimization for Data Analysis*, Cambridge University Press (2022), Section 5.2.2, DOI 10.1017/9781009004282, https://www.cambridge.org/core/books/optimization-for-data-analysis/C02C3708905D236AA354D1CE1739A6A2
