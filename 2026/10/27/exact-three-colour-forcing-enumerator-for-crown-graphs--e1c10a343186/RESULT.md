# Exact three-colour forcing enumerator for crown graphs

## Finding
For each integer \(n\ge4\), let \(\operatorname{Cr}_n\) be the crown graph with vertex classes \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) and edges \(a_i b_j\) exactly when \(i\ne j\). Under local three-colour forcing with named colours \(\{0,1,2\}\), let \(H_n(z)=\sum_{k=0}^{2n}h_{n,k}z^k\) enumerate successful partial proper assignments having exactly \(k\) initially coloured vertices. Success means that repeatedly giving an uncoloured vertex its unique available colour whenever two distinct colours are already present in its neighbourhood eventually produces a proper total three-colouring. Then
\[
\boxed{\begin{aligned}
H_n(z)={}&6z^{2n}\\
&+6z^n\left[(2^n-2-2n)(1+z)^n+2nz(1+z)^{n-1}\right]\\
&+6nz^2\left[(1+z)^{2n-2}-1\right].
\end{aligned}}
\]
In particular, the minimum size of a successful initial assignment is exactly \(3\); there are exactly \(12n(n-1)\) such minimum assignments. The graph has exactly \(6(2^n+n-1)\) proper three-colourings with the colours named (some colours may be unused). The corresponding forced-colouring probability polynomial is
\[
\operatorname{FC}_3(\operatorname{Cr}_n;p)
=(1-3p)^{2n}H_n\!\left(\frac{p}{1-3p}\right),\qquad 0\le p\le\frac13,
\]
where the right side is interpreted by polynomial continuity at \(p=1/3\).

**Sensitivity consequence.** With the same three-colour forcing rule, the complete bipartite graph \(K_{n,n}\) has minimum successful seed size \(n\), whereas deleting only one perfect matching gives \(\operatorname{Cr}_n\), with minimum seed size \(3\). The difference \(n-3\) grows without bound.

## Assumptions and scope
Graphs are finite, simple and labelled. The parameter \(n\) is any integer at least \(4\). There are exactly three **named** colours; two different assignments of colour names count separately. Uncoloured vertices contribute no neighbour colours. A forcing step is legal only when the uncoloured vertex sees exactly two distinct colours, and successful initial assignments must have a final proper colouring. The polynomial counts initial assignments, not orders of forcing moves. The empty assignment does not succeed.

## Proof
**1. Exhaustion of terminal proper colourings.** In any proper colouring, if a colour appears on both sides, its two occurrences must be the nonadjacent matched pair \(\{a_i,b_i\}\): sharing the same colour at an unmatched pair would create a monochromatic edge, and adding any third occurrence of that colour creates an edge. Two different colours cannot each be shared across opposite sides for \(n\ge4\). Indeed, if colours \(c\) and \(d\) occur on two different matched pairs, at least two other indices remain; both corresponding vertices in each side must use the only third colour, producing a monochromatic edge between unmatched indices.

Thus every proper three-colouring is exactly one of three disjoint types:

* Type I: \(A\) and \(B\) are monochromatic in two different colours; the third colour is unused. There are \(6\) total colourings.
* Type II: One entire side is bichromatic using two colours and the other side is monochromatic in the third. The bichromatic side uses both assigned colours. There are \(6(2^n-2)\) such colourings, including both possible choices of side.
* Type III: For a unique index \(i\), \(a_i,b_i\) have colour \(c\), all other \(a_j\) have colour \(a\), and all other \(b_j\) have colour \(b\), with \(a,b,c\) distinct. There are \(6n\) such colourings.

For Type III, after identifying the unique shared colour, the other two colours must be monochromatic on opposite sides. Any further mixed use would put a second colour on both sides or create a monochromatic unmatched edge. Counting the three disjoint types gives \(6(2^n+n-1)\) total proper colourings.

**2. Forcing domains of Type I.** Every vertex has all its neighbours in a single monochromatic class, so no uncoloured vertex can see two colours. Precisely the completely coloured assignment succeeds. This contributes \(6z^{2n}\).

**3. Forcing domains of Type II.** Suppose \(A\) is bichromatic and \(B\) monochromatic. Every \(a_i\) sees only the single colour on \(B\), so all \(n\) vertices in \(A\) must be initially coloured. An uncoloured \(b_i\) can be forced exactly when both colours of \(A\) appear in \(A\setminus\{a_i\}\). If both colours appear at least twice, no \(b_i\) is compulsory; every subset of \(B\) can be seeded. Otherwise, since \(n\ge4\), exactly one colour occurs once, say at \(a_i\), and \(b_i\) is compulsory, while the other \(b_j\) are optional. Among onto two-colourings of \(A\), exactly \(2n\) have a singleton colour class and \(2^n-2-2n\) do not. For each side choice, there are \(3\) ways to choose the monochromatic side's named colour. Therefore Type II contributes
\[
6z^n\left[(2^n-2-2n)(1+z)^n+2nz(1+z)^{n-1}\right].
\]
The criterion is necessary since forcing never changes the colours on the completely seeded side; it is sufficient by forcing each unseeded vertex on the opposite side directly.

**4. Forcing domains of Type III.** Both \(a_i\) and \(b_i\) must initially be coloured: either sees only one colour in its neighbourhood even in the final colouring. If none of the other \(2n-2\) vertices is initially coloured, no forcing step is possible, since the only initially visible colour is \(c\). Conversely, one further seeded vertex suffices. For example, suppose it is \(a_j\) with \(j\ne i\). Every \(b_k\) with \(k\notin\{i,j\}\) sees seeded \(a_i\) and \(a_j\), so is forced; next every \(a_l\) with \(l\notin\{i,j\}\) sees \(b_i\) and at least one of those newly coloured \(b_k\), with \(k\ne l\), since \(n-2\ge2\). Finally \(b_j\) sees \(a_i\) and another newly coloured \(a_l\) and is forced. The case of an extra seeded \(b_j\) is symmetric. Any further initially seeded vertices agreeing with the terminal colouring cannot obstruct these forces. Thus the successful domains are exactly those containing the matched pair and at least one further vertex. Their contribution is \(6nz^2((1+z)^{2n-2}-1)\).

**5. No double counting and consequences.** A successful proper partial assignment has a unique terminal proper colouring: each local forced colour is the only colour available, so it must agree with every possible proper extension. Therefore the three disjoint terminal types give disjoint collections of initial assignments. Summing their contributions proves the displayed polynomial. Its least nonzero exponent is \(3\), exclusively from Type III, with coefficient \(6n(2n-2)=12n(n-1)\). Evaluating at full seed size gives the preceding chromatic-colouring count.

For \(K_{n,n}\), each side is monochromatic in a proper two-used-colour terminal colouring, which cannot force any uncoloured vertex using three colours. In a proper three-used-colour terminal colouring, one side uses two colours and the other uses one; all vertices of the two-colour side must be initially present because each sees only one colour on the opposite side. Hence at least \(n\) seeds are required, and seeding an entire two-colour side attains this bound. Deleting the perfect matching changes the minimum from \(n\) to \(3\).

## Verification
The standalone file `verify_crown.py` constructs each crown graph directly, enumerates every assignment over the three colours and the uncoloured state, rejects improper initial assignments, and repeatedly executes legal forcing steps. It independently enumerates the claimed coefficient formula. It checks all \(4^{8}\) assignments for \(n=4\) and all \(4^{10}\) assignments for \(n=5\); the two polynomials agree coefficient by coefficient. It also checks \(n=3\) as an excluded boundary case, where the formula does not apply. Run `python3 verify_crown.py` without third-party packages. The infinite statement is proved by the structural arguments above, not by this finite enumeration.

## Relationship to prior work
Farr defined and studied the forced-colouring function, including its probability interpretation, basic properties and examples on graphs with at most four vertices [1]. Existing exact results for complete bipartite graphs under three-colour forcing and general results for complete multipartite hosts do not imply the crown-graph formula: deleting a perfect matching changes every vertex's set of neighbours and permits a shared colour on a matched nonedge. Other crown-graph results concerning odd colouring or conflict-free colouring impose different local conditions. The maximum-degree-two forced-colouring formulas apply to \(\operatorname{Cr}_3=C_6\), not to \(n\ge4\). The enumerator and the unbounded seed-number contrast are the claims made here; no historical-priority guarantee beyond the cited comparisons is asserted.

## Limitations
The theorem requires \(n\ge4\) and exactly three named colours. The boundary \(\operatorname{Cr}_3=C_6\) has different proper-colouring types; no claimed formula extends to it. The theorem does not classify forcing polynomials for arbitrary matching-deleted bipartite graphs, other colour palettes, or all graph classes. Exhaustive computations establish only the checked finite instances; historical priority and independent mathematical verification remain open.

## References
[1] G. E. Farr, *The forced colouring function of a graph*, arXiv:2609.17108v1, first posted 15 September 2026, especially Sections 2–3 and 6, https://arxiv.org/abs/2609.17108.
[2] *Crown graph*, standard graph definition and notation, https://mathworld.wolfram.com/CrownGraph.html.
