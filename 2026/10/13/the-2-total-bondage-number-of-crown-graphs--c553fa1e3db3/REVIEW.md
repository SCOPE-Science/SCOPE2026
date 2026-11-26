# Independent mathematical audit

## correctness

PASS

In a bipartite graph total domination splits into the two independent shore minima. In a crown each minimum is 2, and in any spanning subgraph neither can be 1. A failed dominating pair on a shore is contained in a common nonneighbor set on the opposite shore. If all pairs fail, the resulting proper sets S_j (each containing j) cover all pairs, and their total excess is exactly the deletion count. Every point occurs in at least two sets since its own set is proper. If all points occur at least three times the bound holds immediately. Otherwise the two sets P,Q containing a point of multiplicity two cover [n], with intersection of size c. They contribute n+c−2 excess; the other sets cover all cross pairs between the two nonempty differences P\Q and Q\P. On the union of those differences their clique graphs are connected; replacing each nonempty clique by a spanning tree leaves connectivity unchanged and uses at most its set's excess in edges. This forces another n−c−1, for a total of at least 2n−3. Apply to both shores. Independently checked the construction by decomposition: a_r b_c is an isolated edge component, and after removing its endpoints the remaining missing edges are precisely a perfect matching (the remaining diagonal plus a_c b_r). Thus the remainder is Cr_{n−1}, including Cr_2=2K_2 at n=3, and the total domination number of the disjoint union is 2+4=6 with no isolated vertices. The two truncated stars and the extra edge are disjoint and cost 2n−3. The stray y in the displayed sum at line 48 is a typographical artifact, not an extra factor. The frozen checker and output were inspected, not executed; completeness follows from the analytic proof.

## originality

PASS

Credit the earlier ordinary total-bondage crown result with the initial value, persistence through 2n−4 deletions and the second-level lower bound, including an exact second-level witness at n=3. The supported distinct claim is an explicit witness at the same cost attaining a two-unit increase for the full family, hence equality of first- and second-level thresholds. The earlier general construction only increases total domination by one for n≥4.

## value

PASS

For the canonical dense matching-deleted bipartite family, determines whether requiring a two-unit jump costs more than requiring the first increase under a no-isolate constraint. The exact equality is not supplied by knowing the first threshold; the witness forces both independent shore minima to change at the same critical budget. This provides a comparison with the intact biclique for the same second-level invariant, without claiming the previously known lower-bound mechanism as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
