# Independent mathematical audit

## correctness

PASS

Both maps are rank n−1: a collides {n−1,n} and omits n, b collides {1,n} and omits 1. Any proper prefix ends in a and lacks n, or ends in b and lacks 1; hence b is effective only as the initial letter. Later drops must be a, and after each effective a a further effective a needs an intervening b. This forces at least 2s−2 symbols and unique equality word (ba)^(s−1) for s≥2 (at s=1 either a or b works). The complement after k blocks is {n,2,4,...,2k} through k=ceil(n/2)−1, when the next ba has no new drop. Independently reproduced exact subset BFS for n4..13 including unique words and strict saturation; packaged n4..18 BFS and n4..200 witness verification source inspected.

## originality

PASS

Best-of-knowledge PASS: AGV 2010/2013 full texts show the named nonpermutational D''_n and its quadratic reset length n²−3n+2 but no initial alternating rank profile, exact threshold or uniqueness; endpoint does not logically imply them. No located duplicate, but semantic outage and unindexed rank terminology remain residual.

## value

PASS

A sharp universal half-rank bottleneck and unique alternating minimum words for a highly structured nonpermutational slow synchronizer, contrasting its known quadratic reset length. The collision-based proof identifies a genuine structural obstruction rather than just repeating reset folklore.

The dated certificate retains the supplied scientific assessment, sources and limitations.
