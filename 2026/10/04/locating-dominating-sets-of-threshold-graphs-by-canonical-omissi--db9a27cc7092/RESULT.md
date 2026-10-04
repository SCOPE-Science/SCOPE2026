# Locating-dominating sets of threshold graphs by canonical omissions
## Finding
Let \(G\) be a connected threshold graph with canonical positive block decomposition
\[
0^{a_1}1^{b_1}\cdots 0^{a_p}1^{b_p},
\]
where \(A_i\) is the \(0\)-block of size \(a_i\) and \(B_i\) is the \(1\)-block of size \(b_i\). Thus every vertex of \(A_i\) is adjacent exactly to \(B_i\cup\cdots\cup B_p\), while every vertex of \(B_j\) is adjacent to all other \(B\)-vertices and to \(A_1\cup\cdots\cup A_j\).

For a set \(D\subseteq V(G)\), write \(P\subseteq[p]\) for the indices of \(A\)-blocks from which exactly one vertex is omitted, and \(Q\subseteq[p]\) for the indices of \(B\)-blocks from which exactly one vertex is omitted. Put
\[
\alpha_i=a_i-\mathbf 1_{i\in P},\qquad \beta_i=b_i-\mathbf 1_{i\in Q}.
\]
Then \(D\) is locating-dominating if and only if it omits at most one vertex from every canonical block and the following five conditions hold:

1. for every \(i\in P\), \(\sum_{t=i}^{p}\beta_t>0\);
2. for every \(j\in Q\), \(\sum_{t\ne j}\beta_t+\sum_{t=1}^{j}\alpha_t>0\);
3. if \(i<i'\) are consecutive elements of \(P\), then \(\sum_{t=i}^{i'-1}\beta_t>0\);
4. if \(j<j'\) are consecutive elements of \(Q\), then \(\sum_{t=j+1}^{j'}\alpha_t>0\);
5. for every \(i\in P\) and \(j\in Q\),
\[
\sum_{t=1}^{j}\alpha_t+\sum_{t=1}^{i-1}\beta_t>0.
\]

Consequently, if \(N=|V(G)|\) and \(\mathcal A\) is the family of pairs \((P,Q)\) satisfying these conditions, the full locating-domination polynomial is
\[
L_G(x)=\sum_{(P,Q)\in\mathcal A}
\left(\prod_{i\in P}a_i\right)
\left(\prod_{j\in Q}b_j\right)
 x^{N-|P|-|Q|}.
\]
In the natural twin-thick case \(a_i,b_i\ge2\) for every \(i\), every pair \((P,Q)\) is admissible, so
\[
L_G(x)=\prod_{i=1}^{p}
\bigl(x^{a_i}+a_i x^{a_i-1}\bigr)
\bigl(x^{b_i}+b_i x^{b_i-1}\bigr),
\]
\[
\gamma_L(G)=N-2p,
\qquad
\#\{\text{minimum locating-dominating sets}\}=\prod_{i=1}^{p}a_i b_i.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. The displayed block representation is the canonical alternating threshold decomposition with all \(a_i,b_i\ge1\) and final block of type \(1\), so the graph is connected. A locating-dominating set \(D\) dominates every vertex outside \(D\) and gives distinct open-neighborhood traces \(N(u)\cap D\) to distinct vertices \(u\notin D\).

The theorem concerns ordinary locating-domination, not solid- or self-locating-domination. The variable \(x\) marks the cardinality of \(D\).

## Proof
Vertices inside one \(A_i\) have identical open neighborhoods. Vertices inside one \(B_i\) have identical closed neighborhoods, and if two of them are both outside \(D\), their traces on \(D\) are identical. Hence a locating-dominating set can omit at most one vertex from each canonical block. Once this necessary condition holds, its omitted vertices are determined, up to the choice of which vertex is omitted in each indicated block, by \((P,Q)\).

For an omitted vertex \(u\in A_i\), its trace is
\[
N(u)\cap D=\bigcup_{t=i}^{p}(B_t\cap D).
\]
This trace is nonempty exactly when condition 1 holds. For an omitted vertex \(v\in B_j\), since \(v\notin D\), its trace is
\[
N(v)\cap D=(B\cap D)\cup\bigcup_{t=1}^{j}(A_t\cap D),
\]
where \(B=B_1\cup\cdots\cup B_p\). This trace is nonempty exactly when condition 2 holds.

Now compare two omitted \(A\)-vertices, one in \(A_i\) and one in \(A_{i'}\) with \(i<i'\). Their traces differ exactly on
\[
\bigcup_{t=i}^{i'-1}(B_t\cap D).
\]
Thus they are distinguished exactly when this union is nonempty. It is enough to test consecutive elements of \(P\), giving condition 3. Similarly, omitted vertices from \(B_j\) and \(B_{j'}\), with \(j<j'\), have traces differing exactly on
\[
\bigcup_{t=j+1}^{j'}(A_t\cap D),
\]
so consecutive omitted \(B\)-blocks are distinguished exactly by condition 4.

Finally, compare an omitted \(u\in A_i\) with an omitted \(v\in B_j\). The trace of \(u\) contains only selected \(B\)-vertices from blocks \(B_i,\ldots,B_p\), whereas the trace of \(v\) contains every selected \(B\)-vertex and also every selected \(A\)-vertex in \(A_1,\ldots,A_j\). Therefore the two traces are equal if and only if there is no selected \(B\)-vertex in \(B_1,\ldots,B_{i-1}\) and no selected \(A\)-vertex in \(A_1,\ldots,A_j\). This is excluded exactly by condition 5.

The five conditions are therefore jointly necessary and sufficient. For a fixed admissible \((P,Q)\), there are \(\prod_{i\in P}a_i\prod_{j\in Q}b_j\) ways to choose the omitted vertices, and every such set has size \(N-|P|-|Q|\), yielding the polynomial formula.

If all canonical blocks have size at least \(2\), then after one omission every block still contains a selected vertex. Every sum in conditions 1--5 is therefore positive whenever it is relevant, so all \((P,Q)\) are admissible. The factorization follows by choosing independently, in each block, either no omitted vertex or exactly one omitted vertex. The least possible code size occurs by omitting one vertex from every one of the \(2p\) blocks, which gives \(\gamma_L(G)=N-2p\), and the number of such minimum sets is \(\prod_i a_i b_i\).

## Verification
The standalone verifier constructs every canonical connected threshold profile of orders \(2\) through \(10\). For each profile it enumerates every vertex subset, tests the defining locating-domination condition directly from the adjacency matrix, and compares the resulting cardinality polynomial with the theorem's admissible-omission formula. It also checks the twin-thick factorization whenever all block sizes are at least \(2\).

A replay from the packaged verifier returns `VERIFY_OK profiles=511 subset_checks=349524 coefficient_checks=2104 max_order=10`.

This finite computation is a regression test of the formulas, not a proof for arbitrary order; the proof above supplies the infinite argument.

## Relationship to prior work
Locating-domination is classical. Foucaud, Henning, Löwenstein, and Sasse define the parameter and prove general bounds, including the half-order bound for twin-free split graphs. Their split-graph theorem is an extremal upper bound under a twin-free hypothesis; it neither classifies threshold-graph locating-dominating sets nor enumerates them by cardinality.

Junnila, Laihonen, Lehtilä, and Puertas study the stronger solid- and self-locating variants. Their Proposition 19 characterizes threshold graphs by the extremal identity \(\gamma^{DLD}(G)=N-1\) for solid location-domination. This does not imply the present ordinary locating-domination theorem because solid location-domination additionally forbids inclusion among the traces of non-codewords, while ordinary locating-domination only requires the traces to be distinct and nonempty.

Foucaud's complexity survey establishes hardness for locating-domination on broader classes such as split graphs. Algorithmic hardness on the superclass does not determine the exact all-set structure on threshold graphs.

## Limitations
The theorem depends on the canonical threshold-block decomposition and is not claimed for arbitrary split graphs. The polynomial is given as an explicit admissible-pair sum; outside the twin-thick case it is not reduced here to a constant-state transfer matrix. The literature search found no statement implying this all-set classification, but poorly indexed older theses or papers using creation-sequence terminology remain a residual bibliographic risk.

## References
1. F. Foucaud, M. A. Henning, C. Löwenstein, T. Sasse, “Locating-dominating sets in twin-free graphs,” arXiv:1412.2376; Discrete Applied Mathematics 200 (2016), 52–58, DOI 10.1016/j.dam.2015.06.038.
2. F. Foucaud, “Decision and approximation complexity for identifying codes and locating-dominating sets in restricted graph classes,” Journal of Discrete Algorithms 31 (2015), 48–68, DOI 10.1016/j.jda.2014.08.004.
3. V. Junnila, T. Laihonen, T. Lehtilä, M. L. Puertas, “On Stronger Types of Locating-Dominating Codes,” arXiv:1808.06891; Discrete Mathematics and Theoretical Computer Science 21 (2019), no. 1.
