# Sharp second maximum of the number of three-path-convex sets in connected graphs

## Finding
Let \(G\) be a finite, connected, simple graph on \(n\ge9\) vertices, not isomorphic to the star \(K_{1,n-1}\). A subset \(S\subseteq V(G)\) is \(P_3\)-convex precisely when every vertex outside \(S\) has at most one neighbor in \(S\). Let \(c(G)\) count these subsets, including the empty set.

Define the broom \(B_n\) by subdividing one edge of \(K_{1,n-2}\): it has one vertex of degree \(n-2\), one vertex of degree two, and \(n-2\) leaves. Then
\[
 c(G)\le 3\cdot 2^{n-3}+2n-2,
\]
with equality **if and only if** \(G\cong B_n\). Thus for every \(n\ge9\), the broom is the unique connected nonstar maximizing isomorphism type. For comparison, the previously established unrestricted connected maximum is \(2^{n-1}+n\), attained by the star at these orders.

## Assumptions and scope
Graphs are finite, undirected and simple. Vertex subsets are labelled subsets; graph isomorphism is used only to classify equality. A convex set obeys the local rule for *every* vertex outside the set, not just for induced three-vertex paths. The claim covers all connected graphs of order at least nine, including graphs with cycles. It makes no assertion about disconnected graphs or about the second maximum below order nine.

## Proof
**1. A rooted inclusion lemma.** For any tree \(H\) with \(t\ge5\) vertices and any \(v\in V(H)\), at least \(2t-2\) of its convex sets contain \(v\). Denote this count by \(A(H,v)\). The three trees on five vertices are the star, the one-edge-subdivided star, and the path; direct inspection gives respective minimum rooted counts \(9,8,9\), establishing the bound at \(t=5\). For \(t\ge6\), choose a leaf \(x\ne v\), and remove it. Every convex subset containing \(v\) in \(H-x\) remains convex in \(H\) when \(x\) is omitted. Two further distinct convex subsets contain both \(v\) and \(x\): the entire vertex set, and either \(\{v,x\}\) when \(d_H(v,x)\ge3\), or the vertex set of the unique \(v\)-to-\(x\) path when \(d_H(v,x)\le2\). An outside vertex in a tree has at most one neighbor in any connected subtree; the distant pair has no common neighbor. Thus \(A(H,v)\ge A(H-x,v)+2\ge 2t-2\).

**2. A rooted one-neighbor lemma.** For a tree \(T\) and \(v\in V(T)\), set
\[
D(T,v)=\#\{S\subseteq V(T):S\text{ is }P_3\text{-convex},\ v\notin S,\ |N_T(v)\cap S|=1\}.
\]
If \(T\) is a nonstar of order \(m\ge6\), then
\[D(T,v)\ge 2m-4.\]
For \(d_T(v)=1\), let \(a\) be the neighbor of \(v\). Removing \(v\) identifies the sets counted by \(D(T,v)\) with convex subsets of \(T-v\) containing \(a\). By step 1 there are at least \(2(m-1)-2=2m-4\).

For \(d=d_T(v)\ge2\), nonstarhood ensures \(t=m-1-d\ge1\) vertices at distance at least two from \(v\). For every \(z\ne v\), the vertex set of the unique path from \(v\) to \(z\), with \(v\) removed, is a connected and hence convex set meeting \(N(v)\) once: this gives \(m-1\) distinct sets. For each of the \(t\) vertices \(z\) at distance at least two, choose any of the \(d-1\) neighbors \(x\) of \(v\) in branches other than the branch of \(z\). Then \(d_T(x,z)\ge3\); the disconnected pair \(\{x,z\}\) is convex and meets \(N(v)\) exactly in \(x\). These \((d-1)t\) pairs are distinct from the connected-path sets. Consequently
\[
D(T,v)\ge (m-1)+(d-1)t=(2m-4)+(d-2)(t-1)\ge2m-4.
\]

**3. The leaf-extension identity.** If \(T^+\) is obtained by adding a new leaf adjacent to \(v\) in the tree \(T\), partition the convex sets by membership of the new leaf. Sets not containing it correspond to every convex set of \(T\). Among sets containing the new leaf, those of \(T\) having \(v\) selected are admissible, as are those with \(v\) unselected and no neighbor of \(v\) selected. The only lost sets are those counted by \(D(T,v)\). Therefore
\[
c(T^+)=2c(T)-D(T,v).
\]

**4. Broom count and strict equality.** In \(B_m\), call the degree-\(m-2\) hub \(h\), its degree-two neighbor \(b\), the far endpoint \(z\), and the \(m-3\) ordinary hub leaves \(y\). If \(h\) belongs to a convex set, the pair \((b,z)\) has the three allowed patterns \((0,0),(1,0),(1,1)\), while ordinary leaves may be chosen independently: \(3\cdot2^{m-3}\) choices. If \(h\) does not belong, at most one of its neighbors is chosen. Counting the possibilities with \(b\) chosen or not gives \(2m-2\) choices. Hence
\[
c(B_m)=3\cdot2^{m-3}+2m-2.
\]
The exact rooted one-neighbor counts are
\[
\begin{aligned}
D(B_m,h)&=2m-4,\\
D(B_m,b)&=2^{m-3}+m-2,\\
D(B_m,z)&=2^{m-3}+1,\\
D(B_m,y)&=3\cdot2^{m-4}.
\end{aligned}
\]
For \(m\ge9\), all of these except the hub value are *strictly* greater than \(2m-4\). These formulas follow by conditioning on the selected neighbor and the forced status of the degree-two branch.

**5. Base case and induction for trees.** Exhaustive enumeration of all 47 isomorphism types of nine-vertex trees using rooted parenthesis codes, and direct checking of all vertex subsets, gives the unique nonstar maximum \(208=3\cdot2^6+16\), attained by the degree sequence \((7,2,1,1,1,1,1,1,1)\), which uniquely specifies \(B_9\). Details and executable verification are in `verify.py`.

Suppose the sharp assertion holds for nonstar trees of order \(n-1\), with \(n\ge10\), and let \(T\) be a nonstar tree of order \(n\). Delete any leaf \(r\), adjacent to \(v\), obtaining \(T'\). If \(T'\) is a star, adjoining \(r\) to its hub would make \(T\) a star, excluded here; the only other choice adjoins it to one of the leaves and gives \(T\cong B_n\). If \(T'\) is nonstar, step 2 and the leaf identity yield
\[
\begin{aligned}
c(T)&=2c(T')-D(T',v)\\
&\le2\bigl(3\cdot2^{n-4}+2(n-1)-2\bigr)-(2(n-1)-4)\\
&=3\cdot2^{n-3}+2n-2.
\end{aligned}
\]
Equality forces \(T'\cong B_{n-1}\) and \(D(T',v)=2(n-1)-4\). Since \(n-1\ge9\), step 4 forces \(v\) to be the hub, and adjoining the leaf produces \(B_n\). Thus the bound and equality classification hold for every nonstar tree of order \(n\ge9\).

**6. General connected graphs.** Adding edges cannot create new convex vertex subsets: the defining outside-neighbor bound only becomes harder. Moreover, adding any edge \(uv\) to a tree \(T\) strictly decreases its convex-set count. Indeed, let \(P\) be the unique \(u\)-to-\(v\) path in \(T\) and choose \(S=V(P)\setminus\{u\}\). This is a connected subtree's vertex set, so convex in \(T\), but in \(T+uv\) the omitted vertex \(u\) has two neighbors in \(S\), the first path neighbor and \(v\).

If a connected nonstar graph \(G\) has no universal vertex, every spanning tree is nonstar. If \(G\) is not itself a tree, strict edge monotonicity gives \(c(G)<c(T)\le c(B_n)\). If \(G\) has a universal vertex and is not a star, it contains as a spanning subgraph a star with one additional leaf-to-leaf edge. This graph has \(2^{n-2}+n\) convex subsets (the hub-selected case has \(2^{n-2}\) possibilities and the hub-absent case has \(n\)), which is strictly smaller than \(3\cdot2^{n-3}+2n-2\) for \(n\ge9\). Together with the tree case, this proves the theorem for all connected simple graphs, with equality only for \(B_n\). \(\square\)

## Verification
The standalone `verify.py` enumerates all unlabelled trees through order nine by adjoining leaves and quotienting by exact rooted-tree parenthesis isomorphism codes. Its counts of unlabelled trees at orders one through nine are \(1,1,1,2,3,6,11,23,47\). It checks the defining local convexity rule on every subset, verifies the nine-vertex base case and its unique optimizer, verifies the rooted inclusion base and rooted defect bounds on the accessible small trees, checks leaf-extension identities directly, and checks the closed forms on finite broom and one-extra-edge examples. The infinite induction and reduction from connected graphs are mathematical arguments; the executable base-case search is exhaustive on nine vertices, not evidence about larger orders by itself.

Reproduce by running `python3 verify.py` with a standard Python 3 interpreter. Expected final line: `ONE_PASS`.

## Relationship to prior work
Dourado, Grippo, Lin and Protti (2026), Theorem 11, proved the unrestricted connected upper bound \(2^{n-1}+n\) and established stars as the unique maximizers for \(n\ge6\). Their Section 2 develops a tree counting recursion. The present theorem strengthens that extremal statement to the exact next layer after excluding the star, identifies one unique nonstar equality type at every order \(n\ge9\), and gives its sharp value and rooted rigidity mechanism. It does not claim their star theorem or their basic tree dynamic programming as new.

## Limitations
This statement concerns \(P_3\)-convexity (the two-selected-neighbor closure), not geodesic or monophonic convexity. The threshold \(n\ge9\) is genuine for the nonstar equality classification: at orders \(6,7,8\), the path is the unique best nonstar tree, with counts \(37,65,114\), respectively. Unrestricted historical priority under alternate terminology has not been independently established; an earlier equivalently strong theorem is possible. Independent mathematical assessment has not been performed.

## References
Dourado, M. C., Grippo, L. N., Lin, M. C., and Protti, F. (2026). *Counting \(P_3\)-convex sets in graphs*. arXiv:2603.04706v1, first publicly submitted 2026-03-05. https://arxiv.org/html/2603.04706v1 . Theorem 11 and Section 2.
