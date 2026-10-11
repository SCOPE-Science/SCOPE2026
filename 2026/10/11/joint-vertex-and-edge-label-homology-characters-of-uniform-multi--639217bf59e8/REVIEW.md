# Same-model review

## Correctness — PASS
The underlying multiclique poset is identified with the edge-inflated simplex of Ayzenberg--Rukhovich, whose theorem proves homology concentration in degree \(n-1\). The original argument independently derives the signed cellular fixed-point trace: stable faces are cycle unions, orientation signs cancel to \((-1)^{|J|-1}\), and orbit enumeration of pairs gives the exact \(\gcd\)/\(\operatorname{lcm}\) exponents. The Hopf trace formula then fixes the full character. For the three-vertex quotient, the invariant cellular degree-one group is zero, while the invariant degree-two group is the exterior cube of the edge-label module. Direct signed traces, exact mod-two boundary ranks and low-degree exterior-character comparisons replay using `verify.py`. The checked computations cover finite cases only; the infinite statement follows from the stated general argument and the cited wedge theorem.

## Originality — PASS, with qualifications
The 2020 primary source already proves the multiclique homotopy type and top Betti count, and the 2026 source proves their generalization to flabby finite étale spaces. Both accessible full-text sources were examined for equivariant statements, including the original functoriality section. Neither states the joint \(S_n\times S_q\) homology character, the cycle-type orbit formula, or the exterior-cube quotient module. Published-index and broader mathematical literature searches did not identify a stronger covering claim. The result is an **equivariant refinement**, not a new nonequivariant homotopy theorem. A formally equivalent unindexed character calculation remains possible.

## Mathematical value — PASS
The joint character determines all rational irreducible multiplicities of the complete two-group action from cycle types, reducing a cellular problem with \(q^{\binom n2}\) top cells to subsets of the vertex cycles. The three-vertex quotient detects \(\binom q3\) surviving two-dimensional rational classes and their full color-permutation structure; Betti numbers of the unquotiented complex do not provide this. The complete formula is a reusable invariant for symmetric multigraph clique complexes, a family used in combinatorial topology and network-oriented complexes. No downstream theorem beyond these exact topological symmetry statements is claimed.

## Closest literature and limitations
Ayzenberg--Rukhovich, arXiv:2012.07600v1, Theorem 1 and Sections 4/6/7; Ayzenberg--Khoroshavkina, arXiv:2602.08694v1, Proposition 4.12, Theorem 5.1, Corollary 7.2. These supply underlying homotopy concentration, not the claimed equivariant computation. The theorem is rational, and the literature search cannot establish absolute novelty.

Same-model review: passed. Independent audit: not yet performed.
