# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

PASS.  Decomposing a total dominating set of the central graph into original
vertices and subdivision vertices forces the original part to be a vertex cover.
For a fixed vertex cover A, exactly the vertices v with A contained in N_G[v]
fail to receive domination from an original vertex; the selected subdivision
vertices must therefore correspond exactly to an edge set covering this residual
set.  The converse construction checks every vertex type and gives equality.
The auxiliary identity for partial edge covers follows from maximum matching in
the induced graph on the residual set.  The proof uses the hypothesis that G has
no isolated vertices precisely where an uncovered residual vertex is assigned an
incident edge.

The equality criterion with tau(G) is also exact: zero residual edge-cover cost
is equivalent to the chosen minimum vertex cover being a total dominating set of
the complement.  Known formulas for complete graphs and long paths are recovered.
A separate finite check on all 995 connected Graph-Atlas graphs of orders 2--7
agrees with direct total-domination MILPs.

## Originality

PASS, to the best of our knowledge.  The closest directly inspected primary
source is Kazemnejad--Moradi (2019), whose Theorem 1.1 gives the tight but
non-exact general bounds tau(G) <= gamma_t(C(G)) <= tau(G)+rho(G), followed by
exact computations for selected families.  The new formula identifies the exact
residual edge-cover term for every vertex cover and minimizes it globally.

Chen--Sohn--Wang (2020) is the most important residual risk because it studies
central trees and a relationship between gamma_t(C(T)) and tau(T).  Its abstract
and bibliographic record were inspected, but the complete theorem text was not
directly inspected.  The reported scope is trees, while the present theorem holds
for every finite simple graph without isolated vertices.  Searches also checked
ordinary domination of central graphs and the September 2026 independent-
domination preprint; those concern different parameters.  Searches using total
domination, vertex-cover, edge-cover, complement and matching formulations did
not locate the exact identities stated here.

## Value

PASS.  The result upgrades the foundational 2019 two-sided bound to a single
exact formula, explains the role of subdivision vertices through a residual
partial edge-cover problem, converts that residual cost to the matching number of an induced residual
subgraph, and gives a concise structural characterization of equality with the
vertex-cover lower bound.  The formula simultaneously covers arbitrary connected
and disconnected graphs without isolated vertices and recovers established
special cases.

## Evidence and limitations

The mathematical proof is self-contained.  Finite computation is supporting
evidence only.  The principal literature limitation is incomplete direct access
to the theorem text of the 2020 central-tree paper; an equivalent result under a
different terminology also remains possible.  No algorithmic complexity claim
is made for evaluating the optimization formula.
