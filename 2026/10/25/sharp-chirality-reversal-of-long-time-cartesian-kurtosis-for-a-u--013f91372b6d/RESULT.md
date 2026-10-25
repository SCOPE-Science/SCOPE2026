# Sharp chirality reversal of long-time Cartesian kurtosis for a uniformly reorienting active particle

## Finding
Consider a free two-dimensional particle of propulsion speed \(v>0\), with orientation rotating deterministically at angular speed \(\omega\in\mathbb R\) between Poisson events of rate \(\gamma>0\). At each event, the orientation is replaced independently by a uniform angle. Let the initial angle be uniform and let independent planar Brownian translation have diffusivity \(D\ge0\). Write \(X_t\) for either fixed Cartesian projection of its displacement from the origin, and put \(w=\omega/\gamma\). The limits of its second and fourth cumulants are
\[
\lim_{t\to\infty}\frac{\kappa_2(X_t)}t=2D+\frac{v^2}{\gamma(1+w^2)},
\qquad
\lim_{t\to\infty}\frac{\kappa_4(X_t)}t=\frac{3v^4}{\gamma^3}\frac{3w^4-10w^2-1}{(1+w^2)^3(1+4w^2)}.
\]
The fourth-cumulant growth rate is strictly negative for \(0\le |w|<w_*\), zero for \(|w|=w_*\), and strictly positive for \(|w|>w_*\), where the unique threshold is
\[
w_*=\sqrt{\frac{5+2\sqrt7}{3}}=1.852161136090232\ldots.
\]
In particular, for every fixed \(|w|\ne w_*\), the excess kurtosis of the projected displacement has the same sign as this fourth-cumulant growth rate at all sufficiently large times; its magnitude decays like \(1/t\). The sign threshold is independent of \(D\), even though \(D\) increases the variance.

## Assumptions and scope
The angular process \(\Theta_t\in\mathbb R/(2\pi\mathbb Z)\) starts uniformly, follows \(d\Theta_t/dt=\omega\) between independent exponential waiting times of rate \(\gamma\), and is freshly uniformized at each waiting-time endpoint. The position is \(\mathbf R_t=v\int_0^t(\cos\Theta_s,\sin\Theta_s)\,ds+\sqrt{2D}\,\mathbf B_t\) with an independent standard planar Brownian motion. All parameters and quantifiers above are fixed before taking \(t\to\infty\). A projected coordinate is measured along any fixed direction; rotational invariance makes all choices equivalent. \(\kappa_4(Z)=\mathbb E[(Z-\mathbb EZ)^4]-3\operatorname{Var}(Z)^2\) and \(\kappa_2(Z)=\operatorname{Var}(Z)\). No statement about the sign of the finite-time fourth cumulant on the threshold is asserted.

## Proof
The backward angular generator acting on periodic functions is
\[
(Lf)(\theta)=\omega f'(\theta)+\gamma\left(\frac1{2\pi}\int_0^{2\pi}f(\phi)\,d\phi-f(\theta)\right).
\]
Its constant Fourier mode has simple eigenvalue zero and each nonconstant mode \(e^{in\theta}\) has eigenvalue \(-\gamma+in\omega\). The nonzero spectrum is separated from zero by real-part gap \(\gamma\). Thus the bounded perturbation \(L+kv\cos\theta\) has a simple analytic eigenvalue \(\Lambda(k)\) emerging from zero for sufficiently small real \(k\). The positive Feynman--Kac semigroup and the spectral gap give \(\log\mathbb E[e^{kX_t}]=t[\Lambda(k)+Dk^2]+O(1)\) locally analytically in \(k\). Differentiating the analytic asymptotic expansion at the origin identifies the linear-in-time cumulants, while the Brownian term contributes only to the second cumulant.

Set \(z=kv/\gamma\), \(w=\omega/\gamma\), and \(\ell(z)=\Lambda(k)/\gamma\). Normalize the eigenfunction so that its zeroth Fourier coefficient is one and denote the others by \(c_n\). The Fourier equations are
\[
\ell=\frac z2(c_1+c_{-1}),\qquad (\ell+1-inw)c_n=\frac z2(c_{n-1}+c_{n+1})\quad(n\ne0).
\]
Reality and rotational symmetry imply \(c_{-n}=\overline{c_n}\) and evenness in \(z\). To fourth order only the modes \(|n|\le2\) can contribute. Write
\[
c_1=zA_1+z^3B_1+O(z^5),\quad c_2=z^2A_2+O(z^4),\quad \ell=z^2a_2+z^4a_4+O(z^6).
\]
Coefficient comparison gives
\[
A_1=\frac1{2(1-iw)},\quad A_2=\frac{A_1}{2(1-2iw)},\quad a_2=\operatorname{Re}A_1,
\quad B_1=\frac{A_2/2-a_2A_1}{1-iw},\quad a_4=\operatorname{Re}B_1.
\]
Straightforward conjugate-denominator reduction, reproducible in the supplied checker, yields
\[
a_2=\frac1{2(1+w^2)},\qquad
a_4=\frac{3w^4-10w^2-1}{8(1+w^2)^3(1+4w^2)}.
\]
Because \(\Lambda(k)=\gamma\ell(kv/\gamma)\), differentiating twice and four times gives the displayed cumulant rates. The denominator of \(a_4\) is strictly positive for every real \(w\). Setting \(u=w^2\ge0\) reduces the numerator to \(3u^2-10u-1\), whose two roots are \((5\pm2\sqrt7)/3\); precisely one is nonnegative. Its leading coefficient is positive and its value at zero is negative, proving the asserted strict signs and uniqueness. For \(|w|\ne w_*\), the fourth cumulant is its nonzero rate times \(t\) plus \(O(1)\), while the variance is its strictly positive rate times \(t\) plus \(O(1)\); division proves the excess-kurtosis claim. This is not a thermodynamic phase transition.

## Verification
The attached standalone `check.py` recomputes the complex Fourier perturbation coefficients in exact symbolic arithmetic, factors the unique-threshold quadratic, and independently extracts the fourth-order Taylor coefficient from finite Fourier-section eigenvalues at eight chirality parameters and three small tilts each. Its recorded run passes 52 assertions. The finite Fourier checks are diagnostic only: the infinite-mode reduction at fourth order follows from the Fourier recurrence in the proof, not from truncation. A zero of the linear-in-time fourth cumulant at threshold does not establish vanishing fourth cumulant at fixed time.

## Relationship to prior work
Santra, Basu and Sabhapandit [1] develop exact moment recursions and long-time non-Gaussian corrections for the uniform-reset planar run-and-tumble process with \(\omega=0\), with and without translational Brownian diffusion. Their achiral fourth-cumulant coefficient is recovered here when \(w=0\). Their earlier broad active-particle expansion framework [2] gives a general method, but does not in its abstract specialize to this angular-drift-plus-uniform-reorientation threshold. Mallikarjun and Pal [3] treat a distinct *four-heading* chiral jump process, not a continuously rotating orientation with fresh uniform angles. The assessed contribution is the exact continuum-heading chirality threshold and its strict one-crossing classification, rather than the eigenvalue-perturbation technique itself. Existing treatments of chiral active Brownian particles with rotational diffusion [4] are dynamically distinct because their higher Fourier harmonics decay at rates proportional to squared harmonic number, rather than the constant \(\gamma\) here.

## Limitations
This theorem concerns one freely moving noninteracting particle, uniform Poisson reorientation, constant rotation frequency, and long-time fourth cumulants of a one-dimensional projection. It does not give the full finite-time distribution, the full spatial large-deviation rate, a finite-time sign classification, interacting swimmers, biased/nonuniform tumble laws, or a thermodynamic transition. An equivalent threshold hidden in a broader published high-order spectral expansion would affect priority; independent scholarly priority assessment has not been performed.

## References
[1] I. Santra, U. Basu and S. Sabhapandit, *Long time behavior of run-and-tumble particles in two dimensions*, arXiv:2211.07337 (first posted 2022-11-14), https://arxiv.org/abs/2211.07337; full-text version inspected: https://arxiv.org/html/2211.07337v3.

[2] I. Santra, U. Basu and S. Sabhapandit, *Universal framework for the long-time position distribution of free active particles*, arXiv:2202.12117 (first posted 2022-02-24), https://arxiv.org/abs/2202.12117.

[3] R. Mallikarjun and A. Pal, *Chiral run-and-tumble walker: transport and optimizing search*, arXiv:2209.05912 (first posted 2022-09-13), https://arxiv.org/abs/2209.05912.

[4] A. Pattanayak, A. Shee, A. Chaudhuri and D. Chaudhuri, *Inertia–chirality interplay in active Brownian motion: exact dynamics and phase maps*, *New Journal of Physics* (2026), https://doi.org/10.1088/1367-2630/ae5f40 (different angular noise and inertia model).
