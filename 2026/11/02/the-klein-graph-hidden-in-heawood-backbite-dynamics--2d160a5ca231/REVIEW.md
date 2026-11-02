# Scientific review: Heawood backbite dynamics and the Klein graph

## Correctness — PASS
The result has a fully specified finite domain (all undirected Hamiltonian paths of the Fano-plane incidence graph) and an unambiguous endpoint-to-interior backbite rule. The path-order depth-first search enumerates all configurations; an independent complement-edge test checks all 203,490 possible eight-edge complements, retains precisely the connected thirteen-edge paths, and obtains the same total of 504. Both methods independently obtain 672 backbite adjacencies, the 336/168 degree split, and the 56-vertex cubic quotient of girth seven and diameter six. The first additionally enumerates every incidence automorphism and proves quotient arc-transitivity; the Foster census supplies the identification with the cubic Klein graph. All-root shortest-path computations establish radius 24 and diameter 25. These are complete finite checks, not stochastic evidence. Residual dependency: the recognized Foster classification is an external published theorem, not reproved here.

## Originality — PASS, qualified
Oberdorf et al. introduce and analyze backbite dynamics for square-lattice walks; their inspected full manuscript does not classify Heawood paths. Dejter's inspected full manuscript constructs the cubic Klein graph from the Coxeter graph and remarks on the Coxeter graph's construction from Heawood hexagons, but does not assert that Heawood Hamiltonian-path backbite dynamics produce the doubled-truncation subdivision of the Klein graph. Conder--Dobcsányi classify the target cubic symmetric graph rather than this reconfiguration construction. The 2026 Kazazi abstract announces broad sufficient conditions that cannot cover a girth-six graph through a spanning path square. A full text for that recent source was not available, so an unmentioned special example remains a risk. Prior known counts of Heawood Hamiltonian cycles, Klein graph invariants, and the Foster classification are credited, not claimed. Searches under path rotation, endpoint pivot, backbite, Heawood, Klein, and Coxeter terminology returned no equivalent construction; absence of indexed matches is not a uniqueness proof.

## Value — PASS
The structural graph isomorphism is more than a count: it gives an explicit geometric reduction of the state space of local Hamiltonian-path dynamics on the classical Heawood graph to the highly symmetric cubic Klein graph. It proves that all 504 states communicate under local moves, exposes two sharply different vertex degrees and three symmetry orbits, and determines exact worst-case conversion length 25. This is a natural exact benchmark for a Markov-chain move used to sample Hamiltonian walks and a nonobvious link between standard Foster graphs. The result is deliberately finite; no general-family theorem is inferred.

## Closest literature and limits
- R. Oberdorf, A. Ferguson, J. L. Jacobsen, J. Kondev, *Secondary Structures in Long Compact Polymers*, first public 2005-08-03, https://arxiv.org/pdf/cond-mat/0508094 ; inspected sections on backbite and finite lattice transition graph.
- M. Conder and P. Dobcsányi, *Trivalent symmetric graphs on up to 768 vertices*, 2002, https://www.math.auckland.ac.nz/~conder/preprints/cubic768.pdf ; checked classification scope, with the published Foster uniqueness used for identification.
- I. J. Dejter, *From the Coxeter graph to the Klein graph*, arXiv 2010-02-09, https://arxiv.org/pdf/1002.1960 ; inspected definition, Coxeter/Heawood relation, and conclusion.
- A. Kazazi, *Connectivity of the reconfiguration graph of Hamiltonian paths*, 2026-10-04, https://arxiv.org/abs/2610.05068 ; abstract only, full text inaccessible.

The theorem has no claims about other cubic graphs, random-walk mixing times, or absolute historical priority. It has not been checked by a separate external mathematical reviewer.

Self-review: passed. Independent audit: not yet performed.
