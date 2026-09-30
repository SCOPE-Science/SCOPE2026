# Complete multipartite dual general-position sets and exact variant enumerators
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), parts \(V_1,\ldots,V_r\), and
\[
N=\sum_i n_i,\qquad M=\max_i n_i,\qquad s=|\{i:n_i=1\}|,\qquad p=|\{i:n_i\ge2\}|,\qquad q=|\{i:n_i=2\}|.
\]
For \(v\in\{o,t,d\}\), define the counting polynomial
\[
P_v(G;x)=\sum_{X\in\mathcal G_v(G)}x^{|X|},
\]
where \(\mathcal G_o(G)\), \(\mathcal G_t(G)\), and \(\mathcal G_d(G)\) are the outer, total, and dual general-position sets.

The outer polynomial and number are
\[
P_o(G;x)=1+Nx+\sum_i\bigl((1+x)^{n_i}-1-n_i x\bigr)+\bigl((1+x)^s-1-sx\bigr),
\]
\[
\operatorname{gp}_o(G)=\max\{M,s\}.
\]
If
\[
\tau=\begin{cases}N,&p=0,\\M,&p=1,\\0,&p\ge2,\end{cases}
\]
then the total polynomial and number are
\[
P_t(G;x)=(1+x)^\tau,\qquad \operatorname{gp}_t(G)=\tau.
\]

The dual sets have the following complete classification. Besides the empty set, a dual set is precisely one of these two types:

1. a nonempty subset \(X\subseteq V_i\) for a part \(V_i\) such that every other part is a singleton;
2. when \(M\le2\), a set containing exactly one vertex from every 2-vertex part and an arbitrary subset of the singleton parts.

Accordingly,
\[
P_d(G;x)=\begin{cases}
(1+x)^N,&M=1,\\
(1+x)^2+2x\bigl((1+x)^s-1\bigr),&M=2,\ q=1,\\
1+(2x)^q(1+x)^s,&M=2,\ q\ge2,\\
(1+x)^M,&M\ge3,\ p=1,\\
1,&M\ge3,\ p\ge2,
\end{cases}
\]
and
\[
\operatorname{gp}_d(G)=\begin{cases}
r,&M\le2,\\
M,&M\ge3,\ p=1,\\
0,&M\ge3,\ p\ge2.
\end{cases}
\]
In particular, if there are at least two non-singleton parts and one part has size at least three, then the empty set is the only dual general-position set.

## Assumptions and scope
Graphs are finite, simple, and connected. The complete multipartite graph has \(r\ge2\) nonempty parts. The empty set is admitted as a general-position set, so a dual general-position number of zero is meaningful. The outer and total arguments use the published characterizations that outer general-position sets are exactly sets of pairwise mutually maximally distant vertices, while total general-position sets are exactly subsets of the simplicial vertices. The dual condition is that the set is in general position and its complement is convex.

## Proof
First note the ordinary general-position structure. A set \(X\) is in general position if and only if either \(X\subseteq V_i\) for some part, or \(|X\cap V_i|\le1\) for every part. Indeed, two selected vertices in the same part together with a selected vertex in another part lie on a length-two geodesic. Conversely, a set contained in one part has every internal geodesic vertex outside the set, while a set meeting each part at most once is a clique.

For the outer variant, consider distinct vertices \(u\in V_i\) and \(v\in V_j\). If \(i=j\), then \(d(u,v)=2\), and every neighbor of either endpoint is adjacent to the other endpoint; hence \(u,v\) are mutually maximally distant. If \(i\ne j\), then \(d(u,v)=1\). Vertex \(u\) is maximally distant from \(v\) exactly when \(V_j=\{v\}\), because any second vertex of \(V_j\) is a neighbor of \(u\) at distance two from \(v\). Symmetrically, the pair is mutually maximally distant exactly when both parts are singletons. Thus an outer set of size at least two is either contained in one part or contained in the singleton-vertex set. Counting these families, with the empty set and one-vertex sets counted only once, gives \(P_o(G;x)\), and its degree is \(\max\{M,s\}\).

A vertex in \(V_i\) is simplicial exactly when every part other than \(V_i\) is a singleton, because its open neighborhood consists of all vertices outside \(V_i\). Therefore every vertex is simplicial when \(p=0\); exactly the \(M\) vertices of the unique non-singleton part are simplicial when \(p=1\); and no vertex is simplicial when \(p\ge2\). The published total-set characterization now gives \(P_t(G;x)=(1+x)^\tau\).

It remains to classify the dual sets. A subset \(C\subseteq V(G)\) is convex if and only if
\[
|C\cap V_i|\ge2\quad\Longrightarrow\quad V(G)\setminus V_i\subseteq C
\]
for every \(i\). The reason is that the only nonadjacent vertex pairs lie in a common part, and for distinct \(u,v\in V_i\) their interval consists of \(u,v\) together with every vertex outside \(V_i\). Pairs from distinct parts are adjacent and impose no additional condition.

Let \(X\ne\varnothing\) be dual and put \(C=V(G)\setminus X\). If \(X\subseteq V_i\), convexity of \(C\) forces every other part to be a singleton: otherwise two vertices of another part lie in \(C\), and their interval contains \(X\). Conversely, if every other part is a singleton, then every subset of \(V_i\) is in general position and its complement satisfies the displayed convexity criterion.

Suppose instead that \(X\) meets at least two parts. By the ordinary general-position structure, it meets every part in at most one vertex. If some part has size at least three, then its complement contains at least two vertices of that part; convexity would force all of \(X\) into that one part, a contradiction. Hence \(M\le2\). Moreover, every 2-vertex part must contribute exactly one vertex to \(X\); if one contributed none, both of its vertices would lie in \(C\), again forcing \(X\) into that part. Singleton parts may be chosen arbitrarily. Conversely, under these conditions both \(X\) and \(C\) meet every part at most once, so \(X\) is in general position and \(C\) is a clique, hence convex. This proves the classification. The displayed formulas for \(P_d(G;x)\) follow by direct counting, and the dual number is the degree of that polynomial.

## Verification
The standalone file `verify.py` enumerates all 58 unordered complete multipartite part-size types of orders two through eight and every vertex subset. It checks the ordinary general-position lemma, the outer classification via mutual maximal distance, the total classification via simpliciality, and the dual classification via direct convexity of the complement. It then compares the complete coefficient vectors of \(P_o(G;x)\), \(P_t(G;x)\), and \(P_d(G;x)\) with the formulas above. The certificate reports `VERIFY_OK types=58 subsets=8084 property_checks=32336 polynomial_checks=174`.

This finite exhaustive computation is corroborative only; the proof above establishes the formulas for all admissible part sizes.

## Relationship to prior work
Tian and Klavžar introduced and systematically related the dual, total, and outer general-position variants. Their source theorem identifies total sets with subsets of simplicial vertices and outer sets with pairwise mutually maximally distant sets, while the dual notion is general position with convex complement. The earliest public version located is arXiv:2402.17338v1, dated 27 February 2024, with primary MSC2020 class 05C12 among its classifications.

The source and the checked later survey material do not give the complete-multipartite formulas above. The best-of-knowledge originality claim is therefore restricted to the complete structural classification of dual sets and the explicit complete-multipartite enumerators. The ordinary complete-multipartite general-position observation and the source characterizations of the three variants are not claimed as new. The outer and total formulas should be viewed as companion consequences that make the three-variant picture explicit in one family.

## Limitations
No independent audit, proof-assistant verification, or expert attestation has been performed. The computational certificate covers only orders at most eight and is not used as a substitute for the general proof. The literature claim is best-of-knowledge rather than an absolute priority guarantee. In particular, older strong-resolving-graph results may implicitly contain the outer-number consequence because mutual maximal distance is a standard notion; no novelty claim depends on that consequence alone.

## References
1. Jing Tian and Sandi Klavžar, *Variety of general position problems in graphs*, arXiv:2402.17338v1, 27 February 2024; later published in *Bulletin of the Malaysian Mathematical Sciences Society*, DOI 10.1007/s40840-024-01788-z.
