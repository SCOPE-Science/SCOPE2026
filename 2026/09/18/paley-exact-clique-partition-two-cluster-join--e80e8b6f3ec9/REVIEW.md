# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The lower bounds are immediate from the standard cut inequality and a four-edge induced K_{2,2} witness for the covering number. The upper construction was checked algebraically at the level of every edge type. The finite-field map T_r is invertible because 1-r^2 is nonzero; it sends the two quadratic-character edge classes according to the sign of 1-r; and, because r is a nonsquare, a fixed crossing edge can occur in at most one K_4 from a fixed cell. The four cells therefore use every internal edge exactly once and no crossing edge more than once, leaving exactly 4q crossing edges as singleton K_2 blocks. The resulting partition has q^2+3q cliques, matching the lower bound.

The congruence obstruction was separately stress-tested through the equality conditions in both oriented cut inequalities. Simultaneous equality forces every block to have side sizes (1,1) or (2,2). For odd k this forces a (k-1)/2-regular assignment graph in each cell; when k == 3 (mod 4), that graph would have odd order and odd degree, which is impossible by the handshake lemma.

No computational claim is needed for either proof.

## Originality

The closest direct source is Bo Ning, arXiv:2608.11536 (2026). Its construction uses the same family G_{h,k}; Proposition 3.1 states an exact formula for even k under h >= k-1, using a one-factorization of K_k. The present theorem instead has h=2 and odd prime-power q == 1 (mod 4), so for q >= 5 it lies outside that exact regime and requires a different finite-field mechanism. The same source supplies the cut lower bound used here but does not state the two-cluster formula or the odd congruence obstruction.

Searches were made for the exact formula q^2+3q, for G_{2,q} and (2K_q)∨(2K_q), for Paley/quadratic-character clique partitions, and for equivalent design-language constructions involving Room/Howell designs and orthogonal edge pairings. No source found stated or implied the theorem above.

Older primary literature inspected included Erdős--Faudree--Ordman (1988) and Caccetta--Erdős--Ordman--Pullman (1985), which develop clique-partition/covering tools and earlier large-spread constructions but did not reveal this exact two-cluster result.

### Residual literature risk

W. D. Wallis and G.-H. Zhang, *On the partition and coloring of a graph by cliques*, Discrete Mathematics 120 (1993), 191--203, was located bibliographically, but its full theorem text was not inspected here. It is relevant because it concerns general clique partitions and may encode specialized constructions not visible from metadata. Classical Room-square, Howell-design, and orthogonal-design literature is another plausible source of an equivalent edge-pairing construction under different terminology. No concrete statement located in those searches covered the present graph-parameter equality, so this is treated as residual rather than affirmative prior coverage.

Originality is therefore assessed as PASS to the best of our knowledge, with the above residual risk explicitly retained.

## Value

The result fills a qualitatively different exact regime in the construction central to the newest asymptotic spread theorem: two clusters rather than h growing at least as large as k-1, odd rather than even clique order, and a finite-field orthogonality mechanism rather than one-factorization. The parity obstruction on k == 3 (mod 4) further shows that attaining the cut lower bound at h=2 has genuine arithmetic structure rather than being a routine extension of the even-k formula.

## Scope limitations

No exact value is claimed for k == 3 (mod 4), only strict nonattainment of the cut lower bound. No claim is made for non-prime-power k == 1 (mod 4), or for a complete characterization of all h,k attaining the cut bound. No independent validation or independent audit is asserted.
