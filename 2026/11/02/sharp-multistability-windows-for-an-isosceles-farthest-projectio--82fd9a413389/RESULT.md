# Sharp multistability windows for an isosceles farthest-projection map

## Finding
Consider the Euclidean triangle with vertices \(A=(-1,0)\), \(B=(1,0)\), and \(C=(0,h)\), where \(h>1\). Write \(z=h^2\). On its boundary let \(T\) send a point to whichever of its perpendicular projections onto the other two supporting lines is farther from the point; a tie is fixed. Because the triangle is acute, all of these projections land on the corresponding closed sides.

Define
\[
\varphi=\frac{1+\sqrt5}{2},\qquad b=3+2\sqrt3,
\]
\[
Q(z)=z^5-5z^4-5z^3-4z^2-2z-1,
\]
and let \(r=5.9614978980\ldots\) be the unique positive zero of \(Q\). The following **two disjoint open multistability windows** have exact algebraic endpoints:

1. For every \(1<z<\varphi\), the map has two distinct locally attracting primitive three-cycles and an additional locally attracting primitive four-cycle, so at least three distinct attracting periodic orbits coexist.
2. For every \(r<z<b\), the map has those two distinct locally attracting primitive three-cycles and an additional locally attracting primitive eight-cycle, again with at least three distinct attracting periodic orbits.

The primitive four-cycle has successive side labels \(0102\), and the primitive eight-cycle has labels \(01210212\), where side \(0\) is \(AB\), side \(1\) is \(BC\), and side \(2\) is \(CA\). The stated windows are **sharp for the simultaneous existence of the specified itineraries**: the two three-cycles exist precisely for \(1<z<b\) in this acute family; the \(0102\) orbit exists precisely for \(1<z<\varphi\); and, within \(1<z<b\), the \(01210212\) orbit exists precisely when \(r<z<b\). No global census of other periods is asserted.

## Assumptions and scope
Each side \(i\) is parametrized by a fraction \(u\in[0,1]\) from its first listed endpoint to its second: \(AB\), \(BC\), \(CA\). This is the farthest-*orthogonal*-projection rule, not reflected billiards, nearest projection, or a randomly switched map. All listed periodic points lie in the interiors of sides, and all branch inequalities are strict; a boundary tie is not silently assigned to a branch. A periodic orbit is locally attracting if an open relative neighborhood of its points converges cyclically to that orbit.

The eligible motivating source is Samuel Everett's *A Piecewise Contractive Map on Triangles*, published online on 2021-01-07; its journal issue bears a 2020 cover date and its later author preprint was uploaded in 2024. Primary MSC2020: 37E05.

## Proof
**1. Orthogonal-projection coordinates.** Put \(s=z+1\). Projection from side \(i\) with coordinate \(u\) to side \(j\) has the following parameter:
\[
\begin{array}{c|ccc}
 &j=0&j=1&j=2\\ \hline
 i=0&-&2(1-u)/s&(s-2u)/s\\
 i=1&(2-u)/2&-&(z-1)(1-u)/s\\
 i=2&(1-u)/2&(s-(z-1)u)/s&-
\end{array}
\]
These are dot-product projection identities on the three actual supporting lines. When \(z>1\), each of the six affine expressions takes \([0,1]\) into \([0,1]\); hence the boundary dynamics agrees with the complete-line rule. At a putative orbit point, selecting the prescribed branch is equivalent to a **strictly positive** difference between the squared distance to its target projection and the squared distance to the competing projection.

**2. Both three-cycles.** For the side word \(012\), the unique fixed point of the affine three-step projection composition has successive side coordinates
\[
\left(\frac2{z+3},\frac2{z+3},\frac{z-1}{z+3}\right).
\]
The successive target-minus-competitor squared-distance margins are exactly
\[
\frac{4z(z-1)}{(z+1)(z+3)},\quad
\frac{4z^2}{(z+3)^2},\quad
-\frac{4z(z^2-6z-3)}{(z+1)(z+3)^2}.
\]
For \(z>1\), all three are strictly positive exactly when \(z<b\). Reflection in the vertical axis produces a second three-cycle with the reverse side word \(021\). They are distinct, since their cyclic side words are inequivalent and their points are in side interiors. Each has return multiplier of modulus \((z-1)/(z+1)^2<1\). The existence and exact number of three-cycles alone were established in the earlier public two-orientation classification cited below; they are included here as an independently checked ingredient, **not** claimed as the new contribution.

**3. The four-cycle.** For side word \(0102\), solving the four-step affine fixed-point equation gives successive side parameters
\[
\left(\frac1{z+2},\frac2{z+2},\frac{z+1}{z+2},\frac z{z+2}\right).
\]
Its four distance margins, in order, are
\[
\frac{4z^2}{(z+1)(z+2)},\quad
-\frac{4z(z^2-z-1)}{(z+1)(z+2)^2},\quad
\frac{4z^2}{(z+1)(z+2)},\quad
-\frac{4z(z^2-z-1)}{(z+1)(z+2)^2}.
\]
All are positive precisely when \(1<z<\varphi\). At \(z=\varphi\), the tie is fixed rather than continued along the prescribed orbit. The side word cannot have period \(1\) or \(2\), and all four coordinates are strictly interior; the least period is four. Its four-step return multiplier equals \(1/(z+1)^2\), so the orbit is locally attracting.

**4. The eight-cycle and its quintic threshold.** Let \(D=z^3+4z^2+z+2\). For the side word \(01210212\), the eight successive coordinates of the unique affine itinerary fixed point are
\[
\frac1D\Big(3z^2+1,\ 2(z^2+1),\ z(z^2-1),\ 2(3z^2+1),
\ (z+1)(z^2+1),\ z(z+1)^2,\ 2(2z^2+z+1),\ z(z-1)^2\Big).
\]
All eight are strictly between zero and one for \(z>1\), by subtracting their numerators from \(D\). Their eight target-minus-competitor squared-distance margins are two copies each of the following four quantities (in order and then repeated at positions \(4\) through \(7\)):
\[
\begin{aligned}
M_0&=\frac{4z^2(z-1)^2}{(z+1)D},\\
M_1&=\frac{4z(z^5+2z^4+3z^3-z^2-1)}{D^2},\\
M_2&=\frac{4zQ(z)}{D^2},\\
M_3&=-\frac{4zR(z)}{(z+1)D^2},
\end{aligned}
\]
where \(R(z)=z^6-13z^5-3z^4-10z^3-5z^2-z-1\). For \(1<z<b<7\), the first two margins are positive and \(R(z)<0\), since \(z^6-13z^5<0\) and every remaining term of \(R\) is negative. Thus the only remaining inequality is \(Q(z)>0\). Descartes' rule of signs shows that \(Q\) has exactly one positive zero, and \(Q(1)<0<Q(6)=59\), so this zero is \(r\in(1,6)\), hence \(r<b\). Therefore, throughout \(1<z<b\), the eight-step itinerary is legal exactly for \(r<z<b\).

The word \(01210212\) has no smaller cyclic period and the two visits to side \(0\) have different interior coordinates, so its least period is eight. Its return multiplier is \((z-1)^4/(z+1)^6<1\); all eight switching inequalities are strict on the claimed open interval, proving local attraction. At \(z=r\), one competing distance equals the target distance, and the tie-to-fixed rule excludes the eight-cycle.

**5. Coexistence and sharpness.** The two reflection-related three-cycles are distinct from the even-period cycles by their least periods. Their basins, and the four- or eight-cycle's basin, each contain nonempty relatively open subsets of the triangle boundary because the itineraries persist and their affine returns contract. Intersecting the exactly determined admissibility inequalities gives precisely the two stated coexistence windows for these displayed families. In particular \(\varphi<r\), so the windows are disjoint. Other attracting itineraries are not ruled out.

## Verification
Run `python3 verify.py` with Python 3's standard library. The checker implements perpendicular projections using the metric \(\mathrm{diag}(1,z)\) on normalized coordinates, checks every claimed next-side parameter and strict farthest-distance decision with exact fractions for 2,145 word/parameter combinations, and verifies rational brackets around the algebraic boundaries. The return-map multipliers, factorizations, root-uniqueness and all-parameter implications are proved above rather than inferred from the finite diagnostic.

## Relationship to prior work
Everett's 2021-online paper proves qualitative asymptotic periodicity and illustrates isosceles bifurcations; its Section 4 focuses on boundary trajectories and gives no algebraic coexistence windows with simultaneous least periods three/four or three/eight. The published *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map* establishes the **three-cycle part** in greater geometric generality on complete supporting lines, including the equivalent isosceles interval \(1<z<b\). It contains no four- or eight-cycle formula or coexistence criterion. General periodic-attractor bounds for one-dimensional increasing piecewise contractions do not supply the particular triangle itinerary or its quintic switching threshold. The new statement is the simultaneous, open-parameter presence and sharp algebraic delimiters of the distinct even-period attractors alongside the already classified three-cycles.

## Limitations
The theorem supplies rigorous **lower bounds** on the number of attracting periodic orbits, not a complete period census for each parameter. The eight-cycle criterion is proved only in the displayed acute parameter region \(1<z<b\); other eight-cycle itineraries or persistence beyond that interval are not classified. No global-basin volume proportions are asserted. Publication priority beyond the inspected primary papers and published research record has not been independently established.

## References
1. Samuel Everett, *A Piecewise Contractive Map on Triangles*, *Journal of Dynamical Systems and Geometric Theories* 18(2), 183–192; first verified online publication 2021-01-07; DOI `10.1080/1726037X.2020.1847765`; author preprint arXiv `2408.16019v1` (2024-08-26); journal page `https://tarupublications.com/journals/jdsgt/volume/18/issue/2`.
2. *Exact two-orientation classification of primitive three-cycles for the farthest-projection triangle map*, public research record (2026-10-11), `https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-exact-two-orientation-classification-of-primitive-three-cycles-f--2944d54e59d8`.
3. Arnaldo Nogueira and collaborators, *Dynamics of piecewise increasing contractions*, *Bulletin of the London Mathematical Society* (2022), DOI `10.1112/blms.12577` (general contraction background; different hypotheses).
