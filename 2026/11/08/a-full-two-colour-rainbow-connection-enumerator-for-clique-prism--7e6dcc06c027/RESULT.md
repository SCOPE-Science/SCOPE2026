# A full two-colour rainbow-connection enumerator for clique prisms

## Finding
For an integer \(n\ge 2\), let \(G_n=K_2\square K_n\). Its vertices are \((a,i)\), where \(a\in\{0,1\}\) and \(i\in[n]\). Two vertices are adjacent when either their first coordinates agree and their second coordinates differ, or their first coordinates differ and their second coordinates agree. Give every edge one of the two **named** colours red and blue; proper edge colouring is not required. A colouring is rainbow-connected when every two vertices have a path on which all edge colours are distinct. Define the blue-edge enumerator
\[
R_n(z)=\sum_{\substack{\phi:E(G_n)\to\{\mathrm{red},\mathrm{blue}\}\\\phi\text{ rainbow-connected}}} z^{|\phi^{-1}(\mathrm{blue})|}.
\]
Then, for every \(n\ge 2\),
\[
\boxed{R_n(z)=\sum_{b=0}^{n}\binom nb z^b
  [z(2+z)]^{\binom{n-b}{2}}
  (1+2z)^{\binom b2}
  (1+z^2)^{b(n-b)}.}
\]
In particular, the total number of admissible named two-colourings is
\[
\boxed{R_n(1)=3^{\binom n2}\sum_{b=0}^n\binom nb\left(\frac23\right)^{b(n-b)}},
\]
and the fewest possible blue edges is \(n-1\), attained by exactly \(n^2\) colourings. Those minimizers are precisely the following two families, with all unmentioned edges red:

1. Choose one index \(s\in[n]\) and make all matching edges except the edge indexed \(s\) blue. There are \(n\) choices.
2. Choose two distinct indices \(s,t\in[n]\), make all matching edges except those indexed \(s,t\) blue, and make the edge between \(s,t\) in exactly one of the two clique layers blue. There are \(2\binom n2\) choices.

The polynomial is reciprocal in the sense that \(R_n(z)=z^{n^2}R_n(1/z)\), and its nonzero coefficients occur only at degrees from \(n-1\) through \(n^2-n+1\). Finally, as \(n\to\infty\),
\[
R_n(1)\sim 2\,3^{\binom n2}.
\]

## Assumptions and scope
All graphs are finite and simple. The labels \(a\in\{0,1\}\), \(i\in[n]\) and the red/blue palette are fixed: no quotient by automorphisms or colour exchange is taken. Every pair of adjacent vertices is automatically rainbow-connected by its single edge. For the remaining pairs, a rainbow path with only two available colours has at most two edges. Since \(G_n\) has diameter two, ordinary rainbow connectivity and strong rainbow connectivity are equivalent for these colourings. The graph has \(n^2\) edges.

## Proof
Write \(r_i\in\{0,1\}\) for the colour of matching (rung) edge \((0,i)(1,i)\), with blue encoded by one; write \(x_{ij}\) and \(y_{ij}\) for the respective colours of the edges \((0,i)(0,j)\) and \((1,i)(1,j)\), where \(i<j\).

The only nonadjacent pairs are \((0,i),(1,j)\) and \((0,j),(1,i)\), for \(i<j\). Each has exactly two possible two-edge paths. Their simultaneous rainbow connectivity is equivalent to both Boolean conditions
\[
(x_{ij}\ne r_j)\ \lor\ (r_i\ne y_{ij}),\qquad
(x_{ij}\ne r_i)\ \lor\ (r_j\ne y_{ij}).
\]
If \(r_i=r_j=c\), these conditions reduce to forbidding the single choice \(x_{ij}=y_{ij}=c\). If \(r_i\ne r_j\), the two conditions hold together **if and only if** \(x_{ij}=y_{ij}\). These are necessary and sufficient, independently for each unordered pair \(\{i,j\}\).

Condition on the set \(B\subseteq[n]\) of blue matching edges, and put \(|B|=b\). The matching edges contribute \(z^b\). For each of the \(\binom{n-b}{2}\) pairs of indices outside \(B\), the permitted ordered layer-colour pairs are red/blue, blue/red, blue/blue; their enumerator is \(2z+z^2=z(2+z)\). For each of the \(\binom b2\) pairs inside \(B\), the permitted layer-colour pairs are red/red, red/blue, blue/red; their enumerator is \(1+2z\). For the \(b(n-b)\) mixed pairs, the permitted choices are red/red and blue/blue; their enumerator is \(1+z^2\). Multiplication is valid because different unordered pairs use disjoint, unconstrained edge variables. There are \(\binom nb\) ways to select \(B\). Summing over \(b\) proves the polynomial identity and, on setting \(z=1\), its total-count identity.

If there are \(t=n-b\) red matching edges, the \(\binom t2\) corresponding same-red pairs each require at least one blue edge in a clique layer. All other clique-layer edges may be red. Thus the minimum number of blue edges with this matching pattern is exactly
\[
(n-t)+\binom t2=n-1+\frac{(t-1)(t-2)}2.
\]
For integer \(0\le t\le n\), this equals \(n-1\) only when \(t=1\) or \(t=2\). The independent pair restrictions force precisely the two classes of minimizers listed in the finding. They are disjoint, and their number is \(n+2\binom n2=n^2\).

Exchanging the named colours is an involution sending a colouring with \(k\) blue edges to one with \(n^2-k\) blue edges, proving reciprocity and the asserted support range. For the asymptotic, put \(q=2/3\). The normalized total is
\[
\frac{R_n(1)}{3^{\binom n2}}=2+\sum_{b=1}^{n-1}\binom nb q^{b(n-b)}.
\]
By symmetry and \(b(n-b)\ge bn/2\) for \(1\le b\le n/2\), the interior sum is at most \(2((1+q^{n/2})^n-1)\), which tends to zero. This proves the stated asymptotic.

## Verification
The accompanying standalone `verify.py` independently constructs \(G_n\), searches actual two-edge paths between every nonadjacent pair, and counts every named edge colouring for \(2\le n\le4\). It reproduces, respectively, \(10\), \(126\), and \(4050\) successful colourings, and \(4\), \(9\), and \(16\) minimizers. It also compares path-based tests with the local restrictions on 25,000 reproducibly sampled colourings for each \(5\le n\le8\), checks reciprocity, and independently checks the total-count specialization. Executing `python3 verify.py` ends in `VERIFY_OK`. This finite verification corroborates but is not used to justify the all-\(n\) theorem.

## Relationship to prior work
The motivating 2026 work of Barát, Boyadzhiyska, and Freschi studies the existence of red/blue rainbow length-two connections in dense graphs, including graphs near two disjoint cliques. Here the focus is a different invariant: a full, blue-edge-weighted census for the precisely defined two-clique-plus-matching product and an exhaustive description of the sparsest successful recolourings. Prior work on Cartesian-product rainbow connection provides colour-number bounds, and general work on counting rainbow-connected colourings establishes counting complexity. None of those scalar or complexity statements implies the displayed class-specific generating polynomial. General two-colour rainbow connectivity is equivalent to the existence of a rainbow length-two path between each nonadjacent pair in diameter-two graphs; the local pair factorization here is the additional ingredient.

## Limitations
The formula applies to a single, fixed labelled two-layer complete-graph product with exactly two named colours, without an edge-properness requirement. It does not enumerate connected colourings of arbitrary products or require multiple internally disjoint rainbow paths. The motivating 2026 preprint was verified at the bibliographic and abstract level but its full text was inaccessible, so historical priority is provisional. The 2024 counting-complexity chapter was likewise inspected only as an accessible publisher preview. No independent mathematical validation is claimed.

## References
1. J. Barát, S. Boyadzhiyska, and A. Freschi, *Rainbow connecting 2-colorings of super-Dirac graphs*, arXiv:2609.11437, initially posted 2026-09-10. https://arxiv.org/abs/2609.11437.
2. R. D. Barish and T. Shibuya, *Counting on Rainbow k-Connections*, Theory and Applications of Models of Computation (2024), 272–283. https://doi.org/10.1007/978-981-97-2340-9_23.
3. C. Brause, S. Jendrol’, and I. Schiermeyer, *Loose Edge-Connection of Graphs*, Graphs and Combinatorics 39 (2023), article 79. https://doi.org/10.1007/s00373-023-02669-1.
4. S. Klavžar and G. Mekiš, *On the rainbow connection of Cartesian products and their subgraphs*, Discussiones Mathematicae Graph Theory 32 (2012), 783–793. https://doi.org/10.7151/dmgt.1644.
