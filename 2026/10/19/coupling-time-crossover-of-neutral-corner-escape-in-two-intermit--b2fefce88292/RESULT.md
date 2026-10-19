# Coupling-time crossover of neutral-corner escape in two intermittent maps

## Finding
Fix \(1<p<2\), let \(\xi_p\in(0,1)\) solve \(\xi_p+\xi_p^p=1\), and fix \(0<r<\xi_p\). On the unit square consider the coupled Pomeau–Manneville map
\[
F_{p,\varepsilon}(x,y)=\left(f_p((1-\varepsilon)x+\varepsilon y),\ f_p((1-\varepsilon)y+\varepsilon x)\right),\qquad f_p(u)=(u+u^p)\bmod1,
\]
with \(0\le\varepsilon\le 1/2\). Let \(\tau_r\) be the first nonnegative iterate at which \(\max(x,y)\ge r\), and choose the initial point uniformly in \([0,r)^2\). Write \(\beta=p-1\) and \(a_p=\beta^{-1/\beta}\).

For any sequence \(\varepsilon_n\in[0,1/2]\) with \(n\varepsilon_n\to\rho\in[0,\infty]\), including \(\rho=+\infty\), the following limit exists:
\[
\boxed{\lim_{n\to\infty}n^{2/\beta}\Pr_{[0,r)^2}\{\tau_r>n\}=\frac{A_p(\rho)}{r^2}.}
\]
For finite \(\rho\), let \(\Phi^\rho_t(u,v)\) solve the positive-quadrant ODE
\[
\dot U=U^p+\rho(V-U),\qquad \dot V=V^p+\rho(U-V),\quad (U(0),V(0))=(u,v),
\]
and let \(T_\rho(u,v)\) be its maximal forward existence time, with \(T_\rho(0,0)=+\infty\). The *intrinsic crossover coefficient* is the completely specified finite area
\[
A_p(\rho)=\operatorname{Leb}_2\{(u,v)\in[0,\infty)^2:T_\rho(u,v)>1\},\qquad 0\le\rho<\infty.
\]
At the fast-coupling endpoint put \(A_p(+\infty)=2a_p^2\). The coefficient is continuous and nondecreasing on \([0,+\infty]\), with sharp endpoint values and strict interior bounds
\[
\boxed{A_p(0)=a_p^2,\qquad a_p^2<A_p(\rho)<2a_p^2\quad(0<\rho<\infty),\qquad\lim_{\rho\to\infty}A_p(\rho)=2a_p^2.}
\]
Thus for every *fixed* \(0<\varepsilon\le1/2\) the leading escape-survival coefficient is exactly twice the uncoupled coefficient, although both have exponent \(2/(p-1)\). The singular crossover occurs when coupling times observation duration is of order one: \(\varepsilon_n\asymp1/n\). The finite-coupling coefficient is defined intrinsically by an ODE area; no elementary closed form is claimed for general finite \(\rho\).

## Assumptions and scope
The result concerns first exit from the local square, not global recurrence, mixing, invariant densities, or return times after reinjection. The initial ensemble is normalized two-dimensional Lebesgue measure on \([0,r)^2\); no stationary-measure assertion is made. On every orbit segment before first exit, each mixed coordinate lies below \(r<\xi_p\), and therefore the nonlinear map has the exact branch form \(f_p(u)=u+u^p\). For \(n\)-dependent coupling the same \(\varepsilon_n\) is held fixed during all \(n\) iterates. The first-public motivating source is arXiv:1410.4806v1, publicly submitted 2014-10-17, whose equation (2.2) is the map above.

## Proof
**1. Localization of every survivor.** Put \(h_n=n^{-1/\beta}\). Until exit write \(m_k=(x_k+y_k)/2\). Row-stochastic mixing preserves the mean. Jensen's inequality, valid because \(p>1\), gives
\[
m_{k+1}=m_k+\frac{a_k^p+b_k^p}{2}\ge m_k+m_k^p,
\]
where \(a_k=(1-\varepsilon_n)x_k+\varepsilon_n y_k\) and \(b_k=(1-\varepsilon_n)y_k+\varepsilon_n x_k\). Let
\[
c_{p,r}=\min_{0\le t\le r^\beta}\frac{1-(1+t)^{-\beta}}{t}>0,
\]
with the quotient at \(t=0\) defined as \(\beta\). If \(\tau_r>n\), then \(m_k<r\) for \(k\le n\), and the scalar inequality yields
\[
m_k^{-\beta}-m_{k+1}^{-\beta}\ge c_{p,r}\quad (0\le k<n).
\]
Therefore \(m_0\le (nc_{p,r})^{-1/\beta}\) and both coordinates of the scaled initial point \((x_0/h_n,y_0/h_n)\) lie in the fixed compact interval \([0,2c_{p,r}^{-1/\beta}]\). This uniform localization works for every coupling sequence.

**2. Exact scaled recurrence and finite crossover.** For scaled coordinates \(X_k=x_k/h_n\), \(Y_k=y_k/h_n\), let \(\rho_n=n\varepsilon_n\). Before exit, and equally for the globally defined positive polynomial extension, the evolution is *exactly*
\[
\begin{split}
X_{k+1}&=X_k+\frac{\rho_n}{n}(Y_k-X_k)+\frac1n\left((1-\varepsilon_n)X_k+\varepsilon_n Y_k\right)^p,\\
Y_{k+1}&=Y_k+\frac{\rho_n}{n}(X_k-Y_k)+\frac1n\left((1-\varepsilon_n)Y_k+\varepsilon_n X_k\right)^p.
\end{split}
\]
If \(\rho_n\to\rho<\infty\), this is a consistent first-order Euler scheme for the displayed ODE, with locally Lipschitz vector field on the positive quadrant. Standard finite-interval Euler estimates give uniform convergence of trajectories on any compact time interval strictly before their ODE blow-up, uniformly for initial data from a compact set where the limiting solutions remain bounded.

Let \(S_\rho=\{T_\rho>1\}\). If an initial scaled point belongs to \(S_\rho\), its ODE solution is bounded through time one, and the actual orbit remains in \([0,r)^2\) for all \(n\) steps when \(n\) is large. Conversely, if \(T_\rho<1\), select a time \(t_0<T_\rho\) such that the ODE mean is arbitrarily large. The discrete scaled mean satisfies \(M_{k+1}\ge M_k+M_k^p/n\). Starting from \(M\), the time to rise through dyadic levels \(M,2M,4M,\ldots\) until reaching \(r/h_n\) is bounded by
\[
\frac{nM^{-\beta}}{1-2^{-\beta}}+O(\log n)
\]
iterations. Taking \(t_0\) sufficiently close to the ODE blow-up time makes this less than the remaining \(n(1-t_0)\) steps, forcing first exit before time \(n\). No finite computation is used to infer finite-time blow-up.

The ODE is cooperative: each off-diagonal vector-field derivative equals \(\rho\ge0\). Thus \(S_\rho\) is coordinatewise downward closed. For rigor concerning the blow-up-time equality set, observe that the maximum coordinate \(M(t)=\max(U(t),V(t))\) obeys \(M^p-\rho M\le M\prime\le M^p\) almost everywhere. Consequently every finite-time blow-up has the universal leading profile \(M(t)\sim[\beta(T_\rho-t)]^{-1/\beta}\). If two strictly positive initial vectors satisfy \(w_2\le\alpha w_1\) coordinatewise for some \(0<\alpha<1\), the field at \(\alpha W_1(t)\) is bounded above by the derivative of that path, because \(\alpha U^p\ge\alpha^pU^p\) while coupling is linear. Cooperative comparison gives \(W_2(t)\le\alpha W_1(t)\). They cannot both blow up at the same time, since their maxima would each have the same leading blow-up coefficient, contradicting the ratio bound. Hence decreasing a positive initial vector strictly increases its blow-up time. For \(\rho>0\), any nonzero solution enters the strictly positive quadrant immediately; for \(\rho=0\) strict scalar monotonicity applies directly. Thus \(\{T_\rho=1\}\) lies on the boundary of \(S_\rho\). In each bounded rectangle, the boundary of a coordinatewise downward-closed set is a graph of a monotone function together with at most countably many vertical segments, so its planar Lebesgue measure is zero. Therefore survivor-indicator convergence holds almost everywhere. Localization from Step 1, a fixed Jacobian \(h_n^2=n^{-2/\beta}\), and dominated convergence now prove the asserted area formula for \(0\le\rho<\infty\).

**3. Endpoint for coupling faster than inverse observation time.** Suppose \(n\varepsilon_n\to\infty\) with \(0\le\varepsilon_n\le1/2\). For the scaled polynomial recurrence put \(m_k=(X_k+Y_k)/2\), \(d_k=(X_k-Y_k)/2\), and \(\lambda_n=1-2\varepsilon_n\in[0,1]\). On bounded portions of the trajectory,
\[
\begin{split}
m_{k+1}&=m_k+\frac{(m_k+\lambda_nd_k)^p+(m_k-\lambda_nd_k)^p}{2n},\\
d_{k+1}&=\lambda_nd_k+\frac{(m_k+\lambda_nd_k)^p-(m_k-\lambda_nd_k)^p}{2n}.
\end{split}
\]
Choose integers \(k_n=o(n)\) with \(k_n\varepsilon_n\to\infty\), possible since \(n\varepsilon_n\to\infty\). For bounded initial scaled states, the mean changes by only \(O(k_n/n)=o(1)\) during this initial layer; the mean stays bounded there using \(m_{k+1}\le m_k+2^{p-1}m_k^p/n\). By the mean-value theorem,
\[
|d_{k+1}|\le\lambda_n(1+C/n)|d_k|
\]
while the mean remains bounded. Hence \(d_{k_n}\to0\) because \(\lambda_n^{k_n}\le\exp(-2k_n\varepsilon_n)\to0\). On any later bounded part of the evolution, \(|d_k|\le|d_{k_n}|e^C=o(1)\); the mean is therefore an Euler approximation to \(\dot m=m^p\), with initial value \(m(0)=(u+v)/2\). The scalar solution survives through time one precisely when \(m(0)<a_p\). If \(m(0)>a_p\), Jensen's scalar inequality and the dyadic argument from Step 2 force discrete exit before time \(n\). The exceptional line \(u+v=2a_p\) has zero area. Dominated convergence using Step 1 gives the endpoint area of the triangle \(u+v<2a_p\), namely \(2a_p^2\). This includes every fixed positive coupling and the limiting case \(\varepsilon_n=1/2\).

**4. Geometry and variation of the crossover area.** In the ODE let \(m=(U+V)/2\) and \(d=|U-V|/2\). With
\[
F(m,d)=\frac{(m+d)^p+(m-d)^p}{2},\qquad G(m,d)=\frac{(m+d)^p-(m-d)^p}{2},
\]
one has \(\dot m=F(m,d)\) and \(\dot d=G(m,d)-2\rho d\) on \(0\le d\le m\). Both cross-partials \(\partial_d F\) and \(\partial_mG\) are nonnegative. The comparison theorem for cooperative systems shows that increasing \(\rho\) cannot increase either \(m(t)\) or \(d(t)\) for common initial conditions before blow-up; thus \(S_{\rho_1}\subseteq S_{\rho_2}\) if \(\rho_1\le\rho_2\). At \(\rho=0\) the coordinates solve independent scalar equations, so \(S_0=[0,a_p)^2\) up to its boundary and \(A_p(0)=a_p^2\).

For all \(\rho\), the upper coordinate has derivative at most its scalar power, hence the open square \((0,a_p)^2\) survives. Jensen gives \(\dot m\ge m^p\), hence \(S_\rho\) is contained, up to its boundary, in \(u+v<2a_p\). If \(0<\rho<\infty\), the initial point \((a_p,b)\), \(0<b<a_p\), survives: while its coordinates differ, the maximum grows strictly more slowly than the scalar solution starting at \(a_p\), and comparison after any positive time postpones blow-up beyond one. An open neighborhood of this point adds positive area beyond the square. In contrast, starting with \(u+v=2a_p\) and \(u\ne v\), strict convexity gives \(\dot m(0)>a_p^p\) and the mean blows up before one; an open neighborhood inside the triangle is excluded. Thus \(a_p^2<A_p(\rho)<2a_p^2\) for every finite positive \(\rho\). Parameter-continuous dependence of the ODE away from the zero-area blow-up boundary proves continuity of \(A_p\) at each finite \(\rho\). As \(\rho\to\infty\), transverse deviations decay in a layer of length \(o(1)\) while the mean changes by \(o(1)\); on bounded scalar trajectories the mean tends to \(\dot m=m^p\). Therefore survivor indicators converge almost everywhere to the triangle indicator and \(A_p(\rho)\to2a_p^2\), completing the proof.

## Verification
The included file `check.py` is runnable using Python 3 without third-party packages. It verifies the scalar threshold and endpoint area constants at \(p=3/2\), compares a Runge–Kutta solution of the crossover ODE with its exact scaled discrete recurrence, and checks the strong-coupling scalar limit on a fixed non-diagonal sample. Run `python3 check.py`; expected output begins `VERIFY_OK`. These are finite numerical consistency checks only; the complete infinite-family assertion is proved in the preceding steps.

## Relationship to prior work
Sala, Manchein and Artuso (arXiv:1410.4806) define this exact two-site coupling and numerically observe an escape exponent \(2/(p-1)\) from a small square, across uncoupled and positively coupled systems (Section 3.3 and Figure 4). Their inspected analysis does not give the leading coefficient, the factor-two noncommuting limit, or an ODE-valued coupling-time crossover. Kim's work on coupled-map intermittency (arXiv:chao-dyn/9808002) treats saddle-node critical renormalization, not this neutral-corner survivor area. Bahsoun and Korepanov (arXiv:2303.05311) treat self-consistent mean-field stationary measures and correlation decay, rather than the two-site first-exit ensemble. General Euler-limit and cooperative-ODE comparison principles are standard proof tools; the object-specific survivor constant and its sharp endpoints are the claimed findings.

## Limitations
No closed form is established for the interior area function \(A_p(\rho)\), and no pointwise convergence rate in \(n\) is asserted. The phenomenon concerns initial data drawn from ordinary area measure near the neutral corner and a first-exit event, not the invariant distribution or asymptotic Poincaré recurrence time. Historical priority cannot be guaranteed from the inspected corpus, particularly for work not indexed under coupled intermittent-map escape geometry. No independent external validation has been carried out.

## References
1. M. Sala, C. Manchein, R. Artuso, *Extensive numerical investigations on the ergodic properties of two coupled Pomeau-Manneville maps*, arXiv:1410.4806v1 (2014-10-17); continuous HTML text of v2 (2015), Sections 2.1–2.2 and 3.3. https://arxiv.org/html/1410.4806v2
2. S.-Y. Kim, *Intermittency in coupled maps*, arXiv:chao-dyn/9808002 (1998-08-02), Sections I–III and discussion of saddle-node renormalization. https://arxiv.org/abs/chao-dyn/9808002
3. W. Bahsoun, A. Korepanov, *Statistical aspects of mean field coupled intermittent maps*, arXiv:2303.05311 (2023-03-09), Sections 1–2. https://arxiv.org/abs/2303.05311
4. G. Froyland, R. Murray, O. Stancevic, *Spectral degeneracy and escape dynamics for intermittent maps with a hole*, Nonlinearity 24 (2011), 2435; DOI 10.1088/0951-7715/24/9/003 (abstract-level comparison only).
