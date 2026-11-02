# Sharp \(qk\) cutoff for intersection-defined finite-set graphs

## Finding
Fix \(k\ge1\), \(q\ge2\), and \(S\subseteq\{0,1,\ldots,k-1\}\). For each \(n\ge k\), let \(G_{n,k,S}\) be the graph on the \(k\)-subsets of \([n]\), with distinct vertices adjacent exactly when their intersection size is in \(S\). Then
\[
G_{n,k,S}\equiv_qG_{m,k,S}\qquad\text{whenever }n,m\ge qk.
\]
The cutoff \(qk\) is sharp uniformly: for \(S=\{0\}\), the graphs on ground sets of sizes \(qk-1\) and \(qk\) are separated by a sentence of rank \(q\). Every graph in this family therefore has a rank-\(q\)-equivalent representative on at most \(\binom{qk}{k}\) vertices, a sharp uniform bound.

## Assumptions and scope
All graphs are finite, simple, and undirected, with equality and one adjacency symbol. The parameters \(k\), \(q\), and \(S\) are fixed when comparing the graph orders \(n,m\). The cutoff does not claim that all smaller orders yield different theories, nor that the same rank-\(q\) theory persists when \(k\) or \(S\) varies.

## Proof
**Finite-support back-and-forth lemma.** Suppose \(t<q\) selections have been played in the ordinary \(q\)-round Ehrenfeucht–Fraïssé game between \(G_{n,k,S}\) and \(G_{m,k,S}\), both ground-set sizes at least \(qk\). Maintain a bijection \(f:U\longrightarrow V\) between the unions of the chosen \(k\)-subsets in the two ground sets, carrying each previously selected subset exactly onto its corresponding subset. This is true initially with empty unions.

Let Spoiler select any \(k\)-subset \(A\) in one graph; the roles are symmetric. Its intersection \(A\cap U\) must be carried to \(f(A\cap U)\). Write \(r=|A\setminus U|\), with \(0\le r\le k\). As the old union has size at most \(tk\), at least \(qk-tk\ge k\) ground elements remain outside the other union, so choose \(r\) of those fresh elements for the answer subset \(B\). Extend \(f\) by any bijection from \(A\setminus U\) to the fresh elements of \(B\setminus V\). The extended map again carries every previously selected subset and this new subset exactly onto their corresponding subsets. If the selected subset had been played earlier, this construction automatically returns the identical counterpart; if it is new, injectivity ensures the counterpart is new.

After \(q\) rounds the map is a bijection between the underlying unions preserving all selected sets, so corresponding graph vertices are equal exactly in the same cases and all pairwise intersection cardinalities are identical. Since adjacency depends only on these cardinalities, the induced graphs on the selected vertices are isomorphic. Duplicator therefore wins the game. The standard Ehrenfeucht–Fraïssé theorem proves rank-\(q\) equivalence.

**Sharpness.** Take \(S=\{0\}\), so adjacency means disjointness. A clique of size \(q\) is exactly \(q\) pairwise disjoint \(k\)-subsets and hence exists precisely when \(n\ge qk\). The graph at ground-set size \(qk-1\) lacks such a clique, whereas the graph at size \(qk\) has one. The first-order sentence
\[
\exists x_1\cdots\exists x_q\ \bigwedge_{1\le i<j\le q}\bigl(x_i\ne x_j\wedge E(x_i,x_j)\bigr)
\]
has quantifier rank exactly \(q\) and distinguishes them. Both parameters are valid, since \(q\ge2\) implies \(qk-1\ge k\). Thus no strictly smaller uniform ground-set threshold, or corresponding smaller universal vertex-representative bound within this family, is possible.

## Verification
The game invariant gives a fully symbolic verification for all permitted parameters: after \(t\) moves the union uses at most \(tk\) points, and for every \(t<q\) the other domain has at least \(k\) unused points. Each extension uses at most \(k\) points. On completion, equality and every required intersection cardinality are preserved. The sharpness sentence is checked by the pigeonhole principle and an explicit partition of \([qk]\) into \(q\) consecutive \(k\)-blocks. No finite search, computational certificate, or probabilistic approximation is needed for the infinite statement.

## Relationship to prior work
Kneser graphs are a classical instance of intersection-defined graphs. Matoušek and Ziegler study their set representation and topological chromatic bounds, without providing a quantifier-depth stabilization statement in the inspected introduction. Pikhurko and Verbitsky's survey explains finite graph logical depth and Ehrenfeucht games; the inspected relevant section does not give this uniform intersection-scheme cutoff. Previously established specialized rank-three Kneser classifications and a rank-four three-subset Kneser classification agree with the corresponding thresholds but do not imply this all-\(k\), all-\(q\), all-\(S\) statement. The fresh-element proof is elementary, and analogous results may be implicit in standard finite-model-theory folklore; no historical priority beyond the checked sources is claimed.

## Limitations
The theorem is a sharp uniform **eventual** equivalence theorem, not an enumeration of all exceptional rank-\(q\) theories below \(qk\). Its signature excludes counting quantifiers, named ground-set points, and interpretations varying with \(n\). Independent external audit and exhaustive historical-priority verification have not been performed.

## References
- J. Matoušek and G. M. Ziegler, *Topological lower bounds for the chromatic number: A hierarchy*, arXiv:math/0208072, first posted 2002-08-09; introduction and Kneser-graph setup.
- O. Pikhurko and O. Verbitsky, *Logical complexity of graphs: A survey*, arXiv:1003.4865, first posted 2010-03-25; Section 3 on Ehrenfeucht games.
