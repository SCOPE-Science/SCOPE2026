# Dominant edge metric dimension and minimum bases of hypercubes

## Finding
For the binary hypercube \(Q_n\), let \(\operatorname{Ddim}_e(Q_n)\) denote the minimum cardinality of a vertex set that is simultaneously a vertex cover and an edge metric generator. Then, for every integer \(n\ge 1\),
\[
\operatorname{Ddim}_e(Q_n)=
\begin{cases}
1,&n=1,\\
3,&n=2,\\
2^{n-1},&n\ge3.
\end{cases}
\]
Moreover, for every \(n\ge3\), the only minimum dominant edge metric bases are the two parity classes of \(\{0,1\}^n\). For \(Q_2\), the minimum bases are exactly its four three-vertex subsets, while \(Q_1\) has its two singleton bases.

## Assumptions and scope
All graphs are finite, simple, and undirected. Vertices of \(Q_n\) are binary vectors in \(\{0,1\}^n\), with adjacency when two vectors differ in exactly one coordinate. For a vertex \(s\) and edge \(uv\), the edge distance is
\[
d(s,uv)=\min\{d(s,u),d(s,v)\}.
\]
A set \(S\subseteq V(Q_n)\) is an edge metric generator when the vectors \((d(s,e))_{s\in S}\) are distinct for all distinct edges \(e\). It is a dominant edge metric generator when it is also a vertex cover.

## Proof
Assume first that \(n\ge3\). Write \(E\) and \(O\) for the even- and odd-Hamming-weight parity classes. Each has cardinality \(2^{n-1}\), and each is a vertex cover because every hypercube edge joins opposite parities.

We show that \(E\) edge-resolves \(Q_n\). Orient every edge uniquely as
\[
(u,u\oplus e_i),
\]
where \(u\in E\) and \(e_i\) is the \(i\)-th coordinate vector. Consider two distinct oriented edges \((u,u\oplus e_i)\) and \((u',u'\oplus e_j)\).

If \(u\ne u'\), take the landmark \(s=u\in E\). Its distance to the first edge is \(0\), whereas its distance to the second edge is positive: the second edge contains the even vertex \(u'\ne u\) and an odd vertex, so it does not contain \(u\).

If \(u=u'\), then necessarily \(i\ne j\). Choose a coordinate \(k\notin\{i,j\}\), which is possible because \(n\ge3\), and put
\[
s=u\oplus e_i\oplus e_k\in E.
\]
Then
\[
d\bigl(s,(u,u\oplus e_i)\bigr)=1,
\qquad
d\bigl(s,(u,u\oplus e_j)\bigr)=2.
\]
Thus the two edges receive different distance vectors. Therefore \(E\) is a dominant edge metric generator; by symmetry, so is \(O\).

For the lower bound, \(Q_n\) has a perfect matching, so every vertex cover has size at least \(2^{n-1}\). Hence \(\operatorname{Ddim}_e(Q_n)=2^{n-1}\) for \(n\ge3\).

The equality case also classifies all minimum bases. Let \(S\) be a dominant edge metric basis of size \(2^{n-1}\), and let \(I=V(Q_n)\setminus S\). Since \(S\) is a vertex cover, \(I\) is independent and has size \(2^{n-1}\). The graph \(Q_n\) is \(n\)-regular and has \(n2^{n-1}\) edges. Thus the sum of degrees over \(I\) is
\[
n|I|=n2^{n-1}=|E(Q_n)|.
\]
Because \(I\) is independent, each edge is counted at most once in this degree sum; equality therefore forces every edge to have exactly one endpoint in \(I\). Consequently \(S\) is independent as well, so \((S,I)\) is a bipartition of the connected graph \(Q_n\). The bipartition of a connected bipartite graph is unique up to swapping its two classes, hence \(S\) is exactly one of the two parity classes.

For \(n=2\), \(Q_2=C_4\). A two-vertex cover must consist of two opposite vertices, but the two edges incident with either selected vertex have identical distance vectors to that cover, so no two-vertex cover edge-resolves. Any three vertices do. For example, if the cycle is \(v_0v_1v_2v_3v_0\) and \(S=(v_1,v_2,v_3)\), the four edge vectors are
\[
(0,1,1),\quad(0,0,1),\quad(1,0,0),\quad(1,1,0),
\]
which are distinct. Hence \(\operatorname{Ddim}_e(Q_2)=3\), and by symmetry all four three-vertex subsets are bases. For \(n=1\), the graph has one edge; either endpoint alone is a vertex cover, and the edge-resolving condition is vacuous because there is no pair of distinct edges. Thus \(\operatorname{Ddim}_e(Q_1)=1\), with two singleton bases.

## Verification
The standalone script `verify.py` reconstructs hypercubes directly from binary vertices, checks the vertex-cover and edge-resolution conditions, and exhaustively searches every candidate subset for \(Q_1,Q_2,Q_3,Q_4\). It obtains respectively the minimum-size/basis-count pairs
\[
(1,2),\ (3,4),\ (4,2),\ (8,2).
\]
It also checks both parity classes directly as dominant edge metric generators for every \(Q_n\) with \(3\le n\le10\). The archived output terminates with `VERIFY_OK`. These finite computations corroborate the proof but are not a substitute for the infinite argument.

## Relationship to prior work
The dominant edge metric dimension was introduced and studied for several basic graph families in the 2023 paper identified by DOI `10.5614/ejgta.2023.11.1.16`; its listed primary classification includes \(05C12\). The case \(Q_2=C_4\) belongs to the cycle family treated there. Earlier hypercube work identified by `arXiv:2102.10916` studies ordinary metric, edge metric, and mixed metric dimensions, but not the dominant edge metric dimension. A later paper identified by DOI `10.11648/j.acm.20261503.13` studies the dominant edge metric dimension for star-fan graphs rather than hypercubes. The contribution here is the exact formula for all higher-dimensional binary hypercubes together with the complete characterization of minimum dominant edge metric bases.

## Limitations
The theorem concerns binary hypercubes only; it does not determine the parameter for general Hamming graphs or other Cartesian products. The originality assessment is best-of-knowledge and may miss inaccessible or differently phrased literature. The computational checks cover only the stated finite range and are supporting evidence rather than a formal proof. No independent audit, formal proof assistant verification, or expert attestation has been performed.

## References
1. `doi:10.5614/ejgta.2023.11.1.16` — *The dominant edge metric dimension of graphs*; verified public source dated 2023-04-11.
2. `arXiv:2102.10916` — *On Metric Dimensions of Hypercubes*; first public version dated 2021-02-22.
3. `doi:10.11648/j.acm.20261503.13` — later work on dominant edge metric dimension for star-fan graphs.
