# Spectral saturation for geometric-lattice Hausdorff operators on BMOA and Bloch spaces

## Finding
Let \(0<t<1\) and let \(F(w)=\sum_{j=0}^{\infty}a_jw^j\) be nonconstant, with \(a_j\geq0\) and convergence on \(|w|<\rho\) for some \(\rho>t^{-1}\). Set \(\mu=\sum_{j\geq0}a_j\delta_{t^j}\), a finite positive measure on \((0,1]\). Write \(\mathcal H_\mu\) for the Hausdorff matrix operator on each of the analytic Banach spaces \(X=\mathrm{BMOA}\) and \(X=\mathscr B\) (the classical Bloch space). Then on **each** space

\[
\sigma(\mathcal H_\mu;X)=\sigma_{\mathrm{ess}}(\mathcal H_\mu;X)
 =F(\{w\in\mathbb C:|w|\le t^{-1}\}),\qquad
\sigma_{\mathrm p}(\mathcal H_\mu;X)=\varnothing.
\]

Here essential spectrum means failure of Fredholmness. More precisely, whenever \(0<|w|<t^{-1}\) and \(\lambda=F(w)\), the closure of the range of \(\lambda I-\mathcal H_\mu\) has **infinite codimension** in either \(X\). This is true even if distinct values of \(w\) have the same image under \(F\).

For example, \(t=1/2\) and \(\mu=\delta_{1/2}+\delta_{1/4}\) give the exact common ordinary and Fredholm essential spectrum \(\{w+w^2:|w|\le2\}\), with no eigenvalues, on both spaces.

## Assumptions and scope
For a finite positive measure \(\mu\) on \((0,1]\), the Hausdorff operator is induced on Taylor coefficients by

\[
 c_{n,k}=\binom nk\int_{(0,1]}u^k(1-u)^{n-k}\,d\mu(u),\quad
 (\mathcal H_\mu f)(z)=\sum_{n\ge0}\left(\sum_{k=0}^n c_{n,k}\widehat f(k)\right)z^n.
\]

Equivalently, for an atom at \(u\in(0,1]\),

\[
 (H_uf)(z)=\frac{f\!\left(uz/[1-(1-u)z]\right)}{1-(1-u)z}.
\]

The Bloch norm is \(|f(0)|+\sup_{|z|<1}(1-|z|^2)|f'(z)|\); BMOA has its usual analytic mean-oscillation norm. The measure is supported on the geometric multiplicative lattice \(\{1,t,t^2,\ldots\}\), and the analytic-radius assumption is **strict**. It includes every nonconstant finite positive atomic combination of these points. It does not cover arbitrary atomic support or the limiting case where the radius of convergence is exactly \(t^{-1}\).

## Proof
**1. Semigroup reduction and spectral upper bound.** The fractional-linear maps in the formula satisfy \(H_uH_v=H_{uv}\), so \(H_t^j=H_{t^j}\), with \(H_1=I\). These operators are bounded on BMOA and Bloch. In fact there is a constant \(C_X\), independent of \(0<u\le1\), such that

\[
 \|H_u\|_{X\to X}\le C_X/u.
\]

For BMOA this follows from the preadjoint composition operator \(A_u f=f(uz+1-u)\) on \(H^1\) and the classical subordination estimate \(\|A_u\|_{H^1\to H^1}\le(2-u)/u\). For Bloch use the preadjoint \(B_u=JA_uJ^{-1}\) on Bergman \(A^1\), where \(Jf=(zf)'\) is a bounded isomorphism from \(D^1=\{f:f'\in A^1\}\) to \(A^1\). To see the scale explicitly, the change of variables \(v=1-u+uz\) gives \(\|(f\circ\psi_u)'\|_{A^1}\le u^{-1}\|f'\|_{A^1}\), while the Bergman evaluation estimate gives \(|f(1-u)|\le|f(0)|+u^{-1}\|f'\|_{A^1}\). Thus \(\|A_u\|_{D^1\to D^1}\le C/u\), and the stated Bloch bound follows by duality. All duality and identification statements are documented in the cited primary article [1].

Consequently the spectral-radius formula gives

\[
 r(H_t;X)=\lim_{j\to\infty}\|H_t^j\|^{1/j}\le t^{-1}.
\]

**2. Entire open disk belongs to the Fredholm essential spectrum.** On the Hardy predual \(H^1\), \(A_tg(z)=g(1-t+tz)\). For every complex \(s\) with \(\operatorname{Re}s>-1\), the analytic function \(g_s(z)=(1-z)^s\) belongs to \(H^1\) and obeys \(A_tg_s=t^sg_s\). On the Bergman predual \(A^1\), \(Jg_s\) belongs to \(A^1\) and obeys \(B_t(Jg_s)=t^sJg_s\). Indeed \(g_s'=-s(1-z)^{s-1}\in A^1\) for \(\operatorname{Re}s>-1\), including the constant case \(s=0\).

Fix any \(w\ne0\) with \(|w|<t^{-1}\). All solutions

\[
 s_k=\frac{\log w+2\pi i k}{\log t},\qquad k\in\mathbb Z,
\]

have \(\operatorname{Re}s_k>-1\), and \(t^{s_k}=w\). The corresponding Hardy functions \(g_{s_k}\), and their images under \(J\), are linearly independent: after the change of variable \(v=\log(1-z)\) this is independence of exponentials with distinct exponents on an open set. Thus the preadjoint of \(H_t\) has an infinite-dimensional eigenspace for each such \(w\). The dual pairings give infinite independent continuous functionals annihilating the range of \(\lambda I-H_t\) for every \(0<|\lambda|<t^{-1}\) (conjugate the eigenparameter where dictated by the sesquilinear pairing). Hence that range has infinite-codimensional closure. Since the Fredholm essential spectrum is closed, it contains the entire closed disk. Combined with Step 1, this proves

\[
 \sigma(H_t;X)=\sigma_{\mathrm{ess}}(H_t;X)
 =\{w:|w|\le t^{-1}\}.
\]

**3. No point spectrum.** Suppose \(H_tf=\lambda f\), with nonzero \(f\) analytic on the disk. Near zero use \(v=z/(1-z)\), so \(z=v/(1+v)\), and put \(G(v)=f(v/(1+v))/(1+v)\). The identity for \(H_t\) becomes \(G(tv)=\lambda G(v)\). Comparing Taylor coefficients shows that \(\lambda=t^k\) for some integer \(k\ge0\) and \(G(v)=cv^k\); hence \(f(z)=cz^k/(1-z)^{k+1}\). Every nonzero such \(f\) fails the Bloch derivative bound as \(z\to1^-\), and BMOA embeds into Bloch. Thus \(\sigma_{\mathrm p}(H_t;X)=\varnothing\).

**4. Holomorphic spectral mapping for a geometric lattice.** The growth bound in Step 1 ensures convergence in operator norm of \(\sum_{j\ge0}a_jH_t^j\). Coefficient identities then give \(\mathcal H_\mu=F(H_t)\). The convergence radius exceeds \(t^{-1}\), so holomorphic spectral mapping applies both in \(\mathcal B(X)\) and in its quotient by the compact operators. Step 2 therefore gives the two asserted spectral equalities. For any \(\lambda\in\mathbb C\), analyticity and nonconstancy imply that \(F(z)-\lambda\) has finitely many zeros in a neighborhood of the compact spectrum. Factoring those zeros in the holomorphic functional calculus leaves an invertible factor times a finite product of injective operators \(H_t-\zeta I\). Step 3 makes that product injective, so \(F(H_t)\) has no eigenvalues. Finally, if \(\lambda=F(w)\) for \(0<|w|<t^{-1}\), the infinitely many predual eigenvectors from Step 2 are also eigenvectors of \(F(A_t)\) or \(F(B_t)\) with eigenvalue \(F(w)\); this gives the asserted infinite-codimension conclusion.

## Verification
The proof is infinite-dimensional and does not rely on a numerical extrapolation. A standalone exact-rational coefficient diagnostic is provided as `verification/checker.py`. Running `python verification/checker.py` gives `PASS: 21360 exact rational coefficient assertions`, checking semigroup multiplication, formal eigenvector coefficient identities, and a two-atom Hausdorff polynomial on multiple finite truncations. The spectral-radius, infinite-multiplicity and holomorphic-calculus steps are analytical, not finite-data consequences.

## Relationship to prior work
Galanopoulos, Mahillo, Oliva-Maza and Siskakis [1] determine the spectrum and Fredholm essential spectrum of positive Hausdorff operators on BMOA and Bloch **provided** their Mellin transforms belong to the extended Dunford–Riesz class. For the present measures, \(\mathcal M\mu(z)=F(t^{z-1})\) is nonconstant and periodic in the imaginary direction, and therefore does not have the required limit at infinity on any sector of aperture greater than a half-plane. Their condition is not met; the present interior Fredholm collapse does not follow by substituting these measures into their spectral formula. The proof does use their established duality framework [1].

Abadias and Oliva-Maza [2] develop broader semigroup-based spectral methods for Hausdorff-type operators on Hardy, Bergman, Dirichlet, and little Korenblum spaces. Their accessible abstract does not establish the BMOA/Bloch geometric-lattice claim above; a full-text comparison was not available, so priority remains uncertain. Earlier results on invertible weighted composition operators [3] concern disk automorphisms, whereas \(z\mapsto tz/[1-(1-t)z]\) for \(0<t<1\) is not an automorphism. Deddens [4] concerns sequence \(\ell^2\), not these function spaces. Galanopoulos and Papadimitrakis [5] characterize bounded Hausdorff operators on these function spaces rather than this spectral geometry.

## Limitations
The radius assumption \(\rho>t^{-1}\) is used for holomorphic spectral mapping; no claim is made at equality or for incommensurable atomic supports. The proof does not classify the fine spectrum at all boundary points or provide resolvent norm asymptotics. Published spectral-calculus literature may contain equivalent or stronger versions not identified from accessible full text, particularly [2].

## References
[1] P. Galanopoulos, A. Mahillo, J. Oliva-Maza and A. G. Siskakis, *Hausdorff Matrices on the BMOA and Bloch spaces*, arXiv:2610.22554v1, submitted 2026-10-15, Sections 1–4, especially Theorems 1.1–1.2 and Lemmas 3.7, 4.9–4.12. https://arxiv.org/html/2610.22554v1

[2] L. Abadias and J. Oliva-Maza, *Spectral sets of generalized Hausdorff matrices on spaces of holomorphic functions on the disk*, Journal of Functional Analysis **286** (2024), 110298, DOI:10.1016/j.jfa.2023.110298. Abstract and repository first-page preview consulted; full paper unavailable during this review.

[3] T. Eklund, M. Lindström and P. Mleczko, *Spectral properties of weighted composition operators on the Bloch and Dirichlet spaces*, Studia Mathematica **232** (2016), 95–112, DOI:10.4064/sm8310-3-2016.

[5] P. Galanopoulos and M. Papadimitrakis, *Hausdorff and Quasi-Hausdorff Matrices on Spaces of Analytic Functions*, Canadian Journal of Mathematics **58** (2006), 548–579, DOI:10.4153/CJM-2006-023-5. Full primary text, especially the introductory characterization and scope, consulted.

[4] J. A. Deddens, *On spectra of Hausdorff operators on* \(\ell^2\), Proceedings of the American Mathematical Society **72** (1978), 74–76, DOI:10.1090/S0002-9939-1978-0500207-7.
