# A sharp fast-refresh search threshold for two positive fluctuating reset intensities

## Finding

Consider an absorbed Brownian searcher, diffusivity \(D>0\), which starts and repeatedly resets to \(a>0\). A *persistent* independent two-state Markov environment, initially uniform in its two states, has generator \(Q=\frac{\nu}{2}\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\) and controls the position-reset intensities \(r+\eta\) and \(r-\eta\), where \(0<\eta<r\). A position reset does not change the environment. Write \(T_\nu(r,\eta)\) for the mean time to hit zero and \(\ell=a/\sqrt D\). Define

\[
 h(s)=\frac{e^{\ell\sqrt{s}}-1}{s},\qquad s>0,
\]

and the symmetric positive matrix

\[
 B=\begin{pmatrix}r&\eta\\\eta&r+\nu\end{pmatrix},\qquad H=h(B).
\]

The *exact* mean is the scalar Schur complement

\[
 \boxed{T_\nu(r,\eta)=H_{11}-\frac{\nu H_{12}^{\,2}}{1+\nu H_{22}}
 =\frac{H_{11}+\nu\det H}{1+\nu H_{22}}.}
\]

For fixed \(r>\eta>0\), as the environment refresh frequency tends to infinity,

\[
 \boxed{T_\nu(r,\eta)=h(r)-\frac{\eta^2 h'(r)}{\nu}
 +\frac{\eta^2h(r)+\frac12\eta^4h''(r)}{\nu^2}
 +O_{r,\eta,\ell}(\nu^{-3}).}
\]

The expansion and its first derivative in \(r\) are locally uniform on compact subsets of \(\{r>\eta>0\}\). In the opposite slow-refresh limit,

\[
 \lim_{\nu\downarrow0}T_\nu(r,\eta)
 =\frac{h(r-\eta)+h(r+\eta)}2>h(r).
\]

The Poisson-reset benchmark \(h(r)\) has its unique global minimizer \(r_*=(z_*/\ell)^2\), where \(z_*=1.5936242600\ldots\) is the positive solution of \((z-2)e^z+2=0\). At that optimal mean rate the first fast-refresh correction vanishes; the next correction has a strictly positive coefficient:

\[
 \boxed{\lim_{\nu\to\infty}\nu^2[T_\nu(r_*,\eta)-h(r_*)]
 =\eta^2h(r_*)+\tfrac12\eta^4h''(r_*)>0,\quad 0<\eta<r_*.}
\]

More sharply, fix \(\eta\in(0,r_*)\) and place the mean rate in the **critical window** \(r=r_*+c/\nu\), with fixed \(c\in\mathbb R\). Set

\[
 c_{\mathrm{crit}}=\frac{h(r_*)}{h''(r_*)}+\frac{\eta^2}{2}.
\]

Then, uniformly for \(c\) in any fixed compact interval,

\[
 \boxed{\lim_{\nu\to\infty}\nu^2
 \left[T_\nu\!\left(r_*+\frac c\nu,\eta\right)-h\!\left(r_*+\frac c\nu\right)\right]
 =\eta^2h''(r_*)\bigl(c_{\mathrm{crit}}-c\bigr).}
\]

Hence for sufficiently rapid refresh, fluctuations **slow** search at fixed \(c<c_{\mathrm{crit}}\) and **accelerate** search at fixed \(c>c_{\mathrm{crit}}\), relative to a constant reset intensity equal to the same mean \(r\). For all sufficiently large \(\nu\), there is exactly one zero of \(T_\nu(r,\eta)-h(r)\) in a fixed sufficiently small neighborhood of \(r_*\), and it obeys

\[
 \boxed{r_{\mathrm{thr}}(\nu)=r_*+\frac{c_{\mathrm{crit}}}{\nu}+O(\nu^{-2}).}
\]

This local uniqueness is **not** a claim of global uniqueness at arbitrary rates. The critical-window formula does not determine the sign at its exactly balanced coordinate \(c=c_{\mathrm{crit}}\).

## Assumptions and scope

The position evolves as \(dX_t=\sqrt{2D}\,dW_t\) between resets, with absorption at zero. Conditional on the environment, resets form a Poisson process of intensity \(r+\eta\) in state one and \(r-\eta\) in state two; a reset sends \(X_t\) to \(a\) but **preserves the current environmental state**. The independent environment flips between its two states at rate \(\nu/2\) in either direction. Its initial distribution is stationary, assigning probability \(1/2\) to each state. All parameters \(D,a,\nu,r,\eta\) are strictly positive with \(0<\eta<r\).

The first displayed exact formula and slow/fast limits hold for all such parameters. The near-critical statements fix \(a,D,\eta\), require \(\eta<r_*\), and take \(\nu\to\infty\). In the local-zero statement the neighborhood is chosen so \(r>\eta\) throughout. The limit statements concern **mean first-passage time**, not the full hitting-time distribution or optimality over nonconstant controls. The environmental refresh convention is: redraw the intensity independently from the two equiprobable values at Poisson rate \(\nu\); this is equivalent, after ignoring redraws of the same value, to flips at rate \(\nu/2\).

## Proof

**1. Finiteness and the backward boundary-value problem.** Each state has reset intensity bounded between \(r-\eta>0\) and \(r+\eta\). In any sufficiently long fixed time block, uniformly over the initial position and environment, there is a positive probability of a reset in its first half and of hitting zero without another reset in its second half. Iteration gives a geometric survival bound and finite hitting-time means. Let \(u_i(x)\) denote the mean starting at position \(x\) and environmental state \(i\), and set \(v_i=u_i(a)\). The backward equation with absorbing boundary is

\[
 -\mathbf1=D\mathbf u''(x)+Q\mathbf u(x)+\Lambda(\mathbf v-\mathbf u(x)),
 \qquad \mathbf u(0)=0,
\]

where \(\Lambda=\operatorname{diag}(r+\eta,r-\eta)\). Set \(B_0=\Lambda-Q\), a strictly positive matrix. Solving the constant-coefficient boundary problem and evaluating at \(a\) gives

\[
 \mathbf v=K(\mathbf1+\Lambda\mathbf v),\qquad
 K=B_0^{-1}(I-e^{-\ell\sqrt{B_0}}).
\]

The bounded solution is uniquely determined. If \(E=e^{-\ell\sqrt{B_0}}\), then \(I-K\Lambda=E-KQ=E(I-H_0Q)\), where \(H_0=E^{-1}K=h(B_0)\). Thus

\[
 (I-H_0Q)\mathbf v=H_0\mathbf1.
\]

**2. Exact two-state reduction.** Move to the normalized symmetric/antisymmetric environmental basis. In this basis \(Q=\operatorname{diag}(0,-\nu)\), \(B_0\) becomes the symmetric matrix \(B\) stated in the finding, and \(\mathbf1\) becomes \(\sqrt2(1,0)^\top\). Consequently, the first component of the last linear system reads

\[
 \frac{v_{\mathrm{sym}}}{\sqrt2}
 =H_{11}-\frac{\nu H_{12}^2}{1+\nu H_{22}}.
\]

This component is the stationary-environment average of the two physical first-passage means. The determinant identity follows by elementary algebra. The denominator is positive since \(H\) is positive definite.

**3. Spectral representation and the fast-refresh expansion.** Define

\[
 \Delta=\sqrt{\nu^2+4\eta^2},\quad
 \lambda_-=r+\frac{\nu-\Delta}{2},\quad
 \lambda_+=r+\frac{\nu+\Delta}{2},\quad
 p=\frac{1+\nu/\Delta}{2},\quad q=1-p.
\]

The eigenvalues are positive, with \(\lambda_-\ge r-\eta>0\). Writing \(h_\pm=h(\lambda_\pm)\), the preceding formula becomes

\[
 T_\nu=\frac{\nu h_-h_++p h_-+q h_+}
 {1+\nu(qh_-+p h_+)}.
\]

As \(\nu\to\infty\), for fixed \(r,\eta\),

\[
 \lambda_-=r-\frac{\eta^2}{\nu}+O(\nu^{-3}),\quad
 p=1-\frac{\eta^2}{\nu^2}+O(\nu^{-4}),\quad
 q=\frac{\eta^2}{\nu^2}+O(\nu^{-4}).
\]

Also \(h_+=e^{\ell\sqrt\nu+O(\nu^{-1/2})}/\nu\,(1+o(1))\), so its inverse decreases faster than every inverse power of \(\nu\). Divide the spectral quotient by \(\nu h_+\): then

\[
 T_\nu=\frac{h_-}{p}+O(\nu^{-3})
 =h(r)-\frac{\eta^2h'(r)}\nu
 +\frac{\eta^2h(r)+\frac12\eta^4h''(r)}{\nu^2}
 +O(\nu^{-3}).
\]

All operations and their first \(r\)-derivatives are uniform on compact parameter regions with \(r>\eta>0\). This establishes the stated expansion including the derivative needed for local uniqueness.

**4. Curvature of the Poisson benchmark.** Let \(z=\ell\sqrt{s}\). Direct differentiation gives

\[
 h'(s)=\frac{1+e^z(z/2-1)}{s^2},\qquad
 h''(s)=\frac{e^z(z^2-5z+8)-8}{4s^3}.
\]

The derivative of the numerator of \(4s^3h''(s)\) with respect to \(z\) is \(e^z(z^2-3z+3)>0\), and that numerator vanishes at \(z=0\). Hence \(h''(s)>0\) for all \(s>0\). The numerator of \(s^2h'(s)\) starts at zero, decreases until \(z=1\), and then increases through its unique positive zero \(z_*>1\). Therefore the unique positive global minimizer is \(r_*=(z_*/\ell)^2\). At \(r=r_*\), the first-order term vanishes while the displayed second-order coefficient is positive. As \(\nu\downarrow0\), the spectral matrix tends to \(\begin{pmatrix}r&\eta\\\eta&r\end{pmatrix}\), giving the average of \(h(r-\eta)\) and \(h(r+\eta)\); strict convexity proves the inequality.

**5. Critical window and the local zero.** Fix \(0<\eta<r_*\) and substitute \(r=r_*+c/\nu\) into the locally uniform expansion. Taylor's theorem with \(h'(r_*)=0\) gives

\[
 T_\nu(r,\eta)-h(r)
 =\frac{-\eta^2h''(r_*)c+\eta^2h(r_*)+\frac12\eta^4h''(r_*)}{\nu^2}
 +O_{c}(\nu^{-3}),
\]

uniformly over compact sets of \(c\), proving the critical-window limit. For a sufficiently small fixed neighborhood of \(r_*\), differentiated uniformity and strict positivity of \(h''\) give

\[
 \partial_r\{T_\nu(r,\eta)-h(r)\}
 =-\frac{\eta^2h''(r)}\nu+O(\nu^{-2})<0.
\]

The difference is positive at the left endpoint and negative at the right endpoint for all sufficiently large \(\nu\), because \(h'\) changes sign from negative to positive at \(r_*\). Thus it has exactly one zero in that neighborhood. Its distance from \(r_*\) is \(O(\nu^{-1})\); inserting the critical-window expansion and using the derivative bound refines its location to \(r_*+c_{\mathrm{crit}}/\nu+O(\nu^{-2})\).

## Verification

The self-contained companion program `verify.py` uses Python 3 and `mpmath` (version 1.2 or newer). Execute `python verify.py` from the directory containing this document. It independently solves the two-component backward boundary linear system and compares its mean with the spectral Schur formula; checks analytic derivatives against high-precision differentiation; tests slow/fast limits, strict curvature, the positive correction at the Poisson optimum, and the signs and scale of the critical-window crossover across three distances and multiple amplitudes. Its executed result is: `PASS: 294 bounded high-precision checks`.

For an illustrative normalization \(\ell=1\) and amplitude \(\eta=1\), the critical benchmark is \(r_*=2.539638282188165\ldots\), and the threshold coefficient is \(c_{\mathrm{crit}}=22.2301179837920\ldots\). These numerical examples are finite consistency checks, not substitutes for the asymptotic proof.

## Relationship to prior work

Arutkin and Reuveni (2025), *Diffusion with doubly stochastic resetting* (arXiv:2509.25365v1), introduced the independent fluctuating reset-rate framework and derived stationary spatial distributions, explicitly identifying the first-passage problem as an extension. Their paper does not state an absorbed-searcher mean, a positive-two-rate fast-refresh expansion, or the critical-window boundary.

Bressloff (2020), *Switching diffusions and stochastic resetting* (J. Phys. A **53**, 275003), derives first-passage means for **switching diffusivities** coupled to a constant position-reset rate, in a protocol that resets the diffusion state. The generator and reset-state memory are different from the present rate-modulation protocol. Pal, Kundu and Evans (2016), *Diffusion under time-dependent resetting*, treat reset intensity dependent on time **since the previous reset**, rather than on an autonomous environment retained across position resets. The standard optimal Poisson resetting rate and its defining scalar equation predate this work.

The exact fixed-rate mean is a special case of standard renewal theory; the contribution here is the threshold **in the singular window where the ordinary first-order fast-environment comparison vanishes**, including the strictly positive second-order offset and the local-zero location. A general undiscovered modulated-reset first-passage comparison theorem may still subsume these results; the claim is not independently priority-validated.

## Limitations

The local zero is proved only for sufficiently rapid refreshing and near the Poisson-optimal mean intensity; no global phase diagram or uniqueness at finite switching speed is asserted. Neither a full hitting-time distribution nor stochastic resetting-cost optimization is established. The amplitude \(\eta\) is fixed in all fast-refresh limits. The exact balanced critical-window coordinate has no sign determined to the displayed order. Finite numerical tests cannot certify universal statements. Full text of some tangential switching/resetting literature was not accessible; independent mathematical validation and publication-priority review have not been performed.

## References

1. M. Arutkin and S. Reuveni, *Diffusion with doubly stochastic resetting*, arXiv:2509.25365v1 (first public submission September 29, 2025), https://arxiv.org/html/2509.25365v1.
2. P. C. Bressloff, *Switching diffusions and stochastic resetting*, J. Phys. A: Math. Theor. **53** (2020), 275003, https://doi.org/10.1088/1751-8121/ab97e0. Lawful author manuscript: https://www.math.utah.edu/~bresslof/publications/20-10.pdf.
3. A. Pal, A. Kundu and M. R. Evans, *Diffusion under time-dependent resetting*, J. Phys. A **49** (2016), 225001, https://doi.org/10.1088/1751-8113/49/22/225001.
4. Y. Baouche and C. Kurzthaler, *Optimal first-passage times of active Brownian particles under stochastic resetting*, Soft Matter **21** (2025), 5998–6011, https://doi.org/10.1039/D5SM00340G (for the established Poisson benchmark).
