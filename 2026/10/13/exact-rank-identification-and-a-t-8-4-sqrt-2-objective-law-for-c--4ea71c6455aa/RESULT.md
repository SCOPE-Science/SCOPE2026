# Exact rank identification and a \(t^{-8-4\sqrt{2}}\) objective law for centered \(2\times2\) ERSO-FW
## Finding

For Algorithm 1 (ERSO-FW) of Qi--Wang--Zhang, specialize to the spectrahedron \(\mathcal S^2=\{X\succeq0:\operatorname{tr}X=1\}\), the centered quadratic \(f(X)=\tfrac12\|X-\tfrac12 I_2\|_F^2\), the exact lower bound \(B_0=0\), and the exact quadratic-growth constant \(\mu=1\). For every nonoptimal diagonal start \(X_0=\tfrac12 I_2+s_0\operatorname{diag}(1,-1)\) with \(0<|s_0|\le\tfrac12\), the source simple steps \(\eta_t=2/(t+1)\) give \(X_t=\tfrac12 I_2+s_t\operatorname{diag}(1,-1)\), \(s_2=\operatorname{sgn}(s_0)/6\), and the efficient rank equals the optimal rank \(\widehat r_t=r_t=r^*=2\) for every \(t\ge3\). Thereafter \[s_t=\frac{t-3-2\sqrt2}{t+1}s_{t-1},\qquad s_t=\operatorname{sgn}(s_0)\frac{\Gamma(t-2-2\sqrt2)}{\Gamma(-2\sqrt2)\Gamma(t+2)}.\] Consequently \(f(X_t)\sim \Gamma(-2\sqrt2)^{-2}t^{-8-4\sqrt2}\). Under the source exact-line-search option, the same family instead reaches the optimizer \(I_2/2\) in the first iteration. Thus on this natural full-rank quadratic the adaptive oracle identifies rank exactly at iteration three under the canonical simple steps (versus the paper's general sufficient bound \(T_0' = 290\) for this instance), while the subsequent objective decay has an explicit much-higher-order polynomial law; exact line search collapses the trajectory in one step.

## Assumptions and scope

Let
\[
\mathcal S^2=\{X\in\mathbb S^2:X\succeq0,\ \operatorname{{tr}}X=1\}
\]
and consider
\[
f(X)=\frac12\left\|X-\frac12 I_2\right\|_F^2.
\]
The unique minimizer is \(X_\star=I_2/2\), its rank is \(r^*=2\), and its smallest nonzero eigenvalue is \(\lambda_{r^*}(X_\star)=1/2\). The gradient is \(\nabla f(X)=X-I_2/2\), so \(L=1\). Moreover,
\[
f(X)-f(X_\star)=\frac12\|X-X_\star\|_F^2,
\]
so the source quadratic-growth condition holds globally with the exact constant \(\mu=1\). Because \(r^*=n=2\), the eigengap clause of the source strict-complementarity assumption is not required. We use the valid and natural lower bound \(B_0=f^*=0\).

Restrict the start to the diagonal invariant line
\[
X_0=\frac12 I_2+s_0D,\qquad D=\operatorname{{diag}}(1,-1),\qquad 0<|s_0|\le\frac12.
\]
The claim concerns Algorithm 1 of the source, both with its simple step rule \(\eta_t=2/(t+1)\) and, separately, with its exact-line-search option.

## Proof

Write \(X(s)=I_2/2+sD\). Then
\[
f(X(s))=s^2,\qquad \nabla f(X(s))=sD.
\]
Because \(B_0=0=f^*\) and every working lower bound produced by the source oracle is at most \(f^*\), the monotone update \(B_t=\max\{B_{t-1},B_t^w\}\) gives \(B_t=0\) for all \(t\). Hence the source radius is exactly
\[
d_t=\sqrt{2f(X_t)}=\sqrt2\,|s_t|.
\]

For \(s\ne0\), the minimum-gradient eigenvector is the coordinate vector on the side opposite the sign of \(s\). At the first call, the efficient rank can only be \(0\) or \(1\). For either value, the source thresholding map \(H\) reduces exactly to the opposite rank-one vertex: if \(s>0\), \(\widehat Y=\operatorname{{diag}}(0,1)\), while if \(s<0\), \(\widehat Y=\operatorname{{diag}}(1,0)\). With \(\eta_1=1\), the first iterate is therefore the opposite vertex, so
\[
s_1=-\frac12\operatorname{{sgn}}(s_0).
\]
At the second call the efficient rank is exactly \(1\), the oracle returns the opposite vertex again, and \(\eta_2=2/3\) yields
\[
s_2=\frac16\operatorname{{sgn}}(s_0).
\]

At this point
\[
d_2=\frac{\sqrt2}{6}<\frac13=\lambda_2(X_2).
\]
Since the historical maximum efficient rank is already \(1\), equation (14) of the source forces \(\widehat r_3=2\). Equivalently, the thresholding rank is already the full optimal rank. More generally, whenever \(|s|\le1/6\),
\[
\lambda_2(X(s))-d=\frac12-|s|-\sqrt2|s|
\ge \frac12-\frac{1+\sqrt2}{6}>0,
\]
so the thresholding rank is \(2\).

For full thresholding rank \(2\), the source formula (15) can be evaluated exactly. Its two eigenvalues are paired in reverse order with the two gradient eigenvectors, and the extra \(2d\) mass is placed on the minimum-gradient eigenvector. This gives the scalar oracle map
\[
s\longmapsto -(1+\sqrt2)s.
\]
Thus for every \(t\ge3\),
\[
s_t=(1-\eta_t)s_{t-1}+\eta_t\bigl(-(1+\sqrt2)s_{t-1}\bigr)
=\frac{t-3-2\sqrt2}{t+1}s_{t-1}.
\]
The multiplier has modulus strictly below one for every integer \(t\ge3\), so \(|s_t|\le1/6\) is forward invariant. Hence \(\widehat r_t=r_t=2\) for all \(t\ge3\), proving exact rank identification.

Multiplying the recurrence and using the gamma-product identity gives, for \(t\ge2\),
\[
s_t=\operatorname{{sgn}}(s_0)\frac{\Gamma(t-2-2\sqrt2)}{\Gamma(-2\sqrt2)\Gamma(t+2)}.
\]
The standard gamma-ratio asymptotic \(\Gamma(t+a)/\Gamma(t+b)\sim t^{a-b}\) therefore yields
\[
s_t\sim \frac{\operatorname{{sgn}}(s_0)}{\Gamma(-2\sqrt2)}t^{-4-2\sqrt2},
\qquad
f(X_t)=s_t^2\sim \Gamma(-2\sqrt2)^{-2}t^{-8-4\sqrt2}.
\]

For exact line search, the first oracle point is again the opposite vertex. The segment from any nonoptimal \(X(s_0)\) to that vertex contains \(X_\star\); the minimizing step is
\[
\eta_1^*=\frac{|s_0|}{|s_0|+1/2}\in(0,1],
\]
which makes the new scalar coordinate exactly zero. Thus exact line search reaches \(X_\star\) in one iteration.

## Verification

The identities above were replayed with exact symbolic arithmetic in `artifacts/verify_centered_erso.py`. The checker verifies the source-instance constants, the first two iterates, the strict inequality \(d_2<\lambda_2(X_2)\), the full-rank oracle map, the recurrence, the forward-invariant rank-two region, finite-horizon agreement of the gamma product, and the exact-line-search step. Its recorded output is `VERIFY_OK`.

The computation is supporting evidence only. The infinite-horizon rank statement and asymptotic law follow from the analytic inequalities and product identity in the proof.

## Relationship to prior work

Qi--Wang--Zhang introduce ERSO-FW, prove \(\widehat r_t\le r_t\le r^*\), and show eventual rank identification. Their general sufficient bound specializes here to
\[
T_0=\frac{72L}{\mu\lambda_{r^*}^2}=288,
\qquad
T_0'=T_0+r^*=290.
\]
The source does not give the exact centered \(2\times2\) trajectory, the iteration-three identification, the gamma-product formula, or the \(t^{-8-4\sqrt2}\) objective law.

The earlier Spectral Frank--Wolfe paper of Ding--Fei--Xu--Yang studies fixed block sizes and linear convergence under strict complementarity; it does not contain the efficient-rank mechanism of the 2026 source or this trajectory. The simplex-ball predecessor of Wang--Qi--Zhang supplies the geometric scalar/simplex analogue underlying the spectral ball, but its inspected oracle and convergence sections do not state this matrix full-rank identification trajectory or its exact decay exponent.

## Limitations

The result is an exact theorem for a natural two-dimensional, diagonal, centered quadratic and does not claim the same exponent for arbitrary objectives, dimensions, initial lower bounds, or nondiagonal starts. It uses the source parameter \(\mu=1\), which is exact for this objective, and the known lower bound \(B_0=0\). The full-rank optimum avoids the positive gradient eigengap clause that is needed when \(r^*<n\). The asymptotic claim is for the simple-step branch; exact line search instead terminates at the first update.

## References

Qi, H.; Wang, H.; Zhang, L. *Rank-Adaptive and Linearly Convergent Frank--Wolfe Method over Spectrahedron via Nonconvex Oracle*. arXiv:2609.08522v1, 2026.

Ding, L.; Fei, Y.; Xu, Q.; Yang, C. *Spectral Frank-Wolfe Algorithm: Strict Complementarity and Linear Convergence*. Proceedings of Machine Learning Research 119, 2535--2544, 2020; arXiv:2006.01719.

Wang, H.; Qi, H.; Zhang, L. *Simplex Frank--Wolfe: Linear Convergence and Its Numerical Efficiency for Convex Optimization over Polytopes*. Journal of the Operations Research Society of China, 2026; arXiv:2509.24279.
