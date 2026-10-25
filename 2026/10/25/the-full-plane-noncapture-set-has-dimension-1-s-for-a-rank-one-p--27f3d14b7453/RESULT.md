# The full-plane noncapture set has dimension \(1+s\) for a rank-one planar map

## Finding
Consider the continuous planar map
\[
F(x,y)=(|x|-y-1,\ x-|y|-13/16).
\]
Let \(\mathcal P\) be its least-period-six orbit starting at \((-11/16,-1/2)\), explicitly
\[
(-11/16,-1/2)\mapsto(3/16,-2)\mapsto(19/16,-21/8)
\mapsto(45/16,-9/4)\mapsto(65/16,-1/4)
\mapsto(53/16,3)\mapsto(-11/16,-1/2).
\]
Define the **finite-time noncapture set**
\[
E=\{z\in\mathbb R^2:F^n(z)\notin\mathcal P\text{ for every integer }n\ge0\}.
\]
Then
\[
\boxed{\dim_{\mathrm H}(E)=1+s,\qquad
16^{-s}+8^{-s}=1,\quad 0<s<1.}
\]
Numerically \(s=0.28776078708402886\ldots\); thus \(\dim_{\mathrm H}(E)=1.2877607870840289\ldots\), and \(E\) has zero planar Lebesgue measure. For the compact polygonal invariant graph \(\Gamma\) described in [1], with the possible isolated fixed point adjoined, one also has \(\dim_{\mathrm H}(E\cap\Gamma)=s\). This distinguishes the one-dimensional recurrent exceptional geometry from its two-dimensional basin complement. The statement concerns **exact eventual landing** in the six-cycle, not asymptotic convergence to it.

## Assumptions and scope
All points in \(\mathbb R^2\), including quadrant boundaries, are allowed. The absolute-value map is continuous. Hausdorff dimension uses the Euclidean metric. The parameter value \((-1,-13/16)\) is the endpoint of the positive-entropy interval treated in Proposition 27 of [1], where the sixth return has exactly two full affine branches. The graph-entry and connected-graph visitation assertions from Theorem B and Proposition 27(d) of [1] are invoked as published premises. One isolated fixed point \(p=(13/16,-1)\), not in the chaotic segment, must be treated separately.

## Proof
**1. The exact return and its exceptional Cantor set.** Define the invariant line segment
\[
\Pi=\{(u,u+3/16):-11/16\le u\le13/16\}\subset\Gamma.
\]
The sixth return on \(\Pi\), either by direct composition or by specializing formula (22) in the proof of Proposition 27(d) of [1], is \(F^6(u,u+3/16)=(G(u),G(u)+3/16)\), with
\[
G(u)=\begin{cases}
16u+165/16,&-11/16\le u\le-19/32,\\
13/16,&-19/32\le u\le-3/16,\\
-8u-11/16,&-3/16\le u\le0,\\
-11/16,&0\le u\le13/16.
\end{cases}
\]
Let \(I=[-11/16,13/16]\), \(I_L=[-11/16,-19/32]\), and \(I_R=[-3/16,0]\). Each of \(G|_{I_L}\) and \(G|_{I_R}\) maps its source interval *bijectively onto* \(I\); their inverses are similarities of contraction ratios \(1/16\) and \(1/8\) and have disjoint images. Both complementary plateau intervals map to endpoints of \(I\), which map to the fixed endpoint \(-11/16\) in at most one additional sixth-return step. Therefore the infinite branch-survivor
\[
K=\bigcap_{n\ge0}G^{-n}(I_L\cup I_R)
\]
is the self-similar attractor of these two inverse similarities. The open-set condition (indeed, strong separation) holds; its Hausdorff dimension and upper Minkowski dimension are the unique \(s\in(0,1)\) satisfying \(16^{-s}+8^{-s}=1\). The only points of \(K\) whose orbit eventually lands at the six-cycle are contained in the countable backward orbit of the endpoint \(-11/16\). Removing those points does not change Hausdorff dimension. Hence \(\dim_{\mathrm H}(E\cap\Pi)=s\).

**2. Exceptional dimension on the whole published graph.** By the finite-entry/visitation results of [1, Theorem B and Proposition 27(d)], all points in the connected invariant polygonal graph, except the six-cycle \(\mathcal P\) itself, eventually enter \(\Pi\). The exception described in Proposition 27(d) is the same six-cycle: at this parameter its distinguished repelling point is \((-11/16,-1/2)\). The separate fixed point \(p\) is an isolated additional exception. The connected graph is a finite union of affine edges, and the restrictions of \(F^n\) to finitely many subedges are affine. Any constant subedge maps through one of the graph's two plateau branches; Proposition 27(c) of [1] shows that both plateau images eventually reach the orbit of \(P_2=(-19/16,-1)\), and direct iteration gives \(F^5(P_2)=(-11/16,-1/2)\in\mathcal P\). Thus constant subedges contain no points of \(E\). On nonconstant subedges the restriction of \(F^n\) is bi-Lipschitz onto its image and inverse images of \(E\cap\Pi\) have dimension at most \(s\). A countable union over \(n\), finitely many edges, and finitely many affine pieces gives \(\dim_{\mathrm H}(E\cap\Gamma)\le s\). The reverse inequality follows from \(\Pi\subset\Gamma\). The isolated fixed point contributes dimension zero. Accordingly \(\dim_{\mathrm H}(E\cap\Gamma)=s\).

**3. Why constant planar itinerary regions cannot be exceptional.** Write \(X=16x\), \(Y=16y\); on this integer-affine scale the map is
\[
T(X,Y)=(|X|-Y-16,\ X-|Y|-13).
\]
In each open quadrant the derivative has rank one in the first and third quadrants, and is invertible in the second and fourth. Consider any open polyhedral itinerary cell on which some \(F^n\) has rank zero. Choose its *first* such iterate. Its last step must be a singular rank-one quadrant, so the now constant image \(c\) belongs to the singular image line \(Y-X=3\) (first quadrant) or \(X+Y=-29\) (third quadrant). Furthermore \(c\in\mathbb Z^2\), since it is obtained by applying finitely many integer-affine branch maps to a constant point produced at a first rank-zero step; more directly, a zero linear branch composition has only its integer affine translation remaining.

The only fixed point outside the connected graph is \(p=(13/16,-1)\), or \((13,-16)\) after scaling. Its global preimage is uniquely itself: neither singular image line contains \((13,-16)\); solving the two invertible branch equations gives the valid fourth-quadrant preimage \((13,-16)\), whereas the second-quadrant candidate \((-16,-13)\) violates its quadrant condition. Hence \(c\) cannot ever reach \(p\). By [1, Theorem B, Proposition 17, and Proposition 27(d)], its orbit must consequently enter \(\Pi\) (or first enter \(\mathcal P\)). Because \(T\) preserves \(\mathbb Z^2\), its entry point in \(\Pi\) is \((k,k+3)\) with an integer \(-11\le k\le13\). Under the scaled sixth return, each such integer is sent by
\[
\widehat G(k)=\begin{cases}
16k+165,&-11\le k\le-19/2,\\
13,&-19/2\le k\le-3,\\
-8k-11,&-3\le k\le0,\\
-11,&0\le k\le13,
\end{cases}
\]
into the finite set \(\{-11,5,13,-3\}\), all of whose elements reach \(-11\) within three more iterations. Every constant-image open cell therefore lands in \(\mathcal P\), and its intersection with \(E\) is empty.

**4. Planar upper bound.** Partition \(\mathbb R^2\) into the countably many finite-iterate polyhedral itinerary cells. Their one-dimensional boundaries have Hausdorff dimension at most one. On each open cell on which \(F^n\) has rank two, the preimage of \(E\cap\Gamma\) has Hausdorff dimension at most \(s\). On a rank-one cell, an invertible affine coordinate change identifies the preimage of \(E\cap\Gamma\) with a subset of a product \(B\times\mathbb R\), where \(B\) lies in a line and has Hausdorff (and suitable upper box) dimension at most \(s\), because \(E\cap\Gamma\) is a countable union of affine copies of a subset of the self-similar \(K\) plus finitely/countably many points. Working on bounded pieces, the standard product upper bound gives dimension at most \(1+s\). Rank-zero cells contribute no points by Step 3. Since every point eventually enters \(\Gamma\), countable union over \(n\) yields \(\dim_{\mathrm H}E\le1+s\).

**5. Sharp planar lower bound.** For every \(u\in I\) and \(v\in[5,6]\), the point \((1+u+v,v)\) belongs to the positive quadrant and satisfies
\[
F(1+u+v,v)=(u,u+3/16).
\]
Choose \(u\in E\cap I\) interpreted on \(\Pi\). The points \((1+u+v,v)\), \(v\in[5,6]\), all belong to \(E\); their parameterization is bi-Lipschitz from \((E\cap\Pi)\times[5,6]\). The product dimension equals \(s+1\), proving the reverse inequality. Thus \(\dim_{\mathrm H}E=1+s\), as claimed. \(\square\)

## Verification
An accompanying standalone script `verify.py` uses exact rational arithmetic to check the six-cycle, the plateau preperiodic orbit, the original sixth-return formula at 306 rational inputs, all 25 integer grid states in the invariant interval, the two inverse contraction ratios, branch scaling, and the singular-image nonintersection with the isolated fixed point. It reports 1,333 assertions passed. The script is supporting reproducibility evidence only: no finite grid is used to infer the infinite-dimensional conclusion. The proof of the infinite Cantor dimension uses strong separation; the reduction to the finite graph is the published theorem [1].

## Relationship to prior work
Cima, Gasull, Mañosa and Mañosas [1] supplied the planar map, graph-entry theorem, explicit invariant graphs, orbit visitation, entropy information, and the four-piece sixth return. Those are explicitly prior results. Their paper does not state the Hausdorff dimension of the *full-plane exact noncapture set*. The sequel [2] proves full graph-arclength measure of preperiodic behavior for ranges of parameters; this measure result does not determine the fractal Hausdorff dimension of the complementary planar basin. The present conclusion combines the two differently expanding branches with a rank-zero exclusion and a one-dimensional lift of the graph exception, producing the precise planar Hausdorff dimension.

## Limitations
The theorem concerns the one specified natural endpoint parameter and exact hitting of the distinguished six-cycle. It does not compute dimensions for other parameters, other periodic orbits, sets of points converging asymptotically but not hitting, or multifractal spectra. Its graph-entry and graph-itinerary premises are published results of [1], not independently re-proved here. This is a self-reviewed mathematical argument, not an independent validation or historical priority certification. An unindexed equivalent theorem remains possible.

## References
[1] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Invariant Graphs and Dynamics of a Family of Continuous Piecewise Linear Planar Maps*, first public arXiv version 2024-10-01, arXiv:2410.01052v1; *Qualitative Theory of Dynamical Systems* 24 (2025), article 70, DOI:10.1007/s12346-025-01221-1. Especially Theorem B, Proposition 17 and Proposition 27(d) and its proof. https://arxiv.org/abs/2410.01052 ; https://link.springer.com/article/10.1007/s12346-025-01221-1

[2] A. Cima, A. Gasull, V. Mañosa and F. Mañosas, *Further results for a family of continuous piecewise linear planar maps*, arXiv:2503.02411v1, first public 2025-03-04. https://arxiv.org/abs/2503.02411
