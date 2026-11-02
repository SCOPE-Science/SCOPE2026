# Three swaps suffice for two-seat justified representation, with a sharp five-candidate detour

## Finding
For every approval election with a positive number \(n\) of voters, at least two candidates, and committee size two, the graph whose vertices are justified-representation (JR) committees and whose edges replace exactly one committee member is connected and has diameter at most three. For two JR committees \(W,V\), their exact graph distance is zero when equal, one when they share one candidate, two when disjoint with a JR cross pair, and otherwise three. The upper bound is attained with five candidates and six voters; five candidates are necessary, and for five candidates at most five voters do not suffice.

## Assumptions and scope
Let \(N\) be a set of \(n\ge1\) voters and \(C\) a set of \(m\ge2\) candidates. Each voter \(i\) has an arbitrary approval ballot \(A_i\subseteq C\), including possibly the empty ballot. For \(c\in C\), write \(N_c=\{i\in N:c\in A_i\}\). A committee \(W\subseteq C\) has exactly two distinct candidates; it represents \(i\) if \(A_i\cap W\ne\varnothing\). Define
\[
u_c(W)=|\{i\in N:c\in A_i,\ A_i\cap W=\varnothing\}|.
\]
The standard size-two JR condition is equivalent to \(2u_c(W)<n\) for every \(c\in C\). Indeed, JR fails exactly if at least \(n/2\) mutually \(c\)-approving voters are unrepresented. Let \(G\) be the graph induced by the JR two-subsets of \(C\) in the Johnson graph \(J(m,2)\), with adjacency given by intersection of cardinality one. No restriction on ballot correlations, distinctness of voter types, or candidate support is imposed.

## Proof
Choose \(z\in C\) maximizing \(|N_z|=s\). There is at least one JR committee (the following cases give one explicitly).

**Case 1: \(s<n/2\).** For every committee \(W\), and every candidate \(c\), \(u_c(W)\le |N_c|\le s<n/2\). All two-subsets are JR; hence \(G=J(m,2)\), whose diameter is at most two.

**Case 2: \(s>n/2\).** Any committee containing \(z\) is JR, since every voter unrepresented by that committee lies outside \(N_z\), of cardinality \(n-s<n/2\). Every JR committee not containing \(z\) has a JR neighbor containing \(z\), obtained by replacing either member. All committees containing \(z\) form a clique. Thus any two vertices of \(G\) are connected by at most three edges.

**Case 3: \(s=n/2\).** In particular, \(n\) is even. Each unrepresented voter under a pair containing \(z\) lies in the complement \(N\setminus N_z\) of size \(n/2\), but some such pairs may fail JR. We first show that at least one JR pair containing \(z\) exists. If a pair \(\{z,a\}\) fails JR, then a witnessing candidate \(y\) must have all \(n/2\) complementary voters as supporters, so \(N_y=N\setminus N_z\) (because \(|N_y|\le s\)). The pair \(\{z,y\}\) covers all voters and is JR. If no \(z\)-pair fails, any is JR.

Next let \(W=\{a,b\}\) be any JR committee not containing \(z\). Suppose both \(\{a,z\}\) and \(\{b,z\}\) fail JR. The first failure has a witness \(y\) supported by all complementary voters, none of whom approves \(a\); therefore \(N_a\subseteq N_z\). The second failure similarly gives \(N_b\subseteq N_z\). Hence all \(n/2\) supporters of \(y\) are unrepresented by \(W\), contradicting JR. Thus every JR pair has a JR neighbor containing \(z\), or already contains \(z\). All JR pairs containing \(z\) are mutually adjacent, whether or not other \(z\)-pairs fail. This gives diameter at most three.
For arbitrary \(W,V\in G\), choose their valid \(z\)-neighbors if needed; the neighbors are adjacent or equal, giving a path of length at most three. If \(W,V\) have a candidate in common they are adjacent. If disjoint, a two-edge path exists exactly when one of the four cross pairs \(\{w,v\}\), \(w\in W,v\in V\), is JR. Otherwise the diameter bound makes their distance exactly three.

**Five candidates are necessary.** For \(m\le3\), any two two-subsets overlap and have distance at most one. For \(m=4\), two disjoint committees partition the entire candidate set. Every neighbor of the first is a cross pair with the second. Since \(G\) is connected, a path must start with a JR cross pair, which is already a length-two bridge to the second. Thus no detour of length three is possible when \(m\le4\).

**Sharp five-candidate, six-voter witness.** Label the five candidates \(a,b,c,d,e\). The six approval ballots, including multiplicities, are
\[
\{e\},\quad\{e\},\quad\{a,c,e\},\quad\{a,d,e\},\quad\{b,c,e\},\quad\{b,d,e\}.
\]
Both \(W=\{a,b\}\) and \(V=\{c,d\}\) represent four voters, leaving the two \(\{e\}\)-only voters unrepresented. For every candidate the number of its unrepresented supporters is at most two, strictly below \(n/2=3\); hence both are JR. Each cross pair from \(\{a,b\}\) and \(\{c,d\}\) represents exactly three voters and leaves three supporters of \(e\) unrepresented, so every cross pair fails JR. All pairs containing \(e\) represent all six voters and are JR. Consequently \(W\to\{a,e\}\to\{c,e\}\to V\) is a shortest length-three JR path.

**Five candidates with at most five voters.** For this finite extremal assertion, enumerate the \(2^5=32\) possible approval-ballot subsets, including empty. An anonymous profile of \(n\) voters is determined by its \(32\) nonnegative type multiplicities summing to \(n\), so all such profiles are covered by the explicit stars-and-bars recursion in `verify.cpp`. For every \(1\le n\le5\), the program checks all ten size-two committees, computes JR independently by \(2u_c(W)<n\), and computes breadth-first distances. It finds no graph distance exceeding the Johnson distance. In particular, at \(n=5\) it exhausts exactly \(\binom{36}{5}=376{,}992\) anonymous profiles. This is a finite, complete, reproducible enumeration, not a sampling claim.

## Verification
Compile with `g++ -O2 -std=c++17 -Wall -Wextra verify.cpp -o verify` and run `./verify`. The program enumerates all anonymous profiles for \(m\in\{2,3\}\) through ten voters, \(m=4\) through eight voters, and \(m=5\) through five voters, testing JR, connectivity, actual BFS distances, and Johnson-geodesicity; it also checks the six-voter witness directly. Exact integer arithmetic is used. The file `verification_output.txt` records the actual execution, including \(376{,}992\) anonymous profiles for the five-candidate five-voter layer and the sharp witness. The all-sizes diameter theorem follows from the analytical pivot proof, not from finite enumeration.

## Relationship to prior work
Dong, Frank, Peters and Suksompong (2025, first posted April 21) introduced systematic reconfiguration of proportional committees. Their Theorem 3.1 gives disconnectedness and isolated examples when the committee size is at least three. Proposition 3.3 excludes isolated two-seat JR committees but does not imply connectedness or an exact diameter. Their Theorem 3.7 permits a path via an approximately JR intermediate committee; it does not ensure every intermediate committee satisfies exact JR. Their candidate-interval domain provides geodesic routes in a restricted profile family. The present unrestricted two-seat theorem separates these cases: exact JR connectivity with a sharp three-swap bound, while shortest ambient two-swap routes can fail. The published results and definitions are acknowledged rather than re-claimed. Work on reconfiguration of score-optimal committees studies a different vertex family.

## Limitations
The theorem is specific to standard justified representation with two seats and unit-cost candidate swaps. It does not assert connectivity for three or more seats, which is known to fail, nor for extended JR. The claim that five voters are insufficient at five candidates rests on an exhaustive integer program and the completeness of the stars-and-bars enumeration; it is not presented as an independent short structural classification. A search of available prior mathematical records and publications did not identify the same theorem, but this is not proof of bibliographic uniqueness. Independent audit has not been performed.

## References
- C. Dong, F. Frank, J. Peters, W. Suksompong, *Reconfiguring Proportional Committees*, arXiv:2504.15157v1, submitted April 21, 2025, https://arxiv.org/html/2504.15157v1 . Published in *Proceedings of AAAI 2026*, DOI:10.1609/aaai.v40i20.38727.
- R. Aziz et al., *Justified Representation in Approval-Based Committee Voting*, established formulation of JR; see references and preliminaries of Dong et al. cited above.
- Source code and exact finite output are reproduced in the accompanying `verify.cpp` and `verification_output.txt`.
