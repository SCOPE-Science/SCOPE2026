# Independent mathematical audit

## correctness

PASS

In K_3^square3 each vertex has degree six. A valid majority colour class induces minimum internal degree at least 3. A class of <=4 vertices would require a K4, but cliques occupy coordinate lines of size at most 3. In a five-set, a degree-four vertex makes every other member adjacent to at most two other members because its open neighbourhood comprises three disjoint edges; otherwise the five-set would be 3-regular, ruled out by the handshake parity lemma. So classes have >=6 vertices and at most floor(27/6)=4 colours. The displayed disjoint 9/6/6/6 rectangular partition induces one K3 square K3 and three K3 square K2 blocks, attaining four colours. For d=2r+3, using base three-coordinate class plus r retained coordinates gives 3+2r same-colour neighbours out of degree 2d, and exactly 4*3^r colours. Independent bitmask enumeration checked all 101583 nonempty <=5 vertex sets; independent full-vertex lifted checks d=3,5,7, with infinite lifting proved algebraically.

## originality

PASS

The exact open parameter cell K_3^square3 is explicitly within Open Problem 3 of Bujtás et al. 2026. Its Proposition 6 gives the weaker odd-dimensional baseline 3^floor(d/2); Theorem 7 improves it only for alphabet size n=5 or n≥7, not n=3. The prior 2011 improper C-colouring language is equivalent for regular degree six and includes binary cube results, not a quoted value for this ternary cube. Other published Resultary result on complete multipartite graphs has different adjacency. Searches and actual full relevant sections of the strongest paper support best-of-knowledge novelty, retaining old impropriety literature priority risk.

## value

PASS

The ternary dimension-three case is a natural smallest unsolved odd-alphabet parameter explicitly listed in the recent majority C-colouring problem. The exact sharp four-colour bound gives a nontrivial local-degree obstruction plus a construction and propagates a factor-4/3 improvement over the previous ternary lower bound through every odd higher dimension.

The dated certificate retains the supplied scientific assessment, sources and limitations.
