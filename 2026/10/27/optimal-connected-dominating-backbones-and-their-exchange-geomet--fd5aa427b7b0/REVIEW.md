# Scientific review

## Correctness — PASS

The five-vertex lower bound is proved by internal-edge/boundary counting and the two-common-neighbor property of the cube. A concrete path proves attainability at six. The complete 11-orbit classification of all 1,952 connected six-sets establishes that precisely the 192-element path orbit dominates the cube. Independently generated coordinate-word paths agree with that orbit; explicit exhaustive exchange adjacency and breadth-first searches from all 192 states establish regularity, connectedness, diameter and every distance count. The executable proof certificate is `verify.py`; no extrapolation to other dimensions is made.

## Originality — PASS, subject to stated limitations

Griggs's hypercube spanning-tree work and older connected-domination papers establish the framework, and Chen–Syu (2012) is directly relevant to the minimum connected-domination number. None of the *inspected* full texts records the combined all-optimal-path classification with the optimum-preserving exchange-graph distance distribution. Search comparisons against published mathematical records and the primary literature did not identify an implication that would recover the exchange metric. The complete text of Chen–Syu was inaccessible and could contain overlap with the minimum-set component; a connected-dominating-subsets database may include implicit enumeration. In neither case is the full exchange-graph profile demonstrated to be previously covered. Residual unindexed prior coverage remains possible; lack of a search result is not a proof of universal novelty.

## Value — PASS

Maximum-leaf spanning trees of hypercubes are a natural network-backbone extremal problem. Beyond the known minimum cardinality, all 192 optimal backbones have a concrete coordinate-word description. The connected 4-regular exchange graph and its exact diameter quantify whether globally optimal backbones can be locally reconfigured without losing optimality; this is not a textbook consequence of \(\gamma_c(Q_4)=6\). The complete finite result gives a benchmark for optimizer reconfiguration even without an infinite-dimensional theorem.

## Limits and references

The proof is an explicit exact finite classification, not a claim about arbitrary hypercubes. Especially relevant are Camby–Schaudt, arXiv:1303.2868v1; Mane–Waphare, DOI:10.1080/09728600.2012.12088957; Chen–Syu, IPCSIT 41 (2012), 15–19 (full text unavailable); Griggs, INTEGERS 21A #A13 (2021); and OEIS A291704 (different enumeration).

Self-review: passed. Independent audit: not yet performed.
