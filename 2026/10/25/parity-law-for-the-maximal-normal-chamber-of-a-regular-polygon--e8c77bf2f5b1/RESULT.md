# Parity law for the maximal-normal chamber of a regular polygon

## Finding

Let \(n\ge5\), let \(P_n\) be a regular Euclidean \(n\)-gon of circumradius \(R>0\), and number its edges cyclically as \(E_0,\ldots,E_{n-1}\). Write \(t_j\) for either unit tangent to the line containing \(E_j\). For an interior point \(y\), count a normal by its distinct boundary base point, as in the polyhedral normal convention of the references.

The closure of the locus of points from which all \(2n\) faces give distinct normals is

\[
S_n=\bigcap_{j=0}^{n-1}\{y\in\mathbb R^2:|\langle y,t_j\rangle|\le R\sin(\pi/n)\}\subset P_n.
\]

Its shape depends on parity: \(S_n\) is a regular \(2n\)-gon for odd \(n\), and a regular \(n\)-gon for even \(n\). The exact area fraction is

\[
\frac{\operatorname{area}(S_n)}{\operatorname{area}(P_n)}=
\begin{cases}
2\tan\!\left(\frac{\pi}{n}\right)\tan\!\left(\frac{\pi}{2n}\right),&n\text{ odd},\\[3pt]
\tan^2\!\left(\frac{\pi}{n}\right),&n\text{ even}.
\end{cases}
\]

In both parity classes the leading term is \(\pi^2/n^2\), but the next term distinguishes them:

\[
\frac{\operatorname{area}(S_n)}{\operatorname{area}(P_n)}=
\begin{cases}
\dfrac{\pi^2}{n^2}+\dfrac{5\pi^4}{12n^4}+O(n^{-6}),&n\text{ odd},\\[5pt]
\dfrac{\pi^2}{n^2}+\dfrac{2\pi^4}{3n^4}+O(n^{-6}),&n\text{ even}.
\end{cases}
\]

Thus the maximal-normal locus has a parity-dependent polygonal shape and an exact relative area; its area shrinks quadratically while the fourth-order correction records parity.

## Assumptions and scope

The metric is Euclidean. A normal from an interior point \(y\) to a boundary point \(z\) is the segment \([y,z]\) perpendicular to a supporting line of the polygon at \(z\); distinct normals are counted by distinct bases \(z\). Each edge contributes at most one normal, at its orthogonal projection, and each vertex contributes at most one. The maximum count is therefore at most \(2n\).

The result is for regular polygons with \(n\ge5\). The parity condition determines how many strip directions remain distinct modulo sign. The containment argument excludes the triangle and square cases. No claim is made about the full distribution of smaller normal counts or about nonregular polygons.

## Proof

Set \(x=\pi/n\) and \(s=R\sin x\). The midpoint of edge \(E_j\) lies on the radius in its outward normal direction, and the two endpoints have tangent coordinates \(-s\) and \(s\) relative to that midpoint. Orthogonal projection of \(y\) onto the line containing \(E_j\) consequently falls in the edge segment exactly when

\[
|\langle y,t_j\rangle|\le s.
\]

If all these inequalities are strict, each edge contains an interior critical point of the squared distance to \(y\), a strict local minimum along the boundary. At each vertex, the squared distance decreases along both incident edges as one leaves the vertex; hence every vertex is a strict local maximum and the segment from \(y\) to that vertex lies in its normal cone. There are therefore \(n\) edge-based and \(n\) vertex-based normals, with distinct bases, giving exactly \(2n\). Conversely, attaining \(2n\) distinct face-based normals requires a normal from every edge, so all the strip inequalities must hold. The maximal-count locus thus differs from \(S_n\) only by its boundary, a set of area zero.

The outward normals of the strips are \(\pm t_j\). Their directions modulo sign are equally spaced. If \(n\) is odd, all \(n\) directions are distinct modulo sign, giving a regular \(2n\)-gon with inradius \(s\) and circumradius

\[
\rho_n^{\mathrm{odd}}=\frac{R\sin x}{\cos(x/2)}.
\]

For \(0<x\le\pi/5\), monotonicity and \(\tan(\pi/5)<\cos(\pi/10)\) give \(\tan x\le\cos(x/2)\), hence \(\rho_n^{\mathrm{odd}}\le R\cos x\). The inscribed disk of \(P_n\) has radius \(R\cos x\), so \(S_n\subset P_n\).

If \(n\) is even, opposite edge tangents give the same strip modulo sign, leaving \(n/2\) distinct directions and a regular \(n\)-gon with inradius \(s\) and circumradius

\[
\rho_n^{\mathrm{even}}=\frac{R\sin x}{\cos x}=R\tan x.
\]

For even \(n\ge6\), \(0<x\le\pi/6\) and \(\tan x\le\cos x\), so \(\rho_n^{\mathrm{even}}\le R\cos x\). This again puts \(S_n\) inside the inscribed disk of \(P_n\).

A regular \(2n\)-gon with inradius \(s\) has area \(2ns^2\tan(x/2)\). A regular \(n\)-gon with inradius \(s\) has area \(ns^2\tan x\). Meanwhile \(\operatorname{area}(P_n)=nR^2\sin x\cos x\). Division gives the odd ratio \(2\tan x\tan(x/2)\) and the even ratio \(\tan^2x\). Taylor expansion gives \(\tan x\tan(x/2)\cdot2=x^2+5x^4/12+O(x^6)\) and \(\tan^2x=x^2+2x^4/3+O(x^6)\), proving both asymptotic branches. The argument covers every integer \(n\ge5\), not just sampled dimensions.

## Verification

The proof reduces the normal-count statement to exact orthogonal-projection inequalities, then to the geometry and area of a regular polygon whose side count is determined by parity. The strict strip interior realizes the face-count maximum \(2n\); conversely, realizing that maximum forces every edge projection to lie in its segment. The containment inequalities are established on the full intervals \(0<x\le\pi/5\) for odd \(n\) and \(0<x\le\pi/6\) for even \(n\ge6\).

As supplementary arithmetic checks, the exact area formulas and the strip-polygon area formulas agree for \(n=5,6,7,8,9,10,11,21\). These finite checks are sanity checks only; the analytic argument proves the infinite family. The chamber boundary has area zero, so its inclusion does not change the area fraction. Independent validation has not been performed.

## Relationship to prior work

The study of normals through interior points is established, and the cited polyhedral work develops face-based normal counting, active regions, and bounds by the number of faces. The present result computes the exact geometry and area of the maximal-count locus for every regular polygon with at least five sides, including its parity split; it does not introduce a new definition of a normal or a general theorem about convex polytopes.

The result is distinct from average normal count: the latter integrates the count over all interior points, whereas this formula measures the intersection of all edge-projection strips. A separate exact area invariant for regular polygons, the Estermann measure, concerns a different region and does not determine this chamber area.

## Limitations

The formula does not classify the regions with fewer than \(2n\) normals, and it does not establish a general concentration law for arbitrary convex polygons. The literature comparison was bounded rather than exhaustive; an unlocated prior computation of this particular chamber area remains possible. The result is an exact geometric derivation, not an independent expert certification.

## References

1. I. Nasonov, G. Panina, and D. Siersma, “Concurrent normals problem for convex polytopes and Euclidean distance degree,” arXiv:2406.01773, first publicly posted 3 June 2024; published in *Acta Mathematica Hungarica* 174 (2024), 522–538. https://arxiv.org/abs/2406.01773 ; https://doi.org/10.1007/s10474-024-01483-2
2. G. Domokos and Z. Lángi, “On the average number of normals through points of a convex body,” arXiv:1406.0813. https://arxiv.org/abs/1406.0813
