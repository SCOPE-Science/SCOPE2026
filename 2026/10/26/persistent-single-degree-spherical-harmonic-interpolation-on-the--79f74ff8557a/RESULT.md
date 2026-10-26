# Persistent single-degree spherical-harmonic interpolation on the truncated octahedron

## Finding
Let \(X\subset S^2\) comprise the 24 normalized coordinate permutations of \((0,\pm1,\pm2)/\sqrt5\), the vertices of the regular truncated octahedron. For every integer \(\ell\ge0\), let \(\mathcal H_\ell\) denote the real spherical harmonics of **exact degree** \(\ell\), and let \(E_\ell:\mathcal H_\ell\to\mathbb R^X\) be their evaluation map.

Then
\[
\operatorname{rank}E_\ell=\begin{cases}
1,&\ell=0,\\
3,&\ell=1,\\
5,&\ell=2,\\
6,&\ell=3,\\
9,&\ell=4,5,\\
10,&\ell=6,\\
12,&\ell=7,\\
11,&\ell=8,\\
12,&\ell\ge9.
\end{cases}
\]

The maximum rank of 12 is imposed by antipodal parity. Thus degree 7 is the first degree that can interpolate all data of its antipodal parity, degree 8 exhibits a genuine one-dimensional rank defect, and \(\ell=9\) is the sharp **persistent** interpolation threshold: every degree at least 9 interpolates all parity-compatible data on \(X\).

An explicit obstruction at degree 8 is the sample-value vector of the polynomial
\[
H(x,y,z)=(x^2-y^2)(y^2-z^2)(z^2-x^2),
\]
which is a nonzero homogeneous harmonic polynomial of degree 6. Its values on \(X\) are orthogonal to the values of *every* degree-8 spherical harmonic; their 24-dimensional vector spans the sole parity-compatible missing data direction.

## Assumptions and scope
All points lie on the Euclidean unit two-sphere. The Legendre polynomial \(P_\ell\) has \(P_\ell(1)=1\). A datum \(f:X\to\mathbb R\) is parity compatible in degree \(\ell\) when \(f(-x)=(-1)^\ell f(x)\). The statement concerns interpolation by one *homogeneous* spherical-harmonic degree, not by all degrees up to a cutoff, and it makes no claim of numerical conditioning.

## Proof
**Addition formula and antipodal reduction.** With any orthonormal basis \(Y_{\ell m}\) of degree-\(\ell\) harmonics, the spherical addition theorem states
\[
P_\ell(x\cdot y)=\frac{4\pi}{2\ell+1}\sum_{m=-\ell}^{\ell}Y_{\ell m}(x)Y_{\ell m}(y).
\]
Consequently \(G_\ell=(P_\ell(x\cdot y))_{x,y\in X}\) is the positive-semidefinite evaluation Gram matrix and has rank \(\operatorname{rank}E_\ell\). Write \(X=R\sqcup(-R)\), with \(|R|=12\) representatives, and \(B_\ell=(P_\ell(r\cdot s))_{r,s\in R}\). Since \(P_\ell(-t)=(-1)^\ell P_\ell(t)\), the full Gram matrix is permutation-conjugate to
\[
\begin{pmatrix}B_\ell&(-1)^\ell B_\ell\\(-1)^\ell B_\ell&B_\ell\end{pmatrix}.
\]
Its rank is exactly the rank of \(B_\ell\), and every parity-compatible datum can be interpolated exactly when \(B_\ell\) is nonsingular.

**Finite rational certificate.** Each normalized pairwise dot product is a rational number of the form \(j/5\), where \(j\in\{-5,-4,\ldots,5\}\), so every \(B_\ell\) has rational entries. Starting with \(P_0(t)=1\), \(P_1(t)=t\), use
\[
(\ell+1)P_{\ell+1}(t)=(2\ell+1)tP_\ell(t)-\ell P_{\ell-1}(t).
\]
The attached standalone checker constructs the vertices, constructs representatives without dependence on their order, computes Legendre values with exact rational arithmetic, and applies exact row reduction to \(B_\ell\), individually for every \(0\le\ell\le128\). It obtains precisely the ranks stated above. In addition, for \(\ell=8\), it checks the **exact** identity \(B_8 H|_R=0\) with \(H|_R\ne0\). The one-dimensionality follows from the certified rank 11. The polynomial \(H\) is harmonic because it is alternating in \(x^2,y^2,z^2\): applying the symmetric Laplacian would produce an alternating polynomial of degree 4 in \(x,y,z\), which must vanish since the smallest nonzero alternating polynomial in the three squared variables has total degree 6.

**Exhaustive large-degree bound.** If \(r,s\in R\) are distinct then \(|r\cdot s|\le4/5\), so \(\sqrt{1-(r\cdot s)^2}\ge3/5\). The classical Bernstein bound for Legendre polynomials, for \(\ell\ge1\) and \(|t|<1\), gives
\[
|P_\ell(t)|\le\left(\frac{2}{\pi\ell\sqrt{1-t^2}}\right)^{1/2}.
\]
Thus every off-diagonal row sum of \(B_\ell\) is at most \(11\sqrt{10/(3\pi\ell)}<1\) for every integer \(\ell\ge129\); the final strict inequality is already certified by the classical rational bound \(\pi>223/71\), since \(1210\cdot71<3\cdot223\cdot129\). Its diagonal entries are 1, so strict diagonal dominance and Hermitian symmetry imply positive definiteness and rank 12 for all such degrees. The exact finite calculation and this uniform tail bound jointly exhaust all \(\ell\ge0\).

## Verification
Run `python checker.py` using Python 3 and the standard library. This re-derives the entire 24-point configuration and performs the 129 exact rational rank computations. The checker independently verifies the degree-eight null vector and the explicit strict inequality at the Bernstein/Gershgorin threshold. Its output is not used in place of the proven analytic tail bound. The rank result is a statement about exact arithmetic, not floating-point singular values.

## Relationship to prior work
Spherical interpolation and exact harmonic transforms are studied by An, Chen, Sloan and Womersley (2010) and by Khalid, Kennedy and McEwen (2014). Their results concern general design/interpolation schemes and mixed-degree bandlimits rather than the pure-degree rank profile of this specific 24-vertex Archimedean configuration. Standard addition-theorem methods establish positivity but do not determine these ranks. The distinction between single-degree interpolation and low-pass interpolation is essential here: the former loses one rank exactly at degree 8 after achieving full parity rank at degree 7.

## Limitations
The proof is specific to normalized permutations of \((0,\pm1,\pm2)\). It does not establish optimal placement of sample nodes, estimates on singular values, or rank formulas for other Archimedean solids. The evidence for novelty is a bounded comparison with identified primary and indexed sources, not a proof of worldwide uniqueness. An independent mathematical audit has not been conducted.

## References
- C. An, X. Chen, I. H. Sloan, R. S. Womersley, *Well Conditioned Spherical Designs for Integration and Interpolation on the Two-Sphere*, SIAM Journal on Numerical Analysis 48 (2010), 2135–2157, DOI 10.1137/100795140; online publication 2010-12-14.
- Z. Khalid, R. A. Kennedy, J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, arXiv:1403.4661, publicly posted 2014-03-19.
- G. Szegő, *Orthogonal Polynomials*, Theorem 7.3.3, classical Bernstein-type bound for Legendre polynomials.
- W. Gautschi and C. Giordano, *Luigi Gatteschi’s work on asymptotics of special functions and their zeros*, Numer. Algorithms (2008), DOI 10.1007/s11075-008-9208-5, equation (56), Legendre Bernstein bound.
