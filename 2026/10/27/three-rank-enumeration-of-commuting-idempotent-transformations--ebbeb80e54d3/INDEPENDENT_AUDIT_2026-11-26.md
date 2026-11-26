# Independent mathematical audit

## correctness

PASS

For commuting idempotents the composite h is a retraction onto the simultaneous fixed set; each h-fiber is preserved. In one fiber, the root contributes one to both image ranks and to the composite rank. The p other e-fixed points are sent to the root by f and the q other f-fixed points are sent to it by e. Each remaining point chooses any of p+1 and q+1 respective targets, independently, and both composites are consequently the root. This is a bijection. Multiplying the labeled root and subset EGFs and then taking an unordered set of rooted fibers gives exactly the stated expression, including the empty map pair and ordered roles for e and f. The intersection size and union size give the necessary inequalities; one fiber with p=a-k, q=b-k, r=n-a-b+k and k-1 singleton fibers gives sufficiency. Independent replay (python3 /workspace/checks/check124.py, record 4) brute-forced all functions up to n=5, tested all ordered idempotent pairs and matched the full rank cells to a separately implemented labeled-set partition expansion. That expansion also confirmed support through n=8 and totals 1, 7, 58, 601, 7616, 113989, 1963060, 38178193 at n=1 through 8; the analytic bijection proves the unbounded theorem.

## originality

PASS

Support inequalities already occur in a related larger census, and the core fixed-idempotent structure is classical. The distinct supported claim is the full joint-rank enumerator with simultaneous commutation and idempotence on the unrestricted labeled set. Neither a checked larger but unrefined census nor a narrower monoid supplies that enumerator.

## value

PASS

The natural simultaneous generator and meet ranks of a semilattice action give a full distribution, not just a support law or a few total counts. This supplies all rank-conditioned commuting counts, a useful invariant for labeled finite retractions. The rank-cell enumerator, rather than the already related support inequalities, carries the value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
