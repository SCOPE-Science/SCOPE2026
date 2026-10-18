# The all-transverse diagonal quartic over \(\mathbf F_5\) and its anticanonical Bertini spectrum

## Finding

Let \(k=\mathbf F_5\). For \(a,b,c\in k^\times\), consider the smooth degree-two del Pezzo surface
\[
S_{a,b,c}:\quad w^2=ax^4+by^4+cz^4\subset\mathbf P_k(1,1,1,2).
\]
Let \(m(a,b,c)\) denote the number of geometrically smooth members among the 31 \(k\)-rational members of \(|-K_{S_{a,b,c}}|\). Among the 64 ordered nonzero coefficient triples, the complete distribution is

| \(m(a,b,c)\) | Number of triples |
|---:|---:|
| 15 | 16 |
| 23 | 12 |
| 27 | 24 |
| 31 | 12 |

In particular, **all 31 rational anticanonical members are geometrically smooth if and only if** \((a,b,c)\) is a permutation of \((\lambda,\lambda,2\lambda)\) for some \(\lambda\in k^\times\). Equivalently, within the diagonal quartic family, the plane branch curve has no \(k\)-rational tangent line precisely for these twelve ordered triples; its dual curve has no \(k\)-rational point.

The all-smooth surfaces form exactly two \(k\)-isomorphism classes within this diagonal family: the quadratic-twist presentations \(S_{1,1,2}\) and \(S_{2,2,4}\). Each has 31 smooth genus-one anticanonical members, with the following **complete rational-point spectra**:

| Number of \(k\)-points on a smooth member | \(S_{1,1,2}\) | \(S_{2,2,4}\) |
|---:|---:|---:|
| 2 | 2 | 8 |
| 4 | 1 | 4 |
| 6 | 16 | 16 |
| 8 | 4 | 1 |
| 10 | 8 | 2 |

The two surfaces have respectively \(36\) and \(26\) rational points.

## Assumptions and scope

All enumerations are over \(k=\mathbf F_5\), not arbitrary extensions or arbitrary plane quartics. Every nonzero \(a,b,c\) gives a smooth quartic branch curve: its three partial derivatives are \(4ax^3,4by^3,4cz^3\), with no common projective zero. Because the characteristic is odd, the indicated double cover is a smooth degree-two del Pezzo surface. Its anticanonical morphism is the projection to \(\mathbf P^2\), and \(|-K|\) is the complete linear system of inverse images of lines. The 31 rational lines form the 31 rational anticanonical members.

For a rational line \(L\), the curve \(\pi^{-1}(L)\) is a double cover of \(L\simeq\mathbf P^1\) branched at the four points of the quartic intersection divisor. It is geometrically smooth exactly when that divisor has four distinct geometric points; by Riemann--Hurwitz the resulting smooth curve has genus one. Thus geometric smoothness of an anticanonical section is equivalent to transversality of the corresponding line to the quartic branch curve, including tangencies at nonrational geometric points.

## Proof

Write \(F=ax^4+by^4+cz^4\). The 31 lines \(u x+v y+t z=0\) fall into three types by the number of nonzero coefficients \((u,v,t)\): 3 coordinate lines, 12 lines supported on two coordinates (four in each coordinate pair), and 16 lines with three nonzero coefficients.

Every coordinate line is transverse because its quartic restriction is a diagonal binary quartic with two nonzero terms. If the line equation has nonzero coefficients on the \(x\)- and \(y\)-coordinates only, then eliminating \(x\) gives a binary quartic proportional to \((a+b)y^4+cz^4\): all nonzero elements of \(k\) have fourth power one. Thus those four lines are transverse exactly when \(a+b\ne0\). The other coordinate pairs are analogous.

For a line with three nonzero equation coefficients, rescale the coordinates by elements of \(k^\times\). This does not change \(F\), since every such rescaling has fourth power one, and transforms the line to \(x+y+z=0\). All 16 lines therefore have the same transversality status. Writing \(z=-x-y\), their common restricted binary quartic is \(a x^4+b y^4+c(x+y)^4\). Its discriminant is
\[
D(a,b,c)= (ab)^3+(ac)^3+(bc)^3 +3abc(a^2b+a^2c+ab^2+ac^2+b^2c+bc^2)+4a^2b^2c^2
\]
in \(k\). This is obtained by expanding the binary-quartic discriminant \(\operatorname{disc}_u(au^4+b+c(u+1)^4)\). The full line-count formula is consequently
\[
m(a,b,c)=3+4\bigl({\mathbf 1}_{a+b\ne0}+{\mathbf 1}_{a+c\ne0}+{\mathbf 1}_{b+c\ne0}\bigr)+16{\mathbf 1}_{D(a,b,c)\ne0}.
\]

The vanishing conditions are invariant under common nonzero coefficient scaling, so set \(a=1\) to check the sixteen possible normalized pairs \((b,c)\). With rows indexed by \(b=1,2,3,4\) and columns by \(c=1,2,3,4\), their exact discriminant values are
\[
\begin{pmatrix}0&2&0&2\\2&0&4&1\\0&4&3&1\\2&1&1&2\end{pmatrix}.
\]
In this matrix, the additional conditions \(1+b\ne0\), \(1+c\ne0\), \(b+c\ne0\) leave exactly the three all-transverse normalized pairs \((b,c)=(1,2),(2,1),(3,3)\). Rescaling and permuting yields precisely the twelve triples in the finding. Classifying the sixteen normalized pairs by the number of zero pair-sums and whether \(D\) vanishes gives the counts \(12,24,12,16\) for \(m=31,27,23,15\), respectively. No sampling or geometric extrapolation is used.

For \((a,b,c)=(1,1,2)\), evaluate \(F\) on \(\mathbf P^2(k)\). Every nonzero coordinate contributes its coefficient, because its fourth power is one; none of the seven nonempty subset sums of \((1,1,2)\) equals zero in \(k\). Thus the branch curve has no rational point, and each rational fiber has either zero or two rational points according to the quadratic character of its nonzero value.

The 3 coordinate lines have inverse-image point counts \(2,2,4\). The four lines involving \(x,y\) have 8 points each; the four involving \(x,z\) and four involving \(y,z\) have 10 points each. Each of the sixteen lines with three nonzero equation coefficients has three plane points with exactly two nonzero coordinates (all yielding nonsquare values) and three with all three coordinates nonzero (yielding the square 4); its inverse image has 6 points. This proves the first spectrum without machine enumeration.

Multiplying all coefficients by the nonsquare 2 gives the quadratic twist \(S_{2,2,4}\). Since every \(F(P)\ne0\), the point count on each rational anticanonical member changes from \(n\) to \(12-n\), proving the second spectrum. The number of plane points with square \(F(P)\) is 18, so \(\#S_{1,1,2}(k)=36\) and \(\#S_{2,2,4}(k)=26\). These unequal counts show the two twist presentations are not \(k\)-isomorphic. Every successful coefficient triple is obtained from one of them by coordinate permutation and multiplication by a common square (which is absorbed by scaling \(w\)), proving the stated two-class assertion within the diagonal family.

## Verification

The two complete independent reproducibility programs are `check_formula.py` and `scan_lines.py`. The first evaluates the displayed closed discriminant on all 64 coefficient triples and reconstructs the 31-line and point-count spectra using the three support patterns. The second constructs every rational point and line, restricts every one of the 64 branch quartics to all 31 lines, and tests the common projective zeros of the two partial derivatives using a 6-by-6 homogeneous Sylvester resultant over \(k\). The second method handles repeated contacts at geometric, possibly nonrational, points and roots at infinity. It then counts rational points directly by quadratic characters.

Both programs reproduce the complete tuple classification, the counts \(16,12,24,12\), the two 31-member rational-point spectra, and the surface point counts. Their expected captured outputs are in `formula_output.json` and `scan_output.json`. Run `python3 check_formula.py` and `python3 scan_lines.py` with ordinary Python 3 (no third-party dependencies). The displayed formula, discriminant table, and point-support argument also furnish a short independent mathematical proof of the main claim.

## Relationship to prior work

Asgarli--Freidin (2020) study **transverse-free** smooth plane curves, the opposite extreme in which *every* rational line is tangent; they explain this as the dual curve containing every rational point of the dual plane. The present result gives the converse extremal phenomenon \(C^*(\mathbf F_5)=\varnothing\) and a complete classification inside the diagonal quartic family, not an implication of their asymptotic density bounds.

Bergvall (2022) counts degree-two del Pezzo surfaces by the Frobenius action on their geometric Picard groups, yielding arithmetic surface-point counts. That invariant does not specify the transversality of each of the 31 rational anticanonical divisors or their point-count spectrum; the latter are the focus here.

Howe--Lauter--Top (2004) give \(x^4+y^4+z^4=0\) as a pointless quartic over \(\mathbf F_5\). **Pointlessness is not the claimed result**: within the present diagonal family that earlier displayed quartic has only 15 transverse rational lines, whereas the all-transverse branch quartic has 31. Asgarli--Ghioca (2022) investigate all-smooth rational members of linear families of hypersurfaces; their results concern hypersurface pencils, not this exact anticanonical classification on degree-two del Pezzo surfaces.

## Limitations

The result classifies the 64 ordered coefficient triples of **diagonal** quartics, not all smooth plane quartics, degree-two del Pezzo surfaces, or curves over arbitrary finite fields. Equation counts are not counts of isomorphism classes. No conclusion is claimed about geometric singularities of anticanonical members defined only over extension fields. Exact scientific priority beyond inspected literature and searchable records has not undergone independent expert verification; older unpublished tables or results phrased in dual-curve terms could present residual overlap.

## References

- S. Asgarli and B. Freidin, *On the proportion of transverse-free plane curves*, arXiv:2009.13421, first public 2020-09-28, Sections 1--2 and Theorem 1.1.
- O. Bergvall, *Frobenius actions on Del Pezzo surfaces of degree 2*, arXiv:2211.12855, first public 2022-11-23, Sections 2--4.
- S. Asgarli and D. Ghioca, *Smoothness in pencils of hypersurfaces over finite fields*, arXiv:2203.07169, first public 2022-03-14, Introduction and Theorem 1.3.
- E. W. Howe, K. E. Lauter, and J. Top, *Pointless curves of genus three and four*, arXiv:math/0403178, Table 2 (2004).
