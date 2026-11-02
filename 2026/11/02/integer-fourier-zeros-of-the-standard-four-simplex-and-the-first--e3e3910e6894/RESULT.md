# Integer Fourier zeros of the standard four-simplex and the first midpoint resonance

## Finding
Let \(\Delta_4=\{x\in\mathbb R^4:x_j\ge0,\ \sum_{j=1}^4 x_j\le1\}\) and let \(\widehat{\mathbf1}_{\Delta_4}(k)=\int_{\Delta_4} e^{-2\pi i\,k\cdot x}\,dx\) at \(k\in\mathbb Z^4\). Form the five-element multiset \(V(k)=\{0,k_1,k_2,k_3,k_4\}\), with multiplicities. **The complete zero classification is**
\[
\widehat{\mathbf1}_{\Delta_4}(k)=0
\quad\Longleftrightarrow\quad
\begin{cases}
\text{all five entries of }V(k)\text{ are distinct},\\
\text{or}\ V(k)=\{a,a,b,b,c\},\ a,b,c\in\mathbb Z\text{ distinct},\ 2c=a+b.
\end{cases}
\]
The second case is a genuine arithmetic cancellation despite repeated vertex phases: for example \(k=(0,1,2,2)\) and \(k=(1,1,-1,-1)\) both give zero. **Four is the first simplex dimension for this phenomenon**: in dimensions one through three, every integer-frequency zero has pairwise distinct vertex phases.

## Assumptions and scope
The Fourier transform is unnormalized (Lebesgue measure), uses the negative exponential \(e^{-2\pi i k\cdot x}\), and is evaluated at **all** integral frequencies \(k\in\mathbb Z^4\), including zero. The simplex has ordinary Euclidean volume \(1/24\), so the origin is not a zero. The five nodes are the scalar phases of the five vertices, not the frequency coordinates alone. The classification is not asserted for nonintegral frequencies or arbitrary nonstandard simplices.

## Proof
Put \(t=-2\pi i\), \(a_0=0\), and \(a_j=k_j\) for \(1\le j\le4\). For the exponential \(f_t(z)=e^{tz}\), the Genocchi–Hermite formula and the contour representation of confluent divided differences give
\[
t^4\widehat{\mathbf1}_{\Delta_4}(k)
=[a_0,a_1,a_2,a_3,a_4]f_t
=\frac1{2\pi i}\oint_{\Gamma}
\frac{e^{tz}}{\prod_{j=0}^4(z-a_j)}\,dz.
\]
Here the ordered integration variables of Genocchi–Hermite range over the standard four-simplex, and \(f_t^{(4)}=t^4f_t\); therefore there is no extra Jacobian or factorial. The contour encloses the distinct integer nodes.

Write the distinct nodes as \(a\), each with multiplicity \(m_a\), and expand the rational denominator into partial fractions:
\[
\prod_a(z-a)^{-m_a}=\sum_a\sum_{r=1}^{m_a}c_{a,r}(z-a)^{-r}.
\]
All \(c_{a,r}\) are rational and the residues give
\[
t^4\widehat{\mathbf1}_{\Delta_4}(k)=
\sum_{r\ge1}\frac{t^{r-1}}{(r-1)!}\sum_{a:m_a\ge r}c_{a,r},
\]
because \(e^{ta}=1\) for integral \(a\). Since the denominator is \(O(z^{-5})\) at infinity, its \(z^{-1}\) coefficient vanishes; hence \(\sum_a c_{a,1}=0\). This is a rational-coefficient polynomial in \(t\) without constant term. Since \(t=-2\pi i\) is transcendental, its value vanishes precisely when **all** of its coefficients vanish.

If all five nodes are distinct, the polynomial is identically zero. If the largest multiplicity \(M\ge2\) occurs at exactly one node \(a\), the leading polynomial coefficient cannot vanish: its nonzero numerator is
\[
c_{a,M}=\prod_{b\ne a}(a-b)^{-m_b}\ne0.
\]
The only remaining partition of five with a tied largest multiplicity is \((2,2,1)\). Put double nodes at \(a,b\) and the singleton at \(c\); the sole potentially nonzero polynomial coefficient is
\[
\begin{split}
c_{a,2}+c_{b,2}
&=\frac1{(a-b)^2}\left(\frac1{a-c}+\frac1{b-c}\right)\\
&=\frac{a+b-2c}{(a-b)^2(a-c)(b-c)}.
\end{split}
\]
It vanishes exactly for the midpoint relation \(2c=a+b\). This proves both directions, including all coincidences and the origin.

For dimension \(d\le3\), there are at most four vertex phases. The sole tied-maximal-multiplicity partition with repetitions is \((2,2)\). For distinct double nodes \(a,b\), the leading coefficient is \(2/(a-b)^2\ne0\); all other repeated-node partitions have a unique maximal multiplicity. Thus dimension four is the first dimension permitting a zero with repeated phases.

## Verification
The embedded `check.py` computes confluent divided differences as polynomials in \(t\) over exact rational numbers, independent of the residue-based partition argument. It exhaustively compares the resulting zero test against the proposed classification for integer-frequency boxes \([-3,3]^d\), for each dimension \(1\le d\le4\). There are respectively \(7\), \(49\), \(343\), and \(2401\) test cases. The four-dimensional box contains \(402\) zeros, of which \(42\) arise from the extra midpoint resonance. The checker reproduces the zero polynomials for the two displayed resonances and a nonzero comparison. These finite computations corroborate—but do not replace—the proof for all integer frequencies.

## Relationship to prior work
The Genocchi–Hermite and contour identities for divided differences are established in de Boor, *Divided Differences*, particularly the historical contour and Genocchi–Hermite discussions; they are used, not claimed as new. Diaz, Le, and Robins develop the general Fourier transform of real polytopes by iterated Stokes formulas, describe non-generic lattice directions, and explicitly illustrate a tetrahedron. The present result concerns the special, separately determined **complete vanishing locus** at all integer frequencies for the standard four-simplex, including the isolated midpoint arithmetic resonance and the first-dimensional boundary. The general transform formulas are not themselves claimed here.

## Limitations
The zero set concerns the standard integral four-simplex only. No claim is made about arbitrary lattice simplices, quantitative decay, nonintegral frequencies, or lattice sums. The proof uses the classical transcendence of \(\pi\), as well as standard interpolation identities whose hypotheses are explicitly satisfied. An equivalent formulation in earlier divided-difference or polytope-Fourier literature may exist; independent validation has not been performed.

## References
1. C. de Boor, “Divided Differences,” *Surveys in Approximation Theory* 1 (2005), 46–69, arXiv:math/0502036v1, publicly submitted 2005-02-01; contour representation and Genocchi–Hermite formula.
2. R. Diaz, Q.-N. Le, and S. Robins, “Fourier transforms of polytopes, solid angle sums, and discrete volume,” arXiv:1602.08593v1, publicly submitted 2016-02-27; sections 1–3, 5, 9.
