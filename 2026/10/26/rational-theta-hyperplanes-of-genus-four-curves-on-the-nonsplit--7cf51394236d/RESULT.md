# Rational theta-hyperplanes of genus-four curves on the nonsplit quadric over \(\mathbf F_2\)

## Finding
Fix the nonsplit nonsingular quadric \(Q\subset\mathbf P^3_{\mathbf F_2}\) with equation
\[
Q=X_0X_1+X_2^2+X_2X_3+X_3^2=0.
\]
For any geometrically smooth curve \(C=Q\cap\{F=0\}\) where \(F\) is cubic, a **rational theta-hyperplane** is a hyperplane defined over \(\mathbf F_2\) whose effective intersection divisor on \(C_{\overline{\mathbf F}_2}\) is everywhere even. Write \(t(C)\) for the number of these hyperplanes among the 15 rational hyperplanes.

Exactly **27,060** nonzero cubic classes modulo \(Q\) times a linear form define geometrically smooth curves. The complete equation-weighted distribution is:

| \(t(C)\) | Cubic classes |
| ---: | ---: |
| 0 | 5,680 |
| 1 | 13,580 |
| 2 | 7,020 |
| 3 | 320 |
| 4 | 460 |
| **Total** | **27,060** |

Hence \(t(C)\le 4\) and the bound is attained. The 460 attaining equations form **seven** distinct orbits under the 120-element projective orthogonal group of the fixed quadric:

| Cubic coefficient mask | Orbit size | \(\#C(\mathbf F_2)\) | Smooth/tangent theta sections |
| --- | ---: | ---: | --- |
| `0x0093` | 120 | 2 | (2, 2) |
| `0x05be` | 30 | 3 | (2, 2) |
| `0x1293` | 60 | 2 | (3, 1) |
| `0x134d` | 60 | 1 | (3, 1) |
| `0x1cb2` | 10 | 3 | (4, 0) |
| `0x1f3c` | 60 | 3 | (1, 3) |
| `0x207a` | 120 | 3 | (2, 2) |

The parenthesized pair separates hyperplanes whose intersection with the ambient quadric is geometrically smooth (ten possibilities) from those yielding two conjugate lines (five possibilities). In particular the two kinds of theta-section behavior coexist at the sharp extremum.

## Assumptions and scope
The ground field is exactly \(\mathbf F_2\). We count scalar-normalized cubic classes modulo the four-dimensional subspace \(Q\cdot H^0(\mathbf P^3,\mathcal O(1))\), **not** 20-variable raw cubics and **not** abstract isomorphism classes. As \(\mathbf F_2^*=\{1\}\), each nonzero element of the 16-dimensional quotient is a distinct section of \(\mathcal O_Q(3)\). The complete intersection of type \((2,3)\) has degree six and canonical bundle \(\omega_C\simeq\mathcal O_C(1)\); a smooth such curve has genus four. Hyperplane evenness is tested at every geometric intersection point, not merely at rational points.

The 16 cubic basis monomials are the degree-three monomials in four coordinates **except those divisible by** \(X_0X_1\). Their ordering is specified by `data/qminus_genus4_results.json` and is used for the coefficient masks in the table. The quadratic identity \(X_0X_1=X_2^2+X_2X_3+X_3^2\) reduces all other cubic monomials to this basis.

## Proof
**1. Complete quotient and group enumeration.** The vector space of cubic forms in four variables has dimension 20, and multiplication by the nonzero quadric embeds its four-dimensional linear-form space; hence the quotient has dimension 16 and 65,535 nonzero elements. The five rational points of the nonsplit quadric are represented by the bitmasks `1, 2, 7, 11, 15`. They form a projective frame. Every permutation of the five is realized by a unique rational projective isometry preserving the displayed quadratic form; the program constructs all 120 matrices and checks preservation on all 15 nonzero vectors. Two generating permutations, a five-cycle and a transposition, induce linear transformations on the 16 cubic coefficients. Breadth-first search exhausts the 65,535 nonzero classes in exactly **683** disjoint orbits. Each orbit's size equals its explicitly enumerated set of elements; their weighted sum is 65,535.

**2. Geometric smoothness, not merely rational smoothness.** For each orbit representative, form the six Jacobian minors \(Q_iF_j+Q_jF_i\) in characteristic two, along with \(Q,F\). On each of the four affine charts \(X_i=1\), compute the Gröbner basis of the resulting ideal over \(\mathbf F_2\). The complete intersection is geometrically smooth precisely when every one of the four ideals is the unit ideal, by the Jacobian criterion and the Nullstellensatz over the algebraic closure. Exact polynomial calculations identify **254 smooth orbits**, with sizes totaling **27,060** classes. Projective isometries preserve smoothness, so this checks every class. This is an exhaustive finite calculation, not a sample over small field extensions.

**3. Exact even-divisor tests.** The 15 rational hyperplanes intersect \(Q\) in exactly ten smooth conics and five tangent conics, the latter splitting over \(\mathbf F_4\) into two conjugate lines. For a smooth conic use its explicit quadratic parametrization by \(\mathbf P^1\), restrict \(F\) to obtain a binary sextic, and test that the coefficients of all three odd-power terms vanish. Over a perfect field of characteristic two this is equivalent to the sextic being a square, hence to its divisor being everywhere even. For a tangent hyperplane with rational vertex \(P\), work over \(\mathbf F_4=\mathbf F_2(\omega)\), \(\omega^2+\omega+1=0\), on one of the conjugate lines. Evenness of the total degree-six hyperplane divisor is equivalent to \(F(P)=0\) and to the restricted cubic factoring as the linear coordinate vanishing at \(P\) times the square of a linear form. In coordinates with \(P\) at the second basis vector, the conditions are vanishing of the coefficient of the cubic term in that vector and of the mixed term of bidegree \((2,1)\) on the line. The latter coefficient has two \(\mathbf F_2\)-coordinates, so both hyperplane types give an exact three-bit linear syndrome on the 16 cubic coefficients. The code constructs all 15 syndromes from the explicit quadric geometry.

**4. Weighted classification and extremum.** Evaluate all 15 syndromes on each of the 254 smooth representatives. Since each rational hyperplane is permuted by the orthogonal group, the theta count is an orbit invariant. Weight the representatives by their enumerated orbit sizes. The resulting distribution is precisely the five bins stated above; seven smooth representative orbits have four zero syndromes, with sizes and contact-section types as displayed. Thus every smooth cubic section is included and four is sharp. The 15-syndrome calculation also reproduces the full unrestricted 65,535-class distribution as a separate consistency check.

## Verification
The standalone files `code/qminus_genus4.py` (Python and SymPy 1.14), `code/qminus_secondary.py` (Python standard library) and `data/qminus_genus4_results.json` are complete and do not depend on earlier records. From the package root run:

```sh
python code/qminus_genus4.py
python code/qminus_secondary.py data/qminus_genus4_results.json
```

The primary program exhausts all 65,535 section classes by group orbits, proves smoothness exactly with Gröbner bases, constructs the 15 theta syndromes and prints the distribution. Its actual recorded execution is in `data/replay_primary.txt`. The secondary program independently evaluates all derivatives on points over \(\mathbf F_{2^d}\) for \(d=1,2,3,4\), for all 254 smooth representatives (1,016 representative/extension tests); it also reconstructs the equation-weighted and smooth/tangent joint histograms from the certificate. Its actual recorded execution is in `data/replay_secondary.txt`. The finite-extension check corroborates, but does **not** replace, the algebraically closed-field Gröbner smoothness proof. No independent external audit has been performed.

## Relationship to prior work
Harris and Len (2017) study classical tritangent planes to canonical space sextics. Pacini and Testa (2020) give the characteristic-two notion of theta-hyperplanes via even hyperplane divisors (Definition 3.10) and general geometric counts; these do not count rational theta-hyperplanes of the nonsplit quadric over the smallest field. Xarles (2020) enumerates genus-four curves over \(\mathbf F_2\) and distinguishes the types of ambient quadrics, with point-count data. His class list provides underlying curve models, but the examined paper and public accompanying computations do not directly tabulate this equation-weighted, fixed-nonsplit-quadric theta-hyperplane distribution, its refined conic-type incidence, or its seven equality orbits. In contrast to the corresponding fixed **split** quadric, a nonsplit quadric has five (rather than nine) rational points and its rational hyperplane sections include five conjugate-line pairs, so the two fixed-quadric families are inequivalent. A classification of abstract curves alone does not mechanically determine the equation-weighted distribution without additional incidence calculations.

## Limitations
The result concerns only cubic sections of the **fixed nonsplit smooth quadric** over \(\mathbf F_2\), up to automorphisms of that quadric; it is not a count of all genus-four curves or their abstract isomorphism classes, and does not apply to smooth cubic sections of singular quadrics. Bibliographic comparison was made with the cited full papers and accessible classification program; indirect numerical derivations from existing classified models or unindexed historical tables remain possible. The verification programs are exact computational mathematics with review recorded here, not independent scientific certification.

## References
1. C. Harris and Y. Len, *Tritangent planes to space sextics: the algebraic and tropical stories*, arXiv:1701.02353, earliest public version 2017-01-09, https://arxiv.org/abs/1701.02353.
2. M. Pacini and D. Testa, *Complex and tropical counts via positive characteristic*, arXiv:2004.00955, earliest public version 2020-04-02, https://arxiv.org/abs/2004.00955.
3. X. Xarles, *A census of all genus 4 curves over the field with 2 elements*, arXiv:2007.07822, earliest public version 2020-07-15, https://arxiv.org/abs/2007.07822.
