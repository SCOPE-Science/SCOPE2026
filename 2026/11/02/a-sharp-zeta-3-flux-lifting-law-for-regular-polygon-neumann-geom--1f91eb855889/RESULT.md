# A sharp \(\zeta(3)\) flux-lifting law for regular-polygon Neumann geometry

## Finding
Let a smooth circular Neumann boundary be replaced by its regular inscribed \(N\)-gon. The radially pulled-back *normal-flux defect*, after harmonic Neumann lifting on the unit disk, has the exact universal energy law
\[
\lim_{N\to\infty}N^3\int_D|\nabla v_N|^2\,dx
=2\zeta(3)\int_0^{2\pi}|f'(\theta)|^2\,d\theta.
\]
For nonconstant boundary trace \(f\), the corresponding energy norm is exactly asymptotic to \(\sqrt{2\zeta(3)}\,\|f'\|_{L^2}N^{-3/2}\). The coefficient depends only on the tangential boundary trace. This gives a quantitative benchmark for straight-sided Neumann geometric consistency, rather than a full finite-element error constant.

## Assumptions and scope
Write \(D=\{(r,\theta):0\le r<1\}\). For integer \(N\ge3\), the regular polygon \(P_N\) has vertices at angles \(2\pi(j+1/2)/N\); its side-normal rays are centered at \(2\pi j/N\). Let \(\delta_N=\pi/N\), and let \(\tau_N(\theta)\in[-\delta_N,\delta_N)\) be the representative of \(\theta-2\pi j/N\) in the cell containing \(\theta\). Its polygonal boundary has radial graph
\[
 r_N(\theta)=\frac{\cos\delta_N}{\cos\tau_N(\theta)}.
\]
Take any real-valued \(u\in C^2\) on a fixed open annular neighborhood of the unit circle, with \(\partial_r u(1,\theta)=0\), and set \(f(\theta)=u(1,\theta)\). No assumption that \(u\) is harmonic is needed. On each polygon side, let \(n_N\) be the exterior unit normal and define the pulled-back flux density (including the side-length Jacobian) by
\[
 G_N(\theta)=\partial_{n_N}u(r_N(\theta),\theta)\frac{ds_{\partial P_N}}{d\theta}
 =r_N(\theta)\partial_r u(r_N(\theta),\theta)
 -\tan\tau_N(\theta)\,\partial_\theta u(r_N(\theta),\theta).
\]
Define \(\bar G_N=(2\pi)^{-1}\int_0^{2\pi}G_N(\theta)\,d\theta\). Let \(v_N\in H^1(D)\) be the unique zero-mean harmonic function satisfying the weak Neumann datum \(\partial_r v_N|_{\partial D}=G_N-\bar G_N\) and \(\int_Dv_N=0\). The mean subtraction is required for Neumann solvability.

The exact same limit holds for the canonical radial extension \(u(r,\theta)=f(\theta)\) near the boundary with \(f\in H^{3/2}(\mathbb S^1)\), interpreted weakly; then \(G_N=-f'(\theta)\tan\tau_N(\theta)\). For this low-regularity formulation \(u\) need not be defined at the disk center.

## Proof
**1. Pullback identity and error.** The side has radial tangent \(r_N' e_r+r_Ne_\theta\), with \(r_N'/r_N=\tan\tau_N\). Since the outward normal is the side's midpoint radial direction, the side-length Jacobian is \(r_N\sec\tau_N\); substitution gives the displayed exact identity for \(G_N\). Uniformly in \(\theta\), \(r_N-1=O(N^{-2})\), \(|\tau_N|=O(N^{-1})\), and \(\partial_r u(1,\theta)=0\). Bounded second derivatives yield
\[
 \|G_N+f'\tan\tau_N\|_{L^2(\mathbb S^1)}=O(N^{-2}).
\]
Since \(\tan t-\sin t=O(t^3)\), it follows that for the periodic facet profile \(S_N(\theta)=\sin\tau_N(\theta)\),
\[
 \|G_N+f'S_N\|_{L^2(\mathbb S^1)}=O(N^{-2}).
\]
Mean subtraction preserves this estimate up to a fixed factor.

**2. Disk Neumann energy.** For real mean-zero boundary datum \(g\) with Fourier coefficients \(\widehat g(n)=(2\pi)^{-1}\int_0^{2\pi}g(\theta)e^{-in\theta}\,d\theta\), the harmonic lift is
\[
 v(r,\theta)=\sum_{n\ne0}\frac{\widehat g(n)}{|n|}r^{|n|}e^{in\theta},
 \qquad
 \int_D|\nabla v|^2\,dx=2\pi\sum_{n\ne0}\frac{|\widehat g(n)|^2}{|n|}.
\]
The second identity follows from Green's formula and Parseval. Hence the Neumann lifting operator sends mean-zero \(L^2\) boundary data into the energy space with norm bounded by \(\sqrt{2\pi}\) in the corresponding normalized Fourier convention. Consequently the \(O(N^{-2})\) correction in step 1 is negligible after multiplying the energy norm by \(N^{3/2}\).

**3. Facet Fourier coefficients.** Each cell has width \(2\delta_N\). Direct integration gives the sine series, convergent in \(L^2\),
\[
 S_N(\theta)=\sum_{k\ge1}b_{k,N}\sin(kN\theta),\qquad
 b_{k,N}=\frac{2(-1)^{k+1}kN}{(kN)^2-1}
 \frac{\sin(\pi/N)}{\pi/N}.
\]
Writing \(S_N=\sum_{k\ne0}a_{k,N}e^{ikN\theta}\) gives \(|a_{k,N}|=|b_{|k|,N}|/2\), and, for fixed nonzero integer \(k\),
\[
 \lim_{N\to\infty}N|a_{k,N}|=\frac1{|k|},\qquad
 |a_{k,N}|\le\frac{C}{N|k|}
\]
with a uniform constant for \(N\ge3\).

**4. No sideband collisions.** Initially assume \(h=f'\) is a trigonometric polynomial with Fourier frequencies \(|m|\le M\). For \(N>2M\), all frequencies \(kN+m\), with \(k\ne0\) and \(|m|\le M\), are distinct and nonzero. Therefore Parseval and step 2 give exactly
\[
 E_N(h):=\int_D|\nabla\mathcal N(S_Nh-\overline{S_Nh})|^2\,dx
 =2\pi\sum_{|m|\le M}|\widehat h(m)|^2
  \sum_{k\ne0}\frac{|a_{k,N}|^2}{|kN+m|},
\]
where \(\mathcal N\) denotes the zero-mean disk harmonic Neumann lift. Dominated convergence yields
\[
 \lim_{N\to\infty}N^3 E_N(h)
 =2\pi\sum_m|\widehat h(m)|^2\sum_{k\ne0}\frac1{|k|^3}
 =2\zeta(3)\|h\|_{L^2(\mathbb S^1)}^2.
\]

**5. Extension to the Sobolev endpoint.** Give Fourier Sobolev norms the weights \(1+|m|\). For every integer \(l\), triangle inequality implies \((1+|m|)(1+|m+l|)\ge1+|l|\), and therefore
\[
 \|e^{il\theta}h\|_{H^{-1/2}}\le(1+|l|)^{-1/2}\|h\|_{H^{1/2}}.
\]
Combined with the coefficient bound in step 3 this proves the uniform operator estimate
\[
 \sup_{N\ge3}N^{3/2}\|S_Nh\|_{H^{-1/2}}
 \le C\sum_{k\ne0}|k|^{-3/2}\|h\|_{H^{1/2}}.
\]
For a zero-mean datum the disk harmonic energy is bounded by a fixed multiple of its squared \(H^{-1/2}\) norm. Trigonometric polynomials are dense in \(H^{1/2}\), so the step-4 limit extends to all \(h\in H^{1/2}\), in particular to \(h=f'\) for \(f\in H^{3/2}\). For the smooth physical polygonal flux, step 1 transfers this leading law to \(G_N-\bar G_N\), completing the proof.

## Verification
The standalone standard-library script `verify_polygon_neumann.py` checks the closed facet coefficients against independent midpoint quadrature, compares the independently computed two-sideband energy with the exact single-mode series, tests the two-frequency limiting constant across refinements, and checks the size of the exact tangent-versus-sine flux correction. It reports 34 successful finite consistency checks. Numerical Fourier sums are not used as infinite-dimensional proof; the proof is in the five steps above.

For a radially constant extension with \(f(\theta)=\cos\theta\), the sine-profile surrogate admits the exact finite series
\[
 E_N^{\sin}=2\pi\left(\frac{\sin(\pi/N)}{\pi/N}\right)^2
 \sum_{k=1}^{\infty}\frac{(kN)^3}{((kN)^2-1)^3},
 \quad \lim_{N\to\infty}N^3E_N^{\sin}=2\pi\zeta(3).
\]
This gives a second check on all normalization factors.

## Relationship to prior work
Boffi and Gastaldi (arXiv:2610.31822v1, Sections 7 and 9 and the introduction) establish geometric consistency effects and an order \(h^{3/2}\) energy error barrier for straight-sided finite elements on piecewise smooth domains. Their treatment does not state the present regular-polygon normal-flux lifting functional, its sharp coefficient \(2\zeta(3)\), or the \(H^{3/2}\) trace endpoint. The classical disk Neumann-to-Dirichlet multiplier \(1/|n|\) and periodic Fourier analysis are ingredients, not claimed innovations. Ruas (arXiv:2607.07963) and Bertrand–Ruas (arXiv:2312.09098) study corrected natural boundary conditions on straight-edged meshes; available abstracts indicate numerical method error estimates rather than the particular exact regular-polygon functional. Their complete texts were not verified here, so historical equivalence remains possible.

## Limitations
This is an exact result for the disk, regular inscribed polygons and the radially pulled-back *isolated* polygonal normal-flux density, with mean removed. It does not identify an actual finite-element Galerkin error: interior consistency, domain integrals, variable coefficients, mesh discretization, and cancellation can change the full solution error, including superconvergence. The proof uses Fourier structure specific to uniform regular polygon facets; irregular polygons and three-dimensional polyhedra are not covered. The constant vanishes when \(f\) is constant; a positive \(N^{-3/2}\) asymptotic is asserted only for nonconstant trace. The low-regularity endpoint is for a radial extension, not arbitrary nonsmooth physical traces. Neither historical priority nor independent validation has been established.

## References
1. D. Boffi and L. Gastaldi, *Finite element approximation on piecewise smooth domains*, arXiv:2610.31822v1, first submitted October 22, 2026, https://arxiv.org/abs/2610.31822 (full manuscript inspected, especially Sections 7 and 9).
2. V. Ruas, *Off-site enforcement of natural conditions on smooth boundaries for finite elements upon fitted straight-edged triangular meshes*, arXiv:2607.07963, 2026, https://arxiv.org/abs/2607.07963 (abstract available; full-text access not confirmed).
3. F. Bertrand and V. Ruas, *A variant of the Raviart–Thomas method to handle smooth domains using straight-edged triangles. Part II — Approximation results*, arXiv:2312.09098, 2023, https://arxiv.org/abs/2312.09098 (abstract compared; full text not inspected).
