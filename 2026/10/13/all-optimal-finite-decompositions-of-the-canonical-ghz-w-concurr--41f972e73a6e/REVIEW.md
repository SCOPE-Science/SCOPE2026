# Self-review

## Correctness
PASS. For \(0<\lambda<1\), the source objective \(g(r)=(5\lambda^2r^2-4\lambda r+8)/9\) is strictly convex and the HJW constraints give \(\sum_jp_jr_j=1\). Equality in Jensen therefore forces \(r_j=1\) term by term. The probability identity then forces both HJW row entries in each column to have modulus \(\sqrt{p_j}\), while row orthogonality is exactly the zero-barycenter equation for their relative phases. The converse reconstructs a co-isometry from any such phase polygon. Rank two excludes support one, and the two-vector zero-sum equation forces equal weights and antipodal phases. Phase independence of the pure-state fill was independently checked from \(4\det\rho_A=(5q^2-4q+8)/9\).

Risk: the classification assumes the standard finite HJW parametrization and the source's scalar convex-roof reduction. Both were checked against the anchor; no numerical experiment is used as an infinite proof.

## Originality
PASS. Full-text inspection of arXiv:2608.07145v1 found the Jensen lower bound, the statement that many co-isometries can attain it, and one four-column optimizer, but no equality-case theorem, zero-barycenter phase-polygon classification, or support-minimality statement. Focused semantic searches covered those aliases and the exact source identifier. Aggarwal's related generalized GHZ/W concurrence-fill work provides eigenstate formulas and an upper bound, not this exact canonical equality classification. Classical HJW theory parametrizes ensembles but does not impose the concurrence-fill optimum.

Risk: the anchor is recent, so an equivalent short corollary could exist in an unindexed follow-up. The closest inspected literature did not contain it.

## Value
PASS. The result turns a convex-roof value plus one witness into the complete finite optimizer geometry. It reduces the preparation support from the source's displayed four labels to the exact minimum of two and identifies every other optimum through a simple complex barycenter condition. Equality structure and minimum ensemble cardinality are natural invariants of a convex-roof solution and are directly useful for reproducing or benchmarking the source construction.

Risk: the simplification is special to the canonical GHZ–W family; it should not be extrapolated to arbitrary rank-two states.

## Closest literature and limitations
The decisive comparison is arXiv:2608.07145v1 itself. arXiv:2506.16935v2 is the closest earlier concurrence-fill treatment of generalized GHZ/W mixtures, while the HJW theorem is the structural ensemble parametrization. None implies the full iff equality classification stated here.

Self-review: passed. Independent audit: not yet performed.
