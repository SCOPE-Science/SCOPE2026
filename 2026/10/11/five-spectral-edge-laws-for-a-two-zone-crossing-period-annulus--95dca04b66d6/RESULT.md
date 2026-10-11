# Five spectral edge laws for a two-zone crossing period annulus

## Finding

For a naturally balanced two-zone piecewise-affine center, the amplitude domain and original-time period have a sharp five-case spectral classification. In particular, when the left linearization has a **stable defective node**, the period has a logarithm-plus-logarithm-of-logarithm expansion; at an **unstable defective node**, the crossing period instead has a simple pole at a *finite* initial speed. These are distinct physical-time boundary laws, although the return map is the identity throughout each crossing annulus. The focus-domain crossing-time asymptotic follows directly from a single affine half-system and is included solely to connect the spectral regimes; it is not independently claimed as new.

Precisely, take parameters \(a,D,\kappa>0\) and \(\tau\in\mathbb R\), and define the planar piecewise differential equation
\[
(\dot x,\dot y)=\begin{cases}
(\tau x-y,\ Dx-a),&x<0,\\
(-\kappa\tau x-y,\ \kappa^2Dx+\kappa a),&x>0.
\end{cases}
\]
At transverse points of \(x=0\) the normal field is \(\dot x=-y\) on either side, so no sliding convention affects the claimed periodic orbits. Parameterize the orbits by their initial upward-section velocity \(y=r>0\) at \(x=0\); this is the point at which the vector field points into \(x<0\). Define \(C=1+\kappa^{-1}\), \(c=\sqrt D\), and, when \(|\tau|>2c\), \(\delta=\sqrt{\tau^2-4D}\), \(\lambda_+=(\tau+\delta)/2\). For \(\tau=2c\), define \(\lambda_+=c\). Let \(R=+\infty\) when \(\tau<2c\), while \(R=a/\lambda_+\) when \(\tau\ge2c\).

Exactly the initial speeds \(0<r<R\) produce transverse crossing cycles; one cycle passes through each \((0,r)\). Their physical-time minimal period \(P(r)\) increases strictly with \(r\), and the time proportions in \(x<0\) and \(x>0\) are, respectively, \(\kappa/(\kappa+1)\) and \(1/(\kappa+1)\), for every admissible \(r\). The sharp boundary laws are:

1. If \(\tau<-2c\) (stable distinct eigenvalues),
\[
P(r)=\frac C{-\lambda_+}\left[\log\!\left(\frac{Dr}{a\delta}\right)+o(1)\right],\quad r\to\infty.
\]
2. If \(\tau=-2c\) (stable repeated eigenvalue),
\[
P(r)=\frac Cc\left[\log\!\left(\frac{cr}a\right)+\log\log\!\left(\frac{cr}a\right)+o(1)\right],\quad r\to\infty.
\]
3. If \(|\tau|<2c\) (focus), putting \(\omega=\sqrt{D-\tau^2/4}\),
\[
P_\infty=\frac{C\pi}{\omega},\qquad
P_\infty-P(r)\sim\frac{Ca(1+e^{-\tau\pi/(2\omega)})}{Dr},\quad r\to\infty.
\]
4. If \(\tau=2c\) (unstable repeated eigenvalue),
\[
P(r)\sim\frac{Ca}{D(R-r)},\qquad r\uparrow R=a/c.
\]
5. If \(\tau>2c\) (unstable distinct eigenvalues),
\[
P(r)=\frac C\delta\left[\log\!\left(\frac{a\delta}{D(R-r)}\right)+o(1)\right],\quad r\uparrow R=a/\lambda_+.
\]
In each case the asymptotic is taken with \(a,D,\kappa,\tau\) fixed. The small-amplitude law, valid in all five cases, is
\[
P(r)=C\left[\frac{2r}a+\frac{2\tau r^2}{3a^2}+O(r^3)\right],\quad r\downarrow0.
\]

## Assumptions and scope

All parameters are real, \(a,D,\kappa>0\), and \(\tau\in\mathbb R\); \(D\) remains positive in the real-node cases. An orbit is counted only if it has two transverse intersections with the switching line during one least period. At both intersections \(y\ne0\). A possible Filippov equilibrium or nonunique nontransverse motion at the origin is outside the assertion. The results concern actual physical time and not an orbitally equivalent time-rescaled system.

## Proof

**Step 1: Exact left-flight parametrization.** Set \(v=-x>0\) during the left flight. Direct differentiation gives
\[
v''-\tau v'+Dv=-a,\qquad v(0)=0,\quad v'(0)=r.
\]
Let \(u\) be the unique solution to
\[
u''-\tau u'+Du=0,\quad u(0)=0,\quad u'(0)=1,
\]
and set \(W(t)=\int_0^t u(s)\,ds\). Then \(v(t)=r u(t)-aW(t)\). For \(|\tau|<2c\), put \(\omega=\sqrt{D-\tau^2/4}\) and \(t_{\max}=\pi/\omega\); otherwise put \(t_{\max}=\infty\). On \((0,t_{\max})\), \(u>0\) and has the following exact representations:
\[
u(t)=\begin{cases}
 e^{\tau t/2}\sin(\omega t)/\omega,&|\tau|<2c,\\
 t e^{\tau t/2},&|\tau|=2c,\\
 (e^{\lambda_+t}-e^{\lambda_-t})/\delta,&|\tau|>2c,
\end{cases}
\]
where in the last case \(\lambda_\pm=(\tau\pm\delta)/2\). The speed producing a first return at time \(t\) is
\[
r(t)=a\frac{W(t)}{u(t)},\qquad 0<t<t_{\max}.
\]

**Step 2: Strict monotonicity and first return.** For each representation above, \(\log u\) is strictly concave on \((0,t_{\max})\). In the focus, repeated-root, and distinct-real-root cases its second derivative is, respectively,
\[
-\omega^2\csc^2(\omega t),\qquad -t^{-2},\qquad -\frac{\delta^2}{4}\operatorname{csch}^2(\delta t/2),
\]
which are all negative. Write
\[
\frac{W(t)}{u(t)}=\int_0^t\frac{u(t-s)}{u(t)}\,ds.
\]
Differentiation under the integral, noting \(u(0)=0\), shows a strictly positive derivative: its integrand for \(0<s<t\) is positive because the logarithmic derivative of \(u\) strictly decreases. Consequently \(r(t)\) is strictly increasing, with \(r(t)\sim at/2\) as \(t\downarrow0\). If \(r=r(t)\), then for each \(0<s<t\),
\[
v(s)=u(s)[r(t)-r(s)]>0,
\]
so \(t\) is the **first** left return. Its crossing velocity is nonzero, since \(v'(t)=-u(t)r'(t)<0\). The right half is therefore met transversely. Limits of \(W/u\) show that its range is \((0,R)\), with \(R\) exactly as stated. In particular, when \(\tau>2c\), \(W/u\to1/\lambda_+\); at \(\tau=2c\), the same limit equals \(1/c\). In all other cases the ratio diverges at \(t_{\max}\).

**Step 3: Right flight and exact time partition.** Let \(x_L(s),y_L(s)\) denote the left flight on \(0\le s\le t\), with \(x_L(0)=0,y_L(0)=r\). Define
\[
x_R(s)=-\kappa^{-1}x_L(t-\kappa s),\qquad y_R(s)=y_L(t-\kappa s),\quad 0\le s\le t/\kappa.
\]
Direct differentiation verifies the right-zone differential equation, with \(x_R(s)>0\) for its interior and matching switching states at both endpoints. Thus the trajectory closes after exactly one excursion in each zone. Its least period is \(P(r)=t(r)+t(r)/\kappa=Ct(r)\), because no intervening switching-line intersection exists. The displayed residence fractions and strict period monotonicity follow. No transverse crossing cycle can occur for \(r\ge R\), as such an orbit would require a positive first left return. A periodic orbit completely in one open half-plane is impossible: its affine equilibrium lies in the opposite half-plane, and the Poincaré index of a closed planar trajectory would force an enclosed equilibrium.

**Step 4: Asymptotic edge calculations.** For stable distinct real eigenvalues, \(\lambda_+<0\), \(u(t)\sim e^{\lambda_+t}/\delta\) and \(W(t)\to1/D\), hence \(r(t)\sim(a\delta/D)e^{-\lambda_+t}\). For a stable double root \(\tau=-2c\),
\[
r(t)=\frac ac\left[\frac{e^{ct}-1}{ct}-1\right],
\]
which implies, with \(z=ct\), \(z-\log z=\log(cr/a)+o(1)\); logarithmic inversion yields \(z=\log(cr/a)+\log\log(cr/a)+o(1)\). In the focus, \(u(t)\sim e^{\tau\pi/(2\omega)}(\pi/\omega-t)\) and \(W(\pi/\omega)=(1+e^{\tau\pi/(2\omega)})/D\), giving the stated finite period ceiling and its first correction. For the unstable double root \(\tau=2c\),
\[
r(t)=\frac ac\left[1-\frac{1-e^{-ct}}{ct}\right],\qquad R-r(t)\sim\frac{a}{Dt}.
\]
For unstable distinct roots, \(\lambda_->0\) and the exact closed form for \(u,W\) yields
\[
R-r(t)=\frac{a\delta}{D}\frac{e^{\lambda_-t}-1}{e^{\lambda_+t}-e^{\lambda_-t}}\sim\frac{a\delta}{D}e^{-\delta t}.
\]
Each formula yields the corresponding period law on multiplying \(t\) by \(C\). Finally \(u(t)=t+(\tau/2)t^2+O(t^3)\) and \(W(t)=t^2/2+(\tau/6)t^3+O(t^4)\), so \(r(t)=a[t/2-\tau t^2/12+O(t^3)]\); inversion proves the common small-speed law.

## Verification

The standalone `verify.py` uses only the Python standard library and independently evaluates the closed-form fundamental solutions, integral and edge diagnostics for representatives of all five regimes. Run `python3 verify.py`; it prints `CHECK_OK` when the finite tests succeed. The monotonicity and asymptotic claims are analytic consequences of the preceding proof, **not** extrapolations from finite tests.

## Relationship to prior work

Carmona, Fernández-Sánchez, and Novaes [1,2] established necessary and sufficient algebraic conditions for a crossing period annulus in two-zone planar piecewise-linear fields. The present balanced coefficients satisfy those conditions exactly; the existence of the annulus itself is not claimed as a new general criterion. The single-zone focus-flight formula follows directly from an elementary Green-function calculation; its monotonicity and endpoint expansion are included for completeness and are not independently claimed as new. The contribution proposed here is the **sharp, original-physical-time spectral boundary diagram** in the real-node and repeated-node regimes, including the new logarithmic-logarithmic and pole asymptotics.

Liu, Liu, and Wang [3] subsequently addressed at most one critical period in the general two-zone class, a statement about the number of critical points rather than the displayed sharp five-way outer-edge asymptotics. Rezende, Santos, and Torregrosa [4] study period functions for continuous piecewise-linear systems with centers at infinity, in contrast to this discontinuous, virtual-equilibrium, node-inclusive family. These are distinctions of stated claims, not a declaration of publication priority: full texts of [3] and [4] were not both available for definitive comparison.

## Limitations

The theorem is limited to the balanced affine family shown above, transverse crossing cycles, and fixed parameters in each asymptotic regime. No uniform formula is asserted when \(\tau\) varies simultaneously with \(r\); in particular, the five edge expansions cannot be interchanged blindly at either double-eigenvalue boundary. No claim is made about nontransverse Filippov motions through the origin, arbitrary unbalanced piecewise-linear vector fields, or independent external proof certification. A 2026 paper with broad period-function results remains a publication-priority uncertainty because its full text could not be inspected.

## References

[1] V. Carmona, F. Fernández-Sánchez, and D. D. Novaes, *A succinct characterization of period annuli in planar piecewise linear differential systems with a straight line of nonsmoothness*, arXiv:2212.09063, first posted 18 December 2022.

[2] Same authors, *Journal of Nonlinear Science* 33, article 88 (2023), DOI 10.1007/s00332-023-09947-5. The full open-access article includes the characterizing conditions and Poincaré half-map analysis.

[3] H. Liu, C. Liu, and S. Wang, *The crossing period annulus and critical periods for the planar piecewise linear systems with a straight line of separation*, *Journal of Nonlinear Science* 36, article 51 (2026), DOI 10.1007/s00332-026-10269-5. Abstract available; complete text not inspected.

[4] A. C. Rezende, M. A. S. Santos, and J. Torregrosa, *The period function of centers at infinity in planar piecewise linear systems*, *Bulletin des Sciences Mathématiques* 210, article 103809 (2026), DOI 10.1016/j.bulsci.2026.103809. Abstract available.

[5] S. Wang and J. Yang, *Period functions and critical periods of piecewise linear system*, *Electronic Journal of Differential Equations* 2020, article 79, DOI 10.58997/ejde.2020.79; the separating curves in its construction need not be straight.
