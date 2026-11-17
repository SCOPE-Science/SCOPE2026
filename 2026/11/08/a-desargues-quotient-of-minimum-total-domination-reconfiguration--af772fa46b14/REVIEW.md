# Independent mathematical audit

## correctness

PASS

On D=GP(10,2), a selected subset is total dominating iff OR of its open-neighbor masks is the all-20-vertex mask. Complete independent enumeration of every subset of size 0..8 finds none at 0..7 and exactly 190 at 8, so min=8. Enumerating every selected-to-unselected replacement among 190 optima reconstructs 360 legal jumps and zero slides; degree histogram 40 zeros, 120 fours, 30 eights. Exact connected-component search returns 40 isolates and one 150-vertex component; BFS from every one of 150 vertices gives eccentricity 10. Its degree-4 induced subgraph consists of twenty six-cycles; each of thirty degree-8 vertices neighbors exactly four vertices in each of two distinct hexagons. Quotient pairs are 30 distinct edges, each of 20 hexagons has degree 3. Exact explicit permutation phi=[0,1,3,2,12,11,17,14,13,4,5,18,10,19,9,8,16,15,7,6] sends complete quotient edge set to GP(10,3)=Desargues graph. Source independently enumerates full 120 base automorphisms and five optimal-set orbits (60,60,30,30,10). Fresh independent finite exhaustive GP enumeration reverified quotient and all eccentricities; source also contains independent LCF-model checker. Because finite input and complete enumeration with exact predicates/bijection, this supports the full finite claim rather than a sample.

## originality

PASS

Important coverage: full 2026-11-02 earlier publication 'Forty chordless-cycle obstructions in minimum total-domination exchanges of the dodecahedral graph' already gives size-8 optimum, 190 states, 360 jumps, 40 isolates, 150-vertex component, degree histogram, common eccentricity 10 and five orbit cardinalities. These shared components are **not new**. However that earlier complete primary theorem/proof does NOT identify degree-four induced twenty hexagons nor derive an incidence quotient with the Desargues graph; neither its 40 induced 12-cycle characterization nor scalar graph census logically determines those finer incidence relationships without new edge-structure work. The surviving original main claim is precisely the twenty-hexagon/thirty-hub quotient isomorphism and no-slide phenomenon (no-slide also not in prior), under best knowledge. Older generalized Petersen domination papers only establish the min set size/examples.

## value

PASS

The exact Desargues GP(10,3) quotient emerging naturally from minimum total-domination exchange states of the dodecahedral GP(10,2), via intrinsic degree-four six-cycles and degree-eight hubs, is a motivated nontrivial finite reconfiguration-geometry classification distinct from an existing scalar census. A complete 20-vertex graph isomorphism certificate and orbit structure make it a useful exact example rather than arbitrary re-indexing.

The dated certificate retains the supplied scientific assessment, sources and limitations.
