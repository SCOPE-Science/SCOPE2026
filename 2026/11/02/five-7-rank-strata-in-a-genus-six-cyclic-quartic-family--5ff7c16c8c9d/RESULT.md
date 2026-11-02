# Five \(7\)-rank strata in a genus-six cyclic-quartic family

## Finding

Let \(k=\overline{\mathbb F}_7\), and let \(C_{a,b}\) be the smooth projective model of
\[
 y^4=x^5+a x^2+b x+1,
\]
where \((a,b)\in k^2\) and
\[
 \Delta(a,b)=3a^5+a^4b^2+3a^2b+3ab^3-3b^5+3\ne0.
\]
Every member of this smooth locus has genus \(6\). Put
\[
 U=a^3-b,\qquad V=3a,\qquad H=3b^3-3ab-2a^4.
\]
Writing \(f_7(C)\) for the Jacobian \(7\)-rank and \(\alpha(C)\) for the Jacobian \(a\)-number, the exact formulas are
\[
 f_7(C_{a,b})=2\mathbf{1}_{H\ne0}+\mathbf{1}_{U\ne0}+\mathbf{1}_{V\ne0},
 \qquad
 \alpha(C_{a,b})=2+\mathbf{1}_{UV=0}.
\]
The formulas give all five ranks \(0,1,2,3,4\): rank \(4\) off \(HUV=0\); rank \(3\) on \(UV=0\), away from \(H=0\); rank \(2\) on \(H=0\), away from \(UV=0\); rank \(1\) precisely at the five points \(b=a^3\), \(a^5=4\); and rank \(0\) only at \((a,b)=(0,0)\). The \(a\)-number is \(3\) when \(UV=0\) and \(2\) otherwise. Every assertion concerns coefficient-marked parameters on the smooth locus, not geometric isomorphism classes.

The projective closure of the third rank-drop component \(H=0\) is a geometrically irreducible plane quartic with one ordinary node and normalization of genus \(2\). Thus a genus-two curve, two rational components, five smooth rank-one parameter points, and one smooth rank-zero parameter govern the entire stratification.

## Assumptions and scope

The base field is algebraically closed of characteristic \(7\). All parameters satisfy \(\Delta\ne0\). The affine polynomial has degree \(5\), is squarefree, and is coprime in degree to the exponent \(4\); hence the cover has full ramification index \(4\) at its five finite branch points and at infinity. The Riemann–Hurwitz formula gives \(2g-2=-8+6(4-1)=10\), so \(g=6\). The distinguished fiber \(y^4=x^5+1\) has an additional order-five scaling symmetry; the two monomials \(x^2\) and \(x\) supply two independent coefficient deformations preserving the order-four deck action.

The polynomial \(\Delta\) is the discriminant of \(x^5+ax^2+bx+1\) in characteristic \(7\). Its nonvanishing, not a restriction on rational points alone, is necessary for every case of the theorem.

## Proof

Write \(\omega_{j,i}=x^i\,dx/y^j\). A basis for regular differentials, in the stated order, is
\[
 (\omega_{1,0},\omega_{2,0},\omega_{2,1},\omega_{3,0},\omega_{3,1},\omega_{3,2}).
\]
At the unique point over infinity, \(\operatorname{ord}(x)=-4\), \(\operatorname{ord}(y)=-5\), and \(\operatorname{ord}(dx)=-5\); thus these six forms have nonnegative orders and are regular also at finite branch points. They are independent and span because \(g=6\).

Let \(F=x^5+ax^2+bx+1\). For a column \(\omega_{j,i}\), choose \(j'\in\{1,2,3\}\) with \(7j'\equiv j\pmod4\), and set \(e=(7j'-j)/4\). The Cartier coefficient of \(\omega_{j',t}\) is the seventh root of \([x^{7(t+1)-1-i}]F^e\). Thus, in the displayed basis, the seventh powers of the Cartier matrix entries form the following coefficient matrix (all coefficients reduced modulo \(7\)):
\[
 M=\begin{pmatrix}
 0&0&0&0&1&0\\
 0&U&3a^2b+3&0&0&0\\
 0&0&V&0&0&0\\
 3a^3+2a^2b^2-2ab^4-b&0&0&0&0&0\\
 H&0&0&0&0&0\\
 -2&0&0&0&0&0
 \end{pmatrix}.
\]
The action preserves the two-dimensional character subspace with \(j=2\) and interchanges the \(j=1\) one-dimensional subspace with the \(j=3\) three-dimensional subspace. For \(j=2\) its triangular coefficient block has diagonal entries \(U,V\). Every iterated Frobenius-semilinear product therefore has eventual rank exactly \(\mathbf1_{U\ne0}+\mathbf1_{V\ne0}\): if both vanish, then \((a,b)=(0,0)\) and the block is strictly upper triangular; if one is nonzero, its diagonal gives one persistent direction; if both are nonzero, the block is invertible.

On the other four-dimensional block, the map from \(j=3\) to \(j=1\) selects its middle coordinate. The return map sends the \(j=1\) generator to a vector whose middle coordinate is exactly \(H\) and whose last coordinate is the nonzero constant \(-2\). Consequently its stable semilinear rank is \(2\) for \(H\ne0\), while for \(H=0\) its third iterate is zero. These statements remain true after any Frobenius twisting because the nonzero/zero conditions are stable under seventh powers. The sum of the stable ranks gives the claimed \(f_7\) formula.

The Cartier rank on the four-dimensional block is always \(2\). Its rank on the \(j=2\) block is \(2\) exactly when \(UV\ne0\), and otherwise \(1\): at \(U=V=0\) its upper-right coefficient equals \(3\). Hence \(6-\operatorname{rank}(\mathrm{Cartier})=2+\mathbf1_{UV=0}\), the stated \(a\)-number.

For the deeper intersections, \(H(0,b)=3b^3\) gives only the origin on the line \(a=0\). On \(b=a^3\), substitution gives \(H=a^4(2+3a^5)\); its nonzero roots satisfy \(a^5=4\). The derivative \(5a^4\) shows that there are exactly five distinct such roots in \(k\). Direct substitution in the discriminant yields \(\Delta=4\) at all five points, and \(\Delta(0,0)=3\), so all six deepest points belong to the smooth family. The rank formulas and these intersections give the five-stratum classification.

Finally, homogenize \(H\) to \(3B^3Z-3ABZ^2-2A^4\). At infinity there is only \([0:1:0]\), where the \(Z\)-derivative is \(3\), so it is smooth. In the affine chart, the equations \(H_a=H_b=0\) imply \(b=2a^3\) and either \(a=0\) or \(a^5=3\). The latter is incompatible with \(H=a^4(3a^5-1)=0\). Hence the only singular point is \((0,0)\). Its quadratic tangent cone is \(-3ab\), two distinct lines, so it is an ordinary node. The quartic is geometrically irreducible: otherwise distinct components would meet by Bézout, necessarily only at this ordinary node, with total intersection multiplicity at least \(3\) for any partition of degree \(4\), contradicting its transverse two-branch multiplicity \(1\). A plane quartic has arithmetic genus \(3\), and subtracting the node's delta-invariant \(1\) gives normalization genus \(2\).

## Verification

Run `python verify_symbolic.py` and `python verify_primefield.py` with Python 3; the first uses SymPy and the second uses only the standard library. Both files are standalone and their displayed assertions are exact arithmetic. Successful output is `CYCLIC4_G6_SYMBOLIC_OK` and `CYCLIC4_G6_PRIMEFIELD_OK {0: 1, 1: 1, 2: 4, 3: 9, 4: 29}`.

The symbolic program independently regenerates the full matrix using coefficient extraction, verifies the discriminant, all deeper-intersection identities, and the complete projective singularity conditions for the quartic. The second program independently constructs the matrix by finite-field polynomial convolution for every smooth parameter over \(\mathbb F_7\), checks ranks of sixfold products and Cartier rank, and confirms the point-count congruence \(\#C_{a,b}(\mathbb F_7)\equiv1-\operatorname{tr}M\pmod7\). There are \(44\) smooth prime-field marked pairs, distributed among the five rank values as \(1,1,4,9,29\). This finite census corroborates but does not replace the all-geometric-parameter proof above.

## Relationship to prior work

Obus–Shaska (2020) describe exceptional superelliptic curves with extra automorphisms, including cyclic monomial models, motivating deformation of a highly symmetric cyclic-cover fiber; their work studies automorphism groups and complex multiplication rather than this characteristic-seven rank stratification. Sutherland (2020) gives general superelliptic Cartier–Manin matrix formulas and coefficient algorithms, which underlie the method but do not state the particular five-stratum classification or the nodal genus-two parameter component. Özman–Pries–Weir (2019) study moduli-theoretic rank strata of cyclic covers, with the principal existence theorem for cyclic triple covers; their methods do not yield this explicit composite-degree-four coefficient family. The present calculation uses established Cartier theory, not a new general Cartier algorithm.

## Limitations

The theorem concerns the marked affine coefficient family with \(\Delta\ne0\). No classification modulo projective or geometric isomorphism, of Newton polygons, supersingularity, Ekedahl–Oort type beyond the stated \(a\)-number, or of all genus-six fourfold covers is asserted. The prime-field census is finite and is not used as a proof for all algebraically closed-field parameters. Prior-work comparisons cannot exclude every unindexed earlier computation; no independent external validation is claimed.

## References

- A. Obus and T. Shaska, *Superelliptic curves with many automorphisms and CM Jacobians*, arXiv:2006.12685, first submitted 2020-06-23, Sections 1 and 3 (https://arxiv.org/html/2006.12685v2).
- A. V. Sutherland, *Counting points on superelliptic curves in average polynomial time*, arXiv:2004.10189, first submitted 2020-04-21, Sections 2 and 7 (https://arxiv.org/html/2004.10189v5).
- E. Özman, R. Pries, and C. Weir, *The boundary of the \(p\)-rank \(0\) stratum of the moduli space of cyclic covers of the projective line*, arXiv:1907.05684, first submitted 2019-07-12, Introduction and Sections 4–5 (https://arxiv.org/abs/1907.05684).
