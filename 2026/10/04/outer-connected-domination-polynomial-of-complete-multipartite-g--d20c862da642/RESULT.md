# Outer-connected domination polynomial of complete multipartite graphs

## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a connected complete multipartite graph with \(r\ge2\), partite classes \(V_1,\ldots,V_r\), and \(N=\sum_i n_i\). For \(D\subseteq V(G)\), put \(C=V(G)\setminus D\). Under the standard convention that \(D=V(G)\) is outer-connected dominating, \(D\) is outer-connected dominating if and only if either \(D=V(G)\), or both conditions hold:

1. \(C\) is a singleton or meets at least two partite classes.
2. \(D\) meets at least two partite classes or equals one whole part \(V_i\).

Equivalently, the non-outer-connected-dominating subsets are exactly three disjoint families: the empty set; nonempty proper subsets of one part; and subsets whose complement has at least two vertices and lies wholly inside one part. Therefore the outer-connected domination polynomial is
\[
\widetilde D(G;x)=(1+x)^N-1-\sum_{i=1}^r\left((1+x)^{n_i}-1-x^{n_i}\right)-\sum_{i=1}^r\sum_{c=2}^{n_i}\binom{n_i}{c}x^{N-c}.
\]
Evaluating at \(x=1\) gives the exact total number
\[
|\mathcal D_{oc}(G)|=2^N+N+3r-1-2\sum_{i=1}^r2^{n_i}.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The complete multipartite graph has \(r\ge2\) nonempty partite classes. An outer-connected dominating set is a dominating set \(D\) such that either \(D=V(G)\) or the induced graph on \(V(G)\setminus D\) is connected. This is the convention used in the polynomial paper arXiv:1112.0846.

The result classifies every subset and counts every cardinality. It does not claim novelty for the scalar outer-connected domination number of complete multipartite graphs, which was already published, nor for the star polynomial.

## Proof
A nonempty induced subgraph of a complete multipartite graph is connected exactly when it is a singleton or contains vertices from at least two partite classes. Thus for a proper set \(D\), the outer-connectivity condition is equivalent to saying that \(C=V(G)\setminus D\) is a singleton or meets at least two parts.

For domination, if \(D\) meets at least two parts, then every omitted vertex lies in one part and has a selected neighbor in another part. If instead \(D\) meets exactly one part \(V_i\), then an omitted vertex of \(V_i\) has no neighbor in \(D\). Hence such a set dominates exactly when it is the whole part \(V_i\). The empty set does not dominate. This proves the structural characterization.

Now start from all \(2^N\) subsets. The empty set contributes the subtraction \(1\). For each part \(V_i\), the nonempty proper subsets of that part contribute
\[
\sum_{d=1}^{n_i-1}\binom{n_i}{d}x^d=(1+x)^{n_i}-1-x^{n_i}.
\]
For each part \(V_i\), a disconnected nonempty complement supported inside \(V_i\) has size \(c\ge2\), and choosing it contributes \(\binom{n_i}{c}x^{N-c}\). These three excluded families are disjoint: a nonempty proper subset of one part leaves vertices in that part and every other nonempty part in the complement, so its complement meets at least two parts. Subtracting the three families gives the displayed polynomial. Setting \(x=1\) and simplifying gives the total-count formula.

## Verification
The standalone script `verify.py` constructs every nondecreasing complete-multipartite part profile of order at most \(10\), checks every vertex subset against the literal domination-plus-connected-complement definition, compares it with the structural criterion, and compares the resulting cardinality counts with every coefficient of the formula. It also verifies the published complete-multipartite minimum formula and the published star polynomial on all profiles in the checked range.

A successful replay prints a line of the form `VERIFY_OK ... max_order=10`. The finite census is a consistency check only; arbitrary order follows from the symbolic proof above.

## Relationship to prior work
Alikhani, Akhbari, Eslahchi, and Hasni introduced the outer-connected domination polynomial. Their arXiv record was first submitted on 5 December 2011 and lists primary MSC 05C69. The same paper states the exact outer-connected domination number for complete multipartite graphs, computes the polynomial for complete graphs, paths, cycles, and stars, and gives a join formula under connected-factor hypotheses. It does not state the arbitrary complete-multipartite all-set classification or the polynomial above. In particular, its scalar complete-multipartite theorem and its star polynomial are treated here as prior-covered consequences and checks, not as novelty.

Panda and Pandey later studied algorithms and hardness for minimum outer-connected domination, including a linear-time minimum algorithm on chain graphs. That broader algorithmic result concerns minimum cardinality rather than the full set census of arbitrary complete multipartite graphs.

The present formula is not a consequence of the published complete-multipartite minimum value alone: many different all-set distributions share the same minimum exponent. The connected-factor join formula also does not directly cover a general decomposition of a complete multipartite graph into edgeless partite factors.

## Limitations
The claim is restricted to connected complete multipartite graphs. It gives an exact cardinality polynomial, not a multivariate polynomial that remembers each part occupancy separately. The finite verifier stops at order \(10\); it is not used as an infinite proof. Literature searches cannot exclude every obscure or poorly indexed equivalent formulation, so a residual originality risk remains.

## References
S. Alikhani, M. H. Akhbari, C. Eslahchi, and R. Hasni, “On the number of outer connected dominating sets of graphs,” arXiv:1112.0846, first submitted 5 December 2011; published in Utilitas Mathematica 91 (2013), 99–107.

J. Cyman, “The outer-connected domination number of a graph,” Australasian Journal of Combinatorics 38 (2007), 35–46.

B. S. Panda and A. Pandey, “Algorithm and Hardness Results for Outer-connected Dominating Set in Graphs,” Journal of Graph Algorithms and Applications 18(4) (2014), 493–513.
