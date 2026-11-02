# The strong-resolving-set polynomial and forcing rigidity of clique–cycle Cartesian graphs

## Finding
For every pair of integers \(q\ge3\) and \(n\ge3\), consider the Cartesian product \(G_{q,n}=K_q\square C_n\), and let \(\mathcal R_{q,n}(z)=\sum_{S}z^{|S|}\), summed over **all** strong resolving vertex sets. Define \(h_q(t)=(1+t)^q-1-qt\) and
\[
B_q(t)=\begin{pmatrix}1&qt&h_q(t)\\1&t&0\\1&0&0\end{pmatrix}.
\]
Then, with negative powers cancelled by the indicated prefactor,
\[
\mathcal R_{q,n}(z)=\begin{cases}
\bigl(2z^q(z+1)^q-z^{2q}+qz^{2q-2}\bigr)^{n/2},&n\text{ even},\\
z^{qn}\bigl(\operatorname{tr}(B_q(z^{-1})^n)+(q-1)z^{-n}\bigr),&n\text{ odd}.
\end{cases}
\]
These are exact finite polynomials, including the constant and highest-degree coefficients. In particular, the corresponding minimum strong resolving sets (strong metric bases) are completely classified:

* If \(n\) is even, each basis chooses one entire \(K_q\)-layer from each antipodal pair of cycle layers; there are exactly \(2^{n/2}\) bases.
* If \(n\ge5\) is odd, each basis is the union of all \(K_q\)-layers indexed by a minimum vertex cover of the cycle obtained by joining maximally distant cycle vertices; there are exactly \(n\) bases.
* If \(n=3\) and \(q>3\), each basis comprises two entire \(K_q\)-layers; there are exactly three.
* If \(n=q=3\), there are exactly six: the three complements of a complete layer and the three complements of a single color across all three layers.

The strong metric dimension (also implied by earlier product theory) and forcing strong metric dimension are respectively
\[
(\operatorname{sdim}(G_{q,n}),\operatorname{fsdim}(G_{q,n}))=
\begin{cases}
(qn/2,n/2),&n\text{ even},\\
(q(n+1)/2,2),&n\ge5\text{ odd},\\
(2q,2),&n=3,\ q>3,\\
(6,3),&n=q=3.
\end{cases}
\]
The original contribution assessed here is the complete cardinality distribution, exhaustive basis census, and forcing rigidity. The scalar strong metric dimension is **not** asserted as new.

## Assumptions and scope
All graphs are finite, simple and connected. The cycle \(C_n\) has vertices \(\mathbb Z/n\mathbb Z\); the complete factor has colors \([q]\). Distances in the product obey
\[d((a,i),(b,j))=\mathbf1_{a\ne b}+\min(|i-j|,n-|i-j|).\]
A vertex \(s\) strongly resolves distinct vertices \(u,v\) when \(d(s,u)=d(s,v)+d(u,v)\) or \(d(s,v)=d(s,u)+d(u,v)\). A set is strong resolving when it resolves every pair. A *basis* is a minimum-cardinality strong resolving set. A forcing subset of a basis is a subset contained in no **other basis**; the forcing number is the minimum cardinality of such a subset, and the forcing strong metric dimension is the minimum of this number over all bases.

For clarity, the odd-cycle layer order in the displayed polynomial follows the edges of the maximally-distant graph, not necessarily the original cyclic order. Relabeling does not change the enumerator or the labeled count.

## Proof
**1. Reduction to a vertex-cover enumerator.** The standard strong-resolving-graph theorem states that strong resolving sets of a connected graph are exactly vertex covers of the graph whose edges join mutually maximally distant (MMD) vertices [1]. For Cartesian products, a pair is MMD precisely when each factor-coordinate pair is MMD: the distance is a sum, and changing just one coordinate witnesses any failure of maximality. Every two distinct vertices in \(K_q\) are MMD; equal vertices are not MMD when considered as a coordinate of a distinct product pair. In \(C_n\), MMD means antipodal layers for even \(n\), or separation \((n-1)/2\) for odd \(n\). Thus the strong resolving graph is the categorical (direct) product of \(K_q\) with the cycle MMD graph. Its vertex-cover polynomial is \(z^{qn}\) times the independence polynomial evaluated at \(z^{-1}\). This reduction is credited to [1], not claimed as an original lemma.

**2. Even cycles.** The MMD graph of an even cycle is a matching on \(n/2\) edges. Each corresponding connected component of the product is the crown graph \(K_{q,q}\) with its diagonal matching removed. An independent set lies on one bipartition side, or else consists of the two matched vertices across the sides. Inclusion–exclusion gives its independence polynomial \(2(1+t)^q-1+qt^2\). Taking its \(n/2\)-th power and complementing independent sets gives the stated even polynomial. Since \(q\ge3\), the only maximum independent sets of a crown are the two entire sides. This proves the even basis census and \(\operatorname{sdim}=qn/2\).

**3. Odd cycles and the transfer matrix.** The MMD graph of an odd cycle is itself a cycle, since its step \((n-1)/2\) is coprime to \(n\). For an independent set in \(K_q\times C_n\), write \(A_i\subseteq[q]\) for the colors chosen in layer \(i\). Two adjacent layers are permitted precisely when at least one is empty, or both are the same singleton. Classify each layer as empty \(E\), one of \(q\) singleton colors, or a heavy subset of at least two colors. Their weights are \(1\), \(t\), and total \(h_q(t)\), respectively. Empty layers can meet any state, a singleton can meet only empty or its own color, and heavy layers meet only empty. Consequently the full \((q+2)\)-state cyclic transfer matrix is the direct sum, at trace level, of the three-dimensional invariant block \(B_q(t)\) and \(q-1\) color-difference modes, each of eigenvalue \(t\). Summing over closed cyclic words gives \(\operatorname{tr}(B_q(t)^n)+(q-1)t^n\). Complementing independent sets gives the odd polynomial, with no limiting or asymptotic step.

**4. Maximum independent configurations.** If an independent configuration on the odd cycle contains an empty layer, every maximal run of at least two adjacent nonempty layers must consist of singleton colors, all the same within the run. Replacing the run, while leaving its neighboring empty layers untouched, by full \(q\)-color layers on alternate positions increases its cardinality: \(q\lceil r/2\rceil>r\) for every \(r\ge2\) since \(q\ge3\). Hence a maximum with an empty layer has only isolated occupied layers, all containing every color. The maximum possible number of such layers is \((n-1)/2\), with exactly \(n\) distinct supports on the odd cycle. If no layer is empty, all layers must be the same singleton color, giving just \(n\) vertices. For odd \(n\ge5\), \(q(n-1)/2>n\); the full-layer configurations are therefore the only maxima. At \(n=3\), the full-single-layer pattern of size \(q\) beats all-singleton patterns of size three when \(q>3\); at \(q=3\) they tie and yield six maximum independent sets. Complementation gives the complete basis classification and displayed scalar dimensions.

**5. Forcing numbers.** In the even case every crown component independently chooses one of two entire sides for a basis. A forcing subset must identify all \(n/2\) component choices, so at least one selected vertex per component is necessary and sufficient. For odd \(n\ge5\), the \(n\) bases are complements of maximum independent column supports of an odd cycle. No single vertex belongs to only one of these bases. Each minimum cover of the odd cycle contains a unique adjacent column pair; selecting one vertex in each column of that pair uniquely determines the cover: removing the pair leaves an odd-order path with a unique maximum independent set of the required cardinality. Hence every basis has forcing number two. For \(n=3,q>3\) the bases are complements of single full layers; two selected vertices in different selected layers identify their basis, and one does not. For \(n=q=3\), the six bases are three two-layer complements and three two-color complements. Any two selected vertices lie together in at least two bases (one of each family, or two within a family); three selected vertices covering both selected layers and all three colors single out a given two-layer basis. By color–layer symmetry the same applies to the other bases. Thus the minimum forcing number is three.

## Verification
A standalone standard-library Python program `verify.py` is included. It builds graph neighborhoods and independent sets from the defining Cartesian adjacency, reconstructs MMD pairs directly by checking every neighbor against exact graph distances, enumerates all independent sets on small instances, and compares **every coefficient** with the closed polynomials. Where the vertex count is at most 15 it separately tests the original metric strong-resolution definition for all subsets rather than relying only on the MMD theorem. It also enumerates every minimum basis and checks forcing numbers on all tested graphs of at most 16 vertices.

Successful parameter tests: \((q,n)=(3,3),(4,3),(5,3),(3,4),(4,4),(3,5),(4,5),(3,6),(3,7)\), ending with `VERIFY_OK`. These finite computations test boundary behavior but do not establish the infinite-family statement; the preceding proof does.

## Relationship to prior work
Rodríguez-Velázquez, Yero, Kuziak and Oellermann [1] establish the strong-resolving-graph/vertex-cover equivalence and its Cartesian product behavior; their work determines, or immediately implies, the **scalar** strong metric dimension in this family. The scalar is included for context, not presented as novel. Lenin, Kathiresan and Bača [2] introduce forcing strong metric dimension and compute it for single cycles and several other families, not these clique–cycle products. Bergougnoux, Defrain and Mc Inerney [3] give a general polynomial-delay framework for enumerating minimal strong resolving sets, without the present full all-cardinality polynomial, labeled optimal-set classification, or product-specific forcing transition. The full independence polynomial is an equivalent reformulation of the strong-resolving-set polynomial under [1], so novelty rests on the explicitly evaluated family-specific enumerator and rigidity statements, **not** the conversion itself.

## Limitations
The result assumes \(q\ge3\) and \(n\ge3\) and does not cover binary complete factors, arbitrary Cartesian factors, or non-cycle base graphs. The known scalar strong metric dimensions, categorical-product reduction, and vertex-cover equivalence are prior contributions, not new results. Although relevant full texts and targeted searches were compared, a previously published equivalent independence-polynomial formula for the categorical product of a complete graph and a cycle could imply the enumerator; publication priority is not independently certified. The result has not undergone independent mathematical review.

## References
[1] J. A. Rodríguez-Velázquez, I. G. Yero, D. Kuziak and O. R. Oellermann, *On the strong metric dimension of Cartesian and direct products of graphs*, arXiv:1307.4722 (first submitted 2013-07-17). https://arxiv.org/abs/1307.4722

[2] R. Lenin, K. M. Kathiresan and M. Bača, *The Forcing Strong Metric Dimension of a Graph*, Contributions to Discrete Mathematics 12(2), published 2017-11-27, DOI:10.55016/ojs/cdm.v12i2.62287. https://cdm.ucalgary.ca/article/view/62287

[3] B. Bergougnoux, O. Defrain and F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419 (first submitted 2023-09-29). https://arxiv.org/abs/2309.17419
