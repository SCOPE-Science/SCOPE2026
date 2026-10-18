# An eighth-degree harmonic blind spot on truncated-octahedral orbits

## Finding

Let \(S^2\subset\mathbb R^3\) have probability surface measure and let \(\mathcal H_\ell\) be the complex vector space of restrictions of homogeneous harmonic polynomials of **exact** degree \(\ell\ge0\). Let
\[
V_t=\left\{\frac{g(0,1,t)}{\sqrt{1+t^2}}:g\text{ is a signed coordinate permutation}\right\},\qquad t>1.
\]
Its \(24\) vertices form \(12\) antipodal pairs. Choose representatives \(X_t\) whose first nonzero coordinate is positive; let \(E_{\ell,t}:\mathcal H_\ell\to\mathbb C^{X_t}\) be point evaluation. The case \(t=2\) consists of the normalized vertices of a regular truncated octahedron.

**Theorem (symmetry-protected obstruction and exact recovery).** For **every** real \(t>1\), the image of \(E_{8,t}\) lies in the hyperplane
\[
 \sum_{x\in X_t}\varepsilon(x)y(x)=0,\qquad
 \varepsilon(x)=\operatorname{sgn}\!\bigl[(x_1^2-x_2^2)(x_2^2-x_3^2)(x_3^2-x_1^2)\bigr].
\]
For the regular truncated octahedron \(t=2\), the ranks are exactly
\[
\bigl(\operatorname{rank}E_{0,2},\ldots,\operatorname{rank}E_{8,2}\bigr)
 =(1,3,5,6,9,9,10,12,11),
\]
and \(\operatorname{rank}E_{\ell,2}=12\) for **every** integer \(\ell\ge9\). At degree \(8\), the displayed sign relation is the **only** restriction on compatible samples. Thus degree \(7\) is the first surjective degree, degree \(8\) loses one data dimension, and degree \(9\) is the sharp permanent-surjectivity threshold.

Moreover, for **every transcendental real** \(t>1\), degrees \(7\) and all degrees \(\ell\ge9\) are surjective, whereas degree \(8\) has rank exactly \(11\) and the same unique sign constraint. More generally, for each fixed degree among \(7,8,9,10,\ldots\), the same rank assertion holds outside a finite set of algebraic parameters \(t\); the union of the exceptional sets is at most countable. No claim is made that exceptional algebraic parameters other than \(2\) have been completely classified.

## Assumptions and scope

The evaluation space is one homogeneous **spherical-harmonic degree**, not the cumulative polynomial band through that degree. Each complex-valued harmonic satisfies \(h(-x)=(-1)^\ell h(x)\), so data on all \(24\) vertices must have the same antipodal parity and are identified with arbitrary data on \(X_t\). The rank is independent of which antipodal representative is selected. For the concrete \(t=2\) computation, \(X_2\) is ordered lexicographically as
\[
\begin{gathered}
(0,1,-2),(0,1,2),(0,2,-1),(0,2,1),\\
(1,-2,0),(1,0,-2),(1,0,2),(1,2,0),\\
(2,-1,0),(2,0,-1),(2,0,1),(2,1,0),
\end{gathered}
\]
with each vector divided by \(\sqrt5\). Thus every normalization and every matrix entry is rational.

## Proof

**Step 1: a forbidden alternating harmonic at degree eight.** Define the homogeneous degree-six alternant
\[
 \Delta(x)=(x_1^2-x_2^2)(x_2^2-x_3^2)(x_3^2-x_1^2).
\]
It is invariant under independent coordinate sign changes and changes sign under odd coordinate permutations. Any polynomial with this character must be even in each coordinate and divisible by \(\Delta\) (alternation in the three squared variables). Therefore every such homogeneous polynomial of degree \(8\) is a multiple of \(\|x\|^2\Delta(x)\), since its quotient must be a symmetric homogeneous polynomial of degree \(2\). The Laplacian preserves this character. Because there is no nonzero alternant of degree \(4\), \(\Delta\) is harmonic, and the direct identity
\[
 \nabla^2\bigl(\|x\|^2\Delta(x)\bigr)=30\Delta(x)
\]
shows that **no nonzero harmonic polynomial of degree eight** carries this alternating character.

Average any \(h\in\mathcal H_8\) against the coordinate-permutation sign character over the signed-permutation group. Its alternating projection vanishes by the preceding argument. Evaluating that projection at the orbit seed \((0,1,t)/\sqrt{1+t^2}\), and noting that the seed stabilizer only flips the zero coordinate, gives
\[
 \sum_{x\in V_t}\varepsilon(x)h(x)=0.
\]
Both \(h\) and \(\varepsilon\) are even under the antipodal map, so this is twice the stated equation on \(X_t\). Since all three squared coordinate magnitudes are distinct, the weights are nonzero signs. The constraint holds at every \(t>1\), without a finite computation.

**Step 2: exact evaluation ranks from the addition kernel.** The spherical-harmonic addition theorem with probability measure gives the reproducing kernel
\[
 K_\ell(x,z)=(2\ell+1)P_\ell(\langle x,z\rangle),
\]
where \(P_\ell\) is the standard Legendre polynomial normalized by \(P_\ell(1)=1\). Consequently, the evaluation Gram matrix is \((2\ell+1)B_\ell\) with
\[
 (B_\ell)_{ij}=P_\ell(\langle x_i,x_j\rangle),\qquad x_i,x_j\in X_2.
\]
It is positive semidefinite, and \(\operatorname{rank}B_\ell=\operatorname{rank}E_{\ell,2}\). All its contacts belong to \(\{0,\pm1/5,\pm2/5,\pm3/5,\pm4/5,1\}\); no off-diagonal contact has absolute value greater than \(4/5\).

Exact rational elimination with the standard Legendre recurrence
\[
 P_0(z)=1,\quad P_1(z)=z,\quad
 (n+1)P_{n+1}(z)=(2n+1)zP_n(z)-nP_{n-1}(z)
\]
gives the nine ranks \((1,3,5,6,9,9,10,12,11)\) at degrees \(0\) through \(8\). In degree \(8\) the nullspace is one-dimensional and is generated by the preceding alternant sign vector. The attached exact-arithmetic program reconstructs all twelve representatives and all matrices; no empirical tolerance is used.

**Step 3: finite exact nonsingularity certificate.** For **each** of the \(520\) degrees \(9\le\ell\le528\), reduce the rational Legendre recurrence modulo either prime \(1000000007\) or \(1000000009\), invert each denominator modulo that prime, form the \(12\)-by-\(12\) matrix \(B_\ell\), and use modular Gaussian elimination. The attached checker actually establishes **nonzero determinants for every one of these degrees modulo both primes**. All recurrence denominators and coordinate denominators \(5\) are units modulo these primes; hence a nonzero determinant modulo either prime proves that the original rational determinant is nonzero. This finite range is completely checked, not extrapolated.

**Step 4: infinite-degree positivity.** For \(-1<z<1\), the Laplace integral representation yields
\[
 P_\ell(z)=\frac1\pi\int_0^\pi
 \bigl(z+i\sqrt{1-z^2}\cos u\bigr)^\ell\,du.
\]
Taking absolute values, using \(1-s\le e^{-s}\) and \(\sin u\ge2u/\pi\) on \([0,\pi/2]\), then extending the Gaussian integral, gives for every \(\ell\ge1\)
\[
 |P_\ell(z)|\le\sqrt{\frac{\pi}{2\ell(1-z^2)}}.
\]
For the contacts on \(X_2\), each off-diagonal entry of \(B_\ell\) is thus at most \(\sqrt{25\pi/(18\ell)}\) in absolute value. If \(\ell\ge529\), then
\[
 11^2\frac{25\pi}{18\ell}
 \le\frac{3025\cdot22}{18\cdot7\cdot529}
 =\frac{33275}{33327}<1.
\]
Every diagonal entry is \(1\), so the matrix is strictly diagonally dominant and symmetric positive definite. Combining Steps 2--4 proves all unrestricted ranks and the sharp permanent threshold.

**Step 5: generic orbit parameters.** For fixed \(\ell\), every Gram entry at \(t>1\) is a rational function in \(t\) with coefficients in \(\mathbb Q\), because all representatives are coordinate permutations of \((0,\pm1,\pm t)/\sqrt{1+t^2}\), and their dot products divide an integer polynomial by \(1+t^2\). The Gram determinant at \(t=2\) is nonzero for \(\ell=7\) and every \(\ell\ge9\), so none of the corresponding rational determinant numerators vanishes identically. Each such polynomial has finitely many real roots. Likewise, an \(11\)-by-\(11\) minor of \(B_8(t)\) is nonzero at \(t=2\); combined with the universal alternant obstruction, its rank is \(11\) away from finitely many algebraic parameter roots. A transcendental real \(t>1\) avoids **all** these algebraic roots simultaneously. This proves the generic assertions.

## Verification

The self-contained file `check_sampling.py` is executed with `python check_sampling.py`; it requires Python 3 and SymPy. The checker enumerates the \(24\) signed-permutation vertices, the \(12\) antipodal representatives, exact pairwise contacts, exact ranks in degrees \(0\) through \(8\), and the one-dimensional alternant nullspace at degree \(8\). It then evaluates the Legendre recurrence and determinants in the finite prime fields for **all \(520\) degrees** in \([9,528]\), under **two** independently chosen primes. A completed execution reported no failed assertion, and the certificate SHA-256 for the concatenated modular determinant residues is `db404eb282a54c7cb605520f99a6c727a841e6f1c0bfc50e3635aa7414e9ee01`. The analytic bound, the signed-symmetry argument and the genericity argument above are mathematical proofs, not conclusions drawn from bounded computation.

For any attainable representative data vector \(y\), put \(B_\ell=(P_\ell(\langle x_i,x_j\rangle))\) and let \(B_\ell^\dagger\) be its Moore--Penrose inverse. The unique minimum-\(L^2(S^2)\)-norm interpolant is
\[
 h_y(z)=\sum_{i=1}^{12}P_\ell(\langle z,x_i\rangle)
 (B_\ell^\dagger y)_i,
 \qquad
 \|h_y\|_{L^2}^2=\frac1{2\ell+1}\,y^*B_\ell^\dagger y.
\]
In particular, for \(\ell=8,t=2\), attainability is exactly the single alternating relation and no other linear constraint.

## Relationship to prior work

Polynomial interpolation on \(S^2\) is studied by zu Castell, Laín Fernández and Xu (arXiv:math/0407448, first posted 27 July 2004). Their inspected Theorem 3.1 constructs unisolvent configurations on finitely many paired latitudes for **cumulative-degree polynomial spaces**; the result does not imply an exact-degree interpolation rank on the truncated-octahedral orbit. Ganesh and Mhaskar (SIAM J. Numer. Anal. 44 (2006), DOI 10.1137/050624005) describe trigonometric interpolation and quadrature constructions in the accessible abstract, which does not itself supply the alternating rank obstruction here; their full article was not inspected. Bannai, Okuda and Tagami (arXiv:1308.5101, first posted 23 August 2013) define harmonic-index spherical designs and normalized reproducing kernels; their inspected definitions and examples concern **unweighted vanishing sums** and design cardinalities, not the signed alternant obstruction and complete \(24\)-vertex rank sequence established here. The signed-permutation vertex geometry is the standard regular truncated octahedron. More general principles of finite reflection-group harmonic invariants are background to the explicit alternant proof rather than being claimed new.

## Limitations

No classification of every exceptional algebraic ratio \(t>1\), all singular values, optimal conditioning, or interpolation after sample erasures is claimed. The degree-by-degree full classification beyond degree eight is established explicitly for \(t=2\), while the parameter-family statement is generic (in particular transcendental), not uniform across every algebraic ratio. The finite modular checks concern only degrees \(9\) through \(528\); the independent analytical argument is necessary for all higher degrees. An equivalent version might be implicit in classical signed-permutation representation tables; an exhaustive historical priority proof is not claimed.

## References

1. W. zu Castell, N. Laín Fernández, Y. Xu, *Polynomial Interpolation on the Unit Sphere II*, arXiv:math/0407448 (first public preprint 27 July 2004), https://arxiv.org/abs/math/0407448.
2. M. Ganesh and H. N. Mhaskar, *Matrix-free Interpolation on the Sphere*, SIAM J. Numer. Anal. 44 (2006), 1314--1331, https://doi.org/10.1137/050624005 (online 25 July 2006).
3. E. Bannai, T. Okuda and M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101 (first public preprint 23 August 2013), https://arxiv.org/abs/1308.5101.
4. G. Ruffini, J. Marco and C. Grau, *Spherical Harmonics Interpolation, Computation of Laplacians and Gauge Theory*, arXiv:physics/0206007 (first public preprint 3 June 2002), https://arxiv.org/abs/physics/0206007; contextual interpolation source; only its abstract was inspected, which does not state an exact-degree rank classification.
