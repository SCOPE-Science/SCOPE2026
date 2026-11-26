# Independent mathematical audit

## correctness

PASS

For each fixed live-edge state, induction in the synchronous one-round model identifies first infection with the first finite directed distance from the seed. The post-deletion reachable set is a subset. If the original maximum finite distance is 0 or 1, all remaining reachable nonseed vertices retain their direct arc from the seed and the maximum cannot increase. Otherwise the original maximum is at least 2, and the new one is at most n−2 by simplicity of shortest paths; these cases give max(0,n−4), including n=2,3,4. The supplied attaining family has maximum distance 2 before deletion and n−2 after, with exactly one vertex removed from reachability, and an empty graph attains zero in the small cases. For the specified five-vertex independent-edge model, an independent topological pass on all 64 states gives expected-duration coefficient vectors (0,2,2,1,−3,−1,1) and (0,1,1,1,0,0,0), in increasing powers of p, before and after deletion; exact rational substitution brackets p_c as stated. Replay: `python /workspace/branches/review-computations/check_finite.py`. This confirms the finite polynomial rather than extrapolating a simulation. The quintic has Q(0)=1,Q(1)=−1 and Q″=2p(10p²−6p−9)<0 for 0<p<1, with Q′ strictly decreasing from 1 to −7, so exactly one crossing occurs. The clock is last new infection; adding one generation to both times leaves their difference unchanged. Read the frozen verification notes and code without executing them.

## originality

PASS

The live-edge representation, monotonicity of ever-infection and the general possibility of longer epidemic duration in another model are credited precedents. The statement-level checks identify no theorem covering the exact fixed-source maximum finite distance change under one nonseed deletion, its sharp all-size bound, or the specified homogeneous five-vertex mean-duration threshold. Priority for equivalent elementary graph observations remains uncertain.

## value

PASS

The exact sharp bound and small-size obstruction distinguish a legitimate duration statistic from cumulative case count under the same idealized intervention. The minimal-size fixed example and exact threshold test whether the pathwise distinction survives taking expectations, rather than merely exhibiting one exceptional state. The result is finite graph theory and a caution about model metrics, not an applied inference about real vaccination choices.

The dated certificate retains the supplied scientific assessment, sources and limitations.
