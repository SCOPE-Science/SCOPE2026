# Independent mathematical audit

## correctness

PASS

The binary 2-adic valuation definition p_{t−1}=d_e⊕(j mod2) for t=2^e(2j+1) gives the exact eight-letter decomposition B_j=[a,b,1−a,x_j,a,1−b,1−a,y_j] of every dyadic prefix W_k, k≥3, with 2^{k−3} blocks and last bit y=d_k. Greedy binary arch factorization counts the largest h such that every binary scattered subsequence length h occurs: each completed arch contains both letters, and the sequence of last arch letters followed by a final missing letter witnesses failure at h+1. The eight-letter transition table holds for all x_j,y_j and reachable pending-letter states: a≠b yields exactly 3 arches per block; a=b yields contribution 3−I_j on an empty state or 4−I_j on pending 1−a, and next state I_j(1−a). The corrections telescope over blocks to 3*2^{k−3}−1_{d0=d1≠d_k}. Independent code exhaustively enumerated all 8-block parameter/state transitions and every 2^{k+1} instruction prefix for k=3..8, and independently constructed the valuation bits and greedy arches. The one-quarter defect follows by counting triples (d0,d1,dk), and 3/8 normalized limit by dividing by 2^k. The all-instructions all-k theorem is proved by transitions and telescoping, not finite prefixes.

## originality

PASS

Barker et al. (2020) formally define scattered-subsequence universality and greedy arches for arbitrary words; Schnoebelen–Veron (2023) give arch-jumping algorithms and universality signatures. Those general procedures can in principle compute any supplied finite prefix but do not yield the exact dyadic closed expression uniformly for every infinite binary paperfolding instruction stream, including its first-two-versus-depth-k defect. Holub (2012/2013) proves abelian powers of paperfolding words, a different contiguous Parikh-block invariant. Shallit (2024/2025) classifies runs and synchronized statistics, also distinct. The Goč–Mousavi–Schaeffer–Shallit CiE 2015 paper on generalized paperfolding factors is a plausible overlap source, but lawful OA and publisher retrieval did not yield full text; this is a stated residual risk rather than a fabricated NOT_COVERING assertion.

## value

PASS

The largest h for which a word contains every binary scattered subsequence is a standard natural invariant; an exact formula for all instruction streams over a self-similar family is stronger than a routine one-prefix computation or unmotivated subsequence count. The universal 3/8 density, sharp one-unit boundary defect, and precise dependence on d0,d1,dk are structural and explain the mechanism; no general theory of all nondyadic prefixes or all shortest absent subsequences is claimed.

The dated certificate retains the supplied scientific assessment, sources and limitations.
