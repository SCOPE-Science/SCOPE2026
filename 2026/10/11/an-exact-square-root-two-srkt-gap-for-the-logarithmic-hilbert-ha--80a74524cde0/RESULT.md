# An exact square-root-two SRKT gap for the logarithmic Hilbert Hankel symbol

## Finding
For the analytic logarithmic symbol \(\psi(z)=-\log(1-z)\) on the unit disk, the associated Hardy Hankel operator and its normalized-kernel testing norm satisfy the exact strict inequality
\[
\sup_{w\in\mathbb D}\|H_{\overline\psi}k_w\|_2
=\|\psi\|_G=\frac\pi{\sqrt2}
<\pi=\|H_{\overline\psi}\|.
\]
The quotient of kernel-testing norm to operator norm is exactly \(1/\sqrt2\). The function \(\psi\in\mathrm{BMOA}_0\) is unbounded. In particular, this canonical infinite-rank Hankel operator fails the strong reproducing kernel thesis (SRKT). The exact gap is a benchmark, **not** a general impossibility theorem for unbounded SRKT symbols.

## Assumptions and scope
The Hardy space \(H^2=H^2(\mathbb D)\) is given its standard coefficient norm, and \(H^2_-:=L^2(\partial\mathbb D)\ominus H^2\). The Hankel operator is \(H_{\overline\psi}f=P_-(\overline\psi f)\), initially on polynomials. The normalized Szegő kernels are \(k_w(z)=\sqrt{1-|w|^2}/(1-\overline w z)\). The Poisson kernel is normalized to integrate to one on the circle. Define
\[
\Phi_\psi(w)=P(|\psi|^2)(w)-|\psi(w)|^2,
\qquad\|\psi\|_G^2=\sup_{w\in\mathbb D}\Phi_\psi(w).
\]
The dilogarithm \(\operatorname{Li}_2(z)=\sum_{n\ge1}z^n/n^2\) is used only with arguments of modulus at most one for which the series converges.

## Proof
**1. Exact Garsia seminorm.** Fix \(w\in\mathbb D\), and put \(\phi_w(z)=(w-z)/(1-\overline w z)\) and \(\eta=(1-\overline w)/(1-w)\), so \(|\eta|=1\). Changing harmonic measure by \(\phi_w\) gives
\[
\Phi_\psi(w)=\|\psi\circ\phi_w-\psi(w)\|_{H^2}^2.
\]
The logarithms can be chosen by analytic continuation from the origin, and the exact identity
\[
\psi(\phi_w(z))-\psi(w)
=\log(1-\overline w z)-\log(1+\eta z)
=\sum_{n\ge1}\frac{(-\eta)^n-\overline w^{\,n}}n z^n
\]
follows by factoring \(1-\phi_w(z)=(1-w)(1+\eta z)/(1-\overline w z)\). Therefore, writing \(r=|w|\),
\[
\Phi_\psi(w)=\frac{\pi^2}{6}+\operatorname{Li}_2(r^2)
-2\operatorname{Re}\operatorname{Li}_2(-\eta w).
\]
For each fixed \(0<r<1\), the function \(\theta\mapsto\operatorname{Re}\operatorname{Li}_2(re^{i\theta})\) decreases on \([0,\pi]\): differentiating the absolutely convergent series and using \(\operatorname{Li}_1(z)=-\log(1-z)\) gives derivative \(\operatorname{Arg}(1-re^{i\theta})<0\) in the interior. By conjugation symmetry, the smallest real part on the circle occurs at \(-r\). Consequently
\[
\Phi_\psi(w)\le\frac{\pi^2}{6}
+\operatorname{Li}_2(r^2)-2\operatorname{Li}_2(-r)
=\frac{\pi^2}{6}+2\operatorname{Li}_2(r).
\]
The final equality uses the even/odd series identity \(\operatorname{Li}_2(r)+\operatorname{Li}_2(-r)=\operatorname{Li}_2(r^2)/2\). For every positive real \(w=r\), \(\eta=1\), and equality holds. Sending \(r\uparrow1\), with \(\operatorname{Li}_2(1)=\pi^2/6\), shows
\[
\sup_{w\in\mathbb D}\Phi_\psi(w)=\frac{\pi^2}2.
\]
In particular \(\psi\in\mathrm{BMOA}_0\), even though its values diverge on approaching \(1\).

**2. Exact Hankel norm.** The coefficient of \(z^n\) in \(\psi\) is \(1/n\) for each \(n\ge1\). In the usual monomial bases the Hankel matrix is therefore \(\mathcal H_{jk}=1/(j+k+1)\) for \(j,k\ge0\). It is the positive Hilbert matrix. For completeness, the sharp norm \(\|\mathcal H\|=\pi\) follows directly as follows.

Set \(p_j=(j+1/2)^{-1/2}\). For any \(s>0\), \(F_s(t)=t^{-1/2}/(s+t)\) is convex on \((0,\infty)\). The midpoint-integral inequality and the elementary beta integral give
\[
\sum_{k\ge0}\mathcal H_{jk}p_k
=\sum_{k\ge0}F_{j+1/2}(k+1/2)
\le\int_0^\infty F_{j+1/2}(t)\,dt
=\pi p_j.
\]
By the symmetric Schur test, \(\|\mathcal H\|\le\pi\). For the reverse inequality, take \(x_j=(j+1)^{-1/2}\) for \(1\le j\le N\) and zero otherwise. Then \(\|x\|_2^2=\log N+O(1)\), and positivity gives
\[
\langle\mathcal Hx,x\rangle
\ge\int_2^{N+2}\!\int_2^{N+2}
\frac{du\,dv}{\sqrt{uv}(u+v)}.
\]
With \(u=e^s\), \(v=e^t\), the last integral becomes \(\int_0^{L}\int_0^L[2\cosh((s-t)/2)]^{-1}ds\,dt\), where \(L=\log((N+2)/2)\). Since this positive convolution kernel has total mass \(\pi\) and finite first moment, the integral equals \(\pi\log N+O(1)\). Thus the Rayleigh quotients tend to \(\pi\), proving \(\|H_{\overline\psi}\|=\pi\).

**3. Kernel testing.** For this Hankel operator, the Bonsall/Poisson identity \(\|H_{\overline\psi}k_w\|_2^2=\Phi_\psi(w)\) applies. Combining steps 1 and 2 proves the claim. The Hilbert matrix has infinite rank: each finite principal block is strictly positive definite, as \(\mathcal H_{jk}=\int_0^1t^{j+k}dt\) is the Gram matrix of linearly independent monomials.

## Verification
The accompanying `check_hilbert_garsia.py` numerically evaluates the automorphism Fourier-coefficient variance at several real and complex points, checks the exact real-radius dilogarithm sum, and computes increasing finite Hilbert-matrix Rayleigh lower bounds. Run `python3 check_hilbert_garsia.py`. These finite checks corroborate the formulas; the all-radii and infinite-dimensional conclusions are certified by the displayed analytic arguments, not the finite tests. Every normalizing factor in the Hardy norm and Poisson measure is stated above.

## Relationship to prior work
Dyakonov (2026, arXiv:2609.33242v1, Section 2, Problem 1) asks for structural conditions guaranteeing the SRKT and explicitly raises the separate existence question of an unbounded symbol obeying it. The present example is a quantitative **negative test** for that unbounded-symbol question, not an existence solution. The same paper establishes the Garsia/kernel-testing identity but does not calculate this logarithmic symbol's exact deficit. Brevig–Seip (arXiv:2301.07937v1) investigate maximal Hankel norms for bounded symbols; Dyakonov (arXiv:2404.05565v1) studies Garsia-extremal bounded functions and the geometry of the BMO ball. The current symbol is unbounded and gives a strict ratio for two distinct operator norms. Classification results restricted to finite-rank Hankel operators do not apply, because the Hilbert matrix has infinite rank.

## Limitations
The sharp ratio \(1/\sqrt2\) is asserted **only** for the specified logarithmic symbol. No universal inequality, classification of all unbounded SRKT symbols, or solution to the unbounded-example existence question is claimed. The literature overlap analysis cannot exclude unindexed older derivations of the same exact Garsia constant; the classic Hilbert-matrix norm itself is not claimed as new. No independent mathematical audit has been performed.

## References
1. K. M. Dyakonov, *The Strong Reproducing Kernel Thesis for Hankel Operators and the Garsia Norm*, arXiv:2609.33242v1 (2026), Section 2.
2. K. M. Dyakonov, *Extremal problems in BMO and VMO involving the Garsia norm*, arXiv:2404.05565v1 (2024), Sections 1–2.
3. O. F. Brevig and K. Seip, *Maximal norm Hankel operators*, arXiv:2301.07937v1 (2023), Sections 1–2.
4. F. F. Bonsall, *Boundedness of Hankel matrices*, Journal of the London Mathematical Society 29 (1984), 289–300; the Poisson/kernel identity is also derived by coefficient calculation above.
