# Exact full linearization of a spherical Alexandrov–Fenchel flow
## Finding
Let \(n\ge 2\), \(0\le k\le n-1\), and let \(S_R\subset \mathbb S^{n+1}\) be a geodesic sphere of radius \(R\in(0,\pi/2)\). For the globally constrained flow
\[
\partial_tX=\left(\frac{\phi(t)}{F}-F\right)\nu,\qquad F=\frac{E_{k+1}}{E_k},\qquad \phi(t)=\frac{\int E_kF\,d\mu}{\int E_k/F\,d\mu},
\]
the full Fréchet linearization on an outward normal graph \(f\) over \(S_R\) is
\[
L_R f=\frac{2}{n}\Delta_{S_R}f+2\csc^2R\,(f-\bar f),
\]
where \(\bar f\) denotes the area average on \(S_R\). In particular, the full linearization is independent of the quotient index \(k\).

The degree-zero and degree-one spherical-harmonic eigenspaces have eigenvalue \(0\). They are precisely the infinitesimal directions obtained by varying the radius and center within the family of stationary geodesic spheres. For every harmonic degree \(\ell\ge2\),
\[
\lambda_\ell=2\csc^2R\left(1-\frac{\ell(\ell+n-1)}{n}\right)<0.
\]
Thus the exact spectral gap on shape modes is
\[
\frac{2(n+2)}{n\sin^2R},
\]
and is attained by degree-two harmonics.

## Assumptions and scope
The ambient space is the unit sphere \(\mathbb S^{n+1}\), the normal is the outward unit normal, and \(E_j=\binom{n}{j}^{-1}\sigma_j\). The statement concerns the Fréchet derivative of the nonlocal normal speed at a geodesic sphere, expressed in the usual normal-graph gauge. It is a linearized statement: it does not assert that every nonlinear solution has an asymptotic expansion with the displayed sharp exponent.

The restriction \(R\in(0,\pi/2)\) is the strictly convex range used by the source flow. The Laplacian convention is the geometric one for which a degree-\(\ell\) harmonic on \(S_R\) has eigenvalue \(-\ell(\ell+n-1)/\sin^2R\).

## Proof
Put \(c=\cot R\) and \(s=\sin R\). On \(S_R\), all principal curvatures equal \(c\), hence \(E_j=c^j\), \(F=c\), and \(\phi=c^2\), so every geodesic sphere is stationary.

For an outward normal variation with scalar height \(f\), the standard first-variation formula in the unit sphere gives
\[
\delta H=-\Delta_{S_R}f-n(c^2+1)f=-\Delta_{S_R}f-ns^{-2}f.
\]
At the umbilic curvature vector \((c,\ldots,c)\), symmetry and homogeneity give
\[
\frac{\partial E_j}{\partial\kappa_i}=\frac{j}{n}c^{j-1}.
\]
Differentiating \(F=E_{k+1}/E_k\) therefore yields
\[
\delta F=\frac1n\delta H=-\frac1n\Delta_{S_R}f-s^{-2}f.
\]
This is already independent of \(k\).

It remains to differentiate the global normalization. Write
\[
N=\int E_kF\,d\mu,\qquad D=\int E_k/F\,d\mu,\qquad \phi=N/D.
\]
At \(S_R\), the pointwise first variations are
\[
\delta(E_kF)=(k+1)c^k\delta F,
\qquad
\delta(E_k/F)=(k-1)c^{k-2}\delta F.
\]
The area-element variation contributes the same relative term to \(N\) and \(D\), so it cancels in \(\delta\log\phi\). Consequently
\[
\delta\phi=2c\,\overline{\delta F}=-2cs^{-2}\bar f,
\]
because the average of a Laplacian on the closed sphere vanishes. If \(V=\phi/F-F\) is the outward normal speed, then at the stationary sphere
\[
\delta V=\frac{\delta\phi}{c}-2\delta F
=\frac{2}{n}\Delta_{S_R}f+2s^{-2}(f-\bar f).
\]
This proves the stated full linearization.

For a degree-\(\ell\ge1\) spherical harmonic, \(\bar f=0\) and
\[
\Delta_{S_R}f=-\frac{\ell(\ell+n-1)}{s^2}f.
\]
Substitution gives the displayed \(\lambda_\ell\). Degree \(1\) gives zero, while the sequence is strictly decreasing for \(\ell\ge1\), so degree \(2\) is the least negative shape mode and gives the gap \(2(n+2)/(ns^2)\). Constants are annihilated directly by \(f-\bar f\), completing the spectrum description relevant here.

## Verification
The accompanying checker verifies, by exact rational combinatorics, the derivative \(\partial_iE_j=(j/n)c^{j-1}\), the cancellation of the \(k\)-dependent coefficients in the quotient derivative and in the normalization derivative, and the scaled harmonic eigenvalues for representative dimensions and every admissible quotient index. It also checks that degrees zero and one are neutral and that degree two is the slowest decaying shape mode.

The proof itself is analytic and all-dimensional. The finite checker is only a replay of algebraic identities; no infinite conclusion is inferred from sampling.

## Relationship to prior work
Luo, Wei, and Zhou introduce the displayed flow and prove global existence and smooth exponential convergence to a geodesic sphere for smooth strictly convex initial data. In their evolution section they explicitly identify a local spatial operator while noting that it is not the full linearization of the nonlocal equation. Their convergence theorem gives positive exponential constants depending on the initial hypersurface and parameters, but does not state the harmonic spectrum of the full nonlocal linearization or the quotient-index independence above.

Earlier spherical quermassintegral-preserving flows of Cabezas-Rivas and Scheuer, and of Albert-Niclòs, Cabezas-Rivas, and Pan, use different nonlocal speeds and hypotheses. They establish convergence to geodesic spheres but do not imply the full linearization of this quotient flow. Targeted searches for the source equation, its nonlocal linearization, spherical-harmonic spectrum, and the resulting gap did not locate a statement covering the formula above.

## Limitations
This result concerns only the linearization at stationary geodesic spheres. It does not upgrade the source's nonlinear convergence theorem to an exact nonlinear asymptotic rate, nor does it supply a nonlinear center-manifold or modulation theorem. The neutral degree-one space reflects the freedom to move the center by ambient isometries; fixing a center removes those gauge directions, while fixing the preserved quermassintegral removes the radius direction to first order.

## References
1. T. Luo, Y. Wei, and R. Zhou, *Alexandrov–Fenchel inequalities for convex domains in the sphere*, arXiv:2609.13829v1, 2026.
2. E. Cabezas-Rivas and J. Scheuer, *The quermassintegral-preserving mean curvature flow in the sphere*, Analysis & PDE 17 (2024), 3589–3621; arXiv:2211.17040.
3. S. Albert-Niclòs, E. Cabezas-Rivas, and S. Pan, *The quermassintegral preserving curvature flow for horo-convex hypersurfaces in the sphere*, arXiv:2608.10745v1, 2026.
