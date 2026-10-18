# A sharp two-term small-population extinction-basin law for an exponential ratio-dependent predator–prey flow

## Finding
For the ratio-dependent predator–prey system below, the proportion of a *small square of initial positive densities* that produces extinction of both species is determined, to two orders, by the lower Lambert-root extinction direction and the curvature of its saddle separatrix. This is an exact statement about deterministic initial-condition area, not a stochastic extinction probability for an individual population process.

Write \(P_\varepsilon\) for the area fraction of initial states \((u_0,v_0)\in(0,\varepsilon)^2\) satisfying \(\lim_{t\to\infty}(u(t),v(t))=(0,0)\). For the parameters and quantities defined below,
\[
P_\varepsilon=\begin{cases}
1-\dfrac{z_-}{2}-\dfrac{\kappa}{3}\varepsilon+O(\varepsilon^2),&0<z_-\le 1,\\[6pt]
\dfrac{1}{2z_-}-\dfrac{\kappa}{3z_-^3}\varepsilon+O(\varepsilon^2),&z_->1,
\end{cases}\qquad \kappa<0.
\]
The first correction to extinction risk is therefore strictly positive in both branches. The quantity \(z_-\) is the asymptotic slope of the extinction/prey-rescue basin interface; the correction \(\kappa\) records its exact quadratic bending in physical density coordinates.

## Assumptions and scope
Consider the normalized positive-density flow
\[
\begin{aligned}
\dot u&=u(1-u)-a v e^{-\alpha v/u},\\
\dot v&=v(b e^{-\alpha v/u}-d),
\end{aligned}\qquad u,v>0,
\]
where \(a,b,d,\alpha>0\), \(b<d\), and
\[
z_m=\frac1\alpha-\frac ba>0,\qquad
\frac a\alpha e^{-1+\alpha b/a}>d+1.
\]
These strict assumptions ensure exactly two *positive simple* roots \(0<z_-<z_m<z_+\) of
\[
F(z)=(b+az)e^{-\alpha z}-(d+1)=0.
\]
Equivalently,
\[
z_-=-\frac ba-\frac1\alpha W_0\!\left(-\frac{\alpha(d+1)}a e^{-\alpha b/a}\right),
\]
where \(W_0\) is the real principal Lambert function. Define
\[
q=e^{-\alpha z_-},\quad
\lambda_u=1-a z_-q=bq-d<0,\quad
\lambda_z=z_-q[a-\alpha(b+az_-)]>0,\quad
\kappa=\frac{z_-}{\lambda_u-\lambda_z}<0.
\]
All big-O constants may depend on the fixed model parameters. Statements concern every sufficiently small \(\varepsilon>0\); no assertion is made for arbitrary large initial-state squares, positive delays, stochastic population extinctions, or the nonhyperbolic double-root equality.

## Proof
**1. Global regularity and blow-up.** Positivity follows from each equation having its own density as a factor after writing \(v=uz\). Logistic comparison gives \(0<u(t)\le \max\{1,u_0\}\), and \(v'(t)\le-(d-b)v(t)\), so solutions remain positive and global, with \(v(t)\to0\). Put \(z=v/u\). On \(u,z>0\), without any time rescaling,
\[
\dot u=u\left(1-u-a z e^{-\alpha z}\right),\qquad
\dot z=z\bigl(F(z)+u\bigr).
\tag{1}
\]
The transformation is invertible wherever \(u>0\).

**2. The extinction-direction saddle and its graph.** The function \(F\) increases on \((0,z_m)\) and decreases after \(z_m\); \(F(0)=b-d-1<0\), its maximum is positive by hypothesis, and its limit at infinity is \(-(d+1)\). Thus it has exactly the two stated roots. On \(u=0\), the point \((0,z_-)\) is a saddle of (1), with diagonal eigenvalues \(\lambda_u<0\) and \(\lambda_z>0\) and lower-left Jacobian entry \(z_-\). The point \((0,z_+)\) is a sink because both \(1-az_+e^{-\alpha z_+}=be^{-\alpha z_+}-d\) and \(z_+F'(z_+)\) are negative. The stable-manifold theorem supplies a smooth local saddle stable manifold of the form \(z=s(u)\) for \(0\le u<\eta\), with \(s(0)=z_-\). Substitute \(s(u)=z_-+\kappa u+O(u^2)\) into the invariant-graph equation
\[
s'(u)u\bigl(1-u-a s(u)e^{-\alpha s(u)}\bigr)
=s(u)\bigl(F(s(u))+u\bigr).
\]
The coefficient of \(u\) gives \(\kappa\lambda_u=\kappa\lambda_z+z_-\), proving the stated nonzero \(\kappa\). The sign is strictly negative.

**3. The graph is the entire small-square basin divider.** Choose \(\delta>0\) sufficiently small that \(0<z_--\delta<z_-+\delta<z_++\delta\), \(F(z_-\!-\delta)<0<F(z_-\!+\delta)\), and
\[
a z e^{-\alpha z}>1\quad\text{for }z\in[z_-\!-\delta,z_+\!+\delta].\tag{2}
\]
Such a choice is possible: at both roots \(a z e^{-\alpha z}=1+d-be^{-\alpha z}>1\), and the function \(a z e^{-\alpha z}\) has a single maximum on the intervening interval. Shrink \(\delta\) also so \(F(z_+\!+\delta)<0\). Select a small cap \(\eta>0\) so the vector field at \(z=z_++\delta\) points inward to the strip \([z_-+\delta,z_++\delta]\), and for \(z\in[z_-\!+\delta,z_+\!+\delta]\) the \(u\)-coordinate decreases whenever \(u<\eta\). Hence \((0,\eta)\times[z_-+\delta,z_++\delta]\) is positively invariant; its trajectories have \(u(t)\to0\) and \(z(t)\to z_+\). For the last convergence, use the scalar asymptotically autonomous equation \(\dot z=z(F(z)+u(t))\) on a compact positive \(z\)-interval with the single zero \(z_+\).

Pick \(z_\ell\in(0,z_-\! -\delta)\) so \(b+a z_\ell<d\). For every orbit with \(u_0<1\), logistic comparison gives \(u(t)<1\). Once \(z(t)\le z_\ell\),
\[
\dot z/z\le b+a z-d\le b+a z_\ell-d<0.
\]
Thus \(z(t)\to0\), and the asymptotically logistic prey equation \(\dot u/u=1-u-a z e^{-\alpha z}\) gives \(u(t)\to1\). On the intervening compact intervals \([z_\ell,z_-\! -\delta]\) and \([z_+\!+\delta,Z]\), \(F\) is strictly negative, so for \(u\) below a fixed small cap every orbit moves into the respective prey-rescue or extinction region in a bounded time independent of the starting density. Since \(\dot u\le u\), \(u\) stays small during each bounded passage.

It remains to control *arbitrarily large initial ratios* \(z_0=v_0/u_0\) in a density square. Choose \(Z>z_++\delta\) sufficiently large that \(F(z)+u\le-c\) for \(z\ge Z\) and \(0\le u\le\eta\), where \(c=1+d/2>1\). Before the first crossing \(z=Z\), \(u(t)\le u_0 e^t\) and \(z(t)\le z_0e^{-ct}\). The crossing time is at most \(c^{-1}\log(z_0/Z)\); consequently
\[
u(t)\le u_0(z_0/Z)^{1/c}
=u_0^{1-1/c}v_0^{1/c}Z^{-1/c}\le \varepsilon Z^{-1/c}
\]
for all earlier times when \(0<u_0,v_0<\varepsilon\). This uniform bound closes the cap bootstrap for sufficiently small \(\varepsilon\) and ensures bounded-time entry to the upper invariant strip. It also shows no high-ratio states can escape to the prey-only basin while the square shrinks.

Finally, in the saddle neighborhood \(z\in(z_-\! -\delta,z_-\!+\delta)\) the prey coordinate decreases by (2). The local stable manifold \(z=s(u)\) is the unique boundary: points initially below it leave through \(z=z_-\! -\delta\), enter the prey-rescue region, and approach \((1,0)\); those above leave through \(z=z_-+\delta\) and approach \((0,0)\) through the sink \((0,z_+)\). Points on the graph itself satisfy \(u(t)\to0\), \(z(t)\to z_-\), hence also approach \((0,0)\) in physical coordinates. The preceding compact-interval and high-ratio estimates extend this local saddle partition to *every* point in \((0,\varepsilon)^2\) for one common sufficiently small \(\varepsilon\). Therefore the exact physical divider there is
\[
v_0=u_0s(u_0)=z_-u_0+\kappa u_0^2+O(u_0^3).\tag{3}
\]

**4. Uniform-area extinction law.** The prey-rescue states in the square are exactly those below the graph (3). If \(z_-\le1\), then \(\kappa<0\) ensures \(u s(u)<\varepsilon\) for all \(0<u<\varepsilon\) when \(\varepsilon\) is sufficiently small (including \(z_-=1\)); hence
\[
P_\varepsilon=1-\frac1{\varepsilon^2}\int_0^\varepsilon u s(u)\,du
=1-\frac{z_-}{2}-\frac{\kappa}{3}\varepsilon+O(\varepsilon^2).
\]
If \(z_->1\), let \(u_\varepsilon\) be the unique small positive solution of \(u_\varepsilon s(u_\varepsilon)=\varepsilon\). Taylor expansion gives \(u_\varepsilon=\varepsilon/z_- -\kappa\varepsilon^2/z_-^3+O(\varepsilon^3)\). Extinction occupies only the part above the graph where \(0<u<u_\varepsilon\), so
\[
P_\varepsilon=\frac1{\varepsilon^2}\int_0^{u_\varepsilon}\bigl(\varepsilon-u s(u)\bigr)\,du
=\frac1{2z_-}-\frac{\kappa}{3z_-^3}\varepsilon+O(\varepsilon^2).
\]
This completes the proof. In particular, because the prey-survival sector persists arbitrarily close to the origin, the physical extinction equilibrium is *not Lyapunov stable on the whole first quadrant* (though the blown-up \((0,z_+)\) extinction direction is attracting).

## Verification
The accompanying standard-library script `verify.py` computes \(z_-\), \(z_+\), the saddle eigenvalues, \(\kappa\), and the two extinction-fraction coefficients for both branch regimes, then integrates sample trajectories just above and below (3). Its ODE experiments are finite sanity checks only; the preceding analytic argument establishes the infinite-time and small-square conclusions.

For \((a,b,d,\alpha)=(6,1/2,1,1)\), the primary study's Figure 4 regime, direct root/eigenvalue calculations yield
\[
z_-=0.4281269556316030\ldots,\quad z_+=1.6468255098070288\ldots,\quad
\kappa=-0.2869450114628078\ldots,
\]
\[
P_\varepsilon=0.7859365221841985\ldots+0.0956483371542693\ldots\varepsilon+O(\varepsilon^2).
\]
For \((a,b,d,\alpha)=(3/2,1/2,1,1/5)\), which lies in the \(z_->1\) branch, the coefficients are
\[
z_-=1.4477784382396821\ldots,\quad \kappa=-0.8657447309504778\ldots,\quad
P_\varepsilon=0.3453567112160737\ldots+0.0950960086381595\ldots\varepsilon+O(\varepsilon^2).
\]
The second-order stable-manifold coefficient, though not needed for the theorem, follows from the same invariant equation and is reproduced in the script to facilitate independent numerical convergence checks.

## Relationship to prior work
Blyuss, Kyrychko, and Blyuss (2022) derive this normalized model, the blow-up (1), both Lambert-function extinction directions, and qualitative coexistence of prey-only survival with extinction (their Eq. (4), Eq. (5), and Figure 4). Those findings are *assumed as known background*, not presented as new. The additional contribution here is the local basin-dividing curve's explicit nonzero curvature and a uniform, sharp, two-term area law for *all* initial ratios in a shrinking physical density square, including the large-ratio corner and the change of clipping formula at \(z_-=1\). The earlier time-delay/stochastic paper analyzes the same trophic function with different modeling questions but does not provide this density-square deterministic basin statistic. Related ecological separatrix and extinction-rate studies do not by themselves determine the requested two-term area law for this exponential ratio-dependent flow.

## Limitations
The theorem requires strict simple-root and \(b<d\) hypotheses; it does not treat fold equality, predator invasion \(b\ge d\), stochastic demographic extinction, or arbitrary non-small initial distributions. The uniform initial-square law is a geometric fraction, not an empirical population probability without a specified sampling model. The independent external audit has not been performed.

## References
1. K. B. Blyuss, Y. N. Kyrychko, and O. B. Blyuss (2022), *Complex dynamics near extinction in a predator-prey model with ratio dependence and Holling type III functional response*, Frontiers in Applied Mathematics and Statistics, 8, article 1083815. DOI: 10.3389/fams.2022.1083815. Freely accessible full text: https://arxiv.org/html/2305.04053v1 (first arXiv version 06 May 2023).
2. K. B. Blyuss, S. N. Kyrychko, and Y. N. Kyrychko (2021), *Time-delayed and stochastic effects in a predator-prey model with ratio dependence and Holling type III functional response*, Chaos 31, article 073141. DOI: 10.1063/5.0055623.
