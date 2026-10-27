# Unique weak-reset threshold for projective qubit diffusion and its two geometric limits

## Finding

Let \(X_t=|\langle\psi_t,\eta\rangle|^2\) be target fidelity for isotropic Brownian diffusion of pure qubit states on the complex projective line, with generator \(\mathcal Lf=c[x(1-x)f''+(1-2x)f']\) for \(c>0\). Fix a target fidelity \(0<b<1\), initial fidelity \(0\le x<b\), and the completion time \(T_b=\inf\{t\ge0:X_t\ge b\}\). Independently reset the process to that same initial pure state at Poisson rate \(r\ge0\), and write \(M_{x,b,c}(r)\) for its mean completion time.

Define \(\delta=1-b\), \(y=1-x\), and the real dilogarithm \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\). Put
\[
\Phi_b(y)=\operatorname{Li}_2(b)-\operatorname{Li}_2(1-y)
-(1+\log y)\log\frac{y}{1-b},\qquad 1-b<y\le1.
\]
Then the exact right derivative at zero reset rate is
\[
M_{x,b,c}'(0+)=-\frac{\Phi_b(1-x)}{c^2}.
\]
For every \(b\in(0,1)\), there exists a **unique** critical initial fidelity \(x_c(b)\in(0,b)\) such that
\[
\begin{cases}
M_{x,b,c}'(0+)>0,&0\le x<x_c(b),\\
M_{x,b,c}'(0+)=0,&x=x_c(b),\\
M_{x,b,c}'(0+)<0,&x_c(b)<x<b.
\end{cases}
\]
The threshold is independent of the diffusion timescale \(c\) and has two sharp endpoint laws:
\[
x_c(b)=\frac b3+\frac{14}{243}b^2+O(b^3)\quad(b\downarrow0),
\]
\[
x_c(1-\delta)=1-e^{-1}-\frac{\pi^2/6-\operatorname{Li}_2(1-e^{-1})}{e\log(1/\delta)}
+O\!\left(\frac1{\log^2(1/\delta)}\right)\quad(\delta\downarrow0).
\]
Thus for any fixed \(x\ne x_c(b)\), every sufficiently small positive reset rate respectively slows or speeds completion as indicated. No claim about positive-rate global optimality is made at the equality boundary.

## Assumptions and scope

The process is isotropic Fubini–Study Brownian motion on \(\mathbb{CP}^1\), equivalently rotational Brownian motion on the Bloch sphere, with the radial generator specified above. The target is the spherical cap of fidelity at least \(b\). All parameters satisfy \(c>0\), \(0<b<1\), \(0\le x<b\); complete Poisson resetting restores the original state and is independent of the Brownian path. Reaching the cap, not an exact zero-measure pure state, ends the process. The endpoint \(x=0\) is an entrance boundary of the fidelity diffusion; the explicit regular solution is selected there. \(x=b\) is excluded since the completion time then vanishes.

## Proof

**Moment boundary equations.** Let \(m(x)=\mathbb E_x[T_b]\), \(q(x)=\mathbb E_x[T_b^2]\), \(v=q-m^2\). The generator boundary problems \(\mathcal Lm=-1\), \(\mathcal Lq=-2m\) on \(0\le x<b\), together with \(m(b)=q(b)=0\) and regularity at \(0\), give
\[
m(x)=\frac{\log[(1-x)/(1-b)]}{c},
\]
\[
v(x)=\frac{\log^2(1-b)-\log^2(1-x)
+2[\operatorname{Li}_2(b)-\operatorname{Li}_2(x)]
+2\log[(1-b)/(1-x)]}{c^2}.
\]
These are directly checked by differentiating twice, applying \(\mathcal L\), and enforcing boundary conditions. Equivalently the positive Laplace transform of \(T_b\) is \(F_r(x)/F_r(b)\), where
\[
F_r(z)={}_2F_1\left(\frac{1-\sqrt{1-4r/c}}2,
\frac{1+\sqrt{1-4r/c}}2;1;z\right).
\]
The diffusion is compact with an absorbing nonempty cap, so first-passage moments required below are finite. When \(r\) is near zero, the transform is analytic.

**Poisson renewal.** Set \(\varphi(r)=\mathbb E_x[e^{-rT_b}]\). The independent restart-cycle identity yields
\[
M_{x,b,c}(r)=\frac{1-\varphi(r)}{r\varphi(r)}\quad(r>0),\qquad
M_{x,b,c}(0)=m(x).
\]
Taylor expansion at zero gives \(M'(0+)=[m(x)^2-v(x)]/2\). Substituting the two displayed moments and simplifying proves \(M'(0+)=-\Phi_b(1-x)/c^2\).

**Single interior transition.** Fix \(0<b<1\) and set \(\delta=1-b\). We have \(\Phi_b(\delta)=0\) and
\[
\Phi_b(1)=\operatorname{Li}_2(b)+\log(1-b)<0,
\]
where the strict inequality follows termwise from \(\operatorname{Li}_2(b)=\sum_{n\ge1}b^n/n^2\) and \(-\log(1-b)=\sum_{n\ge1}b^n/n\). Differentiating yields
\[
\Phi_b'(y)=\frac{A(y)-\log(y/\delta)}y,
\quad A(y)=-\frac{\log y}{1-y}-1,
\quad A'(y)=-\frac{1-y+y\log y}{y(1-y)^2}<0
\]
for \(\delta<y<1\); indeed \(1-y+y\log y>0\) for \(0<y<1\). Also \(A(y)>0\), while \(\log(y/\delta)\) increases strictly from \(0\). Therefore \(\Phi_b'\) changes sign exactly once, from positive to negative. Since \(\Phi_b\) first increases from \(0\) and ends negative, it crosses zero at precisely one \(y_c\in(\delta,1)\). Put \(x_c=1-y_c\). For \(0\le x<x_c\), \(\Phi_b(1-x)<0\); for \(x_c<x<b\), it is positive. The derivative signs follow. Strict signs imply the corresponding improvement/worsening for sufficiently small positive \(r\).

**Low-fidelity threshold.** In the regime \(b\downarrow0\), substitute \(x=zb\) in \(\Phi_b(1-x)\). Taylor expansion uniformly for \(z\) near \(1/3\) gives
\[
\Phi_b(1-zb)=\frac{b^2}{4}(1-z)(3z-1)
-\frac{b^3}{18}(z-1)(14z^2+5z-4)+O(b^4).
\]
The leading factor has a simple interior root at \(z=1/3\). The implicit-function theorem gives \(z=1/3+(14/243)b+O(b^2)\), establishing the stated \(b\downarrow0\) expansion. Geometrically this limit magnifies the small neighborhood of the state antipodal to the target into a flat two-dimensional disk, explaining the leading fraction \(1/3\).

**High-fidelity target.** As \(\delta=1-b\downarrow0\), write \(L=\log(1/\delta)\). The root equation is
\[
(1+\log y_c)(L+\log y_c)=
\operatorname{Li}_2(1-\delta)-\operatorname{Li}_2(1-y_c).
\]
Its unique root lies above \(e^{-1}\) for small \(\delta\) and converges to \(e^{-1}\): the right-hand side remains bounded, while \(L\to\infty\). Expanding at \(y_0=e^{-1}\) and using \(\operatorname{Li}_2(1-\delta)=\pi^2/6+O(\delta|\log\delta|)\) yields
\[
y_c=e^{-1}+\frac{\pi^2/6-\operatorname{Li}_2(1-e^{-1})}{eL}+O(L^{-2}).
\]
Subtracting from \(1\) proves the high-fidelity expansion. The positive coefficient ensures approach to \(1-e^{-1}\) from below.

## Verification

Run `python CHECK.py` with Python 3 and the `mpmath` package. The self-contained diagnostics reproduce the backward generator equations, differentiate the hypergeometric Laplace transform for first and second moments, verify root signs and threshold equations, and check both limiting expansions. The program returned `PASS 178 analytical/numerical identities and threshold diagnostics`. It also prints critical fidelities \(0.0339408277074088552\) for \(b=0.1\), \(0.186569338443218592\) for \(b=0.5\), \(0.410324066822562249\) for \(b=0.9\), and \(0.588435347020043672\) for \(b=0.9999\). These finite checks corroborate the formulas but do not replace the analytic uniqueness and endpoint proofs.

## Relationship to prior work

Tóth (2026) establishes isotropic projective Brownian diffusion, fidelity coordinates, and first-passage mean/tail results without the present Poisson-reset phase classification. D'Onofrio, Tamborrino and Lansky (2018) give general Jacobi first-passage moments; the use of these moment methods is prior knowledge, not a novelty claim. Pal and Reuveni's universal coefficient-of-variation criterion, also discussed by Chen and Huang (2022), establishes the general weak-restart sign rule. Chen and Huang classify Brownian motion **inside** an absorbing Euclidean sphere, as opposed to Brownian motion **on** the sphere or on projective pure-state space. Their two-dimensional leading critical-radius rule is consistent with the flat \(b/3\) limit, but does not determine the global projective threshold or the high-fidelity constant. The claimed contribution is the exact single critical-fidelity curve, its proof of uniqueness for each cap and its two sharp asymptotic expansions, not the general restart formula, the Jacobi moment framework or the source diffusion.

## Limitations

The conclusion concerns infinitesimal reset rate only. It does not assert that the rate-zero derivative characterizes a global finite-rate optimum, nor does it decide the second-order rate response exactly at \(x=x_c(b)\). The geometric result is specific to the pure-qubit projective line and to reset-to-initial-state Poisson control, not a generic anisotropic Lindblad process or higher-dimensional projective space. Literature-wide priority is not independently certified. Numerical diagnostics cover finitely many parameters; the mathematical result is established by the preceding proof.

## References

1. G. I. Tóth, *Isotropic random walks and Brownian diffusion on complex projective space*, arXiv:2606.11438v1 (first publicly submitted 2026-06-09), https://arxiv.org/abs/2606.11438 .
2. G. D'Onofrio, M. Tamborrino, P. Lansky, *The Jacobi diffusion process as a neuronal model*, Chaos **28**, 103119 (2018), https://doi.org/10.1063/1.5051494 .
3. H. Chen, F. Huang, *First passage of a diffusing particle under stochastic resetting in bounded domains with spherical symmetry*, Physical Review E **105**, 034109 (2022), https://arxiv.org/abs/2109.11101 .
4. S. Reuveni, *Optimal Stochastic Restart Renders Fluctuations in First Passage Times Universal*, Physical Review Letters **116**, 170601 (2016), https://doi.org/10.1103/PhysRevLett.116.170601 .
5. A. Pal, S. Reuveni, *First Passage under Restart*, Physical Review Letters **118**, 030603 (2017), https://doi.org/10.1103/PhysRevLett.118.030603 .
