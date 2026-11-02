# Gaussian second-moment Fourier extension: migrating angular extremizers and sharp spectral stability

## Finding
Let \(E\) denote extension from the unit circle in \(\mathbb R^2\), normalized as below. Weight its squared Euclidean norm by \(|x|^2 e^{-t|x|^2}\), with \(t>0\), and put \(z=(2t)^{-1}\). The exact spectral multiplier on angular frequency \(m\in\mathbb Z\) is
\[
\lambda_{|m|}(z)=2z^2e^{-z}\big[(|m|+1-z)I_{|m|}(z)+zI_{|m|+1}(z)\big],
\]
where \(I_n\) is the modified Bessel function of the first kind. Its trace is exactly \(2z^2\). For all \(z>0\), the optimal squared extension norm \(C_z\) is the attained maximum of these multipliers.

The following conclusions hold.

1. For \(0<z\le 1/4\), the only extremizers are nonzero constant functions. At \(z=1\), constant functions are not extremizers.
2. The **uniform all-frequency Gaussian spectral law** is
\[
\lim_{z\to\infty}\sup_{n\ge0}\left|\frac{\lambda_n(z)}{z^{3/2}}-\frac{1+(n/\sqrt z)^2}{\sqrt{2\pi}}e^{-n^2/(2z)}\right|=0.
\]
Consequently,
\[
 C_z\sim\frac{2e^{-1/2}}{\sqrt{2\pi}}z^{3/2},\qquad
 \frac{n_z}{\sqrt z}\longrightarrow1
\]
for **every** choice of maximizing index \(n_z\in\operatorname*{argmax}_{n\ge0}\lambda_n(z)\).
3. For every \(\varepsilon>0\), there are \(c_\varepsilon>0\) and \(z_\varepsilon<\infty\) such that for all \(z\ge z_\varepsilon\) and all \(f=\sum_{m\in\mathbb Z}c_m e^{im\theta}\),
\[
C_z\|f\|_{L^2(\mathbb S^1)}^2-\mathcal Q_z(f)\ \ge\ c_\varepsilon z^{3/2}
\sum_{\substack{m\in\mathbb Z:\big||m|/\sqrt z-1\big|\ge\varepsilon}}|c_m|^2.
\]
Thus any sequence of normalized asymptotic extremizers has angular energy concentrated in an arbitrarily thin relative window around \(|m|=\sqrt z\).

## Assumptions and scope
Use \(d\theta/(2\pi)\) on \(\mathbb S^1\) and \(dx/(2\pi)\) on \(\mathbb R^2\). For \(f\in L^2(\mathbb S^1)\) define
\[
(Ef)(x)=\frac1{2\pi}\int_0^{2\pi}e^{i x\cdot(\cos\theta,\sin\theta)}f(\theta)\,d\theta,
\quad
\mathcal Q_z(f)=\frac1{2\pi}\int_{\mathbb R^2}|Ef(x)|^2|x|^2e^{-|x|^2/(2z)}\,dx.
\]
Define \(C_z=\sup_{\|f\|_2=1}\mathcal Q_z(f)\). The quadratic form is finite for every \(z>0\), the positive associated operator is trace class, and the supremum is attained. All statements concern integer angular frequencies on this circle and fixed Gaussian second-moment observation; no claim is made about arbitrary radial weights or higher-dimensional spheres.

## Proof
**Diagonalization and exact coefficients.** By the Jacobi–Anger expansion, for the orthonormal basis \(e_m(\theta)=e^{im\theta}\),
\[(Ee_m)(r,\phi)=i^m J_m(r)e^{im\phi}.\]
Angular orthogonality and Tonelli give
\[\mathcal Q_z(f)=\sum_{m\in\mathbb Z}\lambda_{|m|}(z)|c_m|^2,\qquad
\lambda_n(z)=\int_0^\infty r^3e^{-r^2/(2z)}J_n(r)^2\,dr>0.\]
Weber's second exponential integral (DLMF 10.22.67) implies, with \(t=(2z)^{-1}\),
\[\int_0^\infty re^{-tr^2}J_n(r)^2\,dr=z e^{-z}I_n(z).\]
Differentiating with respect to \(t\), justified by dominated convergence for \(t>0\), yields
\[\lambda_n(z)=2z^2\frac{d}{dz}\big(ze^{-z}I_n(z)\big).
\]
Use \(zI_n'(z)=nI_n(z)+zI_{n+1}(z)\) to obtain the stated closed form. Also \(\sum_{m\in\mathbb Z}J_m(r)^2=1\) yields
\[\sum_{m\in\mathbb Z}\lambda_{|m|}(z)=\int_0^\infty r^3e^{-r^2/(2z)}dr=2z^2.\]
Positivity and summability imply attainment of the largest multiplier at a finite angular degree.

**The finite-parameter symmetry change.** Write \(B_n(z)=(n+1-z)I_n(z)+zI_{n+1}(z)\). The nonnegative series for \(I_n\) gives
\[I_n(z)\le\frac{(z/2)^n}{n!}I_0(z)\qquad(n\ge0,z>0).\]
For \(0<z\le1/4\) and \(n\ge1\), it follows that
\[ B_n(z)\le I_0(z)\left(z+\frac{z^3}{8}\right)
 <(1-z)I_0(z)\le B_0(z).\]
Indeed \((n+1)(z/2)^n/n!\le z\) and \(z(z/2)^{n+1}/(n+1)!\le z^3/8\) in this range. Thus the zero mode alone maximizes. At \(z=1\), \(B_0(1)=I_1(1)\) and \(B_1(1)=I_1(1)+I_2(1)>B_0(1)\), so the maximizer is nonconstant.

**Uniform spectral limit.** The Fourier representation
\[e^{-z}I_n(z)=\frac1{2\pi}\int_{-\pi}^{\pi}e^{-z(1-\cos\theta)}\cos(n\theta)\,d\theta\]
combined with the derivative formula, after \(y=\sqrt z\,\theta\), gives
\[
\frac{\lambda_n(z)}{z^{3/2}}=\frac1\pi\int_{\mathbb R}G_z(y)\cos\big(ny/\sqrt z\big)\,dy,
\]
where
\[
G_z(y)={\bf1}_{\{|y|\le\pi\sqrt z\}}
\big[1-z(1-\cos(y/\sqrt z))\big]e^{-z(1-\cos(y/\sqrt z))}.
\]
For \(|y|\le\pi\sqrt z\), \(2y^2/\pi^2\le z(1-\cos(y/\sqrt z))\le y^2/2\). Thus
\[|G_z(y)|\le(1+y^2/2)e^{-2y^2/\pi^2},\]
an integrable dominating function. Pointwise, \(G_z(y)\to(1-y^2/2)e^{-y^2/2}=:G(y)\). Dominated convergence gives \(\|G_z-G\|_1\to0\). Since the absolute Fourier-transform difference is bounded by \(\|G_z-G\|_1/\pi\) **uniformly over real frequencies**, the law holds uniformly over all nonnegative integers \(n\). The Gaussian Fourier transform computes
\[\frac1\pi\int_{\mathbb R}G(y)\cos(uy)dy=\frac{1+u^2}{\sqrt{2\pi}}e^{-u^2/2}.\]

**Sharp maximum and stability.** The profile \(\Phi(u)=(1+u^2)e^{-u^2/2}\), for \(u\ge0\), has derivative \(\Phi'(u)=u(1-u^2)e^{-u^2/2}\); its unique global maximum is \(\Phi(1)=2e^{-1/2}\). The discrete grid \(\{n/\sqrt z:n\ge0\}\) approaches \(1\) as \(z\to\infty\). Uniform convergence therefore gives both the sharp norm asymptotic and \(n_z/\sqrt z\to1\) for every maximizing index. For any \(\varepsilon>0\), set
\[d_\varepsilon=\frac1{\sqrt{2\pi}}\left[\Phi(1)-\sup_{\substack{u\ge0:\,|u-1|\ge\varepsilon}}\Phi(u)\right]>0.\]
Uniform convergence supplies \(C_z-\lambda_n(z)\ge d_\varepsilon z^{3/2}/3\) for every excluded index once \(z\) is sufficiently large. Summing this scalar inequality against \(|c_m|^2\) proves stability with \(c_\varepsilon=d_\varepsilon/3\). If the relative quadratic-form deficit tends to zero, the normalized Fourier mass outside each window tends to zero.

## Verification
The file `check.py` verifies the exact integral-to-Bessel formula against numerical quadrature at multiple parameters, the finite symmetry change, trace normalization by sufficiently long partial sums, the uniform spectral profile on bounded scaled grids, and convergence of maximizing frequencies. It is a **finite numerical cross-check**, not the proof of the uniform or infinite-dimensional claims. Reproduce with Python 3 and SciPy via `python check.py`. The analytical argument above covers all \(z>0\) and all integers \(m\).

## Relationship to prior work
Negro and Oliveira e Silva (first publicly posted 2021-07-29) give sharp Agmon–Hörmander Fourier-extension estimates for **hard Euclidean balls**, where the maximizing spherical harmonic degree is among \(0\) and \(1\). Their theorem handles the sharp ball cutoff, not the present smooth radial multiplier \(|x|^2e^{-|x|^2/(2z)}\), whose maximizing degree diverges like \(\sqrt z\). DLMF 10.22.67 contains the classical Weber integral used to calculate the coefficients, but does not yield the sharp extremizing-degree law or global stability inequality by itself. The uniform all-degree Fourier analysis and the contrast between constant-mode and migrating-mode maximizers constitute the additional claim. Searches for Gaussian radial Fourier extension, modified-Bessel mode maximizers and weighted Agmon–Hörmander estimates did not locate the same result, but absence from searches cannot certify historical priority.

## Limitations
The result determines the large-\(z\) maximizer scale, not the full exact sequence of finite-\(z\) switching thresholds or uniqueness at every finite parameter. Gaussian second-moment weights and the planar unit circle are essential in the current proof. Potential coverage by a general theorem for arbitrary radial weights remains a historical-priority risk; no such implication was identified in the inspected sources.

## References
1. G. Negro and D. Oliveira e Silva, *Intermittent symmetry breaking and stability of the sharp Agmon–Hörmander estimate on the sphere*, arXiv:2107.14273, first posted 2021-07-29, especially Theorem 1 and Section 2. https://arxiv.org/abs/2107.14273 . Author-posted full-text copy: https://www.researchgate.net/publication/353635170_Intermittent_symmetry_breaking_and_stability_of_the_sharp_Agmon--Hormander_estimate_on_the_sphere .
2. NIST Digital Library of Mathematical Functions, §10.22(iv), equation 10.22.67 (Weber's second exponential integral). https://dlmf.nist.gov/10.22.E67 .
3. E. W. Weisstein, *Weber's Formula*, MathWorld, https://mathworld.wolfram.com/WebersFormula.html .
