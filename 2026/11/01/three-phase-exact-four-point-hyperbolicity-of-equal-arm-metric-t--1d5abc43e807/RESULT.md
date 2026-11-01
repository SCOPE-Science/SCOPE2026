# Three-phase exact four-point hyperbolicity of equal-arm metric theta graphs

## Finding
Let \(X_{a,b}\) be a three-path theta graph with two path lengths equal to \(a>0\) and the third equal to \(b\), where \(0<b\le a\). Equip its **entire geometric realization**, including edge interiors, with the shortest-path metric. The exact four-point hyperbolicity constant has three branches:

\[
\delta_4(X_{a,b})=\begin{cases}
(a+b)/4,&0<b\le a/3,\\
b,&a/3\le b\le a/2,\\
a/2,&a/2\le b\le a.
\end{cases}
\]

In particular the dependence on the shortcut length changes at precisely \(b/a=1/3\) and \(b/a=1/2\). Equivalently, it is \(\min\{a/2,\max\{(a+b)/4,b\}\}\). The middle segment is not predicted by the girth or diameter alone.

## Assumptions and scope
The space is the quotient of three closed real intervals of respective lengths \(a,a,b\), where their left endpoints are identified with one pole and their right endpoints with another. The metric is the infimum of lengths of paths in this finite metric graph. All points on every interval are admitted, including poles and arbitrary interior points. The restrictions \(a>0\) and \(0<b\le a\) are essential to the stated normalization. Permuting the two equal arms does not change the metric.

For any four points \(x_0,x_1,x_2,x_3\), write
\[
S_0=d(x_0,x_1)+d(x_2,x_3),\quad
S_1=d(x_0,x_2)+d(x_1,x_3),\quad
S_2=d(x_0,x_3)+d(x_1,x_2).
\]
Let \(S_{\max}\) and \(S_{\mathrm{med}}\) be the largest and middle of these three real numbers. The constant \(\delta_4\) is exactly \(\sup(S_{\max}-S_{\mathrm{med}})/2\). This is the *four-point* (or Gromov-product) hyperbolicity constant, **not** the sharp constant for thin geodesic triangles. These notions are equivalent for boundedness but their numerical constants need not coincide.

## Proof
Scaling all lengths by \(a^{-1}\), it suffices to assume long arms have length \(1\) and the third arm has length \(t=b/a\in(0,1]\). Put \(g(t)=(1+t)/4\), \(g(t)=t\), and \(g(t)=1/2\) on the intervals \([0,1/3]\), \([1/3,1/2]\), and \([1/2,1]\), respectively.

**Sharp lower bounds.** For \(0<t\le1/3\), the union of any long arc and the short arc is an isometrically embedded circle of circumference \(1+t\): using the remaining long arc never shortens distances, because its pole-to-pole length \(1\) is at least \(t\). Four equally spaced circle points yield four-point defect \((1+t)/4\). For \(1/3\le t\le1/2\), choose on *each* long arm the two points at distances \(u=(1-t)/2\) and \(v=(1+t)/2\) from the first pole. With the quadruple ordered \((u_1,v_1,u_2,v_2)\), the three pair sums (up to permutation) are \(2t\), \(2(1-t)\), and \(2\). Since \(t\le1/2\), the gap between the two largest is \(2t\), giving \(\delta_4\ge t\). For \(1/2\le t\le1\), use points at positions \(u=1/4\), \(v=3/4\) on each long arm; the pair sums are exactly \(1,1,2\). Hence \(\delta_4\ge1/2\). All constructions also work at transition endpoints.

**Upper bound as a finite, exact rational proof.** Coordinates on each path are measured from the first pole. For points on different paths of lengths \(L_i,L_j\), the distance equals the minimum of the two affine expressions \(u+v\) and \(L_i-u+L_j-v\); for two distinct long paths the two additional expressions \(u+t+1-v\) and \(1-u+t+v\) are required. For two points on one long path, ordered as \(u\le v\), it is the minimum of \(v-u\) and \(1+t-(v-u)\). For two points on the short path the distance is \(v-u\). Thus each of the three pair sums \(S_i\) is the minimum of an explicit finite set \(\mathcal A_i\) of affine functions of the four coordinates and \(t\).

Four labels for path membership can be sorted after permuting the points; swapping the equal arms identifies mirror cases. There are exactly **nine** resulting path multisets. The inequalities \(0\le u_i\le L_i\), the coordinate-order inequalities for points on the same arm, and each of the three closed parameter intervals are affine rational constraints. It is enough to prove, for every \(i\),
\[
\min\{S_i-S_j,S_i-S_k\}\le2g(t),\qquad\{i,j,k\}=\{0,1,2\},
\]
because \(S_{\max}-S_{\mathrm{med}}=\max_i\min\{S_i-S_j,S_i-S_k\}\). Fix arbitrary affine terms \(B\in\mathcal A_j\) and \(C\in\mathcal A_k\). Introduce \(z\) and \(w\), subject to \(z\le A\) for every \(A\in\mathcal A_i\) and
\[
w\le z-B-2g(t),\qquad w\le z-C-2g(t).
\]
The desired upper estimate follows if every such rational linear program has maximum \(w\le0\). This is proved *without numerical optimization assumptions* by supplying, for each program, a nonnegative rational multiplier for each constraint, such that its weighted sum has exactly the coefficient vector of the objective \(w\), and the weighted right-hand sides sum to a nonpositive number. The constraints then imply \(w\le0\) by the elementary Farkas dual argument. The files `theta_dual_certificates.json.gz` and `theta_verify.py` contain, respectively, every dual multiplier and a stand-alone exact-rational verifier. They cover **all 2,685 linear programs** across all nine arc-label types, all three parameter intervals, all three choices of \(i\), and every affine candidate pair \((B,C)\). There are no random/finite samples in this proof. The checker validates both the exhaustive enumeration count and all coefficient identities with `fractions.Fraction`.

For any actual quadruple, choose \(B=S_j\) and \(C=S_k\) among the finitely many attained affine terms, take \(z=S_i\), and let \(w=\min\{S_i-S_j,S_i-S_k\}-2g(t)\). The certified dual identities give \(w\le0\), completing the upper bound. Homogeneity restores general \(a>0\).

## Verification
Run `python theta_verify.py` with `theta_dual_certificates.json.gz` in the same directory using Python 3's standard library. The embedded exact certificate checker completed successfully, reporting: `PASS: 2685 exact rational LP dual certificates; complete continuous parameter domain` and `No floating-point tolerance used in the certificate check.` The certificate file is gzip-compressed JSON solely to reduce size. Each row is independently re-created from the graph metric equations and all multipliers are checked for nonnegativity, exact objective-vector equality, and a nonpositive bound; it is **not** enough to trust the compressed contents or any external solver log.

## Relationship to prior work
Carballosa, Mendez, Reyes and Sigarreta (2026), Section 2 and Theorem 2.15, prove a quarter-point reduction for the four-point/Gromov-product constant of graphs in which all edges have length one; their Section 3 gives vertex/midpoint comparison inequalities. The proof here instead gives an explicit function of an arbitrary real edge-length ratio and uses continuous parameter intervals. Their paper does not state this three-branch theta-graph formula.

Bermudo, Rodríguez, Sigarreta and Vilaire (2013), especially Theorem 8, study **the geodesic-triangle thinness** constant for multiple-edge graphs. Their bounds for unequal edge lengths and equality for equal-length edges do not determine this *four-point* constant for \(0<t<1\). The ordinary cycle lower bound corresponds to only the first branch. Mathematical records on algebraic gnarledness of theta graphs, finite regular-polygon chord metrics and theta-graph configuration homology concern other invariants; equality of graph names does not imply coverage of a four-point metric claim.

## Limitations
This statement is for exactly two equal arms and a third no longer than those arms, not arbitrary three-arm theta networks. It determines the sharp four-point constant only; no numerical equality with the sharp thin-triangle constant is asserted. The upper bound is a complete, finite *rational certificate of a continuous parametric statement*, rather than a short closed-form hand proof for every affine case. Although relevant accessible literature was compared, unindexed older case computations remain a historical-priority uncertainty. The verification and review are not independent audits.

## References
- W. Carballosa, J. Mendez, R. Reyes and J. M. Sigarreta, *The quarter-point theorem for Gromov hyperbolic graphs*, arXiv:2610.16932, initially public 2026-10-12. https://arxiv.org/abs/2610.16932
- S. Bermudo, J. M. Rodríguez, J. M. Sigarreta and J.-M. Vilaire, *Gromov hyperbolic graphs*, Discrete Mathematics **313** (2013), 1575–1585. https://doi.org/10.1016/j.disc.2013.04.009
- SageMath Graph Theory Reference, *Hyperbolicity*, the four-point graph-metric convention. https://doc.sagemath.org/html/en/reference/graphs/sage/graphs/hyperbolicity.html
