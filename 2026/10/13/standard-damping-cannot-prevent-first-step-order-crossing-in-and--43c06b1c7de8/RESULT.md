# Standard damping cannot prevent first-step order crossing in Anderson acceleration
## Finding
Consider the affine fixed-point map
\[
g(x)=x^\star+\Lambda(x-x^\star),\qquad \Lambda=\operatorname{diag}(\lambda_1,\ldots,\lambda_n),\qquad 0<\lambda_i<1.
\]
Let \(x_1=g(x_0)\), write \(f_k=g(x_k)-x_k\), and perform the first depth-one Anderson least-squares stage: choose \(\alpha_0+\alpha_1=1\) to minimize \(\|\alpha_0f_0+\alpha_1f_1\|_2\), then set the Anderson prediction \(\bar x=\alpha_0x_0+\alpha_1x_1\). For a standard mixing parameter \(0\le\omega\le1\), output
\[
x_2^{(\omega)}=(1-\omega)\bar x+\omega g(\bar x).
\]
For every active coordinate, define \(e_i=x_{0,i}-x_i^\star\ne0\) and \(a_i=1-\lambda_i\). Set
\[
\tau=\frac{\sum_i a_i^4e_i^2}{\sum_i a_i^3e_i^2}.
\]
Then
\[
\alpha_1=\frac1\tau,
\qquad
x_{2,i}^{(\omega)}-x_i^\star=(1-\omega a_i)e_i\left(1-\frac{a_i}\tau\right).
\]
Thus the sign of each active error after the accelerated step is independent of the standard damping parameter \(\omega\in[0,1]\): coordinates with \(a_i>\tau\) reverse side relative to the fixed point, coordinates with \(a_i<\tau\) retain their side, and coordinates with \(a_i=\tau\) land exactly on the fixed-point coordinate. If at least two distinct active contraction rates are present, \(\tau\) is a strict weighted mean of the active gaps, so both a reversal and a non-reversal must occur. Standard underrelaxation of the Anderson correction therefore cannot restore coordinatewise order preservation after the least-squares prediction has crossed the fixed point.

The boundary is dimension-sharp. In one dimension, \(\tau=a_1\), so \(\bar x=x^\star\) and every mixed output equals the fixed point. In two dimensions with distinct active rates, exactly one coordinate reverses side and one does not.

There is also a positivity consequence. Take
\[
\Lambda=\operatorname{diag}(1/2,3/4),\qquad x^\star=(1,1),\qquad x_0=(36,36).
\]
The map is \(g_i(x_i)=(1-\lambda_i)+\lambda_i x_i\), hence maps the nonnegative orthant into itself, and ordinary Picard iteration remains positive. The first Anderson least-squares coefficient is \(\alpha_1=36/17\). For every \(0\le\omega\le1\), the first coordinate of the mixed Anderson output is
\[
x_{2,1}^{(\omega)}=1-\frac{35}{17}\left(1-\frac\omega2\right)<0.
\]
So even full standard damping cannot prevent a negative coordinate in this exact two-dimensional positive contraction example.

## Assumptions and scope
The result uses the usual depth-one Anderson residual least-squares coefficients with the affine-sum constraint and the standard scalar mixing parameter applied after the least-squares prediction. Exact arithmetic is assumed. The contraction matrix is diagonal with strictly interior rates \(0<\lambda_i<1\); inactive coordinates with \(e_i=0\) are omitted from the weighted mean. The theorem concerns the first accelerated step after one Picard warm-up. It does not claim that later safeguarded, coefficient-constrained, restarted, or problem-specific Anderson variants must lose positivity.

## Proof
Let \(e=x_0-x^\star\). Since \(x_1-x^\star=\Lambda e\), the two residuals satisfy
\[
f_0=(\Lambda-I)e=-Ae,\qquad f_1=\Lambda f_0,
\]
where \(A=I-\Lambda=\operatorname{diag}(a_i)\). Write \(\alpha_1=\beta\) and \(\alpha_0=1-\beta\). The least-squares objective is
\[
\|f_0+\beta(f_1-f_0)\|_2^2
 =\sum_i a_i^2e_i^2(1-\beta a_i)^2.
\]
Its second derivative is \(2\sum_i a_i^4e_i^2>0\), so the minimizer is unique, with
\[
\beta=\frac{\sum_i a_i^3e_i^2}{\sum_i a_i^4e_i^2}=\frac1\tau.
\]
Therefore
\[
\bar x-x^\star=(1-\beta)e+\beta\Lambda e
 =\bigl(I-\beta A\bigr)e,
\]
which gives \(\bar x_i-x_i^\star=e_i(1-a_i/\tau)\). Applying the standard mixing correction yields
\[
x_2^{(\omega)}-x^\star
 =\bigl((1-\omega)I+\omega\Lambda\bigr)(\bar x-x^\star)
 =(I-\omega A)(I-\beta A)e.
\]
Because \(0<a_i<1\) and \(0\le\omega\le1\), every factor \(1-\omega a_i\) is strictly positive. Hence standard damping cannot change the sign pattern created by the least-squares prediction.

Finally,
\[
\tau=\frac{\sum_i (a_i^3e_i^2)a_i}{\sum_i a_i^3e_i^2}
\]
is a weighted arithmetic mean of the active \(a_i\), with strictly positive weights. If the active gaps are not all equal, \(\min a_i<\tau<\max a_i\). Thus at least one active coordinate has \(a_i>\tau\), causing sign reversal, and another has \(a_i<\tau\), preserving its sign. In one dimension there is only one active gap and the prediction is exact, proving minimality of dimension two.

For the exact witness, \(a_1=1/2\), \(a_2=1/4\), and equal initial errors give \(\tau=17/36\) and \(\alpha_1=36/17\). Substitution gives the displayed negative first coordinate for the entire interval \(0\le\omega\le1\).

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It verifies the closed-form least-squares coefficient, the factorization of the prediction and mixed output, the strict weighted-mean split on a finite family of rational diagonal contractions, the exact two-dimensional witness, positivity of its Picard images, and negativity of the accelerated first coordinate at both endpoints \(\omega=0\) and \(\omega=1\). Since the first coordinate is affine in \(\omega\), endpoint negativity proves negativity for the whole interval. The universal theorem itself is analytic; the finite replay is corroboration rather than an exhaustive proof.

## Relationship to prior work
Walker and Ni give the standard residual least-squares formulation of Anderson acceleration and classify the subject primarily as MSC 65H10. Potra and Engler analyze Anderson acceleration on linear problems, prove its relationship with GMRES, and give a general linear convergence characterization. Their inspected full text includes the linear residual-minimizing formulas but contains no discussion of positivity, coordinatewise order, diagonal sign splitting, or the fact that standard mixing damping cannot repair a sign split already created by the Anderson prediction. Pratapa, Suryanarayana, and Pask apply Anderson acceleration to Jacobi iteration for linear systems; the accessible manuscript metadata and abstract emphasize convergence speed and scaling rather than an order-preservation boundary.

Published-database searches for the exact diagonal-contraction sign law, order-interval crossing, damping invariance, and Anderson-Jacobi positivity did not return an implication-equivalent result. The closest indexed items concerned Euclidean-error transients for GMRES, black-box scalar Aitken-Steffensen robustness, and unrelated stagewise-safe Richardson steps; none states or implies this coordinatewise sign classification under standard Anderson mixing.

## Limitations
The principal originality risk is that an older extrapolation, DIIS, or electronic-structure source may encode the same first-step sign law under different terminology. The Jacobi-acceleration manuscript was accessible here through metadata and abstract rather than complete readable text, so it remains a specific residual risk. The result does not address coefficient-constrained variants such as convex-combination safeguards, nonlinear maps away from their affine linearization, finite precision, or later Anderson steps. It proves that the usual scalar mixing parameter alone cannot undo this first-step crossing mechanism; it does not claim that every stabilization strategy fails.

## References
1. F. A. Potra and H. Engler, “A characterization of the behavior of the Anderson acceleration on linear problems,” arXiv:1102.0796, first public version 2011-02-03; later Linear Algebra and its Applications 438 (2013), 1002–1011.
2. H. F. Walker and P. Ni, “Anderson Acceleration for Fixed-Point Iterations,” SIAM Journal on Numerical Analysis 49 (2011), 1715–1735, doi:10.1137/10078356X. Primary MSC: 65H10.
3. P. P. Pratapa, P. Suryanarayana, and J. E. Pask, “Anderson acceleration of the Jacobi iterative method: An efficient alternative to Krylov methods for large, sparse linear systems,” Journal of Computational Physics 306 (2016), 43–54, doi:10.1016/j.jcp.2015.11.018.
