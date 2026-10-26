# Self-review

## Correctness — PASS

The object is fixed as the 26-vertex point–line incidence graph of \(\operatorname{PG}(2,3)\), with exact projective triples and unit graph edges. The C++17 program tests all \(657800\) seven-landmark and \(1562275\) eight-landmark combinations, yielding zero and 9,828 resolving sets respectively. All 9,828 are balanced four-points/four-lines. It checks all five incidence-preserving generators, their 11,232-element generated group, and the four completed orbits with cardinalities \(936,1404,1872,5616\). An independent Python implementation uses one-sided incidence signatures rather than distance-pair masks and reproduces all four geometric counts, including the exceptional collinear/concurrent case. Exact finite enumeration proves this domain only; neither a sample nor a heuristic is treated as exhaustive evidence.

## Originality — PASS, subject to stated risk

The primary Héger–Takáts 2012 work already states \(\dim(G)=8\) at order three and classifies optimal-size resolving sets only for projective-plane orders \(q\ge23\). Bailey's 2015 published table independently records the same minimum size but not a complete set/orbit enumeration. We therefore make no originality claim for the minimum eight or for their general incidence criteria. Published-record and targeted literature searches for the exact count, point/line balance, alternate wording and symmetry/orbit reductions found no dominating statement or matching table. The absence of a search hit does not establish uniqueness; unindexed supplemental computations remain a real residual risk.

## Value — PASS

This is a full classification of a natural optimum-locating problem in a small projective plane where the large-order classification does not apply. The four distinct projective incidence shapes and stabilizers provide useful structure beyond an isolated integer. The contrast with the known minimum split-resolving cardinality twelve explains why the eight-point optimum uses both vertex types cooperatively. The work is a self-contained finite census, not an infinite theorem or an independent validation.

## Closest literature and boundaries

Héger–Takáts, *Electronic Journal of Combinatorics* 19(4) (2012), #P30, `arxiv:1207.5469`; Bailey, *Australasian Journal of Combinatorics* 62 (2015), Table 4, `arxiv:1312.4973`. These support known definitions and minimum cardinality but do not report the claimed complete four-orbit census. Unindexed prior data cannot be excluded.

Self-review: passed. Independent audit: not yet performed.
