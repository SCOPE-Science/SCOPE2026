# Exact mod-two acyclic deletion landscape of the twelve-vertex collapsible evasive ball
## Finding
Let \(B_{12,38}\) be the simplicial \(3\)-ball of Benedetti--Lutz on vertex set \(\{2,3,\ldots,13\}\). Define the **acyclic deletion graph** \(\mathcal A(B_{12,38})\) as follows. A state is a nonempty induced subcomplex \(B_{12,38}[W]\) that is reachable from the full ball by successively deleting one vertex at a time while every visited induced subcomplex has reduced homology \(\widetilde H_*(\cdot;\mathbb F_2)=0\). A directed edge records one further vertex deletion that preserves this acyclicity condition.

The graph \(\mathcal A(B_{12,38})\) has exactly \(134\) states. By the number of surviving vertices, its nonempty layers have sizes
\[
1,11,36,52,31,3
\]
on \(12,11,10,9,8,7\) vertices, respectively; there is no reachable acyclic state on six vertices. There are exactly \(20\) terminal states, namely \(17\) on eight vertices and \(3\) on seven vertices. The number of maximal directed deletion sequences from the full ball is exactly \(532\): \(292\) end at an eight-vertex terminal and \(240\) end at a seven-vertex terminal.

The three seven-vertex terminals are
\[
\{2,3,5,8,10,11,13\},\quad
\{2,3,6,7,8,9,13\},\quad
\{2,3,6,7,9,12,13\}.
\]
Their complements are exactly the three five-vertex deletion sets in Benedetti--Lutz, Proposition 3.3. Thus their homology obstruction appears as the deepest part of a larger complete deletion landscape: \(17\) additional maximal acyclic deletion chains already stall one level earlier, at eight vertices.

## Assumptions and scope
The input complex is exactly the \(38\)-tetrahedron ball listed in Benedetti--Lutz, Section 3. The calculation is over \(\mathbb F_2\). “Acyclic” means nonempty and with reduced homology zero in every degree. Only **induced subcomplexes obtained by deleting vertices** are considered; arbitrary face deletions, simplicial collapses, and homology over other coefficient rings are outside the claim.

The invariant is tied to the recursive topology behind evasiveness: along any non-evasive vertex-deletion branch, every deletion state must remain contractible and hence \(\mathbb F_2\)-acyclic. Therefore the directed graph above records every branch that survives the necessary homology test. The claim does not assert that every acyclic state is non-evasive.

## Proof
The proof is exhaustive over a finite domain.

First generate every face of \(B_{12,38}\) from the \(38\) source tetrahedra. For each of the \(2^{12}-1=4095\) nonempty vertex sets \(W\), form the induced subcomplex \(B_{12,38}[W]\). Build its simplicial boundary matrices over \(\mathbb F_2\), compute their ranks by exact binary Gaussian elimination, and obtain all Betti numbers from
\[
\beta_i=\dim C_i-\operatorname{rank}\partial_i-\operatorname{rank}\partial_{i+1}.
\]
A state is marked acyclic precisely when \(\beta_0=1\) and every higher Betti number is zero. Across all nonempty induced subcomplexes there are \(585\) acyclic ones.

Next start from the full twelve-vertex state and recursively follow every one-vertex deletion whose child is in that acyclic set. Exact dynamic programming gives layer sizes \(1,11,36,52,31,3\), hence \(134\) reachable states in total. A reachable state is terminal when none of its one-vertex deletions is acyclic. The terminal-size histogram is exactly \(17\) at size eight and \(3\) at size seven.

Finally assign the full state path count \(1\), and propagate each state's count to every acyclic child. Summing the counts of terminal states gives \(532\) maximal deletion sequences. The corresponding sums are \(292\) over the eight-vertex terminals and \(240\) over the seven-vertex terminals. Direct set comparison shows that the three seven-vertex terminals are precisely the complements of the three exceptional five-deletion sets in Proposition 3.3 of the source paper.

## Verification
The bundled `verify.py` reconstructs the complex from the published facet list, enumerates all \(4095\) nonempty induced subcomplexes, computes simplicial homology over \(\mathbb F_2\), checks Euler characteristic independently against the Betti numbers for every state, builds the reachable acyclic deletion graph, and recomputes the terminal and path counts. It also checks the three seven-vertex terminals against the published exceptional deletion sets.

A successful replay prints

`VERIFY_OK acyclic_all=585 reachable=134 layers=12:1,11:11,10:36,9:52,8:31,7:3 terminals=8:17,7:3 maximal_paths=532 path_split=8:292,7:240 paper_terminal7=match`.

The calculation is exhaustive for the stated twelve-vertex complex; there is no sampling or timeout-based inference.

## Relationship to prior work
Benedetti--Lutz introduced this specific ball as a collapsible but evasive \(3\)-ball. Their Proposition 3.3 checks all \(\binom{12}{5}=792\) five-vertex deletions, finds exactly three acyclic seven-vertex induced subcomplexes, and observes that deleting any further vertex from each of those three produces non-acyclic homology. That establishes evasiveness by a single strategically chosen layer.

The present result does not re-prove that statement as its endpoint. It computes the entire **reachable** \(\mathbb F_2\)-acyclic deletion graph from the full ball, including all preceding layers, the \(17\) terminal eight-vertex traps not exposed by Proposition 3.3, and the exact \(532\)-path maximal-chain census. Focused searches for the exact counts, the deletion-graph formulation, and equivalent “acyclic vertex-deletion chain” formulations found no covering statement. A later paper on extremal collapsibility and random discrete Morse theory discusses non-evasiveness and related algorithmic examples but does not state this deletion landscape for \(B_{12,38}\).

## Limitations
The result is coefficient-specific: a subcomplex classified as acyclic here is tested over \(\mathbb F_2\), not over every coefficient ring. The graph is also a necessary-condition landscape for non-evasive deletion branches, not a classification of non-evasive induced subcomplexes. The exact counts concern this labeled triangulation of \(B_{12,38}\); no claim is made for all collapsible evasive balls.

The literature comparison cannot exclude an unindexed or unpublished computation of the same finite census. The strongest identified prior statement is Proposition 3.3 of the source paper, which covers the three deepest seven-vertex terminals but not the full reachable graph or its path counts.

## References
1. B. Benedetti and F. H. Lutz, *Knots in collapsible and non-collapsible balls*, arXiv:1303.2070v1, first public 2013-03-08; Electronic Journal of Combinatorics 20(3) (2013), P31. Primary MSC: 57Q15.
2. K. A. Adiprasito, B. Benedetti, and F. H. Lutz, *Extremal examples of collapsible complexes and random discrete Morse theory*, arXiv:1404.4239, first public 2014-04-16.
