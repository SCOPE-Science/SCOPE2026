# Exact online shattering for acyclic orientations of complete bipartite graphs

## Finding
For every integer \(n\ge1\), the class \(\mathcal A_{2,n}\) of acyclic orientations of \(K_{2,n}\), queried by the direction of individual edges, has
\[
|\mathcal A_{2,n}|=2\cdot3^n-2^n,\qquad
\operatorname{VCdim}(\mathcal A_{2,n})=n+1,\qquad
\operatorname{Ldim}(\mathcal A_{2,n})=\left\lceil\frac{3n}{2}\right\rceil.
\]
In particular the difference is \(\lceil n/2\rceil-1\), unbounded on 2-vertex-connected planar bipartite graphs.

More strongly, the exact residual Littlestone dimension with \(u\) unqueried leaf-pairs, \(a\) one-edge-query leaf-pairs favoring one hub-to-hub direction, and \(b\) favoring the opposite direction, provided neither mixed hub-to-hub path has yet been completed, is
\[
F(u,a,b)=\max\left\{u+a,\;u+b,\;\left\lceil\frac{3u+a+b}{2}\right\rceil\right\},\qquad u,a,b\ge0.
\]

## Assumptions and scope
The graph has distinct hubs \(s,t\), an independent set of \(n\ge1\) leaves, and both hub-to-leaf edges at every leaf. Label an orientation by two bits at each leaf: \(x_i=1\) when \(s\to v_i\) and \(y_i=1\) when \(t\to v_i\). One may query either bit in a complete adaptive binary decision tree. Littlestone dimension is the largest depth at which a complete binary tree of edge-coordinate queries admits, for every root-to-leaf response string, a consistent member of the concept class. VC dimension is the maximum cardinality of a coordinate subset on which all bit assignments are realized. These definitions count the empty tree as depth zero.

## Proof
**Acyclicity and enumeration.** The local bit pairs \(00\) and \(11\) contain no directed path between the hubs; \(10\) creates \(s\to v_i\to t\), whereas \(01\) creates \(t\to v_i\to s\). Every cycle in \(K_{2,n}\) is a four-cycle through two distinct leaves. An orientation has a directed cycle exactly when it contains both types \(10\) and \(01\). Thus its orientation language is the union of the two product languages \(\{00,11,10\}^n\) and \(\{00,11,01\}^n\), with intersection \(\{00,11\}^n\). Inclusion–exclusion gives \(2\cdot3^n-2^n\).

**Residual-state recurrence.** Before a mixed directed hub-to-hub path has been fixed, discard completed neutral leaves. Classify each surviving leaf as unqueried (\(u\)), once queried with its remaining bit able to create a \(10\) path (\(a\)), or once queried with its remaining bit able to create a \(01\) path (\(b\)). Denote the residual Littlestone rank by \(F(u,a,b)\). If a query completes a \(10\) path, all \(01\) paths become forbidden. Every wholly unqueried leaf then has three allowed local patterns of Littlestone rank one; every remaining partially queried \(10\)-favorable leaf has two allowed values of rank one; the other partial leaves become fixed. By additivity of Littlestone dimension for independent coordinate blocks, this forced-signature branch has rank \(u+a-1\) when a particular favorable partial leaf was just completed. The opposite-signature branch has rank \(u+b-1\). A wholly unqueried leaf, after its first query, contributes one partially queried leaf of either category, according to the answer. Consequently, with absent options omitted,
\[
F(u,a,b)=\max\left\{\begin{array}{ll}
1+\min\{F(u-1,a+1,b),F(u-1,a,b+1)\},&u>0,\\
1+\min\{F(u,a-1,b),u+a-1\},&a>0,\\
1+\min\{F(u,a,b-1),u+b-1\},&b>0.
\end{array}\right.
\]
The empty state has rank zero. The independent-block identity follows by concatenating depth-optimal trees for the lower bound and inductively observing that a query changes only one factor; if both resulting restrictions had rank at least one more than the proposed sum, the queried factor itself would have excessive rank. The rank-one claim for a three-state two-bit local concept follows because its nonconstant queries distinguish two outcomes but three hypotheses cannot shatter a binary depth-two tree.

**Solving the recurrence.** Define
\[
H(u,a,b)=\max\{u+a,\;u+b,\;\lceil(3u+a+b)/2\rceil\}.
\]
Strong induction on the number \(2u+a+b\) of unqueried edge bits proves \(F=H\). For \(u=0\), every query reduces either \(a\) or \(b\) by one and its forced-signature branch has rank one less than the corresponding count. Thus the recurrence gives \(F(0,a,b)=\max(a,b)=H(0,a,b)\), by induction on \(a+b\). For \(u>0\), put \(A=u+a\), \(B=u+b\), and \(C=\lceil(3u+a+b)/2\rceil\). The two children of an unqueried-leaf query have inductive ranks \(\max(A,B-1,C-1)\) and \(\max(A-1,B,C-1)\). Suppose \(a\ge b\). Their minimum plus one is \(\max(A,B+1,C)\). If \(a>b\), then \(B+1\le A\), so this equals \(\max(A,B,C)=H\). If \(a=b\), then \(C\ge A+1\) since \(u>0\), and the same conclusion holds. The case \(b>a\) is symmetric. Both partial-leaf query options are at most \(A\) or \(B\), respectively, and thus cannot improve on \(H\). Therefore the formula holds for all \(u,a,b\ge0\). Initially all leaves are unqueried, and so \(\operatorname{Ldim}=F(n,0,0)=\lceil3n/2\rceil\).

**Static dimension and connectedness.** Edge-coordinate sets that form forests are shattered by acyclic orientations: orient the chosen forest arbitrarily, take a topological ordering, and orient every remaining edge in increasing order. A coordinate set containing a cycle is not shattered because the directions following that cycle form a forbidden cyclic response assignment. Thus VC dimension is the maximum size of a forest, \(|V|-1=n+1\), since \(K_{2,n}\) is connected. For \(n\ge2\), this graph is 2-vertex-connected (deleting any one vertex leaves it connected), planar (the parallel two-edge paths can be embedded without crossings), and bipartite, proving the family claim.

## Verification
The standalone standard-library program `verify.py` checks the recurrence against the closed form for every \(0\le u,a,b<30\) (27,000 states), independently enumerates all valid orientation vectors, and computes the exact Littlestone rank by recursive search over every possible edge query for \(1\le n\le7\). The recorded deterministic output is `replay.txt`. These finite computations corroborate, but do not replace, the unrestricted inductive proof.

## Relationship to prior work
The forest criterion and corresponding static shattering dimension for acyclic graph orientations are classical graph-orientation shattering facts, notably situated in Kozma and Moran's work; they are not asserted as new here. Walker (2022) gives general notions and tools for Littlestone/tree dimension rather than the present exact bipartite orientation formula. Prior explicitly treated special cases and bridge-amplified examples do not give the exact residual rank for every complete biclique nor unbounded separation in the 2-vertex-connected family. The contribution here is the three-variable online recurrence, its closed form and the resulting exact dimensions for the entire biclique family.

## Limitations
No claim is made for arbitrary complete bipartite graphs \(K_{p,q}\) with \(p>2\), for other concept/query models, or that this is the first possible dimension gap among all 2-connected planar graphs. Historical priority under alternative online orientation-learning terminology remains open to further human examination. Independent scientific audit has not been performed.

## References
Walker, *Tree Dimension and the Sauer–Shelah Dichotomy*, arXiv:2203.12211 (initial public posting March 23, 2022). Kozma and Moran, *Shattering, Graph Orientations, and Connectivity*, arXiv:1211.1319. Imai and collaborators, *FPT Algorithms to Enumerate and Count Acyclic and Totally Cyclic Orientations*, Electronic Notes in Theoretical Computer Science (2019), doi:10.1016/j.entcs.2019.08.057.
