# Sharp rich-neighbor five-colouring of every cycle prism

## Finding
For every integer \(n\ge3\), the circular ladder (cycle prism) \(P_n=C_n\square K_2\) has rich-neighbor chromatic index
\[
\chi'_{\mathrm{rn}}(P_n)=5.
\]
In particular, every such connected cubic graph meets the conjectured five-colour bound for connected subcubic graphs outside \(K_4\), and the bound cannot be improved for this family.

## Assumptions and scope
All graphs are simple. Put \(V(P_n)=\{(i,s):i\in\mathbb Z/n\mathbb Z,\ s\in\{0,1\}\}\). The edges are the two rim sets \((i,s)(i+1,s)\) and the rungs \((i,0)(i,1)\). A proper edge-colouring gives distinct colours to incident edges. An edge is **rich** if its four distinct adjacent edges have pairwise distinct colours. A colouring is **rich-neighbor** if every edge has an adjacent rich edge. The rich-neighbor chromatic index is the least palette size of such a colouring.

Write a column triple \((a_i,b_i,r_i)\) for the colours of the top rim edge from column \(i\) to \(i+1\), the bottom rim edge from column \(i\) to \(i+1\), and the rung at column \(i\). Indices are cyclic. The five available colours are the integers \(0,1,2,3,4\).

## Proof
**Lower bound.** Every edge of \(P_n\) has neighbours, so a rich-neighbor colouring has at least one rich edge. Each edge joins two distinct degree-three vertices. A rich edge has four mutually differently coloured adjacent edges; properness also prohibits its own colour on those edges. Thus any such colouring uses at least five colours.

**Finite socket certificates.** The following seven cyclic lists of triples use at most five colours and satisfy both properness and the rich-neighbor property. These are exact finite certificates, not samples from an unproved pattern:

```text
length  cyclic list of (top rim, bottom rim, rung) colours
3       (1,4,3) (3,1,2) (4,2,0)
4       (0,3,4) (4,2,1) (2,4,0) (1,0,3)
5       (2,0,4) (4,3,1) (3,4,2) (2,0,1) (0,2,4)
6       (2,0,4) (4,3,1) (3,4,2) (2,0,1) (3,1,4) (1,2,0)
7       (2,0,4) (4,3,1) (3,4,2) (2,0,1) (0,4,1) (1,2,3) (3,1,0)
8       (2,0,4) (4,3,1) (3,4,2) (2,0,1) (4,2,3) (0,4,1) (3,1,2) (1,3,2)
9       (2,0,4) (4,3,1) (3,4,2) (2,0,1) (0,4,1) (1,3,2) (2,0,4) (0,4,3) (3,2,1)
```

For a direct finite check, form the three edges per column, compute all four adjacent edges of every edge, mark an edge rich precisely when these four neighbouring edge colours are distinct, and test that every edge has a marked adjacent edge. The standalone `verify.py` implements this definition without using any graph-colouring library or an optimization solver. It checks every edge in every base certificate.

**Locality lemma.** For an edge anchored in column \(i\), whether it has an adjacent rich edge is determined entirely by the triples in the five consecutive columns \(i-2,i-1,i,i+1,i+2\). Indeed, an adjacent edge to the anchored edge is at line-graph distance one, while the four neighbours of that potential rich witness are at line-graph distance at most two from the anchored edge. Each step of this kind changes the column index by at most one. Properness is even more local. Consequently, validity is determined by cyclic consecutive five-column windows.

**Gluing lemma.** The certificates of lengths \(5\), \(6\), and \(7\) share their first **four** triples, namely \((2,0,4),(4,3,1),(3,4,2),(2,0,1)\). Concatenate any nonempty ordered list of these three certificate strings and interpret the result cyclically. Every consecutive five-column window either lies within one constituent block or crosses one seam. Since every block has length at least five, no such window crosses two seams. A window crossing from a block \(A\) into a block \(B\) consists of the last \(j\) columns of \(A\) followed by the first \(5-j\) columns of \(B\), for some \(1\le j\le4\). As the first four triples of all three blocks agree, this is *exactly* a cyclic five-column window of \(A\), which passed the finite check. This reasoning applies also at the last-to-first seam. The locality lemma therefore proves that **every concatenation** is a valid five-colour rich-neighbor colouring.

**All lengths.** The independent base certificates handle \(3\le n\le9\). For \(n\ge10\), write \(n=10+r+5q\), where \(q\ge0\) and \(r\in\{0,1,2,3,4\}\). The five initial block lists for \(r=0,1,2,3,4\) are respectively \((5,5)\), \((5,6)\), \((5,7)\), \((6,7)\), and \((7,7)\). Append \(q\) blocks of length five. Their total length is \(n\), and the gluing lemma gives a five-colour rich-neighbor colouring. The lower bound then proves equality for all \(n\ge3\).

## Verification
Run `python3 verify.py` with Python 3 and no optional dependencies. The script builds each of the \(3n\) undirected edges, checks that they are distinct and that every edge has exactly four neighbours, checks all properness inequalities and rich-neighbor conditions directly, and then checks all seven certificates. It additionally checks the explicit construction for every \(10\le n\le500\) and every ordered concatenation of at most six blocks chosen from \(5,6,7\). The completed run printed `VERIFY_OK; seven base certificates; all n=10..500; 1092 socket concatenations`. These extra finite tests are consistency checks; the locality and gluing lemmas, not extrapolation from tests, prove the infinite assertion.

## Relationship to prior work
Petruševski and Škrekovski introduced rich-neighbor edge-colouring, obtained a general seven-colour subcubic bound, and conjectured five for connected subcubic graphs except \(K_4\). Kong's 2026 preprint gives the general inequality \(\chi'_{\mathrm{rn}}(G)\le3\chi'(G)\) and exact values for complete and complete bipartite graphs; this does not give a five-colour upper bound for prisms. Kong, Lin and Wang prove five colours when the induced subgraph on degree-three vertices has maximum degree at most one. Every vertex of a cycle prism has degree three, so that hypothesis does not apply. The published sparse/claw-free results give a bound of six for claw-free subcubic graphs, not the sharp value five. The exact five-colour assertion for all cycle prisms was not identified in the inspected literature or mathematical-record searches.

## Limitations
This result concerns **only** the simple cycle prisms \(C_n\square K_2\). It does not prove the five-colour conjecture for general cubic or subcubic graphs, nor classify all optimal colourings. Historical novelty is subject to independent scrutiny: the 2024 foundational article and relevant 2025 articles were available in abstract/bibliographic form but not fully inspectable through the lawful sources consulted. Their potential unexamined examples are residual priority risks. The verifier does not certify arbitrary unseen graphs or prove the concatenation lemma on its own.

## References
1. M. Petruševski and R. Škrekovski, *Proper edge-colorings with a rich neighbor requirement*, Discrete Mathematics 347 (2024), article 113803. DOI: 10.1016/j.disc.2023.113803.
2. L. Chen, Y. Tan and X. Zhou, *On the Rich-Neighbor Edge-Colorings of Subcubic Graphs*, Graphs and Combinatorics 41 (2025), article 89. DOI: 10.1007/s00373-025-02949-y.
3. J. Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:2610.21036v1 (first posted 2026-10-15), https://arxiv.org/abs/2610.21036.
4. J. Kong, Z. Lin and Y. Wang, *Rich-neighbor 5-edge-colorings of subcubic graphs whose 3-vertices induce a matching*, arXiv:2610.21868v1 (first posted 2026-10-15), https://arxiv.org/abs/2610.21868.
5. M. Kashima, M. Petruševski, J. Sedlar and R. Škrekovski, *The rich-neighbor chromatic index is linear in the maximum degree*, arXiv:2610.16446v1 (first posted 2026-10-12), https://arxiv.org/abs/2610.16446.
