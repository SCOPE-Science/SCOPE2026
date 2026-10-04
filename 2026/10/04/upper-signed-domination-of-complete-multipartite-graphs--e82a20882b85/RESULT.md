# Upper signed domination of complete multipartite graphs
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\). Put \(N=\sum_{i=1}^r n_i\), let \(L=\max_i n_i\), and write \(c=N-L\). Then
\[
\Gamma_s(G)=N-2\left\lfloorrac{c}{2}ightfloor.
\]
Here \(\Gamma_s(G)\) is the maximum weight among minimal signed dominating functions. Thus the upper parameter depends only on the order and the size of a largest part.

More precisely, if \(V_\ell\) is any largest part and \(m=\lfloor c/2floor\), then assigning \(-1\) to any \(m\) vertices of \(V(G)\setminus V_\ell\) and \(+1\) to every other vertex is a minimal signed dominating function of maximum possible weight.

## Assumptions and scope
A signed dominating function is a map \(f:V(G)	o\{-1,+1\}\) satisfying \(f(N[v])\ge1\) for every vertex \(v\), where \(N[v]\) is the closed neighborhood. It is minimal when there is no distinct signed dominating function \(g\) with \(g(v)\le f(v)\) for every \(v\). The weight is \(f(V(G))=\sum_{v\in V(G)}f(v)\), and \(\Gamma_s(G)\) is the maximum weight of a minimal signed dominating function.

The theorem concerns finite simple connected complete multipartite graphs, hence \(r\ge2\). No assertion is made for disconnected one-part graphs.

## Proof
For each part \(V_i\), set \(n_i=|V_i|\) and \(c_i=N-n_i\). Let \(f\) be a minimal signed dominating function. Write \(M\) for the total number of vertices assigned \(-1\), \(m_i\) for the number assigned \(-1\) in \(V_i\), and \(t_i=M-m_i\) for the number assigned \(-1\) outside \(V_i\). For any \(u\in V_i\), all vertices outside \(V_i\) are adjacent to \(u\), while no other vertex of \(V_i\) is. Therefore
\[
f(N[u])=c_i-2t_i+f(u).
\]

A standard minimality criterion for signed domination says that for every vertex \(v\) with \(f(v)=+1\), some \(u\in N[v]\) satisfies \(f(N[u])\in\{1,2\}\). Choose a positive vertex \(v\), which must exist, and such a witness \(u\in V_i\).

If \(f(u)=+1\), then \(c_i-2t_i\in\{0,1\}\), hence \(t_i=\lfloor c_i/2floor\). Consequently
\[
M\ge t_i=\left\lfloorrac{c_i}{2}ightfloor\ge\left\lfloorrac{c}{2}ightfloor,
\]
because \(c_i=N-n_i\ge N-L=c\).

If \(f(u)=-1\), then \(c_i-2t_i\in\{2,3\}\), so \(t_i=\lfloor c_i/2floor-1\). Since now \(m_i\ge1\),
\[
M=t_i+m_i\ge\left\lfloorrac{c_i}{2}ightfloor\ge\left\lfloorrac{c}{2}ightfloor.
\]
Thus every minimal signed dominating function has weight
\[
N-2M\le N-2\left\lfloorrac{c}{2}ightfloor.
\]

It remains to attain the bound. Fix a largest part \(V_\ell\), put \(m=\lfloor c/2floor\), choose any \(m\) vertices outside \(V_\ell\), assign those vertices \(-1\), and assign every other vertex \(+1\). For \(u\in V_\ell\),
\[
f(N[u])=c-2m+1\in\{1,2\}.
\]
For a different part \(V_j\), if it contains no negative vertex then the sum of labels outside it is at least \(c-2m\in\{0,1\}\), so every positive vertex there has closed-neighborhood sum at least \(1\). If \(V_j\) contains a negative vertex, at most \(m-1\) negative vertices lie outside \(V_j\), so the sum of labels outside it is at least
\[
c-2(m-1)\in\{2,3\},
\]
and even a negative vertex has closed-neighborhood sum at least \(1\). Hence \(f\) is signed dominating.

Every positive vertex of \(V_\ell\) is itself a tight witness with closed-neighborhood sum in \(\{1,2\}\). Every positive vertex outside \(V_\ell\) is adjacent to every vertex of \(V_\ell\), so it also has such a witness. The minimality criterion therefore makes \(f\) minimal. It has exactly \(m\) negative vertices, proving the formula.

## Verification
The accompanying `verify.py` exhaustively enumerates every ordered complete-multipartite profile through order \(10\), every \(\{-1,+1\}\)-labeling of each corresponding labeled vertex set, and tests signed domination and minimality directly by the definitions. For each profile it compares the maximum weight of a minimal signed dominating function with the displayed formula and separately checks the explicit largest-part construction. This finite census is a stress test only; the theorem for arbitrary order is established by the proof above.

## Relationship to prior work
The 2014 paper *Upper Singed Domination Number of Graphs* defines the same upper parameter, states the minimality witness criterion used above, and determines the complete-bipartite case. If the two part sizes are \(m\le n\), then the present formula gives \(m+n-2\lfloor m/2floor\), exactly recovering that theorem.

Liang's 2012 complete-multipartite paper and the earlier Zhao--Shan--Zhao work determine the signed domination number, signed total domination number, and minus-domination parameters for complete multipartite graphs. Those are minimum-weight parameters and do not imply the maximum weight among minimal signed dominating functions. Liang's 2012 signed \(k\)-domination work and later upper signed \(k\)-domination papers treat complexity and general bounds, not this exact arbitrary complete-multipartite formula.

## Limitations
The novelty comparison is limited by indexing and access to some older domination literature. The closest exact structured-family result inspected in full is the complete-bipartite theorem, and the complete-multipartite sources located concern minimum signed/minus parameters rather than the upper signed parameter. The result has not undergone an independent audit.

## References
1. H. Liang, *On the Signed (Total) \(k\)-Domination Number of a Graph*, arXiv:1204.4827v1, first posted 2012-04-21.
2. H. Liang, *Signed and Minus Domination in Complete Multipartite Graphs*, arXiv:1205.0343v1, first posted 2012-05-02; later Ars Combinatoria 126 (2016), 133--142.
3. H. B. Walikar, S. V. Motammanavar, and T. Venkatesh, *Upper Singed Domination Number of Graphs*, International Journal of Mathematics and Combinatorics 1 (2014), 87--92.
4. Y. Zhao, E. Shan, and W. Zhao, *Several domination numbers of a complete multipartite graph*, Utilitas Mathematica 81 (2010), 99--110.
