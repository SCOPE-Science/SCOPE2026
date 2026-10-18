# Independent mathematical audit

## correctness

PASS

PASS: Read pinned RESULT.md and verifier; independently enumerated all 2^13 subsets of Q=[-6,6], applying separation >3 and 3-coverage of core [-3,3]. Reconstructed all directed overlap witnesses for each graph edge, obtaining 59 vertices, 75 undirected edges and 4 undirected simple four-cycles; unique signed circulation has magnitude four, other sums zero. Independently verified four explicit vertices D0=(-5,-1,3), D1=(-4,0,4), D2=(-3,1,5), D3=(-6,-2,2,6) and all four overlap equalities for g=-1, giving -4. Witness uniqueness follows from two candidate g differing by two contradicting >3 separation; repeated-vertex four-walks backtrack and cancel. The computation is exhaustive for this finite Q only; no higher-dimensional/general labeling impossibility asserted.

## originality

PASS

PASS best-of-knowledge: Wang's arXiv:2609.39824v1 Lemma 7.3 is explicitly L>=4 and its proof uses L+4<=2L and 4<=L. The source's Proposition 7.7 uses that regime, and neither implies the first excluded L=3 canonical-label obstruction or its unique-cycle census. A targeted published-finding search finds other graph cycles but no coverage of these concrete marker-window sets. The result correctly narrows to the canonical witness annotation; absence of an alternative abstract labeling is not asserted.

## value

PASS

PASS: Determines sharpness of a load-bearing cutoff in the finite target used for continuous abelian-action graph homomorphisms; the explicit obstruction and exhaustive uniqueness census inform attempts to reduce the marker-window radius or modify canonical label construction. This is a motivated boundary example, not an arbitrary small graph catalog.

The dated certificate retains the supplied scientific assessment, sources and limitations.
