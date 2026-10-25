# Exact chord-quadrilateral enclosure of the regular heptagon

## Finding
Let \(H=\operatorname{conv}\{(\cos(2\pi k/7),\sin(2\pi k/7)):0\le k<7\}\). Let \(q_{\rm ch}(H)\) be the smallest area of a convex polygon with at most four sides containing \(H\), with every side parallel to a chord joining two vertices of \(H\). Then
\[
q_{\rm ch}(H)=\cos^2(\pi/7)\bigl(\tan(\pi/7)+3\tan(2\pi/7)\bigr)=3.44460347143011537377\ldots .
\]
Consequently the exact enclosure-to-polygon area ratio is
\[
\frac{q_{\rm ch}(H)}{\operatorname{area}(H)}=
\frac{2\cos^2(\pi/7)\bigl(\tan(\pi/7)+3\tan(2\pi/7)\bigr)}{7\sin(2\pi/7)}
=1.25880377354700421640\ldots <\frac3{\sqrt5}.
\]
Exactly seven enclosing polygons attain the minimum. They are congruent via sevenfold rotation. Each has four edge-supporting lines, with circular gaps between successive outward normals of \((2,4,4,4)\) units of \(\pi/7\), in cyclic order.

## Assumptions and scope
A *chord direction* means the unoriented line parallel to a segment between distinct vertices. No central symmetry of the outer quadrilateral is required. A containing polygon with fewer than four sides is included in the definition. The statement concerns the chord-restricted problem, not an unrestricted minimum enclosing quadrilateral.

## Proof
Write \(v_k=(\cos(2\pi k/7),\sin(2\pi k/7))\). The chord \(v_k-v_l\) is perpendicular to the radius at angle \(\pi(k+l)/7\) (modulo \(\pi\)); as \(k,l\) vary, these generate exactly the seven unoriented normal directions at integer multiples of \(\pi/7\) modulo \(\pi\). Thus the oriented normals are
\[
n_j=(\cos(j\pi/7),\sin(j\pi/7)),\qquad 0\le j<14.
\]
Their exact support numbers for \(H\) are \(h_j=1\) when \(j\) is even and \(h_j=\cos(\pi/7)\) when \(j\) is odd. Translate every proposed enclosing side inwards until it becomes a supporting line \(x\cdot n_j=h_j\); this cannot enlarge the area. A bounded triangle of supporting lines can likewise be cut by a further chord-direction supporting line, strictly reducing its area, since the heptagon itself is not triangular. Accordingly it suffices to consider four distinct support normals.

For four cyclic indices \(0\le i_1<i_2<i_3<i_4<14\), set \(i_5=i_1+14\) and \(g_k=i_{k+1}-i_k\). The intersection of these four supporting halfplanes is bounded precisely when each \(g_k<7\); in a bounded configuration \(1\le g_k\le6\). Even when two adjacent support lines meet at a vertex of \(H\), the following exact support-polygon formula is valid (with a zero-length side allowed):
\[
\mathcal A(i_1,i_2,i_3,i_4)
=\sum_{k=1}^4\frac{h_{i_k}h_{i_{k+1}}
-\frac12(h_{i_k}^2+h_{i_{k+1}}^2)\cos(g_k\pi/7)}
{\sin(g_k\pi/7)}.
\]
It follows by solving consecutive support-line intersections and taking the shoelace sum, equivalently by summing \(\frac12h_{i_k}\) times the length of the support edge. Indices for \(h\) are reduced modulo 14.

There are exactly 511 increasing four-index sets with all four circular gaps below seven. A finite exhaustive certificate is supplied in `check_heptagon_chord.py`: it constructs these sets directly, evaluates each formula using 65-decimal-digit outward-rounded interval arithmetic, and confirms strict separation of all but seven candidates. The seven exceptional index sets are
\[
\begin{gathered}
(1,3,7,11),\ (1,5,7,11),\ (1,5,9,11),\ (1,5,9,13),\\
(3,5,9,13),\ (3,7,9,13),\ (3,7,11,13).
\end{gathered}
\]
Their four normal indices are odd, so all support distances are the same \(c=\cos(\pi/7)\). Their circular index gaps are a cyclic arrangement of \((2,4,4,4)\). Thus **symbolically**, not by rounding,
\[
\mathcal A=c^2\sum_{k=1}^4\tan(g_k\pi/14)=c^2\left(\tan(\pi/7)+3\tan(2\pi/7)\right).
\]
The outward-rounded lower difference between any of the other 504 configurations and this exact candidate is strictly larger than \(0.02594731998604\). This certifies all strict comparisons and proves both the area and the complete equality classification. Rotating by \(2\pi/7\) permutes the seven exceptional sets transitively. Dividing by the standard regular-heptagon area \(\frac72\sin(2\pi/7)\) gives the stated ratio.

## Verification
Run `python check_heptagon_chord.py` with Python 3 and `mpmath` installed. The checker performs all 511 interval comparisons and independently constructs the four-line intersection polygons from double-precision coordinates to verify enclosure and the seven proposed minimizing areas. Its successful output begins `HEPTAGON_CHORD_INTERVAL_CERT_OK`; it displays the full set of seven equality configurations and the positive nonminimum gap. The 65-digit interval arithmetic provides a *finite exhaustive certificate* for the finite candidate list; the preceding geometric reduction, not the computation alone, establishes exhaustive applicability to all admissible enclosing polygons.

## Relationship to prior work
Vigh, *A Note on Kuperberg's Quadrilateral Conjecture* (public version of October 6, 2026), studies quadrilateral enclosures and the chord conjecture. The presently computed exact regular-seven-gon chord-restricted benchmark is distinct from the published pentagonal enclosure result. Rote (arXiv:1905.11203) considers inscribed polygon and enclosing-parallelogram algorithms, but that does not furnish this exact unrestricted-four-side chord profile. Related records on a special nonsymmetric hexagonal enclosure and regular-polygon enclosing **parallelograms** concern different restrictions; neither implies the displayed seven-gon equality classification.

## Limitations
This is the **minimum among chord-direction quadrilaterals**, not necessarily the smallest *unrestricted* enclosing quadrilateral. The inequality against \(3/\sqrt5\) is a benchmark comparison, not a proof of the general Kuperberg conjecture. Exhaustive search covers the rigorously reduced finite candidate family, and does not by itself prove the geometric reduction. An equivalent exact heptagon value may be present in older, unindexed geometry literature; historical priority has not been independently established.

## References
- Vigh, *A Note on Kuperberg's Quadrilateral Conjecture*, arXiv:2610.08168v1 (first public October 6, 2026), https://arxiv.org/abs/2610.08168.
- Rote, arXiv:1905.11203, https://arxiv.org/abs/1905.11203.
