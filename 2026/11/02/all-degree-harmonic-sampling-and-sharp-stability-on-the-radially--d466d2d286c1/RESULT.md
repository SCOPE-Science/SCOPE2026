# All-degree harmonic sampling and sharp stability on the radially normalized rhombic dodecahedron

## Finding

Let \(X\subset S^2\) consist of the radially normalized fourteen vertices of the regular rhombic dodecahedron:
\[
X=\{(\varepsilon_1,\varepsilon_2,\varepsilon_3)/\sqrt3:\varepsilon_j\in\{-1,1\}\}\cup\{\pm e_1,\pm e_2,\pm e_3\}.
\]
For each integer \(k\ge0\), let \(E_k\) denote the restriction/evaluation map from the real spherical harmonics of **exact degree** \(k\) on \(S^2\) to their fourteen values on \(X\). Set \(r_k=\operatorname{rank}E_k\). Then
\[
(r_0,r_1,\ldots,r_{14})=(1,3,5,4,6,6,6,7,6,7,6,7,7,7,6),
\qquad r_k=7\quad(k\ge15).
\]
The seven-dimensional maximum is parity-compatible interpolation, not arbitrary interpolation on all fourteen points: each degree satisfies \(Y(-x)=(-1)^kY(x)\). Full parity-compatible interpolation first appears at degree seven, fails at degrees eight, ten and fourteen, and holds permanently from degree fifteen onward.

Choose seven antipodal representatives
\[
R=\{(1,s,t)/\sqrt3:s,t\in\{-1,1\}\}\cup\{e_1,e_2,e_3\},
\]
and let \(K_k=(P_k(u\cdot v))_{u,v\in R}\), where \(P_k\) is the Legendre polynomial with \(P_k(1)=1\). For all \(k\) with \(K_k\) nonsingular, define the spectral condition number \(\kappa_2(K_k)=\lambda_{\max}(K_k)/\lambda_{\min}(K_k)\). Its unique global maximum occurs at \(k=7\):
\[
\max_{k:\,r_k=7}\kappa_2(K_k)
=\frac{1337+\sqrt{889441}}{1337-\sqrt{889441}}
\approx5.788555980751372.
\]
Every other nonsingular degree satisfies the strict separation \(\kappa_2(K_k)<11/2\), while every degree \(k\ge120\) satisfies \(\kappa_2(K_k)<3\).

## Assumptions and scope

The fourteen points are obtained by radial normalization of the two distinct-radius vertex orbits of the actual rhombic dodecahedron. All sampling uses real exact-degree spherical harmonics and **unweighted point evaluation**. The seven representatives are one point from each antipodal pair. The Gram matrix has diagonal entries one, and eigenvalues are those of the specified unweighted Legendre matrix; a common positive normalization factor would not alter rank or condition number. The theorem concerns integer degrees \(k\ge0\), with no restriction on harmonic coefficients. It does not assert full unrestricted fourteen-point interpolation for a single exact harmonic degree.

## Proof

**1. Gram reduction.** The addition theorem on \(S^2\), for any real orthonormal basis \(Y_{k,j}\) of the degree-\(k\) harmonics, is
\[
\sum_{j=-k}^{k}Y_{k,j}(u)Y_{k,j}(v)=\frac{2k+1}{4\pi}P_k(u\cdot v).
\]
Consequently \(K_k\) is a positive-semidefinite scalar multiple of the seven-point evaluation Gram matrix. Antipodal symmetry makes the seven-point and fourteen-point evaluation maps have the same rank. Hence \(r_k=\operatorname{rank}K_k\), and \(r_k\le7\).

**2. Exact spectral decomposition.** Define
\[
a=P_k(1/3),\qquad b=P_k(0),\qquad c=P_k(1/\sqrt3).
\]
The four corner representatives are labeled by pairs \((s,t)\in\{\pm1\}^2\). Two distinct corners have dot product \(1/3\) when exactly one sign differs and \(-1/3\) when both signs differ. Distinct axis representatives have dot product zero; a corner \((1,s,t)/\sqrt3\) has dot products \((1,s,t)/\sqrt3\) with the three axes. Legendre parity gives \(P_k(-z)=(-1)^kP_k(z)\).

When \(k\) is even, the four-by-four corner block has eigenvalue \(1-a\) on the three-dimensional zero-sum subspace and eigenvalue \(1+3a\) on constants. The axis block has eigenvalue \(1-b\) twice and \(1+2b\) on constants. The corner–axis cross block is constant and couples only the two constant directions, with entry \(2\sqrt3\,c\). Thus the entire spectrum consists of
\[
1-a\quad(\text{multiplicity }3),\qquad
1-b\quad(\text{multiplicity }2),\qquad
\operatorname{spec}\begin{pmatrix}1+3a&2\sqrt3\,c\\2\sqrt3\,c&1+2b\end{pmatrix}.
\]
When \(k\) is odd, \(b=0\). The four corner Fourier characters \(1,s,t,st\) diagonalize the corner block. The \(st\)-character has eigenvalue \(1-3a\) and does not couple to the axes; the other three characters have eigenvalue \(1+a\), each coupling to one axis vector with coefficient \(2c\). Hence the spectrum is
\[
1-3a\quad(\text{multiplicity }1),\qquad
\operatorname{spec}\begin{pmatrix}1+a&2c\\2c&1\end{pmatrix}
\quad(\text{each eigenvalue repeated }3\text{ times}).
\]
These formulas are identities for every nonnegative integer degree, including degeneracies and zero eigenvalues.

**3. Entire finite range by exact arithmetic.** Use the Legendre recurrence
\[
P_0(z)=1,\quad P_1(z)=z,\quad
(k+1)P_{k+1}(z)=(2k+1)zP_k(z)-kP_{k-1}(z).
\]
In the provided `rhombic_dodecahedron_exact_check.py`, \(a\) and \(b\) are exact rationals. At \(z=1/\sqrt3\), the coefficient is rational for even degrees and \(\sqrt3\) times a rational for odd degrees; thus \(c^2\) is rational in every degree. The code evaluates the two scalar/2-by-2 spectral sectors and their determinants in exact rational arithmetic for **all degrees \(0\le k\le119\)**, obtaining the asserted rank table and full rank for every degree \(15\le k\le119\). The bound \(\kappa_2(K_k)<11/2\) is proved in exact rational arithmetic for all full-rank degrees \(8\le k\le119\): each eigenvalue is enclosed by strict rational inequalities to mesh \(10^{-5}\), and the exact upper-envelope/lower-envelope ratio is checked strictly below \(11/2\). No floating-point arithmetic is used for these inequalities. The separate `rhombic_geometry_crosscheck.py` constructs the Gram matrix from coordinates and checks the claimed factorizations symbolically for eighteen selected degrees, including the exceptional ones.

**4. Sharp global degree-seven maximum.** At degree seven the Legendre recurrence gives
\[
a=-121/729,\qquad c=5\sqrt3/27.
\]
The eigenvalues are \((1337-\sqrt{889441})/1458\) and \((1337+\sqrt{889441})/1458\), each with multiplicity three, and \(364/243\) once. The last value lies strictly between the first two, since \(943^2<889441<944^2\). The ratio of the extrema is the displayed exact number. The same integer enclosure proves this ratio exceeds \(11/2\), whereas Step 3 bounds all other nonsingular degrees below \(120\) strictly by \(11/2\).

**5. Infinite tail, without extrapolation.** Every off-diagonal inner product \(z\) of \(R\) belongs to \(\{0,\pm1/3,\pm1/\sqrt3\}\), so \(\sqrt{1-z^2}\ge\sqrt{2/3}>4/5\). Bernstein's Legendre inequality, for \(k\ge1\) and \(|z|<1\), is
\[
|P_k(z)|<\sqrt{\frac{2}{\pi k\sqrt{1-z^2}}}
<\sqrt{\frac5{6k}}\le\frac1{12}\quad(k\ge120),
\]
using \(\pi>3\) and the strict sine bound. A row of \(K_k\) has diagonal one and six off-diagonal entries, with total off-diagonal absolute value strictly below \(1/2\). Gershgorin's theorem therefore places every eigenvalue strictly inside \((1/2,3/2)\). Thus \(K_k\) is positive definite for every \(k\ge120\) and \(\kappa_2(K_k)<3\). Combining Steps 3–5 proves every stated rank and the unique global conditioning maximum. \(\square\)

## Verification

Run `python3 rhombic_dodecahedron_exact_check.py` from a directory containing the accompanying standalone script; it uses only the Python standard library. The expected success prefix is `RHOMBIC_DODECAHEDRON_EXACT_CERTIFICATE_OK`, with 120 finite spectral degrees and 109 strict competitor bounds. Run `python3 rhombic_geometry_crosscheck.py` with SymPy installed for a separate coordinate-to-spectrum identity check; the expected success prefix is `RHOMBIC_DODECAHEDRON_GEOMETRY_CROSSCHECK_OK`. Both scripts are complete and have no external data dependencies. Their finite scope is explicit; the separate Bernstein–Gershgorin argument covers every higher degree.

## Relationship to prior work

Marzo's study of Marcinkiewicz–Zygmund inequalities and spherical-harmonic interpolation establishes density and stability conditions for *growing families of nodes and cumulative-degree spaces*; it does not yield these exact-degree ranks or a global finite-point Gram condition maximum. Bannai–Okuda–Tagami characterize harmonic-index designs through a Gegenbauer-kernel quadratic sum and develop associated bounds and examples; that single uniform-sum condition is not a seven-dimensional full Gram rank or conditioning classification. The present calculation is for the radially normalized rhombic-dodecahedron vertex configuration specifically; ordinary geometrical investigations of the rhombic dodecahedron do not determine the harmonic spectrum. Older cubature, group-representation or spherical-grid literature may contain an equivalent formulation; no uniqueness assertion is made beyond the searches described in the accompanying review.

## Limitations

The proof includes computer-assisted **finite** exact-rational verification for degrees below 120. The scripts are supplied in full, and the supplementary symbolic geometry check is additional corroboration; neither finite computation is cited as proof of the unbounded range. The all-degree conclusion uses a separate analytic inequality. This result is not a classification of other polyhedra, arbitrary weighted vertices, cumulative-degree interpolation, or unrestricted values at all fourteen antipodal points. Novelty is supported by bounded literature comparison and is not a claim of exhaustive historical coverage. Independent external validation has not been performed.

## References

1. J. Marzo, *Marcinkiewicz–Zygmund inequalities and interpolation by spherical harmonics*, first publicly posted 2006-11-16, arXiv:math/0611503, https://arxiv.org/abs/math/0611503 .
2. E. Bannai, T. Okuda, and M. Tagami, *Spherical designs of harmonic index t*, first publicly posted 2013-08-23, arXiv:1308.5101v1, https://arxiv.org/html/1308.5101v1 .
3. W. Gautschi and C. Giordano, *Luigi Gatteschi's work on asymptotics of special functions and their zeros*, *Numerical Algorithms* **49** (2008), 11–31, equation (56), https://doi.org/10.1007/s11075-008-9208-5 .
4. D. N. Oldham, J. H. Davies, and T. N. Phillips, *Generic polyhedron grid generation for solving partial differential equations on spherical surfaces*, *Computers & Geosciences* **39** (2012), 11–17, https://doi.org/10.1016/j.cageo.2011.06.004 . (Abstract and bibliographic record available; full text not examined.)
