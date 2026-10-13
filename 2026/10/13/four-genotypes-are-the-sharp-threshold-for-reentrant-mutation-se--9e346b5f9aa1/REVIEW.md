# Scientific review: sharp reentrant mutation–selection ordering

## Correctness — PASS
For every connected mutation graph of order at most three, eigenvector identities and strict monotonicity of the top eigenvalue prohibit two strict pairwise rank changes. For the stated four-genotype path, characteristic-polynomial division, a resultant, three rational root brackets and a second-eigenvalue bound establish precisely two genuine Perron-vector intersections, with opposite signs outside and between. `verify_reentrant.py` recomputes all nontrivial polynomial identities. Numerical eigenvectors are illustrations only. No larger-network theorem is claimed.

## Originality — PASS
The classical mutation–selection model and fitness–frequency mismatch are not new. Epstein studies replication-plus-diffusion genotype dynamics; Kostova and colleagues analyze genotype dominance in an Eigen replication/degradation model; Barbosa and colleagues study graph-constrained quasispecies; Seifert and colleagues analyze fitness inference and explicitly mention discordance between fitness and equilibrium frequency. Their inspected results do not state or directly imply the sharp four-genotype threshold and exact two-switch path. There remains a material risk from inaccessible full papers or a more general spectral-ordering theorem; independently check any external priority claim.

## Value — PASS
The result identifies the minimum number of mutually mutating genotypes required for one pair's equilibrium abundance ranking to leave and then return to its original order as a control parameter increases. Two comparator genotypes have different mutation connections to an exceptionally fit neighbor, giving a structural explanation rather than an unmotivated fixed-size census. Exact roots provide a benchmark for interpreting shifts in variant frequencies. Scope is restricted to deterministic, fixed-fitness, symmetric equal-edge mutation.

## Closest literature and limitations
Relevant scientific sources are Epstein (2006, arXiv:q-bio/0602027), Saakian and Hu (2006, doi:10.1073/pnas.0504924103), Kostova–Zhou–Zemla (2011, doi:10.1080/17513758.2010.544766), Barbosa–Donangelo–Souza (2011 preprint, arXiv:1112.3322), and Seifert et al. (2014, doi:10.1534/genetics.114.172312). Only part of several original full texts could be accessed; see the structured originality assessment for source-specific risks. No empirical, stochastic or broader-graph assertion is included.

Self-review: passed. Independent audit: not yet performed.
