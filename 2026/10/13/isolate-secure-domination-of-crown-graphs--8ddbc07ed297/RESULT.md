# Isolate secure domination of crown graphs
## Finding
For every integer \(n\ge4\), let
\[
\operatorname{Cr}_n=K_{n,n}-M
\]
be the crown graph with bipartition
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where
\[
M=\{a_i b_i:1\le i\le n\}
\]
is the deleted perfect matching.

Then the isolate secure dominating sets of \(\operatorname{Cr}_n\) are exactly
\[
A\quad\text{and}\quad B.
\]
Hence
\[
\gamma_{0s}(\operatorname{Cr}_n)=n,
\]
and there are exactly two minimum isolate secure dominating sets.

Thus deleting one perfect matching from \(K_{n,n}\) changes isolate secure domination from nonexistence, as established for complete bipartite graphs in the initiating paper, to a rigid two-set family.

## Assumptions and scope
An isolate dominating set \(S\) is a dominating set for which the induced graph \(G[S]\) has at least one isolated vertex. An isolate secure dominating set \(S\) is an isolate dominating set such that for every
\[
u\in V(G)\setminus S
\]
there is a neighbor \(v\in S\cap N(u)\) for which
\[
(S\setminus\{v\})\cup\{u\}
\]
is again an isolate dominating set.

The isolate secure domination number \(\gamma_{0s}(G)\) is the minimum cardinality of an isolate secure dominating set.

The theorem is stated for \(n\ge4\). The boundary \(\operatorname{Cr}_3\) has isolate secure domination number \(3\) but has fourteen isolate secure dominating sets, so the rigidity statement starts exactly at \(n=4\).

## Proof
First, \(A\) is an isolate secure dominating set. It is independent and dominating. For an attacked vertex \(b_i\), choose any
\[
a_j\in A,\qquad j\ne i,
\]
and replace \(a_j\) by \(b_i\). The resulting set is
\[
T=(A\setminus\{a_j\})\cup\{b_i\}.
\]
The removed vertex \(a_j\) is dominated by \(b_i\). Every unselected \(b_k\), with \(k\ne i\), has a selected neighbor in \(A\setminus\{a_j\}\), because \(n\ge4\) leaves a selected index different from both \(j\) and \(k\). Finally, \(a_i\) remains selected and is nonadjacent to \(b_i\), so \(a_i\) is isolated in the induced graph on \(T\). Hence \(T\) is an isolate dominating set. Thus \(A\) is isolate secure, and by symmetry so is \(B\).

Now let \(S\) be any isolate secure dominating set. Since \(S\) is an isolate dominating set, \(G[S]\) has an isolated vertex. By symmetry suppose that vertex is \(a_i\).

Because \(a_i\) is adjacent to every vertex of \(B\) except \(b_i\), isolation of \(a_i\) forces
\[
S\cap B\subseteq\{b_i\}.
\tag{1}
\]

Suppose first that \(b_i\notin S\). Then \(S\subseteq A\). If some \(a_j\notin S\), that vertex has no neighbor in \(S\), because \(A\) is independent. This contradicts domination. Therefore
\[
S=A.
\tag{2}
\]

It remains to rule out \(b_i\in S\). Put
\[
P=S\cap A.
\]
Then \(a_i\in P\).

If some \(a_j\notin P\), then \(j\ne i\). The attacked vertex \(a_j\) has only one selected neighbor, namely \(b_i\). Security therefore forces the swap
\[
T=(S\setminus\{b_i\})\cup\{a_j\}=P\cup\{a_j\}.
\]
This set lies entirely in \(A\). For it to dominate, every vertex of \(A\) must belong to it. Consequently
\[
P=A\setminus\{a_j\},
\tag{3}
\]
so \(a_j\) is the unique missing vertex of \(A\).

Now attack \(b_j\). Every possible defender lies in \(P\). Removing any defender \(a_k\in P\) gives
\[
T_k=(A\setminus\{a_j,a_k\})\cup\{b_i,b_j\}.
\]
Since \(n\ge4\), at least two vertices from \(A\) remain selected. Every selected \(a_\ell\) is adjacent to \(b_j\), because \(a_j\) is absent. The vertex \(b_j\) is adjacent to every remaining selected \(A\)-vertex, while \(b_i\) is adjacent to all but possibly \(a_i\), and at least one further \(A\)-vertex remains. Thus every selected vertex in \(T_k\) has a selected neighbor. Hence \(G[T_k]\) has no isolated vertex. No defender can make the swap isolate dominating, a contradiction.

Therefore no \(a_j\) is missing and \(P=A\), so
\[
S=A\cup\{b_i\}.
\]
Choose \(j\ne i\) and attack \(b_j\). A defender is some \(a_k\ne a_j\). After swapping, the selected set contains \(b_i,b_j\) and all vertices of \(A\) except \(a_k\). Every selected \(A\)-vertex has a selected neighbor among \(b_i,b_j\): \(a_i\) sees \(b_j\), \(a_j\) sees \(b_i\), and every other selected \(a_\ell\) sees both. The two selected \(B\)-vertices also have selected neighbors in \(A\) because \(n\ge4\). Thus the swapped set again has no isolated vertex, contradicting security.

Hence \(b_i\in S\) is impossible. Every isolate secure dominating set with an isolated vertex in \(A\) is exactly \(A\). The symmetric argument gives \(B\) when an isolated selected vertex lies in \(B\). Therefore \(A\) and \(B\) are the only isolate secure dominating sets.

## Verification
The included verifier evaluates the definitions directly.

For every \(3\le n\le7\), it exhausts every nonempty subset of the \(2n\)-vertex crown graph, tests domination, tests for an isolated selected vertex, and for each outside vertex tests all possible defending swaps.

It checks
\[
21{,}819
\]
subsets in total. For \(n=4,5,6,7\), exactly two isolate secure dominating sets occur, namely the two bipartition classes. For the boundary \(n=3\), there are fourteen isolate secure dominating sets and the minimum size is \(3\).

The verifier also directly checks that both bipartition classes are isolate secure for every
\[
4\le n\le50.
\]

## Relationship to prior work
The initiating paper on isolate secure domination defines the same swap-preserving isolate-domination condition and explicitly states that complete bipartite graphs admit no isolate secure dominating set. It then gives exact values for paths and cycles and studies computational complexity on bipartite and split graphs.

The crown graph is obtained from the complete bipartite graph by deleting a perfect matching. The theorem therefore identifies a sharp structural boundary: this symmetric edge deletion changes the invariant from nonexistence to existence, but in an extremely rigid way—only the two bipartition classes survive.

The initiating full text contains no crown-graph treatment. Targeted indexed-literature searches under crown graph, complete bipartite minus a perfect matching, and isolate secure domination did not locate a statement implying this classification. Results for ordinary secure domination, secure total domination, restrained domination, and other crown-graph invariants use different feasibility conditions and do not imply the theorem.

## Limitations
The all-set classification begins at \(n=4\). The graph \(\operatorname{Cr}_3\) has the same minimum cardinality \(3\), but additional isolate secure dominating sets occur.

The theorem concerns the exact perfect-matching deletion \(K_{n,n}-M\); it does not classify isolate secure domination under arbitrary edge deletions from complete bipartite graphs.

Finite enumeration is corroborative only. The arbitrary-order theorem follows from the isolated-vertex and forced-swap argument above.

Search coverage cannot exclude a differently phrased or non-indexed treatment of the same crown family.

## References
1. J. Pavan Kumar and P. Venkata Subba Reddy, “Algorithmic Complexity of Isolate Secure Domination in Graphs,” arXiv:2002.05538v1, first public version 12 February 2020; later published in TWMS Journal of Applied and Engineering Mathematics 11(Special Issue) (2021), 188–194.
