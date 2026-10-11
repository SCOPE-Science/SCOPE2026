# Universal two-term period growth in an invariant-square quartic center

## Finding
Consider the quartic vector field
\[
\dot x=-(1-x^2)(1+p x)y,\qquad
\dot y=(1-y^2)(1+q y)x,
\]
with \(p,q\in(-1,1)\). Every point of \((-1,1)^2\setminus\{(0,0)\}\) belongs to a periodic trajectory. If \(T(E)\) is the minimal period in the *original time* of the trajectory at normalized energy \(H=E>0\), then
\[
\boxed{T(E)=4E+2\bigl[J(p)+J(-p)+J(q)+J(-q)\bigr]+o(1)},\qquad E\longrightarrow+\infty,
\]
where
\[
J(z)=\int_0^1\frac{dr}{(1+r)(1+zr)}=\frac{\log 2-\log(1+z)}{1-z},\qquad -1<z<1.
\]
In particular, the coefficient of energy is the universal number \(4\), while the full constant offset depends explicitly on both cubic coefficients. The special case \(p=q=0\) gives \(T(E)=4E+8\log 2+o(1)\).

## Assumptions and scope
The parameters \(p,q\) are fixed real numbers with \(|p|<1\) and \(|q|<1\). This is an exact subfamily of the degree-four invariant-square system of Grau and Szántó: in the notation of their defining equation (3), take \((\lambda,a,b,c,d,e)=(0,0,-p,0,q,0)\). The square \(S=(-1,1)^2\) is invariant. Define
\[
F_p(x)=\int_0^x\frac{s}{(1-s^2)(1+p s)}\,ds,\qquad
G_q(y)=\int_0^y\frac{s}{(1-s^2)(1+q s)}\,ds,
\]
and \(H(x,y)=F_p(x)+G_q(y)\), normalized by \(H(0,0)=0\). The parameter \(E>0\) denotes the value of this specific integral, not an arbitrarily shifted energy coordinate. All periods are measured in the original ODE time, without Hamiltonian time reparametrization.

## Proof
**Global energy foliation.** Put \(A_p(x)=(1-x^2)(1+p x)\) and \(B_q(y)=(1-y^2)(1+q y)\). Both are positive in \((-1,1)\). Direct differentiation gives
\[
\frac{dH}{dt}=\frac{x}{A_p(x)}(-A_p(x)y)+\frac{y}{B_q(y)}(B_q(y)x)=0.
\]
Each of \(F_p\) and \(G_q\) is positive off zero, strictly increases with distance from zero separately along either half-axis, behaves as \(x^2/2\) or \(y^2/2\) near zero, and tends to \(+\infty\) at both ends of its interval. Thus \(H\) is proper on \(S\), and every level \(H=E>0\) is a smooth simple closed oval with four axis crossings. The only equilibrium in \(S\) is the origin, so each oval is a periodic orbit and the ovals fill \(S\setminus\{0\}\).

**Exact quadrant-time representation.** For \(\sigma\in\{-1,1\}\), define the increasing function
\[
U_{\sigma,p}(r)=\int_0^r\frac{s}{(1-s^2)(1+\sigma p s)}\,ds,\quad 0\le r<1,
\]
with inverse \(r_{\sigma,p}:(0,\infty)\to(0,1)\). Similarly define \(r_{\tau,q}\). On the quadrant with \(\operatorname{sgn}(x)=\sigma\) and \(\operatorname{sgn}(y)=\tau\), let \(u=F_p(x)\); then \(H-u=G_q(y)\) and the exact identity
\[
\dot u=-xy
\]
shows that the time traversing that quadrant is
\[
T_{\sigma,\tau}(E)=\int_0^E\frac{du}{r_{\sigma,p}(u)r_{\tau,q}(E-u)}.
\]
The endpoints are integrable: \(r_{\sigma,p}(u)\sim\sqrt{2u}\) as \(u\downarrow0\).

**Exact integral constant.** Define \(f_{\sigma,p}(u)=r_{\sigma,p}(u)^{-1}-1\). It is positive, decreasing and integrable on \((0,\infty)\): it is \(O(u^{-1/2})\) near zero; at infinity it decays exponentially because \(U_{\sigma,p}(r)\) has a logarithmic divergence at \(r=1\), with positive coefficient \(1/[2(1+\sigma p)]\). Changing variables \(u=U_{\sigma,p}(r)\) yields
\[
\begin{aligned}
\int_0^\infty f_{\sigma,p}(u)\,du
&=\int_0^1\Bigl(\frac1r-1\Bigr)\frac{r\,dr}{(1-r^2)(1+\sigma p r)}\\
&=\int_0^1\frac{dr}{(1+r)(1+\sigma p r)}=J(\sigma p).
\end{aligned}
\]
Partial fractions give \(J(z)=(\log2-\log(1+z))/(1-z)\) for \(-1<z<1\).

**Convolution remainder.** Expanding the quadrant integrand gives exactly
\[
\begin{aligned}
T_{\sigma,\tau}(E)=E
&+\int_0^E f_{\sigma,p}(u)\,du
 +\int_0^E f_{\tau,q}(v)\,dv\\
&+\int_0^E f_{\sigma,p}(u)f_{\tau,q}(E-u)\,du.
\end{aligned}
\]
The final convolution tends to zero: split at \(u=E/2\), use monotonicity, and bound it above by
\[
f_{\tau,q}(E/2)\|f_{\sigma,p}\|_{L^1}
+f_{\sigma,p}(E/2)\|f_{\tau,q}\|_{L^1}\longrightarrow0.
\]
Consequently \(T_{\sigma,\tau}(E)=E+J(\sigma p)+J(\tau q)+o(1)\). Summing over the four quadrants gives exactly the displayed two-term expansion and finishes the proof.

## Verification
The standalone file `verify_period.py` verifies the vector-field first-integral identity, the change-of-variables rational identity, and the elementary antiderivative formula using exact symbolic operations. It does not replace the analytic monotone-convolution argument. As an independent normalization check, when \(p=q=0\), separation gives \(T(E)=4K(1-e^{-2E})\) with \(K(m)=\int_0^{\pi/2}(1-m\sin^2\theta)^{-1/2}d\theta\), hence \(T(E)=4E+8\log2+o(1)\), agreeing with the general formula. The numerical readings at \(E=2,4,7\) in `VERIFICATION.md` are illustrative only, not part of the proof.

## Relationship to prior work
Grau and Szántó (2024) formulate the full quartic system, identify its five center strata, and give an inverse integrating factor for the stratum containing the present two-parameter family. Their Theorem 2 establishes **local** center conditions; it does not state the global-square foliation with its exact original-time two-term period asymptotic. Villadelprat and Zhang (2019/2020) study period functions for **canonical separable Hamiltonian flows** and their boundary limits. The present vector field has the state-dependent conformal Hamiltonian factor \(A_p(x)B_q(y)\); period functions are not invariant under this time change. Nascimento (2026) develops sufficient monotonicity criteria for separable Hamiltonian period functions, not this explicit period asymptotic. The exact quadratic-energy reduction \(\dot F_p=-xy\) and summable inverse-coordinate defects provide the original-time constant term here.

## Limitations
The theorem is restricted to \(|p|,|q|<1\), where no interior factor \(1+p x\) or \(1+q y\) vanishes. It gives no global classification of other quartic parameter strata, no assertion about exterior-square trajectories, and no monotonicity theorem for \(T'(E)\). The \(o(1)\) is for fixed parameters, not claimed uniform as parameters approach \(\pm1\). The general period-function literature contains related boundary-limit theory; the full text of the 2019 Villadelprat–Zhang article was not accessible during this comparison, so a residual originality risk remains.

## References
1. M. Grau and I. Szántó, “A Polynomial System of Degree Four with an Invariant Square Containing At Least Five Limit Cycles,” *Qualitative Theory of Dynamical Systems* 23 (2024), article 247, https://doi.org/10.1007/s12346-024-01106-9 (published July 26, 2024).
2. J. Villadelprat and X. Zhang, “The Period Function of Hamiltonian Systems with Separable Variables,” *Journal of Dynamics and Differential Equations* 32 (2020), 741–767, https://doi.org/10.1007/s10884-019-09759-w (first online May 18, 2019).
3. F. J. S. Nascimento, “Monotonicity of the Period Function in Planar Separable Hamiltonian Systems: An Extension of Chicone’s Criterion,” *Qualitative Theory of Dynamical Systems* 25 (2026), article 166, https://doi.org/10.1007/s12346-026-01595-w (published September 16, 2026).
