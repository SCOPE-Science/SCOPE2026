# Optimal sub-quorum colourings of complete multipartite graphs: a sharp rigidity threshold

## Finding

A **sub-quorum colouring** is an onto partial vertex-colouring of a finite simple graph in which each coloured vertex has at least half of its **coloured closed neighbourhood** in its own colour. Colours are distinct named labels unless stated otherwise. Let
\[
G=K_{n_1,\ldots,n_r},\quad r\ge2,\quad n_i\ge1,\quad N=\sum_{i=1}^r n_i,\quad M=\max_i n_i\ge3,
\]
and let \(p=|\{i:n_i=M\}|\). All graph vertices and the multipartite parts are fixed and labelled, and an uncoloured vertex does not belong to any colour class.

**Theorem (complete classification of optimal colourings).** The maximum sub-quorum palette size is \(M\). Every sub-quorum colouring attaining \(M\) colours has exactly one of the following forms:

1. **Pure maximum part:** Colour every vertex of one part of size \(M\) with a distinct colour and leave all other vertices uncoloured.
2. **One shared outsider (only \(M=3\)):** Colour the three vertices of one part of size three distinctly, colour exactly one vertex outside this part with one of those same three colours, and leave every other vertex uncoloured.
3. **Two matched triples (only \(M=3\)):** Choose two distinct parts of size three, colour all six vertices with three colours, each used once in each part, and leave all other vertices uncoloured.

There are no other optimum colourings. If \(U(G)\) counts optimal colourings with the names of colours forgotten, and \(T(G)\) counts surjective colourings onto the fixed palette \(\{1,\ldots,M\}\), then
\[
U(G)=\begin{cases}
 p(3N+3p-11),&M=3,\\
 p,&M\ge4,
\end{cases}\qquad T(G)=M!\,U(G).
\]
Equivalently, for \(M=3\), the three disjoint families have respectively \(p\), \(3p(N-3)\), and \(6\binom p2\) unlabelled-colour configurations.

## Assumptions and scope

The graph is a finite, simple, connected complete multipartite graph with at least two nonempty parts and largest part size at least three. The sub-quorum condition is imposed only on coloured vertices and counts only coloured vertices in a closed neighbourhood. No proper-colouring constraint is imposed. All vertices are distinguished, all \(M\) named colours must be used, and swapping colour names produces a different named colouring.

## Proof

Write \(S\) for the coloured support and \(H=G[S]\). Suppose \(H\) has \(s\ge1\) vertices and the largest of its nonempty multipartite parts has size \(a\). Every closed neighbourhood in \(H\) contains at least \(s-a+1\) vertices. If a colour class is nonempty, its size is therefore at least \((s-a+1)/2\). Thus, for \(a\ge2\) and \(s\ge a+2\), any sub-quorum colouring with \(k\) colours satisfies
\[
k\le \frac{2s}{s-a+1}<a+1,
\]
because \((a-1)(s-a-1)>0\); hence \(k\le a\). For \(s=a\), the support is an independent set and \(k\le a\). For \(s=a+1\), it is the star \(K_{a,1}\), and an \((a+1)\)-colouring would make every vertex a differently coloured singleton, violating the quorum condition at the centre. So \(k\le a\) also in this case. If \(a=1\), \(H\) is complete, each colour class occupies at least half its vertices, and \(k\le2\). Therefore in all cases
\[
k\le\max\{2,a\}.
\]
Colouring one entire original part of size \(M\) with distinct colours and leaving the other vertices uncoloured attains \(k=M\). Since \(M\ge3\), an optimum support must satisfy \(a=M\), and hence contains *all* \(M\) vertices of at least one maximum part, say \(A\).

Let \(t=|S\setminus A|\). The coloured support has \(M+t\) vertices, and the coloured closed neighbourhood of every vertex contains at least \(t+1\) vertices, so each of its \(M\) colour classes has at least \(\lceil(t+1)/2\rceil\) vertices. In particular,
\[
M\frac{t+1}{2}\le M+t,
\qquad\text{so}\qquad t(M-2)\le M.
\]
For \(M\ge4\), this gives \(t\le2\). The case \(t=2\) would require at least two vertices in each of \(M\) colour classes, hence \(2M\le M+2\), which is impossible. If \(t=1\), the \(M+1\) coloured vertices in \(M\) nonempty colour classes consist of exactly one class of size two and \(M-1\) singleton classes. The sole outsider is adjacent to all \(M\) vertices in \(A\), and sees at most two vertices of its own colour in its coloured closed neighbourhood of size \(M+1\ge5\), again impossible. Thus \(t=0\) and the pure maximum-part family is exhaustive when \(M\ge4\).

Now put \(M=3\). The same inequality yields \(t\le3\). If \(t=2\), each of the three classes would contain at least two vertices, contradicting \(|S|=5\). At \(t=0\), the sole coloured part is a triple with three distinct colours, giving the first family. At \(t=1\), the support is a star on four vertices with three nonempty colour classes. Exactly one class has size two; the outside vertex must belong to that class, since its closed coloured neighbourhood has size four and it needs at least two members of its own colour. Its partner is one of the three vertices in \(A\). These and only these configurations form the second family.

At \(t=3\), \(|S|=6\), and all three colour classes have size at least two, so each is exactly a pair. Every vertex in \(A\) has three coloured neighbours outside \(A\), and must be paired with an outsider of its own colour; a pair inside \(A\) could not satisfy its coloured closed-neighbourhood quorum. Hence the pairs give a perfect matching between \(A\) and the three outsiders. Each outsider sees all three vertices in \(A\), so its coloured closed neighbourhood already contains four vertices, of which exactly two have its own colour. If any two outsiders occupied distinct multipartite parts, they would be adjacent, raising one outsider's coloured closed-neighbourhood size to at least five and violating its quorum. Therefore the outsiders form one entire second part of size three, and the three classes are exactly the crossing pairs described in the third family. Conversely, each crossing pair occupies two of the four vertices in every coloured closed neighbourhood, so all these colourings are valid.

The listed families are disjoint. There are \(p\) ways to choose the pure part. If \(M=3\), the single-outsider construction has \(p(N-3)\) choices of full part and outsider, and three choices of which of the triple's colours to reuse. The two-triple construction has \(\binom p2\) unordered pairs of full parts and \(3!\) bijections between them. These give \(U(G)\) as stated. Every optimal colouring uses all \(M\) colours, so naming its colour classes in \(M!\) ways gives \(T(G)\), completing the proof. \(\square\)

## Verification

The standalone, dependency-free program `verify_subquorum.py` directly enumerates canonical partial colour partitions of the labelled vertices. It checks the closed-neighbourhood majority condition without using the theorem's formula and separately checks the claimed structural family of every optimum. Running `python3 verify_subquorum.py` produced:

```
VERIFY_OK profiles=66 classified_optimal_unlabeled=629 smallest_part=1 maximum_order=10
EXAMPLE (3, 1) normalized=4 named=24
EXAMPLE (3, 3) normalized=26 named=156
EXAMPLE (3, 3, 3) normalized=75 named=450
EXAMPLE (4, 3, 3) normalized=1 named=24
EXAMPLE (4, 4, 1) normalized=2 named=48
EXAMPLE (5, 5) normalized=2 named=240
```

The exhaustive checks cover every integer-part-size profile with at least two parts, maximum at least three, and total order four through nine, plus six selected order-ten profiles. They are finite cross-checks; the proof above establishes the infinite-family statement.

## Relationship to prior work

Ma, Sahbi, and Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128v4, Theorem 6.4, determine the maximum number of colours as \(\max\{2,M\}\) for complete multipartite graphs and use a bound on minimum quorum-class sizes. That established scalar result is not claimed here. The contribution here is the complete classification and enumeration of every optimum colouring for \(M\ge3\), including the sharp change between \(M=3\) and \(M\ge4\). The present proof refines the local size inequality in the same paper to its equality cases.

Hedetniemi, Hedetniemi, Laskar, and Mulder developed quorum colourings on the *entire* vertex set and determined full-support quorum numbers for certain bipartite graphs. The present result concerns *partial* support and cannot be inferred from their full-support counts. In particular, the three-colour branch counts configurations using one or two selected parts rather than full-support colourings.

## Limitations

No formula is asserted here for graphs whose largest part has size one or two. The result does not count suboptimal colourings, colourings modulo graph automorphisms, or graphs that are not complete multipartite. The structural proof establishes the specified infinite cases; finite enumeration is not a proof beyond its checked orders. Historical-priority evaluation could change if an equivalent optimiser classification is located in other literature.

## References

1. Haobo Ma, Rafik Sahbi, and Wenlin Zhang, *Sub-quorum colorings of graphs*, arXiv:2609.25128v4 (10 October 2026), especially Definitions 2.2 and Theorem 6.4; initial version submitted 20 September 2026. https://arxiv.org/abs/2609.25128
2. Sandra M. Hedetniemi, Stephen T. Hedetniemi, Renu Laskar, and Henry Martyn Mulder, *Quorum Colorings of Graphs*, Econometric Institute Report EI 2012-20 (13 September 2012), especially Proposition 17. https://repub.eur.nl/pub/37620/EI2012-20.pdf
3. Rafik Sahbi, *On the complexity of some quorum colorings problems of graphs*, AKCE International Journal of Graphs and Combinatorics 17 (2020), 784–787. https://doi.org/10.1016/j.akcej.2019.12.010
