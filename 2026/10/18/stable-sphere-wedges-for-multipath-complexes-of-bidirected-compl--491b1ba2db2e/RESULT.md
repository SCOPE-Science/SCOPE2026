# Stable sphere wedges for multipath complexes of bidirected complete bipartite graphs

## Finding
For every integer \(n\ge7\), replace both directions of each edge of the undirected complete bipartite graph \(K_{2,n}\) by directed arcs, obtaining \(G_n\). Its multipath complex, denoted \(X_n\), consists of subsets of directed arcs which form vertex-disjoint simple directed paths, allowing isolated vertices. Then
\[
X_n\simeq\bigvee^{R(n)}S^3,
\qquad R(n)=n^4-8n^3+19n^2-14n+1.
\]
Consequently, \(\widetilde H_k(X_n;\mathbb Z)=0\) for \(k\ne3\) and \(\widetilde H_3(X_n;\mathbb Z)\cong\mathbb Z^{R(n)}\). The first stable instances have \(R(7)=491\), \(R(8)=1105\), and \(R(9)=2143\). No assertion about the homotopy type for smaller values is needed.

## Assumptions and scope
Write the two hub vertices as \(a,b\), and the leaf vertices as \(x_1,\ldots,x_n\). For each index \(i\), introduce four arc vertices
\[
P_i=(a\to x_i),\quad Q_i=(x_i\to b),\quad
R_i=(b\to x_i),\quad S_i=(x_i\to a).
\]
A set of such arcs is a face precisely when every graph vertex has selected indegree and outdegree at most one and the selected digraph has no directed cycles. Since each of the two hubs supports at most one selected incoming and at most one selected outgoing arc, every multipath has at most four selected arcs. Hence \(X_n\) has dimension at most three. We work with ordinary, unaugmented geometric realizations and integral homology. Here \(\Delta_{4,n}\) is the ordinary four-row, \(n\)-column chessboard complex: its faces are sets of rook positions with no repeated row or column.

## Proof
**1. Identify a canonical chessboard subcomplex.** Declare the four arc kinds \(P,Q,R,S\) to be rows and the leaf index to be the column. Any selection using distinct rows and distinct columns is automatically a directed multipath: hub indegrees and outdegrees are bounded by one; every leaf has at most one incident arc; and a directed cycle requires a leaf with both a selected incoming and outgoing arc. Thus the collection \(A_n\) of all such faces is exactly \(\Delta_{4,n}\).

**2. Classify every face outside the chessboard.** A selected leaf can be incident with two arcs only if one enters and one leaves it. Of the four arc kinds, this gives precisely two admissible two-arc paths,
\[
e_i^+=(P_i,Q_i)\quad\text{and}\quad e_i^-=(R_i,S_i).
\]
The other choices using the same column either give indegree/outdegree two at that leaf or form a directed two-cycle between a leaf and a hub. We call \(e_i^+\) and \(e_i^-\) bent edges. Any multipath containing a bent edge cannot contain another bent edge: two with the same orientation violate a hub indegree/outdegree constraint; two with opposite orientations, if otherwise compatible, close a directed four-cycle. Therefore every non-chessboard face contains **exactly one** bent edge.

**3. Compute the bent-edge links.** Fix \(e_i^+=(P_i,Q_i)\), a directed path \(a\to x_i\to b\). The additional allowable single arcs are precisely \(R_j=(b\to x_j)\) and \(S_k=(x_k\to a)\) with \(j,k\ne i\). A simultaneous choice \(R_j,S_k\) is allowed exactly when \(j\ne k\); equality would close a directed four-cycle. No three additional arcs can coexist. Thus the link \(L_i^+\) is the crown graph \(K_{n-1,n-1}\) with the diagonal perfect matching removed. By reversing all arcs the same holds for \(L_i^-\). For \(n\ge7\), these are connected graphs, each with
\[
\lvert V(L_i^\pm)\rvert=2(n-1),\qquad
\lvert E(L_i^\pm)\rvert=(n-1)(n-2).
\]
Hence each \(L_i^\pm\) has cyclomatic number
\[
c(n)=(n-1)(n-2)-2(n-1)+1=n^2-5n+5,
\]
and is homotopy equivalent to a wedge of \(c(n)\) circles.

**4. Attach the extra faces to the chessboard.** The closed star of every bent edge is \(B_i^\pm=e_i^\pm*L_i^\pm\), the join of a one-simplex with its crown-graph link. The intersection with \(A_n\) is exactly
\[
B_i^\pm\cap A_n=(\partial e_i^\pm)*L_i^\pm\cong\Sigma L_i^\pm.
\]
To see equality, a face in the closed star not containing both endpoints of the bent edge has no repeated column, so lies in the chessboard; conversely every such boundary face is permitted. Any two closed stars for distinct bent edges intersect only inside \(A_n\), by Step 2. Therefore \(X_n\) is obtained from \(A_n\) by attaching, along the \(2n\) indicated suspensions, the contractible complexes \(B_i^\pm\). Since \(e_i^\pm*L_i^\pm\) is a cone on its boundary suspension, this is a collection of ordinary mapping-cone attachments. Every inclusion is a simplicial cofibration.

**5. Nullhomotopy and wedge decomposition.** Ziegler's vertex-decomposability theorem for chessboard complexes gives vertex decomposability, hence pure shellability, of \(\Delta_{m,n}\) whenever \(n\ge2m-1\). For \(m=4\) and \(n\ge7\), \(A_n\) is a three-dimensional wedge of three-spheres. In particular \(\pi_2(A_n)=0\). Each attaching domain \(\Sigma L_i^\pm\) is a wedge of two-spheres, so its attaching map to \(A_n\) is nullhomotopic. Attaching a cone along a nullhomotopic map from a connected suspension adds its suspension as a wedge summand. Iterating through the \(2n\) stars (their pairwise overlap is in \(A_n\)) yields
\[
X_n\simeq A_n\vee\bigvee_{i=1}^n
 \bigl(\Sigma^2L_i^+\vee\Sigma^2L_i^-\bigr)
\simeq A_n\vee\bigvee^{2n c(n)}S^3.
\]
Here suspensions are understood as reduced suspensions up to homotopy after choosing basepoints; all relevant links are connected.

**6. Count the spheres.** The four-row chessboard complex has \(k\)-simplices numbered \(\binom4{k+1}(n)_{k+1}\), for \(0\le k\le3\), with \((n)_j=n(n-1)\cdots(n-j+1)\). Its reduced Euler characteristic is \(-r(n)\), where
\[
r(n)=n^4-10n^3+29n^2-24n+1.
\]
As \(A_n\simeq\bigvee^{r(n)}S^3\), its three-sphere count is exactly \(r(n)\). Thus
\[
R(n)=r(n)+2n c(n)
=n^4-8n^3+19n^2-14n+1.
\]
The integral homology statement follows immediately from the displayed homotopy equivalence, completing the proof.

## Verification
The standalone standard-library program `verify_bidirected_multipath.py` independently enumerates **all** directed-arc subsets of sizes one through four for \(4\le n\le9\), directly checks path constraints and directed cycles, computes face numbers, and performs exact bitwise Gaussian elimination over \(\mathbb F_2\). For \(n=7,8,9\) its Betti vectors \((b_0,b_1,b_2,b_3)\) are \((1,0,0,491)\), \((1,0,0,1105)\), and \((1,0,0,2143)\). The results are recorded in `verify_output.txt`. These finite calculations corroborate but do not replace the unrestricted homotopy proof.

The general face-count cross-check is
\[
(f_0,f_1,f_2,f_3)=
\bigl(4n,\ 6n^2-4n,\ 4n(n-1)^2,\ n(n-1)^2(n-2)\bigr).
\]
It follows either by classifying the bent-edge stars or by direct finite counting and is consistent with the Euler characteristic and claimed sphere rank.

## Relationship to prior work
Caputi, Collari, Di Trani and Smith define multipath complexes and treat several graph families, including *one-way* orientations of complete bipartite graphs in their complete-bipartite section. Their assertions for source-to-sink orientations do not imply the result for a symmetric digraph having two opposite arcs on each edge. Caputi, Collari and Smith's January 2026 work studies bidirectional linear graphs and bidirectional polygons, rather than these bidirected bicliques. Ziegler's result is invoked **only** for the known chessboard subcomplex; it does not identify the additional bent-edge stars or their null attachments. The novelty asserted here is the unrestricted \(n\ge7\) decomposition of the bidirected \(K_{2,n}\) multipath complex, not shellability of chessboard complexes themselves.

## Limitations
The theorem concerns precisely two hub vertices, every spoke oriented in both directions, and integers \(n\ge7\). It makes no homotopy claim for other orientations, higher numbers of hubs, or \(n<7\). The proof does not establish a natural equivariant splitting under all graph automorphisms; the non-equivariant integral homotopy classification is the complete claim. Finite computational agreement alone would not establish this homotopy statement. Bibliographic overlap with work not accessible or indexed remains possible.

## References
1. L. Caputi, C. Collari, J. P. Smith, *Multipath complexes of bidirectional polygonal digraphs*, arXiv:2601.05670v1 (first posted 2026-01-09), Sections 1 and 2. https://arxiv.org/html/2601.05670v1
2. L. Caputi, C. Collari, S. Di Trani, J. P. Smith, *On the homotopy type of multipath complexes*, arXiv:2208.04656v1 (first posted 2022-08-09), especially the complete-bipartite section. https://arxiv.org/abs/2208.04656
3. G. M. Ziegler, *Shellability of chessboard complexes*, Israel Journal of Mathematics **87** (1994), 97–110, DOI:10.1007/BF02772986; vertex-decomposability theorem for \(n\ge2m-1\). https://doi.org/10.1007/BF02772986
