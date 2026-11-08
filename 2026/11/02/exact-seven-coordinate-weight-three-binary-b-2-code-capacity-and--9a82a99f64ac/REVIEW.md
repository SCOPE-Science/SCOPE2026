# Independent mathematical audit

## correctness

PASS

The 35 candidate triples on seven coordinates produce 595 unordered distinct-word sums and 630 distinct forbidden quadruples of triples from collisions; equal-sum input pairs cannot share one triple. Every feasible code is exactly an independent set avoiding all 630 four-hyperedges. A 7-cap on each coordinate degree follows from the C4-free link graph on the other six vertices (sharp edge extremum 7). The inspected C++ exhaustive branch-and-bound enumerates all completions containing fixed {0,1,2}, which is without loss for codebooks >=14 under S7 symmetry; pruning excludes only forced conflicts and tight link degrees. Independent separately implemented C++ complete search found no 15-word solution, 48 size-14 solutions through the fixed triple, all 2-(7,3,2), and generated 630 conflicts (independent search-node counts differ because branching differs). Direct cyclic witness has 14 sums-unique triples; 35*48/14=120 labeled optima and its S7 orbit has size 120, hence single orbit and double-Fano classification. The result is an exhaustive finite certificate for exactly n=7,k=3, distinct pairs, not a general extremal theorem.

## originality

PASS

Meszka–Rosa 2018 already classify simple double Fano planes as one isomorphism class with 120 labeled designs; that portion is expressly not novel. Sima et al. 2023 study constant-weight binary B2 code bounds and large parameters; inspected full text does not provide the exact n=7 weight-3 optimum and pair-sum extremizer equivalence. Novelty is the B2 extremal correspondence and computer-certified upper bound, not the known design enumeration. Best-of-knowledge PASS.

## value

PASS

Fixed-length Sidon/B2 constant-weight codes and optimal designs are natural in coding and combinatorics. The exact seven-coordinate capacity plus complete optimizer rigidity answers a genuine small extremal question, not an arbitrary renamed design count; small but mathematically motivated complete classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.
