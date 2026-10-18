# Complete general-position polynomials of arbitrary caterpillar trees

## Finding
For every integer \(r\geq1\) and every vector of nonnegative integers \(\mathbf a=(a_1,\ldots,a_r)\), construct the caterpillar \(T(\mathbf a)\) from the path \(v_1\cdots v_r\) by adjoining \(a_i\) individually labeled pendant leaves at \(v_i\). Write \(N=r+\sum_i a_i\), and let \(\psi_T(z)=\sum_{S\subseteq V(T)\text{ in general position}}z^{|S|}\). Put
\[
 A_i(z)=(1+z)^{a_i},\qquad E_i(z)=A_i(z)-1+z.
\]
Then the entire general-position polynomial, including all small and degenerate cases, is
\[
\boxed{\displaystyle
\psi_{T(\mathbf a)}(z)=1-r+\sum_{i=1}^{r}\bigl(A_i(z)+z+a_i z^2\bigr)
+\sum_{1\leq i<j\leq r}E_i(z)E_j(z)\prod_{i<k<j}A_k(z).}
\]
The empty product equals \(1\). Every general-position set is characterized uniquely by the branch rules in the proof. In particular, a polynomial recurrence evaluates all coefficients in \(O(N^2)\) integer-arithmetic operations and \(O(N)\) coefficient storage.

As a structural consequence, the degree sequence alone does not determine the general-position polynomial, even among seven-vertex caterpillars with two degree-three vertices. Specifically,
\[
\begin{aligned}
\psi_{T(1,1,2)}(z)&=1+7z+21z^2+10z^3+2z^4,\\
\psi_{T(2,0,2)}(z)&=1+7z+21z^2+8z^3+z^4.
\end{aligned}
\]
Both caterpillars have degree multiset \(\{3,3,2,1,1,1,1\}\), but in the first their degree-three vertices are adjacent and in the second they are at distance two.

## Assumptions and scope
All graphs are finite, simple, undirected, and connected. A vertex subset is *in general position* when no three distinct selected vertices occur on one shortest path. Every tree has a unique path between each pair of vertices, so a selected vertex may not lie internally on the path between two other selected vertices. Each leaf is distinguished as a vertex; the expression counts actual vertex subsets, not automorphism orbits. The backbone is permitted to have a single vertex, and each \(a_i\) may be zero. Any conventional caterpillar (a tree whose non-leaf vertices induce a path) admits such a representation. A representation need not be unique, but the expression counts vertex subsets of its represented tree and therefore is graph-invariant.

## Proof
Let \(L_i\) be the \(a_i\)-element set of leaves attached to \(v_i\), and put \(B_i=L_i\cup\{v_i\}\). For a set \(S\), call branch \(i\) *occupied* when \(S\cap B_i\neq\varnothing\).

**One occupied branch.** If only branch \(i\) is occupied, the induced subtree on its vertices is a star. A general-position subset in that branch is either an arbitrary nonempty subset of leaves, the singleton \(\{v_i\}\), or the pair \(\{v_i,\ell\}\) with \(\ell\in L_i\). In the last case adding a second leaf would put \(v_i\) between two selected leaves. Including the empty subset, the polynomial of these choices is
\[
F_i(z)=A_i(z)+z+a_i z^2.
\]

**At least two occupied branches.** Let \(i<j\) be the minimum and maximum occupied indices. Any selected backbone vertex \(v_k\) with \(i<k<j\) lies on the unique path from a selected vertex in \(B_i\) to one in \(B_j\), so it is forbidden. The interior branches may, however, contain arbitrary subsets of their pendant leaves. At the left endpoint, selecting \(v_i\) together with a pendant leaf of \(B_i\) would put \(v_i\) on the path from that leaf to any selected vertex of \(B_j\), and is forbidden. Thus \(S\cap B_i\) is either a nonempty subset of \(L_i\), or the singleton \(\{v_i\}\); the same holds for \(j\). These endpoint options have polynomial \(E_i(z)\) and \(E_j(z)\). Their intervening branches independently contribute \(A_k(z)\).

Conversely, every set described by these rules is in general position. A selected pendant leaf cannot lie internally on a path between other vertices because its degree is one. A selected backbone vertex is either the unique selected branch or lies at the extreme occupied index with no selected pendant leaf at its own branch; consequently it cannot lie internally between two other selected vertices. This establishes sufficiency as well as necessity.

There is exactly one empty set; the nonempty sets with only branch \(i\) occupied contribute \(F_i(z)-1\), and sets with extreme occupied branches \(i<j\) contribute exactly \(E_i(z)E_j(z)\prod_{i<k<j}A_k(z)\). The displayed formula follows by adding these disjoint families.

**Linear-pass polynomial recurrence.** Initialize \(P_0(z)=1\) and \(H_1(z)=0\). For \(1\le j\le r\), set
\[
\begin{aligned}
P_j(z)&=P_{j-1}(z)+F_j(z)-1+E_j(z)H_j(z),\\
H_{j+1}(z)&=E_j(z)+A_j(z)H_j(z).
\end{aligned}
\]
Inductively, \(H_j(z)=\sum_{i<j}E_i(z)\prod_{i<k<j}A_k(z)\); thus \(P_r(z)=\psi_{T(\mathbf a)}(z)\). If \(N=r+\sum_i a_i\), ordinary convolution by \(A_j\) or \(E_j\) has degree \(a_j\) in its second factor. Its cost is at most \(O(N(a_j+1))\), and multiplication by the constant when \(a_j=0\) reduces to addition. Summing the genuinely nonconstant convolutions and the linear updates gives \(O(N^2)\) integer operations with arrays of \(O(N)\) length. No statement about bit complexity is intended.

Finally, direct substitution of the profiles \((1,1,2)\) and \((2,0,2)\) gives the two asserted seven-vertex polynomials; the degree calculations follow from \(\deg(v_1)=a_1+1\), \(\deg(v_r)=a_r+1\), and \(\deg(v_i)=a_i+2\) for internal backbone vertices.

## Verification
The standalone verifier `verify_caterpillars.py` constructs every represented tree independently, computes graph distances by breadth-first search, rejects exactly those selected subsets containing a collinear triple, and compares the resulting counts with both the closed formula and the polynomial recurrence. It completely enumerates \(992\) leaf profiles with \(1\le r\le5\), \(0\le a_i\le3\), and \(N\le13\), testing \(2{,}806{,}538\) vertex subsets altogether. The checker also tests \(111\) published special-family instances: \(12\) combs and \(99\) brooms. The recorded invocation and output are supplied in standalone files. These finite tests corroborate the formulas but are not used as a proof for unbounded parameters.

## Relationship to prior work
Iršič, Klavžar, Rus, and Tuite introduced the general-position polynomial and derived explicit coefficients for brooms and combs, alongside other graph classes. Their first arXiv version is dated 11 January 2024. Those two tree families are strict specializations of the present arbitrary-profile theorem: choosing \(a_i=1\) for all \(i\) gives the comb formula, while choosing \(\mathbf a=(q,0,\ldots,0)\) gives the broom formula. Neither special case fixes how distinct positive leaf multiplicities interact at multiple backbone positions.

A later treatment by Rather revisits the comb case and studies complete multipartite graphs and coronas, but does not state the arbitrary-caterpillar enumeration. Related published statements about general position polynomials on spiders concern trees with at most one branching vertex. The present result addresses arbitrary numbers and positions of branching vertices on one backbone. An abstract similarity or a general inclusion–exclusion identity for arbitrary graphs does not supply this explicit branchwise classification or its efficient coefficient recurrence.

## Limitations
The formula is for caterpillar trees only, not general trees or arbitrary graph products. It does not assert unimodality, log-concavity, or a closed form for all maximal general-position sets. The complexity bound counts integer coefficient operations, not bit operations. The literature comparison was limited to accessible papers and publicly searchable research records; unindexed equivalent work remains possible.

## References
1. V. Iršič, S. Klavžar, G. Rus, and J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first version, 2024-01-11); *Results in Mathematics* **79** (2024), article 110, DOI: 10.1007/s00025-024-02133-3. See especially the broom formula and comb Theorem 4.1.
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (2026-03-06). See especially the comb and corona sections.
3. B. S. Anand, U. S. V. Chandran, M. Changat, S. Klavžar, and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460 (2018-12-20). General structural background, not a caterpillar counting formula.
