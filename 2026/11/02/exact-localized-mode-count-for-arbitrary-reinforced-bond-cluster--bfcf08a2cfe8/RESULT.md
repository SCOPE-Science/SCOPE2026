# Exact localized-mode count for arbitrary reinforced-bond clusters in a harmonic chain

## Finding

Let an infinite monatomic harmonic chain have identical masses and identical nearest-neighbor springs except for finitely many independently reinforced bonds. The exact number of exponentially localized modes above the acoustic band is determined by the positive inertia of a finite weighted-path Green matrix, including all equality cases at the band edge.

Put reinforced bond positions \(r_1<\cdots<r_p\) in \(\mathbb Z\), relative stiffness increments \(\alpha_i>0\), and separations \(d_i=r_{i+1}-r_i\ge1\). Form the \(p\)-vertex weighted path Laplacian
\[
L=\sum_{i=1}^{p-1}\frac{(e_i-e_{i+1})(e_i-e_{i+1})^T}{d_i},\qquad A=\operatorname{diag}(\alpha_1,\ldots,\alpha_p).
\]
For \(p\ge2\), let \(L^+\) be its Moore--Penrose inverse. Then the number of localized modes, counting multiplicity, is exactly
\[
\boxed{N_{\rm loc}=1+n_+\!\left(\left.(4L^+-I-A^{-1})\right|_{\mathbf1^\perp}\right).}
\]
Here \(n_+\) counts strictly positive eigenvalues of the symmetric quadratic form on the ordinary Euclidean mean-zero subspace \(\mathbf1^\perp\). For \(p=1\), the answer is \(N_{\rm loc}=1\). Every such eigenmode is simple and its squared dimensionless frequency exceeds \(4\). A zero eigenvalue of the finite quadratic form is *not* a localized mode; it marks a band-edge resonance/threshold.

For \(p\) consecutive reinforced bonds of one common relative increment \(\alpha>0\), the exact count reduces to
\[
\boxed{N_{\rm loc}=\left\lceil\frac{2p}{\pi}\arctan\sqrt\alpha\right\rceil.}
\]
More precisely, its \((k+1)\)-st localized mode, for integer \(1\le k\le p-1\), exists if and only if
\[
\boxed{\alpha>\tan^2\!\left(\frac{k\pi}{2p}\right).}
\]
Equality is excluded. Consequently, at fixed \(\alpha\), the mode density of a long contiguous reinforced segment satisfies \(N_{\rm loc}/p\to (2/\pi)\arctan\sqrt\alpha\). Increasing any reinforcement or any separation between consecutive reinforced bonds cannot decrease \(N_{\rm loc}\).

## Assumptions and scope

The infinite site set is \(\mathbb Z\). Every mass is the same \(m>0\), and each ordinary nearest-neighbor spring has stiffness \(K>0\). The spring from site \(r_i\) to site \(r_i+1\) has stiffness \(K(1+\alpha_i)\), with *pairwise distinct* integer \(r_i\) and all \(\alpha_i>0\). No other springs, onsite potentials, damping, driving, or mass defects are present. The dimensionless spatial operator \(H\) acts on \(\ell^2(\mathbb Z)\); its eigenvalues are the dimensionless squared frequencies \(\lambda=m\omega^2/K\). The ordinary band is \([0,4]\), so the localized frequencies satisfy \(\omega>2\sqrt{K/m}\). All conclusions are uniform in finite \(p\ge1\), integer gaps, and positive increments; no large-separation or weak-contrast approximation is imposed.

## Proof

**1. Resolvent reduction.** Write \(H=H_0+BAB^*\), where \((H_0u)_n=2u_n-u_{n-1}-u_{n+1}\), \(B\) has columns \(b_i=e_{r_i}-e_{r_i+1}\), and \(A=\operatorname{diag}(\alpha_i)\). For \(\lambda>4\), put \(\lambda=2+2\cosh t\), \(t>0\). The free resolvent is
\[
(\lambda-H_0)^{-1}_{ab}=\frac{(-1)^{a-b}e^{-t|a-b|}}{2\sinh t}.
\]
Let \(M(t)=B^*(\lambda-H_0)^{-1}B\), and \(S=\operatorname{diag}((-1)^{r_i})\). Direct subtraction of the four free resolvent entries gives the *exact* formula
\[
\boxed{SM(t)S=\coth(t/2)E(t)-I,\quad E_{ij}(t)=e^{-t|r_i-r_j|}.}
\]
The Birman--Schwinger principle says that \(\lambda>4\) is an eigenvalue of \(H\) exactly when \(1\) is an eigenvalue of \(A^{1/2}M(t)A^{1/2}\), with matching multiplicity.

**2. Strict spectral crossings.** Differentiating with respect to \(\lambda\) yields
\[
\frac{d}{d\lambda}\left(A^{1/2}M A^{1/2}\right)
=-A^{1/2}B^*(\lambda-H_0)^{-2}BA^{1/2}\prec0.
\]
The strict inequality follows because the finite-support bond vectors \(b_i\) are linearly independent. Every ordered eigenvalue of the Birman--Schwinger matrix therefore decreases strictly as \(\lambda\) increases; each tends to zero as \(\lambda\to\infty\). The desired mode count equals the number of its limiting eigenvalues exceeding one as \(\lambda\downarrow4\).

**3. The singular band-edge matrix.** Write \(D_{ij}=|r_i-r_j|\), \(w=A^{1/2}\mathbf1\). Since \(E(t)=\mathbf1\mathbf1^T-tD+O(t^2)\) and \(\coth(t/2)=2/t+O(t)\), conjugation by \(S\) gives
\[
SA^{1/2}M(t)A^{1/2}S=\frac2tww^T+A^{1/2}(-2D-I)A^{1/2}+O(t).
\]
Thus precisely one eigenvalue diverges to \(+\infty\). By finite-dimensional Schur complement, the remaining \(p-1\) eigenvalues converge to the compression of \(A^{1/2}(-2D-I)A^{1/2}\) on \(w^\perp\). The criterion that a limiting eigenvalue is greater than \(1\) is a *positive* direction of \(A^{1/2}(-2D-I)A^{1/2}-I\) on \(w^\perp\). For \(y=A^{1/2}x\), the constraint \(x\perp w\) becomes \(y\perp\mathbf1\). Since \(A\) is invertible, this is congruent to the quadratic form \(-2D-I-A^{-1}\) on \(\mathbf1^\perp\).

**4. Exact path resistance identity.** With edge conductance \(1/d_i\), the effective resistance between vertices \(i,j\) of the weighted path equals \(|r_i-r_j|\), so
\[
D_{ij}=(e_i-e_j)^T L^+(e_i-e_j).
\]
For every \(y\in\mathbf1^\perp\), expand this expression and use \(\sum_i y_i=0\) to obtain \(y^TDy=-2y^TL^+y\). Therefore the finite form in Step 3 equals \(4L^+-I-A^{-1}\). Strict monotonicity in Step 2 excludes each exactly critical zero direction from the count. This proves the claimed all-parameter formula. The Jacobi recurrence, with all offdiagonal coefficients nonzero, makes an out-of-band eigenfunction unique up to scalar, so every localized eigenvalue is simple. Outside the finite defect region solutions at \(0\le\lambda\le4\) are oscillatory or at the band edges linear/alternating-linear, none square-summable; hence there are no other localized eigenvalues.

**5. Contiguous and monotone specializations.** If \(d_i=1\) and all increments equal \(\alpha\), the nonzero eigenvalues of \(L\) are \(4\sin^2(k\pi/(2p))\), \(1\le k\le p-1\). Thus a new mode appears precisely when \(1/\sin^2(k\pi/(2p))>1+1/\alpha\), equivalently \(\alpha>\tan^2(k\pi/(2p))\). Counting these strict inequalities, with the ever-present first mode, gives the ceiling formula *including exact thresholds*. Dividing by \(p\) gives the density limit. Increasing any \(\alpha_i\) increases \(-A^{-1}\); increasing any gap \(d_i\) decreases \(L\) on \(\mathbf1^\perp\) and consequently increases its inverse \(L^+\) there. Positive inertia therefore never decreases.

## Verification

The included standalone `check.py` uses two independent numerical representations: (a) the explicitly assembled weighted-path pseudoinverse inertia and (b) direct tridiagonal eigenanalysis of a long free-ended physical chain with the same bond perturbations. It additionally compares the closed contiguous-segment expression for ten sizes and six strengths and tests both monotonicity operations. The script reports `PASS: 104 independent count/formula/monotonicity checks` in Python with NumPy and SciPy. Finite truncations are diagnostics, **not** proof that no arbitrarily near-edge eigenvalues exist; the analytical Birman--Schwinger argument supplies that proof. Band-edge equality is handled strictly by the proof, not by numerical rounding.

## Relationship to prior work

Localized vibrational defect modes and the underlying harmonic-chain equations are classical. Boechler et al. [1] analyze experimental one- and two-particle defects in granular chains and approximate local frequencies using few-site models. Bjork [2] treats an impurity in a diatomic chain; Lipkin--Mannheim [3] prove general bounds for substitutional impurity modes in cubic crystals. The earlier two-reinforced-bond theorem for an equal-mass infinite chain has the count \(1+\mathbf1_{\{2(2d-1)\alpha\beta>\alpha+\beta\}}\), and is fully subsumed by the formula here when \(p=2\); it is **not** a new consequence by itself. Here the target result is the exact *arbitrarily many* independent bond contrasts and gaps, and especially the all-mode staircase for a whole contiguous reinforced segment. Matrix resolvent and effective-resistance identities are standard ingredients; no novelty is asserted for those tools separately.

## Limitations

The spring perturbations must be strictly positive, finite in number, and supported on a monatomic nearest-neighbor chain. Negative or zero stiffness changes, random infinitely extended defects, diatomic chains, phonon dissipation, and nonlinear localization are not covered. The result counts discrete modes but does not give their individual frequencies or normalized eigenvectors. Historical originality is assessed against inspected accessible sources, not independently certified; broader older unpublished or inaccessible impurity analyses could conceivably imply the theorem. Independent scientific validation has not been performed.

## References

[1] N. Boechler, G. Theocharis, Y. Man, P. G. Kevrekidis, C. Daraio, *Defect Modes in One-Dimensional Granular Crystals*, arXiv:1103.2483v1 (first publicly posted 2011-03-12), Phys. Rev. E 85, 037601 (2012), doi:10.1103/PhysRevE.85.037601. https://arxiv.org/abs/1103.2483

[2] R. L. Bjork, *Impurity-Induced Localized Modes of Lattice Vibration in a Diatomic Chain*, Phys. Rev. 105, 456 (1957), doi:10.1103/PhysRev.105.456. https://doi.org/10.1103/PhysRev.105.456

[3] H. J. Lipkin, P. D. Mannheim, *Bounds on Localized Modes in the Crystal Impurity Problem*, arXiv:cond-mat/0510542 (2005), Phys. Rev. B 73, 174105 (2006). https://arxiv.org/abs/cond-mat/0510542

[4] S. M. Lee, *Exact Normal-Mode Analysis for a Linear Lattice with Periodic Impurities*, Am. J. Phys. 37, 888–894 (1969), doi:10.1119/1.1975917. https://doi.org/10.1119/1.1975917
