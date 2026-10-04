# Exact fixed-product rate phase diagram for scalar PDHG
## Finding
Consider the scalar saddle problem
\[
\min_{x\in\mathbb R}\max_{y\in\mathbb R} \frac12x^2+xy-\frac12y^2.
\]
Apply the basic primal-dual hybrid gradient (PDHG) ordering with positive constant steps \(\tau\) and \(\sigma\):
\[
x^{k+1}=\frac{x^k-\tau y^k}{1+\tau},\qquad
\bar x^{k+1}=2x^{k+1}-x^k,\qquad
y^{k+1}=\frac{y^k+\sigma\bar x^{k+1}}{1+\sigma}.
\]
Write \(p=\tau\sigma\) and restrict to \(0<p<1\), the standard sufficient product condition for this unit-coupling problem. For fixed \(p\), the exact asymptotic spectral radius has the following complete phase diagram.

If \(0<p<1/2\), there are exactly two minimizing step pairs, related by swapping primal and dual steps:
\[
\{\tau,\sigma\}=
\left\{
\sqrt{2p(1-p)}-\sqrt{p(1-2p)},
\sqrt{2p(1-p)}+\sqrt{p(1-2p)}
\right\}.
\]
At either pair the two eigenvalues coalesce, and the minimum factor is
\[
\rho_p^*=\frac{\sqrt{1-p}}{\sqrt{1-p}+\sqrt{2p}}.
\]
If \(1/2\le p<1\), the unique fixed-product minimizer is \(\tau=\sigma=\sqrt p\). Over all positive steps with \(\tau\sigma<1\), the unique global minimizer is
\[
\tau=\sigma=\frac1{\sqrt2},\qquad \rho^*=\sqrt2-1.
\]

The reciprocal residual-balancing updates in Algorithm 2 of Goldstein--Li--Yuan--Esser--Baraniuk preserve \(\tau_k\sigma_k\) exactly. Consequently, if that method is initialized with \(\tau_0\sigma_0\ne1/2\), those updates alone cannot reach the globally rate-optimal constant-step pair on this benchmark. This is a limitation of the parameterization, not a claim that the varying-step trajectory cannot transiently outperform a fixed-step trajectory.

## Assumptions and scope
The claim concerns the one-dimensional strongly convex-concave quadratic above, unit coupling, the primal-first PDHG ordering with extrapolation parameter \(1\), positive constant steps for the spectral-radius classification, and the sufficient region \(0<\tau\sigma<1\). The statement about the adaptive method uses only the exact reciprocal form of its step updates; it does not assert a sharp convergence rate for the nonstationary adaptive sequence.

## Proof
With state \(z^k=(x^k,y^k)^T\), one PDHG step is \(z^{k+1}=M z^k\), where
\[
M=\begin{pmatrix}
\dfrac1{1+\tau}&-\dfrac{\tau}{1+\tau}\\[1ex]
\dfrac{\sigma(1-\tau)}{(1+\sigma)(1+\tau)}&
\dfrac{1+\tau-2\tau\sigma}{(1+\sigma)(1+\tau)}
\end{pmatrix}.
\]
Put \(p=\tau\sigma\) and \(s=\tau+\sigma\). Then
\[
T:=\operatorname{tr}M=\frac{s+2-2p}{1+s+p},\qquad
D:=\det M=\frac{1-p}{1+s+p},
\]
and the characteristic discriminant is
\[
T^2-4D=\frac{s^2-8p(1-p)}{(1+s+p)^2}.
\]
For fixed \(p\), positive \(\tau,\sigma\) with product \(p\) realize exactly \(s\ge2\sqrt p\).

Let \(s_c=\sqrt{8p(1-p)}\). In the complex-root regime \(s<s_c\), both roots have modulus \(\sqrt D\), which strictly decreases as \(s\) increases. In the real-root regime \(s>s_c\), the dominant root \(r(s)\) satisfies \(r^2-Tr+D=0\) and
\[
r'(s)=\frac{(3p-1)r(s)+(1-p)}{(1+s+p)^2\sqrt{T^2-4D}}>0.
\]
Indeed, for \(p\ge1/3\) the numerator is immediate; for \(p<1/3\), the bound \(0<r(s)<1\) gives
\[
(1-p)-(1-3p)r(s)>2p>0.
\]
Thus the fixed-product minimum occurs at the feasible point nearest the real/complex transition. The transition is feasible strictly above the arithmetic-geometric lower boundary exactly when
\[
s_c>2\sqrt p\iff p<1/2.
\]
For \(0<p<1/2\), solving \(\tau+\sigma=s_c\) and \(\tau\sigma=p\) gives the two stated pairs. At \(s=s_c\),
\[
1+p+s_c=(\sqrt{1-p}+\sqrt{2p})^2,
\]
so the repeated-root modulus is the stated \(\rho_p^*\). For \(p\ge1/2\), the transition lies at or below the feasible boundary, so strict increase on the real branch makes \(s=2\sqrt p\) optimal; equality in the arithmetic-geometric inequality gives the unique pair \(\tau=\sigma=\sqrt p\).

It remains to minimize over \(p\). On \(0<p<1/2\), \(\rho_p^*=1/(1+\sqrt{2p/(1-p)})\) is strictly decreasing. On \(1/2\le p<1\), put \(t=\sqrt p\). At the balanced pair,
\[
r(t)=\frac{1+t-t^2+t\sqrt{2t^2-1}}{(1+t)^2}.
\]
For \(1/\sqrt2<t<1\), the sign of \(r'(t)\) is the sign of
\[
4t^2+t-1-(3t+1)\sqrt{2t^2-1}.
\]
Both sides of the corresponding comparison are positive, and the exact identity
\[
(4t^2+t-1)^2-(3t+1)^2(2t^2-1)=2(1-t)(1+t)^3>0
\]
shows \(r'(t)>0\). Hence the global minimum is attained uniquely at \(p=1/2\), \(\tau=\sigma=1/\sqrt2\), where \(r=1/(1+\sqrt2)=\sqrt2-1\).

Finally, every nontrivial residual-balancing update in Algorithm 2 multiplies one step by \(1-\alpha_k\) and the other by its reciprocal; the no-update branch changes neither. Therefore \(\tau_{k+1}\sigma_{k+1}=\tau_k\sigma_k\) identically.

## Verification
The accompanying `verify.py` checks the matrix trace and determinant formulas on exact rational samples, checks the discriminant identity, coefficient-checks the polynomial identity used for monotonicity on the balanced branch, and numerically probes the stated phase diagram on a dense deterministic grid. These computations are supplementary checks; the proof above establishes the continuum statements analytically.

## Relationship to prior work
Goldstein--Li--Yuan--Esser--Baraniuk introduce the basic PDHG ordering, state the usual product stability condition, motivate balancing primal and dual residuals, and give reciprocal adaptive updates that keep the step-size product unchanged. Their paper does not state the scalar spectral-radius phase diagram above.

Fercoq later studies PDHG step selection by directly estimating and minimizing the spectral radius on quadratic problems and explicitly observes that spectral monitoring can outperform residual balancing. That work supplies the closest broader framework found: it gives the block iteration matrix for general quadratics and treats spectral-radius minimization algorithmically, but the inspected text does not give this one-dimensional closed-form transition at \(p=1/2\), the two asymmetric fixed-product minimizers for \(p<1/2\), or the global pair \(1/\sqrt2,1/\sqrt2\). The present result is therefore a closed-form classification inside that broader viewpoint, together with an exact statement about the invariant product in the earlier adaptive rule.

## Limitations
This is an exact scalar benchmark, not a multidimensional worst-case theorem. It classifies constant-step asymptotic spectral radii and identifies a parameter invariant of the residual-balancing update; it does not prove that every adaptive trajectory converges at the best constant-step rate, nor that changing the product adaptively is always beneficial on general problems. A residual originality risk remains that the same scalar algebra may appear in an unindexed note, thesis, or implementation analysis.

## References
1. T. Goldstein, M. Li, X. Yuan, E. Esser, R. Baraniuk, *Adaptive Primal-Dual Hybrid Gradient Methods for Saddle-Point Problems*, arXiv:1305.0546. First public arXiv version: 2013-05-02. Primary MSC: 65K15.
2. O. Fercoq, *Monitoring the Convergence Speed of PDHG to Find Better Primal and Dual Step Sizes*, arXiv:2403.19202, 2024.
