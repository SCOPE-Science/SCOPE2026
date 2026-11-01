# A two-resonance law for degree-nine cubic-orbit harmonics and complete truncated-cube ranks

## Finding

For real \(r>0\), \(r\ne1\), let \(X_r\) be the 24 distinct points obtained by taking all signed coordinate permutations of \((r,1,1)/\sqrt{r^2+2}\) on the unit sphere. Let \(E_k(r)\) evaluate every real spherical harmonic of **exactly** degree \(k\) on these points. The following distinct conclusions hold.

1. For degree nine, the two-dimensional signed position-contrast subspace, defined below, is annihilated by \(E_9(r)^T\) **if and only if** \(r=\sqrt2-1\) or \(r=\sqrt2+1\). At each of these two parameters the degree-nine evaluation rank is **exactly ten**. These configurations are respectively the regular truncated cube and the rhombicuboctahedron. The annihilation criterion is not asserted to classify every possible rank defect at other values of \(r\).
2. For the truncated-cube parameter \(r=\sqrt2-1\), the **complete exact-degree rank sequence** is
\[
\operatorname{rank}E_k(\sqrt2-1)=
\begin{cases}
2k+1,&0\le k\le5,\\
10,&k=9,\\
12,&k=6,7,8\text{ or }k\ge10.
\end{cases}
\]
In particular, interpolation onto antipodally compatible values is surjective for all exact degrees at least six **except** degree nine. No assertion is made about arbitrary data on 24 points: a single exact-degree harmonic has even or odd parity.

The continuous-parameter contrast obstruction has the exact nonnegative factorization
\[
\boxed{\displaystyle
\Phi(r)=\frac{19305\,r^2(r^2-1)^2(r^4-6r^2+1)^2}{4(r^2+2)^9}.}
\]
The parameter-uniform identity is the central distinction from an isolated sampling-rank computation for one Archimedean solid.

## Assumptions and scope

Use the Legendre normalization \(P_k(1)=1\), with
\[
P_9(t)=\frac{12155t^9-25740t^7+18018t^5-4620t^3+315t}{128}.
\]
For \(r>0\), set \(D=r^2+2\) and define representatives with positive first coordinate, partitioned into three four-point blocks:
\[
\begin{split}
u_{1,\epsilon,\eta}&=(r,\epsilon,\eta)/\sqrt D,\\
\nu_{2,\epsilon,\eta}&=(1,\epsilon r,\eta)/\sqrt D,\\
\nu_{3,\epsilon,\eta}&=(1,\epsilon,\eta r)/\sqrt D,
\end{split}
\qquad \epsilon,\eta\in\{-1,1\}.
\]
The remaining 12 vertices are their antipodes. Order each block by \((\epsilon,\eta)=(-1,-1),(-1,1),(1,-1),(1,1)\). For each \(i\in\{1,2,3\}\) let \(w_i\in\mathbb R^{12}\) equal \(\epsilon\eta\) on block \(i\), and zero elsewhere. Thus \(w_i\cdot w_j=4\delta_{ij}\). Write \(W=(w_1\ w_2\ w_3)\) and
\[
K_k(r)=\bigl(P_k(\nu_a\cdot\nu_b)\bigr)_{a,b=1}^{12},\qquad H(r)=\tfrac14W^TK_9(r)W.
\]
The signed position-contrast space is \(\{Wc:\ c\in\mathbb R^3,\ c_1+c_2+c_3=0\}\). All ranks are over \(\mathbb R\).

## Proof

**1. Gram representation and antipodes.** The spherical-harmonic addition theorem gives
\[
K_k(r)=\frac{4\pi}{2k+1}\,Y_kY_k^T,
\]
where the rows of \(Y_k\) are values of an orthonormal real basis of degree-\(k\) spherical harmonics at the 12 representatives. Hence \(K_k(r)\) is positive semidefinite and its rank equals the rank of the evaluation map on the representatives. On antipodes, \(Y(-x)=(-1)^kY(x)\), so the full 24-point evaluation has the same rank.

**2. A factorized two-dimensional degree-nine obstruction.** Directly substitute the displayed Legendre polynomial into the four-by-four signed block sums for \(H\). Polynomial expansion, before evaluating \(r\), shows that every diagonal entry of \(H\) is a common value \(A(r)\), and every off-diagonal entry is \(B(r)\). The exact identity is
\[
A(r)-B(r)=\frac{19305\,r^2(r^2-1)^2(r^4-6r^2+1)^2}{4D^9}=\Phi(r).
\]
For clarity, every dot product is \((a r^2+b r+c)/D\) with integers \(a,b,c\). After multiplying by \(128D^9\), the checker expands all pairwise Legendre polynomials with integer coefficients, checks the equality of all three diagonal and all six off-diagonal block sums, and verifies the polynomial factorization coefficient by coefficient. This proves the identity for all real \(r\), not merely sampled parameters.

If \(c_1+c_2+c_3=0\), then
\[
\frac{(Wc)^TK_9(r)(Wc)}{\|Wc\|_2^2}=A(r)-B(r)=\Phi(r).
\]
A vector has zero quadratic form for a positive-semidefinite matrix exactly when it belongs to its kernel. Thus the **entire contrast subspace** is in \(\ker K_9(r)\) exactly when \(\Phi(r)=0\). The positive roots are \(1\) and \(\sqrt2\pm1\), since \(r^4-6r^2+1=(r^2-2r-1)(r^2+2r-1)\). At \(r=1\) there are only eight distinct orbit points, so the stipulated 24-point family excludes it. This proves the two-resonance claim. Exact positive principal minors on rows \(\{0,\ldots,11\}\setminus\{0,4\}\), in the zero-based ordering above, show rank at least ten at both admissible resonances, while the two independent null vectors show rank at most ten.

**3. Exact finite rank certificates for the truncated cube.** For \(r=\sqrt2-1\), write dot products as \((a r^2+b r+c)/(r^2+2)\). The attached standalone checker constructs a rational interval for \(r\) with denominator \(10^{220}\), using the exact integer square root of \(2\cdot10^{440}\). The derivative of each normalized orbit vertex with respect to \(r\) has norm \(\sqrt2/(r^2+2)\), so the derivative of any pairwise dot product is bounded by \(\sqrt2<2\) for every \(r>0\); this justifies the checker’s outward error enclosure from its algebraic rational proxy. It propagates outward-rounded rational intervals by the three-term Legendre recurrence and performs interval \(LDL^T\) factorization with strictly positive lower-bound pivots.

For \(0\le k\le5\), it certifies a positive principal minor of order \(2k+1\); this equals the dimension of the degree-\(k\) harmonic space and thus proves rank \(2k+1\). For each integer \(k\) from six through 161, except nine, it certifies all 12 pivots positive, hence rank 12. For nine, two null vectors are independently verified with rational-pair arithmetic in \(\mathbb Q(\sqrt2)\), and a ten-by-ten minor has all strictly positive pivots, hence rank exactly ten. No floating-point predicates or approximate ranks enter these decisions. A second interval minor verifies rank ten for \(r=\sqrt2+1\).

**4. Analytic tail for every integer degree at least 162.** Exact interval arithmetic on all distinct representative pairs proves \(|\nu_a\cdot\nu_b|<\sqrt3/2\). Bernstein's inequality for Legendre polynomials, for \(-1<t<1\), implies
\[
|P_k(t)|<\sqrt{\frac{2}{\pi(k+1/2)\sqrt{1-t^2}}}
<\sqrt{\frac4{3(k+1/2)}}.
\]
Each row of \(K_k\) has diagonal one and eleven off-diagonal entries. For \(k\ge162\),
\[
\sum_{j\ne i}|K_k(i,j)|<11\sqrt{\frac4{3(k+1/2)}}<1
\]
by the integer inequality \(484<3\cdot162.5\). Gershgorin's theorem therefore puts all eigenvalues strictly above zero. This proves full rank in every degree beyond the finite check, completing the infinite classification.

## Verification

Run `python3 truncated_cube_checker.py` with Python 3.9 or newer and no external dependencies. It emits `TRUNCATED_CUBE_HARMONIC_INTERVAL_CERTIFICATE_OK` only after checking the exact parameter factorization, the cubic-orbit block symmetry, the two exact null vectors, the 24-point resonance minors, all truncated-cube finite ranks through degree 161, and the tail constants. The integer interval denominator is \(10^{220}\); the script contains all inputs and constructs no external files. Its assertions encode the stated finite proof obligations. The infinite tail is the explicit Bernstein–Gershgorin estimate above.

## Relationship to prior work

The Legendre addition theorem and spherical-harmonic interpolation are standard; see Pérez Saborid (2008), Misner (2004), and Nortje et al. (2015). Bannai, Okuda and Tagami (2013) study single-degree harmonic-design moment cancellation, which is distinct from this signed-contrast evaluation-rank problem. Wang (2018), Lemma 2.1, records the classical Bernstein bound used in the tail. An isolated all-degree evaluation-rank calculation for the rhombicuboctahedron already existed; neither its individual rank sequence nor the general addition theorem is claimed here as a discovery. The distinctive assertions here are the *parameter-uniform two-resonance factorization* and the verified exact-degree all-degree truncated-cube rank sequence. The literature review found no direct covering theorem, but this is not a claim of definitive historical uniqueness.

## Limitations

The two-resonance criterion classifies annihilation of the specified two-dimensional signed contrast space; it does **not** classify every possible degree-nine rank defect for all real \(r\). It describes exact-degree harmonic sampling, not all-degree cumulative interpolation, conditioning, approximation rates, or arbitrary 24-point values. The interval certificate is a finite executable argument combined with an analytic tail, not an externally audited formal proof. Only self-review was performed; independent validation and exhaustive historical priority checking remain outstanding. Highly specialized older polyhedral cubature and representation-theoretic calculations might contain equivalent statements.

## References

1. C. W. Misner, *Spherical harmonic decomposition on a cubic grid*, Classical and Quantum Gravity (first published 2004-01-13), DOI `10.1088/0264-9381/21/3/014`. Accessible abstract describes spherical-harmonic decomposition on cubic grids; full article not inspected.
2. M. Pérez Saborid, *The coordinate-free approach to spherical harmonics*, arXiv:`0806.3367` (first posted 2008-06-20), especially the spherical-harmonic addition theorem.
3. E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:`1308.5101` (first posted 2013-08-23), Definition 1.1 and introduction.
4. C. R. Nortje, W. O. C. Ward, B. P. Neuman, L. Bai, *Spherical Harmonics for Surface Parametrisation and Remeshing*, Mathematical Problems in Engineering (first published 2015-12-09), DOI `10.1155/2015/582870`, Sections 2 and 5.
5. H. Wang, *A new and sharper bound for Legendre expansion of differentiable functions*, arXiv:`1803.00336` (first posted 2018-03-01), Lemma 2.1 and its references to classical proofs of Bernstein's inequality.
