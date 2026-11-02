# One-edge robustness of three-colouring reconfiguration for bicliques

## Finding

Let \(m,n\ge 2\) be integers, let \(H=K_{m,n}\) with labelled bipartition \(L\sqcup R\), and let \(G=H-uv\) where \(u\in L\), \(v\in R\). For any graph \(F\), write \(\mathcal C_3(F)\) for the graph of all proper vertex colourings by the individually named colours \(\{0,1,2\}\), with an edge when exactly one vertex changes colour.

**Theorem.** \(\mathcal C_3(G)\) consists of the six-cube cyclic necklace \(\mathcal C_3(H)\) with exactly six new degree-two vertices, each completing a square across two existing neighbours of a junction. Its exact order and size are
\[
|V(\mathcal C_3(G))|=3(2^m+2^n),\qquad |E(\mathcal C_3(G))|=3(m2^{m-1}+n2^{n-1})+12.
\]
Every old-colouring pair has exactly the same shortest-path distance before and after the deletion. **Every** vertex of both reconfiguration graphs has eccentricity
\[
D=\left\lfloor\frac{3(m+n)}2\right\rfloor.
\]
In particular both are connected and self-centred, and their common radius and diameter equal \(D\). The new graph is bipartite precisely when \(m+n\) is even; otherwise its odd girth is exactly \(3(m+n)\) and its chromatic number is three.

This is a perturbation theorem: removal of one constraint edge adds exactly six configurations and twelve moves without shortening any pre-existing recolouring distance or changing the optimal worst-case recolouring bound.

## Assumptions and scope

Graphs are finite, simple and labelled. The deleted edge \(uv\) is arbitrary; biclique automorphisms make its choice immaterial. The three colours are distinct labels, although a colouring may use only two. A recolouring step changes **one** vertex, and all intermediates must be proper. Distance is the ordinary unweighted shortest-path distance. Statements cover every integer \(m,n\ge2\) without a parity restriction. The exclusions \(m=1\) or \(n=1\) are intentional: the classification of exceptional shared-colour configurations differs for stars.

Call a colouring **old** if it is proper on \(H\), and **extra** if it is proper on \(G\) but not \(H\). A **junction** means a colouring monochromatic on each of \(L,R\), with different colours. A **cube** refers to the induced family with one fixed monochromatic side, not a Euclidean cube.

## Proof

**1. Old configurations form a six-cube necklace.** In a proper three-colouring of \(H\), the nonempty palettes used on \(L\) and \(R\) are disjoint. At least one side is therefore monochromatic. For each colour \(i\), the configurations with all of \(L\) coloured \(i\) induce \(Q_n\), by freely choosing one of the other two colours on each vertex of \(R\). Similarly the configurations with all of \(R\) coloured \(j\) induce \(Q_m\). The only overlaps are the six junctions \(C_{i,j}\) with \(i\ne j\). The intersection graph of these six cubes is the cycle whose alternating blocks have dimensions \(n,m,n,m,n,m\). Within each block the two junctions are opposite binary strings, at Hamming distance equal to the dimension. A one-vertex recolouring leaving the interior of such a cube must pass through a junction: if the other side already uses both available colours, no recolouring of the monochromatic side is possible. Thus there are no inter-block edges away from junctions. The necklace circumference (sum of terminal distances) is \(L_0=3(m+n)\).

**2. There are precisely six extra configurations, each of degree two.** An extra colouring has \(\kappa(u)=\kappa(v)=i\), necessarily with the same shared colour \(i\). No other vertex can use \(i\), because each vertex of \(L\setminus\{u\}\) is adjacent to \(v\), and each vertex of \(R\setminus\{v\}\) is adjacent to \(u\). The other two colours must be used on opposite sides, because \(L\setminus\{u\}\) and \(R\setminus\{v\}\) are both nonempty and complete to each other. Hence the extra states are exactly
\[
E_{i,j,k}:\quad \kappa(u)=\kappa(v)=i,\quad
\kappa(L\setminus\{u\})=j,\quad
\kappa(R\setminus\{v\})=k,
\]
where \((i,j,k)\) runs over the six permutations of \((0,1,2)\). The only legal recolourings from \(E_{i,j,k}\) are \(u:i\to j\) and \(v:i\to k\). Their old endpoints are \(X_{j,k}\) (all of \(L\) is \(j\), only \(v\) is different from \(k\) on \(R\)) and \(Y_{j,k}\) (all of \(R\) is \(k\), only \(u\) differs from \(j\) on \(L\)). Both are neighbours of junction \(C_{j,k}\), in its two incident cubes. Thus \(X_{j,k},C_{j,k},Y_{j,k},E_{i,j,k}\) is an induced square. Every junction gets one such new square; no other vertices or edges are added. This proves the order and size formulas, using \(|V(\mathcal C_3(H))|=3(2^m+2^n)-6\) and \(|E(\mathcal C_3(H))|=3(m2^{m-1}+n2^{n-1})\).

**3. Old distances are unchanged.** Any path through an extra vertex uses its two incident edges \(X-E-Y\). Replace those edges by \(X-C-Y\) of the same length. Repeating for all extra vertices converts every path between old states to an old-only walk of no greater length. The reverse inequality follows because \(\mathcal C_3(H)\) is a subgraph of \(\mathcal C_3(G)\).

**4. Necklace metric.** Model the six cubes by six consecutive integer-length arcs of a circle of circumference \(L_0\), with lengths alternating \(m,n\). For each vertex \(x\) in one cube of dimension \(d\), choose its circle coordinate at the integer distance \(t=d_{Q_d}(x,A)\) from the first junction \(A\) of that cube. Its distance to the other junction \(B\) is \(d-t\). For \(x,y\) in *different* cube interiors, the exact old graph distance is the shortest circle distance between these coordinates: every route between blocks passes through a junction, and distances to the two junctions are \(t,d-t\). The same formula applies to distinct junctions. For vertices in the same cube, their graph distance is their Hamming distance (at most \(d\)); a detour through all other blocks is no shorter because its terminal length is \(L_0-d>d\).

Let \(D=\lfloor L_0/2\rfloor\). All old distances are at most \(D\), because different-block distances are circle distances and same-block distances are at most \(\max(m,n)<D\). From each old vertex choose a vertex on another block at an integer circle position clockwise \(D\) away. Such a position always has a cube vertex, and it cannot be in the starting cube because \(D>\max(m,n)\). Therefore its graph distance is \(D\). Every old vertex has eccentricity exactly \(D\), before and after the deletion.

**5. New vertices have the same eccentricity.** Fix extra vertex \(E\) attached to old junction \(C\). Its two neighbours \(X,Y\) lie one circle step to either side of \(C\), in its incident cubes. If an old vertex \(z\) lies in either of these cubes, then \(d(E,z)\le 1+\max(m,n)\le D\), by travelling from \(E\) to the incident portal in that cube. The junction \(C\) itself is at distance two. If \(z\) lies in a nonincident cube, follow a shortest circle arc from \(C\) to the circle coordinate of \(z\). The first step is one of the two portals, so the route from \(E\) through it has length equal to the circle distance \(d_{\mathrm{circ}}(C,z)\le D\). In particular, a vertex at circle position exactly \(D\) clockwise from \(C\) lies in a nonincident cube and is at distance exactly \(D\) from \(E\): after the first portal, all distances to this distant cube are the old exact circle distances, and the nearer portal is at distance \(D-1\) from this point.

For two different extra vertices \(E_C,E_B\), let their junctions have shorter circle separation \(s\le D\). If the junctions are nonadjacent on the six-junction cycle, the first and last portals of that arc lie in different cubes, and the old distance between them is \(s-2\). The extra vertices are consequently at distance at most \(s\). If their junctions are adjacent, with connecting cube dimension \(d\), use the two respective portal neighbours in that cube: their Hamming distance is at most \(d\), yielding \(d+2\le D\). Thus all new-to-new distances are at most \(D\). Combined with the preceding opposite-position witness, every extra vertex has eccentricity exactly \(D\).

**6. Parity.** Every cube is bipartite; a cycle that meets multiple cubes and is not contained in a single cube must traverse the entire six-block ring and has length at least \(L_0\). A ring cycle of length \(L_0\) exists by choosing shortest antipodal paths in each cube. Therefore the old graph is bipartite when \(L_0\) is even and otherwise has odd girth \(L_0\). Adding each square cannot introduce a shorter odd cycle: an odd closed walk using \(X-E-Y\) projects to an old odd closed walk of the same length by substituting \(X-C-Y\); every odd closed walk contains an odd cycle of no greater length. This proves the same parity and odd-girth properties for the new graph. Finally \(\mathcal C_3(G)\) is a subgraph of the coordinate Hamming graph \(K_3^{\square(m+n)}\), which is properly three-coloured by the sum of the coordinate labels modulo three. The presence of an odd cycle gives chromatic number exactly three in the odd case.

## Verification

The attached `verify_direct.py` independently enumerates the \(3^{m+n}\) assignments, filters proper colourings before and after deleting \(uv\), constructs every one-vertex recolouring, and uses exhaustive breadth-first searches to check exact eccentricities and unchanged old-old distances. It also checks odd girth by parity-lifted breadth-first searches. Cases checked are \((m,n)=(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4),(4,5)\).

The attached `verify_structural.py` separately generates states from the six hypercubes and the six special extra assignments without enumerating all \(3^{m+n}\) inputs. It tests direct legal-neighbour sets and exhaustive eccentricities for \((m,n)=(2,2),(2,3),(2,6),(3,3),(3,4),(4,4),(5,5)\). Both checkers completed successfully after being executed from the artifact directory. These finite computations are checks, not the all-parameter proof, which is supplied in the preceding section.

## Relationship to prior work

Celaya, Choo, MacGillivray and Seyffarth (2016) studied the proper recolouring graph of the **complete** biclique, described its monochromatic-side hypercubes, and established the Hamiltonicity criterion for its three-colouring graph. That prior classification of the old states is used and credited here. The new assertion concerns **deleting one constraint edge**, classifying the resulting six extra states and their precise attachment, and proving distance preservation and the same exact, everywhere-attained diameter. General work on reconfiguration of three-colourings treats connectivity and polynomial distance bounds without this perturbation formula. In particular, the 2016 Hamiltonicity result does not establish the perturbation claim. Searches of published mathematical finding records and literature under three-colouring/recolouring, missing-edge bicliques, one-edge deletion, distance, radius and hypercube-necklace terminology did not identify the stated one-edge stability theorem. A negative search is not a proof of historical priority.

## Limitations

The theorem does not address the removal of two or more edges, nor lists/palettes with four or more colours, nor the star cases \(m=1\) or \(n=1\). The shortest odd cycle concerns the reconfiguration graph, not the original bipartite graph. The source comparison relies partly on indexed primary-paper text, because the original author-linked PDF was unavailable; possible unindexed equivalent treatments remain an originality risk. Independent scholarly examination is not claimed.

## References

1. M. Celaya, K. Choo, G. MacGillivray and K. Seyffarth, *Reconfiguring k-colourings of Complete Bipartite Graphs*, Kyungpook Mathematical Journal **56** (2016), 647–655, DOI: 10.5666/KMJ.2016.56.3.647 (online 2016-09-01).
2. L. Cereceda, J. van den Heuvel and M. Johnson, *Finding Paths Between 3-Colorings*, Journal of Graph Theory **67** (2011), 69–82, DOI: 10.1002/jgt.20514.
3. P. Bonsma and L. Cereceda, *Finding paths between graph colourings: PSPACE-completeness and superpolynomial distances*, Theoretical Computer Science **410** (2009), 5215–5226.
