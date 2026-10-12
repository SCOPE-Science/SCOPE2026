# Optimal cyclic covers for binary words without three equal consecutive symbols

## Finding

For an integer \(n\ge 2\), let \(U_n\) consist of the binary words of length \(n\) containing neither `000` nor `111` as a consecutive factor. A *cyclic cover* is a nonempty finite binary word \(W\), regarded modulo cyclic rotation, such that (i) its periodic extension avoids `000` and `111`, and (ii) every word in \(U_n\) appears among its cyclic length-\(n\) factors; repetitions of factors are permitted. Let \(M_n\) be the least possible length \(|W|\). With Fibonacci numbers \(F_0=0\), \(F_1=1\), \(F_{j+2}=F_{j+1}+F_j\), and Lucas numbers \(L_n=F_{n-1}+F_{n+1}\), the exact answer is

\[
\boxed{M_n=2(L_n-1),\qquad n\ge2.}
\]

In particular, \(|U_n|=2F_{n+1}\), and the minimum number of repeated length-\(n\) factors (counted as occurrences in excess of one per required factor) is exactly \(2F_{n-1}-2\). For \(n=2,3,4,5,6,7,8,9,10\), the minimum lengths are \(4,6,12,20,34,56,92,150,244\). An explicit optimal cyclic cover can be constructed by balancing a finite directed overlap graph and taking an Eulerian circuit.

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\). A cyclic factor may wrap around the boundary. The restriction forbids runs of three equal symbols **even across that boundary**; the cover contains no forbidden factors and must contain every allowed factor. The same factor may be realized more than once. Length counts cyclic starting positions, not the length of an artificially unrolled string. The theorem applies to all integers \(n\ge2\), without asymptotic qualification. It does not assert a unique cover or count the distinct shortest covers.

## Proof

**1. Overlap graph and connectivity.** Fix \(n\ge3\) and put \(m=n-1\). Form a directed graph \(G_n\) with the binary words of length \(m\) avoiding `000`,`111` as vertices. Each word \(x_0x_1\cdots x_{n-1}\in U_n\) contributes one edge from its first \(m\) symbols to its last \(m\) symbols. A cyclic cover is precisely a closed walk traversing all edges at least once; its edge labels, read as successively appended bits, spell the cyclic cover. Conversely, any such closed walk spells a valid cyclic cover. The graph is strongly connected: given arbitrary vertices \(u,v\), first append a sufficiently long alternating string, starting with a bit different from the last bit of \(u\), whose final bit differs from the first bit of \(v\) (choose the parity of its length). Then append \(v\). There are no forbidden triples at either junction or internally, and after the final \(m\) append operations the terminal vertex is \(v\).

**2. Unbalanced vertices.** A vertex has indegree two precisely when its first two bits differ, and outdegree two precisely when its last two bits differ. Hence let \(S\) comprise the vertices whose first two bits differ and last two agree (indegree minus outdegree equals one), and \(T\) the vertices whose first two bits agree and last two differ (outdegree minus indegree equals one). All other vertices are balanced. The bit-complement/reversal symmetry gives \(|S|=|T|\). For \(n=3\), both sets are empty.

**3. Lower bound for required repeated edges.** For \(s=s_0\cdots s_{m-1}\in S\), let \(d(s)\) be the smallest index \(i\ge1\) for which \(s_i=s_{i+1}\) (zero-based indices). It exists because the last two bits agree. A path in \(G_n\) starting at \(s\) cannot reach \(T\) in fewer than \(d(s)\) steps: after \(j<d(s)\) shifts the first pair of its vertex is still \((s_j,s_{j+1})\), whose bits differ. Given any edge-covering closed walk, subtract one copy of every original edge and retain the nonnegative multigraph of its extra traversals. Its divergence \(\deg^+-\deg^-\) equals one at every \(s\in S\), minus one at every \(t\in T\), and zero elsewhere. Standard flow decomposition of a finite integral directed multigraph partitions its edges into one unit path starting at each source in \(S\), ending in \(T\), plus optional directed cycles (formally, pair entering and exiting arcs at balanced vertices and leave one unpaired outgoing/incoming arc at each source/sink). Consequently the number of extra edge traversals is at least \(\sum_{s\in S}d(s)\).

**4. Sharp balancing paths.** For each \(s\in S\), append precisely \(d(s)\) bits, at each step appending the complement of the current final bit. The resulting directed path is legal: it extends the original final equal pair by an opposite bit and thereafter alternates. Its endpoint \(t\) begins with the equal pair \((s_{d(s)},s_{d(s)+1})\) and ends with two unequal bits, so \(t\in T\). Crucially, these endpoints are all distinct. Indeed, the *last* equal consecutive pair of \(t\) is the final equal pair inherited from \(s\), at index \(j=m-d(s)-2\); everything following it was formed by alternating appended bits. Thus \(d(s)=m-j-2\) is recoverable from \(t\), the suffix \(s_{d(s)}\cdots s_{m-1}\) is the first \(m-d(s)\) letters of \(t\), and the missing prefix of \(s\) is uniquely determined by alternating backwards from its first recovered bit. The map \(S\to T\) is therefore injective and, because the sets have equal size, bijective. Add all these paths as repeated edges to \(G_n\). The resulting directed multigraph is balanced at every vertex, retains strong connectivity, and hence has an Eulerian circuit. It gives a cyclic cover using exactly \(\sum_{s\in S}d(s)\) extra edges, meeting the lower bound.

**5. Exact enumeration of extra edges.** Fix \(d\ge1\). The initial \(d+1\) bits of \(s\) must alternate, then the pair at indices \(d,d+1\) must agree. There are two choices for the initial bit. The remaining \(r=m-d-2\) bits must preserve the triple-avoidance rule and leave a final equal pair. Their number \(h_r\) is \(h_0=1\), \(h_1=0\), and \(h_r=F_{r-1}\) for \(r\ge2\), by the two-state recurrence recording whether the current last pair agrees. Accordingly,

\[
\sum_{r\ge0}h_rz^r=\frac{1-z}{1-z-z^2},\qquad
\sum_{n\ge4}\left(\sum_{s\in S}d(s)\right)z^{n-3}=
\frac{2z}{(1-z)(1-z-z^2)}.
\]

The coefficient identity \(\sum_{s\in S}d(s)=2F_{n-1}-2\) holds for \(n\ge4\), and also for \(n=3\) since both sides vanish. A binary length-\(n\) word without a triple is counted by the Fibonacci recurrence with initial counts two at length one and four at length two; consequently \(|U_n|=2F_{n+1}\). Adding the mandatory original edges and minimum repeated edges gives \(M_n=2F_{n+1}+2F_{n-1}-2=2(L_n-1)\) for \(n\ge3\). For \(n=2\), all four binary pairs are required, giving a lower bound of four positions, and the cyclic word `0011` attains it without a cyclic triple. This proves the result for all \(n\ge2\).

## Verification

`construct.py` constructs the overlap graph, appends the explicit balancing paths, computes an Euler circuit by edge-indexed Hierholzer traversal, and directly verifies every cyclic length-\(n\) factor and every wraparound triple for all \(3\le n\le14\). Its independent equality checks compare total cover length with the Fibonacci/Lucas formula and each extra path's endpoint with the corresponding imbalance sink. `independent_optimality.py` independently constructs the graph, runs breadth-first searches between each surplus/deficit vertex, and solves the corresponding min-cost perfect matching by a standalone Hungarian algorithm for \(3\le n\le13\). The latter computation agrees with the explicit construction at every tested size. These finite tests are cross-checks; the proof above establishes every integer \(n\ge2\).

## Relationship to prior work

Moreno and Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings* (arXiv:0711.1695, first public preprint November 12, 2007), study lexicographic minimization of exact-once Eulerian de Bruijn cycles for restricted languages; despite the word “minimum,” the objective is not the length of a repeated-edge cyclic covering walk. Tan and Shallit, *Sets Represented as the Length-n Factors of a Word* (arXiv:1304.3666), explicitly define the shortest circular witness for a prescribed set, establish general bounds, and report general computational results. The present theorem determines this shortest-witness invariant for the natural **entire family** of dictionaries \(U_n\), including the exact unavoidable multiplicity of repetitions and a closed-form optimal construction. Chee and collaborators, *Maximum Length RLL Sequences in de Bruijn Graph* (arXiv:2403.01454), study maximum-length constrained cycles without repeating prescribed states/factors, in contrast to minimum-length complete covers allowing repeated factors. Neither the general shortest-witness bounds nor the maximum nonrepeating trail statements imply the present Lucas formula. The usual directed Chinese-postman balancing framework is standard; the precise optimal pairing and its Fibonacci weight are the new statement assessed here.

## Limitations

The paper-level originality comparison is based on inspected primary texts and query searches, not an exhaustive index of unpublished computations. An inaccessible older publisher-hosted preprint on restricted-language de Bruijn constructions may contain a related special case; the residual bibliographic risk is recorded separately. No claim is made that the Euler tour, the balancing path assignment, or the optimum cyclic word is unique. The result does not cover run limits other than two, alphabets other than binary, non-cyclic superstrings, or the exact number of minimizers. The combinatorial proof is self-contained and does not rely on any unverified numerical extrapolation.

## References

1. E. Moreno and M. Matamala, *Minimum de Bruijn Sequence in a Language with Forbidden Substrings*, arXiv:0711.1695v1, November 12, 2007, https://arxiv.org/abs/0711.1695.
2. S. Tan and J. Shallit, *Sets Represented as the Length-n Factors of a Word*, arXiv:1304.3666v1, April 12, 2013, https://arxiv.org/abs/1304.3666.
3. Y. M. Chee et al., *Maximum Length RLL Sequences in de Bruijn Graph*, arXiv:2403.01454, March 2024, https://arxiv.org/abs/2403.01454.
4. Directed Chinese postman / integral-flow path-decomposition principle, standard graph-theoretic tool invoked and reconstructed in the proof.
