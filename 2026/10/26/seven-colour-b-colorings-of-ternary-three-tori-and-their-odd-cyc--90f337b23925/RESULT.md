# Seven-colour \(B\)-colorings of ternary three-tori and their odd cyclic lifts

## Finding

**Theorem.** For every three positive odd integers \(a,b,c\), the Cartesian product of cycles
\[
G=C_{3a}\square C_{3b}\square C_{3c}
\]
has \(B\)-coloring number
\[
\boxed{q_B(G)=7.}
\]
In particular, the ternary three-dimensional Hamming graph \(C_3\square C_3\square C_3\), with 27 vertices and 81 edges, has \(B\)-coloring number seven. This resolves the previously open seven-versus-eight gap for that graph and gives an infinite family of odd three-dimensional discrete tori satisfying the degree-plus-one conjecture.

## Assumptions and scope

All graphs are finite, simple, and undirected. The cycle \(C_m\) has vertex set \(\mathbb Z/m\mathbb Z\) and edges between consecutive residues; \(C_3\) is a triangle. In a Cartesian product, vertices are adjacent when they differ along one factor by a cycle edge. A \(B\)-coloring is a proper edge-colouring in which every simple four-cycle is rainbow, meaning that its four edges receive pairwise distinct colours. The symbol \(q_B\) denotes its minimum palette size. The parameters \(a,b,c\) are arbitrary **positive odd** integers, so all three cycle lengths are positive odd multiples of three. No assertion is made for odd factor lengths not divisible by three.

## Proof

**1. Universal lower bound.** The graph \(G\) is six-regular and has an odd number \(N=27abc\) of vertices. It contains \(3N\) edges. A proper edge-colouring with six colours would partition the edges into six matchings, each with at most \((N-1)/2\) edges, so it would colour at most \(3(N-1)<3N\) edges. Hence \(q_B(G)\ge7\).

**2. A finite seven-colour seed on \(T=C_3\square C_3\square C_3\).** Write a vertex as \(x=(x_0,x_1,x_2)\in\mathbb Z_3^3\). Let \(e_i\) be the unit vector in direction \(i\), where \(i\in\{0,1,2\}\). Every undirected edge has a unique orientation of the form \(x\to x+e_i\), with all coordinates reduced modulo three. Define its colour by
\[
\operatorname{col}(\{x,x+e_i\})=A_i[x_2][x_0][x_1]\in\{0,1,2,3,4,5,6\}.
\]
Here the three arrays \(A_i\) are given *in full* in `certificate.json`: `colors[i][z][u][v]` is \(A_i[z][u][v]\). Each \(A_i\) contains three \(3\times3\) matrices, one for each \(z\in\{0,1,2\}\). For readability, their nine matrices, with rows indexed by \(u\) and columns by \(v\), are:

```
       z=0                z=1                z=2
A_0:  4 0 1              1 3 0              6 1 2
       0 6 4              4 0 2              1 4 0
       5 3 2              2 1 5              3 5 6

A_1:  2 4 3              6 2 4              4 3 0
       1 3 2              2 1 6              3 5 4
       4 5 6              5 6 3              0 2 5

A_2:  0 5 6              5 0 1              1 6 5
       3 4 5              0 6 3              5 2 6
       1 2 0              6 3 4              2 1 3
```

We now give an exact finite certificate check, not a probabilistic test. Enumerate the 27 triples \(x\), construct all 81 distinct undirected edges \(\{x,x+e_i\}\), and assign their colours from these arrays. At every vertex \(x\), inspect the six incident edges and verify that their colours are pairwise distinct. Next construct **every simple four-cycle directly from graph adjacency**, without assuming its product-square form, and inspect its four edge colours. The standalone exhaustive checker `verify.py` verifies precisely 27 proper vertices and 81 rainbow four-cycles in \(T\); all seven colours occur. Its full executable source, colour table, and literal recorded result are included. Thus the arrays define a seven-colour \(B\)-coloring and \(q_B(T)\le7\). The preceding lower bound with \(a=b=c=1\) gives \(q_B(T)=7\).

**3. Lift to all stated cycle triples.** On the cycle \(C_{3a}\), reduction of vertex labels modulo three is a graph covering onto \(C_3\), with the two incident cycle edges mapping bijectively to the two edges incident with the image vertex. The same holds for \(C_{3b}\) and \(C_{3c}\). Their Cartesian product yields a covering map
\[
\pi:C_{3a}\square C_{3b}\square C_{3c}\longrightarrow T,
\qquad (x_0,x_1,x_2)\mapsto(x_0\bmod3,x_1\bmod3,x_2\bmod3).
\]
Colour every edge \(uv\) of \(G\) with \(\operatorname{col}(\{\pi(u),\pi(v)\})\). The edge map is well-defined. At each vertex the six incident edges map bijectively to the six incident edges downstairs, so the colouring is proper. Because each cycle factor has odd length and therefore is not a four-cycle, every simple four-cycle of \(G\) is a Cartesian product square involving two distinct factor directions. Its four projected vertices remain distinct and its boundary projects edge-by-edge to a four-cycle of \(T\), so its colours are pairwise distinct. Therefore the lifted colouring is a seven-colour \(B\)-coloring, proving \(q_B(G)\le7\). Together with Step 1 this gives equality for all stated \(a,b,c\).

## Verification

The package includes `certificate.json` (the 81-entry three-axis array), `verify.py` (Python standard library only), and `verification_output.txt` (literal execution output). Run `python verify.py` from their directory. The checker independently builds the simple graph, enumerates every simple four-cycle from adjacency, and asserts properness and rainbow colours. The base case has 27 vertices, 81 edges, and 81 distinct simple four-cycles. Direct checks on the lifts with cycle triples \((3,3,3)\), \((9,3,3)\), \((9,9,3)\), \((15,9,3)\), \((9,9,9)\), and \((15,9,9)\) also succeed; the last instance has 1215 vertices and 3645 distinct simple four-cycles. The finite checks do **not** establish the infinite conclusion by extrapolation; Step 3 proves it using the covering argument.

## Relationship to prior work

Gyárfás and Sárközy (2023), Theorem 1.8, give \(7\le q_B(C_3^3)\le8\); their Theorem 1.7 proves degree-plus-one equality when every odd cycle length is divisible by seven, a different divisibility family. Their product bound is not a seven-colour construction on \(C_3^3\). Jiang and Li (arXiv:2608.21774v1, posted 22 August 2026), Theorem 1.4, determine all **two-dimensional** torus grid cases; Section 7, Conjecture 7.1, predicts \(q_B=2d+1\) for every product of \(d\) odd cycles, while their Lemma 2.4 establishes that colours can be periodically repeated in cycle factors. The present finite seed is not supplied by that lemma or by the listed exact results, and its odd triple-cycle lifts yield a concrete previously unresolved subfamily of the conjecture. The resulting infinite lift argument agrees with Jiang and Li's already-known repetition mechanism; it is not claimed independently as a new lemma.

The term \(B\)-coloring here concerns **edges**, not the unrelated vertex-colouring invariant called b-colouring. Likewise, the previously studied ordinary chromatic number of the distance-at-least-two threshold graph on 27 ternary triples does not imply a \(B\)-edge-colouring of this product graph.

## Limitations

The result does not prove the full conjecture for all products of three odd cycles, nor does it treat more than three factors. The construction is an explicit finite certificate plus a general covering proof, not a structural classification of *all* minimum colourings. A database and literature search can miss unpublished or differently indexed equivalent certificates; independent mathematical review and definitive bibliographic priority remain outstanding.

## References

1. A. Gyárfás and G. N. Sárközy, “Proper Edge Colorings of Cartesian Products with Rainbow \(C_4\)-s,” *Graphs and Combinatorics* **39**, Article 98 (2023). DOI: `10.1007/s00373-023-02697-x`. Relevant: Theorems 1.6–1.8 and their proofs. https://link.springer.com/article/10.1007/s00373-023-02697-x
2. Z. Jiang and J. Li, “\(B\)-coloring of grid graphs,” arXiv:`2608.21774v1` (first posted 22 August 2026). Relevant: Theorem 1.4, Lemma 2.4, Section 7 Conjecture 7.1. https://arxiv.org/pdf/2608.21774
