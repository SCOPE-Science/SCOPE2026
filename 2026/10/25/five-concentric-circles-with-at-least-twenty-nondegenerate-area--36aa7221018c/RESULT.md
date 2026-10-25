# Five concentric circles with at least twenty nondegenerate area critical points

## Finding

For five concentric circles of radii \(1,\,7/5,\,1,\,7/5,\,1\), the signed-area function on the rotation-reduced configuration torus \(\mathbb T^4\) has at least twenty distinct nondegenerate critical points. It therefore is not a perfect Morse function, which on \(\mathbb T^4\) would have exactly sixteen critical points.

## Assumptions and scope

The five circles are centered at the origin of the Euclidean plane and are indexed cyclically. A vertex \(P_i\) lies on circle \(i\); common rotation of all vertices is quotiented out. Let \(\delta_i\) be the oriented angular increment from \(P_i\) to \(P_{i+1}\), with \(P_6=P_1\). Thus \(\sum_{i=1}^5\delta_i=0\pmod{2\pi}\), and \((\delta_1,\ldots,\delta_4)\) are coordinates on \(\mathbb T^4\), with \(\delta_5=-\sum_{i=1}^4\delta_i\pmod{2\pi}\).

The signed double area is

\[
F=\frac75\sum_{i=1}^4\sin\delta_i+\sin\delta_5.
\]

The claim is a lower bound on the number of nondegenerate critical points, not a census of every critical point for this radius tuple.

## Proof

Write \(A=7/5\), \(B=1\). Differentiating in the independent coordinates \(\delta_1,\ldots,\delta_4\) gives the critical equations

\[
A\cos\delta_i=B\cos\delta_5=\lambda\qquad (i=1,\ldots,4).
\]

For \(-1<\lambda<1\), set

\[
\alpha(\lambda)=\arccos(5\lambda/7),\qquad
\beta(\lambda)=\arccos\lambda.
\]

Each of the first four increments is \(+\alpha\) or \(-\alpha\), and the fifth is \(+\beta\) or \(-\beta\). Define

\[
\begin{aligned}
g_1(\lambda)&=4\alpha(\lambda)+\beta(\lambda)-4\pi,\\
g_2(\lambda)&=4\alpha(\lambda)-\beta(\lambda)-2\pi,\\
g_3(\lambda)&=2\alpha(\lambda)+\beta(\lambda)-2\pi,\\
g_4(\lambda)&=4\alpha(\lambda)+\beta(\lambda)-2\pi.
\end{aligned}
\]

The exact-rational interval checker supplied with this result certifies the following strict endpoint signs:

- \(g_1(-0.9993)>0\) and \(g_1(-0.9992)<0\);
- \(g_2(-0.837)>0\) and \(g_2(-0.836)<0\);
- \(g_3(-0.615)>0\) and \(g_3(-0.614)<0\);
- \(g_4(0.400)>0\) and \(g_4(0.401)<0\).

By continuity, each function has a root in its stated interval. These four intervals are disjoint. The roots produce the following distinct critical configurations:

1. At a root of \(g_1\), the all-positive sign pattern has sum \(4\alpha+\beta=4\pi\); its all-negative complement has sum \(-4\pi\). This gives two points.
2. At a root of \(g_2\), the patterns \((-\alpha,-\alpha,-\alpha,-\alpha,+\beta)\) and its complement have sums \(-2\pi\) and \(2\pi\). This gives two points.
3. At a root of \(g_3\), choose exactly one of the first four increments to be \(+\alpha\), the other three to be \(-\alpha\), and set \(\delta_5=-\beta\). The sum is \(-2\alpha-\beta=-2\pi\). There are four choices for the exceptional position; their complements give four more points. This gives eight points.
4. At a root of \(g_4\), the all-positive and all-negative patterns have sums \(2\pi\) and \(-2\pi\). This gives two points.
5. At \(\lambda=1\), let \(\alpha_0=\arccos(5/7)\), set \(\delta_5=0\), and choose any two of \(\delta_1,\ldots,\delta_4\) to equal \(+\alpha_0\), the other two equaling \(-\alpha_0\). The sum is zero and the critical equations hold. There are \(\binom42=6\) such points.

The total is \(2+2+8+2+6=20\). Distinctness follows from the disjoint multiplier intervals, the different sign patterns, and the six separate choices at \(\lambda=1\).

It remains to check nondegeneracy. In the four independent coordinates the Hessian is

\[
H=-A\,\operatorname{diag}(\sin\delta_1,\ldots,\sin\delta_4)
-B\sin\delta_5\,\mathbf 1\mathbf 1^{\mathsf T}.
\]

For the all-positive and all-negative patterns in items 1 and 4, \(H\) is respectively negative definite and positive definite. For item 2, the Hessian eigenvalues are \(A\sin\alpha\) with multiplicity three and \(A\sin\alpha-4B\sin\beta\) in the remaining direction, with signs reversed for the complementary pattern. On \((-0.837,-0.836)\), \(\sin\beta=\sqrt{1-\lambda^2}>0.54\), so \(4B\sin\beta>2.16>1.4\ge A\sin\alpha\); neither eigenvalue is zero. For item 3, the determinant lemma reduces nondegeneracy to

\[
\sum_{i=1}^5\frac{1}{a_i\sin\delta_i}\ne0,
\qquad (a_1,\ldots,a_5)=(A,A,A,A,B).
\]

For the stated pattern this sum is \(-2/(A\sin\alpha)-1/(B\sin\beta)<0\), and it is positive for the complement. For the six points in item 5, \(\sin\delta_5=0\), so \(H\) is diagonal with entries \(\pm A\sin\alpha_0\), all nonzero. Thus all twenty exhibited critical points are nondegenerate.

Finally, the Betti numbers of \(\mathbb T^4\) are \(\binom4k\), whose sum is \(2^4=16\). A perfect Morse function has exactly this many critical points. Since this function has at least twenty nondegenerate critical points, it cannot be perfect Morse.

## Verification

The companion script uses only the Python standard library and exact rational interval bounds. It evaluates the signs of the eight endpoint expressions using a Machin-formula enclosure for \(\pi\), rational square-root bounds, and alternating-series bounds for arctangent; all sign assertions are exact rational comparisons. The remaining nondegeneracy inequalities are proved symbolically in the text. The argument establishes a lower bound of twenty; it does not assert that no further critical points exist.

## Relationship to prior work

Siersma's paper on polygons whose vertices slide along prescribed curves gives the same area function, derives the general criticality condition, and explicitly asks whether the area function for concentric circles is perfect Morse. It proves the three-circle case and, under opposite-radius inequalities, the four-circle case. The five-circle example above addresses a new parameter tuple and supplies a counterexample to extending perfectness to all such configurations. A separate literature search found related work on perimeter critical points for concentric circles and on perfect Morse functions for three-dimensional polygonal linkages, but neither has the same planar five-circle area function and claim.

## Limitations

Only one explicit radius tuple is treated. The proof supplies twenty nondegenerate critical points but does not classify all critical points for this tuple, determine the complete Morse-index distribution, or decide which other five-circle radius tuples are perfect Morse.

## References

- D. Siersma, *Extremal Area of Polygons sliding along Curves*, arXiv:2211.13978v1, first public 2022-11-25; 2020 Mathematics Subject Classification 58K05, 57R70. Published in *Journal of Geometry and Physics* 187 (2023), article 104786, DOI 10.1016/j.geomphys.2023.104786.
- G. Khimshiashvili and D. Siersma, *Connecting Cycles for Concentric Circles*, arXiv:1901.09866 (perimeter, not area).
- G. Panina, *Oriented area is a perfect Morse function*, arXiv:1611.04265 (a three-dimensional polygon-linkage setting, not the planar concentric-circle configuration here).
