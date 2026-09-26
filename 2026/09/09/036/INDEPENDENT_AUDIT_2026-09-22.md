# Independent audit — 2026/09/09/036

Date: 2026-09-26. Disposition: retain accepted.

## Correctness — PASS

I independently enumerated all (2^{20}=1,048,576) triangle masks under all 720 vertex permutations, marking each orbit. This produces 2,136 total orbits, 2,102 covering representatives, and 1,042,642 labelled covering masks; the 2,102 representatives exactly match the stored CSV mask set. For every representative I rebuilt the integral edge–triangle boundary matrix and independently calculated its rational rank, graph component count and ranks modulo every prime (ple241) (53 primes). All 2,102 stored (E,b_0,b_1,b_2) values agree. Only mask 242467 loses rank modulo a prime, and only for (p=2). Every nonzero rank minor has absolute determinant at most (3^{r/2}le3^5=243) by Hadamard (each triangle column has three unit entries, and (rle10)), so testing every prime up to 241 excludes other torsion primes.

For the unique orbit I checked (d_2(1,ldots,1)=2c), (d_1c=0), (w,d_2=0pmod2), and (wcdot c=1pmod2). An independently selected (10	imes10) edge–triangle minor on edge indices (0,1,2,3,5,6,7,9,10,12) has Bareiss determinant (-2). Rank drops by exactly one modulo 2, and the determinant bound by 2 fixes the nonunit Smith factor as 2. Thus (H_1=mathbb Z/2), (H_2=0). Its ten triangles form the familiar six-vertex (mathbb RP^2) triangulation. The published result about no torsion on at most five vertices is consistent with the known sharp minimum.

## Originality — PASS, narrowly

The six-vertex (mathbb RP^2) and its (mathbb Z/2) homology, minimal vertex count and unique minimal triangulation are prior facts. The closed 2,102-type triangle-family homology and signature table, including the statement that this is the sole torsion orbit among all such complexes, was not found in the checked manifold and small-complex literature. The datum is an exhaustive finite classification, not a new example of torsion or general torsion theorem.

## Scientific value — PASS, bounded

The full small-complex table and unique torsion orbit offer a reproducible baseline for homology algorithms and extremal simplicial-complex questions. Its novelty and value lie in the broader family of pure triangle complexes, not in rediscovering projective-plane homology.

## Sources

- Lutz, small triangulated-surface tables: https://page.math.tu-berlin.de/~lutz/stellar/surfaces.html
- Newman, *Small simplicial complexes with prescribed torsion in homology*, arXiv:1707.09271: https://arxiv.org/abs/1707.09271
- Ripke and Yoon, *Characteristic Independence of Betti Numbers of Monomial Ideals in Five Variables*, arXiv:2607.10639, cites the sharp five/six-vertex torsion boundary: https://arxiv.org/abs/2607.10639
- Candidate `artifacts/census_2102.csv` and `artifacts/witness.json`; independent orbit, modular-rank and determinant computations above.
