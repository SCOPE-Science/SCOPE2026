# Complete \(k\)-metric hierarchy of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n\) be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
and edges \(a_i b_j\) exactly when \(i\ne j\). Equivalently, \(\operatorname{Cr}_n=K_{n,n}-M\), where the deleted perfect matching has pairs \(P_i=\{a_i,b_i\}\).

A set \(S\subseteq V(\operatorname{Cr}_n)\) is a \(k\)-metric generator when every two distinct vertices are distinguished by distance to at least \(k\) vertices of \(S\). The minimum size is \(\dim_k(\operatorname{Cr}_n)\).

The crown graph is \(4\)-metric dimensional, and its complete \(k\)-metric hierarchy is
\[
\dim_k(\operatorname{Cr}_n)=
\begin{cases}
n-1,&k=1,\\
n,&k=2,\\
2n-1,&k=3,\\
2n,&k=4.
\end{cases}
\]
No \(k\)-metric generator exists for \(k>4\).

More strongly, writing
\[
c_i=|S\cap P_i|\in\{0,1,2\},
\]
every minimum basis is classified exactly:

- for \(k=1\), exactly one \(c_i\) is \(0\) and every other \(c_j\) is \(1\);
- for \(k=2\), every \(c_i\) is \(1\);
- for \(k=3\), exactly one \(c_i\) is \(1\) and every other \(c_j\) is \(2\);
- for \(k=4\), every \(c_i\) is \(2\).

Hence the exact numbers of minimum bases are, respectively,
\[
n2^{n-1},\qquad 2^n,\qquad 2n,\qquad 1.
\]
In particular, the fault-tolerant metric dimension, which is the \(k=2\) case, equals \(n\), and every fault-tolerant metric basis is a transversal of the deleted perfect matching.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The restriction \(n\ge3\) is essential for connectedness of the crown graph. Distances are ordinary graph distances.

For distinct vertices \(x,y\), let
\[
\mathcal D(x,y)=\{z:d(x,z)\ne d(y,z)\}.
\]
A set \(S\) is a \(k\)-metric generator exactly when \(|S\cap\mathcal D(x,y)|\ge k\) for every distinct \(x,y\).

## Proof
The crown distances are explicit. For distinct indices \(i,j\),
\[
d(a_i,a_j)=d(b_i,b_j)=2,
\]
while
\[
d(a_i,b_j)=1\quad(i\ne j),\qquad d(a_i,b_i)=3.
\]

Consider first two vertices on the same side, say \(a_i,a_j\) with \(i\ne j\). A vertex outside \(P_i\cup P_j\) has equal distance to them: another vertex of \(A\) is at distance \(2\) from both, and a vertex \(b_\ell\) with \(\ell\notin\{i,j\}\) is at distance \(1\) from both. Each of \(a_i,a_j,b_i,b_j\) distinguishes the pair. Therefore
\[
\mathcal D(a_i,a_j)=P_i\cup P_j.
\]
The same argument gives
\[
\mathcal D(b_i,b_j)=P_i\cup P_j.
\]

Now take vertices on opposite sides. If the pair is \(a_i,b_j\), every vertex distinguishes them. Indeed, for a landmark \(a_\ell\), the distance to \(a_i\) is \(0\) or \(2\), whereas the distance to \(b_j\) is \(1\) or \(3\); the analogous parity-separated statement holds for a landmark in \(B\). Thus
\[
\mathcal D(a_i,b_j)=V(\operatorname{Cr}_n)
\]
for all indices \(i,j\), including \(i=j\).

It follows that the only restrictive pairs are same-side pairs. If \(c_i=|S\cap P_i|\), then
\[
S\text{ is a }k\text{-metric generator}
\quad\Longleftrightarrow\quad
c_i+c_j\ge k\text{ for all distinct }i,j.
\]
Since each \(c_i\in\{0,1,2\}\), the maximum feasible value of \(k\) is \(4\), attained by the full vertex set; hence the graph is \(4\)-metric dimensional.

For the minima, order the profile values so that \(c_{(1)}\le c_{(2)}\le\cdots\le c_{(n)}\). The pair inequalities are equivalent to the single extremal inequality
\[
c_{(1)}+c_{(2)}\ge k.
\]
Minimizing \(\sum_i c_i\) under this condition gives the four cases.

For \(k=1\), one zero is allowed but two are not; all other entries can be one. Thus the minimum profile is one zero and \(n-1\) ones, of size \(n-1\).

For \(k=2\), the all-one profile has size \(n\). A zero would force every other entry to be two, giving size \(2n-2>n\) because \(n\ge3\). Thus every minimum profile is all ones.

For \(k=3\), no zero is possible, and if an entry is one then every other entry must be two. This yields size \(2n-1\), smaller than the all-two profile, so exactly one entry is one.

For \(k=4\), every pair sum can reach four only when all profile entries are two. Thus the minimum size is \(2n\).

Finally, count the bases from the classified profiles. For \(k=1\), choose the omitted pair in \(n\) ways and one of its two vertices from each of the remaining \(n-1\) pairs, giving \(n2^{n-1}\). For \(k=2\), choose one endpoint from every pair, giving \(2^n\). For \(k=3\), choose the unique singleton pair and its chosen endpoint, giving \(2n\). For \(k=4\), only the full vertex set occurs.

## Verification
The bundled `verify.py` constructs \(\operatorname{Cr}_n\), computes all-pairs graph distances, verifies the distinctive-set formulas above directly, and then exhaustively checks every vertex subset for \(3\le n\le9\). For each \(k\in\{1,2,3,4\}\), it confirms the claimed minimum, the exact number of minimum bases, and the profile classification. It also confirms that the minimum size of a distinctive set is \(4\).

The finite computation is corroborative. The theorem for arbitrary \(n\) follows from the explicit distance formulas and the profile optimization in the proof.

## Relationship to prior work
Estrada-Moreno, Rodríguez-Velázquez, and Yero introduced the present notion of \(k\)-metric generator and proved the general characterization of the largest admissible \(k\) through minimum distinctive-set size. Their full text also gives results for complete bipartite graphs, but focused searches of the paper found no crown graph, perfect-matching deletion, or equivalent \(K_{n,n}-M\) treatment. The present argument specializes the general framework to a matching-deleted biclique and obtains all four dimensions, every minimum basis, and exact basis counts.

Salman, Javaid, and Chaudhry record the standard equivalence that a resolving set is fault-tolerant exactly when every vertex pair is distinguished by at least two landmarks. Their full text contains no crown, matching-deletion, or complete-bipartite computation, so it supports the interpretation of the \(k=2\) row but does not imply the crown formula.

The later general-approach paper of Estrada-Moreno, Yero, and Rodríguez-Velázquez studies \(k\)-metric and truncated-distance variants and includes complete bipartite examples. Full-text searches found no crown or perfect-matching-deletion result. Its general monotonicity and distinctive-set machinery do not by themselves determine the profile optimization above.

## Limitations
The claim is only for crown graphs \(\operatorname{Cr}_n\) with \(n\ge3\). It does not classify nonminimum \(k\)-metric generators, weighted variants, truncated-distance variants, or matching deletions that are not perfect.

The originality assessment is based on focused published-finding corpus searches, web searches under the aliases crown graph, complete bipartite graph minus a perfect matching, bipartite double cover of a complete graph, and bipartite Kneser graph \(H(n,1)\), plus inspection of the most relevant primary full texts. Unindexed or unusually phrased literature could still exist.

## References
1. A. Estrada-Moreno, J. A. Rodríguez-Velázquez, and I. G. Yero, “The \(k\)-metric dimension of a graph,” arXiv:1312.6840v1, first publicly posted 2013-12-24. MSC 05C05, 05C12, 05C90.
2. M. Salman, I. Javaid, and M. A. Chaudhry, “Minimum Fault-Tolerant, local and strong metric dimension of graphs,” arXiv:1409.2695v1, first publicly posted 2014-09-09. MSC 05C12.
3. A. Estrada-Moreno, I. G. Yero, and J. A. Rodríguez-Velázquez, “The \(k\)-metric dimension of graphs: a general approach,” arXiv:1605.06709v1, first publicly posted 2016-05-21.
