# Sharp cograph-deletion period and unique optimum for path powers

## Finding

For integers \(n,k\ge 1\), let \(P_n^k\) have vertex set \([n]=\{1,\ldots,n\}\) and an edge \(ij\) exactly when \(0<|i-j|\le k\). A *cograph* is a finite graph containing no induced four-vertex path \(P_4\). Write \(c(G)\) for the greatest size of a vertex set inducing a cograph in \(G\), and \(\tau_{P_4}(G)=|V(G)|-c(G)\) for the minimum number of vertices that must be removed to eliminate all induced four-vertex paths.

**Theorem.** For every \(n,k\ge1\), put \(p=2k+2\), \(b=k+2\), and write \(n=pq+r\), where \(q\ge0\) and \(0\le r<p\). Then
\[
c(P_n^k)=qb+\min\{r,b\},\qquad
\tau_{P_4}(P_n^k)=qk+\max\{0,r-b\}.
\]
Moreover, there is exactly one maximum cograph-inducing vertex subset of \([n]\) if and only if
\[
n\le b\quad\text{or}\quad r=b.
\]
Here uniqueness refers to labelled positions, rather than to isomorphism classes of the induced graphs. The displayed formulas include the cases where \(P_n^k\) is complete or has fewer than four vertices.

## Assumptions and scope

Graphs are finite, undirected, and simple, and the power of a path is defined by its ordinary path metric. The parameter \(k\) need not be smaller than \(n\). A vertex-deletion solution consists solely of removed vertices; no edges are added or removed except those incident to removed vertices. The original indexed vertex set matters for counting optima. The claims are for all positive integer \(n,k\), without asymptotic assumptions.

## Proof

**Local obstruction.** Consider any \(p=2k+2\) consecutive positions \(a,a+1,\ldots,a+2k+1\). Partition them into \(k+1\) opposite pairs
\[
(a+j,a+j+k+1),\qquad 0\le j\le k.
\]
If a chosen subset meets this window in at least \(k+3\) positions, at least two of these pairs are entirely chosen. Let their first coordinates be \(u<v\), so \(1\le v-u\le k\). The four selected positions, ordered as \(u,v,u+k+1,v+k+1\), induce exactly a path on four vertices: its successive gaps are \(v-u\), \(k+1-(v-u)\), and \(v-u\), each between one and \(k\). Its other three gaps are at least \(k+1\), so the three nonconsecutive pairs are nonedges. Thus every cograph-inducing vertex subset contains at most \(b=k+2\) positions in any window of length \(p\). The same upper bound holds on every shorter interval, simply by embedding its positions into a window of length \(p\) with unchosen dummy positions.

**Sharp cardinality.** Partition \([n]\) into \(q\) consecutive full blocks of length \(p\) followed by one residual block of length \(r\). In each full block at most \(b\) vertices may be chosen, and in the residual block at most \(\min\{r,b\}\). Hence \(c(P_n^k)\le qb+\min\{r,b\}\). To attain equality, choose exactly the first \(b\) positions from each full block and the first \(\min\{r,b\}\) positions from the residual block. The resulting zero-one indicator is a concatenation of full patterns \(1^b0^k\) followed by \(1^{\min\{r,b\}}0^{r-\min\{r,b\}}\). Every chosen run has length at most \(k+2\), and any two chosen runs are separated by \(k\) or more unchosen positions, so there are no graph edges between distinct runs. Inside a run of at most \(k+1\) consecutive vertices the induced graph is complete. A run of length \(k+2\) induces a complete graph with the edge between its endpoints removed; it is also \(P_4\)-free (every four-vertex induced subgraph has more than three edges, apart from the three-vertex boundary). A disjoint union of cographs is a cograph. This attains the upper bound and establishes both cardinality identities.

**Uniqueness when \(r=b\).** Let \(n=pq+b\). The upper bound for the partition into \(q\) full blocks and the last \(b\) positions can be an equality only if the last \(b\) positions are all chosen. Suppose there were a chosen vertex \(u\) among the preceding \(k\) positions. Write the first chosen suffix position as \(s=n-b+1\), so \(s-k\le u<s\). Then \((u,s,s+k+1-(s-u),s+k+1)\) are four chosen positions inducing a \(P_4\): the three successive gaps are \(s-u\), \(k+1-(s-u)\), and \(s-u\), while all skipped gaps exceed \(k\). Consequently the \(k\) positions before the final selected run must be unchosen. Since every preceding full block must contain exactly \(b\) chosen positions to achieve the optimal total, the preceding \(b\) positions are then all chosen. Repeating the argument backwards through every full block forces precisely the pattern \((1^b0^k)^q1^b\). Thus the optimum is unique for \(r=b\). If \(n\le b\), the entire graph is itself a cograph, and the sole maximum subset is all \(n\) vertices.

**Nonuniqueness in all other cases.** Suppose \(n>b\). If \(r>b\), the sharp construction has at least one unchosen position at the right boundary. Shifting all its chosen positions one place to the right produces a second, distinct maximum cograph-inducing set. If \(r<b\), then \(q\ge1\) because \(n>b\) and \(r<b\). Both patterns
\[
(1^b0^k)^q1^r\qquad\text{and}\qquad 1^r(0^k1^b)^q
\]
have length \(n\), attain the same sharp cardinality, and induce disjoint unions of cographs by the construction argument. They are distinct since \(r<b\); the case \(r=0\) is included. This exhausts the remaining residues and completes the theorem.

## Verification

The accompanying standalone `verify_cograph.py` implements two separate finite tests of the theorem. A direct routine enumerates every vertex subset, independently builds every induced four-vertex graph from adjacency, and checks both the maximum cardinality and whether exactly one maximizing subset exists. A separate finite-state dynamic program uses only the previous \(3k\) positions to reject newly completed induced four-vertex paths. Finally an independent constructor checks the explicit family of witnesses.

Running `python3 verify_cograph.py` prints exactly `VERIFY_OK direct=91 finite_state=216 witness=456`: direct enumeration covers \(1\le k\le7\), \(1\le n\le13\); finite-state checks cover \(1\le k\le4\), \(1\le n\le54\); and witness checks cover \(1\le k\le12\), \(1\le n\le38\). These finite checks test calculations and boundary cases; the local-window and uniqueness arguments above prove the infinite statements.

## Relationship to prior work

Path powers are standard unit interval graphs, also called *ribbons* in the work of Markenzon and Waga (2014). Their Theorem 8 proves two-subcolorability by partitioning a ribbon into two classes, each inducing a disjoint union of cliques. This guarantees the existence of a cograph containing at least half the vertices, but neither specifies the maximum order of a cograph subset, nor determines all residues where the maximum subset is unique. The sharp formula here allows a selected run of length \(k+2\), which is generally a clique minus an edge rather than a cluster graph, and yields a sharper extremal value.

Alexandersson and Leite (2026) investigate new peak-clique and peak-nesting statistics and enumerative polynomials of unit interval graphs. Those graph-statistic results concern different objects from deletion of vertices to the \(P_4\)-free class. The present theorem addresses a distinct extremal question within a canonical unit interval family. Searches for equivalent formulas using the terms path power, ribbon, cograph, induced four-vertex path, and vertex deletion did not identify a prior symbolic classification; negative searches do not certify absolute historical novelty.

## Limitations

This theorem concerns only powers of paths, not all unit interval graphs, all interval graphs, or powers of arbitrary trees. It determines maximum cardinality and exactly when the maximizing subset is unique, but does not count *all* maximizing subsets in the nonunique cases. The uniqueness argument is for indexed subsets of \([n]\). A comprehensive independent historical-priority audit has not been performed.

## References

1. P. Alexandersson and L. S. M. Leite, *Peaks and peak-nestings on unit interval graphs*, arXiv:2609.38084v1, publicly posted 2026-09-29. https://arxiv.org/abs/2609.38084
2. L. Markenzon and C. F. E. M. Waga, *Generalizating path and fan graphs: subcoloring and toughness*, Pesquisa Operacional 34 (2014), 107–116. DOI:10.1590/S0101-74382014005000004. https://www.scielo.br/j/pope/a/6wzkB9yCGyDxDwdq7FgYY9v/?lang=en
