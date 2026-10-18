# Cograph-induced-subgraph profiles of matching-deleted bicliques

## Finding

Let \(a,b\ge 1\) be integers and let \(0\le t\le\min(a,b)\). From \(K_{a,b}\), delete a matching of size \(t\); denote the resulting graph by \(G_{a,b,t}\). Its two classes are \(A\) and \(B\), and the deleted matching consists of \(A_iB_i\) for \(1\le i\le t\). A **cograph** is a graph with no *induced* four-vertex path \(P_4\). Define the full two-variable induced-cograph polynomial by

\[
C_{a,b,t}(u,v)=\sum_{S\subseteq V(G_{a,b,t})\,:\,G_{a,b,t}[S]\text{ is a cograph}}u^{|S\cap A|}v^{|S\cap B|}.
\]

For all indicated parameters,

\[
\boxed{C_{a,b,t}(u,v)=(1+u+v)^t(1+u)^{a-t}(1+v)^{b-t}
+tuv\big((1+u)^{a-1}+(1+v)^{b-1}-1\big)+\binom{t}{2}u^2v^2.}
\tag{1}
\]

For \(a,b\ge3\) and \(0\le t<\min(a,b)\), deleting one *additional disjoint* edge never increases any coefficient:

\[
\boxed{C_{a,b,t}(u,v)\succeq C_{a,b,t+1}(u,v).}
\tag{2}
\]

Here \(P\succeq Q\) means coefficientwise inequality, not evaluation at particular \(u,v\). The two polynomials in (2) are unequal except for \((a,b,t)=(3,3,2)\), where they coincide.

For the **crown graph** \(H_n=G_{n,n,n}\) with \(n\ge3\), the polynomial enumerating inclusion-maximal vertex subsets inducing cographs is

\[
\boxed{\mathcal M_n(u,v)=\sum_{r=2}^{n-2}\binom nr u^rv^{n-r}
+nuv^n+nu^nv+\binom n2u^2v^2.}
\tag{3}
\]

An empty sum is zero. Substitution \(u=v=z\) gives

\[
\mathcal M_n(z,z)=(2^n-2n-2)z^n+2nz^{n+1}+\binom n2z^4.
\tag{4}
\]

Thus the maximum induced cograph has \(n+1\) vertices, and the minimum number of vertex deletions needed to obtain a cograph is \(n-1\). For \(n\ge4\), precisely \(2n\) deletion sets attain this minimum; for \(n=3\), there are nine. For \(n\ge6\), the possible sizes of inclusion-maximal induced cographs are precisely \(4,n,n+1\), leaving the consecutive missing sizes \(5,6,\ldots,n-1\) (exactly \(n-5\) missing values). The cograph-subset simplicial complex of \(H_n\) is pure exactly for \(n=3\).

## Assumptions and scope

Graphs are finite, simple, undirected and labeled. An induced \(P_4\) has exactly three edges arranged in a chordless path; it is distinct from a non-induced path. The empty vertex set is a cograph, and its contribution to (1) is one. A cograph vertex-deletion set is the complement of an induced-cograph vertex set. Inclusion-minimal deletion sets therefore correspond bijectively to inclusion-maximal induced-cograph sets. No assertions are made about edge-deletion instead of vertex-deletion, or about induced \(P_4\)-free *edge* subsets.

## Proof

**1. Classification of all inducing vertex subsets.** Represent selected vertices as index sets \(X\subseteq\{1,\ldots,a\}\) and \(Y\subseteq\{1,\ldots,b\}\). The shared deleted-matching index set is \(I=X\cap Y\cap\{1,\ldots,t\}\). If \(I=\varnothing\), all cross-edges among selected vertices exist, and the induced subgraph is complete bipartite, hence a cograph.

Conversely, an induced \(P_4\) in a bipartite graph has its endpoints in opposite classes. Since the endpoints must be nonadjacent, and the only absent cross-edges in \(G_{a,b,t}\) are the \(t\) deleted matching edges, any induced \(P_4\) has the form

\[
A_i-B_j-A_k-B_i,
\qquad i\in I,\quad k\in X\setminus\{i\},\quad j\in Y\setminus\{i\},
\]

where \(k\ne j\). Indeed, the other required cross-edges exist precisely when \(k\ne i\), \(j\ne i\), and \(k\ne j\); the same index equality \(k=j\) can only suppress an edge if it is itself a matched index at most \(t\). If one side has just one selected vertex, no \(P_4\) exists. If both sides have at least two selected vertices and \(I\ne\varnothing\), fixing \(i\in I\) shows that no such path exists exactly when both \(X\setminus\{i\}\) and \(Y\setminus\{i\}\) consist of the *same single other matched index* \(j\). This forces \(X=Y=\{i,j\}\subseteq\{1,\ldots,t\}\); conversely the four selected vertices then induce two independent edges. Therefore **exactly three disjoint types** are cographs: (i) \(I=\varnothing\); (ii) \(I\ne\varnothing\) and at least one selected class has size one; (iii) \(X=Y=\{i,j\}\subseteq[t]\), with \(i\ne j\).

**2. Enumeration.** Type (i) contributes \((1+u+v)^t(1+u)^{a-t}(1+v)^{b-t}\), as each deleted matched pair allows neither endpoint or either one, and all other vertices are independently optional. In type (ii), choosing its unique selected left vertex at a deleted matched index gives \(tuv(1+v)^{b-1}\); the reversed choice gives \(tuv(1+u)^{a-1}\). Their common configurations (one selected deleted pair and no other vertices) have total weight \(tuv\) and must be subtracted once. Type (iii) contributes \(\binom t2u^2v^2\). This proves (1), including all boundary cases \(t=0\), \(a=1\), or \(b=1\).

**3. Coefficientwise comparison.** Subtract (1) for consecutive matching sizes. A direct factorization yields

\[
C_{a,b,t}-C_{a,b,t+1}
=uv\left[(1+u+v)^t(1+u)^{a-t-1}(1+v)^{b-t-1}
-(1+u)^{a-1}-(1+v)^{b-1}+1-tuv\right].
\tag{5}
\]

Put \(Q=(1+u+v)^t(1+u)^{a-t-1}(1+v)^{b-t-1}\). This counts two independently chosen subsets from classes of sizes \(a-1,b-1\), with simultaneous selection forbidden on \(t\) designated matched pairs. The terms \(Q-(1+u)^{a-1}-(1+v)^{b-1}+1\) count exactly selections using at least one vertex from **each** class. Every coefficient is nonnegative. The coefficient of \(uv\) therein equals \((a-1)(b-1)-t\); after subtracting the extra \(tuv\) in (5), it is \((a-1)(b-1)-2t\). As \(a,b\ge3\) and \(t\le\min(a,b)-1\), this number is nonnegative. It vanishes only if \(a=b=3\) and \(t=2\); in that exceptional case, \(Q=(1+u+v)^2\) and the entire bracket in (5) is identically zero. In every other case, its \(uv\) coefficient is positive, establishing (2) and its exact equality case. Notice that this comparison is not a consequence of ordinary graph-edge monotonicity: deleting an edge can both create and destroy an induced path.

**4. Inclusion-maximal cographs of a crown.** Set \(a=b=t=n\ge3\). In type (i), \(X\cap Y=\varnothing\). If some index belongs to neither \(X\) nor \(Y\), that index can be added to either class without producing a shared index; hence maximality requires \(X\cup Y=[n]\). If either part is empty, or one part has size one, one can add the opposite endpoint of a chosen matching pair and remain in type (ii). If both parts have size at least two, every added vertex produces shared-index overlap with one part now of size at least three. Such a set is neither type (ii) nor type (iii), so these and only these partitions are maximal.

In type (ii), suppose the left class consists of one selected vertex \(A_i\), and the right class contains \(B_i\). The set is extendible unless every right vertex is selected. With all \(n\) right vertices selected, adding any left vertex creates an induced \(P_4\) because the left class then has size two and the right class has at least three. This gives \(n\) maximal sets with occupancies \((1,n)\) and \(n\) with \((n,1)\). Finally, each type (iii) set is maximal, since adding any vertex makes a class of size three while keeping a deleted-pair overlap. These three cases are disjoint and exhaustive; summing their weights proves (3) and (4). The maximum size, minimum deletion size, pure-complex criterion, and missing-size spectrum follow by checking the displayed exponents, treating \(n=3\) separately where the first sum is empty and all maximal sets have size four.

## Verification

The self-contained program `verify_cograph.py` constructs each graph from adjacency rather than using the structural criterion. It first lists all four-element subsets whose induced degrees are \(1,1,2,2\), then enumerates every vertex subset, rejects precisely those containing one of the detected induced-path masks, and independently tests one-vertex maximality. Across \(129\) finite parameter profiles, it directly examines \(169304\) subsets and checks every coefficient of (1); for crown orders \(3\) through \(8\), it checks every maximal-set coefficient in (3). The verifier also tests the inequalities in (2) symbolically for \(9282\) further parameter triples with \(3\le a,b\le30\). The latter finite checks do **not** prove the general inequality: the proof is the counting argument in Step 3. Running `python3 verify_cograph.py` with Python 3 and the standard library produces the output recorded in `verification_output.txt`.

## Relationship to prior work

The equivalence between cographs and induced-\(P_4\)-free graphs, and recursive cograph structure, is classical and is **not claimed here**; see Oxley–Singh and Singh below. Nastos–Gao develop general algorithms for minimum cograph vertex deletion (their Section 4), including the formulation as an induced-four-path hitting-set problem. Their full-text algorithmic statement does not assert the present complete two-variable counting polynomial, coefficientwise edge-deletion comparison, or crown-graph distribution of *all inclusion-minimal* deletion sets.

The induced-forest and dissociation-set problems on dense bipartite graphs are distinct. An induced \(P_4\) is a forest but is not a cograph; an induced \(C_4\) is a cograph but is not a forest. Dissociation sets (maximum induced degree at most one) form only a proper subset of cograph-inducing sets. Therefore complete forest or dissociation polynomials do not imply (1)–(4) by substitution. The result treats vertex-induced cographs, not arbitrary cograph graphs or their graph-isomorphism census.

## Limitations

The originality assessment is literature-relative, not a guarantee of publication priority. An equivalent formula could exist under the terms *induced four-path transversal*, *minimum cograph deletion*, or *hereditarily well-colored induced subgraph*. The general bivariate face formula holds also when one class has fewer than three vertices; the coefficientwise inequality is claimed only for classes of size at least three, with its specified equality case. The crown maximal-set formula requires a full perfect matching deletion and \(n\ge3\); no maximality formula for arbitrary \(G_{a,b,t}\) is claimed. Computational checks are finite and cannot substitute for the proofs.

## References

1. J. Oxley and J. Singh, *Generalizing Cographs to 2-Cographs*, arXiv:2103.00403v1 (first publicly posted 2021-02-28); subsequent full-text version arXiv:2103.00403v2, Sections 1–2, Theorem 1.1 and Lemma 2.4. https://arxiv.org/abs/2103.00403
2. J. Singh, *Cographs and 1-sums*, arXiv:2210.04139v1 (first publicly posted 2022-10-09), Sections 1–3, Theorem 1.1. https://arxiv.org/abs/2210.04139
3. J. Nastos and Y. Gao, *Bounded Search Tree Algorithms for Parameterized Cograph Deletion: Efficient Branching Rules by Exploiting Structures of Special Graph Classes*, arXiv:1006.3020 (2010), Section 4. https://arxiv.org/abs/1006.3020
