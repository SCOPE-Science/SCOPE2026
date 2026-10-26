# Exact finite-ring spinodal and a five-site instability cutoff for a one-dimensional active lattice gas

## Finding

Consider the one-dimensional, two-orientation, hard-core active lattice-gas **mean-field equations** of Hawthorne, Woellner and Freire on a periodic ring of \(L\geq3\) sites. At homogeneous occupancy \(0<\rho<1\), let \(a>0\) be the active hopping rate, \(t\geq0\) the per-neighbor translational hopping rate and \(r>0\) the orientation-switching rate. Define
\[
c_L=\cos(2\pi/L),\qquad h_L=1-c_L,
\qquad G_L=2(1-\rho)[(1+c_L)\rho-1],
\]
\[
b_L=2r+4t(1-\rho)h_L,\qquad
 d_L=4t[r+t(1-\rho)h_L].
\]
The homogeneous state is **linearly exponentially stable at fixed total occupancy** for every \(a>0\) whenever \(G_L\leq0\). When \(G_L>0\), it is linearly exponentially stable precisely for \(a<a_c\), has a nonconserved zero eigenvalue precisely for \(a=a_c\), and is linearly unstable precisely for \(a>a_c\), where
\[
\boxed{a_c=\frac{b_L+\sqrt{b_L^2+4G_Ld_L}}{2G_L}.}
\]
The first unstable Fourier modes are the longest nonconstant modes \(k=\pm2\pi/L\); at equality they supply a two-dimensional real neutral subspace. The condition \(G_L>0\) can occur **if and only if \(L\geq5\)**, and for such rings it is equivalent to
\[
\boxed{\rho>\frac1{1+\cos(2\pi/L)}.}
\]
Thus periodic mean-field rings of three or four sites never have this linear instability, at any positive activity or nonnegative translational diffusion rate; five sites are the minimum.

When \(t=0\), minimization of the instability threshold over all mean-field densities gives a further exact classification:
\[
\boxed{\rho_*(L)=\frac{2+c_L}{2(1+c_L)},\qquad
\inf_{0<\rho<1}a_c(L,\rho,0,r)=\frac{4r(1+c_L)}{c_L^2}}
\quad(L\geq5).
\]
For example, an admissible five-site mean density \(\rho=4/5\) has the exact boundary \(a_c=25(2+\sqrt5)r\). In the large-ring limit,
\[
\rho_*(L)=\frac34+\frac{\pi^2}{4L^2}+O(L^{-4}),\qquad
\inf_\rho a_c(L,\rho,0,r)=8r+\frac{24\pi^2r}{L^2}+O(L^{-4}).
\]
These assertions concern the mean-field linearization, not a thermodynamic phase transition of the finite stochastic particle system.

## Assumptions and scope

At each site \(j\) there are orientation-resolved mean-field probabilities \(p_{j,+},p_{j,-}\), with \(\rho_j=p_{j,+}+p_{j,-}\). The field takes values with \(p_{j,s}\geq0\) and \(\rho_j\leq1\); the homogeneous equilibrium has \(p_{j,+}=p_{j,-}=\rho/2\). Indices are periodic modulo \(L\), and the dynamical equations are
\[
\begin{aligned}
\dot p_{j,+}={}&a[p_{j-1,+}(1-\rho_j)-p_{j,+}(1-\rho_{j+1})]\\
&+t\!\sum_{\epsilon=\pm1}[p_{j+\epsilon,+}(1-\rho_j)-p_{j,+}(1-\rho_{j+\epsilon})]+r(p_{j,-}-p_{j,+}),\\
\dot p_{j,-}={}&a[p_{j+1,-}(1-\rho_j)-p_{j,-}(1-\rho_{j-1})]\\
&+t\!\sum_{\epsilon=\pm1}[p_{j+\epsilon,-}(1-\rho_j)-p_{j,-}(1-\rho_{j+\epsilon})]+r(p_{j,+}-p_{j,-}).
\end{aligned}
\]
This is the one-dimensional specialization of the source's mean-field equations with each orientation reversing at rate \(r\) and per-neighbor translational diffusion rate \(t\). Linear exponential stability means decay of every linearized perturbation conserving \(\sum_j\rho_j\); the uniform-density mass-conservation eigenvalue is excluded. All inequalities for instability are strict. No nonlinear stability statement is made at the threshold.

## Proof

**1. Exact full-wave-number linearization.** Put \(u_j=\delta p_{j,+}+\delta p_{j,-}\) and \(v_j=\delta p_{j,+}-\delta p_{j,-}\). Insert Fourier modes proportional to \(e^{ikj}\), for \(k=2\pi m/L\), in the equations above. Let \(A=a+2t\), \(B=(1-\rho)A\), \(h=1-\cos k\). The exact \(2\times2\) Fourier matrix is
\[
M(k)=\begin{pmatrix}
-Ah&-ia(1-\rho)\sin k\\
-ia(1-2\rho)\sin k&-2r-Bh
\end{pmatrix}.
\]
At \(k=0\), its eigenvalues are \(0\) (conserved mass) and \(-2r\). For every \(k\not\equiv0\), \(h>0\), its real trace is \(-2r-(A+B)h<0\), while its real determinant is
\[
\det M(k)=h\bigl[2rA+ABh-C(2-h)\bigr],\qquad
C=a^2(1-\rho)(2\rho-1),
\]
using \(\sin^2k=h(2-h)\). A two-by-two characteristic polynomial with negative real trace and positive real determinant has both roots in the strict left half-plane; with negative determinant it has one positive real root; with zero determinant it has a zero root and a negative root. This is a full-spectrum argument, without a small-wave-number expansion.

**2. Why the longest wavelength controls onset.** If \(\rho\leq1/2\), then \(C\leq0\) and the determinant is positive at every nonzero mode. If \(\rho>1/2\), then \(C>0\), and the expression \(2rA-2C+(AB+C)h\) is strictly increasing in \(h\). Among all permitted nonzero Fourier wave numbers, the smallest \(h\) is \(h_L=1-\cos(2\pi/L)\), attained only at \(m=1,L-1\). Therefore the sign of the determinant there controls stability of **all** nonconserved modes, and the earliest neutral modes are exactly that conjugate Fourier pair.

**3. Finite-ring cutoff and exact activity threshold.** At \(h=h_L\), instability is equivalent to
\[
C(2-h_L)>A(2r+Bh_L).
\]
Expansion gives the **equivalent** quadratic inequality
\[
G_La^2-b_La-d_L>0.
\]
Here \(b_L>0\), \(d_L\geq0\). If \(G_L\leq0\), the left side is strictly negative for every \(a>0\). If \(G_L>0\), its unique positive root is the displayed \(a_c\), with the sign changing exactly there. Since \(G_L>0\) is equivalent to \((1+c_L)\rho>1\), and \(0<\rho<1\), it is possible exactly when \(c_L>0\), namely \(L\geq5\). At equality the two longest nonconstant real Fourier directions form the claimed neutral subspace; the other nonconstant directions retain negative spectral real parts.

**4. Exact minimal activity at zero translational diffusion.** If \(t=0\) and \(G_L>0\), then \(b_L=2r\), \(d_L=0\), and
\[
a_c(L,\rho,0,r)=\frac{r}{(1-\rho)[(1+c_L)\rho-1]}.
\]
The denominator is a strictly concave quadratic of \(\rho\), with unique maximum at \(\rho_*(L)\). Completing the square gives its maximum \(c_L^2/[4(1+c_L)]\), proving the global minimum formula. Substituting \(L=5\), \(c_5=(\sqrt5-1)/4\), and \(\rho=4/5\) gives \(a_c=25(2+\sqrt5)r\). Taylor expansion of \(\cos(2\pi/L)\) yields the two large-ring formulas.

**5. Finite-size shift with translational diffusion.** For completeness, fix \(1/2<\rho<1\), \(t\geq0\), \(r>0\). Write \(R=(1-\rho)(2\rho-1)\) and
\[
a_\infty=\frac{r+\sqrt{r^2+8rtR}}{2R},\quad
A_\infty=a_\infty+2t,\quad B_\infty=(1-\rho)A_\infty,\quad C_\infty=a_\infty^2R.
\]
The finite-ring transition solves \(2(C-rA)-h(C+AB)=0\). Its derivative with respect to \(a\) at \((a,h)=(a_\infty,0)\) equals \(2(2a_\infty R-r)>0\), so the implicit-function theorem and \(h_L=2\pi^2L^{-2}+O(L^{-4})\) give
\[
\boxed{a_c(L,\rho,t,r)=a_\infty+\frac{\pi^2(C_\infty+A_\infty B_\infty)}{2a_\infty R-r}L^{-2}+O(L^{-4}).}
\]
The coefficient is strictly positive. The expansion is for fixed \(\rho,t,r\); it is not uniform as \(\rho\downarrow1/2\).

## Verification

The accompanying `verify.py` independently forms the full real-space Jacobian by centered finite differences of the original nonlinear mean-field flow, and compares its eigenvalues against the Fourier blocks. It also checks the exact instability predicate, opposite sides of transition roots, the unconditional three- and four-site stability, the zero-diffusion density optimizer, the large-ring correction, and three symbolic polynomial identities using SymPy. The checker passed 318 deterministic assertion groups for the documented test parameters, covering ring sizes from three to several hundred sites. These finite tests corroborate, but do not replace, the symbolic proof for arbitrary allowed parameters and ring sizes.

Reproduction: with Python, NumPy and SymPy installed, run `python verify.py` from the directory containing this document and the standalone script.

## Relationship to prior work

Hawthorne, Woellner and Freire (2026) introduce the source mean-field flow, its Bloch linearization, and the infinite-lattice long-wave spinodal; the paper states that finite-lattice stability is addressed numerically. Those results are taken as established. Here the distinct claim is a closed, global, **all-wave-number** stability classification on an arbitrary finite one-dimensional periodic lattice, including the exact five-site lower cutoff and the optimal activity across densities. The source's general Fourier matrix is the starting point rather than a newly derived physical model.

Kourbane-Houssene, Erignoux, Bodineau and Tailleur (2018), Mason, Erignoux, Jack and Bruna (2023), and Neville (2025) establish complementary hydrodynamic formulations and long-wave spinodal calculations for related active exclusion systems. Their hydrodynamic models or limits are not identical to the finite-lattice, two-orientation mean-field flow here. No claim is made that the long-wave spinodal itself is new.

## Limitations

The result is confined to linearized **mean-field** dynamics with periodic one-dimensional geometry, two orientations, hard-core vacancy factors, and homogeneous rates. In a finite exact stochastic exclusion chain a sharp thermodynamic phase transition is not asserted. Linear instability does not prove the existence, type, or nonlinear stability of phase-separated stationary states. At equality only linear neutrality is proved. The minimal five-site statement is model-specific and is not a general minimum for motility-induced phase separation. The activity minimum over a continuous mean-field density need not correspond to an integer particle count on a short ring. Extensions to other lattices, boundaries, or director graphs are unproved. Whether a more general finite-volume spectral-stability theorem already subsumes these exact formulas remains an originality risk.

## References

1. F. Hawthorne, C. F. Woellner, J. A. Freire, *Exact mean-field phase diagram for self-avoiding active particles in a lattice*, arXiv:2606.07823v1 (first public 2026-06-05), Sections II--III and supporting information. https://arxiv.org/abs/2606.07823
2. M. Kourbane-Houssene, C. Erignoux, T. Bodineau, J. Tailleur, *Exact Hydrodynamic Description of Active Lattice Gases*, Physical Review Letters 120, 268003 (2018), arXiv:1801.08952. https://arxiv.org/abs/1801.08952
3. J. Mason, C. Erignoux, R. L. Jack, M. Bruna, *Exact hydrodynamics and onset of phase separation for an active exclusion process*, Proceedings of the Royal Society A 479, 20230524 (2023), arXiv:2307.11673. https://arxiv.org/abs/2307.11673
4. A. Neville, *Hydrodynamic equations and near critical large deviations of active lattice gases*, Journal of Statistical Mechanics 2025, 033204 (2025). https://doi.org/10.1088/1742-5468/adbefe
