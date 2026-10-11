# Sharp one-core eight-subdivision threshold for the unit disk
## Finding
Let \(B=\{x\in\mathbb R^2:\lVert x\rVert_2\le 1\}\). An eight-subdivision of \(B\) means eight connected subsets \(C_0,\ldots,C_7\) whose union is \(B\) and whose interiors are pairwise disjoint; no equal-area condition is imposed. Put
\[
d_M(\mathcal S)=\max_{0\le i\le7}\operatorname{diam}(C_i),
\qquad
\operatorname{diam}(C_i)=\sup\{\lVert x-y\rVert_2:x,y\in C_i\}.
\]
Among all such eight-subdivisions for which at least one region is disjoint from the outer circle \(\partial B\), the exact minimum is
\[
\inf d_M(\mathcal S)=2\sin\!\left(\frac{\pi}{7}\right).
\]
The infimum is attained. One optimizer consists of the centered disk of radius \(s=\sin(\pi/7)\) and seven congruent annular radial sectors, each of angular width \(2\pi/7\). Moreover, if equality holds, exactly seven regions meet \(\partial B\); up to shared endpoints, their traces on \(\partial B\) are seven consecutive arcs of angular length \(2\pi/7\).

## Assumptions and scope
The notion of subdivision is the connected-set notion used by Cañete, Schnell, and Segura Gomis: the pieces cover the body and have pairwise disjoint interiors, but need not have equal areas. The theorem concerns the natural one-core topological stratum in which at least one piece misses the outer boundary. It does not determine the unrestricted optimum among all eight-subdivisions of the disk.

The use of supremum in the diameter definition makes the statement insensitive to endpoint conventions on interfaces. The explicit optimizer can be taken with all pieces compact, so its diameters are attained.

## Proof
Set
\[
\alpha=\frac{2\pi}{7},\qquad d_0=2\sin\!\left(\frac{\alpha}{2}\right)=2\sin\!\left(\frac{\pi}{7}\right).
\]
First consider any subset \(A\subset\partial B\) with Euclidean diameter at most \(d_0\). The chord joining two unit-circle points with circular separation \(\delta\in[0,\pi]\) has length \(2\sin(\delta/2)\), which is strictly increasing in \(\delta\). Hence every two points of \(A\) have circular separation at most \(\alpha\).

Choose one point of \(A\) as angular origin and represent every other point by its principal signed angle in \([ -\alpha,\alpha]\). If the largest and smallest such angles had difference greater than \(\alpha\), that difference would be at most \(2\alpha=4\pi/7<\pi\), so those two extreme points would have circular separation greater than \(\alpha\), a contradiction. Therefore \(A\) is contained in a closed circular arc of angular length at most \(\alpha\). If the Euclidean diameter of \(A\) is strictly less than \(d_0\), the containing arc can be chosen with length strictly less than \(\alpha\).

Now let \(\mathcal S=\{C_0,\ldots,C_7\}\) be an eight-subdivision and suppose, after relabeling, that \(C_0\cap\partial B=\varnothing\). The seven traces \(C_i\cap\partial B\), \(1\le i\le7\), cover the whole outer circle. If \(d_M(\mathcal S)<d_0\), each trace is contained in an arc of length strictly less than \(\alpha\). Seven such arcs have total angular length strictly less than \(7\alpha=2\pi\), so they cannot cover \(\partial B\). Thus every admissible subdivision satisfies \(d_M(\mathcal S)\ge d_0\).

It remains to attain this bound. Put \(s=\sin(\pi/7)\). Take the core
\[
C_0=\{x:\lVert x\rVert_2\le s\},
\]
and divide the annulus \(s\le\lVert x\rVert_2\le1\) into seven closed radial sectors of angular width \(\alpha\), with the usual harmless sharing of interfaces. The core has diameter \(2s=d_0\).

For two points in one annular sector, let their radii be \(r,t\in[s,1]\) and their angular separation be \(\delta\in[0,\alpha]\). Their squared distance is
\[
r^2+t^2-2rt\cos\delta.
\]
It increases with \(\delta\), and for fixed \(\delta\) it is a convex function of each radial variable. Consequently a maximum occurs at \(\delta=\alpha\) and at a corner of the square \([s,1]^2\). The three corner types give
\[
4s^2,\qquad 4s^4,\qquad 1+s^2-2s\cos\!\left(\frac{2\pi}{7}\right).
\]
The first equals \(d_0^2\), and the second is smaller. For the mixed corner, using \(\cos(2x)=1-2\sin^2x\),
\[
1+s^2-2s\cos\!\left(\frac{2\pi}{7}\right)-4s^2
=(s-1)(4s^2+s-1).
\]
The alternating Taylor bound gives \(\sin x>x-x^3/6\) for \(x>0\). Since \(\pi>3\),
\[
s=\sin\!\left(\frac{\pi}{7}\right)>
\frac37-\frac{(3/7)^3}{6}=\frac{285}{686}>\frac25,
\]
so \(4s^2+s-1>1/25>0\). Because \(s<1\), the mixed corner is also strictly below \(4s^2\). Therefore every outer sector has diameter exactly \(2s=d_0\), and the constructed subdivision has \(d_M=d_0\).

Finally suppose equality holds in an arbitrary admissible subdivision. Every boundary trace is contained in an arc of angular length at most \(\alpha\). Fewer than seven nonempty traces cannot cover the circle, while seven such arcs can cover it only if all have length exactly \(\alpha\) and their interiors are disjoint. Hence equality forces exactly seven boundary-touching regions, and their traces fill seven consecutive arcs of angle \(2\pi/7\), up to the assignment of shared endpoints.

## Verification
The proof is analytic and uses no finite search as a substitute for an infinite argument. The lower bound depends only on the metric geometry of the outer circle and therefore applies to every connected subdivision in the stated topological class, regardless of the shapes of the interfaces. The construction is checked by an exact maximization of the squared distance over one annular sector.

As a numerical sanity check only,
\[
2\sin\!\left(\frac{\pi}{7}\right)\approx0.8677674782<1.
\]
Thus the exact one-core optimum lies below the standard eight-partition value \(1\) for the unit disk, while remaining strictly positive and geometrically forced by the seven boundary-touching pieces.

## Relationship to prior work
Cañete, Schnell, and Segura Gomis introduced the subdivision framework and maximum-relative-diameter functional used here. Their general theorem proves optimality of the standard partition among arbitrary subdivisions only for \(k\le6\). For \(k=8\), their Example 4.8 exhibits precisely the relevant qualitative topology: an inner region bounded away from the outer circle and seven congruent outer regions, and uses it to show that the standard eight-partition of the disk is not minimizing. The source gives a numerical benchmark for that displayed construction but does not state a sharp lower bound over all one-core eight-subdivisions or the boundary equality structure proved above.

The later paper on multi-rotationally symmetric bodies studies the values of standard \(k\)-partitions across different rotational symmetries. It does not supply a general-subdivision theorem for this one-core eight-piece disk problem.

## Limitations
The theorem does not determine the unrestricted minimum over all eight-subdivisions of the unit disk; an optimizer with all eight regions meeting the outer circle could in principle do better. It also does not classify the interior interfaces of all equality cases. The equality statement proved here concerns the number and angular arrangement of boundary traces.

No claim is made about the exact geometry of the particular drawn subdivision in the earlier paper beyond the topological feature explicitly used here.

## References
A. Cañete, U. Schnell, S. Segura Gomis, “Subdivisions of rotationally symmetric planar convex bodies minimizing the maximum relative diameter,” arXiv:1501.03907v1, first posted 2015-01-16; Journal of Mathematical Analysis and Applications 435 (2016), 718–734, doi:10.1016/j.jmaa.2015.10.053.

A. Cañete, “The maximum relative diameter for multi-rotationally symmetric planar convex bodies,” Mathematical Inequalities & Applications 19 (2016), 335–347, doi:10.7153/mia-19-25.
