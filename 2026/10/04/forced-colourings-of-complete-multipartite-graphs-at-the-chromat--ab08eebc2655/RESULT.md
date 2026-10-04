# Forced colourings of complete multipartite graphs at the chromatic palette size
## Finding
Let \(r\ge 3\) and let \(G=K_{n_1,\ldots,n_r}\) be a finite simple complete \(r\)-partite graph with nonempty partite sets \(V_1,\ldots,V_r\), where \(|V_i|=n_i\). Use exactly \(r\) available colours and Farr's local forcing rule: an uncoloured vertex is immediately forced when exactly \(r-1\) different colours occur among its coloured neighbours, in which case it receives the unique missing colour.

A partial \(r\)-assignment \(f\) forces an \(r\)-colouring of \(G\) if and only if both conditions hold:

1. \(f\) is the restriction of a proper \(r\)-colouring of \(G\); equivalently, every part met by \(\operatorname{dom}f\) uses one colour and distinct met parts use distinct colours.
2. \(\operatorname{dom}f\) meets at least \(r-1\) partite sets.

Define
\[
A_i(x)=(1+x)^{n_i}-1.
\]
Then the domain-size generating polynomial for forcing partial assignments is
\[
\operatorname{FCGP}_r(G;x)=r!\left(\prod_{i=1}^r A_i(x)+\sum_{j=1}^r\prod_{i\ne j}A_i(x)\right).
\]
For \(0\le p\le 1/r\), put
\[
q=1-rp,\qquad B_i(p)=(1-(r-1)p)^{n_i}-q^{n_i}.
\]
The forced-colouring probability polynomial is
\[
\operatorname{FC}_r(G;p)=r!\left(\prod_{i=1}^r B_i(p)+\sum_{j=1}^r q^{n_j}\prod_{i\ne j}B_i(p)\right).
\]
Thus the smallest forcing domain has size \(r-1\), and the total number of forcing partial assignments is
\[
r!\left(\prod_i(2^{n_i}-1)+\sum_j\prod_{i\ne j}(2^{n_i}-1)\right).
\]

## Assumptions and scope
Graphs are finite and simple, \(r\ge3\), and every partite set is nonempty. The palette has exactly \(r=\chi(G)\) colours. The statement is about the iterative local forcing process in arXiv:2609.17108v1, not merely unique extendability. The formulas count all partial assignments, including assignments with arbitrary nonempty subsets of the seeded parts, provided their colours agree with a proper total colouring.

## Proof
Every proper \(r\)-colouring of a complete \(r\)-partite graph makes each part monochromatic and assigns different colours to different parts. Indeed, vertices from distinct parts are adjacent, so a colour cannot occur in two parts; because all \(r\) nonempty parts must be coloured with only \(r\) colours, each part receives exactly one colour.

Suppose first that a partial assignment \(f\) forces an \(r\)-colouring. Every forcing step preserves the initial colours, so \(f\) is the restriction of the resulting proper colouring. If the domain of \(f\) met at most \(r-2\) parts, then every uncoloured vertex would have coloured neighbours in at most \(r-2\) seeded parts. Since each seeded part contributes at most one colour in a proper extension, no uncoloured vertex could see \(r-1\) distinct colours. Hence no first forcing step would exist. Therefore a forcing assignment must meet at least \(r-1\) parts.

Conversely, suppose \(f\) is a restriction of a proper \(r\)-colouring and meets at least \(r-1\) parts. If it meets all \(r\) parts, then any uncoloured vertex in \(V_i\) sees the \(r-1\) distinct colours represented in the other parts, so it is immediately forced to the colour of \(V_i\). If exactly one part, say \(V_j\), is unseeded, then every vertex of \(V_j\) sees the \(r-1\) colours used on the other parts and is immediately forced to the unique missing colour. After one such step every part is seeded, reducing to the previous case. Thus the two conditions are sufficient.

For the generating polynomial, fix one of the \(r!\) proper \(r\)-colourings. In a seeded part \(V_i\), any nonempty subset may be initially coloured, contributing \(A_i(x)=(1+x)^{n_i}-1\). A forcing domain seeds either all \(r\) parts or exactly \(r-1\) parts, giving the displayed expression. The restriction determines the underlying proper total colouring uniquely, so there is no overcounting.

For the probability polynomial, an uncoloured vertex has probability \(q=1-rp\). Relative to a fixed proper colouring, a seeded part \(V_i\) contributes the total weight
\[
(p+q)^{n_i}-q^{n_i}=(1-(r-1)p)^{n_i}-q^{n_i}=B_i(p),
\]
while a completely unseeded part contributes \(q^{n_i}\). Summing the all-seeded and exactly-one-unseeded cases and multiplying by \(r!\) yields the formula. The smallest possible forcing domain chooses one vertex in each of \(r-1\) parts, so its size is \(r-1\). Evaluating the generating polynomial at \(x=1\) gives the total count.

## Verification
The accompanying `verify.py` independently reconstructs every complete multipartite isomorphism type through order six, enumerates every partial assignment, applies the forcing rule by state exploration, and compares the result with the structural characterization and both closed formulas. It also checks the \(r=2\) algebraic specialization against Farr's connected-bipartite formula as a consistency test. The replay result is:

`ALL CHECKS PASSED; multipartite_types=23; partial_assignments=224608; forceable_assignments=11454; max_order=6`

The finite computation is a stress test only; the theorem for arbitrary part sizes follows from the proof above.

## Relationship to prior work
Farr's 2026 paper defines the forced-colouring function and proves an exact formula for bipartite graphs when the palette has two colours. For a connected bipartite graph on \(N\) vertices that formula is
\[
2\bigl((1-p)^N-(1-2p)^N\bigr).
\]
The theorem above treats the chromatic-palette regime for complete multipartite graphs with \(r\ge3\). If its formula is formally specialized to \(r=2\), it reduces to Farr's connected-bipartite formula, so the new statement is compatible with the known boundary case rather than contradicting it. The inspected 2026 full text gives the bipartite \(\lambda=2\) theorem but contains no complete-multipartite theorem. Targeted searches under forced-colouring, complete-tripartite, complete-multipartite, partial-assignment, and chromatic-palette formulations found no statement implying the result.

An older forcing chromatic number asks for a smallest precolouring that uniquely determines a proper colouring; that invariant is different from the iterative local forcing probability polynomial considered here and does not supply the enumerator above.

## Limitations
The theorem assumes the number of available colours is exactly the number of partite sets. It does not give \(\operatorname{FC}_\lambda(G;p)\) when \(\lambda>r\); additional colours allow qualitatively different partial assignments and forcing patterns. The literature search cannot exclude terminology that was not surfaced by the checked sources, so an older equivalent statement remains a residual originality risk. No independent audit has been performed.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first submitted 15 September 2026.
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1; later published in *Model Theory, Computer Science, and Graph Polynomials*.
3. F. Harary, W. Slany, and O. Verbitsky, *On the Computational Complexity of the Forcing Chromatic Number*, SIAM Journal on Computing 37 (2007), 1442–1457.
