# Two conjugate split three-line sections at the first line-splitting field of a cubic threefold

## Finding

Let \(X\subset\mathbb P^4_{\mathbf F_2}\) be the smooth cubic threefold introduced in Debarre–Laface–Roulleau, *Lines on cubic hypersurfaces over finite fields*, Section 4.5.4:
\[
\begin{aligned}
F={}&x_1^3+x_2^3+x_3^3+x_1^2x_2+x_2^2x_3+x_3^2x_1+x_1x_2x_3\\
&+x_1x_4^2+x_1^2x_4+x_2x_5^2+x_2^2x_5+x_4^2x_5=0.
\end{aligned}
\]
Write \(\mathbf F_4=\mathbf F_2(\omega)\), where \(\omega^2+\omega+1=0\), and let \(\alpha\) range over \(\{\omega,\omega^2\}\). The **complete set of eight** lines on \(X\) defined over \(\mathbf F_4\) consists, for each \(\alpha\), of the three lines
\[
\begin{split}
\Pi_\alpha\cap\{x_3=0\},\quad
\Pi_\alpha\cap\{x_3+x_2=0\},\quad
\Pi_\alpha\cap\{x_3+x_1+x_2=0\},\\
\Pi_\alpha:=\{x_4=\alpha x_1,\ x_5=\alpha x_2\},
\end{split}
\]
and the fourth line
\[
M_\alpha:=\big\{[s:s:t:\alpha t:\alpha(s+t)]:[s:t]\in\mathbb P^1\big\}.
\]
The graph on these eight lines, with an edge precisely when two distinct geometric lines intersect, is \(K_3\sqcup K_3\sqcup K_1\sqcup K_1\). Each triangle consists of the three distinct sides of the reducible plane section
\[
 X\cap\Pi_\alpha:\quad x_3(x_3+x_2)(x_3+x_1+x_2)=0.
\]
These are **the only two** \(\mathbf F_4\)-planes whose scheme-theoretic sections split as three distinct \(\mathbf F_4\)-lines. They are exchanged by \(\mathbf F_2\)-Frobenius and meet at \([0:0:1:0:0]\), a point not on \(X\). The two isolated lines \(M_\omega,M_{\omega^2}\) are also Frobenius-conjugate, and all eight lines form four Frobenius orbits of size two. Thus \(\mathbf F_4\) is the first finite extension of \(\mathbf F_2\) carrying a line on this cubic.

The previous literature already supplies the original \(\mathbf F_2\)-line nonexistence and a zeta-function calculation that **implies the cardinality eight** over \(\mathbf F_4\). The added assertion here is the explicit complete configuration: line equations, their geometric incidence, and the unique pair of conjugate split tritangent plane sections.

## Assumptions and scope

All equations use the displayed homogeneous cubic over \(\mathbf F_2\), without coordinate changes. A line is counted when it is a linear projective subspace defined over the indicated base field; geometric intersections are computed over an algebraic closure. The result concerns \(\mathbf F_4\)-rational lines and \(\mathbf F_4\)-rational planes and does **not** classify the full geometric Fano surface or line counts over larger extensions.

## Proof

**Smoothness.** In characteristic two, the five partial derivatives, in the order \(x_1,\ldots,x_5\), are
\[
\begin{aligned}
&x_1^2+x_2x_3+x_3^2+x_4^2,\\
&x_1^2+x_1x_3+x_2^2+x_5^2,\\
&x_1x_2+x_2^2+x_3^2,\qquad x_1^2,\qquad x_2^2+x_4^2.
\end{aligned}
\]
Their common projective zero locus is empty: the fourth equation forces \(x_1=0\); the fifth then forces \(x_4=x_2\), the third forces \(x_3=x_2\), the first forces \(x_2=0\), and the second forces \(x_5=0\). Hence \(X\) is smooth over the algebraic closure.

**Two split plane sections and two further lines.** Since \(\alpha^2+\alpha+1=0\) and \(\alpha^3=1\), substituting \(x_4=\alpha x_1\), \(x_5=\alpha x_2\) into \(F\) cancels the cubic terms in \(x_1,x_2\) and yields exactly \(x_3(x_3+x_2)(x_3+x_1+x_2)\). Thus the six displayed plane lines lie on \(X\). Direct substitution into \(F\) proves \(F(s,s,t,\alpha t,\alpha(s+t))=0\); therefore both \(M_\alpha\) lie on \(X\).

**Exhaustiveness.** A two-dimensional vector subspace of \(\mathbf F_4^5\) has a unique two-row reduced-row-echelon matrix, with two pivot columns \(0\le i<j\le4\) and free entries in \(\mathbf F_4\). The ten pivot choices yield a total of
\[
 {5\brack2}_4=\frac{(4^5-1)(4^4-1)}{(4^2-1)(4-1)}=5797
\]
matrices. For each pair of rows \(u,v\), a projective line is contained in \(X\) exactly when all four coefficients of the homogeneous cubic \(F(su+tv)\) vanish. The fully included standalone verifier `verify_lines.py` enumerates precisely these 5797 matrices, computes the four coefficients by exact polynomial multiplication in \(\mathbf F_4\), and obtains **exactly the eight bases** below; a second point-pair enumeration independently obtains the same eight lines.

Here \(0,1,2,3\) denote \(0,1,\omega,\omega^2\) in the matrix coordinates, respectively:

| Line index | First row | Second row |
| --- | --- | --- |
| 0 | `10020` | `01002` |
| 1 | `10020` | `01102` |
| 2 | `10030` | `01003` |
| 3 | `10030` | `01103` |
| 4 | `10120` | `01102` |
| 5 | `10130` | `01103` |
| 6 | `11002` | `00122` |
| 7 | `11003` | `00133` |

The triples \(\{0,1,4\}\) and \(\{2,3,5\}\) are precisely the plane-section triples, and lines 6 and 7 are \(M_\omega,M_{\omega^2}\). This exhausts all \(\mathbf F_4\)-lines, not merely those found by a search heuristic.

**Incidence and descent.** Two distinct lines meet if and only if the four-row matrix formed by their bases has rank three. Applying exact \(\mathbf F_4\)-row reduction to the eight bases gives precisely the six edges \(\{0,1\},\{0,4\},\{1,4\},\{2,3\},\{2,5\},\{3,5\}\). Each triangle's three pairwise intersection points are distinct (as also follows from the split factorization). No other pair meets. Frobenius permutes the line indices as \((0\ 2)(1\ 3)(4\ 5)(6\ 7)\). Hence none is defined over \(\mathbf F_2\), and the first splitting field is \(\mathbf F_4\). The two planes intersect where \(x_1=x_2=x_4=x_5=0\), namely at \([0:0:1:0:0]\); \(F\) evaluates to one there. Finally, any plane whose section splits into three distinct \(\mathbf F_4\)-lines must contain three pairwise-intersecting members of the eight-line list, and the two graph triangles are the only possibilities. This proves uniqueness.

## Verification

The self-contained Python 3 program `verify_lines.py` was executed from the package and returned:

`VERIFY_OK Grassmann=5797 F4_lines=8 graph=2K3+2K1 Frobenius=2^4 F2_lines=0 points=(9,81) split_planes=2`

The program uses two independent exhaustive descriptions of rational lines: reduced-row-echelon two-planes and pairs of projective points. It also checks the split plane factorizations, rank incidence, Frobenius action, and the point counts \(\#X(\mathbf F_2)=9\) and \(\#X(\mathbf F_4)=81\), both agreeing with the published example. The degree-three vanishing test is exact: the coefficient expansion is zero if and only if the whole projective line lies on \(X\). A separate evaluation at the five rational points of \(\mathbb P^1(\mathbf F_4)\) is cross-checked against the coefficient test; a nonzero cubic on \(\mathbb P^1\) cannot have five distinct zeros.

## Relationship to prior work

Debarre–Laface–Roulleau (2015, Section 4.5.4) introduced this particular line-free \(\mathbf F_2\)-cubic and computed point counts and the Weil polynomial of its Fano surface. Their point-count formula, together with Galkin–Shinder, already implies the cardinality of the line set over \(\mathbf F_4\): indeed \(\bigl(81^2-2(1+4^3)\cdot81+4225\bigr)/(2\cdot4^2)=8\). **That count is not claimed as original**. Their stated example does not describe the eight line equations, the two disjoint triangles, the skew conjugate pair, or the unique conjugate split plane sections. Roulleau (2013) studies Fano-surface zeta computations by a different method under hypotheses including characteristic other than two and existence of a rational line, so it does not directly supply this configuration. The Galkin–Shinder relation controls point counts but does not alone determine intersections among individual rational lines. The geometry here refines arithmetic information about the first extension on which this line-free cubic acquires rational curves.

## Limitations

This is a finite-field, exact arithmetic-geometric configuration, not an assertion about all geometric lines or the entire Fano surface. The eight-line count is already implied by published zeta information; originality is restricted to their explicit incidence and the associated split plane sections. Searches of primary literature and indexed research records found no earlier statement of that configuration, but specialized or unindexed incidence tables may exist. No independent external audit or human literature certification has been performed.

## References

1. O. Debarre, A. Laface, X. Roulleau, *Lines on cubic hypersurfaces over finite fields*, arXiv:1510.05803 (first posted 2015-10-20), Section 4.5.4, https://arxiv.org/abs/1510.05803 .
2. X. Roulleau, *The zeta functions of the Fano surfaces of cubic threefolds*, arXiv:1304.4076 (first posted 2013-04-15), https://arxiv.org/abs/1304.4076 .
3. S. Galkin, E. Shinder, *The Fano variety of lines and rationality problem for a cubic hypersurface*, arXiv:1405.5154 (first posted 2014-05-20), https://arxiv.org/abs/1405.5154 .
