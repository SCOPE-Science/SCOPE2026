# Geodesic certificates for orbit-exact colour refinement on square toroidal grids

## Finding
For every integer \(n\ge5\), let \(G_n=C_n\square C_n\) be the simple Cartesian product of two cycles, with vertex set \((\mathbb Z/n\mathbb Z)^2\). Two vertices are adjacent when precisely one coordinate changes by \(\pm1\) modulo \(n\). Give the origin \(o=(0,0)\) one unique initial colour and all other vertices one common initial colour. Apply ordinary synchronous one-dimensional counting colour refinement.

**Theorem.** Its stable classes are exactly the orbits of the graph automorphisms fixing \(o\). If \(h=\lfloor n/2\rfloor\) and
\[
 a(x)=\min\{x,n-x\},\quad b(y)=\min\{y,n-y\},
\]
where coordinates are represented by integers in \(\{0,\ldots,n-1\}\), the class of \((x,y)\) is determined precisely by the *unordered* pair \(\{a(x),b(y)\}\). There are exactly
\[
 \frac{(h+1)(h+2)}2
\]
stable classes. Set \(t_n(s)=1\) when \(s=0\) or when \(n\) is even and \(s=h\), and \(t_n(s)=2\) otherwise. The class indexed by \(0\le a\le b\le h\) has size \(t_n(a)^2\) if \(a=b\), and \(2t_n(a)t_n(b)\) if \(a<b\).

More precisely, **three elementary rooted invariants suffice to distinguish all these classes**: graph distance \(d(v)=d(o,v)\); number \(p(v)\) of neighbours lying in the preceding distance shell; and number \(g(v)\) of shortest paths from \(o\) to \(v\). All three are determined by the stable counting-refinement colour, and their common level sets are exactly the rooted automorphism orbits.

## Assumptions and scope
Graphs are finite, simple, undirected, and have one uniquely marked vertex as described above. The cycle parameter is \(n\ge5\) and is otherwise arbitrary (odd or even). A refinement step replaces the colour of a vertex by its current colour together with the multiset of its neighbours' colours. Partition stabilization means that no colour class splits further. This is a statement about within-graph orbit recovery; it makes no assertion about identification against arbitrary graph competitors, the exact number of refinement rounds, or arbitrary additional markings.

## Proof
Write \(v=(x,y)\), \(a=\min\{x,n-x\}\), \(b=\min\{y,n-y\}\), and \(h=\lfloor n/2\rfloor\).

**Step 1: rooted automorphism orbits.** Translations allow the origin to be chosen arbitrarily. The coordinate reflections \((x,y)\mapsto(-x,y)\), \((x,y)\mapsto(x,-y)\) and coordinate interchange \((x,y)\mapsto(y,x)\) fix the origin; their orbits are exactly the unordered pairs \(\{a,b\}\).

There are no larger rooted orbits. For \(n\ge5\), every four-cycle in \(G_n\) is an elementary coordinate square. At any vertex, its four incident edges split into two opposite-coordinate pairs: a pair of edges belongs to the same coordinate direction exactly when the two edges do *not* lie together on a four-cycle. An automorphism fixing the origin therefore has at most eight choices for the images of its four neighbours (interchange the two opposite pairs and independently reverse each pair). Those images determine the whole automorphism: from any oriented edge, its unique straight continuation is the other edge in the same local coordinate pair, so fixing the origin and its neighbours fixes both full coordinate-axis cycles. Every elementary square is determined by three of its corners; propagating squares along one fixed axis then fixes the adjacent coordinate row and, by straight continuation, every remaining row. Hence the rooted stabilizer has at most eight elements. The eight displayed signed-coordinate permutations exist, so it has exactly eight elements and the described orbits are complete.

**Step 2: refinement determines the three invariants.** Let \(A\) be the adjacency matrix, and \(W_k(v)=(A^k)_{v,o}\), the number of walks of length \(k\) from \(v\) to the marked origin. The initial colour determines \(W_0\). Inductively, \(W_{k+1}(v)=\sum_{u\sim v}W_k(u)\); since the \((k+1)\)-st colour determines the multiset of \(k\)-th colours of neighbours, it determines \(W_{k+1}\). Thus each \(W_k\) is constant on every stable colour class. The least \(k\) with \(W_k(v)>0\) is \(d(v)\), so distance is also constant on stable classes. Since the stable partition is equitable and every distance shell is a union of its classes, the number \(p(v)\) of neighbours in distance shell \(d(v)-1\) is likewise constant on stable classes. Finally \(g(v)=W_{d(v)}(v)\) is the shortest-path count, also constant on stable classes.

**Step 3: exact formulas.** In the Cartesian product, distances add, so \(d=a+b\). On a single length-\(n\) cycle, a vertex of circular distance \(s>0\) has one neighbour closer to the origin, except that it has two when \(n\) is even and \(s=h\). Put \(\epsilon_n(s)=1\) when \(n\) is even and \(s=h\), and \(0\) otherwise. Therefore
\[
 p=\mathbf1_{a>0}+\mathbf1_{b>0}+\epsilon_n(a)+\epsilon_n(b).
\]
The two coordinate geodesics may be interleaved in \(\binom{a+b}{a}\) ways. There are two shortest choices in a coordinate exactly at an even-cycle antipode, hence
\[
 g=\binom{a+b}{a}\,2^{\epsilon_n(a)+\epsilon_n(b)}.
\]
These formulas include the origin, for which \(d=p=0\) and \(g=1\).

**Step 4: injectivity of \((d,p,g)\) on unordered coordinate distances.** Sort \(0\le a\le b\le h\). If \(n\) is odd, \(p=0\) identifies the origin, \(p=1\) identifies a point on one coordinate axis (then \(b=d\)), and \(p=2\) means \(a,b>0\). In the last case \(g=\binom da\), which is strictly increasing as \(a\) runs through \(1\le a\le\lfloor d/2\rfloor\); thus \((d,g)\) identifies \(a\) and then \(b\).

If \(n\) is even, write \(h=n/2\ge3\). The cases \(p=0,1,3,4\) are immediately determined by \(d\): they describe respectively the origin; one nonzero nonantipodal coordinate; one antipodal coordinate together with a nonzero nonantipodal coordinate; and two antipodal coordinates. The remaining case \(p=2\) has only two forms: (i) both coordinates are positive and nonantipodal, or (ii) \((a,b)=(0,h)\). Form (ii) has \(d=h\), \(g=2\); for form (i) at the same distance, \(g=\binom ha\ge h\ge3\), so it cannot collide with (ii). In form (i), \(g=\binom da\), again strictly increasing in \(a\le d/2\). Therefore \((d,p,g)\) determines \(\{a,b\}\) in every case.

Step 2 shows that stable refinement cannot merge two different unordered coordinate-distance pairs. Step 1 and isomorphism-invariance show that it cannot separate vertices belonging to the same rooted automorphism orbit. Consequently stable classes equal precisely those orbits. Counting unordered pairs and the independent coordinate sign choices gives the stated class number and class sizes. This proves all assertions. \(\square\)

## Verification
Three independent scripts are provided. `verify_direct.py` constructs the graphs and runs literal synchronous colour refinement for all \(5\le n\le70\), comparing every stable class with the predicted unordered coordinate-distance partition (116765 vertex instances). `verify_certificate.py` checks signature injectivity for all \(5\le n\le500\) and independently constructs breadth-first shortest-path/predecessor counts for \(5\le n\le30\) (9425 vertices). `verify_automorphisms.py` uses a general graph-isomorphism search to enumerate rooted automorphisms for \(n=5,6,7\) and verifies exactly eight such automorphisms and the predicted orbit classes. Their recorded outputs appear in the separate text files; these are finite corroborations, not substitutes for the preceding all-\(n\) proof.

## Relationship to prior work
Arvind, Köbler, Rattan and Verbitsky (arXiv:1502.01255, 2015) define refinability as agreement between stable colour classes and automorphism orbits and investigate broader graph-class implications and complexity. Kiefer, Schweitzer and Selman (arXiv:1503.08792, 2015) study the related two-variable counting-logic identification problem. Neither inspected primary work states the present rooted Cartesian-cycle-square theorem or its three-statistic geodesic certificate. The assertion should not be confused with colour-refinement identification among arbitrary graphs, which is stronger and is *not* asserted here.

## Limitations
The theorem addresses the equal-factor toroidal family \(C_n\square C_n\) for \(n\ge5\), one distinguished origin, and standard unweighted, counting-based one-dimensional refinement. It does not classify rectangular toroidal products with unequal circumferences, arbitrary additional vertex colourings, stabilization depth, or graph identification. The lower boundary \(n=4\) has extra Cartesian factor symmetries because \(C_4\square C_4\) is a four-dimensional cube, so the displayed triple-injectivity proof is not intended to apply there. Publication priority requires independent literature review; the mathematical proof is subject only to self-review, not independent certification.

## References
1. V. Arvind, J. Köbler, G. Rattan, O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, first posted 2015-02-04, arXiv:1502.01255, https://arxiv.org/abs/1502.01255.
2. S. Kiefer, P. Schweitzer, E. Selman, *Graphs Identified by Logics with Counting*, first posted 2015-03-30, arXiv:1503.08792, https://arxiv.org/abs/1503.08792.
