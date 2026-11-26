# Exact finite-sample monotonicity thresholds for second-difference smoothing

## Finding

For \(n\ge2\), let \((D_nz)_i=z_i-2z_{i+1}+z_{i+2}\), with no rows when \(n=2\). Set \(S_{n,\lambda}=(I_n+\lambda D_n^{\mathsf T}D_n)^{-1}\), \(\lambda\ge0\). Call a parameter preserving if \(S_{n,\lambda}\) maps every nondecreasing input to a nondecreasing output. The exact preserving regions for the first lengths are
\[
\begin{array}{c|c}
n & \text{preserving parameters}\\\hline
2,3 &[0,\infty)\\
4 &\{0\}\cup[1/6,\infty)\\
5 &\{0\}\cup[7/10,\infty)\\
6 &\{0\}\cup[(14+\sqrt{181})/15,\infty).
\end{array}
\]
For every fixed \(n\ge4\), all sufficiently small positive parameters fail and all sufficiently large parameters preserve order. The sharp worst adjacent decrease (clipped below at zero) on nondecreasing four-point data in \([0,1]\) is
\[
\delta_4(\lambda)=\max\left\{0,\frac{\lambda(1-6\lambda)}{(1+2\lambda)(1+10\lambda)}\right\}.
\]
Its global maximum is \((3-2\sqrt2)/8\), attained uniquely at \(\lambda=(4\sqrt2-3)/46\). For \(0<\lambda<1/6\) the defect is attained by \((0,1,1,1)\) and by its reversal-complement. These finite classifications and sharp defect are the contributions. For comparison, the absence of a common preserving \(\lambda>0\) for all lengths is already implied by prior large-sample filter-weight results.

## Assumptions and scope

Fidelity weights are Euclidean and the second differences have no extra scaling. The endpoints use exactly the penalty given by \(D_n\), with no periodic, clamped, or other added differences. Preservation refers to the order of output values, not to whether fitted values stay within the input range. No complete threshold classification above six samples or uniform rate of growth of restoring strengths is asserted.

## Proof

**Jump-to-slope criterion.** Write \((B_ny)_i=y_{i+1}-y_i\) and \((U_n)_{ij}=\mathbf1_{i>j}\), with zero-based indices. Because constants are fixed, for \(v=B_ny\ge0\) the fitted differences are \(H_{n,\lambda}v\) with \(H_{n,\lambda}=B_nS_{n,\lambda}U_n\). The columns test all unit steps, so preservation is equivalent to entrywise nonnegativity of \(H\). The rows sum to one because affine sequences are fixed. For a direct symbolic replay in slope coordinates, let \(E=B_{n-1}\) (empty at \(n=2\)). Then \(D_n=EB_n\), so multiplying the normal equations by \(B_n\) gives
\[
H_{n,\lambda}=(I_{n-1}+\lambda B_nB_n^{\mathsf T}E^{\mathsf T}E)^{-1}.
\]
This inverse exists: the product inside the penalty is similar to a positive semidefinite matrix using \((B_nB_n^{\mathsf T})^{1/2}\).

**Exact cutoffs.** At \(n=2\), \(H=I_1\). At \(n=3\) it is
\[
\frac{1}{1+6\lambda}\begin{pmatrix}1+3\lambda&3\lambda\\3\lambda&1+3\lambda\end{pmatrix}.
\]
At \(n=4\) inversion gives
\[
H=\begin{pmatrix}
a&4\lambda/(1+10\lambda)&c\\
3\lambda/(1+10\lambda)&(1+4\lambda)/(1+10\lambda)&3\lambda/(1+10\lambda)\\
c&4\lambda/(1+10\lambda)&a
\end{pmatrix},
\quad a=\frac{1+9\lambda+6\lambda^2}{(1+2\lambda)(1+10\lambda)},\quad
c=\frac{\lambda(6\lambda-1)}{(1+2\lambda)(1+10\lambda)}.
\]
Only \(c\) can be negative. At \(n=5\), factoring the entries of the displayed slope-coordinate inverse shows that the only numerator factors with possible negative sign for \(\lambda>0\) are \(15\lambda^2+7\lambda-1,\ 10\lambda-7,\ 5\lambda-1\); all denominators are positive. Specifically,
\[
(H_{5,\lambda})_{0,3}=\frac{\lambda^2(10\lambda-7)}{(1+5\lambda)(1+13\lambda+10\lambda^2)}.
\]
This entry is negative on \((0,7/10)\), and all factors are nonnegative at or above \(7/10\).

At \(n=6\), denominator factors are \(1+8\lambda+3\lambda^2\) and \(1+16\lambda+35\lambda^2\). Factoring the same inverse leaves the following potentially negative numerator factors for \(\lambda>0\):
\[
9\lambda-1,\quad 3\lambda^2-1,\quad15\lambda^2-28\lambda+1,\quad
24\lambda^3+25\lambda^2+4\lambda-1,\quad\lambda-1,\quad 5\lambda-1.
\]
The two entries needed to exclude every positive subthreshold parameter are
\[
(H_{6,\lambda})_{0,2}=\frac{\lambda(9\lambda-1)}{1+16\lambda+35\lambda^2},\qquad
(H_{6,\lambda})_{0,4}=\frac{\lambda^2(15\lambda^2-28\lambda+1)}{(1+8\lambda+3\lambda^2)(1+16\lambda+35\lambda^2)}.
\]
The first is negative on \((0,1/9)\), and the smaller quadratic root is less than \(1/9\), so the second is negative from \(1/9\) to the larger root, excluding that root. All listed factors are nonnegative at or above the larger root. At \(\lambda=0\) the inverse is the identity for every size.

**Four-point defect.** Nonnegative jumps on normalized data sum to at most one, so the most negative possible output slope is the minimum of zero and the smallest entry of \(H\). A unit step in the corresponding column attains it. Hence \(\delta_4=\max(0,-c)\) and the claimed steps attain the positive defect. On \((0,1/6)\) the derivative of the defect has numerator \(1-12\lambda-92\lambda^2\) and denominator \((1+2\lambda)^2(1+10\lambda)^2\). Its unique zero on the interval is the stated maximizer; substitution yields the exact peak.

**Every fixed length.** For \(n\ge4\), use \(y=(0,1,\ldots,1)\). Since \(S=I-\lambda D_n^{\mathsf T}D_n+O(\lambda^2)\) and \(D_ny=(-1,0,\ldots,0)\), the third-to-fourth fitted difference is \(-\lambda+O(\lambda^2)\). Conversely, as \(\lambda\to\infty\), \(S\) tends to the orthogonal projector onto affine sequences. On a unit jump after the \(j\)-th sample this affine fit has slope \(6j(n-j)/[n(n^2-1)]>0\), by the least-squares slope formula. All limiting entries of \(H\) are therefore strictly positive, which implies eventual positivity at fixed \(n\).

**Known large-length obstruction and a direct proof.** The infinite-line kernel \(k_m\) has Fourier multiplier \([1+\lambda(2-2\cos\theta)^2]^{-1}\). At fixed \(\lambda>0\) it is real even and exponentially decaying by analyticity in an annulus. Its sum is one and its second moment is zero, by evaluating the multiplier and its second derivative at zero. Some coefficient must be negative: otherwise the moment forces all off-center coefficients to vanish and the multiplier to be constant. On the infinite step \(y_i=\mathbf1_{i\ge0}\), the convolution equals \(\sum_{m\le i} k_m\), so the difference from index \(i-1\) to \(i\) is \(k_i\). To transfer that slope, restrict to \([-N,N]\). The restricted output solves the finite normal equations off the first and last two indices. At those four indices its residual is exponentially small, since the tails approach the constant input values exponentially and the finite equation is exact on constants. The inverse has Euclidean operator norm at most one, so the finite slope converges to the negative infinite slope. This proves the obstruction without claiming new priority for it.

## Verification

The accompanying `verify.py` checks rational probes with exact Gaussian elimination and optionally compares long-grid slopes numerically (NumPy). The sign regions can be reproduced symbolically by the slope-coordinate inverse above; finite probes do not establish the exact regions or general claims on their own.

## Relationship to prior work

Second-difference Whittaker–Henderson smoothing and the corresponding Hodrick–Prescott filter are classical [1]. Cornea-Madeira [2, Theorem 1] and de Jong and Sakarya [3] give exact finite filter weights. These are weights on data values, whereas the cutoffs depend on signs of cumulative differences of adjacent rows and on extremizing those cumulative differences. The inspected finite-weight formulas do not state the displayed order cutoffs or sharp four-point defect.

The oscillatory bilateral filter weights are known [4], and the finite-to-bulk limit is already available from the finite-weight expansion and bounds of de Jong–Sakarya (see also [5, Chapter 2, Theorems 1–3 and Eqs. (2.10)–(2.11)]). In fact the latter expansion consists of a lag kernel with a summable bound, plus row corrections uniformly \(O(n^{-3})\) for rows at fixed offsets from the center. Summing against a bounded centered step and applying dominated convergence gives the limiting convolution and hence the negative-slope transfer. The no-common-parameter conclusion is thus a prior consequence, not the new part of this result.

The published range-preservation dichotomy [6] concerns whether fitted values lie between the input extremes. For \(n=3\) it gives out-of-range fitted values on a monotone step even though \(H_{3,\lambda}\) is always nonnegative. This is not an order counterexample. Explicitly shape-constrained smoothing [7] is also different from identifying safe parameter regimes for this unconstrained smoother. Equivalent finite sign results elsewhere remain possible.

## References

1. P. H. C. Eilers, *A Perfect Smoother*, Anal. Chem. 75 (2003), 3631–3636, DOI: 10.1021/ac034173t.
2. A. Cornea-Madeira, *The Explicit Formula for the Hodrick–Prescott Filter in Finite Sample*, author manuscript, https://eprints.whiterose.ac.uk/97954/1/HP_ACM.pdf.
3. R. M. de Jong and N. Sakarya, *The Econometrics of the Hodrick–Prescott Filter*, Rev. Econ. Stat. 98 (2016), 310–317, DOI: 10.1162/REST_a_00523.
4. T. McElroy, *Exact Formulas for the Hodrick–Prescott Filter*, Econometrics Journal (2008), DOI: 10.1111/j.1368-423X.2008.00230.x.
5. N. Sakarya, dissertation, Chapter 2, *The Econometrics of the Hodrick–Prescott Filter* (joint work with R. M. de Jong), OhioLINK ETD accession `osu149187075883834`.
6. *Only first-difference Whittaker–Henderson smoothing is universally range-preserving*, Resultary record `b1f399ec57e6`.
7. S. N. Wood, *Monotonic Smoothing Splines Fitted by Cross Validation*, SIAM J. Sci. Comput. 15 (1994), 1126–1133, DOI: 10.1137/0915069.
