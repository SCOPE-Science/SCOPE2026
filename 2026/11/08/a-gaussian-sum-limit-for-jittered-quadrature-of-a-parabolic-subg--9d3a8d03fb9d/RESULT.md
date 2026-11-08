# A Gaussian-sum limit for jittered quadrature of a parabolic subgraph

## Finding
For the independent equal-area square-cell jittered estimator of the area beneath \(y=x^2\),
\[
\boxed{\lim_{n\to\infty}n^3\operatorname{Var}(Q_n)=\frac{311}{1440}+\frac{\log 2}{24}=0.2448533547\ldots.}
\]
The estimator is unbiased: \(\mathbb E Q_n=\int_0^1x^2\,dx=1/3\). This establishes an exact asymptotic error constant for a curved discontinuity, with no restriction to prime or square grid sizes.

## Assumptions and scope
Let \(n\) range over **all** positive integers. Partition \([0,1]^2\) into \(n^2\) squares \([i/n,(i+1)/n]\times[j/n,(j+1)/n]\), \(0\le i,j<n\). Choose a uniform point in each square, independently of all other cells. Let \(Q_n=n^{-2}\sum_{i,j}\mathbf1_{\{Y_{ij}<X_{ij}^2\}}\). Boundaries have zero sampling probability. Variance is over the joint sampling randomness.

## Proof
**1. A phase-dependent one-column functional.** For a straight line of slope \(s\ge0\) and vertical phase \(t\in\mathbb R\), set
\[
p_j(s,t)=\int_0^1\min\{1,\max\{0,t+su-j\}\}\,du,
\quad v_s(t)=\sum_{j\in\mathbb Z}p_j(s,t)(1-p_j(s,t)).
\]
Only finitely many summands are nonzero for bounded \(s\); \(v_s\) is jointly continuous on compact slope ranges and periodic of period one in \(t\) (the \(j\) index reorders). The sum is the total Bernoulli variance from one column intersected by the straight line.

**2. Curvature is negligible at the variance scale.** Within column \(i\), with \(x=(i+u)/n\), the boundary in vertical-cell units is
\[nf((i+u)/n)=\frac{i^2}{n}+\frac{2i}{n}u+\frac{u^2}{n}.\]
Since \(0\le u^2/n\le1/n\) and the clamping map is one-Lipschitz, every boundary-cell probability differs from its tangent-line analogue by at most \(1/n\). For slopes between zero and two, uniformly at most a fixed number of cells per column can have nonzero variance. The function \(p(1-p)\) is one-Lipschitz for \(0\le p\le1\). Summing over \(n\) columns, the variance-sum error is \(O(1)\). Cells outside the square contribute zero to the true curve and tangent construction (the endpoint tangents stay inside the vertical square up to null boundaries). Consequently
\[
n^3\operatorname{Var}(Q_n)=\frac1n\sum_{i=0}^{n-1}v_{2i/n}(\{i^2/n\})+O(n^{-1}). \tag{1}
\]
The error is uniform in the integer \(n\).

**3. Complete quadratic phases are equidistributed.** For fixed integers \(k\ne0\) and \(\ell\), the complete quadratic exponential sum \(G_n(k,\ell)=\sum_{i=0}^{n-1}e^{2\pi\mathrm i(ki^2+\ell i)/n}\) satisfies
\[
|G_n(k,\ell)|^2\le n\gcd(2k,n)\le 2|k|n.
\]
Indeed, expand the square and write the difference of indices as \(h\); the inner geometric sum vanishes unless \(n\mid 2kh\), and there are \(\gcd(2k,n)\) possible \(h\). When \(k=0\) but \(\ell\ne0\), the complete geometric sum vanishes for all sufficiently large \(n\). The two-dimensional Weyl criterion therefore makes the sequence of empirical pairs \((i/n,\{i^2/n\})\), \(0\le i<n\), converge weakly to uniform area measure on the unit torus. Since \(v_{2x}(t)\) is continuous and periodic in \(t\), (1) implies
\[\lim_{n\to\infty}n^3\operatorname{Var}(Q_n)=\int_0^1\int_0^1v_{2x}(t)\,dt\,dx.\]

**4. Exact phase mean by a geometric counting identity.** Take four independent uniform random variables \(U_1,U_2,V_1,V_2\). A pair of independent Bernoulli indicators at each horizontal lattice level \(j\) has disagreement probability \(2p_j(1-p_j)\). For fixed samples, the number of integer levels at which the indicators disagree is the number of integers between \(t+sU_1-V_1\) and \(t+sU_2-V_2\). Averaging \(t\) over one full period gives the distance between these real numbers. Thus
\[
K(s):=\int_0^1v_s(t)\,dt=\tfrac12\mathbb E|s(U_1-U_2)-(V_1-V_2)|.
\]
For \(0\le s\le1\), the triangular-difference density gives \(\mathbb E|h+(V_1-V_2)|=1/3+h^2-h^3/3\) for \(0\le h\le1\). Using \(\mathbb E(U_1-U_2)^2=1/6\) and \(\mathbb E|U_1-U_2|^3=1/10\),
\[
K(s)=\frac16+\frac{s^2}{12}-\frac{s^3}{60},\qquad 0\le s\le1.
\]
Exchanging the two iid differences yields \(K(s)=sK(1/s)=s/6+1/(12s)-1/(60s^2)\) for \(s\ge1\). Finally
\[
\int_0^1 K(2x)\,dx=\int_0^{1/2}\left(\frac16+\frac{x^2}3-\frac{2x^3}{15}\right)dx+\int_{1/2}^1\left(\frac x3+\frac{1}{24x}-\frac{1}{240x^2}\right)dx
=\frac{137}{1440}+\frac{29}{240}+\frac{\log2}{24}=\frac{311}{1440}+\frac{\log2}{24}.
\]
This completes the proof.

## Verification
Run `python VERIFY.py` using Python 3 standard library. It independently integrates boundary-cell Bernoulli probabilities, checks a finite set of local-phase quadratures and compares scaled finite-grid variances for \(n\) up to \(10^4\) against the exact constant. Finite tests are checks only: the proof for every \(n\) is the quadratic Gauss-sum/Weyl argument above. The test script and its dependencies are wholly embedded with this result.

## Relationship to prior work
Doerr (2021) analyzes star discrepancy of square-grid jittered samples; Xian and Xu (2022) derive exact expected \(L^2\)-discrepancy formulas for other stratified partitions. Neither inspected result identifies this single curved-indicator variance constant. Known straight-line jittered variance identities, including exact phase laws for rational slopes, do not directly provide the quadratic-phase equidistribution needed here. The elementary Bernoulli variance identity and the complete quadratic Gauss-sum bound are standard mathematical inputs, not claimed as new. The novel candidate is their combination to obtain the exact curved-target constant along all integer grids.

## Limitations
This establishes only the asymptotic variance for the stated parabola, independent one-point-per-cell sampling, and equal weights; it does not prove an optimality claim over partitions or couplings. A broad older theorem on smooth-boundary stratification might imply the result after specialization, and complete publication precedence has not been independently certified. Numerical finite-grid checks cannot replace the limit proof.

## References
- B. Doerr, *A Sharp Discrepancy Bound for Jittered Sampling*, arXiv:2103.15712, first posted 2021-03-29, https://arxiv.org/abs/2103.15712.
- J. Xian and X. Xu, *Improved Expected L2-Discrepancy Formulas on Jittered Sampling*, arXiv:2211.07862, 2022, https://arxiv.org/abs/2211.07862.
- F. Pausinger and S. Steinerberger, *On the Discrepancy of Jittered Sampling*, arXiv:1510.00251 (2015), https://arxiv.org/abs/1510.00251. (Historical context only.)
