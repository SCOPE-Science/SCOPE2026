# A unit-area annulus beats every disk for first-Hermite spectrogram concentration

## Finding

Fix the unit-normalized Gaussian \(h_0(t)=2^{1/4}e^{-\pi t^2}\) and the unit-normalized first Hermite function \(h_1(t)=2\sqrt\pi\,t h_0(t)\). For a measurable planar set \(E\) define the first-Hermite short-time Fourier concentration
\[
\Phi_1(E)=\sup_{\|f\|_{L^2(\mathbb R)}=1}\int_E |V_{h_1}f(x,\xi)|^2\,dx\,d\xi,
\qquad V_gf(x,\xi)=\int_{\mathbb R}f(t)\overline{g(t-x)}e^{-2\pi i\xi t}\,dt.
\]
Every Euclidean disk \(B\subset\mathbb R^2\) of Lebesgue area \(1\) satisfies the **exact** concentration identity
\[
\Phi_1(B)=1-\frac{2}{e}=0.264241117657\ldots.
\]
Set \(a_*=(e-1)^{-1}\) and let the concentric annulus of the same area be
\[
E_* = \{(x,\xi):a_*<\pi(x^2+\xi^2)<a_*+1\}.
\]
Then the explicitly normalized test signal \(f=h_0\) yields
\[
\Phi_1(E_*)\ge\int_{E_*}|V_{h_1}h_0|^2
=(1-e^{-1})e^{-1/(e-1)}=0.353224356804\ldots
>1-2/e.
\]
The improvement in captured signal energy is greater than \(33\%\) relative to the best disk. Moreover, among **all concentric annuli of area one**, \(E_*\) uniquely maximizes the energy captured from this fixed input \(h_0\). The theorem disproves any direct transfer of the Gaussian-window disk-maximization assertion to the first Hermite window; it does not claim global optimality of \(E_*\) over general sets or even over all annuli for freely varying signals.

## Assumptions and scope

The signal space is complex \(L^2(\mathbb R)\) with usual Lebesgue norm, \(V_g\) uses the \(2\pi\)-frequency convention displayed above, and both \(h_0,h_1\) have norm one. Time-frequency regions are measured by ordinary Euclidean area \(dx\,d\xi\). Disks may have any center; the exhibited annulus is centered at the origin, and covariance permits translating both the annulus and the associated input. The assertion concerns precisely the first excited Hermite window, not Gaussian-window STFT or higher-dimensional spaces.

## Proof

**1. Diagonalization of every centered disk.** Let \(h_m\), \(m\ge0\), be the normalized Hermite basis of \(L^2(\mathbb R)\). The true-polyanalytic Bargmann representation of \(V_{h_1}h_m\), after removal of a unit-modulus phase, is \(e^{-\pi|z|^2/2}\psi_m(z)\), where \(z=x+i\xi\) up to complex conjugation and
\[
\psi_0(z)=-\sqrt\pi\,\overline z,\qquad
\psi_m(z)=\frac{\pi^{(m-1)/2}}{\sqrt{m!}}z^{m-1}(m-\pi|z|^2),\quad m\ge1.
\]
Only absolute values and distinct angular exponents are used, so the harmless conjugation convention does not affect the argument. In polar coordinates with \(t=\pi|z|^2\), the corresponding radial probability densities are
\[
p_0(t)=t e^{-t},\qquad p_m(t)=\frac{t^{m-1}(m-t)^2}{m!}e^{-t}\quad(m\ge1).
\]
Their integrals on \([0,\infty)\) are \(1\) by the gamma factorial integrals. Distinct \(m\) have different angular frequencies \(m-1\), including the \(-1\) frequency for \(m=0\), so angular orthogonality makes the concentration quadratic form diagonal for every centered disk. Thus for \(B_T=\{\pi|z|^2<T\}\),
\[
\Phi_1(B_T)=\sup_{m\ge0}\lambda_m(T),\qquad
\lambda_m(T)=\int_0^T p_m(t)\,dt.
\]
This equality uses the completeness of the Hermite basis, not finite truncation.

**2. Exact disk spectrum at area one.** The normalized lower incomplete gamma tail is \(P(m,T)=1-e^{-T}\sum_{j=0}^{m-1}T^j/j!\) for \(m\ge1\). Direct integration yields
\[
\lambda_0(T)=1-(1+T)e^{-T},\qquad
\lambda_m(T)=P(m,T)+(m-1-T)e^{-T}T^m/m!\quad(m\ge1).
\]
Subtracting adjacent identities (or using the incomplete-gamma recurrence) gives for every \(m\ge0\), \(T>0\),
\[
\lambda_m(T)-\lambda_{m+1}(T)=
 e^{-T}\frac{T^m}{m!}\frac{(m-T)(m+1-T)}{m+1}.
\]
At \(T=1\), the differences with \(m=0,1\) vanish; all subsequent differences, with \(m\ge2\), are strictly positive. Direct integration yields
\[
\lambda_0(1)=\lambda_1(1)=\lambda_2(1)=1-2/e.
\]
Therefore the supremum over *all* Hermite modes equals \(1-2/e\) and is attained precisely on the three-dimensional span of \(h_0,h_1,h_2\). Every translated disk has the same concentration norm by Heisenberg covariance:
\[|V_{h_1}(M_{\xi_0}T_{x_0}f)(x,\xi)|=|V_{h_1}f(x-x_0,\xi-\xi_0)|.\]

**3. Optimized annular counterexample.** Since \(|V_{h_1}h_0(z)|^2=\pi|z|^2e^{-\pi|z|^2}\), every centered unit-area annulus has the form \(E_a=\{a<\pi|z|^2<a+1\}\), \(a\ge0\), and its captured fraction from \(h_0\) is
\[
G(a)=\int_a^{a+1}t e^{-t}\,dt
=(a+1)e^{-a}-(a+2)e^{-(a+1)}.
\]
Its derivative is \(G'(a)=e^{-a}[(a+1)e^{-1}-a]\), which changes sign exactly once on \([0,\infty)\), from positive to negative at \(a_*=(e-1)^{-1}\). Hence this is the **unique** maximizing annular placement for the specified test input, with \(G(a_*)=(1-e^{-1})e^{-a_*}\).

To prove the strict comparison without numerical approximations, put \(u=(e-2)^{-1}>0\). Then
\[
\log\frac{e-1}{e-2}=\log(1+u)>\frac{u}{1+u}=\frac1{e-1}=a_*,
\]
where strictness follows by integrating \(1/(1+t)>1/(1+u)\) over \(0\le t<u\). Exponentiating gives \(e^{-a_*}>(e-2)/(e-1)\), or equivalently
\[
G(a_*)> (1-e^{-1})\frac{e-2}{e-1}=1-2/e.
\]
This proves the claimed counterexample and constrained uniqueness.

## Verification

The accompanying `check.py` recomputes the disk eigenvalue formula and difference identity, independently integrates the radial densities numerically over several radii and up to Hermite index \(39\), verifies the equal-area annulus geometry and strict inequality, and checks both the exact expression and the optimized stationary point. Its finite calculations corroborate, but do not replace, the analytic proof for all infinitely many Hermite modes and all disk centers.

## Relationship to prior work

Abreu–Gröchenig (arXiv:1012.4283, first public 2010-12-20), §2, supplies the first-Hermite/polyanalytic Bargmann correspondence and Hermite-window normalization. The general radial Toeplitz eigenvalue formula in Maximenko–Tellería-Romero (arXiv:1905.00978, Proposition 6.3) gives a spectral integral for radial masks but does not make the optimized equal-area **annulus-versus-disk** comparison established here. Nicola–Tilli (arXiv:2106.03423, Theorem 1.1) proves that disks uniquely maximize **Gaussian-window** spectrogram concentration at fixed area; that theorem does not apply to the first Hermite window. Daubechies' 1988 circular-domain localization results use a Gaussian analysis window and do not imply the claimed non-Gaussian geometry. The comparison of both exact eigenvalue sequences and area-constrained annular optimization is the new element asserted here, rather than a new general diagonalization theorem.

## Limitations

The optimal annular location is proved only for the fixed normalized input \(h_0\), not for the operator norm over arbitrary inputs. There is no assertion of a global maximizing set among all measurable sets of area one, no uniqueness among unconstrained domains, and no theorem for other Hermite windows. The novelty conclusion is contingent on the searched and inspected literature; a more general, presently unidentified shape-optimization theorem might subsume the result. The proof is mathematical and computationally corroborated but has not undergone independent validation.

## References

1. L. D. Abreu and K. Gröchenig, *Banach Gabor frames with Hermite functions: polyanalytic spaces from the Heisenberg group*, arXiv:1012.4283 (2010), especially §2. https://arxiv.org/abs/1012.4283
2. E. A. Maximenko and A. M. Tellería-Romero, *Radial operators on polyanalytic Bargmann–Segal–Fock spaces*, arXiv:1905.00978 (2019), especially Theorem 1.2 and Proposition 6.3. https://arxiv.org/abs/1905.00978
3. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the short-time Fourier transform*, Invent. Math. 230 (2022), 1–30, arXiv:2106.03423. https://arxiv.org/abs/2106.03423
4. I. Daubechies, *Time-frequency localization operators: A geometric phase space approach*, IEEE Trans. Inf. Theory 34 (1988), 605–612, doi:10.1109/18.9761.
