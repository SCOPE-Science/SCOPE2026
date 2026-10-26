# Scientific review: one-edge augmentation of a complete bipartite network

## Correctness
PASS. The graph-wide Rayleigh/embedding bound applies to arbitrary nonsymmetric edge allocations. Explicit feasible embeddings with variance \(\max\{p,q\}\) have strict slack on the extra edge in every nonexceptional ordered size. The seven-edge five-vertex embedding has variance \((11+2\sqrt3)/5\); exact block-diagonal eigenvalue computation of the proposed scaled allocation attains the same bound. The associated exact checker confirms all radical identities. Numerical matrix checks over finite sizes support, but do not replace, the symbolic all-size constructions.

## Originality
PASS on accessible evidence, subject to the risks below. The closest full-text works establish the general SDP and maximum-variance embedding frameworks. Göring–Helmberg–Wappler's clique-plus-three-independent-vertices example is adjacent to the subject but not an implication-equivalent classification of a single intrapartite edge over both part sizes. The Fiedler/Richter–Rocha tree classifications cannot directly cover the triangle-containing augmented bicliques. The earlier results for discrete-time bipartite walks with deleted cross-edges concern different graphs and objectives. Targeted mathematical search records and historical claim excerpts found no statement dominating the sharp \((3,2)\)-only activation law.

## Value
PASS. The natural network-design problem asks whether adding an available local link can change the best possible mixing rate when *the link must compete for a fixed global conductance budget*. The answer gives a complete infinite-family screening classification, proves that **all** optimizers exclude the extra link except for one orientation of a five-vertex network, and gives a strictly positive radical optimal allocation in that exception. The distinction between an available link and one worth funding is mathematically structural rather than merely a one-graph calculation.

## Closest literature and limitations
Göring–Helmberg–Wappler (2005) and Sun–Boyd–Xiao–Diaconis (2006) supply the embedding/SDP paradigm; their inspected examples do not state this family-wide screening law. Fiedler's 1990 tree article was inspected only through its abstract; the graph studied here contains triangles. A highly specialized earlier result for this augmentation could still exist. The statement applies to homogeneous total conductance budgets and continuous-time mixing, not discrete-time SLEM or heterogeneous costs.

Self-review: passed. Independent audit: not yet performed.
