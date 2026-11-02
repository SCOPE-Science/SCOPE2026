# Exact nilpotency-index census of finite Brandt power semigroups

## Finding
Let \(n\ge 1\), let \(G\) be any finite group of order \(g\ge1\), and set \(q=2^g-1\). In the semigroup \(\mathcal P(B_n(G))\) of **nonempty** subsets of the Brandt semigroup under setwise multiplication, the only nilpotency indices are \(1,\ldots,n\), and each index occurs. Write \(N_{n,r}\) for the number of subsets whose least power equal to \(\{0\}\) is \(r\). Then \(N_{n,1}=1\), and for each \(2\le r\le n\),
\[
N_{n,r}=2\sum_{\substack{a_1+\cdots+a_r=n\\a_i\ge1}}
 \frac{n!}{a_1!\cdots a_r!}\,
 (1+q)^{\sum_{1\le j<i-1\le r-1}a_j a_i}\,
 \prod_{i=2}^{r}\big((1+q)^{a_{i-1}}-1\big)^{a_i}.
\]
The exponent in the first product is equivalently \(\sum_{i=3}^{r}\sum_{j=1}^{i-2}a_j a_i\), which is zero for \(r\le2\). For \(n\ge2\), the number having **maximal index** \(n\) is
\[
N_{n,n}=2n!\,(2^g-1)^{n-1}\,2^{g(n-1)(n-2)/2}.
\]
The total number of nilpotent elements is \(2D_n(q)-1\), where \(D_n(q)\) is the edge-weighted labeled directed-acyclic-graph polynomial. It is computed exactly from \(D_0(q)=1\) and
\[
D_n(q)=\sum_{k=1}^{n}(-1)^{k+1}\binom nk (1+q)^{k(n-k)}D_{n-k}(q).
\]
Thus the complete index distribution depends on \(G\) only through its order, not its multiplication table.

## Assumptions and scope
Write \(I=\{1,\ldots,n\}\). The Brandt semigroup is \(B_n(G)=\{0\}\cup(I\times G\times I)\), with \(0\) absorbing and
\[
(i,a,j)(k,b,\ell)=\begin{cases}(i,ab,\ell),&j=k,\\0,&j\ne k.\end{cases}
\]
The setwise product of two nonempty subsets is again nonempty. Its absorbing element is the singleton \(\{0\}\). A subset \(X\) is *nilpotent* precisely when \(X^s=\{0\}\) for some positive integer \(s\), and its *index* is the smallest such \(s\). The empty subset is not an element of the power semigroup considered here. A digraph is labeled on the fixed vertex set \(I\); a path has its usual edge length, and a directed cycle includes a loop.

## Proof
**1. Products and walks.** For each nonempty \(X\subseteq B_n(G)\), form the directed support graph \(\Gamma_X\) on \(I\): there is an arrow \(i\to j\) precisely when \(X\) contains at least one triple \((i,a,j)\). For every \(s\ge1\), the power \(X^s\) contains a nonzero element if and only if \(\Gamma_X\) contains a directed walk of length \(s\). In the forward direction, the multiplication rule demands consecutive matching indices. Conversely, choose one available group label on each arrow of a walk; their product in \(G\) produces a nonzero triple, since every product in a group exists and is nonzero. Consequently a directed cycle prevents nilpotence. An acyclic graph has a longest directed path of length \(\ell\le n-1\), and then \(X^s\) contains no nonzero element for \(s\ge\ell+1\).

If \(\Gamma_X\) is nonempty and acyclic, every arrow has distinct endpoints. Taking the square of any corresponding triple forces a zero product, so \(0\in X^2\). Therefore \(0\in X^s\) for all \(s\ge2\), and \(X^{\ell+1}=\{0\}\) with \(\ell\ge1\). The minimality of \(\ell+1\) follows from the existence of a path of length \(\ell\). If \(\Gamma_X\) is empty, the nonemptiness of \(X\) forces \(X=\{0\}\), of index one. Hence the nilpotency index is one more than the longest directed path length, except for the unique empty-support case, whose index is one.

**2. Lifting labeled graphs.** At each present arrow \((i,j)\), the set \(\{a\in G:(i,a,j)\in X\}\) can be any nonempty subset of \(G\), of which there are \(q\) choices. Missing arrows have exactly one choice. The element \(0\) may independently be included or omitted for every nonempty support graph, producing a factor of two. There is only one nonempty subset with empty support, namely \(\{0\}\). Thus the number of power-semigroup elements with any prescribed nonempty acyclic support graph having \(m\) arrows is \(2q^m\).

**3. Canonical longest-path layers.** In a labeled acyclic graph \(H\), give a vertex the level \(1+\) (maximum length of a directed path ending at that vertex). If the graph has longest path length \(r-1\), these levels form nonempty disjoint sets \(A_1,\ldots,A_r\), with sizes \(a_1,\ldots,a_r\ge1\) summing to \(n\). Every arrow goes from a lower to a higher level. Moreover, for every vertex at level \(i\ge2\), at least one incoming arrow originates at the immediately preceding level \(i-1\); this follows by taking the last arrow of a longest path ending at that vertex. Conversely, any partition into nonempty ordered levels with exactly these arrow restrictions has the specified canonical longest-path levels: induction on \(i\) proves that each level-\(i\) vertex has an incoming path of length \(i-1\), and no longer one exists.

For fixed ordered vertex sets, each vertex of level \(i\ge2\) independently chooses a nonempty collection of incoming arrows from level \(i-1\), weighted by \(q\) per chosen arrow; its total weight is \((1+q)^{a_{i-1}}-1\). Arrows skipping at least one level may be independently absent or present with a group-label subset, contributing \((1+q)^{\sum_{i=3}^r\sum_{j=1}^{i-2}a_j a_i}\). Same-level and backward arrows are forbidden. There are \(n!/(a_1!\cdots a_r!)\) ways to choose the ordered labeled layers. Multiplying these independent factors and multiplying by two for optional \(0\) proves the exact index formula.

**4. Sharpness, maximal layer and total.** A directed path on \(r\) vertices and \(n-r\) isolated vertices gives an acyclic graph with longest path length \(r-1\), for each \(2\le r\le n\); the singleton zero gives \(r=1\). When \(r=n\), the only possible composition has all parts one, so the preceding formula simplifies to \(2n!q^{n-1}(1+q)^{(n-1)(n-2)/2}\). To count all nilpotent subsets, sum the weights of all acyclic graphs, giving \(1+2(D_n(q)-1)=2D_n(q)-1\). Finally, apply inclusion-exclusion to the nonempty set of source vertices of a DAG: a fixed set of \(k\) sources has no incoming edges, its edges to the remaining vertices carry arbitrary weights \((1+q)^{k(n-k)}\), and the remaining graph is any weighted DAG. This gives the displayed recurrence with \(D_0(q)=1\), completing the proof.

## Verification
The standalone, standard-library-only program `verify.py` evaluates the exact composition formula and independently enumerates every acyclic support digraph for \(n\le4\) and \(g\in\{1,2,4\}\), checking each index. It also directly enumerates every nonempty subset and performs actual setwise Brandt multiplication for \((n,g)=(1,1),(1,2),(2,1),(2,2),(2,4),(3,1),(3,2)\), where it checks the least index of every nilpotent subset. The direct finite-group implementation uses cyclic groups, whereas the proof covers every finite group. The two computations agree and print `VERIFY_OK`; see `verify_output.txt`. These finite computations corroborate, but do not substitute for, the all-\(n\) proof.

For instance, when \(g=1\) and \(n=4\), the counts for indices \(1,2,3,4\) are \(1,172,528,384\), totaling \(1085\). When \(g=2\) and \(n=3\), the counts are \(1,144,432\), totaling \(577\).

## Relationship to prior work
Liu and Tringali (2026) study isomorphism rigidity and singleton preservation for nonempty power semigroups of inverse semigroups; their source supplies the modern power-semigroup setting but not the index census. Margolis, Rhodes and Silva (2017), Theorems 5.1 and 5.4, identify Boolean relation representations of the full subset monoid in the aperiodic Brandt case and relate nilpotent *subsemigroups* to acyclic graphs and longest paths. Their structural results are close antecedents, but a subsemigroup is closed under multiplication whereas an arbitrary element of the power semigroup need not be; the present result counts all nilpotent individual subsets, by exact index, over every finite group-labelled Brandt semigroup. The weighted DAG recurrence specializes to the classical unlabeled-edge DAG enumeration when \(q=1\); that underlying recurrence is not presented as new. OEIS A003024 explicitly identifies its classical values with the number of nilpotent binary relations, and McKay (1989) analyzes longest-path height distributions in random acyclic digraphs. Neither is claimed as a newly discovered unweighted count or path stratification; the proposed new result is the exact group-labelled Brandt power-semigroup index spectrum. The contribution is the full group-weighted, index-stratified power-semigroup spectrum and its exact sharp top layer.

## Limitations
The formula applies to finite Brandt semigroups with a finite group at every nonzero matrix unit. It does not classify nilpotent elements of arbitrary finite semigroups, nor the nilpotent subsemigroups of the Brandt semigroup, nor isomorphism types of nilpotent subsets. Its historical-priority claim is limited: earlier exact longest-path-layer enumeration of DAGs, including possibly material related to McKay (1989), or general results on Boolean relation semigroups may imply parts of the formula. Only the abstract of McKay (1989) was accessible for assessment; its complete text was not inspected. No independent mathematical audit has been conducted. The finite checks use cyclic groups only; the group-independence theorem is proved symbolically by support-path arguments.

## References
1. S. Liu and S. Tringali, *Kobayashi's problem for power semigroups of inverse semigroups*, arXiv:2610.29525v1, first public 2026-10-21. https://arxiv.org/html/2610.29525v1
2. S. Margolis, J. Rhodes and P. V. Silva, *On the subsemigroup complex of an aperiodic Brandt semigroup*, arXiv:1705.04956, 2017; Theorems 5.1 and 5.4. https://arxiv.org/abs/1705.04956
3. OEIS A003024, *Number of acyclic digraphs on n labeled nodes*, https://oeis.org/A003024. The ordinary DAG sequence, its nilpotent-binary-relation interpretation, and its source-inclusion-exclusion recurrence precede this calculation.
4. B. D. McKay, *On the shape of a random acyclic digraph*, Mathematical Proceedings of the Cambridge Philosophical Society 106 (1989), 459–465, doi:10.1017/S0305004100068195 (abstract consulted; full text not inspected).
