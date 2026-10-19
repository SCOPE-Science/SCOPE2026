# Pell-classified spherical fifth-order cubature on antipodal hypersimplex orbits

## Finding
For integers \(n\ge4\) and \(1\le k\le n-1\), put \(H_n=\{a\in\mathbb R^n:\sum_i a_i=0\}\), a Euclidean space of dimension \(n-1\), and let \(\mathbf1_S\) be the incidence vector of \(S\subseteq\{1,\ldots,n\}\). Define
\[
 u_S=\sqrt{\frac{n}{k(n-k)}}\left(\mathbf1_S-\frac{k}{n}\mathbf1\right),
 \qquad X_{n,k}=\{u_S,-u_S:|S|=k\}\subset S(H_n).
\]
The finite set \(X_{n,k}\), with equal weight on distinct points, is a **spherical \(5\)-design if and only if**
\[
 \boxed{n(n+1)=6k(n-k).}
\]
Equivalently, after replacing \(k\) by \(n-k\) if needed, all admissible solutions are generated, without omissions, by
\[
 \boxed{(n-1)+(n-2k)\sqrt3=(2+\sqrt3)^j,\qquad j=2,3,\ldots.}
\]
The first orders and subset sizes are \((8,2)\), \((27,6)\), \((98,21)\), and \((363,77)\), as well as their complementary subset sizes. The first case gives the familiar 56-point tight spherical \(5\)-design in seven dimensions; it is not claimed as a new configuration. The next case yields an explicit, equal-weight, \(592020\)-point fifth-order cubature formula on the unit sphere in the 26-dimensional space \(H_{27}\), i.e. \(S^{25}\). The arithmetic criterion yields infinitely many configurations of increasing dimension.

## Assumptions and scope
A spherical \(5\)-design here means that the equally weighted average of **every real or complex polynomial of total degree at most five** over \(X_{n,k}\) equals its rotationally invariant probability average over \(S(H_n)\). Both signs are included. If \(k=n/2\), complementary subsets duplicate the same antipodal points; in that case using all signed subsets yields a constant multiplicity of two and therefore the same average as the distinct-point set. Also \(X_{n,k}=X_{n,n-k}\). The parameter range \(n\ge4\) avoids low-dimensional exceptional sphere conventions; for \(n=3\), the analogous signed singleton orbit is a regular hexagon, also a spherical fifth-order design. No claim is made about unequal weights, unions of several distinct subset orbits, or sixth-order cubature.

## Proof
**First and second moments.** All vectors \(u_S\) have unit norm and lie in \(H_n\). Antipodal symmetry annihilates every odd polynomial. Fix \(a=(a_i)\in H_n\), and write \(p_2=\sum_i a_i^2\), \(p_4=\sum_i a_i^4\). For uniformly random \(k\)-subset \(S\), write \(\varepsilon_i=2\mathbf1_{i\in S}-1\) and \(F=\sum_i a_i\varepsilon_i=2\sum_{i\in S}a_i\). The two-index sampling identity gives
\[
 \mathbb EF^2=\frac{4k(n-k)}{n(n-1)}p_2,
 \qquad \mathbb E\langle u_S,a\rangle^2=\frac{p_2}{n-1}.
\]
This matches the uniform sphere's second moment in dimension \(n-1\) for every \(n,k\).

**Exact fourth tensor.** For distinct indices let \(c_2=\mathbb E(\varepsilon_i\varepsilon_j)\) and \(c_4=\mathbb E(\varepsilon_i\varepsilon_j\varepsilon_h\varepsilon_t)\). With falling factorials \((z)_s=z(z-1)\cdots(z-s+1)\), direct sampling without replacement yields
\[
 c_2=\frac{(n-2k)^2-n}{n(n-1)},\qquad
 c_4=1-\frac{8k}{n}+24\frac{(k)_2}{(n)_2}-32\frac{(k)_3}{(n)_3}+16\frac{(k)_4}{(n)_4}.
\]
Expand \(F^4\), group index patterns of multiplicities \(4\), \(3+1\), \(2+2\), \(2+1+1\), \(1+1+1+1\), and use \(\sum_i a_i=0\). One obtains exactly
\[
 \mathbb EF^4=A_{n,k}p_2^2+B_{n,k}p_4,
\]
where
\[
 A_{n,k}=\frac{48k(k-1)(n-k)(n-k-1)}{n(n-1)(n-2)(n-3)},
 \quad B_{n,k}=\frac{16k(n-k)[n^2+n-6k(n-k)]}{n(n-1)(n-2)(n-3)}.
\]
In particular, \(A_{n,k}=3-6c_2+3c_4\) and \(B_{n,k}=-2+8c_2-6c_4\), so these identities can also be checked by expanding the two exchangeable sign correlations. Since \(\langle u_S,a\rangle=\sqrt{n/[k(n-k)]}\,F/2\),
\[
 \mathbb E\langle u_S,a\rangle^4=
 \frac{n^2}{16k^2(n-k)^2}\left(A_{n,k}p_2^2+B_{n,k}p_4\right). \tag{1}
\]
The rotationally invariant sphere in dimension \(d=n-1\) instead has projection fourth moment \(3p_2^2/[d(d+2)]=3p_2^2/[(n-1)(n+1)]\).

**Necessity and sufficiency.** For every \(n\ge4\), the two mean-zero vectors \(a=(1,-1,0,\ldots,0)\) and \(b=(1,1,-1,-1,0,\ldots,0)\) have distinct ratios \(p_4/p_2^2\), respectively \(1/2\) and \(1/4\). Therefore equation (1) can depend only on \(p_2^2\), as required by a spherical fourth moment, only if \(B_{n,k}=0\). All denominators and \(k(n-k)\) are nonzero in the stated range, hence
\[
 B_{n,k}=0\quad\Longleftrightarrow\quad n(n+1)=6k(n-k). \tag{2}
\]
Conversely, equation (2) makes \(B_{n,k}=0\), and substituting it into the displayed expression for \(A_{n,k}\) gives
\[
 \frac{n^2A_{n,k}}{16k^2(n-k)^2}=\frac{3}{(n-1)(n+1)}.
\]
Thus the full second and fourth projection moments agree with those of the sphere for **every** \(a\in H_n\). Polarization gives agreement for every homogeneous quadratic and quartic polynomial. Odd homogeneous degrees vanish by antipodality. Together with the constant term, this proves exactness for all polynomials of degree at most five. This establishes both directions without numerical extrapolation.

**Pell classification.** Put \(t=n-2k\), after taking \(k\le n/2\). Then (2) is
\[
 (n-1)^2-3t^2=1.
\]
The nonnegative integer solutions to the Pell equation are \((n-1)+t\sqrt3=(2+\sqrt3)^j\), \(j\ge0\). The case \(j=0\) yields \(n=2\), outside our scope; \(j=1\) yields \(n=3\), also excluded. Every \(j\ge2\) yields \(n\ge8\), positive integer \(k=(n-t)/2\) with \(1\le k<n/2\), because \(n-t\) is even and \(0<t<n-2\). Conversely, every admissible pair arises from such a Pell solution or from replacing \(k\) with \(n-k\). This completes the classification.

## Verification
The standalone file `CHECK.py` checks the two independently expanded moment formulas exactly using rational arithmetic, compares the resulting expression with direct combinatorial enumeration for every \(4\le n\le10\) and all \(1\le k\le\lfloor n/2\rfloor\) on three contrasting zero-sum test vectors, verifies the first five Pell solutions, and checks symbolic-formula cubature equalities at the first four admissible large-dimensional examples. It also checks a non-design example. All 425 assertions passed on the supplied checker. The checker corroborates finite instances; the proof above covers every \(n\ge4\) and every permitted \(k\).

## Relationship to prior work
Delsarte, Goethals and Seidel introduced the general spherical-design and harmonic-moment framework. The famous 56-point tight fifth-order design is already known, and is exactly the first arithmetic instance here. Reznick's 1995 article gives general existence and nonexistence results for spherical fifth-order designs, including tight-design bounds; those results are not replaced or rebranded here. Filmus (2014) and Filmus–Mossel (2015) develop the Johnson-slice harmonic analysis and invariance framework, but their inspected statements do not classify antipodal centered Johnson orbits by fifth-order cubature strength. Xiang (2022) and Misawa (2026) construct spherical designs through different general constructions, not by the one-orbit Pell condition. The contribution assessed here is only the **uniform necessity-and-sufficiency condition (2) and its complete infinite Pell parametrization for this fixed orbit family**, not the general design criterion nor the previously known 56-point example.

## Limitations
The case \(n=3\) is recorded separately; the theorem is stated for \(n\ge4\). The Pell solutions are not asserted to minimize the number of nodes or to improve currently known sparse spherical cubature constructions. No sixth-order exactness is claimed. Some foundational design literature, especially Delsarte–Goethals–Seidel (1977), was not accessible for complete full-text originality comparison. An earlier implicit equivalence obtained from general association-scheme formulas remains possible; independent literature and mathematical review are still required before a publication-priority assertion.

## References
- P. Delsarte, J.-M. Goethals and J. J. Seidel, *Spherical codes and designs*, Geometriae Dedicata 6 (1977), 363–388, doi:10.1007/BF03187604.
- B. Reznick, *Some constructions of spherical 5-designs*, Linear Algebra and its Applications 226–228 (1995), 163–196, doi:10.1016/0024-3795(95)00101-V.
- Y. Filmus, *Orthogonal basis for functions over a slice of the Boolean hypercube*, arXiv:1406.0142 (initial public version 2014-06-01).
- Y. Filmus and E. Mossel, *Harmonicity and invariance on slices of the Boolean cube*, arXiv:1507.02713 (initial public version 2015-07-09).
- Z. Xiang, *Explicit spherical designs*, Algebraic Combinatorics (2022), doi:10.5802/alco.213.
- R. Misawa, *Explicit construction of spherical 5- and 7-designs*, arXiv:2602.19757 (2026), for comparison with a different high-dimensional design construction.
