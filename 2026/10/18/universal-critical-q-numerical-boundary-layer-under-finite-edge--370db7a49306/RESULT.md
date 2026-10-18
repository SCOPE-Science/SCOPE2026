# Universal critical \(q\)-numerical boundary layer under finite edge defects

## Finding

Fix a nonnegative integer \(K\). For each integer \(n>2K+3\), choose arbitrary weights \(0<a_{n,j}\leq1\), \(1\leq j<n\), subject only to \(a_{n,j}=1\) whenever \(K<j<n-K\). The exceptional weights in the first and last \(K\) edges may vary with \(n\), without a uniform positive lower bound. Define the finite weighted backward shift on \(\mathbb C^n\) by \(T_ne_{j+1}=a_{n,j}e_j\) and \(T_ne_1=0\). For \(0\leq q\leq1\), write
\[
 w_q(T)=\max\{|\langle Tx,y\rangle|:\ \|x\|=\|y\|=1,\ \langle x,y\rangle=q\}.
\]
Then, for every fixed real \(c\geq0\), with \(q_n=1-c/n^2\) (defined for all sufficiently large \(n\)),
\[
\boxed{\lim_{n\to\infty}n^2\bigl(1-w_{q_n}(T_n)\bigr)=\left(\frac{\pi}{\sqrt2}-\sqrt c\right)_+^2.}
\]
The convergence is **uniform over every admissible choice of the exceptional edge weights**, for each fixed \(K,c\). In particular, the crossover from the classical numerical-radius deficit \(\pi^2/(2n^2)\) to the unit-norm plateau occurs at the exact universal scaled threshold \(c=\pi^2/2\), independent of finite end defects.

## Assumptions and scope

All Hilbert spaces here are finite-dimensional complex Euclidean spaces, with the standard inner product. Weights are strictly positive and at most one; they may tend arbitrarily quickly to zero at the finitely many boundary positions. The integer \(K\) and number \(c\) are fixed as \(n\to\infty\). No assertion is made for defects at macroscopic interior positions, weights exceeding one, or when \(K\) grows proportionally with \(n\).

## Proof

**1. Exact constrained norm envelope.** For any finite positive weighted shift \(T\) of this form, put \(F(t)=\|tI+T\|\) for \(t\geq0\). Rotating coordinates by a diagonal unitary makes \(T\) covariant under complex rotations, so the modulus maximum in the definition of \(w_q\) can be taken in the real direction. For any admissible unit vectors, \(\operatorname{Re}\langle Tx,y\rangle\leq F(t)-tq\); hence
\[
 w_q(T)\leq\inf_{t\geq0}\bigl(F(t)-tq\bigr). \tag{1}
\]
This is equality. For \(t>0\), the matrix \((tI+T)^*(tI+T)\) is a positive irreducible real symmetric tridiagonal matrix, so the top singular value is simple. Choose real positive singular vectors \(x_t,y_t\), with \((tI+T)x_t=F(t)y_t\). Differentiation of the simple singular value gives \(F'(t)=\langle x_t,y_t\rangle\). Convexity and continuity imply that \(F'\) ranges continuously from \(q_0:=F'_+(0)\) to \(1\). Thus for every \(q_0<q<1\), a value of \(t>0\) has \(F'(t)=q\); that singular-vector pair attains the upper bound in (1). For \(0\leq q\leq q_0\), the vectors norming \(T\) give the whole overlap interval \([0,q_0]\): indeed their source coordinates lie in the subspace where incoming edge weights equal one, the real overlap form is a direct sum of symmetric finite paths, and its unit-sphere image contains every number between zero and its maximal eigenvalue \(q_0\). Taking \(y=Tx\) gives \(w_q(T)=\|T\|=1\); convexity gives \(F(t)\geq1+tq_0\), proving equality in (1) here also. At \(q=1\), continuity or the standard numerical-radius characterization yields the same equality with a limiting \(t\to\infty\). Therefore
\[
 w_q(T)=\inf_{t\geq0}\bigl(\|tI+T\|-qt\bigr),\qquad0\leq q\leq1. \tag{2}
\]
The existence of an intact interior edge ensures \(\|T\|=1\).

**2. A uniform tridiagonal squeeze.** Set \(F_n(t)=\|tI+T_n\|\). Direct multiplication gives
\[
 (tI+T_n)^*(tI+T_n)=t^2I+T_n^*T_n+t(T_n+T_n^*).
\]
Its diagonal entries are \(t^2,t^2+a_{n,1}^2,\ldots,t^2+a_{n,n-1}^2\), with off-diagonal entries \(ta_{n,j}\). Entrywise Perron comparison with the all-ones shift gives the upper bound below. The principal submatrix on coordinates \(K+2,\ldots,n-K\) has length \(n-2K-1\), constant diagonal \(1+t^2\), and constant off-diagonal \(t\), giving the lower bound. Hence, for every \(t\geq0\),
\[
\sqrt{(1+t)^2-2t\left(1-\cos\frac{\pi}{n-2K}\right)}
\ \leq\ F_n(t)\ \leq\
\sqrt{(1+t)^2-2t\left(1-\cos\frac{\pi}{n+1}\right)}. \tag{3}
\]
Both bounds are independent of the exceptional edge weights. Consequently, uniformly for \(t\) in any fixed compact interval of \([0,\infty)\) and over all admissible weights,
\[
 n^2\bigl(F_n(t)-1-t\bigr)\longrightarrow-\frac{\pi^2t}{2(1+t)}. \tag{4}
\]

**3. Control of the minimizing parameter.** Fix \(c>0\), and let \(q_n=1-c/n^2\). Since \(F_n(0)=1\), the infimum in (2) is at most one; for \(q_n<1\), a minimizer exists. Put \(\delta_n=1-\cos(\pi/(n-2K))\). The lower bound in (3) and rationalization yield
\[
 F_n(t)\geq1+t-\frac{2t\delta_n}{1+t}.
\]
If a minimizing \(t>0\) satisfies \(F_n(t)-q_nt\leq1\), it follows that
\[
 1+t\leq\frac{2n^2\delta_n}{c}.
\]
Thus all minimizers lie in a compact interval bounded independently of \(n\) and all exceptional weights. Applying (4) uniformly on that interval to the exact envelope (2) yields
\[
\lim_{n\to\infty}n^2\bigl(1-w_{q_n}(T_n)\bigr)
=\max_{t\geq0}\left\{\frac{\pi^2t}{2(1+t)}-ct\right\}.
\]
The maximizer is \(t_*=\max\{\pi/\sqrt{2c}-1,0\}\); its value is \((\pi/\sqrt2-\sqrt c)_+^2\).

**4. The endpoint \(c=0\).** For a positive weighted shift, its ordinary numerical radius equals the largest eigenvalue of \((T_n+T_n^*)/2\). Comparing with the unweighted full path above and with the intact central path below gives
\[
 \cos\frac\pi{n-2K}\leq w_1(T_n)\leq\cos\frac\pi{n+1}.
\]
Therefore \(n^2(1-w_1(T_n))\to\pi^2/2\), which is exactly the asserted value at \(c=0\). All squeezes are weight-independent, so the stated uniformity follows. \(\square\)

## Verification

The included `verify.py` independently constructs the exact Hermitian tridiagonal matrices for \(\|tI+T_n\|\), checks both sides of (3), and numerically minimizes (2) for several dimensions, scaled parameters, and varying boundary defects. It passed 276 finite diagnostic assertions using NumPy and SciPy. The limiting theorem does not follow from those finite checks: the universal content is the analytic squeeze, the exact envelope, and the compact-minimizer argument.

## Relationship to prior work

Kaunisto, O'Loughlin, and Virtanen establish general dilation and spectral-set inequalities for scaled \(q\)-numerical ranges, not this weighted-shift double-scaling law [1]. O'Loughlin and Rani similarly treat spectral-set estimates rather than this asymptotic regime [2]. Vandanjav and Undrakh calculate ordinary numerical radii for certain finite weighted shift matrices [3], not the constrained \(q\)-numerical layer. Earlier calculations of the full finite-dimensional \(q\)-numerical radius of **unweighted** Jordan shifts (research record [4]) include the all-ones subfamily, but do not include arbitrarily varying positive end weights or the claimed uniform critical-layer universality. Another related record treats an exceptional edge of an **infinite** \(\ell_p\) shift for ordinary spatial numerical radius [5], not the coupled finite-size/\(q\) limit. Claims of independent publication priority are not made.

## Limitations

The theorem is about the leading \(n^{-2}\) coefficient, not higher-order terms, which may depend on the boundary weights. Source [3] has been accessible in partial publisher excerpts but not as full text; record [4] has been accessible as a searchable scientific summary rather than its complete research package, leaving a residual formulation-priority risk. The comparison does not establish absolute novelty or independent certification.

## References

[1] M. Kaunisto, R. O'Loughlin, J. Virtanen, *Dilation Theory for Scaled \(q\)-Numerical Ranges*, arXiv:2610.00443, first posted 2026-09-30; MSC2020 47A12. https://arxiv.org/abs/2610.00443

[2] R. O'Loughlin, J. Rani, *\(q\)-Numerical Ranges and Spectral Sets*, arXiv:2603.15536, first posted 2026-03-16. https://arxiv.org/abs/2603.15536

[3] A. Vandanjav, B. Undrakh, *On the numerical range of some weighted shift matrices and operators*, Linear Algebra and its Applications 449 (2014), 76–88; DOI: 10.1016/j.laa.2014.02.018.

[4] *Quadratic exit from the norm plateau for \(q\)-numerical radii of Jordan shifts*, research record 2026/10/11/SCOPE-quadratic-exit-from-the-norm-plateau-for-q-numerical-radii-of-jo--f322322a276d.

[5] *Sharp numerical-radius and attainment thresholds for one-edge perturbations of \(\ell_p\) shifts*, research record 2026/10/11/SCOPE-sharp-numerical-radius-and-attainment-thresholds-for-one-edge-pe--6d4363552adb.
