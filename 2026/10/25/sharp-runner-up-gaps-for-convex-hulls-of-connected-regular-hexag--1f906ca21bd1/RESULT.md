# Sharp runner-up gaps for convex hulls of connected regular hexagon arrays

## Finding
Let \(M(n)\) denote the largest area of the convex hull of an edge-connected system of \(n\) congruent regular planar hexagons, each of area one. For \(n\ge3\), define the **runner-up area** \(M_2(n)\) to be the largest attainable area strictly below \(M(n)\). Then
\[
M(n)=\frac16\left\lceil n^2+\frac{14n}{3}\right\rceil,
\qquad
\boxed{M_2(n)=M(n)-\begin{cases}
\frac16,&n\equiv0,1\pmod3,\\
\frac13,&n\equiv2\pmod3.
\end{cases}}
\]
Thus the nearest nonoptimal convex-hull area is always attained, and the first forbidden discrete level has a sharp dependence on the number of cells modulo three. In particular, for \(n\equiv2\pmod3\), no polyhex has convex-hull area \(M(n)-1/6\).

## Assumptions and scope
A *polyhex* is a finite edge-connected set of cells in the regular hexagonal tiling, with individual cell area one; rotations, reflections and translations are allowed. All systems have exactly \(n\) cells and may have holes. The problem concerns the Euclidean area of the **convex hull of the whole cell union**, not the union area. We use Gaur's normalization and established exact maximum \(M(n)\) [1]. For \(n=1,2\) there is no strictly smaller attainable hull area, so the runner-up is not defined. The new claim is for every integer \(n\ge3\).

The axial-coordinate cell centers are finite connected subsets \(S\subset\mathbb Z^2\) with neighbors differing by \(\pm(1,0),\pm(0,1),\pm(1,-1)\). Writing \(P=\operatorname{conv}(S)\) and \(H\) for a unit-area centered hexagonal cell, the physical hull is area-preservingly equivalent to \(P+H\). The area identity and spanning-tree inequalities used below were proved in [1]; the discrete second-best optimization and witnesses are the new contributions.

## Proof
**1. Exact area lattice and tree defects.** Define linear forms on axial coordinates by
\[
f_1(q,r)=q+2r,\quad f_2(q,r)=q-r,\quad f_3(q,r)=2q+r,
\]
and let \(w_i=\max_{x\in P}f_i(x)-\min_{x\in P}f_i(x)\). Gaur's exact Minkowski-sum formula [1, Lemma 4] is
\[
A(S)=\operatorname{area}(P+H)
=\operatorname{area}(P)+1+\frac{w_1+w_2+w_3}{3}.
\tag{1}
\]
Every width is an integer; the lattice polygon's doubled area is an integer, including degenerate hulls. Thus \(N(S):=6A(S)\) is an integer.

Fix any spanning tree of the cell-adjacency graph, let \(s=n-1\), and let \(a,b,c\) count its edges in the three unoriented lattice directions, so \(a+b+c=s\); put \(m=\max\{a,b,c\}\). The spanning-tree estimates [1, Lemmas 6 and 7] give
\[
2\operatorname{area}(P)\le Q:=ab+bc+ca,
\qquad W:=w_1+w_2+w_3\le3s+m.
\tag{2}
\]
For clarity, the area estimate adds tree vertices one at a time: adjoining a unit edge increases convex-hull area by at most one-half the previously accumulated transverse tree-edge count; summing counts exactly the unordered pairs of nonparallel tree edges. For the width estimate, choose the tree paths realizing each of the three directional widths. A unit tree edge contributes at most three to the sum unless it lies on all three paths in a consistent positive direction; all such four-contribution edges are parallel, and there are at most \(m\) of them. These arguments cover degenerate center hulls as well.

The two quantities
\[
U:=Q-2\operatorname{area}(P),\qquad V:=3s+m-W
\]
are nonnegative **integers**. Combining (1) and (2) yields the exact identity
\[
N(S)=L(a,b,c)-3U-2V,
\quad
L(a,b,c):=3Q+6+6s+2m.
\tag{3}
\]
Gaur's theorem [1, Theorem 2] gives \(N(S)\le N_*(n):=\lceil n^2+14n/3\rceil\), with equality attainable.

**2. The exceptional congruence class.** Suppose \(n=3k+2\) with \(k\ge1\), hence \(s=3k+1\) and
\[
N_*(n)=9k^2+26k+14.
\]
The largest tree-direction count satisfies \(m\ge k+1\); write \(m=k+1+h\) for integer \(h\ge0\). The remaining two counts sum to \(2k-h\), so their product is at most \(\lfloor(2k-h)^2/4\rfloor\). Consequently
\[
N_*(n)-L\ \ge\ h+3h^2-3\left\lfloor\frac{h^2}{4}\right\rfloor.
\tag{4}
\]
If \(h\ge1\), the right side is at least four. If \(h=0\), then the remaining two counts sum to \(2k\), and \(Q\) is maximal only when they both equal \(k\). Any unequal pair reduces their integer product by at least one, hence reduces \(L\) by at least three. We conclude that **every** spanning-tree triple satisfies
\[
L=N_*(n)\quad\text{or}\quad L\le N_*(n)-3.
\tag{5}
\]
In the second case (3) gives \(N(S)\le N_*(n)-3\). In the first case, (3) gives \(N_*(n)-N(S)=3U+2V\), which cannot equal one for nonnegative integers \(U,V\). Therefore **every nonmaximal** polyhex in this residue class has \(N(S)\le N_*(n)-2\). For the other two residue classes, integrality of \(N(S)\) already bounds any nonmaximal area by \(M(n)-1/6\).

**3. Attainment in every residue class.** For nonnegative integers \(a,b,c\), start at \((0,0)\), take \(a\) center steps \((0,1)\), then \(b\) steps \((1,0)\), then \(c\) steps \((1,-1)\). These three straight runs give \(n=1+a+b+c\) distinct edge-connected cells. Their center hull has vertices among \((0,0),(0,a),(b,a),(b+c,a-c)\), with doubled area \(ab+bc+ca\). For the triples below, direct evaluation of the linear forms in (1) gives \(W=3(n-1)+b\). Hence
\[
6A=3(ab+bc+ca)+6+6(n-1)+2b.
\tag{6}
\]
The three explicit witness families are:
\[
\begin{array}{c|c|c|c}
 n& (a,b,c)&6M(n)&6A\\\hline
 3k &(k-1,k+1,k-1)&9k^2+14k&9k^2+14k-1\\
 3k+1 &(k,k+1,k-1)&9k^2+20k+6&9k^2+20k+5\\
 3k+2 &(k,k,k+1)&9k^2+26k+14&9k^2+26k+12
\end{array}
\qquad(k\ge1).
\]
Every witness is strictly nonoptimal and meets the corresponding upper bound. This proves the formula for \(M_2(n)\) for all \(n\ge3\). \(\square\)

## Verification
The accompanying standalone program `verify_polyhex_runnerup.py` uses exact integer arithmetic and an independent convex-hull-of-corners calculation, rather than the widths formula, to check all three witness families for \(3\le n\le149\). It checks every count triple satisfying \(a+b+c=n-1\) for \(3\le n\le109\), and independently enumerates all fixed connected polyhexes for \(3\le n\le9\). The second-largest normalized areas found for these seven orders are respectively \(22,34,47,63,81,100,122\); the corresponding maxima are \(23,35,49,64,82,102,123\). All checks passed. These finite tests support but do not replace the proof for arbitrary \(n\).

## Relationship to prior work
Gaur [1] establishes the exact maximum and supplies the crucial axial-coordinate area formula and tree inequalities; those ingredients are **not claimed here as new**. Its Section 7 explicitly asks for a stability version and the attainable-area spectrum. The result here identifies the first strict area level below the maximum, showing a sharp exclusion for \(n\equiv2\pmod3\). Kurz [2] solves a related full-area-spectrum problem for connected **square** tiles and formulates the regular-hexagon maximum conjecture, but does not state the polyhex runner-up law. OEIS A399934 [3] tabulates maximal values, not the runner-up. The new gap law does not follow from the maximal value alone; it uses integer-defect restrictions plus explicit nonoptimal witnesses.

## Limitations
This is a first-discrete-gap theorem, **not** a structural Hausdorff-distance stability theorem, a uniqueness characterization of near-maximizers, or the complete area spectrum. It uses the area-one regular-hexagon normalization and edge connectivity. Geometric-similarity classes of optimal or runner-up shapes are not classified. The relevant 2015 Steffanová thesis [4] was identified by metadata but not examined in full; historical priority overlap remains possible. No independent external audit has been performed.

## References
[1] P. Gaur, *The maximum area of the convex hull of a polyhex*, arXiv:2609.30310v1 (first posted 2026-09-23), https://arxiv.org/html/2609.30310v1. Theorem 2, Lemmas 4, 6, 7, Sections 4 and 7.

[2] S. Kurz, *Convex hulls of polyominoes*, arXiv:math/0702786v1 (2007), https://arxiv.org/html/math/0702786v1, especially Theorem 2 and concluding remarks.

[3] OEIS Foundation, A399934, *Six times the maximum area of the convex hull of a polyhex*, https://oeis.org/A399934.

[4] V. Steffanová, *Extremal Polyominoes*, Master's thesis, Charles University (2015), https://dspace.cuni.cz/handle/20.500.11956/67578.
