# Minimum perfect dominating sets of connected chain graphs
## Finding
Let \(G\) be a finite connected chain graph with canonical nonempty twin classes \(A_1,\ldots,A_p,B_1,\ldots,B_p\), ordered so that
\[
N(a)=B_1\cup\cdots\cup B_i\quad(a\in A_i),\qquad
N(b)=A_j\cup\cdots\cup A_p\quad(b\in B_j).
\]
Write \(\alpha_i=|A_i|\) and \(\beta_j=|B_j|\). A set \(D\subseteq V(G)\) is perfect dominating when every vertex outside \(D\) has exactly one neighbor in \(D\).

For \(x_i=|D\cap A_i|\), \(y_j=|D\cap B_j|\), \(Y_i=\sum_{j\le i}y_j\), and \(X_j=\sum_{i\ge j}x_i\), the complete profile criterion is
\[
D\text{ is perfect dominating}
\iff
\bigl(x_i<\alpha_i\Rightarrow Y_i=1\bigr)\text{ for every }i,
\quad
\bigl(y_j<\beta_j\Rightarrow X_j=1\bigr)\text{ for every }j.
\]

Let \(A=\bigcup_iA_i\) and \(B=\bigcup_jB_j\). If \(\min\{|A|,|B|\}=1\), then \(\gamma_p(G)=1\). If \(|A|,|B|\ge2\), then \(\gamma_p(G)=2\), and every minimum perfect dominating set is one of the following:

* \(\{a,b\}\) with \(a\in A_p\) and \(b\in B_1\);
* only when \(p=2\), \(\alpha_1=1\), and \(\beta_2=1\), the nonedge consisting of the unique vertex of \(A_1\) and the unique vertex of \(B_2\).

Thus, for \(|A|,|B|\ge2\), the number of minimum perfect dominating sets is
\[
\alpha_p\beta_1+\mathbf 1_{\{p=2,\alpha_1=1,\beta_2=1\}}.
\]
If exactly one bipartition class has size one, its sole vertex is the unique minimum perfect dominating set. For \(K_2\), either vertex is a minimum perfect dominating set, so there are exactly two.

## Assumptions and scope
Graphs are finite, simple, undirected, and connected. The chain-graph representation above is canonical after merging vertices with identical open neighborhoods into nonempty twin classes. The definition of perfect domination is the standard outside-only definition: vertices belonging to \(D\) are not required to have any prescribed number of neighbors in \(D\). This is distinct from efficient domination, which additionally imposes independence.

The theorem includes complete bipartite graphs as the one-block case \(p=1\), but its structural content is the arbitrary nested-neighborhood case \(p\ge2\), including the exceptional minimum pair that is itself a nonedge.

## Proof
For any vertex \(a\in A_i\setminus D\), its neighbors in \(D\) are precisely the selected vertices in \(B_1\cup\cdots\cup B_i\), so it has exactly \(Y_i\) neighbors in \(D\). Therefore every unselected vertex of \(A_i\) is perfectly dominated exactly when either \(x_i=\alpha_i\) or \(Y_i=1\). Similarly, every \(b\in B_j\setminus D\) has exactly \(X_j\) neighbors in \(D\), giving the second half of the profile criterion. This proves the stated if-and-only-if condition.

Suppose first that a perfect dominating set has one vertex. If its vertex lies in \(A\), every other vertex of \(A\) would have no neighbor in the set, so \(|A|=1\). Conversely, when \(|A|=1\), connectedness forces the one block on that side to be adjacent to all of \(B\), and its sole vertex is a perfect dominating set. The argument is symmetric for \(B\). Hence a singleton perfect dominating set exists exactly when one bipartition class has size one.

Now assume \(|A|,|B|\ge2\). Any pair with one vertex in \(A_p\) and one in \(B_1\) perfectly dominates every other vertex, so \(\gamma_p(G)\le2\); the singleton argument gives \(\gamma_p(G)=2\). A two-vertex perfect dominating set cannot lie wholly in one bipartition class: if both selected vertices are in \(A\), every vertex of \(B_1\) sees both, and the symmetric obstruction holds for two selected vertices in \(B\). Thus write the set as \(\{a,b\}\) with \(a\in A_i\), \(b\in B_j\).

If \(j>1\), every vertex in \(A_1\cup\cdots\cup A_{j-1}\) is nonadjacent to \(b\). Such vertices can be perfectly dominated only if all of them are already in the two-vertex set. Because only \(a\) lies on the \(A\)-side, this forces \(j=2\), \(\alpha_1=1\), and \(a\in A_1\). Otherwise \(j=1\). Dually, if \(i<p\), then every vertex in \(B_{i+1}\cup\cdots\cup B_p\) is nonadjacent to \(a\), forcing \(i=p-1\), \(\beta_p=1\), and \(b\in B_p\); otherwise \(i=p\).

Combining these alternatives gives the generic possibility \(i=p\), \(j=1\). The only way both exceptional alternatives can occur is \(p=2\), \(i=1\), \(j=2\), \(\alpha_1=1\), and \(\beta_2=1\). Direct substitution in the profile criterion shows that this exceptional nonedge pair is indeed perfect dominating. Counting the generic pairs and adding the exceptional one proves the formula.

## Verification
A standalone verifier constructs every canonical connected chain-graph profile of order at most \(10\), enumerates every vertex subset, tests the defining perfect-domination condition directly on the labeled graph, independently tests the prefix/suffix profile criterion, and compares the exact minimum size and number of minimum sets with the theorem.

The replay result is:

`VERIFY_OK profiles=511 subset_checks=349524 perfect_sets=13825 criterion_checks=349524 minimum_checks=511 exception_profiles=28 max_order=10`

The exhaustive computation is a finite corroboration only. The general theorem follows from the proof above, not from the order cutoff.

## Relationship to prior work
Dejter and Delgado use the same outside-only definition of perfect domination and study rectangular grid graphs; their first public preprint is arXiv:0711.4345v1, dated 27 November 2007. Their full text does not treat chain or Ferrers graphs.

Nayaka, Ashwini, Sharada, and Puttaswamy introduced a perfect-domination polynomial and gave formulas for several standard graph classes, including complete bipartite and complete multipartite graphs. Their paper therefore overlaps the one-block boundary \(p=1\), but not the nested-neighborhood chain-graph classification above; its searchable full text contains no occurrence of “chain” or “Ferrers”. Moreover, its printed coefficient for two-vertex perfect dominating sets of \(K_{m,n}\) with \(m,n\ge2\) is \(m\), whereas the defining condition gives one valid set for every cross-part pair, namely \(mn\). The present theorem does not rely on that printed coefficient: the one-block case is proved directly and is included in the exhaustive replay.

Lin, Mizrahi, and Szwarcfiter explicitly distinguish perfect domination from the stricter efficient-domination notion. Efficient-domination results therefore do not imply the present theorem.

## Limitations
The theorem is restricted to connected chain graphs and to ordinary vertex perfect domination. It does not classify inclusion-minimal perfect dominating sets of arbitrary cardinality, weighted variants, perfect \(k\)-domination, or efficient domination. The literature search included the aliases “chain graph” and “Ferrers graph”, but an obscure equivalent result under different terminology remains a residual bibliographic risk.

## References
1. I. J. Dejter and A. A. Delgado, “Perfect domination in rectangular grid graphs,” arXiv:0711.4345v1, 27 November 2007; later published in *Journal of Combinatorial Mathematics and Combinatorial Computing*.
2. S. R. Nayaka, Ashwini, Sharada, and Puttaswamy, “Perfect Domination Polynomial of a Graph,” *International Journal of Mathematics Trends and Technology* 67(4) (2021), 110–113, document IJMTT-V67I4P515.
3. M. C. Lin, M. J. Mizrahi, and J. L. Szwarcfiter, “Efficient and Perfect domination on circular-arc graphs,” arXiv:1502.01523, 5 February 2015.
