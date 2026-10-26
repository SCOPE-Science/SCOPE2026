# A sharp cooperation threshold for predator rescue despite failed invasion

## Finding

In the continuous-time fear-and-harvesting predator–prey model below, suppose the predator cannot invade the predator-free prey equilibrium, but could in principle persist at a positive density. Define the predator nullcline parameter \(B=\mu/(\delta-\mu h)\). Under \(0<c<1\), \(h,\beta,\mu>0\), \(\delta>\mu h\), and \(B>1-c\), there is a unique critical positive hunting-cooperation strength \(\alpha_*\) with the following **complete positive-equilibrium count**:

* \(0<\alpha<\alpha_*\): no positive coexistence equilibrium;
* \(\alpha=\alpha_*\): one positive equilibrium, with exactly double multiplicity in the equilibrium equation;
* \(\alpha>\alpha_*\): exactly two distinct simple positive equilibria.

The lower-predator-density equilibrium is always a hyperbolic saddle. The upper-predator-density equilibrium has positive Jacobian determinant, but need not be stable for arbitrary parameters. An exact, strictly positive parameter witness demonstrates that the upper coexistence equilibrium and the predator-free equilibrium can both be hyperbolic sinks, while the lower coexistence equilibrium is a hyperbolic saddle. Thus sufficiently strong cooperative hunting can permit **robust coexistence–predator-extinction bistability without invasion from rarity**.

The critical parameter is specified *exactly* by the one-dimensional optimization formula in the proof; it is not inferred from numerically tracing equilibrium branches.

## Assumptions and scope

Let \(u(t)\ge0\) denote prey density, \(v(t)\ge0\) predator density, and consider

\[
\begin{aligned}
\dot u&=u\left[\frac{1-u}{1+\beta v}-\frac{(1+\alpha v)v}{1+h(1+\alpha v)u}-c\right],\\
\dot v&=v\left[\frac{\delta(1+\alpha v)u}{1+h(1+\alpha v)u}-\mu\right].
\end{aligned}
\]

All of \(\alpha,\beta,h,\delta,\mu\) are positive; \(c\in(0,1)\) is proportional prey harvesting, and \(\mu=m+c_2\) is positive aggregate predator mortality and proportional harvesting. Throughout the theorem \(\delta>\mu h\) and
\[
B=\frac{\mu}{\delta-\mu h}>1-c.
\]
These assumptions make the predator-free equilibrium \(E_0=(1-c,0)\) a strict sink. No claim of global attraction, cycle absence, uniqueness of basin boundary, or finite-population stochastic persistence is made.

For an explicit example take
\[
(\alpha,\beta,h,c,m,c_2,\delta)=
\left(10,1,\frac1{10},\frac1{10},\frac1{200},\frac1{200},\frac{11}{1000}\right).
\]
Then \(\mu=1/100\) and \(B=1\).

## Proof

**1. Eliminate the predator nullcline.** At a strictly positive equilibrium the predator equation implies
\[
(1+\alpha v)u=B,\qquad u(v)=\frac{B}{1+\alpha v}.
\]
Conversely any positive root of the prey per-capita growth rate after this substitution gives a strictly positive equilibrium. Define
\[
F_\alpha(v)=\frac{1-B/(1+\alpha v)}{1+\beta v}-c-\frac{v(1+\alpha v)}{1+hB}.
\]
Clearing the positive denominator gives the quartic \(Q_\alpha(v)=(1+hB)(1+\alpha v)(1+\beta v)F_\alpha(v)\), namely
\[
\begin{aligned}
Q_\alpha(v)={}&-(1+hB)(B+c-1)\\
&+\big[(1+hB)(\alpha(1-c)-c\beta)-1\big]v\\
&-\big[c(1+hB)\alpha\beta+2\alpha+\beta\big]v^2\\
&-\alpha(\alpha+2\beta)v^3-\alpha^2\beta v^4.
\end{aligned}
\]
Its constant coefficient and coefficients of degrees \(2,3,4\) are strictly negative. The linear coefficient is unrestricted. Descartes' rule of signs, with multiplicities, therefore allows **at most two positive roots**, including multiple roots.

**2. Locate one sharp onset of two roots.** Put \(z=\alpha v\), \(t=1/\alpha\), and \(U(z)=1-B/(1+z)\). The inequality \(F_\alpha(z/\alpha)>0\) is equivalent to
\[
U(z)-c-tL(z)-t^2 M(z)>0,
\]
where
\[
L(z)=c\beta z+\frac{z(1+z)}{1+hB},\qquad
M(z)=\frac{\beta z^2(1+z)}{1+hB}.
\]
For \(z\le z_0=B/(1-c)-1>0\), one has \(U(z)\le c\), so positivity is impossible. For each \(z>z_0\), put \(A(z)=U(z)-c>0\). The displayed quadratic inequality holds precisely for \(0<t<t_*(z)\), where
\[
t_*(z)=\frac{2A(z)}{L(z)+\sqrt{L(z)^2+4M(z)A(z)}}>0.
\]
The continuous function \(t_*\) tends to zero as \(z\downarrow z_0\) and as \(z\to\infty\), since \(t_*(z)\le A(z)/L(z)\) and \(L(z)\) grows quadratically. Hence
\[
\boxed{\displaystyle \alpha_*=\left(\max_{z>z_0}t_*(z)\right)^{-1}\in(0,\infty)}.
\]
For \(\alpha<\alpha_*\), the function \(F_\alpha\) is strictly negative on \((0,\infty)\) (including its endpoint limits), so there are no positive roots. At equality its global maximum is zero and it has at least one positive zero of even multiplicity; the Descartes bound makes that root exactly double and unique. If \(\alpha>\alpha_*\), then \(F_\alpha\) is positive somewhere while \(F_\alpha(0)=1-B-c<0\) and \(F_\alpha(v)\to-\infty\) as \(v\to\infty\). It has two distinct sign-changing roots; the Descartes bound makes them simple and excludes all further roots. In particular, the critical zero is a nondegenerate tangency in the scalar equilibrium equation; a dynamical saddle-node normal form at every parameter point is not asserted.

**3. Stability orientation.** Write \(\dot u=u f(u,v)\), \(\dot v=v g(u,v)\) and observe \(g_u>0\). At a positive equilibrium \(u=u(v)\), differentiating \(g(u(v),v)=0\) and using \(f(u(v),v)=F_\alpha(v)\) yields the exact Jacobian identity
\[
\det J=-uv\,g_u\,F_\alpha'(v).
\]
At the smaller simple root \(F_\alpha'\!>0\), hence \(\det J<0\): a hyperbolic saddle. At the larger root \(F_\alpha'\!<0\), so \(\det J>0\); its trace determines attraction or repulsion. The predator-free point has prey eigenvalue \(-(1-c)<0\) and predator eigenvalue \(\delta(1-c)/(1+h(1-c))-\mu<0\), with the latter strict inequality equivalent to \(B>1-c\).

**4. An exact sink–saddle–sink example.** For the stated rational parameters,
\[
Q_{10}(v)=-\frac{10000v^4+12000v^3+2210v^2-879v+11}{100}.
\]
Exact substitutions yield
\[
\begin{array}{c|cccc}
v&1/100&1/50&1/6&1/5\\ \hline
\operatorname{sgn}Q_{10}(v)&-&+&+&-
\end{array}
\]
so the two positive simple roots satisfy \(1/100<v_-<1/50\) and \(1/6<v_+<1/5\). Their prey coordinates are \(u_\pm=1/(1+10v_\pm)>0\). The lower point is a saddle by step 3. Along this nullcline, the Jacobian trace is exactly
\[
\operatorname{tr}J(v)=-\frac{100000v^4+120000v^3+22100v^2-9879v+1331}{1210(1+v)(1+10v)}.
\]
For \(1/6<v<1/5\), the numerator exceeds
\[
\frac{120000}{216}+\frac{22100}{36}+1331-\frac{9879}{5}>0.
\]
Consequently the upper coexistence point has \(\operatorname{tr}J<0\), \(\det J>0\) and is a hyperbolic sink. The predator-free equilibrium is another hyperbolic sink by step 3. Each sink attracts an open set of biologically admissible initial conditions; these open coexistence/extinction basins persist after sufficiently small changes in all model parameters. This proves the advertised local bistability and robustness.

## Verification

Run `python verify.py` with Python 3 and SymPy installed. The standalone script checks the nullcline elimination and quartic coefficient identity symbolically, verifies the determinant identity by the chain-rule derivation stated above, checks all four rational root-isolation signs, verifies the exact trace formula, proves its rational lower bound is positive, and checks both predator-free eigenvalues. There is no numerical sampling in the proof of the universal statements. Decimal root approximations are unnecessary to certify either equilibrium count or stability.

## Relationship to prior work

Belew and Melese (2022, DOI `10.1155/2022/2776698`) introduce and study this fear/cooperation/harvesting vector field. Their Section 3.4 treats a positive equilibrium through a one-root sign regime, with local stability and Hopf analysis in subsequent sections. The present theorem addresses the **other biologically feasible regime in which the predator-free equilibrium is strictly stable**; its global-in-\(\alpha\) two-root onset and exact sink–saddle–sink witness do not follow from their stated one-root condition. No general global stability assertion from that paper is contradicted or imported here.

Du, Niu, and Wei (2021/2022, DOI `10.3934/dcdsb.2021298`) analyze saddle-node and richer bifurcations in a *different*, nondifferentiable group-defense functional response. Jang and Yousef (2023, DOI `10.1080/17513758.2023.2242372`) exhibit cooperative-hunting-induced two-positive-equilibrium behavior in a *discrete-time prey-refuge model*. These works establish the general ecological importance of cooperation-induced strong Allee thresholds; they neither state the exact quartic and critical-cooperation formula of the present continuous-time fear-and-harvesting system nor imply it by an identified parameter substitution.

## Limitations

The sharp threshold concerns equilibrium number under \(B>1-c\), \(0<c<1\), and strictly positive model parameters. It does not classify the upper equilibrium's stability for every parameter tuple, prove global basins, prohibit periodic orbits, or provide stochastic extinction probabilities. The scalar algebraic double root at \(\alpha_*\) is not claimed to be a nondegenerate planar saddle-node without checking the remaining eigenvalue. Publication-priority risk remains from other unexamined treatments of the same vector field; the Du–Niu–Wei full text was inaccessible and the Jang–Yousef text was available only through indexed excerpts including its model equations and conclusions.

## References

1. B. Belew and D. Melese, *Modeling and Analysis of Predator-Prey Model with Fear Effect in Prey and Hunting Cooperation among Predators and Harvesting*, Journal of Applied Mathematics (2022), article 2776698; DOI: `10.1155/2022/2776698`. Public date December 3, 2022.
2. Y. Du, B. Niu, and J. Wei, *A predator-prey model with cooperative hunting in the predator and group defense in the prey*, Discrete and Continuous Dynamical Systems B 27 (2022), 5845–5881; DOI: `10.3934/dcdsb.2021298` (early access December 20, 2021).
3. S. R.-J. Jang and A. M. Yousef, *Effects of prey refuge and predator cooperation on a predator–prey system*, Journal of Biological Dynamics 17 (2023), 2242372; DOI: `10.1080/17513758.2023.2242372` (online August 3, 2023).
