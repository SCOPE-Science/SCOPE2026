# Exact forcing-colouring spectrum of clique windmills

## Finding
Fix integers \(q\ge 3\) and \(n\ge 2\). Let \(W_{q,n}=K_1\vee(nK_{q-1})\) be the finite labelled clique windmill: \(n\) complete graphs of order \(q\), all sharing exactly one hub and otherwise vertex-disjoint. Its chromatic number is \(q\). A partial assignment assigns each vertex either no colour or a colour from \(\{1,\ldots,q\}\). An initially uncoloured vertex may be forced when precisely \(q-1\) different colours appear on its already coloured neighbours, in which case it receives the missing colour. An assignment *forces* if iterating this rule yields a proper total \(q\)-colouring.

Let \(f_j(W_{q,n})\) denote the number of forcing partial assignments initially colouring exactly \(j\) vertices. Then their complete cardinality polynomial is
\[
\boxed{F_{q,n}(z)=\sum_j f_j(W_{q,n})z^j
=q((q-1)!)^n z^{n(q-2)}\bigl[(1+z)(q-1+z)^n-(q-1)\bigr].}
\]
For \(m=n(q-2)\), its coefficients are, for \(0\le j\le n+1\),
\[
\boxed{f_{m+j}(W_{q,n})=q((q-1)!)^n\left[\binom nj(q-1)^{n-j}+\binom n{j-1}(q-1)^{n-j+1}-(q-1)\mathbf{1}_{\{j=0\}}\right],}
\]
where a binomial coefficient with an out-of-range lower index contributes zero, and all other coefficients are zero. Thus the minimum initial domain size that forces a proper colouring is exactly \(m\), attained by precisely
\[
\boxed{q((q-1)!)^n\bigl((q-1)^n-(q-1)\bigr)}
\]
partial assignments.

In the random partial-colouring model, each vertex independently has any specified one of the \(q\) colours with probability \(p\), and remains uncoloured with probability \(r=1-qp\), for \(0\le p\le 1/q\). Its exact forcing probability is
\[
\boxed{\operatorname{FC}_q(W_{q,n};p)=q((q-1)!)^n p^{n(q-2)}\bigl[(p+r)(p+(q-1)r)^n-(q-1)r^{n+1}\bigr].}
\]

## Assumptions and scope
All graph vertices are labelled, all graphs are finite and simple, \(q\ge3\), and \(n\ge2\). The palette is exactly the chromatic number \(q\), not an arbitrary larger palette. Distinct forcing assignments are counted by their initially coloured vertex sets *and* their assigned colour labels. The iteration must end at a proper colouring; a partial assignment using incompatible colours cannot be accepted merely because a propagation rule triggers.

## Proof
**Structural necessity.** Write \(h\) for the hub and call each outer \((q-1)\)-clique a blade. An uncoloured outer vertex has only \(q-2\) outer neighbours; hence it cannot be forced before \(h\) is coloured, because forcing requires \(q-1\) distinct already coloured neighbours. After \(h\) is coloured, if any blade still contains two or more uncoloured outer vertices, none can be forced: each has at most \(q-2\) coloured neighbours (the hub and at most \(q-3\) others). Consequently every blade must initially have at least \(q-2\) coloured vertices. This is necessary whether \(h\) starts coloured or becomes coloured later.

If \(h\) starts uncoloured, it is the only vertex that could possibly be forced first. Thus it can be forced exactly when its initially coloured outer neighbours use precisely \(q-1\) distinct colours. With fewer distinct colours there is no first move; with all \(q\) colours the colouring cannot be extended to \(h\). If \(h\) is initially coloured, or is forced in this way, every blade's at most one remaining outer vertex immediately has \(q-1\) differently coloured neighbours and is forced, provided the initial assignment is a restriction of a proper total colouring. This proves the full necessary-and-sufficient structural rule: a forcing assignment is a restriction of a proper total \(q\)-colouring, has at least \(q-2\) initially coloured vertices in each blade, and either initially colours the hub or uses all \(q-1\) non-hub colours among its outer seeds.

**Unique extensions and enumeration.** Every successful partial assignment has a unique proper total colouring, namely the one determined by the forcing sequence. There are exactly \(q((q-1)!)^n\) proper total colourings: first choose the hub colour, and then permute the remaining \(q-1\) colours independently on each blade. Fix one such total colouring. The admissible initial domain in any blade contains either all \(q-1\) outer vertices or all but one. Its generating polynomial is
\[
A(z)=z^{q-1}+(q-1)z^{q-2}=z^{q-2}(z+q-1).
\]
When the hub is initially coloured, its factor is \(z\), and all choices counted by \(A(z)^n\) force. When the hub is initially uncoloured, its factor is \(1\). The outer seeds must collectively use all \(q-1\) colours different from the hub's colour. Failure occurs precisely when every blade omits its unique outer vertex of the *same* colour: this is possible in \(q-1\) ways, each of weight \(z^{n(q-2)}\). If one blade has all vertices coloured, or different colours are omitted on different blades, the required \(q-1\) colours are represented. Hence the acceptable domain polynomial for each fixed proper colouring is
\[
(z+1)A(z)^n-(q-1)z^{n(q-2)}.
\]
Multiplying by the number of proper total colourings yields the stated complete polynomial. There is no overcounting because the final proper colouring is uniquely forced.

**Minimum and probability.** The constant term of the bracket after factoring out \(z^{n(q-2)}\) equals \((q-1)^n-(q-1)>0\) for \(q\ge3,n\ge2\), proving the sharp minimum and its multiplicity. Binomial expansion gives the full coefficient formula, including the leading coefficient \(q((q-1)!)^n\). Finally each initially coloured vertex contributes probability \(p\), and each initially uncoloured vertex probability \(r\); substituting the weighted blade factor \(p^{q-1}+(q-1)p^{q-2}r\), hub factor \(p+r\), and obstruction subtraction \((q-1)p^{n(q-2)}r^{n+1}\) gives the probability formula.

## Verification
The standalone file `verify.py` independently enumerates all \((q+1)^{1+n(q-1)}\) initial assignments for \((q,n)\in\{(3,2),(3,3),(3,4),(4,2)\}\). For each it builds the labelled graph, directly simulates forced colouring and tests final properness; separately tests the derived structural condition and compares every cardinality count against the closed formula. This examines \(357677\) initial assignments, of which \(13296\) force a proper colouring. It also checks algebraic coefficient identities on \(224\) parameter pairs. A successful run prints:

`VERIFY_OK complete_cases=4 initial_assignments=357677 forcing_assignments=13296 symbolic_profiles=224`

The proof for arbitrary \(q,n\) is the structural argument above. Finite enumeration is not its basis.

## Relationship to prior work
Farr and Morgan introduced forced-colouring polynomials and their sum-over-domain interpretation. Farr subsequently formalized the local forcing rule, proved formulas for complete graphs and small connected graphs, and established general complexity results. In particular, the one-blade boundary \(W_{q,1}=K_q\) is already covered by the complete-graph formula and is intentionally excluded from the new range. The prior chromatic-polynomial factorization over clique separators does not furnish this forcing-domain enumerator. Here a single hub couples the blades through the nonzero correction term \(-(q-1)z^{n(q-2)}\), which records the precise obstruction to forcing an initially uncoloured hub.

Related exact forcing-colouring calculations for paths, cycles, complete bipartite graphs, and complete multipartite graphs address different graph families or palettes. These formulas do not yield the expression above by direct specialisation: for \(q\ge3,n\ge2\), a clique windmill contains triangles and is not a complete multipartite graph. Searches for equivalent results under the terms *friendship graph*, *windmill*, *clique bouquet*, *forced colouring*, and *partial-colouring propagation* did not surface the full all-\(q\), all-\(n\) coefficient formula. Absence from search results is not a proof of historical novelty.

## Limitations
No conclusion is asserted for palettes strictly larger than \(q\), for blades of different sizes, or for non-clique blocks sharing the hub. The result concerns local forced completion rather than merely unique extendability or ordinary graph zero forcing. General reduction schemes could encode the same finite graph instances without giving the closed symbolic family; earlier unindexed block-gluing identities could still affect historical priority. The mathematical argument and code have not undergone independent external review.

## References
1. G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first submitted 15 September 2026. https://arxiv.org/pdf/2609.17108v1
2. G. Farr and K. Morgan, *Graph polynomials: some questions on the edge*, arXiv:2406.15746v1, first submitted 22 June 2024. https://arxiv.org/pdf/2406.15746v1
