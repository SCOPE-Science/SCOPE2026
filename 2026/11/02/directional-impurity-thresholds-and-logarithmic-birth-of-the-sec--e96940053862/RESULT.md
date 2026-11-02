# Directional impurity thresholds and logarithmic birth of the second localized mode on rectangular lattices

## Finding
Fix hopping strengths \(t_x,t_y>0\) and any nonzero lattice displacement \(r=(m,n)\in\mathbb Z^2\). For two identical positive onsite defects of strength \(V\), separated by \(r\), in the nearest-neighbor anisotropic rectangular tight-binding lattice, define the free upper band edge \(E_*=2(t_x+t_y)\) and
\[
 g_r(E)=\int_{[-\pi,\pi]^2}\frac{1-\cos(k\cdot r)}{E-2t_x\cos k_x-2t_y\cos k_y}\,\frac{d^2k}{(2\pi)^2},\qquad E>E_*,
\]
with \(g_r(E_*)\) the finite improper limit. Set \(V_c(r)=1/g_r(E_*)\). There is exactly one eigenvalue strictly above \(E_*\) for \(0<V\le V_c(r)\), and exactly two distinct simple eigenvalues above \(E_*\) for \(V>V_c(r)\). The second one, \(E_-(V)\), enters the continuous spectrum at \(V=V_c(r)\) as a bounded, nonsquare-summable antisymmetric threshold resonance. Its approach to the edge is
\[
 \lim_{V\downarrow V_c(r)}\frac{(E_-(V)-E_*)\log\!\left((t_x+t_y)/(V-V_c(r))\right)}{V-V_c(r)}
 =\frac{16\pi\sqrt{t_xt_y}}{(m^2/t_x+n^2/t_y)V_c(r)^2}.
\]
The logarithm is evaluated for \(V>V_c(r)\) sufficiently close to the threshold, so its argument is positive and tends to infinity. The exact critical strengths at nearest-neighbor separations are
\[
 V_c(1,0)=\frac{\pi t_x}{\arctan\sqrt{t_x/t_y}},\qquad
 V_c(0,1)=\frac{\pi t_y}{\arctan\sqrt{t_y/t_x}}.
\]
For example, at \((t_x,t_y)=(3,1)\), defects on horizontal nearest-neighbor sites require \(V>9\) for the second mode, whereas defects on vertical nearest-neighbor sites require only \(V>6\). These are strict thresholds; equality gives a resonance but no second \(\ell^2\) eigenvector. The general threshold can also be stated as \(V_c(r)=2/R_{\mathrm{eff}}(0,r)\), where the effective resistance is that of the infinite rectangular resistor network with horizontal/vertical conductances \(t_x,t_y\).

## Assumptions and scope
Work on \(\ell^2(\mathbb Z^2)\). Let \(e_x=(1,0)\), \(e_y=(0,1)\), and define
\[
 (H_0\psi)(u)=t_x\bigl(\psi(u+e_x)+\psi(u-e_x)\bigr)+t_y\bigl(\psi(u+e_y)+\psi(u-e_y)\bigr).
\]
For fixed \(r=(m,n)\ne(0,0)\), set \(H_V=H_0+V(|0\rangle\langle0|+|r\rangle\langle r|)\), with \(V>0\). The essential spectrum is \([-E_*,E_*]\). We count only eigenvalues strictly greater than \(E_*\); a threshold resonance is not counted as an eigenvalue. The limit formula holds as \(V\downarrow V_c(r)\) with \(t_x,t_y,r\) fixed.

## Proof
**Step 1 — exact rank-two reduction.** For \(E>E_*\), the free resolvent \(G(E)=(E-H_0)^{-1}\) has matrix elements \(a(E)=\langle 0,G(E)0\rangle\) and \(b(E)=\langle0,G(E)r\rangle\). The Birman–Schwinger matrix at the two defect sites is \(V\bigl(\begin{smallmatrix}a&b\\b&a\end{smallmatrix}\bigr)\); its eigenvalues are \(V(a+b)\) and \(V(a-b)\). Fourier diagonalization identifies \(a-b=g_r(E)\). The heat-kernel representation \(G(E)=\int_0^\infty e^{-Et}e^{tH_0}\,dt\) gives \(b(E)>0\). Both combinations \(a\pm b\) are strictly decreasing in \(E\) by positivity of \(G(E)^2\) on the respective nonzero symmetric/antisymmetric defect vectors, and both tend to zero at infinity. The symmetric integral has numerator \(1+\cos(k\cdot r)\), which is nonzero at the unique upper-band maximum \(k=0\); hence \(a+b\to\infty\) as \(E\downarrow E_*\). The antisymmetric numerator vanishes quadratically there, so \(a-b=g_r(E)\) tends to a finite strictly positive \(g_r(E_*)\). Thus the symmetric branch always has one simple root \(V(a+b)=1\), and the antisymmetric branch has one simple root precisely when \(V>1/g_r(E_*)\). The two roots are distinct, since \(b>0\). Rank two excludes further eigenvalues above the edge.

**Step 2 — threshold resonance and resistance.** Let \(q(k)=2t_x(1-\cos k_x)+2t_y(1-\cos k_y)\). The antisymmetric candidate at criticality has Fourier transform proportional to \((1-e^{-ik\cdot r})/q(k)\). Near \(k=0\), this is \(O(|k|^{-1})\) and is integrable but not square-integrable, since \(r\ne0\). Fourier inversion gives a bounded sequence solving the critical eigen-equation in the generalized sense, but no \(\ell^2\) eigenstate. For the weighted network Laplacian \(L=E_*-H_0\), the voltage difference under unit current from \(0\) to \(r\) is
\[
 R_{\mathrm{eff}}(0,r)=\int_{[-\pi,\pi]^2}\frac{|1-e^{ik\cdot r}|^2}{q(k)}\frac{d^2k}{(2\pi)^2}=2g_r(E_*).
\]
Thus \(V_c(r)=2/R_{\mathrm{eff}}(0,r)\). This identity also shows that the critical strength is finite and strictly positive for any nonzero \(r\).

**Step 3 — exact nearest-neighbor directional integrals.** For \(r=e_x\), integrate over \(k_y\) first using \(\langle(A-2t_y\cos k_y)^{-1}\rangle_y=(A^2-4t_y^2)^{-1/2}\) for \(A>2t_y\). With \(A=2t_y+2t_x(1-\cos k_x)\), the endpoint limit is integrable. Successive substitutions \(u=\sin(k_x/2)\) and \(z=\sqrt{1-u^2}\) yield
\[
 g_{e_x}(E_*)=\frac1{\pi\sqrt{t_x}}\int_0^1\frac{dz}{\sqrt{t_x+t_y-t_xz^2}}
 =\frac{\arctan\sqrt{t_x/t_y}}{\pi t_x}.
\]
The vertical formula follows by exchanging axes. Taking reciprocals proves the stated critical strengths.

**Step 4 — sharp nonanalytic eigenvalue onset.** Write \(E=E_*+\delta\) for \(\delta>0\), and put \(R^2=m^2/t_x+n^2/t_y\). Direct subtraction gives
\[
 g_r(E_*)-g_r(E_*+\delta)=\int\frac{(1-\cos(k\cdot r))\,\delta}{q(k)[q(k)+\delta]}\frac{d^2k}{(2\pi)^2}.
\]
The integrand away from a fixed small ball around \(k=0\) contributes \(O(\delta)\). In that ball, \(q(k)=t_xk_x^2+t_yk_y^2+O(|k|^4)\) and \(1-\cos(k\cdot r)=(k\cdot r)^2/2+O(|k|^4)\). Replacing these by their quadratic parts changes the integral by only \(O(\delta)\) (the errors become integrable after the subtraction). Rescale \(p_x=\sqrt{t_x}k_x\), \(p_y=\sqrt{t_y}k_y\) and average the square of the angular dot product, \(\int_0^{2\pi}(m\cos\theta/\sqrt{t_x}+n\sin\theta/\sqrt{t_y})^2d\theta=\pi R^2\). The radial integral then has leading term \(\tfrac12\delta\log(1/\delta)\), giving the exact expansion
\[
 g_r(E_*)-g_r(E_*+\delta)=\frac{R^2}{16\pi\sqrt{t_xt_y}}\,\delta\log\!\left((t_x+t_y)/\delta\right)+O(\delta).
\]
By the antisymmetric Birman–Schwinger equation, \(g_r(E_*+\delta)=1/V\), and therefore
\[
 g_r(E_*)-\frac1V=\frac{V-V_c(r)}{V_c(r)^2}(1+o(1)).
\]
Monotonicity shows \(\delta\to0\) as \(V\downarrow V_c(r)\). Inverting the preceding \(\delta\log(1/\delta)\) asymptotic (the logarithms of \(\delta\) and \(V-V_c(r)\) are asymptotically equal) proves the claimed limit with its prefactor and the stated domain.

## Verification
Run `python verify_rectangular_two_impurity.py` with Python, NumPy, and SciPy; the recorded output is `verify_rectangular_output.txt`. Independently evaluated one-dimensional and two-dimensional Brillouin-zone integrals agree at six anisotropic/isotropic settings to within \(2.8\times10^{-17}\). The computed critical horizontal/vertical strengths at \((t_x,t_y)=(3,1)\) are exactly \(9\) and \(6\). For three placements at this anisotropy, the upper antisymmetric eigenvalue from the infinite-volume secular equation agrees with the second-largest eigenvalue of a \(41\times41\) finite open box within \(1.3\times10^{-12}\) at the tested, localized parameter values. Near-edge finite differences show the expected slow approach to the coefficient in the logarithmic formula. These finite numerical tests corroborate, but do not replace, the all-displacement analytic argument.

## Relationship to prior work
Cserti's rectangular resistor-network Green-function calculation gives the relevant anisotropic lattice effective resistance; the resistance identity and a corresponding isotropic pin-count criterion are therefore antecedents, not independently claimed as new. General finite-rank impurity determinant formulas, including Glasser's, explain how bound-state equations reduce to a small matrix, but do not themselves state the anisotropy-resolved critical bifurcation law with the displacement-dependent logarithmic coefficient proved here. Bak calculates related rectangular-lattice Green functions for a different two-particle problem, without this two-fixed-onsite-defect threshold result. A published lower-edge threshold classification for a different finite-support neighbor perturbation likewise has different objects, eigenvalue equations and transition parameters. The assessed contribution is the combined **all-displacement, anisotropic second-mode birth law with explicit sharp edge coefficient**, together with its exact directional nearest-neighbor specialization; the general two-site counting mechanism by itself is excluded from originality.

## Limitations
The system has precisely two equal positive onsite perturbations, uniform positive nearest-neighbor hoppings on the whole infinite lattice, and no disorder or interactions. The onset is an asymptotic for fixed nonzero displacement and fixed anisotropy; it is not uniform as displacement or anisotropy vary. The statement counts only eigenvalues strictly above the top of the band. The derivation does not supply finite-box error bounds, higher-order near-threshold constants, or a claim of historical priority against every unpublished treatment of two-center discrete Schrödinger resonances.

## References
1. J. Cserti, *Application of the lattice Green's function for calculating the resistance of an infinite network of resistors*, arXiv:cond-mat/9909120 (first public version 1999-09-08), https://arxiv.org/abs/cond-mat/9909120 .
2. M. Bak, *Two-Particle Lattice Green Functions on a Two-Dimensional Rectangular Lattice with Next-Nearest Neighbor Hopping*, International Journal of Theoretical Physics, first published online 2011-11-05, DOI:10.1007/s10773-011-0993-6, https://link.springer.com/article/10.1007/s10773-011-0993-6 .
3. M. L. Glasser, *A Note on the Exact Green Function for a Quantum System Decorated by Two or More Impurities*, arXiv:1702.05111, https://arxiv.org/abs/1702.05111 ; Frontiers in Physics (2019), https://doi.org/10.3389/fphy.2019.00007 .
4. F. Hiroshima, Z. Muminov, U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on an \(n\)-dimensional lattice*, arXiv:1804.05339, https://arxiv.org/abs/1804.05339 ; distinct finite-support perturbation model.
