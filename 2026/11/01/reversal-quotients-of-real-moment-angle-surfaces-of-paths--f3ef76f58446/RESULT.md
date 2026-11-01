# Reversal quotients of real moment-angle surfaces of paths

## Finding
Let \(P_n\) be the simplicial path with \(n\ge3\) vertices, let \(R_n=(D^1,S^0)^{P_n}\), and let \(\rho\) reverse its coordinate order. Then the ordinary quotient \(Q_n=R_n/\langle\rho\rangle\) is a compact connected surface. The exceptional quotient \(Q_3\) is a disk. For every \(n\ge4\), it is **nonorientable** and has exactly
\[
 b_n=2^{n-3}\quad\text{boundary components},\qquad
 h_n=2+(n-4)2^{n-3}-2^{\lfloor(n-1)/2\rfloor-1}
\]
crosscaps (nonorientable genus). The fixed set of \(\rho\) comprises exactly \(2^{\lfloor(n-1)/2\rfloor}\) proper disjoint arcs, and \(R_n\setminus\operatorname{Fix}(\rho)\) is connected if and only if \(n\ge4\).

In particular, for \(n\ge4\),
\[
 \pi_1(Q_n)\cong F_{\,1+(n-3)2^{n-3}-2^{\lfloor(n-1)/2\rfloor-1}},\qquad
 H_1(Q_n;\mathbb Z)\cong\mathbb Z^{\,1+(n-3)2^{n-3}-2^{\lfloor(n-1)/2\rfloor-1}}.
\]
The first examples, \(n=4,5,6,7\), have respective genus–boundary pairs \((1,2),(4,4),(16,8),(46,16)\). Higher homology vanishes, since the quotient has boundary.

## Assumptions and scope
The interval is \(D^1=[-1,1]\) and its zero-sphere is \(S^0=\{-1,1\}\). The path is the one-dimensional simplicial complex with faces \(\varnothing\), \(\{i\}\), and \(\{i,i+1\}\) for \(1\le i<n\). Thus \(R_n\subset D^{1\,n}\) contains precisely those points whose coordinates strictly between \(-1\) and \(1\) form a face of \(P_n\). The involution is \(\rho(x_1,\ldots,x_n)=(x_n,\ldots,x_1)\). Quotient means the ordinary topological orbit space, not a homotopy quotient; nonorientable genus means the number of real projective-plane summands in the compact-surface classification. All statements concern the actual continuous cubical spaces and all integers \(n\ge3\).

## Proof
**1. The covering surface.** The natural CW structure has \(2^n\) vertices, \(n2^{n-1}\) edges, and \((n-1)2^{n-2}\) squares. Every internal edge varying coordinate \(i\), for \(2\le i\le n-1\), belongs to two squares (involving coordinates \(i-1,i\) and \(i,i+1\)); each end-coordinate edge belongs to one square. Links at vertices are copies of the path \(P_n\), so each vertex has a half-disk neighborhood. The end-coordinate edges assemble into \(2^{n-2}\) boundary circles; each is the four-edge loop obtained by varying \(x_1,x_n\) while fixing the signs of \(x_2,\ldots,x_{n-1}\). The whole space is connected because it contains the full one-skeleton of the \(n\)-cube.

The surface is orientable: give the square varying \((x_i,x_{i+1})\), with all other coordinates fixed at signs \(s_j\), the orientation \((\prod_{j\notin\{i,i+1\}}s_j)\,dx_i\wedge dx_{i+1}\). At an internal edge, the two induced orientations are opposite, since the sign products differ exactly by the two fixed neighboring signs. Its Euler characteristic is
\[
 \chi(R_n)=2^n-n2^{n-1}+(n-1)2^{n-2}=-(n-3)2^{n-2}.
\]
Coordinate reversal sends each oriented square to a square with the same external-sign product but exchanges the two variable axes, hence **reverses** this global orientation.

**2. Fixed arcs and the local quotient.** If \(n=2m+1\), a fixed point has \(x_i=x_{2m+2-i}\). Each mirrored pair lies at nonadjacent vertices of \(P_n\) and therefore must be fixed at a common sign. The central coordinate alone varies freely. Thus the fixed set is \(2^m\) disjoint complete intervals. If \(n=2m\), all \(m-1\) outer mirrored pairs similarly have common endpoint signs and the two central coordinates can vary together along the diagonal of their square. This gives \(2^{m-1}\) disjoint complete intervals. In both cases write \(k_n=2^{\lfloor(n-1)/2\rfloor}\) for the number of arcs.

Each such interval meets the original boundary precisely at its two endpoints, each on a different boundary circle. In a neighborhood of an interior fixed point, reflection interchanges the two sides of a coordinate edge (odd case) or the two half-squares separated by a diagonal (even case). Consequently the quotient is a surface with boundary, with the images of the fixed arcs included in that boundary. The quotient is connected as a continuous image of the connected surface \(R_n\).

**3. Boundary-circle accounting.** The original boundary circles are indexed by the \(n-2\) endpoint-sign strings \((s_2,\ldots,s_{n-1})\); reflection reverses these strings. Exactly \(k_n\) such strings are palindromic. A nonpalindromic pair of original boundary circles gives one quotient boundary circle, contributing \((2^{n-2}-k_n)/2\). On each palindromic original circle, reflection swaps \(x_1,x_n\); its quotient is an interval whose two endpoints are the palindromic all-end-sign vertices. The \(k_n\) fixed arcs join those endpoints in \(k_n/2\) pairs of palindromic boundary intervals; each pair of intervals is joined by exactly two arcs, making a single quotient boundary circle. This pairing is explicit: fix all outer mirrored signs and change the central free sign (odd case), or change both equal central signs (even case). Hence
\[
 b(Q_n)=\frac{2^{n-2}-k_n}{2}+\frac{k_n}{2}=2^{n-3}.
\]

**4. Euler characteristic.** Equivariantly triangulate the squares, subdividing any fixed diagonal when necessary. The standard cell-orbit count for an involution gives \(\chi(Q_n)=[\chi(R_n)+\chi(\operatorname{Fix}(\rho))]/2\). Each fixed arc is contractible, so \(\chi(\operatorname{Fix}(\rho))=k_n\). Therefore
\[
 \chi(Q_n)=-(n-3)2^{n-3}+2^{\lfloor(n-1)/2\rfloor-1}.
\]

**5. Orientability of the quotient.** The off-diagonal cube vertices (sign words not equal to their reversals) are connected by cube edges when \(n\ge4\). Indeed, there are at least two mirrored coordinate pairs. Keep one mismatched pair as a buffer while altering another pair; then use the latter as buffer to change the first. This connects any two nonpalindromic sign words without passing through a palindromic word. Every point of \(R_n\setminus\operatorname{Fix}(\rho)\) joins such an off-diagonal cube vertex without meeting the fixed set: in each cubical cell, the complement of any fixed diagonal or fixed coordinate edge has components meeting off-diagonal corners. Hence \(R_n\setminus\operatorname{Fix}(\rho)\) is connected for \(n\ge4\). Since \(\rho\) reverses orientation on this connected double covering of the quotient's interior, the quotient cannot be orientable. For \(n=3\), the off-fixed set has two components, and the quotient has \(\chi=1\) and one boundary circle, hence is a disk.

By classification of connected compact surfaces, for \(n\ge4\) the crosscap number is \(h_n=2-\chi(Q_n)-b(Q_n)\), precisely the stated formula. A connected surface with nonempty boundary deformation retracts to a wedge of \(h_n+b_n-1\) circles. This proves the integral homology and fundamental-group consequences. No unproved extension to other graph shapes or higher-dimensional polyhedral products is asserted.

## Verification
The included standalone Python program `verify_path_angle.py` enumerates exact cubical cell counts and all sign vertices, checks each boundary-circle reversal orbit, explicitly pairs fixed arcs and checks the two-arc boundary gluing, computes the Lefschetz Euler trace from signed fixed cells, and tests connected components of the nonfixed cube-vertex graph. It independently compares both Euler-characteristic calculations and the genus and boundary formulas for every \(3\le n\le11\), returning `VERIFY_OK`. Those finite tests are cross-checks; the proof above establishes the claims for every integer in the stated range.

## Relationship to prior work
The real moment-angle polyhedral-product construction is classical; see Bahri–Bendersky–Cohen–Gitler (2010). The general Euler-characteristic formula is due to Davis (2011). Zhu (2018), Theorem 2.2, gives a general fixed-point formula for coordinate-permutation actions on polyhedral products; our fixed-point count is compatible with it, but fixed points alone do not determine the quotient boundary or orientability. Amelotte (2020), Example 4.1, cites the closed-polygon moment-angle surface genus and notes that deleting a vertex gives a path whose real moment-angle complex is homotopy equivalent to a wedge of circles. These results do not themselves provide the **homeomorphism classification** of the reversal quotient of the **path** surface, including its nonorientable genus and boundary count. Previous dihedral computations for **closed cycle** polyhedral products concern different spaces and different group quotients; their conclusions are not transferred as if they were path-quotient theorems.

## Limitations
The result concerns only graph paths and the single coordinate-reversal involution. No homeomorphism type is claimed for other graph quotients. Although the inspected sources and research records do not exhibit an equivalent classification, exhaustive publication-priority verification is not possible; the elementary nature of some ingredients leaves a risk of an unindexed equivalent result. Verification code covers finitely many lengths, while the all-length assertion relies on the explicit topological argument.

## References
1. A. Bahri, M. Bendersky, F. R. Cohen and S. Gitler, *Operations on polyhedral products and a new topological construction of infinite families of toric manifolds*, arXiv:1011.0094, originally submitted 2010-10-30; https://arxiv.org/abs/1011.0094.
2. M. W. Davis, *The Euler characteristic of a polyhedral product*, arXiv:1103.3034, originally submitted 2011-03-15; https://arxiv.org/abs/1103.3034.
3. Q. Zhu, *Bredon Cohomology of Polyhedral Products*, arXiv:1811.07076, especially Section 2 and Theorem 2.2; https://arxiv.org/html/1811.07076v1.
4. S. Amelotte, *Connected sums of sphere products and minimally non-Golod complexes*, arXiv:2006.16320, Example 4.1; https://arxiv.org/abs/2006.16320.
