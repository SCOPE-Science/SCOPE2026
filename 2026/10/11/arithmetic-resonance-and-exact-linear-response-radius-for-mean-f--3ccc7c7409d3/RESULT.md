# Arithmetic resonance and exact linear-response radius for mean-field expanding circle maps

## Finding
Fix any integer \(d\ge 2\), any positive integer \(k\), and any real coupling strength \(\varepsilon\). Let \(\mathbb T=\mathbb R/\mathbb Z\). For a probability density \(\rho\) on \(\mathbb T\), define
\[
M(\rho)=\int_{\mathbb T}\cos(2\pi x)\rho(x)\,dx,\qquad
f_\rho(x)=dx+\varepsilon M(\rho)\sin(2\pi kx)\pmod 1,
\]
and the self-consistent evolution \(\mathcal T_\varepsilon(\rho)=(f_\rho)_*(\rho\,dx)\). The uniform density \(\rho_*=1\) is fixed for every \(\varepsilon\).

The natural density linear-response operator \(L_\varepsilon\) at \(\rho_*\), acting on mean-zero \(C^1\) functions, has **exact spectral radius**
\[
\boxed{\quad
r(L_\varepsilon)=
\begin{cases}
\displaystyle \max\big\{d^{-1},\ (\pi d^{j-1}|\varepsilon|)^{1/j}\big\},&k=d^j\text{ for some integer }j\ge1,\\[3pt]
d^{-1},&\text{otherwise}.
\end{cases}\quad}
\]
In the resonant case \(k=d^j\), the \(j\) eigenvalues on the natural finite-dimensional harmonic subspace are exactly the roots of \(\lambda^j+\pi\varepsilon d^{j-1}=0\). In particular, the spectral radius is less than one for *all* real couplings in the nonresonant case; in the resonant case it is less than one exactly when \(|\varepsilon|<1/(\pi d^{j-1})\), equals one at the boundary, and exceeds one beyond it. All such statements concern the density **linearization**, not nonlinear attraction of probability densities or finite-population Lyapunov exponents.

## Assumptions and scope
A smooth density is understood as a nonnegative \(C^2\) function of integral one. The map \(f_\rho\) has degree \(d\) and is uniformly expanding whenever \(\rho\) lies sufficiently close to \(1\), with the permitted neighborhood depending on the fixed \(d,k,\varepsilon\). Thus its transfer action is defined near \(1\). For a smooth real mean-zero perturbation \(u\), first take the directional derivative of \(\mathcal T_\varepsilon(1+t u)\) at \(t=0\), and then extend the resulting bounded linear operator to
\[
X=\left\{u\in C^1(\mathbb T;\mathbb R):\int_{\mathbb T}u\,dx=0\right\},\qquad \|u\|_X=\|u'\|_\infty.
\]
The displayed norm is complete and equivalent to the ordinary \(C^1\) norm on \(X\); spectral radius is taken on the complexification. No Fréchet differentiability of the nonlinear operator as a self-map of \(C^1\) is assumed or claimed.

Let \(P_d u(x)=d^{-1}\sum_{h=0}^{d-1}u((x+h)/d)\), and let \(\ell(u)=\int_{\mathbb T}\cos(2\pi x)u(x)\,dx\). Then
\[
L_\varepsilon u=P_d u+\varepsilon\ell(u)g_{d,k},\qquad
g_{d,k}=\begin{cases}-2\pi(k/d)\cos(2\pi(k/d)x),&d\mid k,\\0,&d\nmid k.\end{cases}
\]

## Proof
**1. Linear-response formula and normalization.** For any smooth test function \(\varphi\) on the circle,
\[
\int\varphi\,\mathcal T_\varepsilon(1+tu)\,dx
=\int_\mathbb T\varphi\big(dx+t\varepsilon\ell(u)\sin(2\pi kx)\big)(1+tu(x))\,dx.
\]
Differentiation at zero gives \(\int\varphi P_d u\,dx+\varepsilon\ell(u)\int\varphi'(dx)\sin(2\pi kx)\,dx\). Averaging over the \(d\) inverse branches makes the last integral zero unless \(d\mid k\); when \(n=k/d\) is an integer, it equals \(\int\varphi'(y)\sin(2\pi ny)\,dy=-2\pi n\int\varphi(y)\cos(2\pi ny)\,dy\). This proves the displayed \(L_\varepsilon\), with no missing factor of \(d\) or \(2\).

**2. A sharp uncoupled scale.** Since \((P_d^tu)'=d^{-t}P_d^t(u')\), \(\|P_d^t\|_{X\to X}\le d^{-t}\). The functional satisfies
\[
|\ell(P_d^t u)|=\left|\int_\mathbb T\cos(2\pi d^t x)u(x)\,dx\right|\le\frac{d^{-t}}{2\pi}\|u'\|_\infty.
\]
For each \(t\) choose \(m>t+1\) and \(u_m(x)=\cos(2\pi d^m x)/(2\pi d^m)\). All first \(t\) iterates under \(L_\varepsilon\) coincide with those under \(P_d\), because the order-one cosine functional vanishes at all earlier stages. Hence \(\|u_m\|_X=1\) and \(\|L_\varepsilon^t u_m\|_X=d^{-t}\). The spectral-radius formula therefore always has the lower bound \(r(L_\varepsilon)\ge d^{-1}\).

**3. Harmonic-return equation.** If \(d\nmid k\), the claimed spectral radius follows immediately. Otherwise put \(n=k/d\). The functions \(P_d^ig_{d,k}\) are either single cosines of integer frequencies \(n/d^i\) or zero. The exact Duhamel expansion is
\[
L_\varepsilon^t u=P_d^t u+\varepsilon\sum_{i=0}^{t-1}\ell(L_\varepsilon^{t-1-i}u)P_d^ig_{d,k}.
\]
Write \(a_t=\ell(P_d^t u)\) and \(m_t=\ell(L_\varepsilon^t u)\). Applying \(\ell\) yields
\[
m_t=a_t+\varepsilon\sum_{i=0}^{t-1}m_{t-1-i}\,\ell(P_d^ig_{d,k}).
\]
The coefficient \(\ell(P_d^ig_{d,k})\) is nonzero only when \(n=d^i\), in which case it is \(-\pi n\). If \(k\) is not a positive power of \(d\), every such coefficient vanishes, so \(m_t=a_t\). Since only finitely many \(P_d^ig_{d,k}\) are nonzero and \(|a_t|\le d^{-t}\|u'\|_\infty/(2\pi)\), Duhamel gives \(\|L_\varepsilon^t\|_{X\to X}\le C_{d,k,\varepsilon}d^{-t}\). Together with Step 2 this gives the nonresonant radius exactly, at **every finite coupling strength**.

If \(k=d^j\), the moment identity instead reads
\[
m_t=a_t-\pi\varepsilon d^{j-1}m_{t-j}\quad(t\ge j),\qquad m_t=a_t\quad(0\le t<j).
\]
Writing \(c=-\pi\varepsilon d^{j-1}\), its exact solution is \(m_t=\sum_{h=0}^{\lfloor t/j\rfloor}c^h a_{t-jh}\). The bound on \(a_s\) gives \(|m_t|\le C(t+1)R^t\|u\|_X\), where \(R=\max\{d^{-1},|c|^{1/j}\}\). Since the Duhamel expansion uses only finitely many images of \(g_{d,k}\), it follows that \(\|L_\varepsilon^t\|_{X\to X}\le C'(t+1)R^t\), perhaps with an enlarged constant for small \(t\). Gelfand's formula yields \(r(L_\varepsilon)\le R\).

**4. Resonant eigenvalues and attainment.** When \(k=d^j\), the subspace
\[
H_j=\operatorname{span}\{\cos(2\pi x),\cos(2\pi d x),\ldots,\cos(2\pi d^{j-1}x)\}
\]
is invariant. For \(h\ge1\), \(L_\varepsilon\cos(2\pi d^h x)=\cos(2\pi d^{h-1}x)\), while \(L_\varepsilon\cos(2\pi x)=-\pi\varepsilon d^{j-1}\cos(2\pi d^{j-1}x)\). Therefore the characteristic polynomial of this cyclic companion block is \(\lambda^j+\pi\varepsilon d^{j-1}\). Its roots all have absolute value \(|\pi\varepsilon d^{j-1}|^{1/j}\), proving the remaining lower bound and hence equality. This completes the classification.

## Verification
The accompanying standalone `verify.py` uses exact rational Fourier coefficients, treating \(b=\pi\varepsilon\) as an exact rational input parameter. It checks first-variation Fourier updates, the finite-time Duhamel identity, resonant companion-block characteristic polynomials, the delayed moment equation, and nonresonant frequency nonreturn. Run from the extracted package with `python verify.py`; the recorded execution returned `VERIFY_OK exact_assertions=18167`. A separate periodic-grid directional test of the original nonlinear pushforward passed 25 numerical comparisons for five parameter combinations. These tests check algebra and normalization but **do not** certify an infinite-dimensional spectral radius; the proof above does.

## Relationship to prior work
Ahmad and Tanzi (2026) introduce observable Lyapunov exponents for globally coupled maps and relate macroscopic rates to linearizations of self-consistent transfer operators; their public abstract also gives weak-coupling decay results. This supplies the immediate motivation, but their full preprint was unavailable for a decisive theorem-by-theorem comparison. Tanzi's 2023 review develops the transfer-operator formalism for doubling maps and surveys weak-coupling contraction and coherent states. Castorrini, Galatolo and Tanzi (2025) prove general differential/spectral criteria and study a translation-type coupling for which the Lebesgue-state differential reduces to an uncoupled transfer operator; their Section 3.1 does not present this multiplicative sine/cosine harmonic family or its all-frequency arithmetic radius. Bahsoun, Froyland and Phalempin (2026) develop Fourier–Fejér and Newton numerical methods for nonlinear fixed points, rather than the exact resonance law stated here. The proof relies on known Perron–Frobenius and finite-rank-perturbation methods; originality, if confirmed, resides in the exact all-\((d,k,\varepsilon)\) harmonic-return classification.

## Limitations
This theorem is about the spectral radius of a specifically defined **linear-response operator**. It does not assert nonlinear convergence of the self-consistent map from nearby probability densities, a bifurcation at the crossing, stability of finite-size particle models, or equality with an observable Lyapunov exponent in any other functional setting. The spectral radius may depend on the chosen function space. A potentially relevant 2026 preprint could be inspected only at the abstract level, so priority against that full text remains unresolved; the exact novelty conclusion requires a subsequent literature audit. No independent mathematical audit has been performed.

## References
1. Masood Ahmad and Matteo Tanzi, *Observable Lyapunov Exponents for Globally Coupled Maps in the Mean-Field Limit*, arXiv:2609.27484, first posted 2026-09-23. https://arxiv.org/abs/2609.27484
2. Matteo Tanzi, *Mean-field coupled systems and self-consistent transfer operators: a review*, Bollettino dell'Unione Matematica Italiana 16 (2023), 297–336, https://doi.org/10.1007/s40574-023-00350-2
3. Roberto Castorrini, Stefano Galatolo, and Matteo Tanzi, *The Differential of Self-Consistent Transfer Operators and the Local Convergence to Equilibrium of Mean Field Strongly Coupled Dynamical Systems*, Journal of Nonlinear Science 35 (2025), article 78, https://doi.org/10.1007/s00332-025-10177-0; first arXiv posting 2024-07-12, arXiv:2407.09314.
4. Wael Bahsoun, Gary Froyland, and Maxence Phalempin, *Fixed-point approximation for self-consistent transfer operators with Newton's method*, arXiv:2605.08803, first posted 2026-05-09. https://arxiv.org/abs/2605.08803
