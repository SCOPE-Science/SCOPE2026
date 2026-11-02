# The sharp four-row cutoff for directed mutual visibility on toroidal grids

## Finding

Let \(D_n=\overrightarrow{C}_4\square\overrightarrow{C}_n\) be the directed Cartesian product of consistently oriented cycles, with integer \(n\ge4\). Its directed mutual-visibility number is exactly

\[
\mu(D_n)=\begin{cases}
5,&n=4,\\
7,&n=5,\\
8,&n\ge6.
\end{cases}
\]

Thus the upper bound of two selected vertices in each of four directed-cycle fibres is attained precisely from width six onward. For every \(n\ge8\), the undirected graph obtained by forgetting orientations has mutual-visibility number \(12\), so the consistently oriented network has an exact deficit of four relative to its underlying undirected toroidal grid (by Korže and Vesel's undirected theorem [2]).

## Assumptions and scope

The vertex set is \(\mathbb Z_4\times\mathbb Z_n\). The only arcs are \((i,j)\to(i+1,j)\) and \((i,j)\to(i,j+1)\), with coordinates reduced modulo their respective cycle lengths. A set \(S\) is *directed mutually visible* when for **every ordered pair** \(a,b\in S\) of distinct vertices, there is a shortest directed \(a,b\)-path whose internal vertices are outside \(S\). This is the bidirectional directed mutual-visibility definition of Stojanović [1]. The extremal quantity \(\mu(D_n)\) is the largest cardinality of such a set.

## Proof

**1. Fibre bound.** A fixed first-coordinate fibre is a consistently directed cycle of length \(n\); a fixed second-coordinate fibre is a consistently directed cycle of length four. If three vertices of a directed-cycle fibre lie in \(S\), order them as \(u,v,w\) along its direction. The unique shortest directed \(u,w\)-path has zero displacement in the other coordinate, hence must traverse \(v\) internally. This contradicts directed mutual visibility. Thus every first-coordinate fibre and every second-coordinate fibre contains at most two members of \(S\). The four first-coordinate fibres imply \(|S|\le8\) for every \(n\ge4\).

**2. Exact geodesic test.** For \(a=(a_1,a_2)\) and \(b=(b_1,b_2)\), put
\[
p=(b_1-a_1)\bmod4,\qquad q=(b_2-a_2)\bmod n.
\]
Every shortest directed \(a,b\)-path has length \(p+q\) and is an interleaving of precisely \(p\) increasing-first-coordinate steps and \(q\) increasing-second-coordinate steps. Therefore such a path avoiding \(S\) internally exists if and only if the following Boolean rectangular reachability recurrence reaches its upper-right corner. Set \(R(0,0)=\mathrm{true}\); for \((r,s)\ne(0,0)\) with \(0\le r\le p\), \(0\le s\le q\), set \(R(r,s)=\mathrm{false}\) if \((a_1+r\bmod4,a_2+s\bmod n)\in S\setminus\{b\}\), and otherwise put
\[
R(r,s)=(r>0\ \mathrm{and}\ R(r-1,s))\ \mathrm{or}\
(s>0\ \mathrm{and}\ R(r,s-1)).
\]
Terms outside the rectangle are false. Mutual visibility is equivalent to \(R(p,q)=\mathrm{true}\) for all ordered distinct selected pairs. This is an exact finite decision procedure derived directly from the definitions, not a heuristic.

**3. Lower-bound witnesses.** For each of the following configurations, the indicated list for first-coordinate \(i\) gives all selected second coordinates in that fibre:

| \(n\) | First-coordinate fibres \(i=0,1,2,3\) | Size |
| --- | --- | ---: |
| \(4\) | \(\varnothing;\{0\};\{1,3\};\{1,3\}\) | \(5\) |
| \(5\) | \(\{0\};\{1,3\};\{1,4\};\{2,4\}\) | \(7\) |
| \(6\) | \(\{0,2\};\{0,3\};\{1,4\};\{2,4\}\) | \(8\) |

The exact recurrence above and, independently, shortest-path search on the defining directed graph verify all three configurations in the included `verify.py`.

**4. Exhaustive sharp small-width obstruction.** At \(n=4\), any mutually visible set of size at least six must have at most two selected vertices in each first- and second-coordinate fibre. Enumerating **all** such sets gives \(2040\) sets of size six, \(816\) of size seven, and \(90\) of size eight, hence \(2946\) possibilities. For each, at least one ordered pair fails the exact recurrence; a separately implemented shortest-path search also rejects it. At \(n=5\), the fibre bound already limits size to eight. Every candidate of size eight selects exactly two vertices in each first-coordinate fibre and at most two in each second-coordinate fibre. There are exactly \(2490\) such candidates; every one fails both tests. These enumerations are exhaustive because a valid configuration with three vertices in any one fibre was already ruled out in step 1. The included standalone verifier constructs the candidate lists afresh from the full combinatorial ranges and raises an error if any forbidden candidate is valid.

**5. Lifting from width six.** The eight-vertex \(n=6\) witness uses second coordinates only from \(\{0,1,2,3,4\}\), leaving the entire fibre at second coordinate five empty. For \(n>6\), retain the same eight selected coordinate pairs and insert \(n-6\) new empty second-coordinate fibres between positions five and zero. Each shortest directed path witnessing visibility at width six can be lifted, replacing any step from column five to column zero by the new empty chain. Its first-coordinate displacement is unchanged; its second-coordinate displacement is increased by exactly the necessary number of newly inserted edges if the old path crosses the wrap-around, and otherwise unchanged. Hence the lifted path remains shortest in \(D_n\) and has no selected internal vertices. This gives \(\mu(D_n)\ge8\) for every \(n\ge6\). Coupled with step 1 and the finite obstructions, the formula follows. \(\square\)

## Verification

Run `python3 verify.py` using Python's standard library. The program checks each witness both by rectangular dynamic programming and by a separate breadth-first search on the original arcs; independently exhausts the entire fibre-reduced candidate spaces at widths four and five; verifies that the forbidden candidate counts are \(2946\) and \(2490\); and tests the lifted witness up to width thirty. Successful execution ends with `VERIFY_OK`.

The finite enumerations establish the two small-width exclusions because the fibre restriction is proved necessary. The all-width claim relies on the explicit lifting argument, **not** on numerical tests up to any finite width.

## Relationship to prior work

Stojanović [1] introduced the directed variant, proved \(\mu(\overrightarrow C_n)=2\), and considered strongly connected components, strong bridges, tournaments and algorithmic complexity, but did not obtain a Cartesian product formula. Cicerone, Di Stefano and Klavžar [3] investigated Cartesian products using *undirected* geodesics and undirected graphs. Korže and Vesel [2] studied undirected products of paths and cycles; their Proposition 3.9 implies \(\mu(C_4\square C_n)=12\) for \(n\ge8\), where both factors are **undirected**. Those results do not establish the directed formula: directed shortest paths in \(D_n\) are one-way coordinate-monotone and require separate ordered-pair avoidance checks. The distinction produces a genuine four-vertex loss at \(n\ge8\).

## Limitations

The classification applies to exactly two *consistently* oriented cyclic factors, one of length four and the other of length at least four. It does not determine other oriented products, twisted orientations or higher-dimensional tori. The small cases \(n=4,5\) have exhaustive algorithmic proofs supported by completely included code, not short closed-form hand classifications. No claim is made to count all maximum sets or to establish absolute historical priority; alternative terminology in older literature remains a residual priority risk. Independent mathematical review has not been performed.

## References

[1] V. Stojanović, *The Mutual-Visibility Problem In Directed Graphs*, arXiv:2602.03267, first public version 3 February 2026. https://arxiv.org/abs/2602.03267

[2] D. Korže and A. Vesel, *Mutual-Visibility Sets in Cartesian Products of Paths and Cycles*, Results in Mathematics **79**, 116 (2024), Proposition 3.9. https://doi.org/10.1007/s00025-024-02139-x

[3] S. Cicerone, G. Di Stefano and S. Klavžar, *On the mutual visibility in Cartesian products and triangle-free graphs*, Applied Mathematics and Computation **438** (2023), 127619; preprint arXiv:2112.13024. https://arxiv.org/abs/2112.13024
