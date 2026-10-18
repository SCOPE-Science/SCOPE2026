# Exact rich-neighbor five-edge-colourings of circular and Möbius ladders

## Finding

**Theorem.** For each integer \(n\ge3\), let \(P_n=C_n\square K_2\) be the circular ladder on \(2n\) vertices, and let \(M_{2n}\) be the Möbius ladder on \(2n\) vertices. Then
\[
\chi'_{\mathrm{rn}}(P_n)=\chi'_{\mathrm{rn}}(M_{2n})=5.
\]
The same explicit five-colour construction works for either closure except for three small values of \(n\), where explicit verified tables are supplied. This settles the conjectured five-colour target for these two infinite families of cubic graphs; it does not settle the general subcubic conjecture.

## Assumptions and scope

All graphs are finite and simple. Two edges are adjacent when they share a vertex. In a proper edge-colouring, an edge is **rich** if its *open* edge-neighbourhood has pairwise distinct colours; the colour of the edge itself is not counted in that open neighbourhood. A proper edge-colouring is **rich-neighbor** when each non-isolated edge is adjacent to a rich edge. The minimum palette size is \(\chi'_{\mathrm{rn}}\).

Use the indexed model \(L_n^\tau\), \(\tau\in\{0,1\}\), on vertices \((r,i)\) with \(r\in\{0,1\}\), \(i\in\{0,\ldots,n-1\}\). It has the \(n\) rungs \((0,i)(1,i)\), the horizontal edges \((r,i)(r,i+1)\) for \(0\le i<n-1\), and the closing horizontal edges \((r,n-1)(r\oplus\tau,0)\). Thus \(L_n^0=P_n\), and \(L_n^1=M_{2n}\). For \(n\ge3\), both are simple connected cubic graphs with exactly \(3n\) edges.

The colours are the integers \(0,1,2,3,4\). A column sequence \((a_i,c_i)\) assigns colour \(a_i\) to *both* horizontal edges indexed by \(i\), including twisted closing edges if applicable, and colour \(c_i\) to rung \(i\). All indices on the column sequences are read cyclically modulo \(n\).

## Proof

**Lower bound.** Every edge of either cubic ladder is adjacent to four edges. An edge can be rich only if those four edges have four distinct colours. Because a proper edge-colouring gives that edge a colour different from all its neighbours, any colouring containing a rich edge needs at least five colours. Every edge has a neighbour and hence a rich-neighbor colouring must contain a rich edge. Thus \(\chi'_{\mathrm{rn}}\ge5\).

**Local-state lemma.** Suppose the colours \(a_i,c_i\) satisfy, for every column \(i\),
\[
\left|\{a_{i-1},a_i,c_i\}\right|=3,
\qquad
\left|\{a_{i-1},a_{i+1},c_i,c_{i+1}\}\right|=4.
\]
The first condition makes the three edges incident with each vertex pairwise differently coloured, including at the twisted seam. The four neighbours of each horizontal edge indexed by \(i\) have colours \(a_{i-1},a_{i+1},c_i,c_{i+1}\), so **every horizontal edge is rich**. Every rung is adjacent to horizontal edges, and every horizontal edge has an adjacent horizontal edge. Consequently, the colouring is rich-neighbor, for either value of \(\tau\).

**State concatenation lemma.** Write \(s_i=(a_{i-1},a_i,c_i)\). Define a permitted transition from \((x,y,z)\) to \((u,v,w)\) by \(y=u\), by the pairwise distinctness of \(u,v,w\), and by the pairwise distinctness of \(x,v,z,w\). A cyclic sequence of states with all transitions permitted gives exactly the two displayed conditions. If several permitted *cyclic* state sequences begin with the same state, concatenating their state lists yields another permitted cyclic sequence: every new join is simply the old last-to-first transition. This observation is valid for an arbitrary number of blocks and needs no limiting argument.

The following four pairs of rows are explicit cyclic blocks; each begins with the state \((0,1,3)\), and checking each successive pair, including the closing pair, against the transition rule verifies the lemma's conditions. In each block, the first row is the sequence \(a\) and the second row is the sequence \(c\):

```text
length   a (successive columns)             c (successive columns)
   5     1 2 3 4 0                          3 4 0 1 2
   6     1 2 0 1 2 0                        3 4 3 4 3 4
   8     1 2 0 4 2 1 4 0                    3 4 3 1 3 0 3 2
   9     1 2 0 1 3 0 1 4 0                  3 4 3 4 2 4 2 3 2
```

The length-five and length-six blocks solve \(n=5,6\). For every \(n\ge8\), choose the unique \(b\in\{8,9,10,11,12\}\) with \(n\equiv b\pmod5\). The base words of lengths \(8,9,10,11,12\) are formed respectively from blocks \((8)\), \((9)\), \((5,5)\), \((5,6)\), \((6,6)\). Concatenate this base with \((n-b)/5\) copies of the length-five block. The common initial state makes all joins valid. The local-state lemma therefore produces a five-colour rich-neighbor edge-colouring of both \(L_n^0\) and \(L_n^1\) for every \(n\ge5\), \(n\ne7\).

**Exceptional orders.** For \(n=3,4,7\), the following tables each give the colours of the top horizontal edges in index order, then the bottom horizontal edges, then the rungs, using the indexed model. Every edge is properly coloured and every edge is adjacent to a rich edge, verified directly from the four-edge neighbourhoods; the rich-horizontal-edge indices for each case are listed in the verification record.

```text
n  tau  top horizontal          bottom horizontal       rungs
3   0   0 4 1                   0 4 1                   2 3 2
3   1   0 4 1                   0 4 1                   2 3 2
4   0   0 4 2 1                 1 2 0 3                 2 3 1 4
4   1   0 3 2 0                 1 2 3 1                 2 4 1 4
7   0   0 4 3 1 2 4 1           0 4 3 1 2 4 1           2 1 2 0 3 0 3
7   1   0 4 3 1 2 4 1           0 4 3 1 2 4 1           2 1 2 0 3 0 3
```

This covers every integer \(n\ge3\) and both closures. Combining with the lower bound proves the theorem. \(\square\)

## Verification

Run `python3 verify.py` using only the Python standard library. It computes graph incidence and every open edge-neighbourhood from the labelled graph, checks properness and rich-neighbor coverage independently of the state proof, verifies the four finite cyclic blocks, and tests all six exceptional assignments. It succeeds for all \(996\) graph instances corresponding to \(3\le n\le500\) and both seam closures, with the final line `VERIFIER_OK`. The exact finite checks authenticate the stated block and exception certificates; they do not themselves prove the infinite theorem. The infinite step is the state concatenation and the complete arithmetic decomposition of lengths.

## Relationship to prior work

Petruševski and Škrekovski introduced rich-neighbor edge-colourings and conjectured five colours for connected subcubic graphs other than \(K_4\) [1]. Chen, Tan and Zhou proved this target under the hypothesis that no two degree-three vertices are adjacent [2]. Chen, Nan and Zhou obtained other bounds for sparse graphs [3]. Our cubic ladders violate the disjoint-degree-three hypothesis maximally: every vertex has three degree-three neighbours. The present proof gives an exact value for two explicit infinite families rather than a general subcubic theorem.

Several independently released 2026 preprints provide further general bounds and results for graphs whose degree-three vertices induce a matching [4–6]. Their bounds do not yield the five-colour claim for cubic ladders. These later preprints are included only for coverage comparison, not as the dated motivating source. The distinction between rich-neighbor colouring and normal or strong edge-colouring is essential: the proof guarantees richness of the horizontal edges, not of every rung.

## Limitations

The general subcubic five-colour conjecture remains open. Full-text access to the original 2024 article and the full 2025 paper was not obtained, so an unadvertised family-specific statement in those papers cannot be categorically excluded. Bibliographic priority is therefore subject to further verification; the mathematics here is a self-reviewed proof, not independently validated. Finite computations are auxiliary to the infinite proof.

## References

[1] M. Petruševski and R. Škrekovski, *Proper edge-colorings with a rich neighbor requirement*, Discrete Mathematics 347 (2024), 113803. DOI: `10.1016/j.disc.2023.113803`.

[2] L. Chen, Y. Tan and X. Zhou, *On the Rich-Neighbor Edge-Colorings of Subcubic Graphs*, Graphs and Combinatorics 41 (2025), article 89, published 2025-07-28. DOI: `10.1007/s00373-025-02949-y`.

[3] L. Chen, C. Nan and X. Zhou, *On the rich-neighbor edge-coloring of sparse graphs*, Discrete Applied Mathematics 378 (2026), pp. 538–546. DOI: `10.1016/j.dam.2025.08.043`.

[4] J. Kong, Z. Lin and Y. Wang, *Rich-neighbor 5-edge-colorings of subcubic graphs whose 3-vertices induce a matching*, arXiv:`2610.21868`, first posted 2026-10-15.

[5] J. Kong, *Linear bounds for rich-neighbor edge-colorings*, arXiv:`2610.21036`, first posted 2026-10-15.

[6] M. Kashima, M. Petruševski, J. Sedlar and R. Škrekovski, *The rich-neighbor chromatic index is linear in the maximum degree*, arXiv:`2610.16446`, first posted 2026-10-12.
