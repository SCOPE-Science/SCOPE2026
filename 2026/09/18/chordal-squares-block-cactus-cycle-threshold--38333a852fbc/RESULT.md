# Sharp five-cycle threshold for chordal squares of cactus-block graphs

## Statement

For a graph $G$, let $G^2$ denote its square: two distinct vertices are adjacent in $G^2$ exactly when their distance in $G$ is at most two. A **cactus-block graph** is a connected graph in which every block is either a complete graph or a cycle.

**Theorem.** Let $G$ be a finite cactus-block graph. Then

\[
G^2 \text{ is chordal}
\quad\Longleftrightarrow\quad
\text{every non-complete cycle block of }G\text{ has length at most }5.
\]

Equivalently, $G^2$ is chordal if and only if $G$ has no block isomorphic to $C_\ell$ for any $\ell\ge 6$.

In particular, for every cactus $G$,

\[
G^2 \text{ is chordal}
\quad\Longleftrightarrow\quad
\text{every cycle of }G\text{ has length at most }5.
\]

The threshold is sharp: $C_5^2=K_5$ is chordal, whereas $C_6^2$ already contains an induced $C_4$.

## Necessity

We first record a metric fact about blocks. If $B$ is a block of a connected graph $G$ and $u,v\in V(B)$, then every shortest $u$--$v$ path may be taken inside $B$. Indeed, if a shortest path left $B$ and later re-entered it at a distinct vertex, the outside segment would be an ear joining two vertices of $B$; adjoining that ear to the 2-connected block $B$ would produce a strictly larger 2-connected subgraph, contradicting maximality of the block. A detour that leaves and re-enters at the same vertex cannot be shortest. Hence

\[
d_G(u,v)=d_B(u,v),
\qquad
G^2[V(B)]=B^2.
\]

Suppose now that $B=C_\ell$ is a cycle block with $\ell\ge6$. Then $C_\ell^2$ contains an induced hole.

- For $\ell=6$, the vertices $0,2,3,5$ induce a $C_4$ in $C_6^2$.
- If $\ell=2m\ge8$, the even vertices $0,2,\ldots,2m-2$ induce $C_m$ in $C_\ell^2$.
- If $\ell=2m+1\ge7$, the vertices $0,2,\ldots,2m$ induce $C_{m+1}$ in $C_\ell^2$; the wrap-around edge has cyclic length one and every other selected consecutive pair has cyclic length two, while nonconsecutive selected vertices have cyclic distance at least three.

Because $G^2[V(B)]=C_\ell^2$, the same hole is induced in $G^2$. Thus chordality forces every cycle block to have length at most five.

## Sufficiency: an explicit perfect-elimination order

Assume every non-complete cycle block is a $C_4$ or $C_5$; triangles are already complete blocks. We construct a perfect-elimination ordering of $G^2$ by peeling leaf blocks of the block-cut tree.

If $G$ has one block, then the block is a clique, $C_4$, or $C_5$, and its square is complete. Otherwise choose a leaf block $B$ with its unique cut vertex $c$, and put

\[
P=V(B)\setminus\{c\},\qquad R=G-P.
\]

Any path between two vertices of $R$ that enters $P$ must enter and leave through $c$, so it cannot shorten their distance. Consequently

\[
R^2=G^2[V(R)].
\]

It is therefore enough to remove the private vertices $P$ as simplicial vertices of the current square and then recurse on $R$.

### Clique leaf block

If $B$ is complete, take any $u\in P$. Its remaining square-neighbors are contained in

\[
(B\setminus\{u\})\ \cup\ N_R(c).
\]

This set is a clique in $G^2$: vertices of $B$ are mutually adjacent, vertices of $N_R(c)$ are pairwise at distance at most two through $c$, and a private vertex of $B$ is at distance at most two from every vertex of $N_R(c)$ through $c$. Thus the private vertices of a clique leaf block can be deleted in arbitrary order.

### A $C_4$ leaf block

Write

\[
B=cx_1x_2x_3c.
\]

Delete $x_2,x_1,x_3$ in this order. The first vertex $x_2$ has no square-neighbor outside $B$ and $C_4^2=K_4$, so it is simplicial. After $x_2$ is gone, every remaining neighbor of $x_1$ lies in

\[
\{c,x_3\}\cup N_R(c),
\]

which is a clique in $G^2$; the same is then true for $x_3$.

### A $C_5$ leaf block

Write

\[
B=cx_1x_2x_3x_4c.
\]

Delete

\[
x_2,x_3,x_1,x_4.
\]

Since $d_G(x_2,c)=d_G(x_3,c)=2$, neither $x_2$ nor $x_3$ has a square-neighbor outside $B$, while $C_5^2=K_5$; hence the first two deletions are simplicial. Afterwards every remaining neighbor of $x_1$ lies in

\[
\{c,x_4\}\cup N_R(c),
\]

again a clique in the square, and the final deletion of $x_4$ is immediate.

Repeating this operation down the block-cut tree yields a perfect-elimination ordering of $G^2$. Therefore $G^2$ is chordal.

## A boundary beyond chordality

The conclusion cannot in general be strengthened to strong chordality, even for cacti satisfying the theorem. Start from a $4$-cycle $a b c d a$ and attach one pendant leaf at each of $b,c,d$. Its square is chordal by the theorem, but the six vertices consisting of $a,b,d$ and the three pendant leaves induce a $3$-sun: $a,b,d$ form the clique, and the leaves at $b,c,d$ are adjacent respectively to the clique pairs $ab$, $bd$, $da$. Thus short cycle blocks preserve chordality without preserving the stronger block-graph phenomenon.

## Context and significance

Squares of trees are classically chordal, and squares of block graphs are in fact strongly chordal. Le and Tuy gave structural characterizations of block-graph squares, recovering this strong-chordality endpoint. The present theorem gives an exact extension from clique blocks to cactus-block graphs: the only obstruction to ordinary chordality is a cycle block of length at least six.

Recent work of Suvagiya studies $G^2$ for cacti through two-distance and list-two-distance coloring. That paper explicitly recalls that tree squares are chordal and develops leaf-block elimination for cactus squares, but its statements concern degeneracy and coloring rather than a chordality characterization. Golovach--Kratsch--Paulusma--Stewart and Ducoffe study recognition and decomposition of cactus or cactus-block square roots; their available statements do not give the five-cycle chordality threshold above.

The proof is constructive: a cactus-block root satisfying the criterion immediately supplies a perfect-elimination ordering of its square by leaf-block peeling. The result also isolates the first obstruction sharply: a $C_5$ block is harmless for chordality because its square is complete, while a $C_6$ block forces an induced $C_4$.

## Limitations

This result assumes the cactus-block root $G$ is given; it is not a new recognition algorithm for deciding whether an arbitrary input graph has such a square root. It characterizes chordality, not strong chordality, and the example above shows that the latter requires additional structure. Originality is to the best of our knowledge. The full journal text of Ducoffe's 2019 cactus-block square-root paper was not inspected in full; its abstract and accessible summaries were inspected, so an unindexed lemma there or in older graph-power literature remains the main residual coverage risk.

## References

1. V. Suvagiya, *Two-distance and list-two-distance coloring of cacti: the subcubic case and the C5 obstruction*, arXiv:2609.20204 (2026). https://arxiv.org/abs/2609.20204
2. P. A. Golovach, D. Kratsch, D. Paulusma, A. Stewart, *Finding Cactus Roots in Polynomial Time*, Theory of Computing Systems 62 (2018), 1409--1426. https://doi.org/10.1007/s00224-017-9825-2
3. G. Ducoffe, *Finding cut-vertices in the square roots of a graph*, Discrete Applied Mathematics 257 (2019), 158--174. https://doi.org/10.1016/j.dam.2018.10.028
4. V. B. Le, N. N. Tuy, *The square of a block graph*, Discrete Mathematics 310 (2010), 734--741. https://doi.org/10.1016/j.disc.2009.09.004
