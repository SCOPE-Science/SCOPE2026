# Sharp two-point tangent-coverage deficit for plane cubics over the field of five elements

## Finding

Let \(F\in\mathbf F_5[X,Y,Z]\) be a nonzero homogeneous cubic. Define \(T(F)\) to be the union, as a set of rational projective points, of the tangent lines at all smooth \(\mathbf F_5\)-points of \(C_F=V(F)\), including when \(C_F\) is reducible or singular. Then

\[
|T(F)|\leq29<|\mathbf P^2(\mathbf F_5)|=31.
\]

The bound is sharp and is achieved by precisely \(186000\) nonzero cubic equations modulo common nonzero scalar. All such equality curves are geometrically smooth. They form exactly **two** \(\operatorname{PGL}_3(\mathbf F_5)\)-orbits, each of size \(93000\) and stabilizer order \(4\). Representatives are

\[
F_A=Y^3+4Z^3+X^2Y+X^2Z,
\qquad
F_B=X^3+2X^2Y+X^2Z+XY^2+4Z^3.
\]

The first has \(10\) rational points and misses precisely \([0:0:1]\) and \([0:1:0]\); the second has \(8\) rational points and misses precisely \([1:4:2]\) and \([1:4:3]\). They have respectively \(10\) and \(8\) distinct rational tangent lines. The distinct point counts certify that the two projective classes differ.

## Assumptions and scope

The base field is exactly \(\mathbf F_5\), and every cubic is considered up to a nonzero *scalar* in that field. A rational point \(P\in C_F(\mathbf F_5)\) is smooth precisely when the three first partial derivatives of \(F\) do not vanish simultaneously at \(P\). Its tangent line has coefficients \((F_X(P),F_Y(P),F_Z(P))\). Coverage refers to the **union of the rational points on these rational tangent lines**, not merely the rational points of the cubic or the rational points of its dual curve. No irreducibility or smoothness restriction is imposed for the universal bound; smoothness is proved for equality cases.

## Proof

A degree-three ternary form has the ordered monomial basis

\[
(X^3,Y^3,Z^3,X^2Y,X^2Z,XY^2,Y^2Z,XZ^2,YZ^2,XYZ).
\]

Since there are ten coefficients, scalar normalization by making the first nonzero coefficient equal to \(1\) gives exactly
\[
(5^{10}-1)/4=2441406
\]
representatives. The rational projective plane has \((5^3-1)/(5-1)=31\) points, represented by triples with first nonzero coordinate \(1\); the dual plane has the corresponding \(31\) rational lines.

For each normalized form, evaluate \(F\) and its three first partial derivatives at all \(31\) rational points, discard nonsmooth curve points, normalize each nonzero gradient to a line coefficient triple, and take the bitwise union of its six incident rational points. The complete 32-bin coverage-frequency enumeration in `verify_gradient.c` gives maximum \(29\), attained by exactly \(186000\) scalar classes. A separate exhaustive implementation, `verify_flags.c`, independently obtains the same entire coverage histogram by a different algebraic test: for every point-line flag \((P,L)\), choose another rational point \(Q\in L\) and check the coefficient of \(t\) in \(F(P+tQ)\). For a smooth curve point, precisely one of its six rational incident lines has vanishing coefficient, identifying the tangent. An all-zero six-flag pattern detects a singular point. The two histograms agree exactly, including the \(29\)-coverage count.

The first enumerator writes all \(186000\) maximizing normalized coefficient vectors, indexed in base \(5\). The code `generate_transformations.py` computes matrices for the five projective changes

\[
(X,Y,Z)\mapsto(X+Y,Y,Z),\quad (X,Y+Z,Z),\quad(X,Y,Z+X),\quad(2X,Y,Z),\quad(Y,X,Z).
\]

The three elementary transvections, their commutators, and the diagonal rescaling generate \(\operatorname{GL}_3(\mathbf F_5)\), and hence the full projective group. The exact orbit search in `classify_orbits.c` covers the maximizing set without leaving it, with two disjoint orbits of \(93000\) coefficients each. Since
\[
|\operatorname{PGL}_3(\mathbf F_5)|=((125-1)(125-5)(125-25))/4=372000,
\]
each stabilizer has order \(4\). This is complete orbit enumeration, not an inference from a partition or selected examples.

Both orbit representatives are geometrically smooth, as follows directly from their partial derivatives. For \(F_A\), they are \(2X(Y+Z)\), \(3Y^2+X^2\), and \(2Z^2+X^2\). At a simultaneous projective zero, \(X=0\) forces \(Y=Z=0\). If \(X\ne0\), then \(Z=-Y\), while the last two derivatives require respectively \(Y^2=3X^2\) and \(Z^2=2X^2\), a contradiction. For \(F_B\), the derivatives are \(3X^2+4XY+2XZ+Y^2\), \(2X(X+Y)\), and \(X^2+2Z^2\). The case \(X=0\) forces \(Y=Z=0\); otherwise \(Y=-X\), the first derivative forces \(Z=0\), and the last forces \(X=0\), again a contradiction. Thus both have no geometric singular point, over the algebraic closure. Smoothness is preserved by all projective transformations, so **all** maximizing cubics are smooth.

Exact rational point and tangent computations give the stated \(10\)- and \(8\)-point counts and the two listed pairs of uncovered points; `check_representatives.py` also independently checks Gröbner bases of the projective gradient equations on all three affine charts.

## Verification

Run the standalone sources in a directory containing the five verification sources and the matrix generator:

```sh
python3 generate_transformations.py
gcc -O3 -std=c11 verify_gradient.c -o verify_gradient
gcc -O3 -std=c11 verify_flags.c -o verify_flags
gcc -O3 -std=c11 classify_orbits.c -o classify_orbits
./verify_gradient > gradient_output.txt
./verify_flags > flags_output.txt
./classify_orbits > orbit_output.txt
python3 check_representatives.py > representative_output.txt
```

The last command requires SymPy for its separate symbolic chart check; the two enumeration programs and orbit checker require only a C compiler, and the matrix generator uses only the Python standard library. A run matches `EXPECTED_OUTPUT.txt`: the two exhaustive frequency histograms agree, both maxima are \(29\) with \(186000\) equations, the exact orbit sizes are \(93000\) and \(93000\), and both representatives' affine gradient ideals are the unit ideal. The orbit search consumes the data file generated by the first program, not any previous calculation.

## Relationship to prior work

Asgarli and Ghioca introduced and investigated tangent-filling plane curves, proved non-filling results under substantially larger-field hypotheses, and gave constructions in other degree regimes. Their complete accessible preprint does not supply the sharp \(\mathbf F_5\) cubic coverage number or the two equality classes. An earlier computational exclusion establishes that no plane cubic over \(\mathbf F_5\) is tangent-filling; that strictly weaker exclusion rules out coverage of \(31\) points but does not distinguish a maximum of \(29\) from \(30\), and does not classify equality. The present result is an exact extremal and orbit-refinement, **not** a new proof that the minimum tangent-filling degree is four.

Finite-projective-plane arc classifications and elliptic-curve tables may in principle imply aspects of the small-field classification, but no such implication was established from the inspected publications. This remains a specific publication-priority uncertainty.

## Limitations

The theorem is for \(\mathbf F_5\) only and makes no claim about other finite fields. All exhaustive searches concern finite exact coefficient spaces, and the geometric smoothness of the two equality representatives is proved separately. It is not claimed that the analogous extremal problem over arbitrary prime powers is solved, nor that no earlier unpublished table contains the same fixed-field result. No independent external audit has been performed.

## References

1. Shamil Asgarli and Dragos Ghioca, *Tangent-filling plane curves over finite fields*, arXiv:2302.13420, first public version 2023-02-26; *Bulletin of the Australian Mathematical Society* 109 (2024), 301–315, DOI:10.1017/S0004972723000382.
2. Kris Coolsaet, *The complete \((k,3)\)-arcs of \(\operatorname{PG}(2,q)\), \(q\le13\)*, *Journal of Combinatorial Designs* 20 (2012), 89–111, DOI:10.1002/jcd.20293. Included as related classification context, not as evidence for the claimed bound.
