# Exact dodecahedral harmonic sampling: signed-Petersen spectra and sharp stability

## Finding

Let \(X\subset S^2\) be the complete set of 20 vertices of a regular dodecahedron, with the normalization and coordinates below. For every integer \(\ell\geq0\), let \(\mathcal H_\ell\) be the real degree-exactly-\(\ell\) spherical harmonics, equipped with probability surface-measure norm, and define
\[
E_\ell:\mathcal H_\ell\longrightarrow\mathbb R^{20},\qquad
(E_\ell f)_x=\frac{f(x)}{\sqrt{2\ell+1}}.
\]
Write \(a_\ell=P_\ell(\sqrt5/3)\), \(b_\ell=P_\ell(1/3)\), where \(P_\ell\) is the standard Legendre polynomial normalized by \(P_\ell(1)=1\). The complete spectrum of \(G_\ell=E_\ell E_\ell^*\), including multiplicities, is as follows.

For **even** \(\ell\), there are ten zero eigenvalues from antipodal parity, together with
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
2(1+3a_\ell+6b_\ell)&1\\
2(1+a_\ell-2b_\ell)&5\\
2(1-2a_\ell+b_\ell)&4
\end{array}.
\]
For **odd** \(\ell\), there are ten zero eigenvalues from antipodal parity, together with
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\\hline
2(1+\sqrt5a_\ell+2b_\ell)&3\\
2(1-\sqrt5a_\ell+2b_\ell)&3\\
2(1-3b_\ell)&4
\end{array}.
\]
Any displayed nonparity eigenvalue can itself be zero. All displayed eigenvalues are rational numbers.

The **complete rank law** is
\[
\operatorname{rank}E_\ell=
\begin{cases}
2\ell+1,&0\leq\ell\leq4,\\
6,&\ell=5,\\
9,&\ell\in\{8,14\},\\
10,&\ell\geq6,\ \ell\notin\{8,14\}.
\end{cases}
\]
Thus degree \(15\) is the sharp threshold for full sampling onto all ten antipodally compatible data coordinates at **every** subsequent degree; full rank already occurs at degree \(6\), but fails again at degrees \(8\) and \(14\).

The sharp uniform bound over every degree and every strictly positive Gram eigenvalue is
\[
\boxed{\lambda_{\min}^{+}(G_\ell)\geq\frac{6188}{1594323}},
\]
with equality **only at degree \(13\)**, on one three-dimensional symmetry sector. Equivalently, for every \(\ell\geq0\) and \(y\in\operatorname{ran}E_\ell\),
\[
\min\{\|f\|_{L^2(S^2)}: E_\ell f=y\}
\leq \sqrt{\frac{1594323}{6188}}\,\|y\|_{\ell^2(X)},
\]
and this common interpolation factor is optimal.

## Assumptions and scope

Put \(\varphi=(1+\sqrt5)/2\). The unnormalized vertices are the eight triples \((\pm1,\pm1,\pm1)\) and the twelve cyclic-coordinate permutations of \((0,\pm\varphi^{-1},\pm\varphi)\) with independent signs. Each has squared norm \(3\), so divide all coordinates by \(\sqrt3\). The standard probability surface measure has mass one, hence \(\dim\mathcal H_\ell=2\ell+1\). The bound concerns only **strictly positive** squared singular values; every degree has a ten-dimensional, parity-incompatible data nullspace, and degrees with incomplete parity rank have additional null directions.

## Proof

**1. Kernel reduction.** The spherical-harmonic addition formula in dimension three gives
\[
\sum_{j=1}^{2\ell+1}Y_j(x)Y_j(y)=(2\ell+1)P_\ell(x\cdot y)
\]
for any orthonormal real harmonic basis. Consequently \((G_\ell)_{x,y}=P_\ell(x\cdot y)\). Antipodal parity \(P_\ell(-t)=(-1)^\ell P_\ell(t)\) leaves ten zero eigenvalues and identifies the active operator with twice a \(10\)-by-\(10\) representative-vertex matrix \(Q_\ell\).

**2. The two finite incidence algebras.** Choose one representative from each antipodal vertex pair. Their off-diagonal absolute inner products are precisely \(\sqrt5/3\) (three neighbors per representative) and \(1/3\) (six other representatives). Let \(A\) be the zero-one adjacency matrix for the three larger-inner-product neighbors. Let \(B\) have the same support, with entries equal to the sign of the corresponding inner products, and let \(C\) have the signed entries on the six remaining off-diagonal positions. Entrywise verification from the 20 exact vertices yields
\[
A^2=2I-A+J,\qquad B^2=3I+C,\qquad B^3=5B,
\]
where \(J\) is the all-ones matrix. The diagonal of each of \(A,B,C\) is zero; \(\operatorname{tr}B=0\) and \(\operatorname{tr}(B^2)=30\). Thus \(A\) has eigenvalues \(3,1,-2\) with multiplicities \(1,5,4\); the signed \(B\) has eigenvalues \(\sqrt5,-\sqrt5,0\) with multiplicities \(3,3,4\), and \(C=B^2-3I\) acts by \(2,2,-3\) on those three sectors. These identities are also checked entry by entry in the standalone exact-arithmetic verifier.

For even \(\ell\), \(Q_\ell=I+a_\ell A+b_\ell(J-I-A)\). For odd \(\ell\), \(Q_\ell=I+a_\ell B+b_\ell C\). Substitution of the spectra gives every listed branch and multiplicity. Since \(P_{2m}(\sqrt5/3)\) and \(\sqrt5P_{2m+1}(\sqrt5/3)\) are rational, so are the final eigenvalues.

**3. Finite exact arithmetic and exceptional ranks.** All branches are computed through degree \(186\) by the recurrence
\[
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t),
\qquad P_0(t)=1,\quad P_1(t)=t.
\]
The verifier represents \(P_\ell(\sqrt5/3)\) as a pair of rational coefficients of \(1,\sqrt5\), so *no floating-point zero or sign test occurs*. It exhaustively checks all \(561\) branch values for \(0\leq\ell\leq186\); it detects the zero sectors exactly at degrees \(0,1,2,3,4,5,8,14\) with the specified multiplicities, and finds the smallest strictly positive eigenvalue of \(Q_\ell\) to be \(3094/1594323\), uniquely at degree \(13\), multiplicity three. The finite arithmetic claim is established by the transparent, terminating, standard-library-only code `code/verify.py`, rather than by incomplete numerical sampling.

**4. Rigorous infinite tail.** The classical Laplace representation of Legendre polynomials, with \(t=\cos\theta\), is
\[
P_\ell(t)=\frac1\pi\int_0^\pi
(\cos\theta+i\sin\theta\cos u)^\ell\,du.
\]
For \(\ell\geq1\), its absolute value is bounded by
\[
|P_\ell(t)|\leq\frac1\pi\int_0^\pi
\exp\!\left(-\frac{\ell(1-t^2)\sin^2u}{2}\right)du
\leq\sqrt{\frac{\pi}{2\ell(1-t^2)}}.
\]
The last inequality follows from \(\sin u\geq(2/\pi)\min(u,\pi-u)\) and a Gaussian-integral bound. In every representative matrix, the sum of absolute off-diagonal entries is
\[
3|a_\ell|+6|b_\ell|\leq\sqrt{\frac{\pi}{2\ell}}\left(\frac92+\frac9{\sqrt2}\right)<\sqrt{\frac{186}{\ell}}.
\]
Here the last inequality follows, for instance, from \(\pi<22/7\) and \(\sqrt2>140/99\). By Gershgorin, for every \(\ell\geq187\), every active eigenvalue of \(Q_\ell\) is at least \(1-\sqrt{186/\ell}\). The exact inequality
\[
\left(1-\frac{3094}{1594323}\right)^2>\frac{186}{187}
\]
shows that this lower bound exceeds \(3094/1594323\) on the entire infinite tail. Therefore no further rank defects occur, and the finite minimum at degree \(13\) is the sharp all-degree positive spectral lower bound. Doubling it proves the claim for \(G_\ell\). The minimum-norm interpolation assertion is the singular-value characterization of the Moore–Penrose inverse.

## Verification

From the directory containing this document, run `python3 code/verify.py`. The script uses only the Python standard library; it builds all vertices in exact \(\mathbb Q(\sqrt5)\), verifies all claimed finite matrix identities entrywise, calculates all rational spectral branches through degree \(186\), checks the exact zero/rank list and global finite minimum, and checks the rational inequalities supporting the infinite tail. Its expected output is `code/verification_output.txt`. This is a finite rational certificate plus a separately proved analytic bound, **not** an extrapolation from floating-point experiments.

## Relationship to prior work

Dai and Xu (2013) give the spherical-harmonic addition formula and discuss fundamental systems and general harmonic interpolation, but no fixed dodecahedral all-degree spectrum. Bannai, Okuda and Tagami (2013) develop harmonic-index spherical designs and explicitly note icosahedral vanishing at degrees \(8\) and \(14\), reflecting classical icosahedral invariant theory; such low-degree first-moment cancellation is **not** claimed to be new here. Bates, Khalid and Kennedy (2015) study antipodally symmetric *bandlimited* spherical reconstruction on constructed iso-latitude grids, not exact-degree dodecahedral evaluation. The present statement concerns the full 20-point signed-Petersen spectral decomposition, all-degree rank, and the global sharp lower *positive* singular value. Known association-scheme methods and Legendre recurrence identities are used as inputs, not claimed as new techniques.

## Limitations

The result concerns the complete regular dodecahedron with uniform normalized point evaluation; it says nothing about arbitrary point subsets, mixed degrees, noise models beyond least-norm linear stability, or other polyhedral orbits. The bound does not make rank-deficient sample vectors attainable. Publication priority is qualified because an older icosahedral association-scheme computation might contain an equivalent spectral statement under a different normalization; an independent historical-literature check is still desirable.

## References

1. F. Dai and Y. Xu, *Spherical Harmonics*, arXiv:1304.2585v1, first submitted 2013-04-09, https://arxiv.org/abs/1304.2585. In particular the addition formula and fundamental-system discussion in Sections 2–3.
2. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101v1, first submitted 2013-08-23, https://arxiv.org/abs/1308.5101. Introduction on icosahedral harmonic-index \(8,14\) and Theorems 1–2.
3. A. P. Bates, Z. Khalid and R. A. Kennedy, *An Optimal Dimensionality Sampling Scheme on the Sphere for Antipodal Signals in Diffusion Magnetic Resonance Imaging*, arXiv:1502.07099v1, first submitted 2015-02-25, https://arxiv.org/abs/1502.07099.
