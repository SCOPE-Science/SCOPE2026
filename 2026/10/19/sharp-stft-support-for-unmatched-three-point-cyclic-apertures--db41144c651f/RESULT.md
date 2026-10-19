# Sharp STFT support for unmatched three-point cyclic apertures

## Finding
Let \(p\ge5\) be prime, and let \(A,B\subset\mathbb Z_p\) be three-element subsets with \(A\) **not** a translate of \(B\). Define the short-time Fourier transform by
\[
V_gf(t,k)=\sum_{x\in\mathbb Z_p}f(x)\overline{g(x-t)}\exp(-2\pi ikx/p).
\]
For a nonzero difference class \(d\in(\mathbb Z_p\setminus\{0\})/\{\pm1\}\), let \(m_A(d)\) count the unordered pairs of points of \(A\) whose difference is \(\pm d\), and put
\[
E(A,B)=\sum_{d}m_A(d)m_B(d).
\]
Write \(\varepsilon(A,B)=1\) precisely when \(p\ge7\), \(A\) is **not** a three-term arithmetic progression, and \(B\) is a translate of \(-A\). In all other cases put \(\varepsilon(A,B)=0\). Then
\[
\boxed{\min_{\operatorname{supp}f=A,\ \operatorname{supp}g=B}
|\operatorname{supp}V_gf|=p(9-E(A,B))-E(A,B)+\varepsilon(A,B).}
\]
The minimum is over complex functions having the *exact* indicated spatial supports, and is always attained using coefficients in \(\{1,-1\}\).

When \(p=5\), every unmatched support pair has \(E=4\) and the minimum is \(5p-4=21\). When \(p\ge7\), one always has \(E\le3\), and the sharp minimum over all unmatched support pairs is \(6p-3\). For the exceptional reflected nonprogression pairs, \(E=3\) and the minimum is instead \(6p-2\). The number of **ordered** exceptional pairs \((A,B)\), for every prime \(p\ge7\), is exactly
\[
\boxed{\frac{p^2(p-1)(p-5)}6.}
\]

## Assumptions and scope
All additions and differences of spatial indices are taken modulo \(p\). A three-point arithmetic progression is a set of the form \(\{c-d,c,c+d\}\) with \(d\ne0\). A *translate* of a set \(S\) has the form \(u+S\); a *reflected translate* has the form \(u-S\). The spatial supports are each of size exactly three, distinct up to translation, and all their coefficients are nonzero. Fourier normalization by any nonzero scalar does not affect the support. The theorem concerns exact support cardinalities, not numerical stability or magnitudes of nonzero STFT samples.

## Proof
**1. Coincidence geometry.** For each time shift \(t\), set \(r_t=|A\cap(t+B)|\). It counts the products \(f(a_i)\overline{g(b_j)}\) for which \(a_i-b_j=t\). Since \(A\) is not a translate of \(B\), \(r_t\le2\). There are exactly nine ordered products, so \(\sum_t r_t=9\). Two different ordered products can share a time shift only when their two row indices and two column indices both differ. Equivalently, an unordered pair from \(A\) and an unordered pair from \(B\) have the same difference up to sign. Because \(r_t\le2\), each such pair-of-pairs yields a distinct double-occupancy shift, and its number is exactly \(E(A,B)\). It follows that there are \(9-E(A,B)\) nonempty time shifts: \(E\) with two terms, and \(9-2E\) with one term.

A one-term time slice has no Fourier zeros. A two-term slice, with nonzero coefficients \(c_1,c_2\) at distinct spatial locations \(a_i,a_j\), has the form \(c_1z^{ka_i}+c_2z^{ka_j}\), where \(z=\exp(-2\pi i/p)\). The map \(k\mapsto z^{k(a_i-a_j)}\) is injective, so this slice has **at most one** Fourier zero. Consequently every candidate pair satisfies
\[
|\operatorname{supp}V_gf|\ge p(9-E)-E.
\]

**2. Simultaneous cancellations.** Assign independent signs \((-1)^{u_i}\) to \(f(a_i)\) and \((-1)^{v_j}\) to \(g(b_j)\), for binary variables \(u_i,v_j\). For a double shift occupied by \((i,j)\) and \((k,l)\), cancellation at Fourier frequency zero is equivalent to
\[
u_i+u_k+v_j+v_l=1\pmod2.
\]
Each constraint involves two distinct row indices and two distinct column indices. For odd \(p\), two distinct double shifts cannot yield the same binary constraint: two alignments of the same row and column pairs would force a nonzero difference to equal its negative. Therefore any one or two constraints are linearly independent.

For \(p\ge7\), every three-point set has an unoriented pair-difference multiplicity pattern either \((2,1)\) (an arithmetic progression) or \((1,1,1)\) (a nonprogression). Two different progression step classes share at most one difference class: if both classes coincided but with exchanged multiplicities, then \(4d=\pm d\), which can occur only in characteristic \(3\) or \(5\). This proves \(E\le3\) unless the progressions are translates, which are excluded. A linear dependence among three cancellation equations requires each row index, and separately each column index, to occur an even number of times. Since a pair of indices can occur in at most two constraints (the other set has at most two pairs of a fixed difference class), this requires the three distinct edges of a triangle on both row and column indices. Thus the three difference classes of \(A\) and \(B\) must coincide, each occurring once. Three nonprogression points are determined by their three distinct unoriented differences up to translation and reflection: after choosing one oriented edge, the remaining two edges must close the triangle, and the only alternative consistent orientation reverses all edges. Hence the dependent case, after excluding translates, is exactly \(B=u-A\) with \(A\) nonprogression.

In every other case the \(E\) binary constraints are independent, so a sign assignment solves all of them. Every double slice then has exactly one Fourier zero (at frequency zero), giving \(p(9-E)-E\).

**3. Reflected nonprogression obstruction.** In the exceptional case translate coordinates so that \(B=-A\), with \(A=\{a_0,a_1,a_2\}\) nonprogression. The three double shifts are precisely \(a_i+a_j\) for \(i<j\). If all three slices vanished at frequencies \(k_{ij}\), write \(h_i=f(a_i)/\overline{g(-a_i)}\). Each cancellation would imply
\[
\frac{h_i}{h_j}=-z^{k_{ij}(a_j-a_i)}.
\]
Multiplying the three directed ratios around the triangle gives \(1=-z^m\) for an integer \(m\). This is impossible because \(p\) is odd and \(-1\) is not a \(p\)-th root of unity. Thus no pair of complex coefficient choices can cancel all three double slices. Any two of their binary sign equations are independent, and signs cancel two of the three slices at frequency zero. The maximum zero count is exactly two, proving the extra \(1\) in the formula.

**4. The prime five boundary.** Every three-point subset of \(\mathbb Z_5\) is a progression. The ten subsets form two translation orbits of five, represented by \(A=\{0,1,2\}\) and \(B=\{0,1,3\}\). The two unoriented difference multiplicity patterns are swapped, so each unmatched pair has \(E=4\). For the representatives, take the coefficient vectors \(f|_A=(1,-1,1)\) and \(g|_B=(-1,-1,1)\). Their four double-occupancy shifts are \(0,1,2,4\), and all four Fourier slices vanish at frequency zero. Translation and common dilation transport the construction to every unmatched pair. Thus the minimum is \(5p-4=21\).

**5. Sharpness and exceptional count.** For every \(p\ge7\), the sets \(A=\{0,1,2\}\), \(B=\{0,1,3\}\) are unmatched, have \(E=3\), and are not exceptional. Taking \(f|_A=(1,1,1)\) and \(g|_B=(1,-1,1)\) cancels all three double slices, proving the sharp minimum \(6p-3\). There are \(\binom p3-p(p-1)/2=p(p-1)(p-5)/6\) nonprogression three-point sets, since a progression has a unique center for \(p\ge7\). Every such set has exactly \(p\) distinct reflected translates, none of which is an ordinary translate (otherwise it would be a progression). Therefore the ordered exceptional-pair count is \(p^2(p-1)(p-5)/6\).

## Verification
The accompanying standalone `checker.py` enumerates all pairs of three-element supports for \(p=5,7,11,13\), omitting translated pairs. It forms all nine products, counts pair coincidences, and solves their binary cancellation equations using exact bitwise Gaussian elimination. It independently checks the arithmetic-progression/reflection characterization, the minimum support lower bound, and the exceptional-pair count. It also independently evaluates exact cyclotomic STFT coefficients for sign-valued witnesses in four representative cases, including the exceptional reflection at \(p=7\). It reports `CHECK_PASS` after respectively \(50\), \(980\), \(25{,}410\), and \(78{,}078\) exhaustive ordered support-pair checks. The finite checks do not prove the all-prime theorem: the proof above does.

## Relationship to prior work
Krahmer, Pfander, and Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications* (arXiv:math/0611493), prove the support-cardinality lower bound \(p(p+1)-(p+1-r)(p+1-s)\) when the signal and window have \(r+s\le p\) nonzero values (Proposition 4.4). For \(r=s=3\) and \(p\ge7\) it gives \(5p-4\); the other branch gives \(21\) at \(p=5\). Neither branch distinguishes fixed nontranslated supports, their difference-class intersection \(E\), or the reflected triangle penalty. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality* (arXiv:2204.14176), classifies equality in the global \(p\)-point lower bound (Theorems 1.1 and 1.2); this is a different extremal level. A publicly available two-sparse STFT trichotomy deals with exactly two nonzero entries per input and cannot imply the three-by-three triangle obstruction.

## Limitations
The theorem is confined to prime cyclic groups and two spatial supports of size exactly three that are not translates. It makes no claims for the matched-support stratum, composites, numerical condition numbers, or near-zeros. The literature comparison is not an exhaustive guarantee of first discovery: an equivalent description in unindexed sparse-radar or discrete ambiguity literature remains a residual risk. All finite verification is fully enumerated only for the explicitly checked primes.

## References
1. F. Nicola, *The uncertainty principle for the short-time Fourier transform on finite cyclic groups: cases of equality*, arXiv:2204.14176, submitted 29 April 2022; Journal of Functional Analysis 284 (2023), 109924.
2. F. Krahmer, G. E. Pfander, and P. Rashkov, *Uncertainty in time-frequency representations on finite Abelian groups and applications*, arXiv:math/0611493, submitted 16 November 2006; Applied and Computational Harmonic Analysis 25 (2008), 209–225.
3. *Exact support trichotomy for two-sparse prime cyclic STFTs*, public mathematical result in published-finding corpus (2026), identifier `2026/10/4/SCOPE-exact-support-trichotomy-for-two-sparse-prime-cyclic-stfts--5b84852d543c`.
