# Scientific review

**Correctness — PASS.** The proof works in the quotient group \(\mathbb F_2^n/\langle\mathbf1\rangle\): an endpoint class has one or two minimal generator supports, and equality of alternative two-step displacements cannot change a support when \(n\ge5\). This establishes the complete classification, including the small \(K_{4,4}\) quotient case, by exact reasoning for every dimension. The packaged finite checker uses vertex-path BFS rather than the generator-word proof, and reproduces every endpoint class for dimensions three through ten. Its limits do not constrain the formal proof.

**Originality — PASS, with risk.** Bonsma gives the rerouting problem but not a folded-cube classification. Asplund et al.'s Proposition 27 establishes the ordinary-cube permutahedron, not the antipodal quotient's distinct endpoint families or the dimension-four exception. Fang's folded-hypercube path-embedding paper treats path lengths rather than the one-vertex transformation graph, but its complete text was inaccessible, leaving residual risk. Multiple targeted literature searches and mathematical-record comparisons found no result that covers the theorem; this does not establish absolute uniqueness.

**Value — PASS.** The complete classification concerns a standard distance-transitive interconnection graph and a natural path-update rule. It exhibits a sharp connectivity transition: in dimension six, a diametric pair already has two disconnected but internally mobile hexagonal families. The exact all-pairs disconnected fraction and component metrics quantify the obstruction, with no arbitrary parameter slice or asserted downstream theorem needed.

**Limitations.** The theorem uses antipodal quotient cubes rather than the alternative added-antipodal-edge convention. It is a result about shortest vertex-path rerouting only. The inaccessible closely related folded-hypercube path-embedding paper and possible unindexed equivalent results remain originality risks.

Self-review: passed. Independent audit: not yet performed.
