# Sharp binding threshold and separation penalty for a neutral pair of cubic-lattice defects

## Finding
Consider the simple-cubic tight-binding Laplacian on \(\ell^2(\mathbb Z^3)\), perturbed by an attractive on-site potential at the origin and a repulsive potential of the same magnitude at an arbitrary distinct lattice site \(r\). Its two possible eigenvalues outside the free band are born **simultaneously** at a strictly positive, separation-dependent coupling threshold. At the threshold they are resonances, not square-summable eigenfunctions; above it they are simple and lie symmetrically about the band center. The threshold exceeds the isolated-impurity critical strength and has a universal inverse-square separation penalty.

Precisely, define
\[
\varepsilon(k)=2\sum_{j=1}^3(1-\cos k_j),\qquad
G_r(\kappa)=\frac1{(2\pi)^3}\int_{[-\pi,\pi]^3}\frac{\cos(k\cdot r)}{\varepsilon(k)+\kappa}\,dk,\qquad g=G_0(0),\quad h_r=G_r(0).
\]
For each \(r\in\mathbb Z^3\setminus\{0\}\), put
\[
\lambda_c(r)=\big(g^2-h_r^2\big)^{-1/2}.
\]
For every \(\lambda>\lambda_c(r)\) there is exactly one simple eigenvalue below the band \([0,12]\), at \(-\kappa_r(\lambda)\), and exactly one above it, at \(12+\kappa_r(\lambda)\), where \(\kappa_r(\lambda)>0\) is the unique solution of
\[
\lambda^2\big[G_0(\kappa)^2-G_r(\kappa)^2\big]=1.
\]
For \(0<\lambda\le\lambda_c(r)\) there are no eigenvalues **outside** \([0,12]\). At equality, both band edges are non-\(\ell^2\) threshold resonances. With \(a_r=g-h_r>0\), the lower binding gap obeys
\[
\kappa_r(\lambda)\sim \frac{16\pi^2}{a_r^2\lambda_c(r)^6}\big(\lambda-\lambda_c(r)\big)^2
\qquad\text{as }\lambda\downarrow\lambda_c(r)\text{ from above}.
\]
The separation-dependent threshold satisfies the sharp large-distance law
\[
\lambda_c(r)>g^{-1},\qquad
\lambda_c(r)-g^{-1}\sim\frac1{32\pi^2g^3\lVert r\rVert_2^2}\quad\text{as }\lVert r\rVert_2\to\infty.
\]
For nearest neighbors \(r=e_1\), the exact identity \(g-h_{e_1}=1/6\) gives
\[
\lambda_c(e_1)=\frac6{\sqrt{12g-1}}\approx 4.20830204122339,
\qquad g\approx0.25273100985866.
\]

## Assumptions and scope
The operator is the bounded self-adjoint operator
\[
(H_{\lambda,r}f)(x)=6f(x)-\sum_{j=1}^3[f(x+e_j)+f(x-e_j)]-\lambda\mathbf1_{\{x=0\}}f(x)+\lambda\mathbf1_{\{x=r\}}f(x),
\]
with integer lattice sites \(x,r\in\mathbb Z^3\), \(r\ne0\), and real coupling \(\lambda>0\). The hopping amplitude is one; rescaling it rescales all displayed energies and critical couplings. The free essential spectrum is \([0,12]\). Statements about the exact number of eigenvalues concern **only the complement of that band**; possible embedded eigenvalues are not classified here. A threshold resonance means a nonzero bounded solution of the zero- or upper-edge eigen-equation decaying at spatial infinity but not belonging to \(\ell^2\).

## Proof
**1. Positivity of the Green functions.** Fourier transformation diagonalizes the free operator with symbol \(\varepsilon\). For \(\kappa\ge0\), the integrals defining \(G_r(\kappa)\) converge (the only possible singularity at \(\kappa=0\) is integrable in dimension three). Their heat-kernel representation is
\[
G_r(\kappa)=\int_0^\infty e^{-\kappa t}(e^{-tH_0})(0,r)\,dt.
\]
The heat kernel of the connected nearest-neighbor random walk is strictly positive for positive time, so \(0<h_r<g\). Equivalently, \(g-h_r\) and \(g+h_r\) are integrals with strictly positive nonnegative numerators \(1-\cos(k\cdot r)\) and \(1+\cos(k\cdot r)\), respectively. At fixed \(r\), both \(G_0(\kappa)-G_r(\kappa)\) and \(G_0(\kappa)+G_r(\kappa)\) strictly decrease to zero as \(\kappa\to\infty\).

**2. Exact two-site determinant and counting.** At energy \(-\kappa<0\), write the equation as
\[
 f=\lambda(H_0+\kappa)^{-1}\big(f(0)\delta_0-f(r)\delta_r\big).
\]
Evaluating at the two defect sites gives a homogeneous linear system with matrix
\[
\begin{pmatrix}
1-\lambda G_0(\kappa)&\lambda G_r(\kappa)\\
-\lambda G_r(\kappa)&1+\lambda G_0(\kappa)
\end{pmatrix}.
\]
Its determinant vanishes precisely when \(\lambda^2F_r(\kappa)=1\), where
\[
F_r(\kappa)=\big[G_0(\kappa)-G_r(\kappa)\big]\big[G_0(\kappa)+G_r(\kappa)\big].
\]
Both factors are strictly decreasing and positive; hence \(F_r\) is continuous and strictly decreasing from \(F_r(0)=g^2-h_r^2>0\) to zero. There is therefore exactly one negative eigenvalue precisely above \(\lambda_c(r)\), and none at or below it. The two-site matrix has rank one at a zero of its determinant because its off-diagonal Green entry is positive, giving simplicity. Finite-rank invariance fixes the essential band.

**3. Reflection–staggering symmetry.** Reflection about the midpoint of the defects exchanges the two sites and negates their potentials. Multiplication by \((-1)^{x_1+x_2+x_3}\) conjugates \(H_0\) to \(12-H_0\) while preserving the on-site potentials. Composing these two unitaries conjugates \(H_{\lambda,r}\) to \(12-H_{\lambda,r}\). Consequently, each negative eigenvalue \(-\kappa\) corresponds to the positive-outlier eigenvalue \(12+\kappa\), with the same simplicity and threshold.

**4. The edge is resonant, not square summable.** At \(\lambda=\lambda_c(r)\), the two-site determinant has a nonzero null vector \((u,v)\). The Fourier transform of its threshold-state Green representation is proportional to
\[
 \frac{u-v e^{-ik\cdot r}}{\varepsilon(k)}.
\]
If \(u=v\ne0\), the two matrix equations would require simultaneously \(1-\lambda(g-h_r)=0\) and \(1+\lambda(g-h_r)=0\), an impossibility. Thus the numerator has a nonzero constant term at \(k=0\). Since \(\varepsilon(k)=|k|^2+O(|k|^4)\) near zero, the Fourier expression belongs to \(L^1\) but not \(L^2\). The inverse Fourier transform is a bounded solution tending to zero at infinity, not an \(\ell^2\) eigenvector. The upper-edge state follows by the symmetry in step 3.

**5. Quadratic onset.** In dimension three, expansion of the free Green integral near its nondegenerate band minimum yields
\[
 G_0(0)-G_0(\kappa)=\frac{\sqrt\kappa}{4\pi}+o(\sqrt\kappa).
\]
Indeed the local substitution \(k=\sqrt\kappa\,q\) reduces the leading integral to \((2\pi)^{-3}\int_{\mathbb R^3} dq/[|q|^2(|q|^2+1)]=1/(4\pi)\), while the complementary part is of lower order. For fixed \(r\ne0\), \(1-\cos(k\cdot r)=O_r(|k|^2)\), so dominated convergence gives
\[
 [G_0(0)-G_r(0)]-[G_0(\kappa)-G_r(\kappa)]=O_r(\kappa).
\]
It follows that \(F_r(0)-F_r(\kappa)=a_r\sqrt\kappa/(2\pi)+o(\sqrt\kappa)\). On the eigenvalue branch, Taylor expansion of \(\lambda^{-2}\) at \(\lambda_c(r)\) gives \(F_r(0)-F_r(\kappa)=2(\lambda-\lambda_c)/\lambda_c^3+o(\lambda-\lambda_c)\). Equating the two expressions proves the stated squared onset with coefficient \(16\pi^2/(a_r^2\lambda_c^6)\).

**6. Sharp separation law.** A standard localized Fourier singularity argument gives
\[
 h_r=\frac{1}{4\pi\lVert r\rVert_2}+o(\lVert r\rVert_2^{-1})
\quad\text{as }\lVert r\rVert_2\to\infty.
\]
For completeness, choose a smooth cutoff near \(k=0\) and subtract \(1/|k|^2\) from \(1/\varepsilon(k)\) there. The inverse transform of the subtracted Newtonian singularity is \((4\pi|r|)^{-1}\) at leading order; the remainder is integrable with two weak derivatives, so its Fourier coefficients are \(O(|r|^{-2})\). Away from the cutoff the symbol is smooth, with rapidly decreasing coefficients. Finally expand
\[
\lambda_c(r)=g^{-1}\big(1-h_r^2/g^2\big)^{-1/2}
=g^{-1}+\frac{h_r^2}{2g^3}+O(h_r^4),
\]
which proves both strict inequality and the inverse-square constant.

**7. Nearest-neighbor constant.** Symmetry and \(\varepsilon(k)=2\sum_{j=1}^3(1-\cos k_j)\) give
\[
 g-h_{e_1}=\frac1{(2\pi)^3}\int\frac{1-\cos k_1}{\varepsilon(k)}dk=\frac16.
\]
Substitution into \(\lambda_c(r)\) proves the exact nearest-neighbor expression.

## Verification
The companion `checks.py` implements the free resolvent through the heat kernel \(e^{-6t}I_{r_1}(2t)I_{r_2}(2t)I_{r_3}(2t)\), and for axial separation computes \(g\), \(h_{ne_1}\), the nearest-neighbor identity, sample critical couplings, and the approach to the two asymptotic coefficients. It uses only the Python standard library. Running `python checks.py` prints an approximately \(4.2083020412\) nearest-neighbor threshold and the predicted limiting coefficients. These quadratures **corroborate**, but do not replace, the analytical proof; convergence of sampled sequences is not treated as an infinite certificate.

## Relationship to prior work
The 2012 rank-one analysis by Hiroshima, Sasaki, Shirai, and Suzuki identifies the dimension-three one-defect threshold and its resonance character. The 2005 work of Albeverio, Lakaev, Makarov, and Muminov studies critical lattice two-particle operators, while a 2018 work of Hiroshima, Muminov, and Kuljanov treats a distinct center-plus-symmetric-neighbors delta family through finite-dimensional Birman–Schwinger reductions. Green-function treatments of a single tight-binding impurity are likewise established. None of these inspected statements gives the *opposite-sign, exactly two-site* critical coupling as a function of arbitrary separation together with its inverse-square penalty and the paired square-root-edge bifurcation. A previously recorded result for the **two-dimensional** opposite-sign pair yields binding at every positive coupling and an exponentially small gap; it does not imply the three-dimensional positive-threshold regime. Priority remains conditional on broader impurity literature not exhaustively available here.

## Limitations
The theorem does not classify embedded eigenvalues within \([0,12]\), scattering amplitudes, finite-volume spectra, multiple defect pairs, or higher-dimensional exponents. The threshold is an \(L^1\)-Fourier / bounded spatial solution, not a normalizable state. The long-separation limit is taken with the lattice spacing and hopping fixed; the near-critical gap limit is for each fixed nonzero separation. Literature and mathematical verification are same-review-stage only; no independent validation is claimed.

## References
- F. Hiroshima, I. Sasaki, T. Shirai, A. Suzuki, *Note on the spectrum of discrete Schrödinger operators*, arXiv:1209.0522 (initial public version 2012-09-04), https://arxiv.org/html/1209.0522v1.
- S. Albeverio, S. N. Lakaev, K. A. Makarov, Z. I. Muminov, *The Threshold Effects for the Two-Particle Hamiltonians on Lattices*, arXiv:math-ph/0501013 (initial public version 2005-01-06), https://arxiv.org/abs/math-ph/0501013.
- F. Hiroshima, Z. Muminov, U. Kuljanov, *Threshold of discrete Schrödinger operators with delta potentials on n-dimensional lattice*, arXiv:1804.05339 (2018-04-15), https://arxiv.org/abs/1804.05339.
- S. N. Lakaev, I. N. Bozorov, *The number of bound states of a one-particle Hamiltonian on a three-dimensional lattice*, Theor. Math. Phys. 158 (2009), 360–376, doi:10.1007/s11232-009-0030-6 (abstract inspected).
- M. McCutcheon, *A Green's Function Analysis of Defect States in Periodic Hamiltonians*, 2004, https://phas.ubc.ca/~berciu/TEACHING/PHYS503/PROJECTS/P503_impurity.pdf (single-impurity sections inspected).
