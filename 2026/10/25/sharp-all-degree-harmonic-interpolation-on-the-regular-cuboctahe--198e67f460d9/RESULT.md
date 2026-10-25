# Sharp all-degree harmonic interpolation on the regular cuboctahedron

## Finding
Let \(X\) be the twelve vertices \( (\pm e_i\pm e_j)/\sqrt2\), \(1\le i<j\le3\), of a unit regular cuboctahedron in \(S^2\). On the space \(\mathcal H_\ell\) of spherical harmonics of **exactly** degree \(\ell\), take probability-surface-measure-orthonormal harmonics and define the normalized sampling map
\[
E_\ell f=\bigl(f(x)/\sqrt{2\ell+1}\bigr)_{x\in X}.
\]
Write \(a_\ell=P_\ell(1/2)\), \(b_\ell=P_\ell(0)\), where \(P_\ell(1)=1\) is the Legendre polynomial. For **even** \(\ell\), the six eigenvalues of \(E_\ell E_\ell^*\) in its antipodally compatible subspace are
\[
2(1+4a_\ell+b_\ell)\ (1),\qquad 2(1-b_\ell)\ (3),\qquad 2(1-2a_\ell+b_\ell)\ (2),
\]
where parenthesized values are multiplicities. For **odd** \(\ell\), they are
\[
2(1+2a_\ell)\ (3),\qquad 2(1-2a_\ell)\ (3).
\]
In both cases the remaining six eigenvalues vanish by antipodal parity. Every listed eigenvalue is rational. The ranks in degrees \(0,1,2\) are respectively \(1,3,5\), and **every** degree \(\ell\ge3\) has rank six, the maximum consistent with antipodal parity. Thus the sharp eventual surjectivity threshold is degree three.

More sharply, across **every** degree \(\ell\ge0\), the smallest strictly positive Gram eigenvalue obeys
\[
\boxed{\lambda_{\min}^{+}(E_\ell E_\ell^*)\ \ge\ \frac{65}{32768}.}
\]
Equality holds **only in degree ten**, on its one-dimensional constant sample sector. Consequently, the largest least-norm amplification for attainable sample data, with the displayed normalization and unweighted Euclidean data norm, is exactly \(\sqrt{32768/65}\). The near-defect at degree ten is not an actual harmonic-index-ten design: its constant eigenvalue is small but positive.

## Assumptions and scope
All degrees are nonnegative integers, and the functions may be real- or complex-valued. The sampling set includes all twelve vertices, not six antipodal representatives. The sphere carries probability surface measure. For an orthonormal basis \(Y_{\ell m}\), the addition formula is \(\sum_m Y_{\ell m}(x)\overline{Y_{\ell m}(y)}=(2\ell+1)P_\ell(x\cdot y)\). Hence the normalized Gram matrix is precisely \(G_\ell=(P_\ell(x\cdot y))_{x,y\in X}\), with twelve diagonal entries equal to one. The positive Gram eigenvalues are the squared nonzero singular values of \(E_\ell\). At deficient degrees the interpolation statement applies only to data in the sampling range, not arbitrary data.

## Proof
Pair each vertex with its antipode, using six representatives \(r_{ij,s}=(e_i+s e_j)/\sqrt2\) for \(1\le i<j\le3\) and \(s\in\{+1,-1\}\). Parity \(P_\ell(-t)=(-1)^\ell P_\ell(t)\) splits the full Gram operator into a six-dimensional zero sector and a six-dimensional compatible sector, the latter equal to twice the representative Gram matrix \(H_\ell\).

For even degree, two distinct representatives with the same support have scalar product zero, while those with different supports have scalar product \(\pm1/2\); Legendre parity makes all such off-diagonal entries \(a_\ell\). Let \(B\) be the perfect-matching adjacency matrix that interchanges the two representatives of each coordinate support. Then \(H_\ell=I+a_\ell(J-I-B)+b_\ell B\). The all-one vector, the two-dimensional orthogonal subspace of \(B\)-even vectors, and the three-dimensional \(B\)-odd subspace give eigenvalues \(1+4a_\ell+b_\ell\), \(1-2a_\ell+b_\ell\), and \(1-b_\ell\).

For odd degree, \(b_\ell=0\). Put the six representative coordinates in a \(6\times3\) matrix \(R\). The ordinary degree-one representative Gram matrix is \(R R^*=I+S/2\), where \(S\) has entries \(0\) for equal or disjoint directed coordinate supports and \(\pm1\) for distinct supports, according to the sign of the scalar product. Each coordinate occurs in four representatives, with cancellation of cross terms, so \(R^*R=2I_3\). Hence \(S\) has eigenvalues \(2\) and \(-2\), each with multiplicity three. The odd-degree representative Gram is \(H_\ell=I+a_\ell S\). This proves both spectral lists.

The Legendre recurrence \((j+1)P_{j+1}(t)=(2j+1)tP_j(t)-jP_{j-1}(t)\), started from \(P_0=1,P_1=t\), gives **exact rational** values at \(t=0,1/2\). The accompanying standalone checker exhaustively computes all nonzero eigenvalues at degrees \(0\) through \(19\) in rational arithmetic. It verifies ranks \((1,3,5)\) at degrees \((0,1,2)\) and six for each degree \(3\le\ell\le19\); among all strictly positive branches in this finite range, the unique minimum is \(65/32768\) at degree ten, in the constant sector.

For the infinite tail, use the classical Bernstein inequality for Legendre polynomials: for every integer \(\ell\ge1\) and \(0<\theta<\pi\),
\[
|P_\ell(\cos\theta)|<\sqrt{\frac{2}{\pi\ell\sin\theta}}.
\]
For \(\ell\ge20\), the elementary inequalities \(\pi>3\) and \(\sqrt3/2>5/6\) therefore imply \(|a_\ell|<1/5\) and \(|b_\ell|<1/\sqrt{30}<11/60\). For an even degree the three listed positive-sector eigenvalues are therefore strictly greater than, respectively, \(1/30\), \(49/30\), and \(5/6\). For an odd degree both are greater than \(6/5\). In particular, all are positive, and each exceeds \(65/32768\). Together with the finite exact computation, this proves the global rank law, the sharp unique minimum and the stated inverse singular-value bound.

## Verification
Run `python check.py` after installing `numpy` and `sympy` as in `requirements.txt`. The checker evaluates all low degrees with Python's exact `Fraction` recurrence, proves the finite minimum by exhaustive comparison of the small explicit lists, and independently constructs sixty-one full \(12\times12\) Gram matrices via Legendre polynomials and numerical diagonalization. It separately verifies the signed-root operator eigenvalues exactly. `CHECK_OUTPUT.txt` contains the recorded output. The infinite tail is established analytically above, not by numerical extrapolation. The exact rational recurrence and explicit bounds are sufficient to reproduce the finite certificate without treating floating-point spectra as proof.

## Relationship to prior work
Bannai, Okuda and Tagami (public arXiv preprint of August 23, 2013) introduce harmonic-index designs and explain the reproducing-kernel framework, but do not supply this all-degree cuboctahedral spectral or sharp conditioning classification. Khalid, Kennedy and McEwen (public arXiv preprint of March 19, 2014) study efficient latitude-based spherical harmonic transforms rather than fixed Archimedean-vertex exact-degree sampling. Classical cubic-group lattice-harmonic tables and the eigenvalues of the octahedral/cuboctahedral association scheme provide related symmetry machinery, but the exact global minimum over all degrees is a further discrete Legendre optimization. Some older literature might encode an equivalent theorem implicitly; publication priority has not been independently established.

## Limitations
This result concerns exact-degree harmonic sampling, not general bandlimited spherical transforms, weighted vertex sets or arbitrary deformations of the cuboctahedron. The inverse constant is tied to the specified normalization, and deficient degrees permit only range-compatible data. The low-degree finite table is certified by exact arithmetic plus the transparent recurrence, while the entire infinite tail requires the stated classical Bernstein inequality.

## References
1. E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, first public preprint August 23, 2013, arXiv:1308.5101; subsequently Journal of Approximation Theory 195 (2015), 1–18.
2. Z. Khalid, R. A. Kennedy, and J. D. McEwen, *An Optimal-Dimensionality Sampling Scheme on the Sphere with Fast Spherical Harmonic Transforms*, first public preprint March 19, 2014, arXiv:1403.4661.
3. S. L. Altmann and A. P. Cracknell, *Lattice Harmonics I. Cubic Groups*, Reviews of Modern Physics 37 (1965), 19–32, doi:10.1103/RevModPhys.37.19 (related symmetry literature; only abstract inspected).
4. G. Szegő, *Orthogonal Polynomials*, AMS Colloquium Publications, fourth edition, 1975, §7.3 (Bernstein's inequality for Legendre polynomials).
