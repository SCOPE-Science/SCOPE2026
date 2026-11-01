# Exact Gegenbauer spectra and low-degree resonances on the type-\(D_n\) root orbit

## Finding
For every integer \(n\ge5\) and every integer \(\ell\ge0\), let
\[
X_n=\{(\epsilon e_i+\delta e_j)/\sqrt2:1\le i<j\le n,\ \epsilon,\delta\in\{-1,1\}\}\subset S^{n-1}.
\]
There are \(2n(n-1)\) distinct points. Let \(E_{n,\ell}\) evaluate the **exact-degree** complex spherical harmonics \(\mathcal H_\ell(S^{n-1})\) on \(X_n\). Define \(\lambda=(n-2)/2\), and
\[
p=\frac{C_\ell^{\lambda}(0)}{C_\ell^{\lambda}(1)},\qquad
q=\frac{C_\ell^{\lambda}(1/2)}{C_\ell^{\lambda}(1)},
\]
where \(C_\ell^{\lambda}\) is the Gegenbauer polynomial. In the following expressions, an eigenvalue listed with multiplicity zero is omitted, and coincident eigenvalues have their multiplicities added.

For **odd** \(\ell\), the normalized evaluation Gram matrix
\[
G_{n,\ell}(x,y)=C_\ell^{\lambda}(x\cdot y)/C_\ell^{\lambda}(1)
\]
has just two eigenvalue sectors:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
2+4(n-2)q&n\\
2-4q&n(n-2)
\end{array}
\]
plus zero with multiplicity \(n(n-1)\) from antipodal parity.

For **even** \(\ell\), its non-forced spectrum has four sectors:
\[
\begin{array}{c|c}
\text{eigenvalue}&\text{multiplicity}\\ \hline
2(1-p)&\binom n2\\
2(1+p)+8(n-2)q+2(n-2)(n-3)p&1\\
2(1+p)+4(n-4)q-4(n-3)p&n-1\\
2(1+3p-4q)&n(n-3)/2
\end{array}
\]
plus zero with multiplicity \(n(n-1)\) from antipodal parity. These tables give the **exact rank for every** \((n,\ell)\): sum the multiplicities of the listed *nonzero* eigenvalues. The normalized Gram spectrum also gives exact frame bounds after multiplication by the positive addition-formula normalization.

In particular, all \(n\ge5\) have
\[
\operatorname{rank}E_{n,0}=1,\quad
\operatorname{rank}E_{n,1}=n,\quad
\operatorname{rank}E_{n,2}=\binom{n+1}{2}-1,
\]
and \(\operatorname{rank}E_{n,3}=\operatorname{rank}E_{n,5}=n(n-1)\). The first even full-interpolation degrees exhibit two isolated **dimension resonances**:
\[
\operatorname{rank}E_{n,4}=n(n-1)-(n-1)\mathbf1_{\{n=8\}},
\qquad
\operatorname{rank}E_{n,6}=n(n-1)-\mathbf1_{\{n=16\}}.
\]
These low-degree formulas are global in \(n\ge5\). The theorem does **not** assert that higher degrees have no further exceptional dimensions; the all-degree tables decide those degrees exactly by the displayed Gegenbauer values.

## Assumptions and scope
The vectors \(e_i\) form the standard orthonormal basis of \(\mathbb R^n\); the root orbit is normalized to unit length. Harmonics are homogeneous harmonic polynomials restricted to the unit sphere, of exactly degree \(\ell\), not cumulative degree. The matrix \(G\) uses the normalization \(C_\ell^{\lambda}(1)>0\) and diagonal entries equal to one. Its rank agrees with the evaluation-map rank by the spherical-harmonic addition formula. Both even and odd degrees, including degree zero, are included. The restriction \(n\ge5\) excludes the exceptional triality case \(D_4\).

## Proof
The addition theorem makes \(G\) a positive scalar multiple of \(EE^*\). The normalized zonal polynomial has parity \(C_\ell^{\lambda}(-t)=(-1)^\ell C_\ell^{\lambda}(t)\), so antipodal symmetry forces half of the \(2n(n-1)\) eigenvalues to be zero.

Index each four-point sign block by an unordered coordinate pair \(\{i,j\}\). Its orthogonal Walsh characters are the constant, the two single-coordinate signs, and the sign product. For even degree only the constant and sign-product characters survive parity. On the product character of each pair, the same-pair sign sum gives \(2(1-p)\); every distinct-pair block annihilates that character, so this level has multiplicity \(\binom n2\). On the constant characters, the pair-indexed matrix has diagonal \(2(1+p)\), entry \(4q\) for intersecting coordinate pairs, and entry \(4p\) for disjoint pairs. It belongs to the Johnson scheme \(J(n,2)\). The adjacency of intersecting pairs has eigenvalues \(2(n-2),n-4,-2\), with multiplicities \(1,n-1,n(n-3)/2\). The complementary disjoint-pair adjacency has corresponding eigenvalues \(\binom{n-2}{2},-(n-3),1\). Substitution gives the remaining three even rows.

For odd degree, only the two single-coordinate-sign characters survive in each pair. The same-pair block acts by the scalar \(2\) on each. Two distinct blocks couple only when they share a coordinate; summing their four sign combinations gives a coupling \(4q\) between signs of the shared coordinate. Consequently this space splits into \(n\) independent coordinate stars, each of size \(n-1\), with matrix \((2-4q)I+4qJ\). Its uniform and orthogonal-to-uniform eigenvalues are the two listed odd rows. The total multiplicities in each parity sum to \(n(n-1)\), completing the all-degree spectrum and rank formula.

For the low-degree consequences, the rational Gegenbauer recurrence
\[
kC_k^{\lambda}(t)=2(k-1+\lambda)tC_{k-1}^{\lambda}(t)-(k-2+2\lambda)C_{k-2}^{\lambda}(t)
\]
with \(C_0^{\lambda}=1\), \(C_1^{\lambda}=2\lambda t\), yields exact factorizations. In degree four the four non-forced eigenvalues, in table order, are
\[
\frac{2(n-2)(n+2)}{(n-1)(n+1)},\quad
\frac{(n-4)^2(n+4)}{2(n-1)(n+1)},\quad
\frac{(n-8)^2(n+2)}{4(n-1)(n+1)},\quad
\frac{3(n+2)(n+4)}{2(n-1)(n+1)}.
\]
Every factor is positive for \(n\ge5\) except the third, which vanishes exactly at \(n=8\) with multiplicity \(n-1\).

In degree six they are
\[
\frac{2(n+4)(n^2-n+3)}{(n-1)(n+1)(n+3)},\quad
\frac{(n-16)^2(n-2)(n+6)}{8(n-1)(n+1)(n+3)},
\]
\[
\frac{(n+4)(n^3-18n^2+560n-1536)}{16(n-1)(n+1)(n+3)},\quad
\frac{15(n-4)(n+4)(n+6)}{8(n-1)(n+1)(n+3)}.
\]
The cubic in the third fraction is positive at \(n=5\) and has strictly positive derivative for all real \(n\); hence the only zero for \(n\ge5\) is the second level at \(n=16\), of multiplicity one. Direct recurrence substitution at degrees zero through three and five gives the other reported ranks (the degree-five uniform-star numerator is \(n^3-16n^2+164n-224\), positive for \(n\ge5\) by the same derivative argument).

## Verification
The included `check_spectrum.py` uses only Python's standard library and exact rational arithmetic. Run `python check_spectrum.py`. It verifies the predicted eigenvalues against full point-by-point Gram-matrix action on explicit basis witnesses for all \(5\le n\le9\), \(0\le\ell\le10\) (55 cases), and verifies the low-degree rank formula for all \(5\le n\le80\), \(0\le\ell\le6\) (532 cases), including the vanishing levels at \((n,\ell)=(8,4)\) and \((16,6)\). The proof, rather than finite tests, establishes the arbitrary-dimensional and all-degree formulas.

## Relationship to prior work
Delsarte, Goethals and Seidel's spherical-code framework supplies the general zonal-polynomial method. Bannai, Okuda and Tagami study harmonic-index design vanishing and bounds; their condition concerns the uniform sampling vector, not the full eigenvalue/multiplicity spectrum for \(D_n\). Cohn, Conway, Elkies and Kumar study the distinct \(D_4\) root orbit and its energy optimality, not the \(n\ge5\) exact-degree rank spectrum. This result gives the explicit signed-pair decomposition, four/two levels in every degree, and the special rank losses at dimensions eight and sixteen. The formulas are compatible with and rely on the standard Johnson-scheme adjacency spectra; no claim is made that the general scheme mechanism is new.

## Limitations
The spectrum is for the single normalized \(D_n\) root orbit, not an arbitrary root shell or a union of shells. It provides an exact finite test for zero levels at arbitrary higher degrees, not a closed description of the set of all higher-degree resonances. A general association-scheme eigenmatrix treatment might yield equivalent formulas, and bibliographic coverage is necessarily bounded. No independent mathematical validation has been performed.

## References
- P. Delsarte, J. M. Goethals, J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, DOI: 10.1007/BF03187604 (month of publication known; exact first public day unverified).
- H. Cohn, J. H. Conway, N. D. Elkies, A. Kumar, *The D4 root system is not universally optimal*, arXiv:math/0607447, initially public 2006-07-19, Experimental Mathematics 16 (2007), 313–320.
- E. Bannai, T. Okuda, M. Tagami, *Spherical designs of harmonic index t*, arXiv:1308.5101, initially public 2013-08-23, Journal of Approximation Theory 195 (2015), 1–17.
