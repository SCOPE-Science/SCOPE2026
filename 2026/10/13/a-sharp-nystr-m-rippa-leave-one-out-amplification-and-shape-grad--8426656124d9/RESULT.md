# A sharp Nyström–Rippa leave-one-out amplification and shape-gradient reversal
## Finding

For the two-site inverse-multiquadric kernel, omitting one Nyström landmark creates an exact and sharp ridge-dependent amplification of leave-one-out cross-validation (LOOCV) residuals, even when the **unapproximated** kernel is nearly the identity. For a particular normalized data vector it also reverses the shape gradient on an entire interval.

Specifically, let \(0<\lambda<1\), and write \(0<t<1\) for the off-diagonal kernel correlation. If \(E\) denotes the inverse-diagonal Rippa leave-one-out residual vector (defined precisely below), then
\[
\sup_{\|y\|_2=1}\|E(Q_t+\lambda I;y)-E(K_t+\lambda I;y)\|_2
=D_\lambda(t)=\frac{t(1-t^2)}{(t^2+\lambda)(1+\lambda)}.
\]

The unique maximizer over \(0<t<1\) is \(t=\sqrt{z_\lambda}\), where
\[
z_\lambda=\frac{\sqrt{(1+3\lambda)^2+4\lambda}-(1+3\lambda)}2,
\qquad
\lim_{\lambda\downarrow0}\sqrt\lambda\,D_\lambda(\sqrt{z_\lambda})=\frac12.
\]
Thus the sharp leading amplification is \(1/(2\sqrt\lambda)\), with exact equality in the operator norm achieved by \(y=(0,1)^{\mathsf T}\).

For that same unit vector, the matched-regularization squared LOOCV losses are
\[
L_{\mathrm{full}}(t)=1+\frac{t^2}{(1+\lambda)^2},\qquad
L_{\mathrm{Nys}}(t)=1+\frac{t^2}{(t^2+\lambda)^2}.
\]
The former is strictly increasing for all \(0<t<1\), while the latter is strictly decreasing for \(\sqrt\lambda<t<1\). The latter has a strict interior **maximum**, not a minimum, at \(t=\sqrt\lambda\), where its value is \(1+1/(4\lambda)\). On this entire interval, the derivatives with respect to either \(t\) or the actual positive RBF shape parameter have opposite signs.

## Assumptions and scope

Take two distinct sites at distance \(h>0\) and the inverse-multiquadric kernel \(\phi(h;\varepsilon)=(1+(\varepsilon h)^2)^{-1/2}\). Every \(t\in(0,1)\) corresponds to a unique \(\varepsilon>0\). The full two-site interpolation matrix and its one-landmark Nyström approximation are
\[
K_t=\begin{pmatrix}1&t\\t&1\end{pmatrix},\qquad
Q_t=K_t[:,1]\bigl(K_t[1,1]\bigr)^{-1}K_t[1,:]
=\begin{pmatrix}1&t\\t&t^2\end{pmatrix}.
\]
The landmark is the first site; choosing it is a permissible specialization, not a claim about every random landmark selection. Apply **the same** ridge \(\lambda>0\) to both operators: \(H_t=K_t+\lambda I\), \(\widetilde H_t=Q_t+\lambda I\). Both are positive definite; \(K_t\) is positive definite with spectrum \(1\pm t\).

For any positive-definite \(H\) and any data vector \(y\in\mathbb R^2\), define the regularized inverse-diagonal leave-one-out residuals by
\[
E_i(H;y)=\frac{(H^{-1}y)_i}{(H^{-1})_{ii}},\qquad i=1,2.
\]
This is the exact leave-one-out error for the ridge-kernel linear predictor on the remaining point, and specializes to Rippa's formula without ridge. The principal claim is about this precisely specified matched-ridge comparison, not about unregularized-versus-regularized objectives or the complete empirical parameter-tuning protocol in the motivating study. The extension to arbitrary dimension below is for block-diagonal normalized positive-definite kernels, not necessarily exact inverse-multiquadric Gram matrices.

## Proof

**1. Exact residual operators.** For any real symmetric positive-definite matrix \(H=\begin{psmallmatrix}a&b\\b&d\end{psmallmatrix}\), direct inversion gives
\[
E(H;y)=\begin{pmatrix}y_1-(b/d)y_2\\y_2-(b/a)y_1\end{pmatrix}.
\]
Consequently
\[
E(H_t;y)=\begin{pmatrix}y_1-\frac{t}{1+\lambda}y_2\\y_2-\frac{t}{1+\lambda}y_1\end{pmatrix},\qquad
E(\widetilde H_t;y)=\begin{pmatrix}y_1-\frac{t}{t^2+\lambda}y_2\\y_2-\frac{t}{1+\lambda}y_1\end{pmatrix}.
\]
Their difference is the rank-one operator \(y\mapsto(-D_\lambda(t)y_2,0)^{\mathsf T}\), where \(D_\lambda\) has the displayed formula, since \(t/(t^2+\lambda)-t/(1+\lambda)=t(1-t^2)/((t^2+\lambda)(1+\lambda))\). Hence the operator norm is exactly \(D_\lambda(t)\), attained at \(y=e_2\).

**2. Sharp amplification.** Differentiating gives
\[
D_\lambda'(t)=\frac{\lambda-(1+3\lambda)t^2-t^4}{(1+\lambda)(t^2+\lambda)^2}.
\]
The numerator is strictly decreasing on \(t>0\), is positive at \(t=0\), and negative at \(t=1\). It therefore has exactly one zero on \((0,1)\). Substituting \(z=t^2\) gives \(z^2+(1+3\lambda)z-\lambda=0\), whose unique positive root is \(z_\lambda\) above. This proves global unique maximization. Dividing the defining equation by \(\lambda\) proves \(z_\lambda/\lambda\to1\) as \(\lambda\downarrow0\), and substitution into \(\sqrt\lambda D_\lambda(\sqrt{z_\lambda})\) yields \(1/2\). Directly at \(t=\sqrt\lambda\),
\[
D_\lambda(\sqrt\lambda)=\frac{1-\lambda}{2\sqrt\lambda(1+\lambda)},
\]
which already realizes the same leading constant. Meanwhile \(\kappa_2(K_{\sqrt\lambda})=(1+\sqrt\lambda)/(1-\sqrt\lambda)\to1\). This is **not** a claim that \(Q_t\) closely approximates \(K_t\) in spectral norm: indeed \(\|K_t-Q_t\|_2=1-t^2\), which approaches one in this limit.

**3. Shape-gradient reversal.** Set \(y=e_2\) in the exact residual formulas to obtain the two losses displayed above. Their derivatives satisfy
\[
L_{\mathrm{full}}'(t)=\frac{2t}{(1+\lambda)^2}>0,\qquad
L_{\mathrm{Nys}}'(t)=\frac{2t(\lambda-t^2)}{(t^2+\lambda)^3}.
\]
For \(0<\lambda<1\), the second derivative changes sign precisely at \(t=\sqrt\lambda\), from positive to negative. Therefore the surrogate has a unique strict interior maximum there, whereas the full loss is increasing throughout. Since \(dt/d\varepsilon=-h^2\varepsilon(1+(\varepsilon h)^2)^{-3/2}<0\), the two shape derivatives also oppose each other whenever \(t>\sqrt\lambda\), equivalently
\[
0<\varepsilon h<\sqrt{\lambda^{-1}-1}.
\]
The maximum surrogate loss is \(1+1/(4\lambda)\), whereas the full loss there is \(1+\lambda/(1+\lambda)^2\to1\). For example, taking \(t=2\sqrt\lambda\) when \(0<\lambda<1/4\) gives strict gradient reversal while \(\kappa_2(K_t)\to1\).

**4. A codimension-one extension.** For every \(n\ge2\), let \(K^{(n)}=K_t\oplus I_{n-2}\), sample every landmark except coordinate two, and let \(y=e_2\). The resulting Nyström approximation is exactly \(Q_t\oplus I_{n-2}\). The full kernel has condition number \((1+t)/(1-t)\), and all above residual formulas persist in its first two coordinates; the other coordinates contribute zero LOOCV error. Thus the same effect is not tied to a rank-one sketch dimension, although the displayed two-site inverse-multiquadric realization is the direct RBF example.

## Verification

The standalone `verify.py` (Python 3 standard library only) independently computes exact rational inverses and leave-one-out residuals for 2,800 rational input cases; it checks the exact operator discrepancy, equality witness, and recovery after filling the missing Nyström diagonal. It checks 2,340 rational derivative-sign and stationary-numerator cases plus 50,000 numerical comparisons of the unique analytic maximum against the full admissible interval. The observed execution result was:

`VERIFY_OK exact_two_by_two_loo_checks=2800 exact_shape_derivative_checks=2340 numeric_peak_comparisons=50000`

These are finite arithmetic checks only. The universal identities, thresholds, and sharp limit are proved algebraically above. Run `python verify.py` from the extracted package contents.

## Relationship to prior work

Lyu and Veiga (2026) define exactly the column-landmark Nyström approximation, positive-ridge Woodbury inverse, inverse-multiquadric RBF, and shape-tuning LOOCV loss used here (Sections 2–3). Their paper includes numerical evidence of sensitivity and discusses landscape optimization; it does **not** give this sharp two-site operator norm, exact worst-case correlation, or sign-reversal phase. Those specific algebraic classifications, not Nyström or Rippa's formula, constitute the stated finding.

Rippa's classical inverse-diagonal identity is the starting point, not a novelty claim. Bucci, Nakatsukasa, and Park (2025) analyze numerical stability of Nyström core pseudoinversion and truncation. Here the one-by-one core is exactly \(1\) and the discrepancy occurs in exact arithmetic through a missing diagonal; their stability results do not imply this sharp cross-validation landscape. Existing diagonal-correction methods for sparse kernel approximations could eliminate the two-site defect by adding \(\operatorname{diag}(0,1-t^2)\); such corrections are not claimed as new.

## Limitations

The concrete inverse-multiquadric example has two sites and one Nyström landmark. It establishes existence, a sharp two-site operator norm, and an exact derivative classification—not a universal failure frequency or a bound for the multi-landmark randomized implementation. Its divergence assumes a ridge parameter tending to zero. The full kernel is well-conditioned in the sharp boundary layer, but the low-rank approximation itself is **not** a small relative error approximation to that kernel; this limits how far the conclusion extrapolates. The codimension-one direct-sum extension applies to general normalized SPD Gram matrices and is not asserted to be an exact multi-site inverse-multiquadric Gram matrix. The result does not imply gradient descent converges to the false maximum. No floating-point errors are needed or analyzed. A complete historical literature exclusion is not asserted; independent validation remains outstanding.

## References

1. J. Lyu and M. Han Veiga, *Low-rank approximation of Rippa method for RBF interpolation*, arXiv:2602.10248v1 (first submitted 2026-02-10), Sections 1–3 and 5. https://arxiv.org/html/2602.10248v1
2. S. Rippa, *An algorithm for selecting a good value for the parameter c in radial basis function interpolation*, Advances in Computational Mathematics 11 (1999), 193–210. DOI:10.1023/A:1018975909870.
3. A. Bucci, Y. Nakatsukasa, and T. Park, *Numerical Stability of the Nyström Method*, arXiv:2511.15583v2 (2025), Sections 1–3. https://arxiv.org/html/2511.15583v2
