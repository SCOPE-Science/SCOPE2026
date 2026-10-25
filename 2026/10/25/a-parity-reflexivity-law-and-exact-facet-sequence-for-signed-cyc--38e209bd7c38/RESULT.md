# A parity-reflexivity law and exact facet sequence for signed-cycle root polytopes

## Finding
For every integer \(n\ge3\), write \(e_1,\ldots,e_n\) for the standard basis of \(\mathbb R^n\), and define the full-dimensional, centrally symmetric lattice polytope
\[
Q_n=\operatorname{conv}\left(\{\pm e_i:1\le i\le n\}\cup\{\pm(e_i-e_{i+1}):1\le i<n\}\cup\{\pm(e_n+e_1)\}\right).
\]
Let \(Q_n^\circ=\{y:\langle x,y\rangle\le1\text{ for all }x\in Q_n\}\) be its polar, taken in the standard integer lattice. The polar has only integral vertices when \(n\) is even. When \(n\) is odd, it has exactly two nonintegral vertices,
\[
\pm\tfrac12(1,-1,1,-1,\ldots,1),
\]
and all its other vertices are integral. Consequently, **\(Q_n\) is reflexive if and only if \(n\) is even**.

Define the integer sequence \(s_0=3\), \(s_1=1\), \(s_2=5\), and, for \(n\ge3\),
\[
s_n=s_{n-1}+2s_{n-2}+2s_{n-3}.
\]
Then the exact number of facets of \(Q_n\) is
\[
\boxed{f_{n-1}(Q_n)=s_n-(-1)^n},\qquad n\ge3.
\]
For dimensions \(n=3,4,5,6,7,8\) the numbers are respectively \(14,24,62,136,310,704\). In particular, the six-dimensional symmetric cohomology polytope of the explicitly triangulated Möbius strip in Donzelmann–Holleben–Juhnke (2026, Example 2.5) is reflexive and has exactly \(136\) facets.

## Assumptions and scope
All polar and integrality statements use the *standard* lattice \(\mathbb Z^n\), not an arbitrary lattice rescaling. Each \(Q_n\) contains the crosspolytope \(\operatorname{conv}\{\pm e_i\}\) and hence is full dimensional with the origin in its interior. The theorem holds for every integer \(n\ge3\); the Möbius-strip realization is asserted only for \(n=6\), not for every dimension.

## Proof
**1. Polar inequalities and possible vertex denominators.** Direct polarity gives
\[
Q_n^\circ=\left\{y\in\mathbb R^n:\ |y_i|\le1,\quad |y_i-y_{i+1}|\le1\ (1\le i<n),\quad |y_n+y_1|\le1\right\}.
\]
Call an edge constraint *active* when its absolute-value inequality is an equality. Its active graph is a subgraph of the cycle on coordinates \(1,\ldots,n\). If at least one edge constraint is inactive, this graph is a union of paths and isolated vertices. At a vertex of the polar, every such component must contain at least one active coordinate constraint \(|y_i|=1\): otherwise the connected component has an available one-dimensional infinitesimal motion preserving its active edge equations, contradicting that the active constraints span \(\mathbb R^n\). Every coordinate of an anchored component is then an integer, since active edge equalities have right side \(\pm1\). Thus vertices with at least one inactive edge are integral.

If all \(n\) edges are active, the first \(n-1\) equations read \(y_i-y_{i+1}=\varepsilon_i\) with \(\varepsilon_i\in\{-1,1\}\), and the last reads \(y_n+y_1=\varepsilon_n\). Hence
\[
2y_1=\sum_{i=1}^n\varepsilon_i,
\]
and every coordinate differs from \(y_1\) by an integer. If \(n\) is even, all coordinates are integral. If \(n\) is odd, all coordinates are half-integral, so the bounds \(|y_i|\le1\) force \(y_i\in\{-\frac12,\frac12\}\). Saturation of the ordinary difference constraints forces alternating signs, and saturation of the twisted last sum is then automatic. There are precisely two such alternating vectors, and each is a polar vertex: its \(n\) active edge normals are independent, since the homogeneous twisted-cycle equations force every coordinate to vanish. No other nonintegral polar vertices are possible. This proves the reflexivity criterion.

**2. Complete integral-vertex criterion.** For any integral feasible point, \(y_i\in\{-1,0,1\}\). Feasibility means successive nonzero entries on each ordinary edge have the *same* sign, while nonzero entries at the twisted closing edge have *opposite* signs. Such a feasible point is a vertex exactly when every zero coordinate has at least one nonzero neighboring coordinate on the cycle, or equivalently when the cyclic ternary word contains no three consecutive zeros. Indeed, each nonzero coordinate is fixed by an active box constraint. A zero with a nonzero neighbor is fixed by their active edge constraint. Conversely, if a zero has two zero neighbors, all constraints involving that coordinate are strict, and it can be perturbed; the point is not a vertex.

**3. Exact enumeration.** Use the nine states \((a,b)\in\{-1,0,1\}^2\). Define the \(9\times9\) integer matrix \(T\) by
\[
T_{(a,b),(u,v)}=\begin{cases}1,&u=b,\ |b-v|\le1,\ (a,b,v)\ne(0,0,0),\\0,&\text{otherwise},\end{cases}
\]
and let \(S\) be the involution \(S(a,b)=(-a,-b)\). A length-\(n\) ternary word satisfying the ordinary and twisted edge conditions and containing no cyclic triple of zeros is precisely a length-\(n\) walk from a state to its image under \(S\); this follows by extending the word antiperiodically, \(y_{n+1}=-y_1\) and \(y_{n+2}=-y_2\). Therefore the number of integral vertices equals \(\operatorname{tr}(T^nS)\).

Direct nine-state matrix multiplication yields \(TS=ST\). On the \(+1\) and \(-1\) eigenspaces of \(S\), the characteristic polynomials of \(T\) are respectively
\[
\lambda^2(\lambda^3-\lambda^2-2\lambda-2)
\quad\text{and}\quad\lambda^3(\lambda-1).
\]
Thus, for every \(n\ge3\),
\[
\operatorname{tr}(T^nS)=s_n-1,
\]
where \(s_n\) is the sum of the \(n\)-th powers of the three roots of \(\lambda^3-\lambda^2-2\lambda-2\). Newton's identities give \(s_0=3,s_1=1,s_2=5\) and the stated recurrence. The polar has two additional vertices exactly in odd dimensions, so polarity gives
\[
f_{n-1}(Q_n)=(s_n-1)+\bigl(1-(-1)^n\bigr)=s_n-(-1)^n.
\]
All steps are exact and valid for arbitrarily large \(n\).

**4. Six-dimensional Möbius-strip realization.** Example 2.5 of Donzelmann–Holleben–Juhnke specifies a \(12\times6\) boundary matrix. Its rows, taken with their negatives, define the symmetric cohomology polytope. Its six one-entry rows are \(\pm e_i\). Its six two-entry rows form the signed cycle in coordinate order \((1,4,3,2,5,6)\); changing coordinate signs by \((+,+,-,+,-,+)\) makes the five successive edge vectors differences and the last a sum. This is a signed permutation of lattice coordinates, so the corresponding polytope is unimodularly equivalent to \(Q_6\). This identification is reproduced exactly in the accompanying checker.

## Verification
Run `python check.py` with Python 3 and SymPy. It independently constructs the polar inequalities; checks the nine-state characteristic-polynomial identities with exact integers; enumerates and rank-tests all feasible ternary points for \(3\le n\le8\); verifies the two fractional vertices in odd test dimensions; and checks the 2026 source's explicit \(12\times6\) matrix under the claimed signed permutation. The outputs include facet counts \(14,24,62,136,310,704\). These finite checks supplement, but do not replace, the all-dimensional proof.

## Relationship to prior work
Donzelmann, Holleben and Juhnke (2026) introduce the symmetric (co)homology polytope and exhibit a Möbius-strip boundary matrix with a determinant-two obstruction to total unimodularity (Example 2.5). Their full accessible text develops general topological and reflexivity criteria, but does not provide this signed-cycle parity criterion, a complete polar-vertex classification, or its facet-count recurrence. Our six-dimensional case computes a concrete invariant of that example; the all-dimensional signed-cycle model is a distinct, explicitly defined extension.

Ohsugi and Tsuchiya (2021, Section 7) study the larger type-B graph polytope \(B_G\), which includes **both** root signs \(\pm(e_i+e_j)\) and \(\pm(e_i-e_j)\) at every graph edge, and establish reflexivity precisely for bipartite graphs. In contrast, \(Q_n\) retains only one root-sign orbit per cycle edge, together with the coordinate generators. Hence those results do not logically settle its polar vertices or facet sequence, even though both have parity phenomena. Ehrenborg's (2024) cycle graph polytope concerns nonnegative coordinates with adjacent *sums* bounded by one, not the present centrally symmetric twisted-difference inequalities; only its indexed abstract was available in this comparison. Related type-C signed-graph root polytopes in Mészáros (2009) concern a cone-intersection construction, not this centrally symmetric hull. Published mathematical-record searches for twisted signed cycles, reflexivity, root polytopes and matching facet sequences did not identify a logically covering result; this is evidence of limited scope, not proof of global priority.

## Limitations
The polynomial recurrence counts **facets**, not the complete face vector or Ehrhart polynomial, and the theorem does not assert all-dimensional realizability as a triangulated Möbius strip. Independent auditing has not been performed. Older or unindexed signed-root-polytope literature may contain equivalent results; the searched literature and remaining access limits are detailed in the accompanying review.

## References
1. T. Donzelmann, T. Holleben, M. Juhnke, *Symmetric (co)homology polytopes*, first submitted 2026-02-19, arXiv:2602.17253v1, https://arxiv.org/html/2602.17253v1 , especially Example 2.5 and Sections 7–9.
2. H. Ohsugi, A. Tsuchiya, *Symmetric edge polytopes and matching generating polynomials*, arXiv:2008.08621v2 (2021), https://arxiv.org/pdf/2008.08621 , especially Section 7 and Example 7.3.
3. R. Ehrenborg, *The Ehrhart and face polynomials of the graph polytope of a cycle*, European Journal of Combinatorics 118 (2024), 103906, https://doi.org/10.1016/j.ejc.2023.103906 .
4. K. Mészáros, *Root polytopes, triangulations, and the subdivision algebra, II*, arXiv:0904.3339 (2009), https://arxiv.org/abs/0904.3339 .
