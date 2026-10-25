# A conical eigenvalue crossing for eccentric Gaussian localization annuli

## Finding
In the analytic Bargmann–Fock space \(\mathcal F\), an exactly fixed-area family of annular localization domains has a **conical top-eigenvalue crossing** at every consecutive Hermite-mode tie. The cone's two slopes and its transverse coupling are explicit. In particular, moving the two circular boundaries relative to one another breaks the tie and increases the sharp concentration linearly in their center separation; translating both circles together does not.

For every integer \(k\ge1\) and width \(w>0\), put
\[
a=\frac{w}{e^{w/k}-1},\qquad b=a+w,\qquad C=a^ke^{-a}=b^ke^{-b},
\]
\[
\lambda_* = \frac{1}{(k-1)!}\int_a^b e^{-t}t^{k-1}\,dt,\qquad
\alpha=\frac{C}{(k-1)!}\left(\frac1b-\frac1a\right)<0,\qquad
\gamma=\frac{C}{\sqrt{(k-1)!k!}}>0.
\]
Let \(D_R(c)=\{z\in\mathbb C:|z-c|<R\}\). For real \(\tau\) and complex \(\delta\) sufficiently small, consider the eccentric annulus
\[
\Omega_{\tau,\delta}=D_{\sqrt{b+\tau}}(\delta)\setminus\overline{D_{\sqrt{a+\tau}}(0)},
\]
whose Euclidean area is exactly \(\pi w\). If \(T_{\tau,\delta}\) is the compression of multiplication by \(\mathbf1_{\Omega_{\tau,\delta}}\) to \(\mathcal F\), then
\[
\boxed{\ \|T_{\tau,\delta}\|
=\lambda_*+\frac{\alpha\tau}{2}
+\sqrt{\left(\frac{\alpha\tau}{2}\right)^2+\gamma^2|\delta|^2}
+O_{k,w}\!\left((|\tau|+|\delta|)^2\right).\ }
\]
The bound is locally uniform in the three real coordinates \(\tau\), \(\operatorname{Re}\delta\), and \(\operatorname{Im}\delta\). Consequently,
\[
\|T_{0,\delta}\|=\lambda_*+\gamma|\delta|+O_{k,w}(|\delta|^2),
\]
and the sharp one-sided radial derivatives at the concentric tie are \(\alpha\) for \(\tau\uparrow0\) and \(0\) for \(\tau\downarrow0\). Here the arrows refer to negative-side and positive-side approaches respectively.

More generally, if the outer and inner circle centers are \(c_o\) and \(c_i\), respectively, the entire norm depends only on \(|c_o-c_i|\), and the displayed expansion holds with \(\delta=c_o-c_i\). This is exact translation covariance, not merely a first-order approximation.

## Assumptions and scope
The Fock norm is
\[
\|F\|_{\mathcal F}^2=\frac1\pi\int_{\mathbb C}|F(z)|^2e^{-|z|^2}\,dA(z),
\]
with orthonormal monomials \(e_n(z)=z^n/\sqrt{n!}\), \(n\ge0\). The Toeplitz localization form is \(\langle T_\Omega F,F\rangle=\pi^{-1}\int_\Omega |F(z)|^2e^{-|z|^2}dA(z)\); its norm is the optimal captured fraction of Fock energy. The parameters satisfy \(k\in\{1,2,\ldots\}\), \(w>0\), \(a+\tau>0\) and \(|\delta|<\sqrt{b+\tau}-\sqrt{a+\tau}\), so the inner disk is strictly contained in the outer disk. The asymptotics hold as \((\tau,\delta)\to(0,0)\) with \(k,w\) fixed; no uniformity in \(k\) or \(w\) is asserted.

## Proof
**1. Exact radial spectrum and location of ties.** At \(\delta=0\) and \(\tau=0\), angular orthogonality gives diagonal entries
\[
\lambda_n(a,b)=\frac1{n!}\int_a^b e^{-t}t^n\,dt\qquad(n\ge0).
\]
Integration by parts yields the exact consecutive difference
\[
\lambda_{n+1}-\lambda_n=\frac{a^{n+1}e^{-a}-b^{n+1}e^{-b}}{(n+1)!}.
\]
The sign is positive, zero or negative according as \(n+1\) is less than, equal to or greater than the logarithmic mean \(L(a,b)=(b-a)/\log(b/a)\). Choosing \(a=w/(e^{w/k}-1)\) makes \(L(a,b)=k\), so \(\lambda_{k-1}=\lambda_k=\lambda_*\) and every other eigenvalue is **strictly smaller**. The top eigenvalue therefore has multiplicity exactly two and is separated by a positive spectral gap from the remaining compact spectrum. This purely radial preliminary is not the new claim.

**2. Trace-norm differentiability.** Define the normalized coherent kernel \(\psi_z(v)=\exp(v\overline z-|z|^2/2)\), whose Fock norm is one. For any bounded measurable set,
\[
T_\Omega=\frac1\pi\int_\Omega |\psi_z\rangle\langle\psi_z|\,dA(z)
\]
in trace norm. The map \(z\mapsto|\psi_z\rangle\langle\psi_z|\) is smooth in the trace-class norm. Translating the outer disk and changing both squared radii smoothly gives a two-real-parameter (indeed three-real-parameter) \(C^2\) expansion in trace norm, with a remainder bounded by a constant times \((|\tau|+|\delta|)^2\). Thus the first variation can legitimately be computed by differentiating the boundary-integral formula.

**3. The exact two-mode matrix.** Let \(P\) project onto \(\operatorname{span}\{e_{k-1},e_k\}\). The concentric radial parameter \(\tau\) changes \(\lambda_n\) by
\[
\partial_\tau\lambda_n\big|_0=\frac{e^{-b}b^n-e^{-a}a^n}{n!}.
\]
At the tie this is \(\alpha\) for \(n=k-1\) and zero for \(n=k\). For a real infinitesimal outer-center shift \(d\), the squared outer radius in polar direction \(\theta\) changes by \(2\sqrt b\,d\cos\theta\). The off-diagonal matrix element is therefore
\[
\left.\frac{d}{dd}\langle T_{0,d}e_k,e_{k-1}\rangle\right|_{d=0}
=\frac{e^{-b}b^k}{\sqrt{(k-1)!k!}}=\gamma.
\]
Rotation covariance gives the corresponding complex off-diagonal term \(\gamma\delta\) up to conjugation depending on basis convention. The diagonal entries have zero first derivative in \(\delta\), since its boundary variation has angular mean zero. Hence
\[
P(T_{\tau,\delta}-\lambda_* I)P
=\begin{pmatrix}\alpha\tau&\gamma\overline\delta\\
\gamma\delta&0\end{pmatrix}+O_{k,w}((|\tau|+|\delta|)^2)
\]
in operator norm.

**4. Reduction of the full operator.** The gap obtained in step 1 bounds the reduced resolvent on \((I-P)\mathcal F\). The Schur complement or the Riesz spectral projection perturbation theorem shows that the two perturbed eigenvalues near \(\lambda_*\) are, to uniform second-order error, the eigenvalues of the displayed two-by-two first-order matrix added to \(\lambda_* I\). Their larger member is exactly the square-root expression in the Finding. All other eigenvalues remain below it for sufficiently small perturbations. This proves the expansion for the full operator norm, not merely a finite-dimensional truncation.

**5. Geometric interpretation.** The Weyl translation \((W_cF)(z)=e^{z\overline c-|c|^2/2}F(z-c)\) is unitary and satisfies \(T_{\Omega+c}=W_c T_\Omega W_c^*\). Subtracting a common center shift therefore changes no eigenvalues. At \(\tau=0\) the radial splitting disappears, while the remaining off-diagonal term has modulus \(\gamma|c_o-c_i|\). This proves exact common-translation invariance and the claimed positive linear eccentricity cusp. The equal-area property follows immediately from the difference of the two disk areas, \(\pi[(b+\tau)-(a+\tau)]=\pi w\).

## Verification
A separate checker, `check_eccentric_annulus.py`, computes independent polar-grid quadratures of the displaced disk's Fock Gram matrix and compares the leading eigenvalue with the conical formula. It executed successfully with **92 deterministic numerical assertions**, including strict isolation of the tied top modes, convergence of the second-order remainder over three scales and finite-difference checks of off-diagonal coupling. Example at \(k=1,w=1\): \(a\approx0.5819767068693263\), \(b\approx1.5819767068693262\), \(\lambda_*\approx0.35322435680394887\), \(\alpha\approx-0.3532243568039489\), and \(\gamma\approx0.3252043381404272\). Numerical checks corroborate only finite-dimensional truncations; the infinite-dimensional result follows from the trace-norm and spectral-gap arguments above.

## Relationship to prior work
The Hermite diagonalization of Gaussian time–frequency localization on radial sets is classical (Daubechies, 1988). Dewage and Ólafsson (first public version July 3, 2021) give general radial Fock Toeplitz eigenvalue formulas, which already imply the radial gamma-integral difference and hence the location of concentric mode ties. The Gaussian Faber–Krahn inequality of Nicola and Tilli (first public version June 7, 2021) bounds all fixed-area localization norms and characterizes disk equality. Gómez, Guerra, Ramos and Tilli (first public version July 18, 2023) prove stability about the **single-eigenvalue disk optimum**. None of these inspected statements supplies the **two-center, doubly-degenerate, sharp linear eccentricity law at a non-disk annular tie**. The genuinely claimed addition is the conical unfolding with explicit coupling, exact area constraint and common-translation cancellation; no priority is claimed for radial diagonalization, the log-mean tie, or general spectral perturbation theory.

## Limitations
The result describes only a local fixed-area perturbation of an eccentric annulus near a consecutive top-mode tie. It does not identify a global maximizer over eccentric annuli, apply to general windows or dimensions, or provide bounds uniform as the mode index or annulus width varies. The coupling is exact at first order, not an exact formula at finite offset. Generic abstract perturbation principles make some ingredients standard; a previously published specialized calculation might imply the same explicit asymptotic. No independent mathematical audit has been performed.

## References
1. F. Nicola and P. Tilli, *The Faber–Krahn inequality for the Short-time Fourier transform*, arXiv:2106.03423v1 (June 7, 2021), Invent. Math. 230 (2022), 1–30, doi:10.1007/s00222-022-01119-8.
2. V. Dewage and G. Ólafsson, *Toeplitz operators on the Fock space with quasi-radial symbols*, arXiv:2107.01465v1 (July 3, 2021), Complex Anal. Oper. Theory 16 (2022), doi:10.1007/s11785-022-01208-9.
3. J. Gómez, A. Guerra, J. P. G. Ramos and P. Tilli, *Stability of the Faber–Krahn inequality for the Short-time Fourier Transform*, arXiv:2307.09304v1 (July 18, 2023).
4. I. Daubechies, *Time-frequency localization operators: a geometric phase space approach*, IEEE Trans. Inform. Theory 34 (1988), 605–612.
