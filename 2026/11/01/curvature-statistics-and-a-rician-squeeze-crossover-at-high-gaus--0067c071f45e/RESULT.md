# Curvature statistics and a Rician squeeze crossover at high Gaussian spectrogram peaks

## Finding

Let \(F(z)=\sum_{n\geq0}a_nz^n/\sqrt{n!}\), where the coefficients are independent standard circular complex Gaussians, and let \(H(z)=e^{-|z|^2}|F(z)|^2\). For a real squeeze parameter \(b\), put \(S_b=\operatorname{diag}(e^b,e^{-b})\) and \(H_b(x,y)=H(e^b x+i e^{-b}y)\). This is the normalized form, in the law of Gaussian white noise, of the spectrogram with the unit-norm dilated Gaussian window \(g_b(t)=e^{b/2}g_0(e^bt)\), where \(g_0(t)=2^{1/4}e^{-\pi t^2}\). In the standard short-time Fourier convention, dilation sends time-frequency coordinates \((x,\xi)\) to \((e^bx,e^{-b}\xi)\), and an independent standard complex white-noise input is invariant in law under the corresponding unitary dilation. The real coordinates are the Bargmann–Fock coordinates in which the unsqueezed field has the displayed formula; the fixed Bargmann reparametrization of frequency may reverse an axis without affecting the Hessian eigenvalues.

At every strict local maximum of \(H_b\), let \(\kappa_+\geq\kappa_->0\) be the eigenvalues of \(-D^2\log H_b\), and set \(K_b=\kappa_+/\kappa_-\). Sampling a maximum uses the intensity-normalized Palm law (defined below), rather than conditioning on the probability-zero event that a fixed location is critical. For the unsqueezed window, the curvature condition number has the *exact* tail

\[
\mathbb P_{\mathrm{Palm}}(K_0>r)=\frac{64r^2}{(3r^2+2r+3)^2},\qquad r\geq1.
\]

In particular, \(\mathbb E_{\mathrm{Palm}}K_0<\infty\) but \(\mathbb E_{\mathrm{Palm}}K_0^2=\infty\).

For any sequence \(b_h\in\mathbb R\) such that \(\sqrt h\,b_h\to\eta\in\mathbb R\), condition the Palm maximum on its *squared* spectrogram height being at least \(h\). Then, as \(h\to\infty\),

\[
\boxed{\sqrt h\,(K_{b_h}-1)\ \Rightarrow\ 2\sqrt{(X-2\eta)^2+Y^2},}
\]

where \(X,Y\) are independent real standard Gaussians. The limiting density is, for \(t>0\),

\[
 f_\eta(t)=\frac t4\exp\!\left(-\frac{t^2}{8}-2\eta^2\right)I_0(|\eta|t),\qquad
 I_0(v)=\frac1{2\pi}\int_0^{2\pi}e^{v\cos\theta}\,d\theta.
\]

At \(\eta=0\), the limit is Rayleigh with tail \(e^{-t^2/8}\); nonzero \(\eta\) produces a Rician crossover. At every *fixed* \(b\ne0\), by contrast, under the same height-thresholded Palm law,

\[
\boxed{\sqrt h\left(\frac{K_b}{e^{4|b|}}-1\right)\Rightarrow N(0,4).}
\]

Thus the transition between random circular splitting and deterministic squeeze-induced splitting occurs at window-squeeze order \(h^{-1/2}\).

## Assumptions and scope

The complex Gaussian variables \(a_n\) have density \(\pi^{-1}e^{-|a|^2}\) with respect to planar Lebesgue measure, so \(|a_n|^2\) is exponential with mean one. The series defines an entire function almost surely. All maxima of positive height are nondegenerate almost surely, and the statements concern Euclidean Hessians in the fixed displayed coordinates.

For any measurable mark functional \(\Phi\) of a peak, and any bounded planar region \(\Omega\) of positive area, define its Palm expectation by

\[
 \mathbb E_{\mathrm{Palm}}\Phi
 =\frac{\mathbb E\sum_{z\in\Omega:\,z\text{ a local maximum of }H_b}\Phi(z)}{\mathbb E\#\{z\in\Omega:z\text{ a local maximum of }H_b\}}.
\]

For the stationary field, this ratio does not depend on \(\Omega\). The height-conditioned law is the above intensity ratio restricted to maxima satisfying \(H_b(z)\ge h\), normalized by the intensity of such maxima. The squeeze is a determinant-one linear coordinate change, so its Palm distributions are transported exactly. The derivatives of \(\log H_b\) are evaluated only at positive maxima; zeros of \(F\) are minima and do not enter.

## Proof

**1. Magnetic-translation reduction and the Kac–Rice measure.** The Gaussian entire function is covariant under magnetic translations: for every fixed \(w\), the translated function \(F_w(z)=e^{-|w|^2/2-z\bar w}F(z+w)\) has the same covariance \(\mathbb E[F_w(z)\overline{F_w(v)}]=e^{z\bar v}\) and therefore the same law as \(F\). Moreover \(e^{-|z|^2}|F_w(z)|^2=H(z+w)\). Thus the field of positive peak heights and Hessians at a Palm maximum can be computed at the origin. Define \(G(z)=F'(z)-\bar zF(z)\). At the origin, \(G(0)=a_1\); the critical-point constraint is \(a_1=0\). The complex partials are \(\partial_zG(0)=\sqrt2a_2\) and \(\partial_{\bar z}G(0)=-a_0\). Consequently the real Jacobian of \(G\) is \(2|a_2|^2-|a_0|^2\), and the zero is a positive-height maximum exactly when \(|a_0|^2>2|a_2|^2\).

Put \(s=|a_0|^2\) and \(t=|a_2|^2\). The zero density of the independent standard Gaussian \(a_1\) is \(1/\pi\), and the positive Kac–Rice Jacobian weight is \((s-2t)_+\). Since \(\mathbb E(s-2t)_+=\int_0^\infty e^{-3t}\,dt=1/3\), the unsqueezed peak intensity is \(1/(3\pi)\). The *normalized* Palm joint density of \((s,t)\) is therefore

\[
 p(s,t)=3(s-2t)e^{-s-t}\mathbf1_{\{s>2t>0\}}.
\]

The phases of \(a_0,a_2\) remain independent uniform variables under this weighting.

**2. The exact unsqueezed curvature distribution.** At a critical point set \(c=\sqrt2a_2/a_0\). An expansion of \(\log H\) to second order gives

\[
 -\frac12D^2\log H(0)
 =\begin{pmatrix}1-\operatorname{Re}c&\operatorname{Im}c\\
 \operatorname{Im}c&1+\operatorname{Re}c\end{pmatrix}.
\]

For a maximum, \(|c|<1\), and its curvature ratio is \(K_0=(1+|c|)/(1-|c|)\). Changing variables from \((s,t)\) to \((s,u)\) with \(u=2t/s=|c|^2\), integrating over \(s\), and using \(\int_0^\infty s^2e^{-qs}ds=2/q^3\), yields

\[
 p_U(u)=\frac{3(1-u)}{(1+u/2)^3}\mathbf1_{\{0<u<1\}},\qquad
 \mathbb P(U>u)=\frac{(1-u)^2}{(1+u/2)^2}.
\]

Substitute \(u=((r-1)/(r+1))^2\) to obtain the exact tail stated above. It decays like \((64/9)r^{-2}\), proving the first-moment and second-moment assertions by the tail-integral criterion.

**3. The high-peak jet limit.** Direct integration of the Palm density gives the squared-height marginal

\[
 p_S(s)=3(s-2+2e^{-s/2})e^{-s},\quad s>0,
\]

and the conditional density

\[
 p_{T\mid S=s}(t)=\frac{(s-2t)e^{-t}}{s-2+2e^{-s/2}}\mathbf1_{\{0<t<s/2\}}.
\]

For \(s\to\infty\), this density converges in total variation to the unit exponential law. Under \(S\ge h\), \(S/h\to1\) in probability (indeed \(S-h\) is tight), so the same exponential limit holds for \(T\), jointly with the independent uniform phase. Hence

\[
 \sqrt h\,c\Rightarrow X+iY,
 \qquad X,Y\overset{\mathrm{iid}}{\sim}N(0,1).
\]

This uses the squared-height threshold, not the amplitude threshold.

**4. Squeezing and the Rician crossover.** Since \(\det S_b=1\) and maxima are taken bijectively to maxima, the preceding Palm jet law applies at the corresponding points of \(H_b=H\circ S_b\). At a critical point, the Hessian is transformed by congruence; with \(c=x+iy\),

\[
 -\frac12D^2\log H_b
 =\begin{pmatrix}e^{2b}(1-x)&y\\y&e^{-2b}(1+x)\end{pmatrix}.
\]

If \(\sqrt h b_h\to\eta\), the preceding matrix is

\[
 I+\frac1{\sqrt h}\begin{pmatrix}2\eta-X_h&Y_h\\Y_h&-2\eta+X_h\end{pmatrix}+o_{\mathbb P}(h^{-1/2}),
\]

where \((X_h,Y_h)=\sqrt h(\operatorname{Re}c,\operatorname{Im}c)\Rightarrow(X,Y)\). The eigenvalues therefore equal \(1\pm r_h/\sqrt h+o_{\mathbb P}(h^{-1/2})\), where \(r_h\Rightarrow\sqrt{(X-2\eta)^2+Y^2}\). Their ratio gives the stated weak limit. Polar integration of the shifted two-dimensional normal density gives the displayed Bessel/Rician density.

For a fixed \(b\ne0\), the deterministic matrix \(\operatorname{diag}(e^{2b},e^{-2b})\) has distinct eigenvalues. First-order nondegenerate eigenvalue perturbation yields \(K_b=e^{4|b|}(1-2\operatorname{sgn}(b)\operatorname{Re}c+o_{\mathbb P}(h^{-1/2}))\). The same jet limit proves the centered normal limit of variance four.

## Verification

The standalone file `checker.py` uses only the Python standard library and tests the exact \(u\)-density normalization, the exact condition-number tail, the positive Kac–Rice mass, the Gamma integral, random eigenvalue calculations, the height-dependent critical scaling, and independent weighted Palm Monte Carlo checks. It prints a passing total of 79 supplementary assertions when executed with `python3 checker.py`. Numerical tests are finite and **not** a proof of weak convergence; the preceding Kac–Rice and conditional-distribution arguments supply the proof.

## Relationship to prior work

Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions* (first publicly posted October 13, 2022), proves the average maxima density and the marginal height distribution; its Sections 3–4 use the same Chern-critical-point and Kac–Rice framework. This proof explicitly verifies those premises, then studies a different *mark*: the ratio of real Hessian eigenvalues, both exactly and under a height-dependent family of squeezed windows. The previously published marginal height law by itself does not state or calculate the real-Hessian curvature ratio or its Rician double-scaling limit.

Haimi, Koliander, and Romero's work on Gaussian Weyl–Heisenberg zeros and topological charge treats counts and critical-index signs, not this curvature ratio. More recent research on repulsion and hyperuniformity studies spatial two-point/number-variance observables, rather than a one-point marked Hessian law. Classical metaplectic covariance provides the coordinate change but does not itself supply the marked Palm distribution or the high-peak transition. These distinctions are mathematical comparisons, not a claim that all potentially related literature has been exhausted.

## Limitations

This theorem concerns complex Gaussian white noise, analytic Gaussian-window STFT, real two-dimensional Hessians in a fixed normalization, and intensity-averaged (not typical-realization or extreme-value-selected) local maxima. The threshold is on squared spectrogram height. The limiting variable concerns *a Palm-selected peak conditioned on height*, not the global tallest peak of a large observation region. It does not prove universality for other windows, non-Gaussian noise, multiwindow transforms, arbitrary non-symplectic deformations, or joint correlations of peak shapes. The high-peak and squeeze scaling limits are weak convergence statements; no uniform rate is claimed. Independent validation and a complete historical-priority determination are not asserted.

## References

1. Luís Daniel Abreu, *Local Maxima of White Noise Spectrograms and Gaussian Entire Functions*, arXiv:2210.06721, first posted 2022-10-13; *Journal of Fourier Analysis and Applications* **28**, article 88 (2022), DOI 10.1007/s00041-022-09979-7. Open-access full text: https://link.springer.com/article/10.1007/s00041-022-09979-7.
2. Antti Haimi, Günther Koliander, José Luis Romero, *Zeros of Gaussian Weyl–Heisenberg Functions and Hyperuniformity of Charge*, *Journal of Statistical Physics* (2022), DOI 10.1007/s10955-022-02917-3. https://link.springer.com/article/10.1007/s10955-022-02917-3.
3. Antti Haimi, Lukas Odelius, José Luis Romero, *Local repulsion between zeros and critical points of the Gaussian Entire Function*, arXiv:2510.06821, posted 2025-10-08. https://arxiv.org/abs/2510.06821.
