# Joint rational theta-contact profiles of smooth plane quartics over \(\mathbf F_2\)

## Finding

Let \(C=V(F)\subset\mathbf P^2_{\mathbf F_2}\) be a geometrically smooth plane quartic. Write \(N=|C(\mathbf F_2)|\). For each of the seven rational projective lines \(L\), call \(L\) a *rational theta line* when its intersection divisor with \(C\) is twice an effective degree-two divisor. Equivalently, after choosing rational homogeneous coordinates \(s,t\) on \(L\), the restriction \(F|_L\) is a nonzero square \(Q_L(s,t)^2\) of a binary quadratic over \(\mathbf F_2\). Define \(n_i\), for \(i=0,1,2\), as the number of rational theta lines whose contact quadratic \(Q_L\) has exactly \(i\) distinct \(\mathbf F_2\)-rational projective zeros. Thus \(n_0\) records conjugate nonrational contacts, \(n_1\) a double rational contact, and \(n_2\) two distinct rational contacts.

**Exact joint classification.** Among all \(2^{15}-1=32767\) nonzero ternary quartic forms over \(\mathbf F_2\), precisely **10,920** define geometrically smooth quartics. The joint arithmetic contact invariant \((N,n_0,n_1,n_2)\) assumes **exactly 40 profiles**, with the following full number of equations and projective-equivalence classes in each profile. Projective equivalence is under \(\operatorname{PGL}_3(\mathbf F_2)\), of order \(168\); the overall 78-class count is known and is not claimed as new.

| \(N\) | \(n_0\) | \(n_1\) | \(n_2\) | Equations | Projective classes |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 | 24 | 1 |
| 0 | 1 | 0 | 0 | 56 | 1 |
| 0 | 2 | 0 | 0 | 84 | 1 |
| 0 | 7 | 0 | 0 | 1 | 1 |
| 1 | 0 | 0 | 0 | 168 | 1 |
| 1 | 0 | 1 | 0 | 252 | 2 |
| 1 | 1 | 0 | 0 | 336 | 2 |
| 1 | 1 | 1 | 0 | 168 | 1 |
| 1 | 3 | 1 | 0 | 84 | 1 |
| 2 | 0 | 0 | 0 | 504 | 3 |
| 2 | 0 | 0 | 1 | 210 | 2 |
| 2 | 0 | 1 | 0 | 840 | 5 |
| 2 | 0 | 2 | 0 | 168 | 1 |
| 2 | 1 | 0 | 0 | 168 | 1 |
| 2 | 1 | 0 | 1 | 84 | 1 |
| 2 | 1 | 1 | 0 | 504 | 3 |
| 2 | 1 | 2 | 0 | 84 | 1 |
| 2 | 2 | 0 | 0 | 84 | 1 |
| 3 | 0 | 0 | 0 | 840 | 5 |
| 3 | 0 | 0 | 1 | 672 | 4 |
| 3 | 0 | 1 | 0 | 840 | 6 |
| 3 | 0 | 1 | 1 | 84 | 1 |
| 3 | 0 | 2 | 0 | 336 | 2 |
| 3 | 1 | 0 | 0 | 224 | 2 |
| 3 | 1 | 0 | 1 | 168 | 1 |
| 3 | 1 | 1 | 0 | 168 | 1 |
| 3 | 1 | 3 | 0 | 28 | 1 |
| 4 | 0 | 0 | 0 | 840 | 5 |
| 4 | 0 | 0 | 1 | 756 | 5 |
| 4 | 0 | 1 | 0 | 504 | 3 |
| 4 | 0 | 1 | 1 | 168 | 1 |
| 4 | 0 | 2 | 0 | 168 | 1 |
| 4 | 1 | 0 | 1 | 84 | 1 |
| 4 | 1 | 0 | 2 | 21 | 1 |
| 5 | 0 | 0 | 0 | 504 | 3 |
| 5 | 0 | 0 | 1 | 336 | 2 |
| 5 | 0 | 1 | 0 | 84 | 1 |
| 5 | 0 | 1 | 1 | 84 | 1 |
| 6 | 0 | 0 | 0 | 168 | 1 |
| 7 | 0 | 0 | 0 | 24 | 1 |
| **Total** |  |  |  | **10,920** | **78** |

In particular the rational theta-line count \(n_0+n_1+n_2\) has frequency distribution \((0:3072,\ 1:5278,\ 2:2352,\ 3:105,\ 4:112,\ 7:1)\). The 218 curves-equations with at least three rational theta lines form exactly five projective orbits, represented in the fixed 15-monomial coefficient encoding by masks \(1617,1687,1689,4689,21945\), with orbit sizes \(84,84,28,21,1\), respectively. The one invariant quartic with seven rational theta lines and zero rational points is classical; its existence is not claimed as new.

## Assumptions and scope

All fields and equations here are over \(\mathbf F_2\), and geometric smoothness means smoothness after extension to an algebraic closure. Equation counts use actual nonzero forms, with no scaling ambiguity because \(\mathbf F_2^\times=\{1\}\). The source projective group acts on equations by invertible rational changes of the three homogeneous variables; these are embedded plane-quartic classes, not unpolarized moduli classes with markings forgotten. The contact quadratic is unique over \(\mathbf F_2\) because squaring is injective. A degree-two quadratic has zero, one or two distinct rational projective zeros; geometric contacts can be nonrational. This classification concerns **rational** theta lines, not all geometric theta lines or all spin structures. The stated source-context year is determined by the first public version of Pacini--Testa (2020-04-02), not by the date of this calculation.

## Proof

Write a ternary quartic as the sum of any subset of its 15 monomials, ordered by descending exponent of the first and then the second coordinate; its coefficient mask is an integer from \(1\) through \(32767\). The exact complete enumeration has two logically complementary certificates.

First, an exhaustive polynomial-arithmetic program classifies **21,847 masks as geometrically singular** by outputting, for every excluded mask, an explicit projective point over one of \(\mathbf F_2,\mathbf F_4,\mathbf F_8,\mathbf F_{16}\) where the polynomial and all three first partial derivatives vanish. The recorded witness degree counts are 20,174, 1,015, 616 and 42 respectively. A separate finite-field evaluator rechecks every printed witness. The finite extension cutoff does **not** assert that all singular quartic points in general have degree at most four: it is used only to witness singularity for the 21,847 particular excluded equations.

Second, the remaining 10,920 masks are partitioned by a complete enumeration of the \(168\) matrices of \(\operatorname{GL}_3(\mathbf F_2)\) into exactly 78 orbits, and **every orbit representative is proven geometrically smooth**: on each of the three affine projective charts, a symbolic Gröbner-basis calculation over \(\mathbf F_2\) verifies that the ideal generated by the dehomogenized polynomial and its two partial derivatives is the whole coordinate ring. Since this is a unit-ideal equality, it excludes singular points over the algebraic closure, rather than only over finitely many tested extensions. Projective transformations preserve smoothness. As all 32,767 nonzero masks occur in precisely one of these two certified partitions, the smooth list is exhaustive.

To obtain the profiles, for each smooth mask and each of the seven rational lines, the restriction to that line is formed as a binary quartic \(a_0s^4+a_1s^3t+a_2s^2t^2+a_3st^3+a_4t^4\). Over \(\mathbf F_2\), this is a nonzero quadratic square exactly when \(a_1=a_3=0\). In that case its unique root quadratic is \(Q_L=a_0s^2+a_2st+a_4t^2\), whose rational zeros are checked directly at \([1:0],[0:1],[1:1]\). Direct point evaluation supplies \(N\). Tallying all 10,920 forms yields the 40 lines of the table. Applying the group to each smooth mask separately yields the class counts, and the sum of the 78 orbit sizes is 10,920. A second independent symbolic substitution implementation rechecks all seven line restrictions and contact counts for each of the 78 representatives.

## Verification

All programs are included as portable source with literal data files and no unavailable generated dependencies. The verification sequence from the package directory is:

```sh
g++ -O3 -std=c++17 quartic_census.cpp -o quartic_census
./quartic_census
python3 quartic_profiles.py
python3 verify_certificates.py
python3 check_orbits_sympy.py
```

The last program requires SymPy (version 1.14.0 used in this run). All five commands were actually executed successfully; the independent singular-witness check certified 21,847 excluded equations and the SymPy unit-ideal/contact check certified all 78 representative classes. The machine-readable tables `contact_profiles.tsv`, `orbit_catalogue.tsv`, `quartic_profiles.json`, `smooth_quartics.txt` and `nonsmooth_certificates.tsv` provide every counted cell, representative and exclusion certificate. Checksums of these files are independently verifiable from the embedded bytes. The 40 profile counts sum to 10,920 and their projective-class counts to 78.

## Relationship to prior work

Nart--Ritzenthaler (first publicly posted 2003), in their genus-three characteristic-two classification, already enumerate the known 78 plane-quartic projective classes over \(\mathbf F_2\) and give normal-model families. Duursma (2003) already describes the exceptional twist with seven rational theta lines. Pacini--Testa (first publicly posted 2020-04-02) analyze characteristic-two theta-hyperplane multiplicities and the geometric meaning of theta hyperplanes. Therefore the bare smooth-curve count, the 78-class total and the exceptional seven-line curve are **not new claims here**. What is asserted as the additional arithmetic datum is the **joint 40-cell frequency distribution of the rational contact-divisor splitting types alongside the rational curve-point count**, including all its projective-class multiplicities. Unlike the previously known unrefined class totals and geometric bitangent configurations, this joint table records the Galois splitting and ramification of the rational theta-contact divisors simultaneously with \(N\). The known classifications allow an independent way to compute these data, but their existence alone does not state the table.

## Limitations

This is an exhaustive arithmetic theorem about one finite field, not a theorem about all extensions or a classification of the geometric bitangents over the algebraic closure. Primary literature could contain an older, unindexed equivalent contact-incidence table or a computational appendix that was not encountered. In particular, normal-model lists in older references may make some entries comparatively straightforward to reconstruct, so external publication-priority verification remains appropriate. The four-term profile is not an invariant of abstract unmarked curves under arbitrary noncanonical embeddings beyond their canonical plane-quartic models. Code replays certify the stated finite computation but do not constitute independent peer review.

## References

- M. Nart and C. Ritzenthaler, *Non-hyperelliptic curves of genus three over finite fields of characteristic two*, arXiv:math/0312366 (2003), especially the characteristic-two models and the finite-field isomorphism-class count.
- I. Duursma, *Twisted Klein curves modulo 2*, arXiv:math/0302154 (2003), especially the exceptional invariant quartic and its bitangents.
- M. Pacini and D. Testa, *Complex and tropical counts via positive characteristic*, arXiv:2004.00955v1 (2020-04-02), especially the characteristic-two theta-hyperplane arguments.
