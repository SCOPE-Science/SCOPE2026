# Opposite global resetting optima for fresh and persistent uniform anchors on a Brownian circle

## Finding

Let a Brownian searcher with generator \(D\partial_{xx}\), \(D>0\), move on a circle of circumference \(2\ell\), \(\ell>0\), with absorption at one fixed point. The initial position is uniform. An independent exponential clock of rate \(r>0\) triggers instantaneous positional resets. In the **fresh-anchor protocol** (A), a reset site is drawn independently and uniformly at each reset. In the **persistent-anchor protocol** (Q), every reset returns to the initial draw.

With \(z=\ell\sqrt{r/D}\), the mean absorption times are
\[
T_{\mathrm A}(r)=\frac{\ell^2}{D}\frac{z\coth z-1}{z^2},\qquad
T_{\mathrm Q}(r)=\frac{\ell^2}{D}\frac{\cosh z\,\arctan(\sinh z)/z-1}{z^2}.
\]
At every \(r>0\),
\[
0<T_{\mathrm A}(r)<T_0=\frac{\ell^2}{3D}<T_{\mathrm Q}(r)<\infty.
\]
The fresh-anchor mean decreases strictly with \(r\), with unattained infimum zero as \(r\to\infty\). The unique global minimizer of the persistent-anchor mean over \(r\ge0\) is \(r=0\). As \(z\downarrow0\),
\[
\frac{DT_{\mathrm A}}{\ell^2}=\frac13-\frac{z^2}{45}+\frac{2z^4}{945}+O(z^6),\qquad
\frac{DT_{\mathrm Q}}{\ell^2}=\frac13+\frac{z^4}{315}+O(z^6).
\]
Thus the linear-in-rate term of the persistent-anchor population mean vanishes. As \(z\to\infty\),
\[
T_{\mathrm A}\sim\frac{\ell^2}{Dz},\qquad
T_{\mathrm Q}\sim\frac{\pi\ell^2}{4D}\frac{e^z}{z^3},\qquad
\frac{T_{\mathrm Q}}{T_{\mathrm A}}\sim\frac{\pi}{4}\frac{e^z}{z^2}.
\]
Also, for every \(s,r>0\), their hitting times satisfy \(\mathbb E e^{-s\tau_{\mathrm Q}}<\mathbb E e^{-s\tau_{\mathrm A}}\).

The transform comparison extends to **renewal resetting** beyond the circle. Let \(\rho\) be the common initial-site distribution and the distribution of each new site in A; in Q the initial site is retained. Assume each reset to \(x\) starts a new excursion, independent of the past conditional on \(x\), with the same reset-free law as the initial excursion started at \(x\). This restarts all dynamical variables needed for the excursion law, not only the position if other variables matter. The reset clocks are independent of the excursions and site draws. Assume absorption almost surely in both protocols. For each \(s,r>0\) the same weak transform order holds, and it is strict if \(\phi_{s+r}(x)=\mathbb E_x e^{-(s+r)\tau_0}\) is not \(\rho\)-almost surely constant.

## Assumptions and scope

The diffusivity convention is \(D\partial_{xx}\), not \((D/2)\partial_{xx}\). The absorbing point is hit continuously by Brownian motion, and resetting does not consume time. Means average both the Brownian paths and the initial position. Brownian motion with the stated independent reset clock has the required excursion renewal property. For the more general transform comparison, the excursion law may otherwise be arbitrary under the renewal hypothesis; the assumption that its transform is nonconstant is at the specific argument \(s+r\). Positional resets retaining hidden dynamical memory are outside that comparison.

## Proof

**Free hitting transform.** Folding the circle gives reflected Brownian motion on \([0,\ell]\), with absorption at zero and reflection at the antipode \(\ell\). Its initial folded distance \(x\) is uniform on that interval. For \(k=\sqrt{\lambda/D}\), the solution to \(D\phi_\lambda''=\lambda\phi_\lambda\), \(\phi_\lambda(0)=1\), \(\phi_\lambda'(\ell)=0\) is \(\phi_\lambda(x)=\cosh(k(\ell-x))/\cosh(k\ell)\). The reset-free mean solves \(Dm''=-1\) with the same reflecting condition and \(m(0)=0\), giving \(m(x)=x(2\ell-x)/(2D)\) and uniform mean \(T_0\).

**Two renewal averages.** An excursion from \(x\) succeeds before its exponential clock with probability \(\phi_r(x)\) and has average duration \((1-\phi_r(x))/r\), whether or not it succeeds. Fixing \(x\) yields \(\mathbb E_x\tau^{(x)}_r=(1-\phi_r(x))/(r\phi_r(x))\). In A, the initial and subsequent successful-or-reset excursion laws are averaged over independent draws from \(\rho\), giving mean \((1-\Phi_r)/(r\Phi_r)\) with \(\Phi_r=\int\phi_r\,d\rho\). In Q, the conditional renewal mean is then averaged, giving \(r^{-1}(\int\phi_r^{-1}\,d\rho-1)\). On the folded circle \(\Phi_r=\tanh z/z\). The other integral is \(\cosh z\,z^{-1}\int_0^z\operatorname{sech}u\,du\), with \(\int_0^z\operatorname{sech}u\,du=\arctan(\sinh z)\). These give the closed forms and are finite for every finite \(r>0\).

**Global comparison.** The partial fractions identity
\[
\frac{z\coth z-1}{z^2}=2\sum_{j=1}^{\infty}\frac{1}{z^2+\pi^2j^2}
\]
shows strict decrease on \(z>0\), from \(1/3\) to zero, the limits following by summable domination. Let \(B(z)=\int_0^z\operatorname{sech}u\,du\) and \(H(z)=\cosh z\,B(z)-z-z^3/3\). Then
\[
H'(z)=\left(\int_0^z\cosh u\,du\right)\left(\int_0^z\operatorname{sech}u\,du\right)-z^2>0
\]
by strict Cauchy–Schwarz, since \(\cosh u\) is not constant on a nontrivial interval. From \(H(0)=0\) we obtain \(T_{\mathrm Q}-T_0=(\ell^2/D)H(z)/z^3>0\) for every \(z>0\). Taylor expansion gives \(z\coth z=1+z^2/3-z^4/45+2z^6/945+O(z^8)\) and \(\cosh z\,B(z)=z+z^3/3+z^7/315+O(z^9)\). The high-rate equivalents follow from \(\coth z\to1\), \(B(z)\to\pi/2\) and \(\cosh z\sim e^z/2\).

**Transform comparison for renewable excursions.** Fix \(s,r>0\) and put \(u(x)=\phi_{s+r}(x)\). A first excursion contributes \(u(x)\) when it hits before the clock. The transform weight of the clock ringing first is \(r(1-u(x))/(s+r)\), by conditioning on the free hitting time and integrating the clock density. Conditional renewal at fixed \(x\) therefore gives \(F_{\mathrm Q}(s\mid x)=g(u(x))\), where \(g(v)=(s+r)v/(s+rv)\). Independent renewal with site law \(\rho\) gives \(F_{\mathrm A}(s)=g(\int u\,d\rho)\). Since \(g''(v)=-2sr(s+r)/(s+rv)^3<0\) on \([0,1]\), Jensen gives \(\int F_{\mathrm Q}(s\mid x)\rho(dx)\le F_{\mathrm A}(s)\), with strictness precisely for nonconstant \(u\). On the circle \(\phi_{s+r}(x)\) is strictly decreasing on \([0,\ell]\), which gives the required nonconstancy.

## Verification

The accompanying `verify.py` compares the circle formulas with a finite-difference solution of the reflecting/absorbing boundary-value problem and numerical averaging. It also checks sampled signs and endpoint asymptotics. These checks are corroborative only; the all-parameter statements and the hypotheses required for the transform order follow from the proof.

## Relationship to prior work

The renewal construction, fixed-site circle MFPT and fresh-site mixture formulas are established in Julián-Salgado, Castro-Villarreal, Dagdug and Boyer (2026). Méndez, Flaquer-Galmés and Campos (2024) discuss independently drawn reset positions and their mean-first-passage averages on the line. Pal and Prasad (2019) study resetting to a fixed start in an absorbing interval. The additional claim here is the all-positive-rate comparison of matched uniform populations distinguished solely by whether a reset site persists, the resulting opposite optima, and their paired transform ordering. The underlying renewal formulas, free-circle solution and Jensen's inequality are not claimed as new.

## Limitations

The strict ordering against the unreset mean is proved for exactly uniform sampling on the circle. The Laplace-transform order is not a claim of ordinary stochastic dominance. No monotonicity of the persistent-anchor mean at positive rates is asserted. The broader transform comparison requires complete conditional renewal and does not cover resets with retained hidden dynamics. Historical priority is not established by the analysis.

## References

1. P. Julián-Salgado, P. Castro-Villarreal, L. Dagdug and D. Boyer (2026), *Mirror transitions in diffusion with stochastic resetting confined on a ring*, [arXiv:2605.08414v1](https://arxiv.org/html/2605.08414v1).
2. V. Méndez, R. Flaquer-Galmés and D. Campos (2024), *First-passage time of a Brownian searcher with stochastic resetting to random positions*, [arXiv:2401.01125v1](https://arxiv.org/html/2401.01125v1).
3. A. Pal and V. V. Prasad (2019), *First passage under stochastic resetting in an interval*, *Physical Review E* 99, 032123, [arXiv:1812.03009](https://arxiv.org/abs/1812.03009).
