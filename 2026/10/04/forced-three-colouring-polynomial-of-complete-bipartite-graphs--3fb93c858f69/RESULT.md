# Forced three-colouring polynomial of complete bipartite graphs
## Finding
Let \(m,n\ge 1\), and let \(K_{m,n}\) have bipartition \(A\cup B\) with \(|A|=m\) and \(|B|=n\). Write \(FC_3(K_{m,n};p)\) for the forced three-colouring polynomial in the sense of Farr: each vertex is independently left uncoloured with probability \(1-3p\), or receives each one of the three colours with probability \(p\), and an uncoloured vertex is forced exactly when its neighbours display precisely two distinct colours.

A partial three-assignment forces a three-colouring of \(K_{m,n}\) if and only if it belongs to exactly one of the following three classes:

1. every vertex of \(A\) is initially coloured, exactly two colours occur on \(A\), and every initially coloured vertex of \(B\) has the third colour;
2. the symmetric condition with \(A\) and \(B\) interchanged;
3. the assignment is total and both \(A\) and \(B\) are monochromatic in two distinct colours.

Consequently,
\[
FC_3(K_{m,n};p)
=3(2^m-2)p^m(1-2p)^n
+3(2^n-2)p^n(1-2p)^m
+6p^{m+n}.
\]

Equivalently, if \(F_{m,n}(x)=\sum_i \operatorname{fcol}(K_{m,n},i;3)x^i\) records forcing partial three-assignments by initial domain size, then
\[
F_{m,n}(x)
=3(2^m-2)x^m(1+x)^n
+3(2^n-2)x^n(1+x)^m
+6x^{m+n}.
\]

## Assumptions and scope
Graphs are finite and simple. Both parts of \(K_{m,n}\) are nonempty. A partial assignment that forces a proper total colouring must itself be proper on its coloured vertices. The result is specific to three available colours and to complete bipartite graphs; it makes no claim for arbitrary bipartite graphs or for \(\lambda
e3\).

## Proof
Suppose first that the initial partial assignment is not total but eventually forces a total three-colouring. Consider the first forced vertex. If it lies in \(B\), then its neighbourhood is all of \(A\), so exactly two colours already occur on the initially coloured vertices of \(A\). Any forced vertex of \(B\) must therefore receive the unique third colour.

If some vertex of \(A\) were initially uncoloured, then every coloured vertex of \(B\), whether initially coloured or subsequently forced, could only have that same third colour: properness forbids either of the two colours already used on \(A\). Hence an uncoloured vertex of \(A\) would see at most one colour in its neighbourhood and could never be forced. Therefore \(A\) was already fully coloured initially. Properness then forces every initially coloured vertex of \(B\) to use the unique third colour. Since the fully coloured side \(A\) displays exactly two colours, every still-uncoloured vertex of \(B\) is immediately forced to the third colour. This is class 1.

The same argument with the two parts interchanged gives class 2 whenever the first forced vertex lies in \(A\).

It remains to consider total initial assignments. Any proper three-colouring of a complete bipartite graph uses disjoint colour sets on the two parts. With only three colours and both parts nonempty, its colour-usage pattern is therefore \((2,1)\), \((1,2)\), or \((1,1)\). The first two patterns are already included in classes 1 and 2, while the last pattern is exactly class 3. Thus the three classes are necessary and exhaustive. Their disjointness is immediate from the number of colours used on the fully coloured parts.

For class 1, choose the two colours used on \(A\) in \(3\) ways and then choose a surjective two-colouring of \(A\), giving \(2^m-2\) choices. Every vertex of \(B\) is independently either initially uncoloured or initially given the remaining colour. In the probability model this contributes \((1-3p)+p=1-2p\) per vertex of \(B\), so class 1 contributes \(3(2^m-2)p^m(1-2p)^n\). Class 2 contributes the symmetric term. In class 3, choose an ordered pair of distinct colours for the two monochromatic parts, giving \(6\) assignments, each with probability \(p^{m+n}\). Summing gives the displayed formula.

Replacing the probability weight of each initially coloured vertex by \(x\) and each initially uncoloured vertex by \(1\) gives the generating polynomial \(F_{m,n}(x)\).

## Verification
A standalone verifier exhaustively enumerates every partial three-assignment of \(K_{m,n}\) for all \(1\le m,n\le5\). It independently implements the forcing rule, tests the structural classification above, and compares the resulting domain-size counts with the stated generating polynomial. The replay covers \(25\) biclique types and \(1,860,496\) partial assignments and reports:

`ALL CHECKS PASSED; biclique_types=25; partial_assignments=1860496; forcing_assignments=19494`

The computation is only a finite stress test. The theorem for arbitrary positive \(m,n\) follows from the analytic classification in the proof.

## Relationship to prior work
Farr introduced and developed the forced-colouring function and proved that, for fixed \(\lambda\ge3\), evaluation is generally \(#P\)-hard. The same paper gives an exact formula for \(\lambda=2\) on arbitrary bipartite graphs and lists several small connected examples for \(\lambda=3\), including \(K_{1,2}\), \(K_{1,3}\), and \(C_4=K_{2,2}\), but it does not state a formula for arbitrary \(K_{m,n}\). A published published-finding corpus finding gives exact \(FC_3\) formulas for graphs of maximum degree at most two; this covers some small bicliques, such as \(K_{1,2}\) and \(K_{2,2}\), but does not imply the formula above when \(\max\{m,n\}\ge3\).

The displayed \(K_{1,2}\) specialization in arXiv:2609.17108v1 is inconsistent with direct enumeration and with the published maximum-degree-two formula; the present theorem agrees with the direct forcing definition and specializes to \(FC_3(K_{1,2};p)=6p^2(1-p)\) and \(FC_3(K_{1,3};p)=6p^3(3-5p)\).

## Limitations
The result does not classify forced \(\lambda\)-colouring polynomials for \(\lambda\ge4\), arbitrary bipartite graphs, or complete multipartite graphs with at least three parts. No statement is made about root locations, coefficient log-concavity, or algorithmic complexity beyond the closed form for this family. Because the initiating literature is very recent, unindexed parallel work remains a residual originality risk.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, 15 September 2026. https://arxiv.org/abs/2609.17108v1
2. *Exact forced 3-colouring polynomials at maximum degree two*, published-finding corpus record `2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd`, 17 September 2026. https://github.com/published-finding corpus/2026/tree/main/2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd
