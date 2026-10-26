# Exact mesoscopic Fourier resonances in a positivity-preserving periodic elliptic stencil

## Finding

The periodic four-branch expectation-based elliptic stencil has an exact, arithmetic family of undamped nonconstant Fourier modes at commensurate meshes. For \(N=k^2\) nodes per coordinate and physical step \(h=1/N\), its averaging symbol is
\[
\Lambda_k(a,b)=\cos(2\pi a/k)\cos(2\pi b/k).
\]
The \(+1\) eigenspace has dimension \(k^2\) when \(k\) is odd and \(2k^2\) when \(k\) is even. For fixed reaction \(r>0\), the discrete elliptic matrix has exactly determined spectral condition number
\[
\kappa_2=1+\frac{(1+b_k)k^2}{r},\qquad
b_k=\begin{cases}\cos(\pi/k),&k\text{ odd},\\1,&k\text{ even}.\end{cases}
\]
These nonconstant \(+1\) modes are not damped by the averaging step, despite positive definiteness of the reaction-elliptic system matrix. A smooth resolved forcing whose wavelength is the jump length has an exact nodal solution error tending to \(1/r\), as proved below.

## Assumptions and scope

Fix any integer \(k\ge2\), set \(N=k^2\), and consider the unit flat torus with independent nodes \((i/N,j/N)\), indexed by \(i,j\in\mathbb Z_N\); duplicated periodic endpoints are identified. Use the spatial mesh width \(h=1/N\) also as the step in the stochastic quadrature. Take the periodic scheme of Xu, Li and Yue [1, Eq. (22)] with diffusion coefficients \(\sigma_1=\sigma_2=1\), correlation \(\rho=0\), drift \(B=0\), and spatially constant reaction \(r>0\). This is a uniformly elliptic constant-coefficient specialization, with four equiprobable branch endpoints. The displacement \(\sqrt h=1/k=k/N\) is exactly \(k\) mesh cells in each coordinate, so bilinear interpolation coincides with nodal evaluation. Define
\[
(P_k v)_{ij}=\frac14\sum_{\varepsilon,\eta\in\{-1,1\}}v_{i+\varepsilon k,j+\eta k},
\qquad A_{k,r}=I-\frac{1}{1+rh}P_k,
\]
with indices modulo \(N\). For nodal forcing \(Q\), the elliptic equation to solve is \(A_{k,r}U=hQ\). Its matrix is a positive-definite symmetric nonsingular M-matrix (off-diagonal entries are nonpositive). The spectral condition number is in Euclidean norm. All statements describe the unique exact solution of the linear system, not the result of a finite number of solver iterations.

## Proof

**1. Specialization.** In [1, §2.3, Eq. (22)], with constant coefficients and no boundary stopping, the source term is \(hq\) and each of four wrapped endpoints has weight \(1/[4(1+rh)]\). With \(\rho=0\), the two stochastic signs are independent, so the endpoints are the four diagonal displacements \((\pm\sqrt h,\pm\sqrt h)\). Since \(N=k^2\), these coincide with the shifts by \((\pm k,\pm k)\) nodes. This proves the stated exact discrete system, including its normalization.

**2. Fourier diagonalization.** The characters
\[
\phi_{ab}(i,j)=\exp\!\bigl(2\pi\mathrm{i}(ai+bj)/N\bigr),
\qquad a,b\in\mathbb Z_N,
\]
form an orthogonal basis. The four shift multipliers average to
\[
\tfrac14(e^{2\pi\mathrm{i}a/k}+e^{-2\pi\mathrm{i}a/k})
(e^{2\pi\mathrm{i}b/k}+e^{-2\pi\mathrm{i}b/k})
=\cos(2\pi a/k)\cos(2\pi b/k).
\]
Thus \(P_k\) is real symmetric and its eigenvalues lie in \([-1,1]\). The value \(+1\) requires both cosine factors to be \(+1\), or both to be \(-1\). Each residue modulo \(k\) has exactly \(k\) lifts in \(\mathbb Z_N\). Cosine \(+1\) occurs only at residue zero; cosine \(-1\) occurs precisely at residue \(k/2\) when \(k\) is even. Consequently
\[
\dim\ker(I-P_k)=\begin{cases}k^2,&k\text{ odd},\\2k^2,&k\text{ even}.\end{cases}
\]
Likewise \(\Lambda_k=-1\) is possible only for even \(k\), when exactly one cosine is \(+1\) and the other \(-1\); its multiplicity is \(2k^2\). For odd \(k\), the smallest cosine equals \(-\cos(\pi/k)\), and this value multiplied by a cosine equal to one is the smallest product. Therefore
\[
\min_{a,b}\Lambda_k(a,b)=-b_k,
\quad b_k=\begin{cases}\cos(\pi/k),&k\text{ odd},\\1,&k\text{ even}.\end{cases}
\]
The eigenvalues of \(A_{k,r}\) are \(1-\Lambda_k/(1+r/k^2)\), so their minimum is \(r/(k^2+r)>0\) and maximum is \(1+b_k/(1+r/k^2)\). Division yields
\[
\kappa_2(A_{k,r})=1+(1+b_k)k^2/r.
\]
Because \(P_k\) is entrywise nonnegative and stochastic, \(A_{k,r}^{-1}=\sum_{m\ge0}(1+rh)^{-m}P_k^m\) is entrywise nonnegative; hence positivity remains intact.

**3. Sub-Nyquist response.** For \(k\ge3\), take the periodic smooth source \(q_k(x,y)=\cos(2\pi kx)\), with spatial frequency \(k<N/2=k^2/2\). On the torus,
\[
\tfrac12\Delta q_k=-2\pi^2 k^2q_k,
\qquad u_k=\frac{q_k}{r+2\pi^2k^2}
\]
solves \(\frac12\Delta u_k-ru_k+q_k=0\) uniquely. At the grid, its character index \((a,b)=(k,0)\) has \(\Lambda_k(k,0)=1\). Thus the unique solution of \(A_{k,r}U_k=hQ_k\) is
\[
U_k=\frac{h}{1-(1+rh)^{-1}}Q_k
=\frac{1+rh}{r}Q_k.
\]
The grid includes \(i=0\) where \(q_k=1\), so the exact supremum norm error is
\[
\|U_k-u_k|_{\rm grid}\|_{\ell^\infty}
=\frac{1+r/k^2}{r}-\frac1{r+2\pi^2k^2}
\longrightarrow\frac1r.
\]
The displayed expression is positive for \(k\ge3\) and \(r>0\). All formulas are exact at every stated integer \(k\); no limiting argument is used in the finite-dimensional spectral classification.

## Verification

A standalone standard-library script in `verification/check_spectrum.py` enumerates the exact modular multiplicity conditions for \(2\le k\le8\), tests Fourier extrema numerically, checks reachability in small grids, and verifies the particular forcing discrepancy for \(r=1\). Its recorded output is `verification/check_output.txt`. Those finite checks corroborate, but do not replace, the all-\(k\) character proof above. Reproduction: run `python3 verification/check_spectrum.py` from the directory containing the embedded `verification` folder.

## Relationship to prior work

Xu, Li and Yue [1, §2.3, Eq. (22), Algorithm 3 and Theorem 3] establish positivity and fixed-smooth-solution convergence for the periodic expectation-based scheme. Their analysis concerns local truncation and global maximum-norm convergence, not the exact discrete Fourier spectrum or its arithmetic multiplicity at commensurate meshes. Debrabant and Jakobsen [2, §§1, 3–5, 7] provide the broader monotone semi-Lagrangian consistency/convergence framework, which does not by itself assert the exact above multiplicities, parity-dependent extremal spectrum, or this source-response law. Related aliasing effects in other discretizations [3] do not imply an exact classification for the present periodic four-branch elliptic matrix.

## Limitations

The source \(q_k\) varies with mesh resolution and its higher derivatives grow with \(k\). This is **not** a counterexample to \(O(h)\) convergence for any fixed smooth periodic datum; no such assertion is made. The result applies to one particular constant isotropic specialization at the commensurate step \(h=1/k^2\); it does not classify noncommensurate steps, variable coefficients, boundary-value problems without periodic wrapping, or nonlinear equations. The resonance is compatible with positivity and matrix invertibility. Aliasing and disconnected-grid effects are classical general phenomena, so literature novelty is claimed only for the exact operator-specific spectral and forcing statements; this is not a claim of universal conceptual novelty.

## References

[1] H. Xu, K. Li and X. Yue, *A Non-compact Positivity-Preserving Numerical Scheme for Elliptic Differential Equations Based on Mathematical Expectation*, arXiv:2604.02797v1, first posted 2026-04-03, https://arxiv.org/html/2604.02797v1.

[2] K. Debrabant and E. R. Jakobsen, *Semi-Lagrangian schemes for linear and fully non-linear diffusion equations*, arXiv:0910.1046, first posted 2009-10-06, https://arxiv.org/abs/0910.1046.

[3] U. M. Ascher, S. J. Ruuth and B. T. R. Wetton, *Implicit-Explicit Methods for Time-Dependent Partial Differential Equations*, SIAM J. Numer. Anal. 32 (1995), doi:10.1137/0732037. Only the abstract of [3] was available in the comparison.
