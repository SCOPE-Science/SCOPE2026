# Independent mathematical audit

## correctness

PASS

Strict concavity and b'(e*)=c give the best response max(0,e*-neighbor effort), so specialized equilibria correspond exactly to maximal independent sets, and strict increase/concavity gives 0<t<1. Consumption is e* or 2e*, hence only t*a(I)-m affects ranking. Internal zero gaps have length one or two, endpoint zero runs length zero or one. The gap count is n=3m-2-a+e. For ceil(n/3)<=m<=floor((n-1)/2), e=2 is feasible because 0<=3m-n<=m-1, and achieves the upper bound on a. At m=M the universal cap a<=M-1 is attained by taking singleton gaps and n-2M+1 zero endpoints. The proof's 'all interior gaps are singletons' here describes an attaining configuration, not every size-M set (even paths can have size-M sets with a double gap). The slope 3t-1 and the top-score differences t-1 (odd) and 2t-1 (even) give the strict and tie cases, including the sole-count cases n=2,4. The first even order with ell<u<M is 12; the three displayed strings attain the claimed scores, and the exponential benefit family realizes the entire open t range. An independently written exact-rational replay enumerated 2508 maximal independent sets at n=2 through 23, checked 66 fixed-count maxima, 176 score comparisons and the stated witnesses; finite corroboration, not the all-orders proof. Replay: /workspace/branches/b782af14-3d15-44d3-b10e-6d59bb3a8150/independent_replay.py and replay_n2_23.txt. The uploaded script was not executed.

## originality

PASS

The specialized-equilibrium/maximal-independent-set correspondence and qualitative welfare precedents are credited to the original literature. The supported distinct claim is the exact welfare envelope under the graph-local overlap reward, with every maximizing count and fixed-count criterion including both tie parameters and the first three-regime path. The inspected graph reformulation and game results do not state or imply this envelope without the new fixed-cardinality overlap calculation. This is a bounded comparison, not exhaustive historical priority.

## value

PASS

This exact envelope identifies which specialized configurations a one-parameter change in benefit shape selects, when all regular counts tie, why the upper alternating count behaves differently by parity, and the smallest path with two genuinely different transitions. It resolves both value and optimizer behavior for the whole natural path family, not a few enumerated path sizes or a new name for independent domination.

The dated certificate retains the supplied scientific assessment, sources and limitations.
