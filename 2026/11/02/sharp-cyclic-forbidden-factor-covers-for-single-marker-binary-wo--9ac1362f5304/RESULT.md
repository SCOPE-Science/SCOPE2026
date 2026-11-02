# Sharp cyclic forbidden-factor covers for single-marker binary words

## Finding

Let \(n\ge 3\) and \(0\le i\le n-1\) be integers. Set \(j=n-1-i\), and forbid the binary word \(f_i=0^i1 0^j\) of length \(n\). A cyclic covering word is a finite nonempty binary word whose cyclic length-\(n\) factors contain every word in \(\{0,1\}^n\setminus\{f_i\}\) and never contain \(f_i\). Factors may repeat; positions and multiplicities count, including those crossing the cyclic boundary. Let \(L(n,i)\) be the minimum number of cyclic positions, with \(L=\infty\) if no such word exists.

**Theorem.** For every \(n\ge 3\),
\[
L(n,i)=\begin{cases}
\infty,&i\in\{0,n-1\},\\
2^n-1+\dfrac{n+1}{2},&n\text{ odd and }i=\dfrac{n-1}{2},\\
2^n+n-1,&1\le i\le n-2\text{ in every other case}.
\end{cases}
\]
For each finite case there is a **unique optimal multiplicity profile** of all cyclic length-\(n\) factors. Precisely, every allowed factor occurs once, except that the distinct factors on the unique shortest directed path from the prefix of \(f_i\) to its suffix in the de Bruijn overlap graph with \(f_i\) removed occur twice; \(f_i\) never occurs. Hence the optimum's entire duplicated-factor set is determined by \((n,i)\), even though the cyclic word itself need not be unique. The same statement applies to the bit-complements of these forbidden words by interchanging zeros and ones.

The unique shortest repair path is explicit. For \(1\le i,j\), write \(u=0^i1 0^{j-1}\) and \(v=0^{i-1}1 0^j\). Its directed edge labels are the \(n\)-windows in \(T=u\alpha\), where
\[
\alpha=\begin{cases}
1 0^i,&i=j,\\
1 0^{i-1}1 0^j,&i\ne j.
\end{cases}
\]
The number of appended symbols is \((n+1)/2\) in the centered case and \(n\) otherwise. Each of the resulting \(n\)-windows is permitted and distinct.

## Assumptions and scope

The alphabet is labeled \(\{0,1\}\); positions are read cyclically and the factors are oriented (not identified under reversal). All words of length \(n\), other than the one specified forbidden word, are mandatory. Extra occurrences of permitted factors are allowed. Only one word is forbidden. The stated impossibility at the two endpoint positions is literal: no finite circular word satisfies coverage and avoidance simultaneously. No conditions of primitivity or aperiodicity are imposed on the covering word.

## Proof

**1. Eulerian reduction.** Form the directed binary de Bruijn overlap graph \(G_n\): its vertices are all length-\((n-1)\) binary strings, and a length-\(n\) string \(x_1\cdots x_n\) labels a directed edge from \(x_1\cdots x_{n-1}\) to \(x_2\cdots x_n\). Cyclic host words correspond to closed walks; the multiplicity of any length-\(n\) factor is its edge traversal count. Delete the forbidden edge \(f_i\). In this graph every other edge is required at least once. The original full de Bruijn graph is connected, and deleting any one of its edges preserves connectivity of its underlying undirected graph: each edge lies on a directed cycle, so its endpoints remain connected after deletion. Thus the surviving required-edge graph is weakly connected.

The deleted edge went from its prefix \(u\) to its suffix \(v\). These are distinct (the forbidden word has one \(1\) and \(n\ge3\)). The surviving graph has an excess of one required in-edge at \(u\), an excess of one required out-edge at \(v\), and balanced degrees elsewhere. To make its required edges into a closed walk, the extra traversals must form a nonnegative integer flow carrying one unit from \(u\) to \(v\), possibly with superfluous directed cycles. Consequently there must be an allowed directed \(u\)-to-\(v\) path, and at least \(\delta(u,v)\) extra traversals, where \(\delta\) is the shortest allowed path length. Conversely duplicating a shortest allowed path balances all degrees, and the resulting weakly connected directed multigraph has an Euler circuit. Hence the exact optimal length is \(2^n-1+\delta(u,v)\), with impossibility exactly when no such path exists. Every minimum extra flow is a shortest path without any additional directed cycle.

**2. Boundary obstructions.** If \(i=0\), the forbidden edge is \(10^{n-1}\). The only edge entering the all-zero vertex \(0^{n-1}\) from outside that vertex is the forbidden edge; its other in-edge is the \(0^n\) self-loop. Thus the source \(10^{n-2}\) cannot reach the all-zero target after deletion. If \(i=n-1\), the forbidden edge is \(0^{n-1}1\). The all-zero source cannot leave its vertex except by that forbidden edge, so it cannot reach the distinct target. This proves both infinite cases.

**3. Lower bound on repairing paths.** Now assume \(1\le i,j\), so \(u=0^i1 0^{j-1}\) and \(v=0^{i-1}1 0^j\). A path of length \(d\) spells a string \(T\) of length \(n-1+d\), beginning in \(u\) and ending in \(v\); its \(d\) length-\(n\) windows are exactly the traversed edges. A path of length \(1\) spells only \(f_i\) and is forbidden.

Suppose \(2\le d<n\). The prefix \(u\) forces a \(1\) at zero-based position \(i\), while the suffix \(v\), beginning at position \(d\), forces a distinct \(1\) at position \(d+i-1\). All positions of \(T\) belong to these prefix and suffix intervals, which overlap or touch since \(d<n\); thus these are the only two ones. For these requirements to be consistent, the second one must lie after the prefix and the first one must lie before the suffix. Therefore
\[
d\ge n-i=j+1,\qquad d\ge i+1.
\]
The first length-\(n\) window of \(T\) would equal the forbidden \(f_i\) unless the second one falls in that window, requiring \(d\le n-i=j+1\). Similarly, the final length-\(n\) window would equal \(f_i\) unless the first one falls in it, requiring \(d\le i+1\). Together these four inequalities imply
\[
d=i+1=j+1,\qquad i=j,\qquad n=2i+1.
\]
Thus an allowed path shorter than \(n\) can exist only for odd \(n\) and exactly centered \(i=j\), and then it must have length \(i+1=(n+1)/2\). Every symbol in that overlapping representation is forced, giving the unique candidate \(T=0^i1 0^{i-1}1 0^i\). Its windows each have two ones, so they avoid the forbidden one-one word. This proves existence, minimality, and uniqueness of that centered repair path.

**4. The remaining path and uniqueness.** The string
\[
T=0^i1 0^{j-1}1 0^{i-1}1 0^j
\]
begins in \(u\), ends in \(v\), and spells \(n\) successive allowed edges. It has three ones. For the first and final ones, the intervening central one prevents the corresponding length-\(n\) window from being \(f_i\); the middle one has neither the requisite \(i\) zeros before it nor the requisite \(j\) zeros after it. Hence no \(n\)-window along this path is forbidden. If \(i\ne j\), Part 3 excludes all paths shorter than \(n\). At length \(n\), a spelling from \(u\) to \(v\) has only one free position (the single gap between the length-\((n-1)\) prefix and suffix); filling this position with \(0\) produces the forbidden word as a window, while filling it with \(1\) gives the displayed allowed string. Thus this shortest path is unique. In the centered case the shorter unique path was already proved.

A shortest path cannot repeat a vertex (any intervening cycle could be deleted), so it cannot repeat an edge. Therefore the extra edge traversal multiset of any optimal closed walk is exactly one additional traversal of each edge of the unique shortest repair path. Euler's theorem gives a cyclic word realizing that multiset and the optimal length. This proves the formula and the exact multiplicity-profile rigidity in all cases. Complementation interchanges the two symbols and preserves the entire argument.

## Verification

The standalone Python 3 standard-library script `verify.py` implements breadth-first search in the actual forbidden-edge overlap graph independently of the closed formula, constructs a path from the displayed expressions, builds an Euler circuit after duplicating the path, and compares the literal multiset of cyclic length-\(n\) factors against the predicted required and repeated edges. Exhaustive checks cover all orders \(3\le n\le12\), all fifty-five interior forbidden positions, and all endpoint obstructions, with 74,161 positions of constructed witnesses in total. An independent literal circular-window search proves nonexistence at length \(8\) and existence at length \(9\) for order \(3\) with forbidden \(010\), and nonexistence at length \(18\) and existence at length \(19\) for both interior order-\(4\) motifs. Run `python3 verify.py` to reproduce the `VERIFY_OK` report. These finite checks corroborate the proof; the all-order statements follow from Parts 1–4, not from enumeration.

## Relationship to prior work

Chen, Kitaev and Sun (2019) study universal cycles after deleting words and identify exact-once universal-cycle obstructions when a single nonconstant word is removed. Here repeated *permitted* factors are allowed and the output is the exact shortest repetition cost, including an exceptional odd-order central saving and rigid repeat-profile classification. Moreno and Matamala (2007) study forbidden-language de Bruijn graphs and lexicographically least Eulerian sequences, but do not supply the specific non-Eulerian one-hot shortest augmentation formula. Bernardini and coauthors (2022) provide a general Eulerian-extension framework and explicitly recognize duplicate-edge balancing, which supplies standard machinery for the reduction; their published general algorithmic bounds do not state this closed all-order forbidden-one-hot formula or uniqueness of the duplicated-factor set. Alhakim (2022) constructs restricted de Bruijn sequences by preference functions while maintaining one-occurrence conditions, not an exact shortest repeated-factor census. These are statement-level comparisons, not a claim that absence of a search result proves novelty.

## Limitations

The theorem covers only single forbidden motifs with one occurrence of one symbol (and, by complementation, those with one occurrence of the other). It does not count the number of different optimal cyclic words or necklaces. The optimal-repeat rigidity concerns factor multiplicities, not a unique Euler tour or a unique host word. Its application to general forbidden sets is not asserted. Related generic Eulerian-extension theory may entail an equivalent specialization, and undiscovered older formulations remain a residual originality risk. No independent scientific audit has been performed.

## References

- H. Z. Q. Chen, S. Kitaev, and B. Y. Sun, *On the probability of existence of a universal cycle or a universal word for a set of words*, arXiv:1908.01116, first posted 2019-08-03. https://arxiv.org/abs/1908.01116
- G. Bernardini, H. Chen, G. Loukides, S. P. Pissis, L. Stougie, and M. Sweering, *Making de Bruijn Graphs Eulerian*, CPM 2022, DOI 10.4230/LIPIcs.CPM.2022.12. https://doi.org/10.4230/LIPIcs.CPM.2022.12
- A. M. Alhakim, *Designing preference functions for de Bruijn sequences with forbidden words*, Designs, Codes and Cryptography (2022), DOI 10.1007/s10623-022-01077-5. https://doi.org/10.1007/s10623-022-01077-5
- E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695 (2007). https://arxiv.org/abs/0711.1695
