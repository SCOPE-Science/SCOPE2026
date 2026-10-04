# Sharpness of the square-mass exponent for pure-point Fourier transforms

## Finding
There exists a continuous function \(f:\mathbb R\to(0,\infty)\), bounded above and below by positive constants, such that the positive measure
\[
\mu=f(x)\,dx
\]
is translation bounded, its distributional Fourier transform is a pure-point Radon measure
\[
\widehat\mu=\sum_{\gamma\in\Gamma}b_\gamma\delta_\gamma
\]
with locally finite support, and for every \(q>0\) the powered-mass measure
\[
\nu_q=\sum_{\gamma\in\Gamma}|b_\gamma|^q\delta_\gamma
\]
is translation bounded exactly when \(q\ge2\).

Consequently, the exponent \(2\) in the local square-mass theorem of Boyvalenkov--Favorov is optimal. In particular, the question in their Remark 2 asking whether the conclusion remains valid for \(q<2\) has a negative answer, simultaneously for every \(0<q<2\), even when \(\mu\) has a continuous positive density bounded away from zero.

## Assumptions and scope
The Fourier transform is normalized by
\[
\widehat\varphi(\xi)=\int_{\mathbb R}\varphi(x)e^{-2\pi i x\xi}\,dx.
\]
A measure \(\sigma\) on \(\mathbb R\) is translation bounded when \(\sup_y |\sigma|(B(y,1))<\infty\). The Fourier transform of \(\mu\) is understood in the sense of tempered distributions. The pure-point measure displayed below is locally finite; its total variation is deliberately allowed to grow faster than every polynomial.

The construction answers the powered-mass question under the hypotheses of Boyvalenkov--Favorov's Theorem 2. It does not assert that the absolutely continuous \(\mu\) is crystalline, and it does not settle their separate question about tempered variation for crystalline measures.

## Proof
Start with the Rudin--Shapiro pair
\[
P_0(z)=Q_0(z)=1,
\]
\[
P_{r+1}(z)=P_r(z)+z^{2^r}Q_r(z),\qquad
Q_{r+1}(z)=P_r(z)-z^{2^r}Q_r(z).
\]
Induction shows that \(P_r\) and \(Q_r\) each have \(2^r\) coefficients, all in \(\{-1,1\}\). On the unit circle,
\[
|P_{r+1}(z)|^2+|Q_{r+1}(z)|^2
=2\bigl(|P_r(z)|^2+|Q_r(z)|^2\bigr),
\]
so
\[
|P_r(z)|^2+|Q_r(z)|^2=2^{r+1},\qquad
\|P_r\|_{L^\infty(\mathbb T)}\le \sqrt{2\,2^r}.
\]

For \(m\ge1\), set
\[
N_m=2^{m^2},\qquad a_m=2^{-m-4},\qquad
\eta_m=\frac{1}{8N_m},\qquad L_m=10m.
\]
Write
\[
P_{m^2}(z)=\sum_{j=0}^{N_m-1}\varepsilon_{m,j}z^j,
\qquad \varepsilon_{m,j}\in\{-1,1\},
\]
and define
\[
g_m(x)=\frac{a_m}{\sqrt{N_m}}\,
\operatorname{Re}\!\left(
 e^{2\pi i L_mx}P_{m^2}(e^{2\pi i\eta_mx})
\right).
\]
The Rudin--Shapiro bound gives
\[
\|g_m\|_\infty\le \sqrt2\,a_m.
\]
Since \(\sum_{m\ge1}a_m=1/16\), the series
\[
f(x)=1+\sum_{m=1}^\infty g_m(x)
\]
converges uniformly and
\[
1-\frac{\sqrt2}{16}\le f(x)\le 1+\frac{\sqrt2}{16}.
\]
Thus \(f\) is continuous and strictly positive, and \(\mu=f(x)\,dx\) is a positive translation-bounded measure of infinite total mass.

Put
\[
\lambda_{m,j}=L_m+j\eta_m,
\qquad 0\le j<N_m.
\]
Every positive block lies in
\[
[L_m,L_m+1/8),
\]
and distinct positive blocks are separated by more than nine units; the same is true for the reflected negative blocks. Expanding the real part yields, in the sense of distributions,
\[
\widehat\mu
=\delta_0+
\sum_{m=1}^\infty\sum_{j=0}^{N_m-1}
\frac{a_m\varepsilon_{m,j}}{2\sqrt{N_m}}
\bigl(\delta_{\lambda_{m,j}}+\delta_{-\lambda_{m,j}}\bigr).
\]
To justify this identity without any global absolute-summability assumption, take partial sums of \(f\). They converge uniformly, hence in tempered distributions. Against any compactly supported frequency test function, only finitely many separated blocks occur, so the Fourier transforms of the partial sums eventually stabilize to the displayed locally finite pure-point measure. Therefore that measure is precisely the distributional Fourier transform of \(\mu\).

Fix \(q>0\). The unit ball centered at \(L_m\) contains the entire positive \(m\)-th block and no other spectral block. Its \(\nu_q\)-mass is therefore
\[
\begin{aligned}
\nu_q(B(L_m,1))
&=N_m\left(\frac{a_m}{2\sqrt{N_m}}\right)^q\\
&=2^{-q}a_m^qN_m^{1-q/2}\\
&=2^{m^2(1-q/2)-qm-5q}.
\end{aligned}
\]
If \(0<q<2\), the positive quadratic term in the exponent dominates the linear term, so these unit-ball masses tend to infinity. Hence \(\nu_q\) is not translation bounded.

For \(q=2\), a whole nonzero block has mass
\[
N_m\left(\frac{a_m}{2\sqrt{N_m}}\right)^2
=\frac{a_m^2}{4}=2^{-2m-10}.
\]
Because the blocks are separated by more than two units, any unit ball meets at most one nonzero block; the ball around zero contributes only the unit atom. Thus \(\nu_2\) is translation bounded. Every nonzero coefficient has modulus less than one, so for \(q>2\),
\[
|b_\gamma|^q\le |b_\gamma|^2,
\]
and therefore \(\nu_q\le\nu_2\). Hence \(\nu_q\) is translation bounded for every \(q\ge2\), completing the proof.

## Verification
The accompanying `verify_q_threshold.py` reconstructs Rudin--Shapiro coefficient pairs through order ten, verifies exactly that their nonzero autocorrelations cancel pairwise (equivalent to the pointwise square-sum identity), checks the exact powered-block exponent for representative values below \(2\), verifies the \(q=2\) formula, and confirms the stated positivity margin. It returns `VERIFY_OK`.

These finite computations are supplementary. The infinite construction, distributional Fourier identity, and threshold \(q=2\) are established by the analytic argument above.

## Relationship to prior work
Boyvalenkov and Favorov prove that if a positive or translation-bounded measure has a pure-point distributional Fourier transform, then the measure obtained by squaring the Fourier masses is translation bounded. Their Remark 2 observes that the same holds for every exponent larger than \(2\) and explicitly asks whether an exponent smaller than \(2\) also works. The construction above gives a negative answer for every exponent smaller than \(2\) at once, and shows that their square exponent is an exact threshold even under the stronger hypothesis that the original measure has a positive continuous bounded density.

Rudin--Shapiro polynomials supply the flat finite Fourier blocks used in the construction. The new point is the scale-separated clustering with rapidly increasing block sizes and summable spatial amplitudes: uniform flatness keeps the density bounded while each subquadratic powered Fourier mass grows without bound on a fixed-radius ball.

The broader recent classification literature on Fourier summation formulas imposes growth or summability conditions that exclude this construction; here the total variation of the Fourier blocks grows superpolynomially, although cancellations keep the inverse transform uniformly bounded.

## Limitations
The example is one-dimensional and intentionally uses increasingly dense finite spectral clusters. It does not show failure for spectra satisfying a fixed separation or bounded local multiplicity condition. The original measure is absolutely continuous rather than crystalline, so no conclusion is drawn about subquadratic powered masses under additional two-sided discreteness assumptions. Targeted searches found no prior statement of this exact sharp-threshold counterexample, but unindexed folklore remains a residual originality risk.

## References
1. P. Boyvalenkov and S. Yu. Favorov, *Growth of masses of crystalline measures*, arXiv:2503.19567 (first public version 25 March 2025); Studia Mathematica 290 (2026), 109--119, DOI: 10.4064/sm250325-8-1.
2. W. Rudin, *Some Theorems on Fourier Coefficients*, Proceedings of the American Mathematical Society 10 (1959), 855--859, DOI: 10.1090/S0002-9939-1959-0116184-5.
3. F. Gonçalves and G. Vedana, *A Complete Classification of Fourier Summation Formulas on the real line*, arXiv:2504.02741.
