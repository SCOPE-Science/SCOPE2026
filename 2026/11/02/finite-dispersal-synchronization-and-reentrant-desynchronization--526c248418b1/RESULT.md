# Finite-dispersal synchronization and reentrant desynchronization in a heterogeneous two-patch model

## Finding

Consider the stationary fluctuations of two coupled habitat patches,
\[
\begin{aligned}
 dX_t&=\bigl[-aX_t+m(Y_t-X_t)\bigr]dt+s\,dW_t,\\
 dY_t&=\bigl[-bY_t+m(X_t-Y_t)\bigr]dt+t\,dW_t,
\end{aligned}
\]
with \(a,b,s,t>0\), coupling \(m\ge0\), and a **single shared standard Brownian motion** \(W\). Write \(C(m)\) for the stationary Pearson correlation of \(X\) and \(Y\). Then the stationary covariance matrix \(P(m)\) obeys the exact determinant identity
\[
\boxed{\det P(m)=\frac{[(b-a)st+m(t^2-s^2)]^2}{4[ab+(a+b)m](a+b+2m)^2}.}
\]
Thus \(C(m)=1\) if and only if \((b-a)st+m(t^2-s^2)=0\). In particular, **whenever \(a>b>0\) and \(t>s>0\), exact synchronization occurs at exactly one finite positive coupling**,
\[
\boxed{m_*=\frac{(a-b)st}{t^2-s^2}.}
\]
For every other finite coupling the correlation is strictly less than one, yet \(\lim_{m\to\infty}C(m)=1\). Consequently, increasing dispersal past \(m_*\) necessarily destroys perfect synchrony before sufficiently strong dispersal restores asymptotically perfect synchrony.

For the exact choice \((a,b,s,t)=(3,1,1,2)\), the correlation increases strictly on \([0,4/3]\), decreases strictly to one unique minimum at \(m\approx7.4842072232\), and increases strictly thereafter. **The same two-turning-point phenomenon persists under genuinely imperfectly correlated noise.** More precisely, replacing the shared Brownian forcing by two unit Brownian motions with instantaneous correlation \(99/100\), while retaining amplitudes \(1,2\), produces exactly one strict interior correlation maximum (\(m\approx1.426558\)) followed by exactly one strict interior minimum (\(m\approx6.882788\)). Both extrema persist under sufficiently small perturbations of the drift, forcing amplitudes, and noise correlation within the positive-definite forcing domain.

## Assumptions and scope

The variables \(X,Y\) are **centered population deviations** in a continuous-time linearized two-patch model, not nonnegative integer population counts. Rates \(a,b>0\) are uncoupled return-to-equilibrium coefficients; \(m\ge0\) is reciprocal dispersal/coupling strength; \(s,t>0\) are distinct local responses to environmental noise. The first theorem assumes perfectly common white noise. The full-rank example uses Brownian drivers \(W_1,W_2\) satisfying \(d\langle W_1,W_2\rangle_t=(99/100)dt\). All results concern the unique invariant centered Gaussian law, not extinction probabilities or synchrony of a nonlinear ecosystem.

## Proof

**1. Existence and covariance.** Put \(U=(X,Y)^\top\), \(g=(s,t)^\top\), and
\[
A(m)=\begin{pmatrix}a+m&-m\\-m&b+m\end{pmatrix}.
\]
The symmetric matrix \(A(m)\) is positive definite because its leading minor is \(a+m>0\) and its determinant is \(ab+(a+b)m>0\). The stable Ornstein--Uhlenbeck process therefore has a unique invariant Gaussian law and
\[
P=\int_0^\infty e^{-Ar}gg^\top e^{-Ar}\,dr,
\qquad AP+PA=gg^\top.
\]
Writing \(P=\begin{psmallmatrix}p_{11}&p_{12}\\p_{12}&p_{22}\end{psmallmatrix}\), the Lyapunov equations are
\[
2(a+m)p_{11}-2mp_{12}=s^2,\quad
2(b+m)p_{22}-2mp_{12}=t^2,\quad
(a+b+2m)p_{12}-m(p_{11}+p_{22})=st.
\]
Solving and simplifying gives the displayed determinant identity. An independent check in `verify.py` symbolically solves these equations and verifies the identity for symbolic positive \(a,b,s,t\).

**2. Exact-synchrony criterion.** The diagonal variances are strictly positive, and the integral representation has positive entries because \(g\) has positive components and \(e^{-Ar}\) preserves the positive cone. Therefore \(C=p_{12}/\sqrt{p_{11}p_{22}}>0\) and \(C=1\) precisely when \(\det P=0\). The determinant identity makes this exactly \((b-a)st+m(t^2-s^2)=0\). Under \(a>b>0\), \(t>s>0\), its only nonnegative solution is the asserted \(m_*\). Equivalently, the common-noise vector \(g\) is an eigenvector of the drift matrix exactly at this coupling; the entire stationary stochastic response lies on the one-dimensional line spanned by \(g\).

**3. The large-coupling boundary.** For \(m\to\infty\), the antisymmetric mode \(X-Y\) has restoring rate asymptotic to \(2m\) and its variance tends to zero; the symmetric mode remains a nondegenerate OU process with limiting drift \((a+b)/2\) and noise amplitude \((s+t)/2\). Hence both individual variances and their covariance converge to the positive common limit \((s+t)^2/[4(a+b)]\), proving \(C(m)\to1\). Since \(C(m_*)=1\), \(C(m)<1\) for every \(m>m_*\), and the limit is one, a strictly subunit minimum is attained at some finite \(m>m_*\).

**4. Exact two-turning-point example.** At \((a,b,s,t)=(3,1,1,2)\), the Lyapunov solution has common positive denominator \(D(m)=2(4+2m)(3+4m)\) and numerators
\[
Dp_{11}=9m^2+10m+4,\quad
Dp_{22}=9m^2+52m+48,\quad
Dp_{12}=9m^2+29m+12.
\]
Thus \(R(m)=C(m)^2\) is
\[
R(m)=\frac{(9m^2+29m+12)^2}{(9m^2+10m+4)(9m^2+52m+48)}.
\]
An exact derivative factorization is
\[
R'(m)=\frac{2(3m-4)(9m^2+29m+12)F(m)}{(9m^2+10m+4)^2(9m^2+52m+48)^2},
\quad F(m)=54m^3-309m^2-664m-360.
\]
Descartes' sign rule gives exactly one possible positive zero of \(F\). Since \(F(0)<0\), \(F(m)\to+\infty\), and \(F(4/3)=-5000/3<0\), it has exactly one positive zero, lying strictly beyond \(4/3\). The sign pattern of \(R'\) is therefore positive, negative, positive on the successive intervals. Since \(C>0\), the same sign pattern holds for \(C'\). In particular \(C(0)=\sqrt3/2\), \(C(4/3)=1\), and \(C\) has precisely one later strict minimum.

**5. Full-rank robustness witness.** Keep \(a=3,b=1\) and noise amplitudes \(1,2\), but use the strictly positive-definite instantaneous covariance
\[
Q=\begin{pmatrix}1&99/50\\99/50&4\end{pmatrix},\qquad\det Q=199/2500>0.
\]
Now the Lyapunov equation is \(AP+PA=Q\), and the exact squared correlation becomes
\[
R_{99/100}(m)=\frac{(224m^2+721m+297)^2}{(224m^2+249m+100)(224m^2+1297m+1200)}.
\]
Its derivative is a strictly positive rational factor times
\[
G(m)=2609152m^4-17076864m^3-10302432m^2+25830809m+22887750.
\]
The descending coefficient signs are \(+,-,-,+,+\), allowing at most two positive roots by Descartes' rule. Yet \(G(1)>0>G(2)\) and \(G(6)<0<G(8)\), so there are exactly two positive roots, one in each indicated disjoint interval. Both are simple sign-changing roots (there cannot be further positive roots counted with multiplicity), giving exactly one maximum followed by one minimum. Their nondegeneracy and continuous dependence of the derivative on parameters give persistence by the implicit-function theorem for a nonempty open set of positive-definite forcing covariances.

## Verification

Run `python verify.py` with SymPy, NumPy, and SciPy. It checks the symbolic Lyapunov solution, determinant identity, the unique perfect-correlation point and covariance values, both exact derivative factorizations, the requisite sign and root-count tests, and independent double-precision Lyapunov solves at selected coupling values. No simulation is used as a substitute for the analytic sign and root-count proofs.

## Relationship to prior work

Spatial synchrony driven by dispersal and correlated environmental fluctuations is classical. Kendall et al. (2000) derive covariances and monotonic correlation behavior in a *homogeneous discrete-time two-patch model*, with equal local regulation and environmental variances. Liebhold, Johnson and Bjørnstad (2006) demonstrate how geographical heterogeneity alters synchrony and study heterogeneous *discrete-time second-order* dynamics largely by simulation. Their full text did not identify the continuous-time perfect-synchrony coupling criterion or the full-rank two-turning-point example above. Ripa (2000) studies linearized synchrony and dispersal; the accessible abstract does not settle the present heterogeneous forcing comparison. Coupled OU variance regulation has also been studied by Ly and Ermentrout (2010), although only the abstract was accessible here. The Lyapunov/Gramian tools and rank-one eigenvector criterion are standard linear-systems mathematics; the proposed contribution is their ecologically motivated sharp tuning rule and its robust, exact nonmonotone Pearson-correlation consequence in a heterogeneous two-patch setting. An unlocated broader theorem may imply the specialization, so publication priority is not independently certified.

## Limitations

This is a stationary linear Gaussian result and does not imply exact trajectory equality from arbitrary initial conditions, persistence, or extinction reduction. Real populations have nonlinear and nonnegative state constraints. For independently varying environmental components with correlation strictly below one, perfect stationary correlation is impossible, although the two turning points survive for explicitly exhibited full-rank forcing. In the general parameter family, existence but not uniqueness of the post-synchronization minimum is proved; uniqueness is asserted only for the two exact examples. The first-public-source date relates to the cited 2006 motivating study and does not assert a publication date for this new theorem.

## References

1. A. M. Liebhold, D. M. Johnson, O. N. Bjørnstad (2006). *Geographic variation in density-dependent dynamics impacts the synchronizing effect of dispersal and regional stochasticity*. Population Ecology 48, 131–138. DOI: 10.1007/s10144-005-0248-6. First online publication 2006-01-26.
2. B. E. Kendall, O. N. Bjørnstad, J. Bascompte, T. H. Keitt, W. F. Fagan (2000). *Dispersal, environmental correlation, and spatial synchrony in population dynamics*. The American Naturalist 155, 628–636. DOI: 10.1086/303350.
3. J. Ripa (2000). *Analysing the Moran effect and dispersal: their significance and interaction in synchronous population dynamics*. Oikos 89, 175–187. DOI: 10.1034/j.1600-0706.2000.890119.x.
4. C. Ly, G. B. Ermentrout (2010). *Coupling regularizes individual units in noisy populations*. Physical Review E 81, 011911. DOI: 10.1103/PhysRevE.81.011911.
