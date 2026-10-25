# A sharp mean-square stability frontier for one-cell randomized Runge–Kutta on delayed feedback

## Finding

Apply the independent uniform-stage randomized two-stage Runge–Kutta construction of Difonzo, Przybyłowicz, Wu and Xie [1], with exactly one step per delay interval, to the scalar delay equation
\[
 u'(t)=-a u(t-\tau),\qquad a>0,\quad \tau>0.
\]
Let \(z=a\tau\). For arbitrary deterministic starting triples of the resulting homogeneous delayed recurrence, **exponential mean-square stability holds exactly when**
\[
 0<z<\rho,
 \qquad q(\rho)=0,\qquad
 q(z)=z^7-z^5-4z^4-4z^3+12z^2-24z+24,
\]
where \(\rho\) is the unique root of \(q\) in \((1,6/5)\), numerically \(\rho\approx1.14447604735408\). At the threshold, the mean-square state cannot decay for any nonzero deterministic starting triple; strictly above it and before the deterministic stability boundary, the mean-square state grows at least geometrically for every nonzero triple.

The expected state follows the *deterministic midpoint-stage recurrence*, whose sharp exponential-stability boundary is the unique positive root \(\delta\) of
\[
 f(z)=4-4z+2z^2-z^4=0,
 \qquad \delta\approx1.20104593104289.
\]
Hence \(\rho<\delta\), and on the entire nonempty interval \(\rho<z<\delta\) the expected state decays exponentially but its expected squared norm grows at least geometrically for every nonzero deterministic starting triple. An exact rational witness is \(z=7/6\):
\[
 q(7/6)=-\frac{181541}{279936}<0,
 \qquad f(7/6)=\frac{263}{1296}>0.
\]
For a constant nonzero prescribed history, the actual method produces a nonzero deterministic initial triple, so the gap also occurs for the original delay integrator rather than only abstract recurrence initializations.

## Assumptions and scope

Use independent stage fractions \(U_j\sim\mathrm{Uniform}(0,1)\) for each delay interval, exact real arithmetic, a one-cell grid \(h=\tau\), and the original *freshly reconstructed* intermediate delayed stage from [1, equations (2.3)–(2.4)]. Write \(Y_j\) for the numerical value at \(t=j\tau\). With a constant history \(u(t)=c\) for \(-\tau\le t\le0\), the method starts at \(Y_{-1}=Y_0=c\), \(Y_1=(1-z)c\), and for \(j\ge1\) obeys
\[
 Y_{j+1}=Y_j-zY_{j-1}+z^2 U_jY_{j-2}.
\]
More generally, analyze this last recurrence from any deterministic \(V_1=(Y_1,Y_0,Y_{-1})^{\mathsf T}\in\mathbb R^3\), independent of future stages, with \(V_1\ne0\). Mean-square stability means \(\mathbb E\|V_j\|_2^2\to0\) for every such triple, exponentially with a common rate depending only on \(z\). The comparison of expectation concerns \(\mathbb E V_j\), not the magnitude \(\mathbb E\|V_j\|_2\).

This one-cell construction is well-defined even outside a separate *finite-horizon error theorem's* mesh-size assumptions; no such error bound is invoked here. The randomized stages are algorithmic quadrature points; there is no stochastic forcing in the underlying differential equation.

## Proof

**1. Exact delayed recurrence and covariance operator.** The source's delayed stage is
\[
 \widetilde Y_{j-1}=Y_{j-1}-zU_jY_{j-2},
\]
and its final update is \(Y_{j+1}=Y_j-z\widetilde Y_{j-1}\), proving the recurrence above. Set
\[
 B_u(z)=\begin{pmatrix}1&-z&z^2u\\1&0&0\\0&1&0\end{pmatrix},\qquad
 A(z)=B_{1/2}(z),\qquad e_1=(1,0,0)^{\mathsf T},\quad e_3=(0,0,1)^{\mathsf T}.
\]
Then \(V_{j+1}=B_{U_j}(z)V_j\) and \(\mathbb E V_{j+1}=A(z)\mathbb E V_j\). Independence, \(\mathbb E U_j=1/2\), and \(\operatorname{Var}(U_j)=1/12\) give for every symmetric covariance/second-moment matrix \(X\)
\[
 \mathcal T_z(X)=A(z)XA(z)^{\mathsf T}
 +\frac{z^4}{12}(e_3^{\mathsf T}Xe_3)e_1e_1^{\mathsf T},
 \qquad \mathbb E[V_{j+1}V_{j+1}^{\mathsf T}]
 =\mathcal T_z\bigl(\mathbb E[V_jV_j^{\mathsf T}]\bigr).
\]
These equations also show why the second-moment evolution differs from deterministic midpoint even though the mean evolution agrees with it.

**2. Deterministic stability boundary.** The characteristic polynomial of \(A(z)\) is
\[
 p_z(\lambda)=\lambda^3-\lambda^2+z\lambda-z^2/2.
\]
The cubic Jury conditions (applied in real coefficients) reduce, for \(z>0\), to \(z^2/2<1\), \(z-z^2/2>0\), the automatically positive inequality \(2+z+z^2/2>0\), and \(f(z)>0\). Because
\[
 f'(z)=-4(1-z+z^3)<0\qquad(z\ge0),
\]
with \(1-z+z^3\ge1-2/(3\sqrt3)>0\), \(f\) has one positive root \(\delta\). Exact evaluations give \(f(6/5)=4/625>0\) and \(f(5/4)=-81/256<0\), placing \(\delta\in(6/5,5/4)\). Thus \(A(z)\) is Schur stable exactly for \(0<z<\delta\). The remaining Jury inequalities hold throughout this interval, and none can restore Schur stability beyond \(\delta\) because \(f\) is strictly decreasing.

**3. A scalar positive-operator stability test.** Assume \(0<z<\delta\). For \(E=e_1e_1^{\mathsf T}\), define the convergent discrete Lyapunov series
\[
 X=\sum_{k=0}^{\infty}A(z)^kE(A(z)^{\mathsf T})^k,
 \qquad H(z)=e_3^{\mathsf T}Xe_3
 =\sum_{k=0}^{\infty}(e_3^{\mathsf T}A(z)^ke_1)^2.
\]
The positive operator \(\mathcal T_z\) is exponentially stable **if and only if** \(z^4H(z)/12<1\). To see sufficiency, apply \((I-\mathcal L)^{-1}\) to \(\mathcal L(X)=AXA^{\mathsf T}\): for \(c=z^4/12\), \(cH<1\) permits a strictly positive definite \(W\) with \((I-\mathcal T_z)W=I\), since the scalar correction is the convergent geometric resolvent \((1-cH)^{-1}\). Positivity and the order-unit norm induced by \(W\) then yield a strict contraction of \(\mathcal T_z\) on symmetric matrices.

For necessity and the stronger nondecay statement, set
\[
 G_\lambda=\sum_{k=0}^{\infty}\lambda^{-k-1}(A^{\mathsf T})^k e_3e_3^{\mathsf T}A^k,
\qquad h(\lambda)=e_1^{\mathsf T}G_\lambda e_1,
\]
for \(\lambda\ge1\). The function \(h\) is strictly decreasing, \(h(1)=H(z)\), and \(h(\lambda)\to0\). If \(cH\ge1\), there is a unique \(\lambda\ge1\) with \(ch(\lambda)=1\), and \(\lambda>1\) if \(cH>1\). The adjoint of the second-moment operator satisfies \(\mathcal T_z^*G_\lambda=\lambda G_\lambda\). Moreover, \(G_\lambda\succ0\): the three row vectors \(e_3^{\mathsf T}\), \(e_3^{\mathsf T}A\), \(e_3^{\mathsf T}A^2\) are exactly the three distinct coordinate rows, hence span \(\mathbb R^3\). Consequently, for **every** nonzero deterministic initial triple,
\[
 \mathbb E[V_j^{\mathsf T}G_\lambda V_j]
 =\lambda^{j-1}V_1^{\mathsf T}G_\lambda V_1,
\]
so the ordinary expected squared norm cannot decay at \(\lambda=1\) and grows at least geometrically when \(\lambda>1\). When \(z\ge\delta\), even the mean matrix \(A(z)\) is not Schur, so uniform mean-square stability for all deterministic triples is impossible by Jensen's inequality.

**4. Exact Lyapunov transfer and unique crossing.** Solve \(X-AXA^{\mathsf T}=E\) in the six entries of a symmetric \(3\times3\) matrix. The three shift equations force \(X_{11}=X_{22}=X_{33}\) and \(X_{12}=X_{23}\). Eliminating the remaining off-diagonal entries gives
\[
 H(z)=\frac{4(4+4z-2z^2-z^4)}{z(2-z)(z^2+2z+4)f(z)}.
\]
Direct expansion, or substitution into the six Lyapunov equations, then yields the exact identity
\[
 1-\frac{z^4}{12}H(z)
 =\frac{4q(z)}{3(2-z)(z^2+2z+4)f(z)}.
\]
The denominator is positive for \(0<z<\delta\). Finally,
\[
 -q'(z)=12\bigl((z-1)^2+1\bigr)
 +z^3(16+5z-7z^3)>0
 \quad(0\le z\le5/4),
\]
since \(16+5z-7z^3\ge16-7(5/4)^3>0\). Now \(q(1)=4>0\) and \(q(6/5)=-127464/78125<0\), so \(q\) has exactly one root \(\rho\) in \((0,\delta)\), and it lies in \((1,6/5)\). The positive-operator criterion proves the advertised exact cutoff and the strict gap \(\rho<\delta\).

## Verification

The standalone, standard-library-only `verify.py` independently builds the six-dimensional symmetric second-moment operator from the random stage formula using exact rational arithmetic, solves the discrete Lyapunov equations, checks the closed transfer formula and crossing identity at several rational parameters, checks the cubic Jury inequalities at a rational gap witness, and reconstructs successive source-stage updates. Run `python3 verify.py` in the same directory as this file. The checker returns `PASS: 239 exact-rational identities and independently reconstructed matrices` under Python 3. These finite tests supplement, rather than replace, the symbolic proof above.

## Relationship to prior work

Difonzo, Przybyłowicz, Wu and Xie [1] specify the fresh delayed-stage construction and establish finite-time convergence estimates for time-irregular delay differential equations. Their definitions are the source of the recurrence, but their theorems do not give this long-time mean-square threshold on the pure-delay test equation. Bochacik, Goćwin, Morkisz and Przybyłowicz [2] establish mean-square stability regions for randomized Runge–Kutta applied to **ordinary** scalar differential equations, without a delayed companion state. Their classical separation motivates the delayed question but does not determine the degree-seven cutoff. Stochastic delay Runge–Kutta methods driven by Brownian noise [3] use a different source of randomness and are not direct coverage of independent random internal stages in a deterministic delay equation.

## Limitations

The classification is exact for one step per lag interval, a scalar *pure-delayed* linear feedback, freshly re-evaluated stage delays, and independent uniform stages. It does not classify multi-cell discretizations, nonuniform stage laws, arbitrary current-state drift, stochastic differential equations, almost-sure Lyapunov exponents, or convergence order at small step sizes. The expected-value and expected-squared-norm assertions concern different observables. The result is a self-review; no independent audit or publication-priority certification has been performed.

## References

[1] F. V. Difonzo, P. Przybyłowicz, Y. Wu, X. Xie, *A Randomized Runge–Kutta Method for Time-Irregular Delay Differential Equations*, arXiv:2401.11658v1 (first publicly submitted 2024-01-22), especially equations (2.3)–(2.4), Theorem 4.3, and Section 5. https://arxiv.org/abs/2401.11658

[2] T. Bochacik, M. Goćwin, P. M. Morkisz, P. Przybyłowicz, *Randomized Runge–Kutta Method—Stability and Convergence under Inexact Information*, arXiv:2006.12131 (2020), especially Section 5. https://arxiv.org/abs/2006.12131

[3] *S-ROCK Methods for Stochastic Delay Differential Equations with One Fixed Delay*, Journal of Computational and Applied Mathematics 353 (2019), 345–354, DOI:10.1016/j.cam.2018.12.042 (abstract and introduction compared for scope).
