# Tetrahedral spin-two harmonic sampling: exact Gram spectrum and a unique cubic blind mode

## Finding

Let \(V=\{(a,b,ab)/\sqrt3:a,b\in\{-1,1\}\}\subset S^2\), the four vertices of a regular tetrahedron. For each integer \(\ell\ge0\), let \(\mathcal H_\ell\) be the complex spherical harmonics of **exact** degree \(\ell\), equipped with the inner product of normalized spherical area measure. At each vertex evaluate the two independent components of the **trace-free intrinsic covariant Hessian**. This defines an eight-coordinate map \(T_\ell:\mathcal H_\ell\to\mathbb C^8\), specified explicitly below.

The rank at every degree is
\[
\boxed{\operatorname{rank}T_\ell=0\ (\ell=0,1),\quad 5\ (\ell=2),\quad 6\ (\ell=3),\quad 8\ (\ell\ge4).}
\]
Thus all eight complex quadrupolar curvature measurements can be interpolated independently starting at degree four. At degree three exactly one nonzero scalar harmonic is invisible: the kernel is spanned by the restriction of \(xyz\) to the sphere. This is different from sampling values, gradients, the full Hessian, or a band of mixed degrees.

More strongly, the normalized Gram operator \(G_\ell=(2\ell+1)^{-1}T_\ell T_\ell^*\) has exactly three eigenvalue expressions, with algebraic multiplicities \(2,3,3\):
\[
\begin{aligned}
\lambda_{\ell,A}&=D+\frac43Q-\frac{32}{9}R+\frac{32}{27}U,\\
\lambda_{\ell,B}&=D-4Q-\frac{32}{9}R-\frac{32}{27}U,\\
\lambda_{\ell,C}&=D+\frac{28}{9}Q+\frac{160}{27}R+\frac{32}{81}U,
\end{aligned}
\]
where \(P_\ell\) is the Legendre polynomial normalized by \(P_\ell(1)=1\) and
\[
D=4P_\ell''(1)=\frac{(\ell-1)\ell(\ell+1)(\ell+2)}2,\quad Q=P_\ell''(-1/3),\quad R=P_\ell'''(-1/3),\quad U=P_\ell''''(-1/3).
\]
The expressions are eigenvalues of the normalized, explicitly framed Gram matrix; the multiplication of harmonic inner products by a positive scalar changes all eigenvalues by that scalar but not the ranks.

## Assumptions and scope

Write \(v=(a,b,c)/\sqrt3\), where \(a,b,c\in\{-1,1\}\) and \(abc=1\). Use the orthonormal tangent frame
\[
u_v=(a,-b,0)/\sqrt2,\qquad w_v=(a,b,-2c)/\sqrt6.
\]
Let \(A_v=u_vu_v^{\mathsf T}-w_vw_v^{\mathsf T}\), \(B_v=u_vw_v^{\mathsf T}+w_vu_v^{\mathsf T}\), and \(\nabla^2_{S^2}f(v)\) denote the intrinsic covariant Hessian. The two observations at \(v\) are \(A_v:\nabla^2_{S^2}f(v)\) and \(B_v:\nabla^2_{S^2}f(v)\), with Frobenius contraction. They are twice the usual components of the trace-free Hessian in the orthonormal tangent frame; either convention has the same rank. The four ordered frames are those above, not independently rotated or rescaled frames.

The domain has complex dimension \(2\ell+1\). The codomain has complex dimension eight. No reality condition, band mixing, or antipodal identification is imposed. A sphere of unit radius and normalized area measure fix the Gram scale.

## Proof

**1. Differentiated addition theorem.** With normalized area measure, the degree-\(\ell\) reproducing kernel is \((2\ell+1)P_\ell(v\cdot z)\). For any tangent, symmetric, trace-free matrices \(A\) at \(v\) and \(B\) at \(z\), contractions by \(A,B\) kill the radial curvature terms in each intrinsic Hessian. Applying the two Hessian contractions to \(P_\ell(v\cdot z)\), followed by the product rule, gives the normalized Gram entry
\[
P_\ell''''(s)(z^{\mathsf T}Az)(v^{\mathsf T}Bv)
+4P_\ell'''(s)v^{\mathsf T}BAz
+2P_\ell''(s)\operatorname{tr}(AB),\qquad s=v\cdot z.
\]
The same formula holds on the diagonal. There, \(Av=Bv=0\), the two chosen matrices have squared Frobenius norm \(2\) and are Frobenius-orthogonal; hence each diagonal two-by-two Gram block is \(D I_2\).

**2. Exact tetrahedral block calculation.** The vertices are the orbit of \((1,1,1)/\sqrt3\) under the Klein four-group of diagonal even sign changes. The chosen tangent frames transform by those sign changes, so \(G_\ell\) is a four-by-four group-circulant matrix of two-by-two blocks. Each distinct vertex pair has inner product \(-1/3\). For the nonidentity sign changes \((+,-,-),(-,+,-),(-,-,+)\), put \(M=9Q+12R+2U\). Direct substitution into the previous displayed Gram identity gives
\[
\begin{aligned}
C_{+--}&=\begin{pmatrix}
-4Q/9-64R/27+16U/81&8\sqrt3 M/81\\
8\sqrt3 M/81&4Q/3+16U/27
\end{pmatrix},\\
C_{-+-}&=\begin{pmatrix}
-4Q/9-64R/27+16U/81&-8\sqrt3 M/81\\
-8\sqrt3 M/81&4Q/3+16U/27
\end{pmatrix},\\
C_{--+}&=\begin{pmatrix}
20Q/9+32R/27+64U/81&0\\
0&-4Q/3-32R/9
\end{pmatrix}.
\end{aligned}
\]
The group Fourier transform yields four two-by-two blocks. For the trivial character the block is \(\lambda_{\ell,A}I_2\). Each of the other three character blocks has trace \(\lambda_{\ell,B}+\lambda_{\ell,C}\) and determinant \(\lambda_{\ell,B}\lambda_{\ell,C}\), giving the asserted multiplicities. This explicit calculation is reproduced symbolically in `check_gram.py`.

**3. Exact low degrees.** The degree-zero and degree-one second derivatives are trace-free zero. Direct exact Legendre substitution gives the three Gram branches
\[
\begin{array}{c|ccc}
\ell&\lambda_{\ell,A}&\lambda_{\ell,B}&\lambda_{\ell,C}\\\hline
2&16&0&64/3\\
3&0&80/3&400/3\\
4&1280/3&560/3&80/9.
\end{array}
\]
For every integer \(4\le\ell\le24\), the exact rational recurrence of Legendre jets at \(-1/3\) gives \(\lambda_{\ell,j}\ge D/25>0\) for all three branches. Specifically initialize \(J_0=(1,0,0,0,0)\), \(J_1=(-1/3,1,0,0,0)\), and use, for derivative orders \(0\le r\le4\),
\[
(n+1)J_{n+1,r}=(2n+1)\left(-\tfrac13J_{n,r}+rJ_{n,r-1}\right)-nJ_{n-1,r},
\]
with \(J_{n,-1}=0\). The bundled standard-library exact-arithmetic checker tests every one of the 63 inequalities; it also independently constructs harmonic-polynomial nullspaces and evaluates all eight Hessian measurements at degrees zero through seven.

**4. Uniform high-degree positivity.** Set \(n=\ell\ge25\), \(x=-1/3\), and \(b=(n-1/2)^{-1/2}\). Bernstein's classical interior Legendre bound
\[
(1-x^2)^{1/4}|P_j(x)|\le\frac{2}{\sqrt{\pi(2j+1)}}
\]
implies \(|P_n(x)|,|P_{n-1}(x)|\le b\). The standard identity \((1-x^2)P_n'=n(P_{n-1}-xP_n)\) and successive differentiations of the Legendre ODE yield at this \(x\)
\[
|P_n'|\le\tfrac32nb,\quad
|P_n''|\le\tfrac54n^2b,\quad
|P_n'''|\le\tfrac{15}{8}n^3b,\quad
|P_n''''|\le\tfrac53n^4b.
\]
For transparency, the differentiated ODEs are \((1-x^2)P_n''-2xP_n'+n(n+1)P_n=0\), \((1-x^2)P_n'''-4xP_n''+(n(n+1)-2)P_n'=0\), and \((1-x^2)P_n''''-6xP_n''+(n(n+1)-6)P_n''=0\). The displayed derivative bounds follow by inserting \(|x|=1/3\), \(1-x^2=8/9\), and \(n\ge25\).

Also \(D\ge(12/25)n^4\) and \(b\le(51/50)n^{-1/2}\). Applying the triangle inequality separately to each of the three explicit Gram branches, and noting that each resulting upper bound decreases with \(n\), gives
\[
\frac{|\lambda_{n,A}-D|}{D}\le\frac{386359}{405000}<1,\quad
\frac{|\lambda_{n,B}-D|}{D}\le\frac{387277}{405000}<1,\quad
\frac{|\lambda_{n,C}-D|}{D}\le\frac{572713}{1215000}<1.
\]
These rational constants are the respective bounds evaluated at \(n=25\); they are reproducible directly from the derivative estimates. Thus every branch is strictly positive for all degrees \(n\ge25\). Together with step 3, full rank is proved for all \(\ell\ge4\).

**5. The cubic blind mode.** The homogeneous cubic \(xyz\) is harmonic. Its restriction is invariant under the tetrahedron's rotational group. The order-three stabilizer of each vertex acts on that vertex's tangent plane by a rotation through \(120^\circ\); an invariant trace-free symmetric two-tensor must be zero. Hence the trace-free Hessian of \(xyz\) vanishes at every vertex. Since degree three has dimension seven and the proved rank is six, its kernel is exactly the one-dimensional span of this cubic.

## Verification

Run `python3 check_exact.py` in this directory to check all Legendre-jet rational inequalities through degree 24 and directly compute the harmonic-polynomial Hessian sampling ranks for degrees zero through seven. Run `python3 check_gram.py` (requires SymPy) to derive all group-circulant blocks and symbolically verify the three-branch factorization. Both scripts were executed against the embedded sources. The two finite computations corroborate the proof; the Bernstein-ODE argument, not finite enumeration, proves the infinite tail.

## Relationship to prior work

The scalar spherical-harmonic addition theorem and coordinate-free tensor differentiation are classical. Pérez-Saborid's *The coordinate-free approach to spherical harmonics* (first publicly posted 2008-06-20) develops the scalar addition theorem and tensorial methods, but does not determine trace-free Hessian sampling ranks at tetrahedral vertices. Bouzas's *Addition theorems for spin spherical harmonics. II Results* (first posted 2011-03-15) supplies more general tensor/spin bilocal addition identities, but not the tetrahedral eight-measurement Gram spectrum or its degree-three kernel. Monteverdi and Winstanley (2024) likewise give spin-weighted addition identities; those identities alone do not assert the specific finite-orbit rank threshold. The theorem here evaluates a concrete geometric operator, decomposes its finite symmetry, and resolves nonvanishing simultaneously for all degrees.

## Limitations

This is a result for the trace-free intrinsic Hessian only, at the four stated tetrahedral points. It does not claim full-jet interpolation, stability bounded uniformly in degree, other Platonic configurations, mixed-degree signal recovery, or originality certified by independent literature review. The normalized Gram eigenvalue formulas are coordinate/frame dependent up to the evident orthogonal re-framings, although ranks are intrinsic. Unindexed older angular-momentum or finite-group sampling tables could contain equivalent spectral information. No independent mathematical audit has been conducted.

## References

1. M. Pérez-Saborid, *The coordinate-free approach to spherical harmonics*, arXiv:0806.3367, first version 2008-06-20; in particular §§II and V.
2. A. O. Bouzas, *Addition theorems for spin spherical harmonics. II Results*, arXiv:1103.2983, first version 2011-03-15; in particular §§1 and 4.
3. A. Monteverdi and E. Winstanley, *Some Addition Theorems for Spin-Weighted Spherical Harmonics*, Universe **10** (2024), 461, DOI:10.3390/universe10120461.
4. G. Szegő, *Orthogonal Polynomials*, fourth edition, American Mathematical Society, 1975, §7.3 (classical Bernstein bounds for Legendre polynomials).
