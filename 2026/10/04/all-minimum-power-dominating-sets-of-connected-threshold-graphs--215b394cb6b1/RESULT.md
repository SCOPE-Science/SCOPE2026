# All minimum power dominating sets of connected threshold graphs
## Finding
Let \(G\) be a finite connected threshold graph with canonical creation-block form
\[
0^{a_1}1^{b_1}\cdots 0^{a_p}1^{b_p},
\]
where every \(a_i,b_i\) is positive. Write \(A_i\) and \(B_i\) for the corresponding zero- and one-blocks. Then \(\gamma_P(G)=1\). More precisely, a singleton \(\{v\}\) is a power dominating set if and only if exactly one of the following structural conditions applies:

1. \(v\in B_i\) and \(a_j=1\) for every \(j>i\);
2. \(v\in A_1\), \(a_1\le2\), and \(a_j=1\) for every \(j\ge2\).

No vertex in \(A_i\) with \(i\ge2\) is a singleton power dominating set. Hence these are all minimum power dominating sets. If
\[
h=\max\bigl(\{j:a_j\ge2\}\cup\{0\}\bigr),
\]
then their number is
\[
\sum_{i=\max\{1,h\}}^p b_i
+a_1\mathbf 1_{\{a_1\le2,\ a_j=1\text{ for every }j\ge2\}}.
\]

## Assumptions and scope
Graphs are finite, simple, and undirected. A threshold graph is represented by its canonical creation sequence: a \(0\)-vertex is added isolated from all earlier vertices, while a \(1\)-vertex is added adjacent to all earlier vertices. Connectedness is equivalent to the final block being a \(1\)-block. Power domination starts by observing \(N[S]\); thereafter an observed vertex with exactly one unobserved neighbor observes that neighbor. The theorem classifies minimum sets, not all larger power dominating sets.

## Proof
Every vertex of the last one-block \(B_p\) is universal, so \(\gamma_P(G)=1\).

Fix a vertex \(v\in B_i\). Its closed neighborhood initially observes every one-block and every zero-block \(A_j\) with \(j\le i\). Thus the only unobserved vertices are those in \(A_{i+1},\ldots,A_p\). If some later block \(A_j\) has at least two vertices, choose two of them. They are false twins: every observed vertex is adjacent to both or to neither. As long as both remain unobserved, no observed vertex has exactly one of them as its unique unobserved neighbor, so neither can be the first vertex of that pair to be forced. Hence \(\{v\}\) fails. Conversely, if every later zero-block is a singleton, then a vertex of \(B_{i+1}\) forces the unique vertex of \(A_{i+1}\); after that, a vertex of \(B_{i+2}\) forces the unique vertex of \(A_{i+2}\), and so on. Therefore condition 1 is necessary and sufficient.

Now let \(v\in A_i\) with \(i\ge2\). Initially the observed set is \(\{v\}\cup B_i\cup\cdots\cup B_p\). The selected vertex \(v\) has no unobserved neighbor. Every observed vertex in \(B_k\), \(k\ge i\), is adjacent to an unobserved vertex of \(A_{i-1}\) and also to an unobserved vertex of \(B_{i-1}\), so it has at least two unobserved neighbors. No force is possible, proving that such a singleton never power dominates.

Finally let \(v\in A_1\). Initially every one-block is observed and the unobserved vertices are \(A_1\setminus\{v\}\) together with \(A_2,\ldots,A_p\). If \(a_1\ge3\), two unobserved vertices in \(A_1\) are false twins, so the process cannot enter that pair. The same obstruction occurs if any later \(A_j\) has size at least two. Conversely, if \(a_1\le2\) and every later zero-block is a singleton, then, when \(a_1=2\), a vertex of \(B_1\) first forces the remaining vertex of \(A_1\); subsequently vertices of \(B_2,B_3,\ldots,B_p\) force the singleton zero-blocks in order. When \(a_1=1\), the same chain starts with \(B_2\). This proves condition 2.

The counting formula follows because a one-block \(B_i\) qualifies exactly when it occurs at or after the last zero-block of size at least two, while the \(A_1\) contribution is exactly the second case.

## Verification
A direct verifier constructs every connected threshold creation sequence of orders \(2\) through \(12\), computes the power-domination closure of every singleton from the definition, and compares it with the theorem's block criterion. It checks 2,047 creation sequences and 22,528 singleton placements and reports:

`VERIFY_OK creation_sequences=2047 singleton_checks=22528 max_order=12`

The finite computation is a stress test only; the proof above establishes the theorem for all finite connected threshold graphs.

## Relationship to prior work
Haynes, Hedetniemi, Hedetniemi, and Henning introduced power domination as a graph model for PMU placement and classified it under MSC 05C69. Liao and Lee proved NP-completeness on split graphs, a superclass of threshold graphs, and gave algorithms for interval and circular-arc classes. Goyal and Panda later showed that minimum connected power domination is polynomial-time solvable on threshold graphs. Those results motivate the class but do not, in the material inspected here, state the exact creation-block criterion above for every optimal singleton location or its counting formula. Because every singleton induces a connected subgraph, the connected-threshold result is the closest potential source of overlap and is retained as a residual literature risk.

## Limitations
The claim concerns ordinary power domination and only minimum sets. It does not enumerate larger power dominating sets or propagation times. The threshold-specific section of the Goyal--Panda paper was not available in full through the accessible public sources during this check, so an unobserved equivalent characterization there remains a specific residual originality risk. The theorem does not depend on that source for correctness.

## References
1. C.-S. Liao and D.-T. Lee, *Power Domination Problem in Graphs*, COCOON 2005, Lecture Notes in Computer Science 3595, 818--828, DOI 10.1007/11533719_83.
2. T. W. Haynes, S. M. Hedetniemi, S. T. Hedetniemi, and M. A. Henning, *Domination in Graphs Applied to Electric Power Networks*, SIAM Journal on Discrete Mathematics 15(4), 519--529, DOI 10.1137/S0895480100375831.
3. P. Goyal and B. S. Panda, *Hardness Results of Connected Power Domination for Bipartite Graphs and Chordal Graphs*, COCOA 2021, 653--667, DOI 10.1007/978-3-030-92681-6_51.
