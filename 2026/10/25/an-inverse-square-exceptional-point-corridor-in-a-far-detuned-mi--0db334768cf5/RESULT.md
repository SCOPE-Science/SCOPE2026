# An inverse-square exceptional-point corridor in a far-detuned minimal Kitaev chain

## Finding

At the equal-coupling sweet spot of a dissipative two-dot Kitaev chain, tuning one dot far off resonance leaves a narrow but nonzero window of the other dot's onsite energy in which two Bogoliubov–de Gennes eigenvalues have **exactly zero real part**. The window is bounded by two second-order exceptional points, and its half-width is asymptotically inverse quadratic in the far-detuned energy, with an explicit next correction.

Fix real parameters \(t>0\), \(\Gamma_{\mathrm L}>\Gamma_{\mathrm R}\geq0\), and set \(\Gamma=(\Gamma_{\mathrm L}+\Gamma_{\mathrm R})/2\) and \(\gamma=(\Gamma_{\mathrm L}-\Gamma_{\mathrm R})/2>0\). Take equal crossed-Andreev and tunnelling amplitudes \(\Delta=t\). For the non-Hermitian Bogoliubov matrix defined below, put \(R=|\varepsilon_{\mathrm R}|\), the absolute onsite energy of the far-detuned dot.

**Theorem.** For every fixed \(B>4\gamma t^2\), there exists \(R_B<\infty\) such that whenever \(R>R_B\) and \(|\varepsilon_{\mathrm L}|\le B/R^2\), there is a unique positive threshold \(w(R)\) with
\[
 w(R)=\frac{4\gamma t^2}{R^2}-\frac{8\gamma t^2(2\gamma^2+t^2)}{R^4}+O(R^{-6}).
\]
For \(|\varepsilon_{\mathrm L}|<w(R)\), precisely two distinct eigenvalues have zero real part; the remaining two have nonzero real parts of order \(R\). At \(|\varepsilon_{\mathrm L}|=w(R)\), the two imaginary-axis eigenvalues coalesce into one eigenvalue of algebraic multiplicity two and geometric multiplicity one (a second-order exceptional point). For \(w(R)<|\varepsilon_{\mathrm L}|\le B/R^2\), none of the four eigenvalues has zero real part. The statement holds for either sign of \(\varepsilon_{\mathrm R}\).

For fixed scaled detuning \(\ell=R^2\varepsilon_{\mathrm L}\) strictly away from the two critical values \(\pm4\gamma t^2\), the two low eigenvalues have the uniform leading expansion
\[
 E_{\pm}=-i(\Gamma+\gamma)+\frac{i}{R^2}\left(4\gamma t^2\pm\sqrt{16\gamma^2t^4-\ell^2}\right)+O(R^{-4}),
\]
with the square root taken real inside the corridor and with its imaginary analytic continuations outside. This formula describes the local spectral splitting but not the higher-order location of the exceptional points; the preceding expansion for \(w(R)\) gives that location.

## Assumptions and scope

Use the ordered particle–hole basis \((L_e,L_h,R_e,R_h)\). The effective matrix is
\[
H_{\rm eff}=-i\Gamma I_4+\begin{pmatrix}
\varepsilon_{\mathrm L}-i\gamma&0&t&t\\
0&-\varepsilon_{\mathrm L}-i\gamma&-t&-t\\
t&-t&\varepsilon_{\mathrm R}+i\gamma&0\\
t&-t&0&-\varepsilon_{\mathrm R}+i\gamma
\end{pmatrix}.
\]
All energies and rates are real and the quoted eigenvalues are algebraic eigenvalues of this finite-dimensional effective non-Hermitian matrix, not many-body dynamical decay rates or directly observable conductance peaks. The strict lead asymmetry \(\gamma>0\) and nonzero sweet-spot coupling \(t>0\) are essential. The theorem is local to the explicit far-detuned scaling strip; it does not assert a global classification at arbitrary onsite energies.

## Proof

Write \(x=E+i\Gamma\), \(u=\varepsilon_{\mathrm L}^2\), and \(v=\varepsilon_{\mathrm R}^2\). Direct evaluation of the determinant gives the exact characteristic polynomial
\[
 p(x)=x^4+(-u-v+2\gamma^2-4t^2)x^2+2i\gamma(u-v)x
 +uv+\gamma^2(u+v)+\gamma^4-4\gamma^2t^2.
\]
An eigenvalue has zero real part exactly when \(x=iy\) with real \(y\). The real polynomial for such eigenvalues is
\[
 q(y)=y^4+(u+v-2\gamma^2+4t^2)y^2-2\gamma(u-v)y
 +uv+\gamma^2(u+v)+\gamma^4-4\gamma^2t^2.
\]

Set \(s=R^{-2}\), \(\varepsilon_{\mathrm L}=s\ell\), and \(y=-\gamma+sz\). An **exact polynomial identity**, without discarded terms, is \(q(-\gamma+sz)=s F(z,\ell,s)\), where
\[
\begin{aligned}
F(z,\ell,s)={}&z^2-8\gamma t^2z+\ell^2\\
&+4s\bigl(\gamma^2\ell^2+(\gamma^2+t^2)z^2\bigr)\\
&-4\gamma s^2(\ell^2 z+z^3)+s^3(\ell^2z^2+z^4).
\end{aligned}
\]
At \(s=0\), the two bounded roots in \(z\) are
\[
 z=4\gamma t^2\pm\sqrt{16\gamma^2t^4-\ell^2}.
\]
They are distinct and real exactly when \(|\ell|<4\gamma t^2\), double at the endpoints, and nonreal conjugates outside. The other two eigenvalues have \(x/R\to\pm1\), by the matrix limit of \((H_{\rm eff}+i\Gamma I_4)/R\), so cannot lie on the imaginary axis for large \(R\).

At the positive fold \((z_0,\ell_0,s)=(4\gamma t^2,4\gamma t^2,0)\), the system \(F=\partial_zF=0\) has Jacobian determinant \(-4\ell_0\ne0\) with respect to \((z,\ell)\). The real-analytic implicit function theorem therefore gives a unique real fold \((z_*(s),\ell_*(s))\) near it. Evenness in \(\ell\) gives the matching negative fold. Compactness and simplicity of the limiting roots away from the folds show that for each fixed \(B>\ell_0\), these are the only low-root collisions for \(|\ell|\le B\) and all sufficiently small positive \(s\). Thus the above root count persists throughout the claimed scaled strip.

Differentiating \(F(z_*(s),\ell_*(s),s)=0\) at \(s=0\) yields
\[
2\ell_0\ell_*'(0)+4\bigl(\gamma^2\ell_0^2+(\gamma^2+t^2)z_0^2\bigr)=0,
\]
so \(\ell_*'(0)=-2\ell_0(2\gamma^2+t^2)\). Therefore \(w(R)=s\ell_*(s)\) has exactly the displayed two-term expansion, with remainder \(O(s^3)\).

To verify defectiveness, split the shifted matrix into the two local Nambu blocks and Schur-complement out the far dot. The latter is invertible at each low root for large \(R\), and its contribution to the local block has off-diagonal magnitude \(t^2|S(x)|\), where
\[
 S(x)=\frac1{x-\varepsilon_{\mathrm R}-i\gamma}
 +\frac1{x+\varepsilon_{\mathrm R}-i\gamma}
 =\frac{2(x-i\gamma)}{(x-i\gamma)^2-R^2}.
\]
At a low fold \(x=-i\gamma+O(R^{-2})\), one has \(S(x)=4i\gamma R^{-2}+O(R^{-4})\ne0\). Consequently the effective two-by-two matrix has a nonzero off-diagonal entry but zero determinant, hence rank exactly one. Its eigenspace is one-dimensional. Since \(\partial_z^2F=2+O(s)>0\), the associated root has algebraic multiplicity exactly two. Both folds are therefore genuine second-order exceptional points.

## Verification

The standalone script `verify.py` reconstructs the four-by-four matrix, checks its characteristic polynomial symbolically, verifies the exact scaled polynomial identity, and solves the double-root equations numerically for several independent parameter choices and detunings. It checks the predicted inverse-square coefficient, the second asymptotic correction, the inside/outside imaginary-axis classification, and rank defectiveness of the reduced Schur matrix. Execute with `python verify.py` in an environment providing SymPy, NumPy and SciPy. The analytic proof above, not finite sampling, establishes the theorem for all allowed parameters in its quantified asymptotic regime.

## Relationship to prior work

Cayao and Aguado's *Non-Hermitian minimal Kitaev chains*, arXiv:2406.18974 (first posted 2024-06-27), introduced and analyzed precisely this two-dot effective Hamiltonian and demonstrated exceptional-point-stabilized zero-real-energy bands, including graphical treatment of unequal onsite energies. That Hamiltonian, the existence of such bands, and the physical interpretation of non-Hermitian Majorana modes are **prior work**. The distinction here is the explicitly quantified far-detuning boundary, its inverse-square power and the next nonzero coefficient, together with a rigorous two-root/zero-root classification uniform in a scaled onsite-energy strip. The originating work reports qualitative detuning phase regions and formulas for equal onsite energies; it does not state or prove this far-detuned unequal-onsite scaling law.

The 2026 work of Cayao and Sato, arXiv:2606.23956, analyzes exceptional points in *Josephson junctions of two coupled* minimal Kitaev chains. Its phase-biased four-dot geometry is not an implication-equivalent treatment of the present single-chain, two-dot large-onsite-detuning limit. The gain/loss Kitaev-chain analysis by Agarwal and Joglekar, arXiv:2103.07058, uses a distinct parity–time-symmetric chain and a different spectral transition. General Schur-complement and fold perturbation tools are standard; no novelty is claimed for those methods.

## Limitations

This is an asymptotic spectral theorem for fixed strictly positive lead asymmetry, not a statement about finite-\(R\) global connectedness or conductance quantization. The big-O constants can depend on \(t\), \(\gamma\), and the chosen scaled interval. The theorem does not apply when \(\gamma=0\), \(t=0\), or \(\Delta\ne t\), nor does it establish robustness to interactions or energy-dependent reservoir self-energies. Originality assessment is limited by possible unindexed equivalent treatments and by general matrix-perturbation results that may subsume some steps; the published source's model alone should not be confused with its having established the present quantitative theorem.

## References

1. J. Cayao and R. Aguado, *Non-Hermitian minimal Kitaev chains*, arXiv:2406.18974, version 1 dated 2024-06-27. https://arxiv.org/abs/2406.18974
2. J. Cayao and M. Sato, *Andreev exceptional points in Josephson junctions formed by minimal Kitaev chains*, arXiv:2606.23956 (2026). https://arxiv.org/abs/2606.23956
3. K. S. Agarwal and Y. N. Joglekar, *PT-symmetry breaking in a Kitaev chain with one pair of gain-loss potentials*, arXiv:2103.07058 (2021). https://arxiv.org/abs/2103.07058
