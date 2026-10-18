# Two-round orbit recovery for line graphs of complete multipartite graphs

## Finding
Let \(r\ge 2\), let \(n_1,\ldots,n_r\) be positive integers, and put \(G=K_{n_1,\ldots,n_r}\). The vertices of its line graph \(L(G)\) are edges of \(G\). Start ordinary synchronous one-dimensional counting colour refinement with all vertices identically coloured. If an edge has endpoints in parts of sizes \(a\) and \(b\), call the unordered pair \(\{a,b\}\) its *type*.

**Theorem.** For every such \(G\), the colour partition after two refinement rounds coincides exactly with the automorphism-orbit partition of \(L(G)\). Its cells are precisely the edge types \(\{a,b\}\). If \(m_s\) denotes the number of parts of size \(s\), the cell of type \(\{a,b\}\) has size
\[
|C_{a,b}|=\begin{cases}
m_a m_b ab,&a<b,\\[3pt]
\binom{m_a}{2}a^2,&a=b.
\end{cases}
\]
Writing \(t\) for the number of distinct part sizes, the exact number of orbit classes is
\[
\binom{t}{2}+\#\{s:m_s\ge2\}.
\]

More precisely, define \(\mathcal T\) as the set of unordered size pairs realized by two distinct parts. The first refinement partition has one class per distinct sum \(a+b\) for \(\{a,b\}\in\mathcal T\). The **exact first round at which the orbit partition is attained** is zero if \(|\mathcal T|=1\), one if \(|\mathcal T|>1\) and the map \(\{a,b\}\mapsto a+b\) is injective on \(\mathcal T\), and two otherwise.

A two-round requirement is possible for the first time at total root-graph order eight; the **unique** nondecreasing part-size vector at this minimum is \((1,2,2,3)\), for which the 23-vertex line graph has three classes after one round but four automorphism orbits. The collision is between types \(\{1,3\}\) and \(\{2,2\}\). The family with part sizes \((u,u+1,u+1,u+2)\), \(u\ge1\), requires two rounds in every order.

## Assumptions and scope
The input graphs are finite, simple, complete multipartite graphs with at least two nonempty parts. A line-graph vertex represents one unordered edge between distinct parts; two line-graph vertices are adjacent if those edges share exactly one endpoint. Refinement round zero is the constant vertex colouring, and round \(k+1\) records the round-\(k\) colour and the multiset of round-\(k\) colours in the open neighbourhood. Colours are compared only within the same graph. The theorem concerns **orbit recovery within a graph**, not distinguishing arbitrary nonisomorphic graphs, nor arbitrary individualizations of vertices.

## Proof
Put \(N=\sum_i n_i\) and \(Q=\sum_i n_i^2\). For a line-graph vertex \(e=xy\), suppose \(x\) lies in part \(i\) of size \(a=n_i\) and \(y\) lies in a different part \(j\) of size \(b=n_j\). Its degree is
\[
D(e)=(N-a-1)+(N-b-1)=2N-a-b-2.
\tag{1}
\]
Thus round one distinguishes exactly the realized values of \(a+b\).

Consider the sum \(S(e)=\sum_{f\sim e}D(f)\) of the line-graph degrees of neighbours of \(e\). Each edge from \(x\) to a vertex in part \(k\ne i\) contributes \(2N-a-n_k-2\). The analogous assertion holds for edges from \(y\), but \(e\) itself is counted once in each of these two collections, and is not a neighbour of itself. Therefore
\[
S(e)=\sum_{k\ne i}n_k(2N-a-n_k-2)
     +\sum_{k\ne j}n_k(2N-b-n_k-2)-2D(e).
\tag{2}
\]
Using \(\sum_{k\ne i}n_k=N-a\) and \(\sum_{k\ne i}n_k^2=Q-a^2\), expansion gives
\[
S(e)=4N^2-8N-2Q+4+(4-3N)(a+b)+2(a^2+b^2).
\tag{3}
\]

Round one determines \(D(e)\), and hence \(a+b\). Round two determines the **entire multiset of degrees of neighbours**, because round-one colours distinguish their degrees. In particular it determines \(S(e)\). For fixed graph constants \(N,Q\), equations (1) and (3) determine both \(a+b\) and \(a^2+b^2\), so also
\[
ab=\frac{(a+b)^2-(a^2+b^2)}2.
\tag{4}
\]
The unordered pair \(\{a,b\}\) is the multiset of roots of \(z^2-(a+b)z+ab=0\). Thus any two different edge types are separated by the second refinement round.

Conversely, permuting vertices within each part and permuting whole parts of equal size are graph automorphisms of \(G\). These automorphisms act transitively on edges with any fixed type \(\{a,b\}\). Their induced actions are automorphisms of \(L(G)\), so an isomorphism-invariant refinement cannot distinguish two vertices having that same type. Combined with the preceding separation, this proves equality of the round-two partition with the full automorphism-orbit partition; no classification of all automorphisms of line graphs is required.

For \(a<b\), there are \(m_a m_b\) ordered choices of the corresponding two parts and \(ab\) edges for each pair; for \(a=b\), there are \(\binom{m_a}{2}\) pairs of parts and \(a^2\) edges each. This yields the cell-size formula, and counting allowable types yields the class-count formula. The precise depth description follows because round zero has one class, round one is characterized exactly by \(a+b\), and round two is the orbit partition.

Finally, if two different unordered size pairs have the same sum, they can be realized using **four distinct parts**: pairs sharing a part have the same size in their other endpoint part and hence represent the same unordered size pair. The smallest positive integer sum admitting two different unordered pairs is four, with exactly the alternatives \(\{1,3\}\) and \(\{2,2\}\). Thus the total sizes of these four parts are at least eight. Equality forces exactly four parts of sizes \((1,2,2,3)\). These indeed realize two distinct types of sum four, so they are not separated in round one. Its line graph has \(1\cdot2+1\cdot2+1\cdot3+2\cdot2+2\cdot3+2\cdot3=23\) vertices, three different endpoint-size sums and four types. For \((u,u+1,u+1,u+2)\), the two pairs \(\{u,u+2\}\) and \(\{u+1,u+1\}\) have equal sum for all \(u\ge1\); hence the bound remains sharp without an upper size limit. \(\square\)

## Verification
Run the accompanying standalone programs with Python 3. The direct graph test (`direct_check.py`) constructs line graphs explicitly for 114 nondecreasing part-size configurations with up to five parts and root order at most 16, totalling 4,558 line-graph vertices over the tests. It verifies the complete predicted round-zero/one/two partition sequence against the independently encoded endpoint-size types. The arithmetic checker (`moment_check.py`) tests formula (3) and injectivity of the pair of integer moments over 3,424 nondecreasing size vectors and 481,572 comparisons of edge types. The separate automorphism checker (`orbit_check.py`, requiring NetworkX) enumerates **all** line-graph automorphisms for seven test configurations, including the minimal obstruction, and checks their orbit partition against the claimed type partition. The recorded program outputs are included as text files.

These are finite cross-checks of explicit computations. The universal assertions, including the exact minimal order and arbitrarily large sharp examples, follow from the preceding symbolic argument rather than empirical extrapolation.

## Relationship to prior work
The line graphs of complete multipartite graphs are explicitly defined and studied in Tananyan, *Domination games played on line graphs of complete multipartite graphs* (arXiv:1405.0087v1, 2014); its results concern domination games rather than refinement-depth or orbit reconstruction. Arvind, Köbler, Rattan and Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness* (arXiv:1502.01255v1, 2015), define refinable graphs through equality of the stable colour and automorphism-orbit partitions, and discuss Johnson graphs (the line graphs of complete graphs); their statements inspected do not give the present arbitrary-multipartite formula or exact two-round criterion. Key and Seneviratne (2007) investigate binary codes of **balanced** multipartite line graphs; the accessible abstract does not decide the arbitrary-unbalanced refinement claim. The contribution here is the precise two-moment reconstruction, complete unbalanced orbit census, exact depth criterion and minimum obstruction. A prior specialized derivation remains possible and independent priority assessment is outstanding.

## Limitations
This result does not assert amenability or identification of distinct input graphs by counting logic. There is no assertion for arbitrary vertex markings, non-complete multipartite graphs, or weighted/directed line graphs. Existence of a short proof or a failed literature search does not establish publication priority. The independent scientific audit has not been performed. The computational tests cover finite sizes only.

## References
1. H. G. Tananyan, *Domination games played on line graphs of complete multipartite graphs*, arXiv:1405.0087v1, 1 May 2014. https://arxiv.org/html/1405.0087v1
2. V. Arvind, J. Köbler, G. Rattan and O. Verbitsky, *Graph Isomorphism, Color Refinement, and Compactness*, arXiv:1502.01255v1, 4 February 2015. https://arxiv.org/abs/1502.01255
3. J. D. Key and P. Seneviratne, *Codes from the line graphs of complete multipartite graphs and PD-sets*, Discrete Mathematics 307 (2007), 2217–2225. https://doi.org/10.1016/j.disc.2006.11.008
