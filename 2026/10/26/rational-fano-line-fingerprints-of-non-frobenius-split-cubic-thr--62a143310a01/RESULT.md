# Rational Fano-line fingerprints of non-Frobenius-split cubic threefolds over \(\mathbf F_2\)

## Finding
Among all geometrically smooth, non-Frobenius-split cubic hypersurfaces in \(\mathbf P^4_{\mathbf F_2}\), there are exactly **13 projective-equivalence classes**. The **new arithmetic Fano-line classification** gives the rational-point count, rational-line count, projective equation orbit, stabilizer order, and point–line incidence profile of every class in the following complete table. Here a `k:v` profile entry means exactly \(v\) rational points lie on exactly \(k\) rational lines contained in the cubic.

| Class | Matrix code | Rational points | Rational lines | Equation orbit | Stabilizer | Point-incidence profile |
|---:|---:|---:|---:|---:|---:|---|
| 1 | `1118480` | 15 | 15 | 13,888 | 720 | `3:15` |
| 2 | `1118482` | 15 | 7 | 208,320 | 48 | `1:12,3:3` |
| 3 | `1118484` | 23 | 27 | 104,160 | 96 | `3:17,5:6` |
| 4 | `1118485` | 7 | 3 | 104,160 | 96 | `1:6,3:1` |
| 5 | `1118486` | 15 | 7 | 624,960 | 16 | `1:13,3:1,5:1` |
| 6 | `1118616` | 19 | 13 | 1,249,920 | 8 | `1:6,2:8,3:4,5:1` |
| 7 | `1118680` | 11 | 1 | 1,249,920 | 8 | `0:8,1:3` |
| 8 | `1118744` | 15 | 3 | 555,520 | 18 | `0:6,1:9` |
| 9 | `1118745` | 15 | 7 | 1,666,560 | 6 | `1:9,2:6` |
| 10 | `1122448` | 15 | 9 | 555,520 | 18 | `1:9,3:6` |
| 11 | `1122450` | 19 | 15 | 833,280 | 12 | `2:12,3:7` |
| 12 | `1122451` | 11 | 3 | 833,280 | 12 | `0:4,1:6,3:1` |
| 13 | `1122820` | 15 | 5 | 1,999,872 | 5 | `0:5,1:5,2:5` |

Every smooth cubic threefold in this locus contains at least one rational line and at most **27** rational lines; both bounds are sharp and each is attained by exactly one projective class. The 27-line class has 23 rational points and stabilizer order 96; the one-line class has 11 rational points and stabilizer order 8. The joint arithmetic fingerprint consisting of rational-point count, rational-line count and complete point–line incidence profile uniquely distinguishes **all 13** projective classes.

The complete equation-weighted rational-line distribution is:

| Rational lines | Smooth defining equations |
|---:|---:|
| 1 | 1,249,920 |
| 3 | 1,492,960 |
| 5 | 1,999,872 |
| 7 | 2,499,840 |
| 9 | 555,520 |
| 13 | 1,249,920 |
| 15 | 847,168 |
| 27 | 104,160 |

The sum of the weights is **9,999,360**, the number of nonsingular binary five-by-five matrices. The unweighted 13-class count is known from the theory of congruence classes of nondegenerate bilinear forms and is **not** asserted to be new. The contribution is the complete geometric Fano-line and incidence refinement and its sharp rigidity consequences.

## Assumptions and scope
The field is exactly \(\mathbf F_2\); coordinate changes are \(\operatorname{PGL}_5(\mathbf F_2)\). A cubic is non-Frobenius-split when its homogeneous coordinate ring is not F-pure (equivalently, it is not Frobenius split in its projectively normal embedding). By Fedder's criterion in characteristic two, precisely these cubics have no squarefree cubic monomials, and every such equation has the unique form
\[F_A(x)=\sum_{i,j=0}^4 A_{ij}x_i^2x_j,\qquad A\in M_5(\mathbf F_2).\]
The integer code in the table means \(\sum_{i,j=0}^4 A_{ij}2^{5i+j}\), with the row-major order \(i,j=0,\ldots,4\). Every matrix code therefore specifies an entire defining equation, without any external table dependency. Since \(\mathbf F_2^\times=\{1\}\), every equation is already uniquely scalar normalized. A rational line means an actual \(\mathbf F_2\)-defined projective line **scheme-theoretically contained** in the cubic, not merely a line having all its three rational points on the cubic. The incidence profile counts, for each rational point of the cubic, the number of its contained rational lines.

## Proof
**Nonsplitting and smoothness.** The Fedder criterion gives the indicated \(F_A\) parameterization. Its derivative is \(\partial F_A/\partial x_j=\sum_i A_{ij}x_i^2\). Over the algebraic closure the square map is bijective, so all derivatives have a common nonzero projective zero exactly when \(A\) is singular. Euler's identity for degree three confirms that a common derivative zero lies on \(F_A=0\). Thus geometric smoothness is *equivalent* to invertibility of \(A\).

**Projective equivalence.** For \(P\in\operatorname{GL}_5(\mathbf F_2)\), the substitution \(x=Py\) sends \(A\) to \(P^TAP\). Thus the classification is exactly matrix congruence, not similarity or unrestricted row–column equivalence. The group order is \(\prod_{i=0}^4(2^5-2^i)=9{,}999{,}360\). Two independently implemented orbit enumerators exhaust the \(2^{25}\) possible matrices, select precisely the invertible matrices, generate each congruence orbit using a generating set of elementary basis transformations, and obtain the identical 13 representative codes, sizes and point counts. The thirteen sizes sum to 9,999,360, and each stabilizer is group order divided by orbit size. The algorithm is exhaustive, not random sampling.

**Scheme-theoretic lines.** Put \(B_A(u,v)=u^TAv\). For independent vectors \(u,v\in\mathbf F_2^5\), the polynomial restricted to their projective line is
\[F_A(su+tv)=s^3F_A(u)+s^2tB_A(u,v)+st^2B_A(v,u)+t^3F_A(v).\]
The line is contained in the cubic *if and only if all four coefficients vanish*. Enumerate each two-dimensional binary subspace once by its unique three nonzero vectors ordered \(u<v<u+v\) as integer bit masks; there are exactly \(155\) such subspaces. The first line checker implements the four-coefficient condition and computes incidence profiles. The second line checker, completely separately, evaluates the restricted cubic on all five points of \(\mathbf P^1(\mathbf F_4)\): a binary cubic that vanishes on five distinct projective points is the zero polynomial. Both agree for every representative and all thirteen profiles in the table.

**Exhaustiveness and rigidity.** Orbit sizes cover *all* invertible \(A\), while incidence is preserved under congruence. Hence the thirteen rows prove the complete claims, including sharp one- and twenty-seven-line extremes, their uniqueness up to projective equivalence, and uniqueness of every listed joint fingerprint. For the 23-point extremizer `1118484`, the rational-point equation simplifies to \(x_2(x_0+x_2)=0\), the union of two rational hyperplanes. For the seven-point class `1118485`, it simplifies to \(x_0^2+x_0x_2+x_2^2=0\), so its rational-point set is exactly the rational projective plane \(x_0=x_2=0\). These are descriptions of **rational point sets**, not claims of geometric factorization of the smooth cubic.

## Verification
The accompanying `verification/census.c` and `verification/crosscheck.c` independently enumerate all congruence orbits. The outputs `verification/census.expected.txt` and `verification/crosscheck.expected.txt` give their exact expected results. Compile each with a standard C compiler, for example `cc -O3 -std=c11 verification/census.c -o census` and similarly for the second program, and compare stdout with the expected files. The independent `verification/lines_gf4.py` verifies rational-line containment using all points of the extension-field projective line. Its expected output is `verification/lines_gf4.expected.txt`. All three programs were executed successfully; the line-profile program agrees with the direct coefficient criterion on all 13 classes. Structured tables are `data/classes.csv` and `data/line_spectrum.csv`.

## Relationship to prior work
Kadyrsizova–Kenkel–Page–Singh–Smith–Vraciu–Witt establish the characteristic-two F-purity/matrix framework for **cubic surfaces**, not the present cubic-threefold arithmetic Fano-line census. Gow and later congruence-form literature give the previously known 13-class count for nondegenerate binary forms; this paper does not claim that count as new. Cheng studies the **geometric** Fano surface of lines of smooth \(q\)-bic threefolds and gives the general totally-isotropic two-plane criterion; the new data here instead comprise all \(\mathbf F_2\)-rational forms, their projective orbits and their *finite-field point–line incidence profiles*. Debarre–Laface–Roulleau give explicit small-field smooth cubic threefolds with various rational-line counts, including zero-line examples outside the restricted non-Frobenius-split locus; their examples do not constitute this thirteen-orbit arithmetic classification.

## Limitations
The result is confined to geometrically smooth **non-Frobenius-split** cubic threefolds over \(\mathbf F_2\); smooth cubic threefolds outside this locus may have no rational lines. Classification is by rational **projective equivalence** of embedded equations; no assertion is made about broader abstract isomorphisms beyond this. The earlier general congruence-class classification is acknowledged. Full text of Gow's 1981 article was not accessible during the literature comparison, leaving residual bibliographic priority uncertainty for the joint arithmetic refinement. The verification establishes finite exact claims; it makes no independent-expert certification claim.

## References
1. Z. Kadyrsizova, J. Kenkel, J. Page, J. Singh, K. E. Smith, A. Vraciu, E. E. Witt, *Cubic Surfaces of Characteristic Two*, arXiv:2007.12018, first public 2020-07-23, https://arxiv.org/abs/2007.12018 .
2. R. Cheng, *\(q\)-bic threefolds and their surface of lines*, arXiv:2402.09884, 2024-02-15, https://arxiv.org/abs/2402.09884 .
3. O. Debarre, A. Laface, X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, https://www.math.ens.psl.eu/~debarre/58.pdf .
4. R. Gow, *The number of equivalence classes of nondegenerate bilinear and sesquilinear forms over a finite field*, Linear Algebra Appl. 41 (1981), 175–181, DOI:10.1016/0024-3795(81)90097-5 (full article not obtained).
5. V. Y. Wang, *Dichotomous Point Counts over Finite Fields*, arXiv:2202.10427, https://arxiv.org/abs/2202.10427 (related general cubic-threefold point-count work, without the fixed-locus line-incidence census).
