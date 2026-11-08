# A 33-line Galois closure of the Klein arrangement with exactly four bad incidence primes

## Finding
For the Klein arrangement \(\mathcal K_\omega\) of 21 lines over \(\mathbb Q(\omega)\), \(\omega^2+\omega+2=0\), form the projective line arrangement \(\mathcal D=\mathcal K_\omega\cup\mathcal K_{-1-\omega}\). Although neither marked configuration is individually rational in these coordinates, their union is invariant under quadratic Galois conjugation and hence defines a **reduced divisor over \(\mathbb Q\)**. Exactly nine lines are common to the two arrangements, so \(\mathcal D\) has **33 distinct geometric component lines**.

In characteristic zero and in every characteristic outside \(\{2,3,7,11\}\), the complete intersection multiplicity profile of \(\mathcal D\) is
\[
(t_2,t_3,t_4,t_5,t_6)=(120,52,27,0,6),
\]
where \(t_r\) is the number of geometric points lying on exactly \(r\) component lines. The **exact set of bad-incidence primes for this integral model is \(\{2,3,7,11\}\)**. Its exceptional fibers are:

| Characteristic | Distinct geometric lines | \(t_2\) | \(t_3\) | \(t_4\) | \(t_5\) | \(t_6\) |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| \(3\) | 33 | 24 | 4 | 27 | 24 | 6 |
| \(7\) | 21 | 0 | 28 | 21 | 0 | 0 |
| \(11\) | 33 | 48 | 40 | 15 | 0 | 18 |
| \(2\) | 7 | 0 | 7 | 0 | 0 | 0 |

The results hold over algebraic closures. No claim is made about the rationality of individual intersection points over the ground finite field. In characteristics 2 and 11, the two roots of the coefficient quadratic have the same listed incidence profile.

## Assumptions and scope
Let \(R=\mathbb Z[\omega]/(\omega^2+\omega+2)\), and define the 21 line coefficient triples in \(R^3\), ordered as follows:
\[
\begin{aligned}
&(1,0,0), (0,1,1), (\omega,1,-1), (\omega,-1,1), (0,-1,1),\\
&(1,\omega,-1), (\omega,-1,-1), (-1,1,\omega), (\omega,1,1), (-1,\omega,1),\\
&(-1,-1,\omega), (1,0,1), (-1,\omega,-1), (1,\omega,1), (-1,0,1),\\
&(1,-1,\omega), (1,1,\omega), (0,0,1), (-1,1,0), (1,1,0), (0,1,0).
\end{aligned}
\]
A row \((a,b,c)\) denotes the line \(aX+bY+cZ=0\). These equations agree with Innamorati's 2024 Klein arrangement, up to nonzero projective scaling. Apply conjugation \(\sigma(\omega)=-1-\omega\) entrywise to the list and add lines not already present, modulo overall signs. This produces the **complete 33-row list**, programmatically constructed in `verify.py`; the nine common lines have rational coefficients. The conjugation-closed union is the canonical reduced Galois closure *relative to these coordinates*; no claim is made that its isomorphism class is independent of every different projective realization of Klein's arrangement.

For a prime characteristic, reduce this integral model at a chosen geometric root of the parameter equation. At characteristic \(3\), the quadratic is irreducible and the residue field is \(\mathbb F_9\); at \(7\) it has the double geometric root \(3\); at \(11\) it has roots \(4\) and \(6\); at \(2\) roots \(0\) and \(1\). The reduced union means coincident specialized lines are counted only once.

## Proof
**1. Exact algebraic arithmetic.** Every entry belongs to \(R\), with \(\omega^2=-\omega-2\). For \(u=a+b\omega\), define the quadratic norm
\[
N(u)=a^2-ab+2b^2.
\]
If a prime \(p\) does not divide \(N(u)\), the image of \(u\) is nonzero in every geometric specialization of characteristic \(p\): \(u\overline u=N(u)\). This argument applies even at the ramified prime \(7\).

**2. Why 33 rationally descended lines.** Conjugate each of the 21 coefficient rows by \(\sigma(a+b\omega)=(a-b)-b\omega\). An exact projective coefficient comparison shows nine of the conjugate lines already occur in the original list and twelve do not; the full set is closed under conjugation. Hence its reduced product equation, up to a rational nonzero scalar, defines a rational projective divisor of degree \(33\). The 33 geometric lines are distinct over characteristic zero.

**3. Exhaustive incidence certificate.** There are \(\binom{33}{2}=528\) line pairs and \(\binom{33}{3}=5456\) triples. For every pair, calculate its cross-product's three \(2\times2\) minors in \(R\); for every triple calculate the \(3\times3\) determinant in \(R\). Exactly **280 triple determinants vanish identically**. The norms of **all remaining nonzero triple determinants**, and the nonzero greatest common divisors of norms of the pairwise minors, have no prime factors outside
\[
\{2,3,7,11\}.
\]
Every one of these four primes actually divides a nonzero triple-determinant norm. Therefore for every prime outside the displayed set, no distinct lines merge and no new triple dependency occurs. The full intersection lattice is constant there, not merely its singular-point totals.

**4. Generic intersection lattice.** Two distinct projective lines have one intersection point. Identify the 528 line pairs whenever a zero triple determinant shows their intersections coincide. The resulting equivalence classes are exactly 120 of size \(1\), 52 of size \(3\), 27 of size \(6\), and six of size \(15\). Each class consists of all \(\binom r2\) pairs of a unique \(r\)-element set of lines, where \(r=2,3,4,6\), respectively. The identity
\[
120\binom22+52\binom32+27\binom42+6\binom62=528
\]
shows that these account for every pairwise intersection. Their dependence pattern is unchanged at every prime outside \(\{2,3,7,11\}\), proving the generic profile uniformly.

**5. All exceptional fibers.** The same exact pair-minor and triple-determinant algorithm, now reduced in the quadratic residue ring of each exceptional prime, first identifies coincident component lines and then computes all distinct pair intersections. The complete profiles are those in the table above. For \(p=3\), compute in the field \(\mathbb F_3[\omega]/(\omega^2+\omega+2)\), not by substituting an absent prime-field root. For \(p=11\), the two roots give identical profiles and 33 distinct lines; for \(p=7\), the conjugation involution specializes to the identity and yields precisely the original 21-line configuration. For \(p=2\), both roots produce the seven-line Fano-plane arrangement. In each case the checker verifies that every intersection class is composed of exactly all pairs of its incident lines, which is an exhaustive test of the multiplicity profile.

The four displayed exceptional profiles each differ from the generic one. Thus all and only the four listed primes are bad for the incidence lattice of this model.

## Verification
The standalone standard-library program `verify.py` performs exact arithmetic using integer pairs representing \(a+b\omega\). It confirms the original 21-line determinant identities, builds the 33-line conjugation-closed union, calculates every triple determinant and pair minor, and reconstructs all generic and exceptional intersection classes. It prints `VERIFY_KLEIN_GALOIS_CLOSURE_OK` upon success. A separate symbolic polynomial-reduction computation checked the original quadratic-ring determinant arithmetic and was consistent with the standalone certificate. No claim is extrapolated from a finite sampling of good prime fields: the all-characteristic conclusion follows from exact integer norm factorization.

## Relationship to prior work
Bauer et al. (2016) establish the 21-line Klein configuration and the geometric behavior of the prime-seven specialization; Gévay–Pokora (2022) prove uniqueness of the Klein realization up to projectivities and Galois conjugates, making the operation of adjoining the conjugate a natural arithmetic question. Innamorati (2024) gives the 21 line equations over a field containing a root of the quadratic and describes the characteristic-seven configuration. Those sources settle the known 21-line incidence pattern; **it is not claimed here as new**. The new object is the rational 33-line *union of conjugate arrangements*, and the new result is its precise generic incidence lattice together with the complete exceptional-prime and exceptional-fiber classification. These are not implied by the incidence lattice of either 21-line subarrangement separately because additional cross-intersections between conjugate components intervene.

## Limitations
The count concerns geometric points and the fixed rational descent model; it does not classify projective isomorphism classes of all Galois-closed realizations, extensions of rationality of the intersection points, or Hilbert/symbolic-power invariants. The Galois closure can have special collisions in characteristics 2 and 7; the characteristic-three and eleven fibers have new concurrences rather than merged components. Historical priority remains possible for an unlocated equivalent study of this 33-line union. The checks establish the claimed finite arrangement identities exactly, but not any broader representation theory of the Klein automorphism group.

## References
1. G. Gévay and P. Pokora, *Klein's arrangements of lines and conics*, arXiv:2211.15309, first public 2022-11-28, https://arxiv.org/abs/2211.15309; particularly the discussion of projective uniqueness and Galois conjugates.
2. S. Innamorati, *Quasi-Configurations Derived by Special Arrangements of Lines*, Axioms 13 (2024) 321, DOI: 10.3390/axioms13050321, published 2024-05-11; especially Section 4.
3. Th. Bauer et al., *Negative curves on symmetric blowups of the projective plane, resurgences and Waldschmidt constants*, arXiv:1609.08648, first public 2016-09-27; especially Sections 2 and 9.
