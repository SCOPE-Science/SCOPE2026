# Sharp universal cyclic cover of the binary golden-mean language

## Finding

For every integer \(n\ge2\), let \(\mathcal L_n\) be the set of all binary words of length \(n\) **without an internal occurrence of `11`**. Let \(T_n\) be the least length of a nonempty cyclic binary word whose periodic extension contains no `11` and whose cyclic length-\(n\) factors contain every member of \(\mathcal L_n\). Repeated length-\(n\) factors are permitted. Writing \(F_0=0\), \(F_1=1\), and \(F_{k+2}=F_{k+1}+F_k\), one has the exact **all-order** equality

\[
T_n=F_{n+2}+F_n-1.
\]

There are \(F_{n+2}\) required distinct factors, so every optimal cycle has exactly \(F_n-1\) surplus factor occurrences, counted with multiplicity. The corresponding lengths for \(n=2,3,4,5,6,7,8\) are \(3,6,10,17,28,46,75\). An explicit balancing rule followed by an Euler tour constructs a minimizer for each \(n\).

## Assumptions and scope

A cyclic word \(w=w_0\cdots w_{t-1}\), with \(t\ge1\), is read modulo \(t\). Its factor at position \(i\) is \(w_i w_{i+1}\cdots w_{i+n-1}\), with indices modulo \(t\). All length-\(n\) words are *internally admissible* when they contain no adjacent ones; **admissibility does not mean that the word itself, when repeated periodically, avoids `11`**. For instance, `101` belongs to \(\mathcal L_3\), even though the repeated word `101101...` violates the restriction at its join. Repetitions of length-\(n\) factors are allowed. No restriction is imposed on the number of different optimal cycles.

## Proof

**1. Exact overlap graph.** Set \(m=n-1\). Form the finite directed graph \(G_n\) whose vertices are all internally admissible words of length \(m\), and whose arcs correspond bijectively to internally admissible length-\(n\) words. An arc labeled \(x_1\cdots x_n\) runs from \(x_1\cdots x_m\) to \(x_2\cdots x_n\). This graph is strongly connected: append \(m\) zeros to go from any vertex to \(0^m\), then append the letters of an arbitrary target vertex. Every circular cover corresponds exactly to a closed directed walk traversing every arc at least once, and conversely. (When \(n=2\), the same interpretation remains valid.)

**2. Degree imbalance and a sharp lower bound.** At a vertex \(u\), the original outdegree is \(1+\mathbf 1_{\{u_m=0\}}\) and indegree is \(1+\mathbf 1_{\{u_1=0\}}\). Hence the vertices requiring **one unit of additional outgoing flow** are exactly those that begin with `0` and end with `1`; call them sources. The vertices requiring one unit of additional incoming flow begin with `1` and end with `0`; call them sinks. Every other vertex is balanced.

In a closed walk traversing every original arc, subtract one traversal of each original arc. The remaining multiset of traversals is a nonnegative integral flow whose divergence is \(+1\) at each source, \(-1\) at each sink, and zero elsewhere. Such a flow decomposes into one directed path from each source to a sink, together with optional directed cycles. This is the standard integral-flow path decomposition; the decomposition can be obtained by following unused positive-flow arcs from each source until a sink is reached, removing that path, and then decomposing the residual circulation into cycles.

Write each source uniquely as \(u=0^r v\), where \(r\ge1\) and the nonempty suffix \(v\) starts and ends with `1`. A directed walk of fewer than \(r\) shifts from \(u\) still starts in one of the original \(r\) zeros, and therefore cannot have reached a sink, which must start with `1`. Consequently every additional source-to-sink path has at least \(r\) arcs. Every covering closed walk therefore has **at least**

\[
S_m=\sum_{u\text{ source}}r(u)
\]

additional traversals.

**3. Matching construction.** For every source \(u=0^r v\), append `0` exactly \(r\) times, each time shifting left one position. All these shifts are admissible, and their final vertex is \(v0^r\), which is a sink. The mapping \(0^r v\longmapsto v0^r\) is a bijection from sources to sinks: its inverse removes the full terminal run of zeros from a sink and prepends exactly that many zeros. Add each of these length-\(r\) paths to the original graph as an extra copy of its arcs. The resulting directed multigraph is balanced at every vertex and has the original strongly connected graph as a spanning subgraph, so Euler's theorem supplies a directed Euler circuit. Its cyclic label covers every required factor using precisely \(S_m\) extra traversals. The lower bound is attained for each \(n\).

**4. Closed form of the extra cost.** Let \(g_\ell\) count nonempty admissible length-\(\ell\) words beginning and ending in `1`. Their ordinary generating function is

\[
\sum_{\ell\ge1}g_\ell z^\ell=\frac{z(1-z)}{1-z-z^2};
\]

indeed \(g_1=1\), \(g_2=0\), and \(g_3=1\). For \(\ell\ge4\), removing the two endpoint `1` symbols and the two forced adjacent `0` symbols leaves an arbitrary internally admissible block of length \(\ell-4\), of which there are \(F_{\ell-2}\). The same formula holds for \(\ell=3\). Each source has a unique split \(0^r v\) with \(r\ge1\) and an admissible \(v\) beginning and ending in `1`. Therefore

\[
\sum_{m\ge0}S_m z^m=\left(\sum_{r\ge1}rz^r\right)\left(\sum_{\ell\ge1}g_\ell z^\ell\right)
=\frac{z^2}{(1-z)(1-z-z^2)}.
\]

The coefficient of \(z^m\) is \(F_{m+1}-1\). As \(m=n-1\), the optimal extra traversal count is \(S_m=F_n-1\). Finally, the number of internally `11`-free words of length \(n\) is \(F_{n+2}\), by splitting on the initial symbol. Thus the minimum walk length is exactly \(F_{n+2}+F_n-1\). This proves the theorem for all integers \(n\ge2\).

## Verification

The standalone Python 3 program `verify.py` constructs the augmented directed multigraph from the proof and uses Hierholzer's algorithm to produce an Euler circuit. For each \(2\le n\le12\), it checks admissibility, the complete set of cyclic factors, the exact length, the source–sink bijection, balanced degrees, and the number of repeated occurrences. For \(2\le n\le5\) an independently structured exhaustive breadth-first search over states (current overlap vertex, covered-arc mask) checks that no shorter covering closed walk exists. Run with `python3 verify.py`. The assertions and output are finite consistency checks; the all-order minimum follows from the mathematical proof above, not from a finite computation.

## Relationship to prior work

Wang and Shallit (1998) prove an exact length \(F_n+F_{n+2}\) for a **linear** shortest word with the Fibonacci subword-complexity profile. This is the numerically closest result, but the open-versus-closed boundary condition is essential: a cyclic factor may cross the cut in up to \(n-1\) positions, so their linear extremum does not establish the extra-traversal lower bound for closed walks here.

Tan and Shallit (2013) introduce shortest witnesses for arbitrary sets of length-\(n\) factors and give universal upper bounds and small data, not this exact all-order golden-mean closed-cover formula. Moreno and Matamala (2007) consider lexicographically minimal de Bruijn cycles of *periodically admissible* length-\(n\) words, requiring each such factor once; this is a different factor family. Their target omits internally admissible words such as `101` that fail cyclic self-admissibility, whereas the present theorem must cover them and necessarily repeats some factors. Generic directed Chinese-postman theory motivates the balancing reduction but does not supply the specified Fibonacci cost without the source-to-sink distance calculation and matching construction given here.

## Limitations

The theorem concerns only the binary alphabet with the single forbidden adjacent pattern `11` and every \(n\ge2\). It does not count, classify, or assert uniqueness of optimal cyclic covers, and it makes no claim for other forbidden languages, mixed alphabets, or additional error constraints. Although the compared sources did not establish this exact all-order statement, the possibility of an earlier unindexed equivalent result remains a bibliographic risk.

## References

1. M.-w. Wang and J. Shallit, “On Minimal Words With Given Subword Complexity,” *Electronic Journal of Combinatorics* 5 (1998), #R35; published 1998-07-15. DOI: 10.37236/1373. https://www.combinatorics.org/ojs/index.php/eljc/article/view/v5i1r35
2. S. Tan and J. Shallit, “Sets Represented as the Length-n Factors of a Word,” arXiv:1304.3666v1 (2013-04-12). https://arxiv.org/abs/1304.3666
3. E. Moreno and M. Matamala, “Minimum de Bruijn Sequence in a Language with Forbidden Substrings,” arXiv:0711.1695v1 (2007-11-12). https://arxiv.org/abs/0711.1695
