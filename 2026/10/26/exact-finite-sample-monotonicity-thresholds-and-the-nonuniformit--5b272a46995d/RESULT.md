# Exact finite-sample monotonicity thresholds and the nonuniformity barrier for second-difference smoothing

## Finding
For integers \(n\ge2\) and real \(\lambda\ge0\), let \(D_n:\mathbb R^n\to\mathbb R^{n-2}\) be the ordinary second-forward-difference matrix, \((D_n z)_i=z_i-2z_{i+1}+z_{i+2}\), with the empty matrix when \(n=2\). Let
\[
S_{n,\lambda}=(I_n+\lambda D_n^{\mathsf T}D_n)^{-1}.
\]
Call \(S_{n,\lambda}\) *order-preserving on monotone sequences* when \(y_0\le\cdots\le y_{n-1}\) implies \((S_{n,\lambda}y)_0\le\cdots\le(S_{n,\lambda}y)_{n-1}\), for every real input.

The first exact monotonicity regions are
\[
\begin{array}{c|c}
n&\text{all preserving smoothing parameters}\;\lambda\\\hline
2,3 &[0,\infty)\\
4 &\{0\}\cup[1/6,\infty)\\
5 &\{0\}\cup[7/10,\infty)\\
6 &\{0\}\cup[(14+\sqrt{181})/15,\infty).
\end{array}
\]
For every finite \(n\ge4\), all sufficiently small *positive* \(\lambda\) violate order preservation, while all sufficiently large \(\lambda\) preserve it. Nevertheless, **there is no positive finite \(\lambda\) preserving order for all sample lengths**: for each fixed \(\lambda>0\), some integer \(n\) and monotone zero-one step input have a decreasing output adjacent pair.

The four-sample worst adjacent decrease over all monotone inputs with values in \([0,1]\) is exactly
\[
\delta_4(\lambda)=\max\left\{0,\frac{\lambda(1-6\lambda)}{(1+2\lambda)(1+10\lambda)}\right\};
\]
its maximum over \(\lambda\ge0\) is
\[
\frac{3-2\sqrt2}{8}=0.0214466094067\ldots,
\]
attained uniquely at \(\lambda=(4\sqrt2-3)/46=0.0577577010759\ldots\). For positive \(\lambda<1/6\), equality in the decrease bound is attained by the monotone step \((0,1,1,1)\) and its reversal-complement.

## Assumptions and scope
The data space is real \(\mathbb R^n\), with standard Euclidean fidelity weights and unscaled consecutive second differences. A change in the normalization of the penalty rescales \(\lambda\) and hence all stated thresholds. No periodic, clamped, or other boundary penalty is substituted for the natural finite-difference matrix. The monotonicity requirement concerns *differences of fitted values*, not the distinct requirement that every fitted value lie between the minimum and maximum original values.

## Proof
Write \(B_n:\mathbb R^n\to\mathbb R^{n-1}\) for first forward differences, \((B_n y)_i=y_{i+1}-y_i\), and \(U_n\) for the \(n\)-by-\((n-1)\) step matrix \((U_n)_{ij}=\mathbf1_{i>j}\). Every nondecreasing \(y\) has \(y=y_0\mathbf1+U_nv\) for \(v=B_ny\ge0\). As \(D_n\mathbf1=0\), the smoother fixes constants. Thus the complete necessary and sufficient criterion for order preservation is entrywise nonnegativity of
\[
H_{n,\lambda}=B_nS_{n,\lambda}U_n.\tag{1}
\]
All rows of \(H_{n,\lambda}\) sum to one, because the smoother also fixes the linear sequence \((0,1,\ldots,n-1)\).

For \(n=3\), direct inversion gives
\[
H_{3,\lambda}=\frac1{1+6\lambda}\begin{pmatrix}1+3\lambda&3\lambda\\3\lambda&1+3\lambda\end{pmatrix},
\]
which is nonnegative for all \(\lambda\ge0\). The case \(n=2\) is the identity.

For \(n=4\), direct inversion and cancellation yield
\[
H_{4,\lambda}=\begin{pmatrix}
a&4\lambda/(1+10\lambda)&c\\
3\lambda/(1+10\lambda)&(1+4\lambda)/(1+10\lambda)&3\lambda/(1+10\lambda)\\
c&4\lambda/(1+10\lambda)&a
\end{pmatrix},
\]
where
\[
a=\frac{1+9\lambda+6\lambda^2}{(1+2\lambda)(1+10\lambda)},\qquad
c=\frac{\lambda(6\lambda-1)}{(1+2\lambda)(1+10\lambda)}.
\]
Only \(c\) can be negative, proving the four-point region. For monotone inputs in \([0,1]\), the nonnegative jump sizes sum to at most one, so the sharp adjacent-decrease defect is \(\max(0,-c)\). Differentiating this rational function on \((0,1/6)\) gives derivative \((1-12\lambda-92\lambda^2)/[(1+2\lambda)^2(1+10\lambda)^2]\), hence the unique maximum and its exact value above.

For \(n=5\), all denominators in \(H_{5,\lambda}\) are positive for \(\lambda>0\). The only possibly negative numerator factors, after removing strictly positive factors, are \(15\lambda^2+7\lambda-1\), \(10\lambda-7\), and \(5\lambda-1\). In particular, the corner entry is
\[
(H_{5,\lambda})_{0,3}=\frac{\lambda^2(10\lambda-7)}{(1+5\lambda)(1+13\lambda+10\lambda^2)}.
\]
It is negative throughout \((0,7/10)\); at and above \(7/10\), each displayed sign-changing factor is nonnegative and all other numerator factors are positive. This proves the five-point region.

For \(n=6\), all denominators are products of \(1+8\lambda+3\lambda^2\) and \(1+16\lambda+35\lambda^2\), or the latter factor alone, and are positive. Up to positive factors, the only possibly negative numerator factors in the complete matrix \(H_{6,\lambda}\) are
\[
9\lambda-1,\quad 3\lambda^2-1,\quad
15\lambda^2-28\lambda+1,\quad
24\lambda^3+25\lambda^2+4\lambda-1,\quad
\lambda-1,\quad5\lambda-1.
\]
Two entries that certify every parameter below the claimed threshold are
\[
(H_{6,\lambda})_{0,2}=\frac{\lambda(9\lambda-1)}{1+16\lambda+35\lambda^2},\qquad
(H_{6,\lambda})_{0,4}=\frac{\lambda^2(15\lambda^2-28\lambda+1)}{(1+8\lambda+3\lambda^2)(1+16\lambda+35\lambda^2)}.
\]
For \(0<\lambda<1/9\), the first is negative; for \(1/9\le\lambda<(14+\sqrt{181})/15\), the second is negative because the smaller positive quadratic root is less than \(1/9\). At and above that larger root, every listed potentially negative factor is nonnegative. This proves the six-point region.

Now fix any \(n\ge4\) and take the step input \(y=(0,1,1,\ldots,1)\). As \(\lambda\downarrow0\),
\[
S_{n,\lambda}=I_n-\lambda D_n^{\mathsf T}D_n+O(\lambda^2).
\]
Since \(D_ny=(-1,0,\ldots,0)\), its fitted third-to-fourth forward difference equals \(-\lambda+O(\lambda^2)\), which is negative for every sufficiently small positive \(\lambda\).

For large \(\lambda\), spectral calculus shows that \(S_{n,\lambda}\) converges to the Euclidean orthogonal projector onto the affine sequences \(a+bi\). On a step with a unit jump after the \(j\)-th sample, its fitted slope equals
\[
\frac{6j(n-j)}{n(n^2-1)}>0,\qquad 1\le j\le n-1.
\]
Thus every entry of the limiting matrix \(H_{n,\infty}\) is strictly positive, so by continuity \(H_{n,\lambda}\) is entrywise positive for all sufficiently large finite \(\lambda\), for each *fixed* \(n\).

It remains to prove that the necessary large smoothing parameter cannot be chosen uniformly in \(n\). Consider the infinite-line fourth-difference resolvent convolution kernel \((k_m)_{m\in\mathbb Z}\), whose Fourier series is
\[
h_\lambda(\theta)=\sum_{m\in\mathbb Z}k_m e^{im\theta}
=\frac1{1+\lambda(2-2\cos\theta)^2}.
\]
For \(\lambda>0\), the denominator has no zero on the unit circle; analyticity in an annulus makes the real even coefficients exponentially decaying. In particular,
\[
\sum_m k_m=h_\lambda(0)=1,\qquad
\sum_m m^2k_m=-h_\lambda''(0)=0.
\]
If all coefficients were nonnegative, the second identity would force \(k_m=0\) for every nonzero \(m\), and hence \(h_\lambda\) would be identically one, contrary to \(\lambda>0\). Therefore some \(k_{m_*}<0\). The infinite-line output of the step \(\mathbf1_{i\ge0}\) has forward difference exactly \(k_i\), and therefore decreases at \(i=m_*\).

For completeness, this negative slope survives on a sufficiently long finite interval: restrict the infinite-line step and its bounded, smoothed output to indices \([-N,N]\). Away from the first and last two indices, that restricted output satisfies exactly the finite normal equations. At the four boundary indices the residuals are exponentially small in \(N\), because the infinite output converges exponentially to zero at the left boundary and to one at the right boundary. The finite inverse has Euclidean norm at most one, since \(I+\lambda D_n^{\mathsf T}D_n\succeq I\). Thus the finite output differs from the restricted infinite output by \(O_\lambda(e^{-c_\lambda N})\) in Euclidean norm. Its fixed interior negative adjacent difference persists for large enough \(N\). This proves failure of any sample-length-independent positive smoothing strength.

## Verification
The accompanying `verify.py` constructs the unweighted smoother and its induced jump-to-slope matrix using exact rational Gaussian elimination. It checks unit row sums, monotonicity on either side of each displayed threshold for sample lengths two through six, the complete four-point defect formula, and the explicit extremizing entry. Optional NumPy calculations on long grids corroborate negative slopes at each of several fixed positive smoothing strengths. The all-size claims are proved analytically above; neither finite numerical tests nor polynomial sampling are substitutes for their proofs.

## Relationship to prior work
Whittaker–Henderson smoothing, its second-difference Hodrick–Prescott specialization, and its finite-sample resolvent are classical. Eilers describes the penalized least-squares formulation; McElroy's 2006 full-text report derives the infinite filter's spectral factorization and oscillatory side-lobe coefficients, not the exact monotone-input positivity regions displayed here. Wood's monotone smoothing splines enforce shape restrictions by a different constrained method.

A published study entitled *Only first-difference Whittaker–Henderson smoothing is universally range-preserving* proves that the second-difference smoother fails the **data-range** condition for some monotone input at every positive smoothing strength, already for three points. Its conclusion is not equivalent to the present **output-order** condition: the three-point operator preserves monotonicity for every smoothing strength even though its smoothed coordinates can escape the input range. The present result quantifies the first order-preservation transitions, the four-point sharp defect, and the impossibility of a common finite restoring parameter for all lengths.

## Limitations
The first three nontrivial exact cutoffs are given; no closed formula, uniqueness-of-threshold theorem, or asymptotic growth law is proved for the smallest restoring parameter at arbitrary finite sample size. The existence of eventual monotonicity at every fixed size does not assert that the preserving parameter set is a half-line for all sizes. Strict range preservation is not claimed, even where monotonicity is restored. Published finite-sample filter-weight formulas may contain additional implicit information about these signs; independent review of exact historical overlap is still warranted. The 2016 finite-sample study by de Jong and Sakarya could not be examined in full.

## References
1. S. N. Wood, *Monotonic Smoothing Splines Fitted by Cross Validation*, SIAM J. Sci. Comput. 15 (1994), 1126–1133, DOI: 10.1137/0915069 (1994-09-30 printed-publication date in institutional record).
2. P. H. C. Eilers, *A Perfect Smoother*, Anal. Chem. 75 (2003), 3631–3636, DOI: 10.1021/ac034173t (first online 2003-05-30).
3. T. McElroy, *Exact Formulas for the Hodrick–Prescott Filter*, U.S. Census Bureau Research Report RRS2006-09 (2006-09-07), https://www.census.gov/content/dam/Census/library/working-papers/2006/adrm/rrs2006-09.pdf.
4. R. M. de Jong and N. Sakarya, *The Econometrics of the Hodrick–Prescott Filter*, Rev. Econ. Stat. 98 (2016), 310–317, DOI: 10.1162/REST_a_00523 (full text not inspected).
5. *Only first-difference Whittaker–Henderson smoothing is universally range-preserving*, published research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-only-first-difference-whittaker-henderson-smoothing-is-universal--b1f399ec57e6 (RESULT.md inspected).
