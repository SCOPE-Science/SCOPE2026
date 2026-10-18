# Critical log–log optimization of stationary confinement in boundary-tumbling active motion

## Finding
Consider a one-dimensional particle with thermal diffusivity \(D>0\) and internal velocity \(\pm v\), \(v>0\), in a reflecting interval of length \(L>0\). The velocity switches only at the wall it points toward, with the boundary reaction convention specified below. Denote the position under its unique stationary law by \(X\). Set
\[
p=\frac{vL}{D},\qquad \beta=\frac{v^2}{D\alpha},\qquad V_\beta(p)=\frac{\operatorname{Var}(X)}{L^2}.
\]
The positive parameters \(p,\beta\) are independent dimensionless controls. In particular, fixing \(v,D,\alpha\) and varying \(L\) varies \(p\) at fixed \(\beta\). The stationary variance obeys the exact identity
\[
V_\beta(p)=\frac1{12}+\frac{\beta-1+e^{-p}}{p+\beta-1+e^{-p}}B(p),\qquad
B(p)=\frac16+\frac2{p^2}-\frac{\coth(p/2)}p,\qquad 0<B(p)<\frac16.
\]
This yields a sharp stationary-confinement threshold: for \(\beta\ge1\), \(V_\beta(p)>1/12\) at every finite \(p>0\), with infimum \(1/12\) not attained; for \(0<\beta<1\), there is at least one finite global minimizer \(p_\beta\) and \(V_\beta(p_\beta)<1/12\). Every such minimizer obeys \(p_\beta>\log(1/(1-\beta))\).

More sharply, put \(\delta=1-\beta\) and \(H=\log(1/\delta)\). As \(\delta\downarrow0\), **every** global minimizer satisfies
\[
\boxed{p_\beta=H+\log H+\frac{\log H+7}{H}
+O\!\left(\frac{(\log H)^2}{H^2}\right)}
\]
and the optimal variance improvement below a uniform distribution is
\[
\boxed{\frac1{12}-\min_{p>0}V_\beta(p)
=\frac{\delta}{6H}\left[1-\frac{\log H+7}{H}
+O\!\left(\frac{(\log H)^2}{H^2}\right)\right].}
\]
The asymptotics and remainders apply to all minimizers without assuming global uniqueness at finite \(\beta\).

## Assumptions and scope
In the bulk \(0<x<L\), the right-moving and left-moving stationary densities \(\rho_+(x),\rho_-(x)\) solve
\[
D\rho_+''-v\rho_+'=0,\qquad D\rho_-''+v\rho_-'=0.
\]
There are no bulk tumbles. At the right wall the \(+\) state converts to \(-\), and at the left wall the \(-\) state converts to \(+\). The local boundary reaction coefficient is
\[
\kappa=\frac{D\alpha}{v}(1-e^{-p})>0.
\]
This is the boundary-local-time normalization of Roberts and Pruessner (2022), in which \(\alpha\) has the interpretation of an effective wall tumble rate. The stationary currents satisfy \(J_+=v\rho_+-D\rho_+'=\kappa\rho_+(L)\) and \(-J_-=\kappa\rho_-(0)\), with opposite currents of the same magnitude. All assertions concern the unique normalized stationary solution of this precise model. The objective is the variance relative to the square of the interval length, not the unnormalized variance, and the optimization fixes \(\beta\) while varying \(p>0\).

## Proof
**1. Reconstructing the stationary law.** By reflection symmetry and the two bulk equations, a normalized stationary pair must have the form
\[
\rho_+(x)=\frac{1-c}{2L}\frac{p e^{px/L}}{e^p-1}+\frac{c}{2L},
\qquad \rho_-(x)=\rho_+(L-x).
\]
Both states then have mass \(1/2\), and their bulk probability currents are \(J_+=vc/(2L)=-J_-\). At the right wall, the condition \(J_+=\kappa\rho_+(L)\) reads
\[
vc=\kappa\left[(1-c)\frac{p}{1-e^{-p}}+c\right].
\]
Substitute \(\kappa/v=(1-e^{-p})/\beta\), solve for \(c\), and obtain
\[
c=C_\beta(p)=\frac{p}{p+\beta-1+e^{-p}}.
\]
The denominator is positive for all \(p,\beta>0\), since \(p-1+e^{-p}>0\). Reflection supplies the left wall condition. The resulting density is
\[
\rho(x)=\rho_+(x)+\rho_-(x)
=\frac{1-c}{L}\frac{p\cosh(p(x/L-1/2))}{2\sinh(p/2)}+\frac cL.
\]
Its symmetry gives \(\mathbb E X=L/2\). The preceding construction also independently checks the stationary density and boundary flux used in the source analysis.

**2. Exact variance and positivity.** Write \(y=x/L-1/2\), and let
\[
w_p(y)=\frac{p\cosh(py)}{2\sinh(p/2)},\qquad -\frac12\le y\le\frac12.
\]
Direct integration yields
\[
\int_{-1/2}^{1/2}y^2w_p(y)\,dy
=\frac14+\frac2{p^2}-\frac{\coth(p/2)}p.
\]
The uniform variance on this centered interval is \(1/12\); hence its excess for \(w_p\) is exactly \(B(p)\). It is strictly positive because \(y^2\) and \(\cosh(py)\) are strictly positively correlated when \(y\) is uniform on the interval: both increase with \(|y|\). It is strictly less than \(1/6\), because \(y^2<1/4\) almost surely under \(w_p\). Integrating the displayed stationary mixture gives \(V_\beta(p)=1/12+(1-c)B(p)\), proving the formula in the finding.

**3. Global confinement threshold.** Put \(\delta=1-\beta\). Because \(B(p)>0\), the sign of \(V_\beta(p)-1/12\) is the sign of \(e^{-p}-\delta\). For \(\beta\ge1\), it is positive at all \(p>0\), while \(V_\beta(p)\to1/12\) as \(p\downarrow0\) and as \(p\to\infty\). For \(0<\beta<1\), let \(H=\log(1/\delta)\) and define the variance gain
\[
W_\delta(p)=\frac1{12}-V_\beta(p)
=\frac{(\delta-e^{-p})B(p)}{p-\delta+e^{-p}}.
\]
It is strictly positive precisely when \(p>H\), vanishes at \(p=H\), and tends to zero at infinity. Its maximum is therefore attained at an interior point \(p_\beta>H\), and the minimum of \(V_\beta\) is strictly below \(1/12\).

**4. Pinning the global optimizer to the critical scale.** For \(\delta\downarrow0\), take the admissible comparison point \(p_0=H+\log H\). The identity
\[
B(p)=\frac16-\frac1p+\frac2{p^2}+O(e^{-p}/p)
\]
gives \(W_\delta(p_0)=\delta(1+o(1))/(6H)\). For every fixed \(\varepsilon>0\), all \(p\ge(1+\varepsilon)H\) satisfy
\[
0<W_\delta(p)<\frac{\delta}{6(p-\delta)}
\le\frac{\delta}{6((1+\varepsilon)H-\delta)},
\]
which is smaller than the comparison value for small enough \(\delta\). Since every optimizer is also larger than \(H\), this proves \(p_\beta/H\to1\) for every choice of global minimizer.

**5. Critical equation and log–log asymptotic.** Write \(u=e^{-p_\beta}\). Differentiating \(\log W_\delta\) at an interior maximizer yields the exact stationarity equation
\[
\frac{u}{\delta-u}=\frac{1-u}{p_\beta-\delta+u}-\frac{B'(p_\beta)}{B(p_\beta)}.
\]
As \(p\to\infty\), differentiation of the elementary expression for \(B\) yields
\[
\frac{B'(p)}{B(p)}=\frac6{p^2}+O(p^{-3}).
\]
Since \(p_\beta/H\to1\) and \(0<u<\delta=e^{-H}\), the critical equation becomes
\[
\frac{u}{\delta-u}=\frac1{p_\beta}-\frac6{p_\beta^2}+O(p_\beta^{-3}),
\qquad
\frac{u}{\delta}=\frac1{p_\beta}-\frac7{p_\beta^2}+O(p_\beta^{-3}).
\]
Taking logarithms of \(u=e^{-p_\beta}\) therefore gives
\[
p_\beta=H+\log p_\beta+\frac7{p_\beta}+O(p_\beta^{-2}).
\]
First this implies \(p_\beta=H+\log H+O(\log H/H)\); inserting that estimate once more yields
\[
p_\beta=H+\log H+\frac{\log H+7}{H}
+O((\log H)^2/H^2).
\]
All estimates hold uniformly for any global optimizer, since the scale pinning and stationarity arguments did not select an optimizer.

**6. Optimal gain.** Substitution of the stationary relation \(u/\delta=1/p_\beta-7/p_\beta^2+O(p_\beta^{-3})\) into the exact gain shows
\[
W_\delta(p_\beta)=\frac{\delta}{6p_\beta}
\left[1-\frac7{p_\beta}+O(p_\beta^{-2})\right].
\]
The expansion of \(p_\beta\) from step 5 proves the claimed gain formula with a remainder of order \(\delta(\log H)^2/H^3\). No finite-parameter uniqueness theorem is needed.

## Verification
The accompanying standalone `CHECKER.py` uses Python standard-library quadrature, differentiations and bounded optimization to check the normalized density, flux balance, independent second-moment integral, sign transition, critical equation and asymptotic scalings. Execute `python3 CHECKER.py` from the directory containing the checker. The completed package's checker produced `PASS 653 independent scalar checks`. These finite computations are supplementary; the global and asymptotic claims follow from the analytic argument above.

## Relationship to prior work
Roberts and Pruessner (2022), arXiv:2206.06105, derive the precise boundary-tumbling model, its exact stationary density (their equations (33), (35), (36)), and the stationary variance (their equation (38)); they numerically report an optimal Péclet value near \(5.54\) in the instantaneous-boundary-reaction limit. Their full stationary formula is a premise here and is not new. The present result analyzes a different, physically dimensionless, fixed-\(\beta\) optimization and proves a singular critical transition, a diverging optimal Péclet scale with a \(\log\log\) correction, and the vanishing optimal confinement gain with its explicit next-order coefficient.

Pietrangeli et al. (2024), arXiv:2404.07680, optimize diffusion *parallel* to confining walls in a slit model with wall sojourns; this is a different observable and dynamics. Dolai and Das (2025), arXiv:2412.20287, study boundary-reservoir-driven active particles with bulk tumbling and transport; their boundary conditions and quantities differ. Fu et al. (2023), arXiv:2401.03161, analyze two-dimensional population-level boundary aggregation and a kinetic-to-Fokker–Planck limit, not this single-particle normalized-variance optimization. The claim is not a new stationary solution or a general assertion about arbitrary active particles.

## Limitations
No uniqueness is claimed for the global minimizer at a fixed \(0<\beta<1\); all global minimizers nonetheless share the stated critical expansion. The limit \(\beta\uparrow1\) is a joint parameter regime. The objective is \(\operatorname{Var}(X)/L^2\), so the critical law should not be substituted into an optimization of the *unnormalized* variance. The wall-reaction normalization \(\kappa=\alpha D(1-e^{-p})/v\) matters. The result does not cover bulk tumbling, asymmetric boundary rates, interacting particles, or other wall conventions. An equivalent earlier analysis of this singular regime may exist beyond the literature considered here.

## References
1. C. Roberts and G. Pruessner, “Exact solution of a boundary tumbling particle system in one dimension,” *Physical Review Research* **4**, 033234 (2022), arXiv:2206.06105, https://arxiv.org/abs/2206.06105, first public June 13, 2022.
2. T. Pietrangeli, C. Ybert, C. Cottin-Bizonne and F. Detcheverry, “Optimal run-and-tumble in slit-like confinement,” *Physical Review Research* **6**, 023028 (2024), arXiv:2404.07680, https://arxiv.org/abs/2404.07680.
3. P. Dolai and A. Das, “Boundary layers, transport and universal distribution in boundary driven active systems,” *SciPost Physics* **19**, 088 (2025), arXiv:2412.20287, https://arxiv.org/abs/2412.20287.
4. J. Fu, J. Liang, B. Perthame, M. Tang and C. Zhong, “Confined run-and-tumble model with boundary aggregation: Long-time behavior and convergence to the confined Fokker–Planck model,” *Mathematical Models and Methods in Applied Sciences* **33**, 2743–2783 (2023); arXiv:2401.03161, https://arxiv.org/abs/2401.03161.
