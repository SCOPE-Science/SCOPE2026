# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The theorem reduces to two independent directions.

For necessity, distances between vertices of a block are unchanged in the ambient connected graph: an outside shortcut between two distinct vertices of a block would be an ear enlarging that 2-connected block. Hence a cycle block $C_\ell$ contributes the induced subgraph $C_\ell^2$ to the full square. The stated vertex sets give explicit induced holes for every $\ell\ge6$: a special four-vertex hole for $\ell=6$, the even vertices for even $\ell\ge8$, and the even-indexed vertices for odd $\ell\ge7$.

For sufficiency, the leaf-block argument was checked case by case. Removing the private vertices of a leaf block does not change distances between the remaining vertices. Private vertices of a clique leaf block are successively simplicial in the square. For $C_4$, the order $x_2,x_1,x_3$ is simplicial; for $C_5$, the order $x_2,x_3,x_1,x_4$ is simplicial. Recursing therefore produces a perfect-elimination ordering. The single-block base cases are complete after squaring.

Boundary cases were checked explicitly: $C_4^2=K_4$, $C_5^2=K_5$, while $C_6^2$ has the induced $4$-cycle on $0,2,3,5$. The proposed stronger statement with “strongly chordal” is false: a $C_4$ with pendant leaves at three cycle vertices has a square containing an induced $3$-sun, as recorded in RESULT.md.

## Originality

Originality is assessed **to the best of our knowledge**. Searches covered the formulations “square of a cactus is chordal”, “cactus graph chordal square”, “cactus-block/cactus block graph square chordal”, the cycle-threshold formulations involving $C_5$ and $C_6$, and the equivalent obstruction formulation by long cycle blocks. The SCOPE archive was also checked by the mathematical object and these synonymous claim families; no overlapping successful record was found.

The most directly relevant recent source is Suvagiya, arXiv:2609.20204. Its accessible full text was inspected. It defines cactus squares, explicitly recalls that squares of trees are chordal, proves a leaf-block distance lemma and a degeneracy ordering, and determines ordinary/list two-distance chromatic numbers. It does not state a chordality classification of cactus squares or the length-five threshold.

Golovach--Kratsch--Paulusma--Stewart (2018) was inspected in its open full-text web version. It studies polynomial recognition of cactus square roots and identifies cactus-block graphs as the natural generalization in which blocks are cycles or cliques; no chordality threshold was found. Le--Tuy (2010), together with Tuy's thesis exposition, covers the clique-block endpoint and states that squares of block graphs are strongly chordal.

The principal residual coverage risk is Ducoffe (Discrete Applied Mathematics 257, 2019), which specifically treats square roots of cactus-block graphs. Its abstract and accessible institutional/bibliographic summaries were inspected and concern clique-cutset decomposition and recognition; the full journal theorem text was not inspected in full. Consequently an unindexed structural lemma in that paper, or an older graph-power result under different terminology, could still subsume the theorem. No such coverage was found in the searches performed.

## Value

The result gives an exact if-and-only-if structural boundary for a standard sparse block class, extends the classical chordality of tree squares and the stronger block-graph endpoint, and has a sharp first obstruction at $C_6$. The proof supplies a direct perfect-elimination ordering, so the characterization is constructive once the root is known. It is also timely relative to current work on coloring cactus squares, where leaf-block elimination is already central but chordality itself was not classified.

## Limitations

The cactus-block square root is assumed given. No claim is made that this criterion improves recognition of cactus-block square roots from an arbitrary square graph. The theorem concerns chordality only; strong chordality fails even within the short-cycle cactus subclass. Originality remains to the best of our knowledge, with the Ducoffe full-text access gap and possible unindexed older graph-power formulations as residual risks. No independent audit is asserted.
