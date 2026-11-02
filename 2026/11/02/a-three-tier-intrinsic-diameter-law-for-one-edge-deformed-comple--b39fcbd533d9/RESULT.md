# A three-tier intrinsic diameter law for one-edge-deformed complete networks

## Finding

Let \(n\ge3\) be an integer. Form a compact metric graph \(G_{n,\lambda}\) by realizing every edge of the complete graph \(K_n\) as an interval, assigning length \(\lambda>0\) to one distinguished edge \(ab\), and length \(1\) to every other edge. Distances are intrinsic shortest-path lengths between **any** points on the edges, not merely vertices. Define the continuous diameter \(D_n(\lambda)=\max_{p,q\in G_{n,\lambda}}d(p,q)\). Then, for every positive real \(\lambda\),

\[
D_n(\lambda)=
\begin{cases}
(\lambda+2)/2,& n=3,\\
(\lambda+3)/2,& n=4,\\
\max\{2,(\lambda+3)/2\},& n\ge5.
\end{cases}
\]

For \(n\ge4\), the two midpoints of the distinguished edge and any edge disjoint from it form a diametral pair whenever \(\lambda\ge1\). For \(n=4\), they are diametral for **every** \(\lambda>0\). If \(n\ge5\) and \(0<\lambda\le1\), midpoints of any two disjoint unit edges whose four cross-endpoint vertex distances equal \(1\) form a diametral pair; such edges always exist.

Let \(m=\binom n2\) and \(L=m-1+\lambda\), the graph's total length. The scale-invariant diameter ratio \(R_n(\lambda)=D_n(\lambda)/L\) satisfies:

* For \(n=3\), \(R_3(\lambda)=1/2\) identically.
* For \(n=4\), \(R_4(\lambda)=(\lambda+3)/(2(\lambda+5))\) is strictly increasing, with unattained infimum \(3/10\) as \(\lambda\downarrow0\). The equilateral point has ratio \(1/3\), not the minimum.
* For every \(n\ge5\), \(R_n(\lambda)\ge 2/m\), with equality **if and only if** \(\lambda=1\). This is a unique minimizer within the precisely specified one-edge-deformed family, up to overall scaling and choice of exceptional edge.

Thus the length-normalized optimization changes qualitatively at four and five vertices, while at three vertices it is completely insensitive to the exceptional length.

## Assumptions and scope

All edge lengths are strictly positive and edges are considered as abstract intervals meeting only at their designated vertices; a planar embedding and shortcut connections at drawings' crossings are neither assumed nor permitted. The vertex count \(n\) ranges over all integers at least \(3\), while \(\lambda\) ranges over all positive real numbers, even \(\lambda>2\) when the direct distinguished edge no longer realizes the shortest vertex-to-vertex path. An optimization over **all** edge weights is not claimed: all nondistinguished lengths must be equal.

## Proof

**Vertex distances.** For \(n\ge3\), the shortest vertex distance between \(a,b\) is \(\min\{\lambda,2\}\), using either the distinguished edge or two unit edges via a third vertex. Every other pair of distinct vertices has shortest distance \(1\). An alternative path between such vertices must traverse at least one unit edge and therefore cannot improve their direct length. For points on distinct edges \(e=[u,v]\) and \(f=[s,t]\), the distance is the minimum over the four choices of exit endpoint on \(e\) and entry endpoint on \(f\), of the corresponding two edge-subinterval lengths plus the shortest vertex distance between those endpoints. This exact formula permits the following exhaustive cases.

**The triangle.** For \(n=3\) the realization is a circle of circumference \(\lambda+2\); its geodesic diameter is half its circumference.

**The distinguished edge versus a disjoint edge.** Assume \(n\ge4\), write \(e=ab\) with coordinate \(x\in[0,\lambda]\) from \(a\), and take any disjoint unit edge \(f=cd\) with coordinate \(y\in[0,1]\) from \(c\). Every cross-endpoint vertex distance is exactly \(1\), so

\[
d(x,y)=\min\{x,\lambda-x\}+1+\min\{y,1-y\}.
\]

Its maximum is \((\lambda+3)/2\), achieved exactly at the two midpoints. This proves the principal lower bound for all \(n\ge4\).

**Remaining pair types.** Two points on \(ab\) at direct separation \(z\in[0,\lambda]\) can travel either along their subinterval of length \(z\), or around the other side through a two-unit-edge \(a\)-to-\(b\) detour. Thus their distance is at most \(\min\{z,\lambda-z+2\}\le(\lambda+2)/2\). Two points on the same unit edge are at distance at most \(1\). For a point on \(ab\) and one on an incident unit edge \(ac\), if \(x\) and \(y\) denote their respective distances from \(a\), the two explicit routes through \(a\), or through \(b\) then \(bc\), give

\[
d(x,y)\le\min\{x+y,\lambda+2-x-y\}\le(\lambda+2)/2.
\]

For two distinct incident unit edges, let \(u,v\in[0,1]\) be the distances from their shared vertex. The common-vertex route has length \(u+v\). The route using the other two endpoints has length \(2-u-v+s\), where \(s\) is the shortest distance between the free endpoints. If these endpoints are not the pair \(a,b\), then \(s=1\), and the displayed minimum is at most \(3/2\). Otherwise \(s=\min\{\lambda,2\}\), and that minimum is at most \(1+s/2\le2\). In particular, for \(0<\lambda\le1\), every incident normal-edge pair has distance at most \(1+\lambda/2\) or \(3/2\).

For two **disjoint** unit edges, the four cross-endpoint pairs include at most one pair \(a,b\). Thus there is a perfect matching between their endpoint sets using two unit-distance cross-pairs. The two resulting routes have total length \(4\) for any positions of the points, so the distance is at most \(2\). If \(n=4\) and \(0<\lambda\le1\), every such pair of unit edges has the form \(ac\) versus \(bd\), or \(ad\) versus \(bc\): the cross-pairs \(a,b\) and \(c,d\) give two routes whose total length is \(\lambda+3\), proving the sharper bound \((\lambda+3)/2\).

**Completion for four vertices.** If \(n=4\) and \(0<\lambda\le1\), the preceding bounds for every pair type are at most \((\lambda+3)/2\). If \(n=4\) and \(\lambda\ge1\), all pairs of unit edges are at distance at most \(2\le(\lambda+3)/2\); every other case has the smaller stated bound. The distinguished/disjoint midpoint pair attains \((\lambda+3)/2\) throughout.

**Completion for at least five vertices.** All the case bounds give \(D_n(\lambda)\le\max\{2,(\lambda+3)/2\}\). If \(\lambda\ge1\), the distinguished/disjoint midpoint pair realizes the larger term. If \(0<\lambda\le1\), select five distinct vertices \(a,b,c,d,e\), and take the midpoints of unit edges \(ac\) and \(de\). All four vertex distances between an endpoint of \(ac\) and an endpoint of \(de\) equal \(1\), giving midpoint distance exactly \(2\). Both regimes meet at \(\lambda=1\), proving the complete diameter formula.

**Sharp normalized optimization.** When \(n=4\), differentiate \((\lambda+3)/(2(\lambda+5))\) to obtain \(1/(\lambda+5)^2>0\), including the stated nonattained infimum. For \(n\ge5\), \(m\ge10\). On \(0<\lambda\le1\) we have \(R_n(\lambda)=2/(m-1+\lambda)\), strictly decreasing. On \(\lambda\ge1\), we have \(R_n(\lambda)=(\lambda+3)/(2(m-1+\lambda))\), whose derivative is \((m-4)/(2(m-1+\lambda)^2)>0\). Their unique meeting point \(\lambda=1\) is therefore the unique global minimizer, with value \(2/m\). For \(n=3\), the circle diameter divided by its circumference is \(1/2\) for all \(\lambda\). This finishes the proof.

## Verification

The companion `CHECK.py` uses only the Python standard library and exact rational arithmetic. For each pair of distinct edges it computes the maximum of the minimum of four affine route lengths over an edge-position rectangle. It enumerates intersections of pairwise route-equality lines and the rectangle boundaries; a piecewise-affine concave lower envelope attains its maximum at one of these subdivision vertices. Same-edge distances are checked separately. The script confirms the formula for \(n=3,4,5,6\) and seven rational values of \(\lambda\), giving \(28\) complete edge-pair cases; it also checks \(320\) rational normalized-diameter inequalities. Executed command: `python3 CHECK.py` (pass). These finite exact computations test, but do not replace, the quantified proof above.

## Relationship to prior work

The intrinsic notion of continuous network distance and farthest-point eccentricity is developed in Bose et al., *Network Farthest-Point Diagrams* (first arXiv version 2013-04-06). Their work gives generic eccentricity-diagram methods, rather than the present all-size one-edge-deformed complete-graph formulas or sharp normalization classification. De Carufel et al.'s *Minimizing the Continuous Diameter when Augmenting Paths and Cycles with Shortcuts* (first arXiv version 2015-12-07) concerns optimization by adding new shortcuts to paths/cycles rather than varying one existing edge of a complete network. Ahn et al.'s *Diameter and Length of Metric Graphs* (first arXiv version 2026-08-09) gives universal length-diameter inequalities in terms of cyclomatic number and leaves, plus equality characterizations; those inequalities are strictly weaker for this family and do not yield the present transition.

A 1982 article by Chen and Garfinkel, *The generalized diameter of a graph*, develops a generic method for the continuous diameter of weighted networks, but its full primary text was not accessible in this examination. The proposed one-parameter theorem is not asserted to be logically independent of that classical method: its claim is an explicit sharp shape-and-size classification not identified in the materially inspected sources. Priority with respect to inaccessible historical literature remains uncertain.

## Limitations

The claimed optimum is only among complete networks having all but one edge of equal length; it says nothing about global optimization over all edge assignments, other network topologies, or discrete diameter measured only at vertices. The edge geometry is abstract, not Euclidean-embedded. The conclusions require strictly positive lengths: the four-vertex infimum at \(\lambda=0\) is a degeneration and not attained by a graph in the stated family. Independent validation and a historical-priority determination have not been performed.

## References

1. P. Bose, K. Dannies, J.-L. De Carufel, C. Doell, C. Grimm, A. Maheshwari, S. Schirra, and M. Smid, *Network Farthest-Point Diagrams*, arXiv:1304.1909, originally posted 2013-04-06. https://arxiv.org/abs/1304.1909
2. J.-L. De Carufel, C. Grimm, A. Maheshwari, and M. Smid, *Minimizing the Continuous Diameter when Augmenting Paths and Cycles with Shortcuts*, arXiv:1512.02257, originally posted 2015-12-07; SWAT 2016, DOI 10.4230/LIPIcs.SWAT.2016.27. https://arxiv.org/abs/1512.02257
3. H.-K. Ahn, S. Cabello, O. Cheong, D. Garijo, and J. Moon, *Diameter and Length of Metric Graphs*, arXiv:2608.08716, posted 2026-08-09. https://arxiv.org/abs/2608.08716
4. C. E. Chen and R. S. Garfinkel, *The generalized diameter of a graph*, Networks 12 (1982), 335–340, DOI 10.1002/net.3230120310 (historical context; full text not inspected).
