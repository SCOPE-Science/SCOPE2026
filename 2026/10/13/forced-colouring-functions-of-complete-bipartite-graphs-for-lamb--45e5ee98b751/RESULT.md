# Forced colouring functions of complete bipartite graphs for \(\lambda\ge3\)
## Finding
Let \(K_{m,n}\) have shores \(A\) and \(B\), where \(|A|=m\ge1\) and \(|B|=n\ge1\). Fix an integer \(\lambda\ge3\) and \(0\le p\le1/\lambda\). In the forced-colouring random model, each available colour is assigned independently to a vertex with probability \(p\), while the vertex is initially uncoloured with probability \(1-\lambda p\).

Write
\[
Q_s(k)=k!\,{s\brace k},
\]
where \({s\brace k}\) is a Stirling number of the second kind, so that \(Q_s(k)\) counts surjections from an \(s\)-set onto a fixed \(k\)-set. Then
\[
\operatorname{FC}_{\lambda}(K_{m,n};p)=
\lambda Q_m(\lambda-1)p^m\bigl(1-(\lambda-1)p\bigr)^n
+\lambda Q_n(\lambda-1)p^n\bigl(1-(\lambda-1)p\bigr)^m
+\bigl(P(K_{m,n};\lambda)-\lambda Q_m(\lambda-1)-\lambda Q_n(\lambda-1)\bigr)p^{m+n}.
\]
Here \(P(K_{m,n};\lambda)\) is the chromatic polynomial; explicitly,
\[
P(K_{m,n};\lambda)=
\sum_{a=1}^{\min\{m,\lambda-1\}}(\lambda)_a{m\brace a}(\lambda-a)^n.
\]

Equivalently, every non-total partial \(\lambda\)-assignment that forces a proper colouring has one shore already fully coloured and using exactly \(\lambda-1\) colours, and every initially coloured vertex on the other shore has the unique missing colour. The two possible choices of the fully coloured shore account for the first two terms; the last term adds the remaining total proper colourings.

For \(\lambda=3\), this gives
\[
\operatorname{FC}_3(K_{1,2};p)=6p^2(1-p),
\]
which corrects the printed \(K_{1,2}\) specialization in arXiv:2609.17108v1. It also reproduces the paper's displayed values
\[
\operatorname{FC}_3(K_{1,3};p)=6p^3(3-5p)
\quad\text{and}\quad
\operatorname{FC}_3(K_{2,2};p)=6p^2(2-8p+9p^2).
\]

## Assumptions and scope
Graphs are finite and simple. A partial \(\lambda\)-assignment is proper on its coloured domain. An uncoloured vertex is immediately forced when its coloured neighbours exhibit exactly \(\lambda-1\) distinct colours, in which case it receives the unique missing colour; forcing is iterated until no further move is possible. The theorem concerns \(m,n\ge1\), \(\lambda\ge3\), and the probability range \(0\le p\le1/\lambda\).

The case \(\lambda=2\) is not part of the new claim: Farr's Theorem 7 already gives the exact forced-colouring function for every bipartite graph. The present result addresses the complementary regime \(\lambda\ge3\) on the canonical complete-bipartite family.

## Proof
Let a proper partial assignment be given. Because every vertex of \(A\) is adjacent to every vertex of \(B\), no colour can occur on both shores. Thus the sets of colours currently used on \(A\) and \(B\) are disjoint.

Suppose the assignment is non-total and eventually forces a proper \(\lambda\)-colouring. Consider its first forcing move. If the first forced vertex lies in \(B\), then its neighbourhood is all of \(A\), so the initially coloured vertices of \(A\) exhibit exactly \(\lambda-1\) colours. The only colour that can occur initially on \(B\) is therefore the single missing colour. Every uncoloured vertex of \(B\) now sees those same \(\lambda-1\) colours on \(A\), hence every such vertex is forced to the missing colour. After this wave, \(B\) is monochromatic. Since \(\lambda\ge3\), a monochromatic shore exhibits only one colour, fewer than \(\lambda-1\), and therefore cannot force any uncoloured vertex of \(A\). Consequently \(A\) must have been fully coloured initially. Moreover, because it exhibited \(\lambda-1\) colours, its initial colouring is surjective onto those colours.

Conversely, if \(A\) is fully coloured and surjective onto any fixed set of \(\lambda-1\) colours, while each vertex of \(B\) is either uncoloured or has the unique missing colour, then every uncoloured vertex of \(B\) is immediately forced to that missing colour. Thus the assignment forces a proper total colouring. Interchanging \(A\) and \(B\) gives the only other non-total possibility.

For the first type, choose the missing colour in \(\lambda\) ways and choose a surjection of \(A\) onto the remaining \(\lambda-1\) colours in \(Q_m(\lambda-1)\) ways. The probability contribution from the fully coloured shore is \(p^m\). Each vertex on the other shore may independently be uncoloured, with probability \(1-\lambda p\), or already have the missing colour, with probability \(p\); their combined admissible probability is \(1-(\lambda-1)p\). This yields
\[
\lambda Q_m(\lambda-1)p^m\bigl(1-(\lambda-1)p\bigr)^n.
\]
The symmetric type gives the second term.

Each of these two sums includes some total proper colourings: respectively, those in which one shore uses all \(\lambda-1\) colours and the other is monochromatic in the missing colour. For \(\lambda\ge3\) these two families are disjoint, and they contain \(\lambda Q_m(\lambda-1)\) and \(\lambda Q_n(\lambda-1)\) total colourings. Since every total proper colouring has probability \(p^{m+n}\), adding all remaining total proper colourings contributes
\[
\bigl(P(K_{m,n};\lambda)-\lambda Q_m(\lambda-1)-\lambda Q_n(\lambda-1)\bigr)p^{m+n},
\]
which proves the formula.

Finally, to obtain the displayed chromatic-polynomial expression, condition on the exact number \(a\) of colours used on \(A\). Choose and surject onto those colours in \((\lambda)_a{m\brace a}\) ways, then colour each vertex of \(B\) independently with one of the remaining \(\lambda-a\) colours.

## Verification
The proof is symbolic and covers all parameters in the stated domain. The accompanying `artifacts/verify.py` independently enumerates partial assignments for \(\lambda\in\{3,4\}\), \(1\le m,n\le3\), and \(m+n\le6\). It checks the structural if-and-only-if classification against a direct forcing simulation, then compares the closed formula with the exact rational probability sum at three values of \(p\) for every profile. It also checks the three displayed \(\lambda=3\) small examples. The replay output is:

`ALL CHECKS PASSED; profiles=18; states=31081; rational_probability_evaluations=54; lambda_values=3,4; max_order=6`

This finite computation corroborates but does not replace the general proof.

## Relationship to prior work
Farr's arXiv:2609.17108v1, first public on 2026-09-15, develops the forced colouring function and proves in Theorem 7 a closed formula for \(\lambda=2\) on every bipartite graph. For \(\lambda\ge3\), the same paper gives selected small-graph examples and proves general evaluation hardness; a targeted full-text inspection found no occurrence of “complete bipartite” and no theorem that specializes to the formula above. The paper explicitly remarks after Theorem 7 that bipartite expressions for larger \(\lambda\) are expected to be more complicated.

A published research-record search located “Exact forced 3-colouring polynomials at maximum degree two” (published-finding corpus identifier `2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd`). That result treats graphs of maximum degree at most two and separately identifies the printed \(\lambda=3\) error for \(K_{1,2}\). It does not cover \(K_{m,n}\) once both shores are nontrivial with unbounded degree, and it does not give the all-\(\lambda\) formula above.

The new theorem therefore supplies a complete exact evaluation for a canonical infinite family throughout the hard-colour regime \(\lambda\ge3\), while also explaining the small-example correction structurally.

## Limitations
The result is specific to complete bipartite graphs. The proof uses the fact that the neighbourhood of every vertex is an entire opposite shore, so it does not directly extend to arbitrary bipartite graphs or to graphs obtained by deleting edges from \(K_{m,n}\). No claim is made about faster evaluation on broader graph classes.

The originality search cannot exclude an equivalent result in a poorly indexed source using different terminology. The principal residual risk is bibliographic rather than mathematical: the invariant is recent, and literature indexing is still developing.

## References
1. G. E. Farr, “The forced colouring function of a graph,” arXiv:2609.17108v1, first submitted 2026-09-15.
2. “Exact forced 3-colouring polynomials at maximum degree two,” published-finding corpus identifier `2026/9/17/SCOPE-forced-three-colouring-max-degree-two--2226d8f07ffd`.
