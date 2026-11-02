# Six-cycle saturation obstruction for strong edge coloring of star products

## Finding

For every integer \(r\ge 2\), the strong chromatic index of the Cartesian product of a star and a six-cycle is
\[
\boxed{\chi'_s(K_{1,r}\square C_6)=2r+5.}
\]
Here a strong edge coloring assigns different colors to any two edges whose endpoint sets meet or have an edge between them; equivalently, each color class is an induced matching.

As a consequence, for **every finite simple graph** \(G\) of maximum degree \(\Delta\ge2\),
\[
\boxed{\chi'_s(G\square C_6)\ge2\Delta+5.}
\]
This lower bound is sharp for every \(\Delta\ge2\), witnessed by \(G=K_{1,\Delta}\). The known two-leaf instance \(\chi'_s(P_3\square C_6)=9\) is included, but the exact formula for arbitrary stars and the general lower bound are the contributions here.

## Assumptions and scope

All graphs are finite, undirected and simple. The six-cycle has vertex set \(\mathbb Z_6\), with indices taken modulo six. Write the vertices of \(K_{1,r}\square C_6\) as \((0,i)\) for the center and \((a,i)\) for leaves \(1\le a\le r\). There are three kinds of edges:

* Spokes \(s_{a,i}=(0,i)(a,i)\).
* Center-cycle edges \(h_i=(0,i)(0,i+1)\).
* Leaf-cycle edges \(e_{a,i}=(a,i)(a,i+1)\).

Two different edges conflict exactly when they share a vertex or an endpoint of one is adjacent to an endpoint of the other. This is the strong-coloring condition, not ordinary proper edge coloring. The case \(r=1\) is excluded: the known value for \(K_2\square C_6\) is eight, and the formula above would give seven.

## Proof

**1. A saturated local clique.** For every index \(i\) and leaf \(a\), consider the following set of edges:
\[
\mathcal Q_{i,a}=\{s_{b,i},s_{b,i+1}:1\le b\le r\}
\cup\{h_{i-1},h_i,h_{i+1},e_{a,i}\}.
\]
The \(2r+4\) edges in this set are pairwise conflicting. Indeed, two spokes within the same layer meet at its center; spokes in consecutive layers have adjacent center endpoints. Each of the three indicated center-cycle edges conflicts with both spoke layers and with the other two center-cycle edges. The leaf-cycle edge conflicts with both spoke layers through the center endpoints and with all three center-cycle edges through its endpoints in layers \(i\) and \(i+1\). Therefore
\[
\chi'_s(K_{1,r}\square C_6)\ge2r+4.
\]

Assume, toward a contradiction, that a coloring with exactly \(2r+4\) colors exists. Since every \(\mathcal Q_{i,a}\) is a clique of that size in the strong edge-conflict graph, its edges use every color exactly once. For fixed \(i\), the spokes and center-cycle edges in \(\mathcal Q_{i,a}\) do not depend on \(a\). Consequently all the edges \(e_{a,i}\), for \(1\le a\le r\), have one and the same color, denoted \(c_i\).

**2. Six local cliques give a color identity.** Fix any color \(c\). Let \(S\) be the number of spokes of that color, \(H\) the number of center-cycle edges of that color, and \(E\) the number of indices \(i\) with \(c_i=c\). Sum the color's unique occurrence over the six cliques \(\mathcal Q_{i,1}\). Every spoke belongs to two such cliques, every center-cycle edge belongs to three, and each edge \(e_{1,i}\) belongs to one. Thus
\[
\boxed{2S+3H+E=6.}\tag{1}
\]
The six center-cycle edges form a cycle; a strong color class has at most two of them. The same is true of the six leaf-cycle edges in any one leaf. Hence \(H,E\le2\). If two edges of one of these cycles have the same color, their indices must differ by three.

**3. Forbidden spoke layers.** If \(h_i\) has color \(c\), then no spoke in any of the four layers
\[
I_i=\{i-1,i,i+1,i+2\}\pmod6
\]
can have color \(c\). Likewise, if \(c_i=c\), no spoke in any layer in \(I_i\) can have color \(c\): at the middle two layers the leaf edge conflicts with all spokes, while at layers \(i-1\) and \(i+2\) each spoke \(s_{a,j}\) conflicts with the corresponding same-colored edge \(e_{a,i}\). This last assertion uses the forced uniformity of all leaf-cycle colors at index \(i\).

Now suppose that color \(c\) appears on at least one leaf-cycle edge, so \(E>0\).

* If \(H=2\), equation (1) forces \(S=E=0\), impossible.
* If \(H=1\), equation (1) and \(E\le2\) force \((S,E)=(1,1)\). Let the sole center-cycle and leaf-cycle indices be \(i,j\). They cannot conflict, so \(j\in\{i+2,i+3,i+4\}\pmod6\). In every one of these cases \(I_i\cup I_j=\mathbb Z_6\), leaving no allowable spoke layer and giving \(S=0\), a contradiction.
* If \(H=0\), equation (1) with \(1\le E\le2\) forces \((S,E)=(2,2)\). The two leaf-cycle indices must be \(j\) and \(j+3\), but \(I_j\cup I_{j+3}=\mathbb Z_6\); again \(S=0\), a contradiction.

No color could occur on a leaf-cycle edge, which is absurd. A \((2r+4)\)-coloring is impossible. Thus
\[
\chi'_s(K_{1,r}\square C_6)\ge2r+5.
\]

**4. A nine-color seed and a leaf-extension rule.** For \(r=2\), assign colors \(0,1,\ldots,8\) using the following explicit table. The entry at cycle index \(i\) colors the edge named in its column; all indices are modulo six.

| \(i\) | \(s_{1,i}\) | \(s_{2,i}\) | \(h_i\) | \(e_{1,i}\) | \(e_{2,i}\) |
|---:|---:|---:|---:|---:|---:|
| 0 | 0 | 1 | 5 | 7 | 8 |
| 1 | 2 | 3 | 6 | 1 | 7 |
| 2 | 4 | 0 | 8 | 3 | 5 |
| 3 | 7 | 2 | 1 | 0 | 4 |
| 4 | 5 | 6 | 3 | 2 | 0 |
| 5 | 8 | 7 | 4 | 6 | 2 |

Direct pairwise checking verifies that edges sharing any one color form an induced matching. For completeness, the standalone checker included with this result reconstructs the actual product adjacency, enumerates all edge pairs, and checks this table without relying on the statement of the theorem.

Suppose an \((2r+5)\)-coloring of the \(r\)-leaf product is given for some \(r\ge2\). Add a new leaf to the star and its six corresponding cycle vertices. Color its six new spokes alternately with **two previously unused colors**, according to parity of the cycle index. Same-parity spokes are pairwise nonconflicting on a six-cycle. Color each new leaf-cycle edge \(e_{r+1,i}\) with the existing color of \(e_{1,i}\). The copied cycle is internally strongly colored. Two leaf-cycle edges on different leaves cannot conflict; and any old center edge or old spoke conflicting with the new \(e_{r+1,i}\) would also conflict with the old \(e_{1,i}\). Thus the copied colors introduce no conflict with an old edge. The new spoke colors are fresh, so they introduce none either. This gives an \((2(r+1)+5)\)-coloring. Induction from the displayed seed proves
\[
\chi'_s(K_{1,r}\square C_6)\le2r+5
\]
for all \(r\ge2\), completing the exact formula.

**5. Universal graph corollary.** Let \(G\) have a vertex of degree \(\Delta\ge2\). Selecting that vertex and its \(\Delta\) neighbors and retaining only the incident edges yields a star subgraph \(K_{1,\Delta}\). Its Cartesian product with \(C_6\) is an edge-subgraph of \(G\square C_6\). Restricting any strong edge coloring to an edge-subgraph preserves the strong condition. Hence \(\chi'_s(G\square C_6)\ge2\Delta+5\). Equality holds for stars, as proved above.

## Verification

Run the included standalone program with `python3 verify_star_c6.py`. It uses no third-party modules. It independently reconstructs all edges of the product, tests every pair for the graph-theoretic strong conflict, and validates the explicit extension for every \(2\le r\le30\). It also checks that the proposed local cliques really are pairwise conflicting for \(2\le r\le7\), and verifies the six-cycle interval-cover facts used in the lower obstruction.

Recorded output:

`VERIFY_OK: saturation obstruction; 29 strong colorings (r=2..30); 228114 conflict pairs; 6 clique checks per leaf for r<=7`

The computational range is a consistency check, not a proof for unbounded \(r\). The local-clique counting argument and leaf-extension induction above supply the infinite proof.

## Relationship to prior work

Dara, Mishra, Narayanan and Tuza established in their 2021 preprint (published in 2022) a general bound \(2\Delta+4\le\chi'_s(T\square C_6)\le2\Delta+6\) for trees \(T\), and reported the particular equality \(\chi'_s(P_3\square C_6)=9\). Their exact four-divisible cycle result and their bounds for other cycle lengths are not asserted as new here. The present proof replaces the unresolved three-value interval on every star \(K_{1,r}\) with a single exact value and strengthens the six-cycle lower bound even for arbitrary (not necessarily tree) graphs of degree at least two. The mechanism is a six-clique color-saturation identity and a two-color leaf-extension operation, rather than a numerical test of isolated examples.

## Limitations

The exact assertion is for stars with at least two leaves and the cycle of length six. The general lower bound does not determine the strong chromatic index of \(G\square C_6\) for every other graph \(G\). No classification or enumeration of all optimal strong colorings is claimed. The verification program is finite and does not establish the theorem without the proof. Publication-priority assessment is based on the identified accessible literature, not a guarantee that every possible prior work has been found.

## References

1. S. Dara, S. Mishra, N. Narayanan and Z. Tuza, *Strong edge coloring of Cayley graphs and some product graphs*, arXiv:2107.00718v1, first posted 1 July 2021. https://arxiv.org/abs/2107.00718
2. S. Dara, S. Mishra, N. Narayanan and Z. Tuza, *Strong Edge Coloring of Cayley Graphs and Some Product Graphs*, *Graphs and Combinatorics* **38**, article 51 (2022), DOI:10.1007/s00373-021-02408-4. https://link.springer.com/article/10.1007/s00373-021-02408-4
