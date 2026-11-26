# Two sharp asymptotic saturation laws for one-leaf perturbations of metric-star p-energy extensions

## Finding

Let \(T_m\) be a real scalar metric star with \(m\ge3\) arms of length one. For \(1<p<\infty\), let \(E_p\) be the extension minimizing the sum of the arm \(p\)-energies at prescribed leaf values. Set \(v=(-1,0,1,0,\ldots,0)\). For \(t>0\) put \(v^{(t)}=v+t e_2\) if \(p>2\), and \(v^{(t)}=v+t e_1\) if \(1<p<2\), where \(e_i\) changes just leaf \(i\). Let
\[
Q_p(t)=\frac{\operatorname{Lip}(E_p(v^{(t)})-E_p(v);T_m)}{\operatorname{Lip}(v^{(t)}-v;\partial T_m)}.
\]
The exact leading deficit from the sharp nonquadratic amplification \(2\) is
\[
2-Q_p(t)\sim
\begin{cases}
\displaystyle 2\left(\frac{p-1}{m-2}\right)^{1/(p-1)} t^{(2-p)/(p-1)},&1<p<2,\\[6pt]
\displaystyle \frac{t^{p-2}}{p-1},&p>2,
\end{cases}\qquad t\downarrow0.
\]
Thus each fixed star and fixed nonquadratic exponent has a one-parameter path approaching the sharp modulus, with a specific power and a nonzero leading coefficient. The rate is for these normalized perturbations; it is not an optimal rate over arbitrary data paths or a uniform expansion as \(p\to2\).

## Setup and proof

The extension with center value \(c\) is affine along each arm by Jensen's inequality. Its center uniquely minimizes \(\sum_i|c-v_i|^p\), and satisfies \(\sum_i\psi_p(c-v_i)=0\), where \(\psi_p(z)=\operatorname{sgn}(z)|z|^{p-1}\) and \(\psi_p(0)=0\). Here \(c_p(v)=0\) by symmetry. The equation is strictly increasing in \(c\), strictly decreasing when any leaf coordinate increases, and invariant under common translation of center and leaves. Consequently, for \(s=c_p(v^{(t)})\), one has \(0<s<t\): compare first with \(v\) and then with \(v+t\mathbf1\).

The boundary perturbation has Lipschitz seminorm \(t/2\) because all leaf distances are two. A difference of affine extensions has maximum Lipschitz slope among the arms: a path through the center bounds an off-arm difference by the maximum arm slope times path length. Thus the numerator is \(\max(t-s,s)\). Both arguments below give \(s=o(t)\), and hence the deficit is exactly \(2s/t\) for all sufficiently small \(t>0\).

**Above the quadratic exponent.** For \(p>2\) the exact center equation, at small \(t\), is
\[
(1+s)^{p-1}-(1-s)^{p-1}+(m-3)s^{p-1}=(t-s)^{p-1}.
\]
The difference of the two terms near one is \(2(p-1)s+o(s)\), and the other term on the left is nonnegative. Since the right side is bounded by \(t^{p-1}\), \(s=O(t^{p-1})=o(t)\). Thus \((t-s)^{p-1}\sim t^{p-1}\) and \((m-3)s^{p-1}=o(s)\). It follows that \(s\sim t^{p-1}/[2(p-1)]\).

**Below the quadratic exponent.** For \(1<p<2\) the exact small-\(t\) equation is
\[
(m-2)s^{p-1}=(1-s)^{p-1}-(1+s-t)^{p-1}.
\]
Both arguments on the right tend to one, uniformly for \(0\le s\le t\), and the derivative of the power function there is bounded. The right side is \(O(t)\); thus \(s=O(t^{1/(p-1)})=o(t)\). By the mean-value theorem the right side equals \((p-1)(1+o(1))(t-2s)\sim(p-1)t\). Consequently \(s\sim[(p-1)/(m-2)]^{1/(p-1)}t^{1/(p-1)}\). Dividing both center responses by \(t/2\) proves the displayed laws, including their coefficients.

## Context: the covered global modulus

For any two leaf data with nonconstant difference \(z\), monotonicity and translation equivariance imply that the center difference lies strictly between \(\min z\) and \(\max z\). Therefore the full-star Lipschitz seminorm of the extension difference is strictly less than \(\max z-\min z\); the boundary seminorm is half that range. The perturbations above approach the resulting bound of \(2\). The center for \(p=2\) is the ordinary average, so for coordinate \(i\) the relevant arm difference is \(m^{-1}\sum_{j\ne i}(z_i-z_j)\), bounded in absolute value by \((m-1)(\max z-\min z)/m\); a singleton difference attains this. Two equal arms have the midpoint center for all finite \(p>1\) and ratio one. Fixed-data continuity in \(p\) follows from uniform convergence of the scalar energies on the compact leaf range and uniqueness of their minima.

The global classification, its nonattainment away from \(p=2\), and fixed-data continuity are covered by the stronger positive-weight classification in [A discontinuous Hilbert-exponent transition in weighted star p-harmonic extension stability](https://github.com/Resultary/2026/blob/main/2026/11/17/SCOPE-a-discontinuous-hilbert-exponent-transition-in-weighted-star-p-h--169c7e389bc1/RESULT.md), with equal weights and identical graph distances. Its superquadratic argument computes a tangent response (zero derivative along the perturbed center coordinate after translation); it does not give the first nonzero finite-perturbation coefficient. Its subquadratic argument uses a separate family of regular base data with nonzero residuals and then takes a tangential perturbation. That two-stage sharpness argument does not quantify the response from the single singular base vector above. The distinct claim here is the specific finite-perturbation deficit on the two sides, not the global stability profile or its priority.

The scalar minimization equation and its order principle are standard, as in M. Ishiwata, R. Magnanini and H. Wadade, [A natural approach to the asymptotic mean value property for the p-Laplacian](https://arxiv.org/abs/1604.00520), §2. Their comparison theory supplies the center but not the two finite-data rate laws. Ambient \(\ell_p\) projection norms for the same constant-line minimization describe a different input and output geometry. The full text of the closest such record (`c5b935fc4ff6`) was not available in the lookup, and an equivalent calculation under robust-location or projection terminology remains possible.

## Verification and scope

The two exact scalar balance identities above prove the asymptotic rates for every fixed \(m\ge3\) and \(1<p<\infty\), \(p\ne2\). The accompanying `checker.py` can be run with standard Python 3. Its bisection checks representative center-response coefficients and some global two-data comparisons; those finite computations are not a proof or a check of priority. No claim is made for weighted or unequal-length arms, general trees, nonreal targets, or simultaneous limits in \(p\) and \(t\).
