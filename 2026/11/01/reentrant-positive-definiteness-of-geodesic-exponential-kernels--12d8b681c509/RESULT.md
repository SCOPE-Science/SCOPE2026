# Reentrant positive definiteness of geodesic exponential kernels on the six-cycle

## Finding
Let \(X=\mathbb Z/6\mathbb Z\) have the unit-edge cycle metric \(d(i,j)=\min\{|i-j|,6-|i-j|\}\), with the difference represented between \(0\) and \(5\). For \(p,t>0\), define the symmetric six-by-six Gram matrix
\[
K_{p,t}(i,j)=\exp\bigl(-t\,d(i,j)^p\bigr),\qquad i,j\in X.
\]
**Theorem.** For **every real exponent**
\[
\frac{647}{300}\le p\le\frac{653}{300},
\]
the following strict three-bandwidth sign pattern holds:
\[
K_{p,7/25}\succ0,\qquad
\operatorname{inertia}(K_{p,2/5})=(5,0,1),\qquad
K_{p,3/5}\succ0.
\]
Here inertia is ordered as (positive, zero, negative) eigenvalue counts. In particular the set
\[
\mathcal P_p=\{t>0:K_{p,t}\text{ is positive definite}\}
\]
**is disconnected for each exponent in this nontrivial closed interval**. Thus strict positive definiteness of an exponential graph-distance kernel at a bandwidth need not be preserved at every larger bandwidth, even on a homogeneous unweighted six-vertex graph. This is an explicit nonmonotone finite-sample phenomenon, not a characterization of all admissible bandwidths.

## Assumptions and scope
The graph is the simple six-cycle with all edges of graph length \(1\); its metric distances are exactly \(0,1,2,3\). The power \(p\) acts on the original metric distance before exponentiation. All six distinct vertices are included, without additional normalization or vertex weighting. Positive definiteness is **strict**: \(z^{\mathsf T}Kz>0\) for every nonzero real vector \(z\); indefiniteness means both positive and negative eigenvalues. No claim is made about other graph sizes or the precise number of connected components of \(\mathcal P_p\).

## Proof
Write
\[
a=e^{-t},\qquad b=e^{-t2^p},\qquad c=e^{-t3^p}.
\]
The circulant first row of \(K_{p,t}\) is \((1,a,b,c,b,a)\). The discrete Fourier characters \(j\mapsto e^{2\pi i k j/6}\) diagonalize it. The four distinct real eigenvalues, with multiplicities in parentheses, are
\[
\begin{aligned}
L_0&=1+2a+2b+c &(1),\\
L_1&=1+a-b-c &(2),\\
L_2&=1-a-b+c &(2),\\
L_3&=1-2a+2b-c &(1).
\end{aligned}
\]
For the real interval of exponents above, exact rational interval bounds on \(2^p\) and \(3^p\), combined with exponential Taylor bounds, establish the **uniform** signs below. The displayed endpoints are outward coarse bounds; the accompanying standalone checker supplies exact fraction arithmetic.

\[
\begin{array}{c|ccc}
& t=7/25&t=2/5&t=3/5\\\hline
L_0 &>3.12 &>2.68 &>2.23\\
L_1 &>1.41 &>1.48 &>1.47\\
L_2 &>0.004 &>0.17 &>0.38\\
L_3 &>0.002 &<-0.017 &>0.033
\end{array}
\]
For completeness, the exact comparison is constructive. If \(u\) is either \(2\) or \(3\), integer-power comparisons with a \(10^{-6}\) grid, using denominator \(300\), give for all \(p\) in the interval
\[
\begin{aligned}
4.458834&<2^p<4.521078,\\
10.690339&<3^p<10.927831.
\end{aligned}
\]
The strict bounds are verified by raising the rational grid endpoints to the \(300\)-th power and comparing against \(u^{647}\) and \(u^{653}\), respectively. For every \(x\ge0\) and integer \(N\ge0\), Taylor's theorem gives
\[
\sum_{j=0}^{2N+1}\frac{(-x)^j}{j!}
\ \le\ e^{-x}\ \le\
\sum_{j=0}^{2N}\frac{(-x)^j}{j!}.
\]
The exponential is decreasing, so replacing an uncertain exponent argument by its rational lower and upper endpoints gives a valid enclosure for \(a,b,c\). With \(N=35\), rational interval arithmetic in the four displayed Fourier expressions gives the strict sign margins in the table, simultaneously for **all** real \(p\) in the stated interval. In particular at \(t=2/5\), precisely the one-dimensional alternating Fourier sector has a negative eigenvalue; the other five eigenvalues are positive.

For fixed \(p\), each Fourier eigenvalue is continuous in \(t\). Thus \(\mathcal P_p\) contains \(7/25\) and \(3/5\) but excludes the strictly intermediate value \(2/5\). Any connected subset of \(\mathbb R\) is an interval; hence \(\mathcal P_p\) is disconnected. The positive and indefinite signs are strict, so they each persist in an open neighborhood of their respective bandwidths. This completes the proof.

## Verification
Run the standalone `verify_cycle_reentrant.py` using Python 3's standard library. It makes exact integer-power comparisons, constructs rational Taylor enclosures, and checks all twelve Fourier-sector signs at the three stated bandwidths. It prints `ALL_UNIFORM_REENTRANT_C6_CHECKS_OK` on success. In the critical alternating sector at \(t=2/5\), the exact rational enclosure is contained in \((-0.027,-0.017)\); at \(t=7/25\), the two smallest guaranteed positive lower bounds are above \(0.004\) and \(0.002\). The certificate validates the full continuum of exponents, because the root intervals are uniform and the enclosure preserves all quantifiers. No floating-point tolerance, finite exponent grid, or external computation is invoked in the proof.

## Relationship to prior work
Meckes (2010) studies positive-definite metric spaces using similarity matrices \(e^{-d}\) and relates the all-scale property to negative type; those definitions do not imply bandwidth monotonicity of \(e^{-t d^p}\) when \(p>2\). Feragen, Lauze and Hauberg (2014) analyze exponential geodesic kernels and the restrictions on **all-bandwidth** positive definiteness. Feragen and Hauberg (2016) explicitly investigate positive bandwidth intervals on finite samples, but do not supply this fixed-graph reentry example. Sra (2011) establishes a **noninterval universal parameter set** for an S-divergence determinant kernel on positive-definite matrices; its space, kernel and quantifiers differ from the six-cycle. Da Costa, Mostajeran and Ortega (2023) prove nonpositivity for some finite configurations on the **entire continuous circle** at every Gaussian scale; this does not imply indefiniteness on a particular fixed six-point subset, and their Gaussian exponent is \(2\), not the present exponent interval. The Schur product theorem implies that each admissible bandwidth set is closed under addition; an additive subsemigroup of positive real numbers need not be an interval, so this general structural constraint does not prohibit the demonstrated gap. The result above is an explicit finite graph-kernel sign reversal and does not claim to originate the general idea of disconnected admissible parameter sets.

## Limitations
The proof shows three strict bandwidth signs and disconnectedness, not the exact boundary roots or total number of components of the admissible set. It does not claim minimal graph order, a full classification of other exponents or cycles, or utility for a particular statistical data distribution. The statement concerns the fixed finite graph metric, not the continuum circle or a normalized Gaussian bandwidth convention. Priority of similar unindexed finite-cycle calculations remains an external literature risk; independent review has not been performed.

## References
1. M. W. Meckes, *Positive definite metric spaces*, arXiv:1012.5863 (publicly posted December 29, 2010), https://arxiv.org/abs/1012.5863.
2. S. Sra, *Positive definite matrices and the S-divergence*, arXiv:1110.1773 (publicly posted October 8, 2011), https://arxiv.org/abs/1110.1773.
3. A. Feragen, F. Lauze and S. Hauberg, *Geodesic Exponential Kernels: When Curvature and Linearity Conflict*, arXiv:1411.0296 (publicly posted November 2, 2014), https://arxiv.org/abs/1411.0296.
4. A. Feragen and S. Hauberg, *Open Problem: Kernel methods on manifolds and metric spaces. What is the probability of a positive definite geodesic exponential kernel?*, Proceedings of Machine Learning Research 49 (2016), 1647–1650, https://proceedings.mlr.press/v49/feragen16.html.
5. N. Da Costa, C. Mostajeran and J.-P. Ortega, *The Gaussian kernel on the circle and spaces that admit isometric embeddings of the circle*, arXiv:2302.10623 (2023), https://arxiv.org/abs/2302.10623.
