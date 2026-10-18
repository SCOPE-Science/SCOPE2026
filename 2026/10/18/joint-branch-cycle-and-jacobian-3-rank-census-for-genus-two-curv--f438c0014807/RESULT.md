# Joint branch-cycle and Jacobian \(3\)-rank census for genus-two curves over \(\mathbf F_3\)

## Finding

For each smooth genus-two curve \(C/\mathbf F_3\), let \(\lambda(C)\) be the partition of six formed by Frobenius-orbit lengths of its Weierstrass points. Let \(f_3(C)\in\{0,1,2\}\) be the \(3\)-rank of its Jacobian. The following gives the complete joint classification of **arithmetic**, rather than geometric, isomorphism classes. The last column is the count of squarefree binary sextic equations in the fixed coefficient space, not a count of curves.

| Frobenius cycle partition | \(3\)-rank | \(\mathbf F_3\)-isomorphism classes | Equations |
|---|---:|---:|---:|
| \(1,1,1,1,2\) | 2 | 1 | 6 |
| \(1,1,1,3\) | 2 | 4 | 64 |
| \(1,1,2,2\) | 2 | 3 | 36 |
| \(1,1,4\) | 0 | 2 | 48 |
| \(1,1,4\) | 1 | 2 | 24 |
| \(1,1,4\) | 2 | 6 | 144 |
| \(1,2,3\) | 0 | 2 | 48 |
| \(1,2,3\) | 1 | 2 | 48 |
| \(1,2,3\) | 2 | 4 | 96 |
| \(1,5\) | 1 | 4 | 96 |
| \(1,5\) | 2 | 12 | 288 |
| \(2,2,2\) | 2 | 2 | 2 |
| \(2,4\) | 1 | 2 | 24 |
| \(2,4\) | 2 | 5 | 84 |
| \(3,3\) | 1 | 2 | 24 |
| \(3,3\) | 2 | 3 | 32 |
| \(6\) | 0 | 2 | 48 |
| \(6\) | 1 | 4 | 72 |
| \(6\) | 2 | 7 | 112 |

The entries sum to **69** arithmetic isomorphism classes and **1,296** smooth binary sextic equations. There are ten occurring Frobenius partitions and exactly nineteen nonempty partition/rank strata. Refinement by \(N(C)=\#C(\mathbf F_3)\) produces **46** nonempty triples \((\lambda,f_3,N)\); all forty-six exact counts are in `full_joint.csv` and the 69 explicit orbit representatives in `census.json`.

The six supersingular arithmetic classes occur only in the branch partitions \( (1,1,4)\), \( (1,2,3)\), \( (6)\), with exactly two classes in each. Only one arithmetic isomorphism class has four rational Weierstrass points: its branch partition is \( (1,1,1,1,2)\), it has \(3\)-rank two, and it has four rational curve points. A model is \(Y^2=XZ^5+2X^5Z\).

The raw total 69 was known before this computation. The claimed finding is the **joint** branch-cycle/\(3\)-rank/rational-point refinement, not the raw curve count, general existence, or the known extremal eight-point branch spectrum.

## Assumptions and scope

The base field is exactly \(\mathbf F_3\), and isomorphisms are defined over that field. We count smooth projective geometrically connected genus-two curves, not pointed curves, marked branch divisors, or geometrically defined isomorphism classes. Every such curve is hyperelliptic. In odd characteristic its equation takes the form \(Y^2=F(X,Z)\), where \(F\) is a homogeneous degree-six binary form with six distinct geometric roots. Set \(F(X,Z)=\sum_{i=0}^6 c_iX^iZ^{6-i}\). Models differing by \(\operatorname{GL}_2(\mathbf F_3)\) substitution represent the same arithmetic curve; since every square in \(\mathbf F_3^*\) is one, no extra coefficient-scaling equivalence is introduced. The scalar matrices act trivially on sextics, so the effective group is \(\operatorname{PGL}_2(\mathbf F_3)\), of order 24.

A branch partition records the degrees of the squarefree irreducible factors of the dehomogenized sextic, including a linear factor at infinity if the degree is five. The Jacobian \(3\)-rank equals the stable rank of the Cartier–Manin matrix, **not** necessarily its ordinary matrix rank. Squarefreeness and factorization refer to the algebraic closure, not merely to four rational positions.

## Proof

**Completeness of the model space.** Every genus-two curve has a unique hyperelliptic involution and its quotient is a genus-zero curve. Over a finite field such a conic has a rational point and is isomorphic to \(\mathbf P^1\); choosing coordinates and a model gives the stated binary sextic. The coordinate transformations and their corresponding changes of \(Y\) are precisely those described above.

**Exhaustive squarefree parameter set.** A squarefree binary sextic has affine degree either six or five: in smaller degree it is singular at infinity. The number of such nonzero forms is
\[
2(3^6-3^5)+2(3^5-3^4)=1296.
\]
The first summand counts affine degree-six polynomials and the second those of degree five. `classify.py` enumerates all \(3^7\) coefficient vectors, tests derivative gcd in \(\mathbf F_3[x]\), and reconstructs exactly this set. Its 24 explicit fractional-linear coordinate substitutions yield exactly 69 orbits, with Burnside fixed-point sum 1656, hence \(1656/24=69\).

**Two invariants.** For \(F=\sum c_iX^iZ^{6-i}\), write
\[
A=\begin{pmatrix}c_2&c_1\\c_5&c_4\end{pmatrix}.
\]
The genus-two Cartier–Manin formula in characteristic three gives \(f_3(C)=\operatorname{rank}(A^{(3)}A)\). Since the coefficients lie in \(\mathbf F_3\), this is the rank of \(A^2\). The Frobenius branch partition comes from the distinct irreducible factors of the sextic, adding a degree-one point when infinity is a root. Both invariants are constant on each orbit, as explicitly verified for every one of the 1,296 forms. Applying these rules to all 69 representatives yields the nineteen entries above; adding point counts gives the 46 strata in the included table.

**Independent arithmetic cross-check.** The separate program `crosscheck.py` uses independent SymPy gcd/factorization for all models and orbit representatives, and counts points over \(\mathbf F_3\) and \(\mathbf F_9\) by direct evaluation. With \(N_i=\#C(\mathbf F_{3^i})\) put
\[
a_1=N_1-4,\qquad a_2=\frac{a_1^2-(10-N_2)}2.
\]
The zeta numerator is \(1+a_1T+a_2T^2+3a_1T^3+9T^4\). Its degree modulo three is exactly the \(3\)-rank. Thus this check does not use the Cartier matrix for rank determination. It agrees on all 1,296 equations and on all 69 branch partitions. The class-count mass identity \(\sum_[C]1/\#\operatorname{Aut}(C)=27\) independently follows from \(1296/(24\cdot2)=27\), with the factor two coming from the hyperelliptic involution.

**The extremal rational-branch class.** Having four rational Weierstrass points forces the branch divisor to contain all four \(\mathbf P^1(\mathbf F_3)\)-points. The census finds one orbit of six sextic models of partition \( (1,1,1,1,2)\), represented by \(Y^2=XZ^5+2X^5Z\); its matrix \(A\) has stable rank two. All other branch partitions have at most three rational degree-one roots, and the table gives the claimed uniqueness.

## Verification

Run `python classify.py` in the directory containing `classify.py`; it regenerates `census.json` and prints the exact orbit and joint-stratum counts. Then run `python crosscheck.py` (requires SymPy) to check the independent splitting data and the independent extension-field rank calculation. `expected_primary.txt` records the primary output, `expected_crosscheck.txt` records the independent check, and both have been reproduced on the enclosed data. `joint_branch_prank.csv` and `full_joint.csv` are machine-readable summaries, whereas `census.json` lists all 69 explicit arithmetic orbit representatives, sizes, point counts, ranks and splitting patterns.

## Relationship to prior work

Cardona, *On the number of curves of genus 2 over a finite field* (2003), determines the number of arithmetic isomorphism classes in odd characteristic. In particular the total 69 for \(\mathbf F_3\) is not new; it is also listed in OEIS A363840. Zobernig, *Genus 2 Curves in Small Characteristic* (arXiv:2111.07270v1, 2021-11-14), determines the sizes of the geometric coarse-moduli \(p\)-rank strata; over \(\mathbf F_3\) they have sizes three, six and eighteen. These geometric counts are not the 69 arithmetic classes and do not give the joint Frobenius splitting table. Howe, *Supersingular genus-two curves over fields of characteristic three* (arXiv:math/0604413v1, 2006), determines supersingular Weil-polynomial possibilities and uses ramification factorization to exclude some possibilities. These earlier descriptions and their consequences are not claimed as new. The refined arithmetic joint frequencies across all ranks and splitting types, with rational-point counts, are the subject here.

## Limitations

The result concerns the fixed field \(\mathbf F_3\), not all characteristic-three fields. The classification is finite and proved by executable exhaustive search, not by a closed formula for arbitrary field size. It gives arithmetic classes, model frequencies, and the stated invariants, but does not classify absolute automorphism groups or derive the full individual Weil polynomials for every class. The existing arithmetic total 69 and the known eight-point spectra are prior information. The full text of Cardona's 2003 article was not available for inspection, so a previously published equivalent refinement remains a priority risk; an unsuccessful search is not proof of novelty.

## References

1. L. Zobernig, *Genus 2 Curves in Small Characteristic*, arXiv:2111.07270v1, first public 2021-11-14. https://arxiv.org/pdf/2111.07270
2. E. W. Howe, *Supersingular genus-two curves over fields of characteristic three*, arXiv:math/0604413v1, 2006. https://arxiv.org/pdf/math/0604413
3. G. Cardona, *On the number of curves of genus 2 over a finite field*, Finite Fields and Their Applications 9 (2003), 505–526. DOI: 10.1016/S1071-5797(03)00039-X.
4. OEIS A363840, arithmetic isomorphism-class counts for genus-two curves over prime fields. https://oeis.org/A363840
