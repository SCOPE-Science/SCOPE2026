# Independent mathematical audit

## correctness

PASS

The exact model is a path P_n, n>=2, one uniformly chosen seed, one independently successful contact per edge of probability 0<q<=1, and a distinct time order. By uniqueness of the underlying path, target v can be reached from u exactly if the consecutive edge contacts increase in that direction, with probability q^{|u-v|}. Each adjacent unordered pair contributes 2q/n; distance-two pairs contribute q^2/n; every length d>=3 contributes 0 or q^d/n according to monotonicity of its edge-time subword. This yields min 1+2(n-1)q/n+(n-2)q^2/n and max 1+2(n-1)q/n+sum_{d=2}^{n-1}(n-d)q^d/n. For n>=4 all positive long-interval contributions vanish iff signs of adjacent time differences alternate; all are present iff the entire time list is monotone; n=2,3 tie. Independent random order makes each length-d interval monotone with probability 2/d!, yielding mean 1+(2/n)sum_{d=1}^{n-1}(n-d)q^d/d!. The index case has q*deg(u) expected direct offspring, hence 2(n-1)q/n after uniform averaging, independent of order. For q=1-1/n dominated convergence gives min->4, max/n->1/e, random mean->2e-1 and max/min~n/(4e). Reviewed RESULT.md, definitions and independent event-by-event verify.py. Unique-path proof is global; the finite event simulation for n<=7 and q in {1/2,2/3,1} is corroboration, not infinite proof.

## originality

PASS

The all-order uniform-seed stochastic mean, equality calendars, random-order factorial average, and common-direct-offspring unbounded separation are not asserted in the inspected older temporal-outbreak and reachability results. The general temporal SI reachability argument and R0 inadequacy are prior art. The same-source zero-forcing result has a different propagation and objective; an unlocated average-reachability theorem remains a historical risk.

## value

PASS

This is a motivated exact extremal question for time-respecting single-contact epidemics: calendars on the same graph and with the same index-case direct reproduction mean yield an unbounded ratio of final outbreak sizes. Both sharp equality classifications and random-calendar baseline give useful quantitative comparators, beyond a textbook reachability observation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
