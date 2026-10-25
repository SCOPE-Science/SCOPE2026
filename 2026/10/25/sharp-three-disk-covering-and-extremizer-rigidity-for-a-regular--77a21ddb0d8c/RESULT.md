# Sharp three-disk covering and extremizer rigidity for a regular hexagon

## Finding

Let \(H_R\subset\mathbb R^2\) be the closed regular hexagon with vertices \(V_j=R(\cos(j\pi/3),\sin(j\pi/3))\), for \(j=0,\ldots,5\) and \(R>0\). Define the unrestricted three-center radius
\[
\rho_3(H_R)=\inf_{c_0,c_1,c_2\in\mathbb R^2}\ \max_{x\in H_R}\ \min_{i=0,1,2}\|x-c_i\|_2.
\]
Then \(\rho_3(H_R)=3R/4\). Moreover, every minimizing **unordered** center triple is one of exactly two configurations:
\[
\mathcal C_0=R\left\{e^{2\pi i j/3}\left(\frac38+i\frac{\sqrt3}{8}\right):j=0,1,2\right\},\qquad
\mathcal C_1=e^{i\pi/3}\mathcal C_0.
\]
We identify \(\mathbb R^2\) with the complex plane only in these displayed center formulas. The two configurations are related by a symmetry of the original hexagon. In particular, there is only one minimizing configuration up to dihedral symmetry. The constructive upper bound already appears in geometric covering literature; sharpness and all equality configurations are the asserted additions.

## Assumptions and scope

Disks are closed, have the same common radius, and their centers may be anywhere in the plane; there is no extra restriction that a center lie in the covered set. The entire filled hexagon, including its boundary, must be covered. No assertion is made for nonregular hexagons, other disk counts, unequal radii, or higher dimensions. Scaling reduces the proof to \(R=1\), where \(H_1\) has vertices \(V_j=(\cos(j\pi/3),\sin(j\pi/3))\).

## Proof

**Upper bound.** Set
\[
P=(V_5+V_0)/2=(3/4,-\sqrt3/4),\quad
Q=(V_1+V_2)/2=(0,\sqrt3/2),\quad
C=(3/8,\sqrt3/8).
\]
The squared distances from \(C\) to \(P,Q,V_0,V_1,0\) are, respectively, \(9/16,9/16,7/16,7/16,3/16\). Because a disk is convex, the radius-\(3/4\) disk centered at \(C\) contains the pentagonal sector \(\operatorname{conv}\{0,P,V_0,V_1,Q\}\). Its rotations by \(2\pi/3\) and \(4\pi/3\) cover the other two sectors. These three sectors partition \(H_1\), so \(\rho_3(H_1)\le3/4\). Rotating all three disks by \(\pi/3\) gives the second exhibited covering.

**Forced vertex matching.** Suppose three disks of common radius \(r\le3/4\) cover \(H_1\). Two nonadjacent distinct hexagon vertices are at least \(\sqrt3\) apart, while a disk of radius \(r\le3/4\) has diameter at most \(3/2<\sqrt3\). A disk thus contains at most two hexagon vertices, and, if it contains two, they must be adjacent. Covering six vertices with three disks forces exactly two vertices in each disk, with no repeated vertices. The three occupied hexagon edges consequently form a perfect matching of the six-cycle. There are exactly two such matchings: the alternating edge patterns. Fix one of them, say the edges \(V_0V_1\), \(V_2V_3\), \(V_4V_5\).

**The sharp gap-contact inequality.** Consider the disk containing \(V_0,V_1\). Its intersection with the previous edge \(V_5V_0\) is an initial segment, measured from \(V_0\), of fraction \(a\in[0,1]\). Its intersection with the next edge \(V_1V_2\) is an initial segment, measured from \(V_1\), of fraction \(b\in[0,1]\). The last points of these segments are
\[
P_a=V_0+a(V_5-V_0)=(1-a/2,-\sqrt3 a/2),\qquad
Q_b=V_1+b(V_2-V_1)=(1/2-b,\sqrt3/2).
\]
Both lie in the same radius-\(r\) disk. Their squared separation therefore satisfies
\[
\left(b+\frac{1-a}{2}\right)^2+\frac34(1+a)^2
=\|P_a-Q_b\|_2^2\le4r^2\le\frac94.
\]
If \(a+b\ge1\), then \(b\ge1-a\), and the first term increases with \(b\ge0\). Consequently
\[
\|P_a-Q_b\|_2^2\ge
\left(\frac32(1-a)\right)^2+\frac34(1+a)^2
=\frac94+3\left(a-\frac12\right)^2\ge\frac94.
\]
Thus every matched-pair disk satisfies \(a+b\le1\). Furthermore, equality \(a+b=1\) is possible only at \(r=3/4\), \(a=b=1/2\), with \(\|P_a-Q_b\|_2=3/2\). In this equality case the disk center is forced to be \((P_a+Q_b)/2=C\), since it contains two points at distance equal to the disk diameter.

**Covering all three unmatched edges.** Consider the unmatched edge \(V_1V_2\). The disk containing the remote matched pair \(V_4,V_5\) cannot intersect this edge: every point of \(V_1V_2\) has vertical coordinate \(\sqrt3/2\), and \(V_4,V_5\) have vertical coordinate \(-\sqrt3/2\), a separation \(\sqrt3>2r\). So this edge must be covered by the two matched-pair disks containing \(V_1\) and \(V_2\). Their intersections with the edge are closed subsegments anchored at the two endpoints; their covered length fractions must sum to at least one. The same reasoning applies to the two other unmatched edges by rotation. Summing the three edge requirements yields \(\sum(a_i+b_i)\ge3\), where the sum is over the three matched-pair disks. The contact inequality on each disk gives \(\sum(a_i+b_i)\le3\); hence all three disk inequalities are equalities. Thus \(r=3/4\), and for each occupied pair the disk center is uniquely fixed by its two adjacent unmatched-edge midpoint contacts. This produces exactly \(\mathcal C_0\); the other perfect matching produces exactly \(\mathcal C_1\). No other optimal centers exist. Scaling by \(R\) completes the proof. \(\square\)

## Verification

The standalone script `verify.py` uses exact rational arithmetic for the squared coordinates in \(\mathbb Q(\sqrt3)\): the two contact distances are \(9/16\), the occupied vertices lie at squared distance \(7/16\), and the center has squared norm \(3/16\). It checks the threshold polynomial identity and the strict equality case on rational regression grids. The proof above derives the inequality for **all real** \(a,b\in[0,1]\); finite regression tests do not replace that universal argument. Run `python verify.py` with Python 3 and no external packages.

## Relationship to prior work

Liu (2022) formulated exactly the continuous polygonal \(p\)-center problem and reported heuristic upper and lower computations for regular hexagons with \(p=3,\ldots,10\); the regular hexagon at \(p=3\) was not among the cases reported with coincident computational bounds. Bezdek and Henderschedt (arXiv version 1, 2024) explicitly use Borsuk's decomposition of a regular hexagon into three congruent pentagons, each with the requisite circumscribed circle, to establish an upper-covering construction. Therefore the radius-\(3R/4\) *construction itself* is not new. Their finite-point universal-cover guarantee and the older Borsuk partition do not by themselves prove that **no three smaller disks cover a fixed regular hexagon**, nor classify all optimal center placements. Birgin, Gardenghi, and Laurain (preprint dated 18 April 2022) provide global asymptotic bounds and numerical regular-polygon configurations; those bounds are for large disk counts, and their reported hexagon numerical table starts at ten disks. The new boundary-gap argument supplies exact unrestricted sharpness and rigidity for three disks.

## Limitations

The proof is specific to the regular Euclidean hexagon and three congruent disks. The numerical checker does not certify infinite statements independently; the analytic inequalities and equality cases above do so. Publication-priority assessment is limited to the cited full texts and research indexes, and further older covering literature could contain equivalent proofs. An independent mathematical audit has not been performed.

## References

1. Yanchao Liu, “Two lower-bounding algorithms for the p-center problem in an area,” *Computational Urban Science* 2, article 5 (first online 24 January 2022), doi:10.1007/s43762-021-00032-9. Open full text: https://link.springer.com/article/10.1007/s43762-021-00032-9.
2. András Bezdek and Owen Henderschedt, “On a generalized hexagonal dart board problem,” arXiv:2407.03553v1 (4 July 2024), especially Sections 2 and 5, https://arxiv.org/html/2407.03553v1. This original version uses the regular-hexagon three-pentagon cover.
3. Ernesto G. Birgin, John L. Gardenghi, and Antoine Laurain, “Asymptotic bounds on the optimal radius when covering a set with minimum radius identical balls,” preprint dated 18 April 2022, https://john.pro.br/papers/bglcovering.pdf; published in *Mathematics of Operations Research*, doi:10.1287/moor.2022.0104.
