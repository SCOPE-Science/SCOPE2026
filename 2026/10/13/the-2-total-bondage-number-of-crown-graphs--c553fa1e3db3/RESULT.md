# The 2-total bondage number of crown graphs
## Finding
For every integer \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\) have bipartition classes
\[
A=\{a_1,\ldots,a_n\},\qquad B=\{b_1,\ldots,b_n\},
\]
where \(a_i b_i\) is the deleted perfect-matching edge for every \(i\). For a graph without isolated vertices, let \(\gamma_t\) denote total domination number, and let \(b_t^2(G)\) be the minimum number of edges whose deletion leaves no isolated vertices and increases \(\gamma_t\) by at least \(2\). Then
\[
\gamma_t(\operatorname{Cr}_n)=4,
\qquad
b_t^2(\operatorname{Cr}_n)=2n-3.
\]
More strongly, if \(F\subseteq E(\operatorname{Cr}_n)\), \(|F|\le 2n-4\), and \(\operatorname{Cr}_n-F\) has no isolated vertices, then \(\gamma_t(\operatorname{Cr}_n-F)=4\). On the other hand, for any distinct indices \(r,c\), deleting
\[
F_{r,c}=\{a_r b_j:j\notin\{r,c\}\}\cup
\{a_i b_c:i\notin\{r,c\}\}\cup\{a_c b_r\}
\]
gives \(|F_{r,c}|=2n-3\), leaves no isolated vertices, and yields total domination number exactly \(6\).

## Assumptions and scope
All graphs are finite and simple. A total dominating set \(D\) satisfies that every vertex has a neighbor in \(D\). For a bipartite graph \(H=(A,B;E)\) without isolated vertices, write \(\tau_A(H)\) for the minimum size of a subset of \(A\) that dominates all of \(B\), and define \(\tau_B(H)\) symmetrically. Then
\[
\gamma_t(H)=\tau_A(H)+\tau_B(H),
\]
because the two shores of a total dominating set must independently dominate the opposite shores, and conversely the union of such two shore-dominating sets is total dominating.

For the crown graph, one vertex from either shore cannot dominate the opposite shore because of its missing matched edge, while any two distinct vertices from one shore dominate the opposite shore. Hence \(\tau_A(\operatorname{Cr}_n)=\tau_B(\operatorname{Cr}_n)=2\), proving \(\gamma_t(\operatorname{Cr}_n)=4\).

## Proof
We first prove a set-system lemma.

**Pair-cover lemma.** Let \(S_1,\ldots,S_n\) be proper subsets of \([n]\) such that \(j\in S_j\) for every \(j\). If every two-element subset of \([n]\) is contained in at least one \(S_j\), then
\[
\sum_{j=1}^n (|S_j|-1)\ge 2n-3.
\]

For each point \(x\in[n]\), let \(r_x\) be the number of sets containing \(x\). Since \(S_x\) is proper, choose \(y\notin S_x\). The pair \(\{x,y\}\) must lie in some set other than \(S_x\), so \(r_x\ge2\). If every \(r_x\ge3\), then \(\sum_j|S_j|\ge3n\), which is stronger than required.

Otherwise choose \(x\) with \(r_x=2\), and call the two sets containing it \(P\) and \(Q\). Every other point must share a set with \(x\), so \(P\cup Q=[n]\). Both sets are proper, hence \(X=P\setminus Q\) and \(Y=Q\setminus P\) are nonempty. Put \(c=|P\cap Q|\), so \(|X\cup Y|=n-c\). A pair with one endpoint in \(X\) and the other in \(Y\) is contained in neither \(P\) nor \(Q\), so the remaining \(n-2\) sets cover every edge of the complete bipartite graph between \(X\) and \(Y\).

Intersect those remaining sets with \(U=X\cup Y\). The union of the corresponding clique graphs is connected on \(U\), because it contains the connected complete bipartite graph between \(X\) and \(Y\). A clique on \(q\) vertices contributes graphic rank at most \(q-1\); therefore connectivity forces
\[
\sum_R \max\{|R\cap U|-1,0\}\ge |U|-1=n-c-1,
\]
where the sum is over the remaining sets. Since \(|R|-1\ge\max\{|R\cap U|-1,0\}\), their total contribution is at least \(n-c-1\). Also \(|P|+|Q|=n+c\). Thus
\[

y\sum_{j=1}^n(|S_j|-1)
\ge (n+c-2)+(n-c-1)=2n-3.
\]
We now apply the lemma to edge deletions. Let \(H=\operatorname{Cr}_n-F\) have no isolated vertices. For each \(b_j\), define its nonneighbor-index set in \(A\) by
\[
S_j=\{j\}\cup\{i\ne j:a_i b_j\in F\}.
\]
Because \(b_j\) is not isolated, \(S_j\) is proper, and
\[
|F|=\sum_{j=1}^n(|S_j|-1).
\]
A pair \(\{a_p,a_q\}\) fails to dominate \(B\) exactly when \(\{p,q\}\subseteq S_j\) for some \(j\). Therefore, if no pair from \(A\) dominates \(B\), the family \(S_1,\ldots,S_n\) covers every two-element subset of \([n]\), and the pair-cover lemma gives \(|F|\ge2n-3\). Applying the same argument after transposing the bipartition gives the identical conclusion if no pair from \(B\) dominates \(A\).

Hence when \(|F|\le2n-4\), each shore contains a dominating pair for the opposite shore. Since one vertex from a shore can never dominate its matched opposite vertex in a subgraph of the crown, both shore domination numbers remain exactly \(2\). Thus \(\gamma_t(H)=4\). This proves the lower bound \(b_t^2(\operatorname{Cr}_n)\ge2n-3\).

For the upper bound, fix distinct \(r,c\) and use \(F_{r,c}\) from the finding. The vertices \(a_r\) and \(b_c\) each retain exactly their mutual edge, while every other vertex retains at least one edge, so no isolate is created. For domination from \(A\) to \(B\), the nonneighbor sets are
\[
S_c=[n]\setminus\{r\},\qquad S_r=\{r,c\},\qquad S_j=\{r,j\}\quad(j\notin\{r,c\}).
\]
Every pair of indices is contained in one of these sets, so no two vertices of \(A\) dominate \(B\). If \(x\notin\{r,c\}\), however, \(\{a_r,a_c,a_x\}\) does dominate all of \(B\). Hence \(\tau_A(H)=3\). By the transposed construction, \(\tau_B(H)=3\), with \(\{b_c,b_r,b_x\}\) as an explicit dominating triple. Consequently \(\gamma_t(H)=6\), proving \(b_t^2(\operatorname{Cr}_n)\le2n-3\) and completing the proof.

## Verification
The proof above is analytic for every \(n\ge3\). The accompanying checker is corroborative rather than a substitute for the proof. It independently enumerates every no-isolate edge-deletion set below the claimed threshold for \(n=3,4\), exhausts the pair-cover lemma for \(n=3,4\), and checks the explicit extremal construction for every \(3\le n\le40\). Its recorded output is `ALL CHECKS PASSED`.

## Relationship to prior work
Appel, Fischberg, Kelley, Shank, and Sosis introduced the \(k\)-total bondage number in arXiv:2506.07000v1. Their complete-bipartite theorem gives
\[
b_t^2(K_{a,b})=b\qquad(2\le a\le b\le2a),
\]
so in particular \(b_t^2(K_{n,n})=n\). Their inspected full text contains no crown-graph or matching-deletion theorem. The present result shows that deleting one perfect matching from \(K_{n,n}\) changes the exact second-level threshold from \(n\) to \(2n-3\).

Targeted searches also considered the aliases “crown graph”, “\(K_{n,n}-M_n\)”, “matching-deleted complete bipartite graph”, “2-total bondage”, and ordinary total bondage. No located statement implies the exact \(2\)-total bondage formula above. A prior exact ordinary-total-bondage result for crowns supplies at most the monotonic lower-bound direction for the new invariant; it does not supply an edge deletion that raises \(\gamma_t\) by two. The upper construction and the exact \(\gamma_t=6\) analysis are therefore essential to the present claim.

## Limitations
The theorem determines only the \(2\)-total bondage number. It does not classify every optimal deletion set, and it makes no assertion about \(b_t^k(\operatorname{Cr}_n)\) for \(k\ge3\). The literature search cannot exclude a poorly indexed equivalent result under unusual terminology; this remains the principal originality risk. Finite verification covers only the stated bounded test ranges and is not used to justify the infinite theorem.

## References
1. J.-P. Appel, G. Fischberg, K. Kelley, N. Shank, and E. Sosis, *The k-Total Bondage Number of a Graph*, arXiv:2506.07000v1, first public 2025-06-08. Primary MSC 05C69.
