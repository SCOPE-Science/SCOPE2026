# Minimum dominating-set rigidity and a four-column exception in two-token bicliques

## Finding
Let \(A=\{a_1,a_2,a_3\}\) and \(B=\{b_1,\ldots,b_n\}\), where \(n\ge 3\), and let \(T_n=F_2(K_{3,n})\) be the two-token graph. All vertices of \(T_n\) are unordered two-element subsets of \(A\cup B\); two such subsets are adjacent if their symmetric difference is an edge of \(K_{3,n}\).

Every minimum dominating set of \(T_n\) has exactly \(n\) vertices. The complete classification is as follows.

**Family I (all \(n\ge3\)).** Choose a distinguished vertex \(a\in A\) and an unordered pair \(\{b,c\}\subset B\). Select the two-token vertices
\[
D(a;\{b,c\})=\{A\setminus\{a\},\{b,c\}\}\ \cup\ \bigl\{\{a,d\}:d\in B\setminus\{b,c\}\bigr\}.
\]
Here \(A\setminus\{a\}\) denotes its unique two-element subset, viewed as one vertex of \(T_n\). There are \(3\binom n2\) such sets.

**Family II (only \(n=4\)).** Partition \(B\) into unordered pairs \(P,Q\), designate one of the pairs \(P\) as the two-element set of unused vertices, and choose an injection \(f:Q\to A\). Select
\[
E(P,f)=\{P,Q\}\ \cup\ \bigl\{\{f(b),b\}:b\in Q\bigr\}.
\]
There are \(\binom42(3\cdot2)=36\) such sets. The families are disjoint, and no other minimum dominating sets exist. Consequently their number is
\[
d_n=3\binom n2+36\,\mathbf 1_{\{n=4\}}.
\]
Equivalently, \(d_3=9\), \(d_4=54\), and \(d_n=3\binom n2\) for every \(n\ge5\). Under the natural part-preserving action of \(S_3\times S_n\), there is one orbit of minimum sets except at \(n=4\), where there are exactly two orbits.

## Assumptions and scope
Graphs are finite, simple, and labelled. A dominating set contains or neighbors every vertex, and a minimum dominating set has the least possible cardinality. Throughout \(n\) is an integer at least \(3\). The two sides \(A,B\) are identified and carry their own labelled vertices; when \(n=3\), the displayed part-preserving action is considered, although the full graph may have additional symmetries. Counts are of actual subsets of the labelled token-graph vertex set, not of symmetry orbits.

## Proof
Write \(\mathcal A=\binom A2\), \(\mathcal B=\binom B2\), and \(\mathcal X=\{\{a,b\}:a\in A,b\in B\}\). For an arbitrary dominating set \(D\subseteq V(T_n)\), put \(D_A=D\cap\mathcal A\), \(D_B=D\cap\mathcal B\), \(D_X=D\cap\mathcal X\), and denote their cardinalities by \(y,z,x\), respectively. Regarding \(D_X\) as an edge set of a bipartite graph \(H\) on \(A\cup B\), let \(A_0,B_0\) be the vertices of degree zero in \(H\). Let \(C_A\) and \(C_B\) be the vertices covered by pairs in \(D_A\) and \(D_B\).

**Domination criterion.** Such a set \(D\) is dominating if and only if
\[
\binom{A_0}{2}\subseteq D_A,\qquad \binom{B_0}{2}\subseteq D_B,\qquad
\bigl\{\{a,b\}:a\in A\setminus C_A,\ b\in B\setminus C_B\bigr\}\subseteq D_X.\tag{1}
\]
Indeed, a token vertex \(\{a,a'\}\in\mathcal A\) is adjacent exactly to cross pairs incident with \(a\) or \(a'\), so it is undominated precisely when it lies outside \(D_A\) and both its endpoints lie in \(A_0\). The same applies to \(\mathcal B\). A cross-pair token \(\{a,b\}\in\mathcal X\) is adjacent exactly to same-side pairs containing \(a\) or \(b\), proving the third condition. This establishes necessity and sufficiency without invoking any other theorem.

Put \(k=|B_0|\). Each of the \(n-k\) vertices of \(B\setminus B_0\) is incident with a selected cross pair, while every pair within \(B_0\) must be selected in \(D_B\). Therefore
\[
x\ge n-k,\quad z\ge\binom k2,\quad x+z\ge n-k+\binom k2\ge n-1.\tag{2}
\]
Equality in the last inequality is possible only for \(k\in\{1,2\}\), and equality throughout forces \(x=n-k\) and \(z=\binom k2\).

**Minimum cardinality.** Every Family-I set satisfies (1) and has size \(n\), so \(\gamma(T_n)\le n\). If a dominating set had size at most \(n-1\), (2) would force \(y=0\), \(x+z=n-1\), and \(k=1\) or \(2\). For \(k=1\), we would have \(z=0\); the vertex of \(B_0\) would not be covered by \(D_B\) and could not have all three incident cross pairs selected, contrary to (1). For \(k=2\), we would have \(z=1\), \(x=n-2\), and \(D_B=\{B_0\}\); since \(C_A=\emptyset\), condition (1) requires all three cross pairs at each of the \(n-2\) other vertices of \(B\), yielding \(x\ge 3(n-2)>n-2\). Thus \(\gamma(T_n)=n\).

**Exactly one selected \(A\)-pair.** In a minimum set \(x+y+z=n\), so (2) implies \(y\le1\). If \(y=1\), then \(x+z=n-1\), so \(k\in\{1,2\}\) with the equalities just established. The case \(k=1\) is impossible because \(z=0\) and the one vertex of \(A\setminus C_A\) together with the unused \(B\)-vertex forms an undominated cross pair. Thus \(k=2\), \(D_B=\{B_0\}\), and \(x=n-2\). Let \(a\) be the one vertex of \(A\setminus C_A\). Every \(b\in B\setminus B_0\) lies outside \(C_B\), so (1) requires \(\{a,b\}\in D_X\). There are exactly \(n-2\) such cross pairs, exhausting \(D_X\). This is precisely Family I.

**No selected \(A\)-pair.** Suppose \(y=0\), so \(x+z=n\) and \(C_A=\emptyset\). Put \(t=|B\setminus C_B|\). Condition (1) forces all three cross pairs at every such \(B\)-vertex; furthermore \(B_0\subseteq C_B\). Counting cross pairs at the \(t\) uncovered \(B\)-vertices and at the other \(n-t-k\) vertices with positive \(H\)-degree gives
\[
x\ge3t+(n-t-k)=n+2t-k,\qquad z\le k-2t.\tag{3}
\]
Together with \(z\ge\binom k2\) and \(z\ge\lceil k/2\rceil\) (the latter because \(B_0\subseteq C_B\)), (3) rules out \(t\ge1\): for \(k\le2\) the bound \(z\le k-2\) is below the necessary coverage bound, and for \(k\ge3\) it is below \(\binom k2\).

Thus \(t=0\), so every vertex in \(B\) is covered by a selected pair of \(D_B\) and \(z\ge\lceil n/2\rceil\). From \(x\ge n-k\) and \(x+z=n\), we have \(z\le k\). This excludes \(k=0,1\) since \(n\ge3\), and excludes \(k\ge4\) since \(\binom k2>k\). If \(k=3\), equality forces \(z=3\), \(D_B=\binom{B_0}{2}\), and hence \(C_B=B_0\); because \(t=0\), necessarily \(n=3\) and \(x=0\), leaving all three \(A\)-vertices isolated and contradicting (1). Therefore \(k=2\), \(z\le2\), and \(n\le4\).

For \(n=3\), coverage requires \(z=2\), leaving \(x=1\). At most one vertex of \(A\) is then incident with any cross pair, so two distinct vertices lie in \(A_0\) while \(D_A=\emptyset\), contradicting (1). Hence \(n=4\), \(z=2\), and \(x=2\). The two vertices of \(B_0\) form one selected \(B\)-pair. The other selected \(B\)-pair must be the complementary pair to cover all four \(B\)-vertices. Each of the remaining two \(B\)-vertices has exactly one selected cross pair; their \(A\)-endpoints must be distinct to ensure \(|A_0|\le1\). This is exactly Family II. Conversely, every Family-II set satisfies all three conditions of (1).

Finally, the choices in Family I and Family II yield the displayed counts. The independent permutations of \(A\) and \(B\) act transitively within each family; the families cannot lie in the same orbit because their \(D_A\)-cardinalities differ. This proves the orbit assertion. \(\square\)

## Verification
A standalone C++17 program, `verify_minimum_token_domination.cpp`, constructs the entire two-token graph independently from the definition. It enumerates every \(n\)-element vertex subset for \(n=3,4,5,6,7\), tests domination from closed-neighborhood bitmasks, and checks that every successful subset belongs to exactly one stated family. The exact counts are \(9,54,30,45,63\), including \(36\) exceptional sets when \(n=4\). In total this is \(47,432,132\) tested candidate subsets. The universal result is proved above; exhaustive finite enumeration is an additional check, not an infinite proof. Reproduction: compile with `c++ -std=c++17 -O3 verify_minimum_token_domination.cpp -o verify` and execute `./verify`.

## Relationship to prior work
Two independent October 2026 papers determine \(\gamma(F_2(K_{m,n}))\) for every \(2\le m\le n\). Chinman et al. give the value for \(m=3\) and exhibit one Family-I construction. Acosta Troncoso et al. prove the same value and provide a general necessary-and-sufficient domination criterion, equivalent to (1), and observe the Family-I structure in one equality case. These established results are credited. The present claim instead classifies *every* minimum set, counts its labelled realizations, and identifies the additional Family-II orbit at \(n=4\); these conclusions are not stated in the inspected texts. The proof of (1) is included here for self-containment. Existing results for the two-token graph of \(K_{2,n}\) have a different graph parameter and do not imply this three-vertex-side classification.

## Limitations
The theorem concerns only ordinary domination of \(F_2(K_{3,n})\) for \(n\ge3\), with labelled vertices. It does not give the full domination polynomial or the minimum-set counts for \(K_{m,n}\) when \(m\ge4\), nor does it enumerate all inclusion-minimal dominating sets. Earlier work already determines the minimum size \(n\); that value is not claimed as new. The comparison of accessible current literature supports, but cannot guarantee, historical priority; independent mathematical validation has not been performed.

## References
1. N. Chinman, A. Cortijo, B. Pedroni, I. Seong, and L. Stenger, *The domination number of the \(k\)-token graph of the complete bipartite graph \(K_{m,n}\)*, arXiv:2610.28936v1 (first public 20 October 2026), https://arxiv.org/html/2610.28936v1.
2. E. Acosta Troncoso, I. Caldera Caldera, and L. M. Rivera, *The domination number of the 2-token graph of the complete bipartite graph*, arXiv:2610.31557v1 (first public 22 October 2026), https://arxiv.org/html/2610.31557v1.
