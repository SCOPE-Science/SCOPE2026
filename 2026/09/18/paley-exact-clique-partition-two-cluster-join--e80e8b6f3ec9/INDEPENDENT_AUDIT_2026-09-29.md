# Independent audit — 2026-09-29

Record: `2026/09/18/paley-exact-clique-partition-two-cluster-join--e80e8b6f3ec9`  
Assigned and audited source tree: `15081308cc54678f91f4e68c719d657e431b8644`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**independently_supported**. The cut lower bound and the Paley pairing construction check. For q≡1 mod 4 the quadratic-character edge classes of K_q are well defined; for either desired sign of χ(1-r) there is a nonsquare r, and the linear map (x,y)↦(x+ry,rx+y) is invertible because r≠±1. It maps the chosen character class bijectively to the required class. For a fixed crossing edge, the two possible input differences differ by the nonsquare factor r, so at most one belongs to the chosen class; consequently the four cellwise K_4 families never repeat a crossing edge. They use every internal edge exactly once and q(q−1) K_4 blocks, leaving 4q crossing edges as K_2 blocks, for q^2+3q blocks. I also reconstructed the congruence obstruction: equality in both oriented cut inequalities forces every useful block to have side sizes (1,1) or (2,2); for k≡3 mod4 each cell would then induce a (k−1)/2-regular graph on odd k vertices with odd degree, contradicting the handshake lemma. Direct finite-field checks for small admissible prime q agree with the construction.

## Originality

**supported_qualified**. Bo Ning’s 2026 paper treats the same G_{h,k} family and attains the cut bound for even k under h≥k−1 using one-factorizations. The present h=2, odd prime-power q≡1 mod4 regime is outside that theorem and uses a different quadratic-character pairing. Searches did not locate the exact q^2+3q formula or the k≡3 mod4 nonattainment argument. Older clique-partition and design literature remains a residual equivalence risk, so priority is asserted only for this exact two-cluster formulation to the best of current evidence.

## Scientific value

**meaningful_exact_regime**. The result fills an exact infinite regime omitted by the recent even-order construction and shows that cut-bound attainment at h=2 has arithmetic structure rather than being parity-insensitive. The complementary obstruction is useful even though it does not determine the full k≡3 mod4 value.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/paley-exact-clique-partition-two-cluster-join--e80e8b6f3ec9
- https://arxiv.org/abs/2608.11536
- https://www.renyi.hu/~p_erdos/1988-04.pdf
- https://www.renyi.hu/~p_erdos/1985-35.pdf

## Limitations

- The exact formula is only proved for prime powers q≡1 mod4, q≥5.
- For k≡3 mod4 the result proves only strict nonattainment of the cut lower bound, not the exact partition number.
- Classical design literature was searched but not exhaustively reducible to the present graph parameterization; originality is therefore qualified.
