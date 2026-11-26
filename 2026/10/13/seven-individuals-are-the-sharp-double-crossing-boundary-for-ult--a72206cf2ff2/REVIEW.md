# Independent mathematical audit

## correctness

PASS

The four root-anchored edges have lengths H−h,H−h,H,h and abundance coverages a,b,c,a+b; the edge-miss probability for z covered individuals is C(N−z,m)/C(N,m), with the zero convention. Both profiles therefore have PD H at m=1 and 3H−h at m=N. I inspected the proof, notes and checker, and independently enumerated actual individual subsets. A subset's PD divided by H is its represented-taxon count minus t times the indicator that both sisters occur. Enumerating the sorted-sister profiles via cut positions gave sizes 1,2,4,6,9 and 58 unordered pairs. For every pair I used the subset counts as exact affine coefficients and checked all open root cells and interior roots (116 tests), dropping all zero signs. This confirms absence below N=7 and the three open intervals (1/2,13/23), (1/7,3/17), and (1/5,3/13) for the stated pairs in order, including ties at the excluded endpoints. The H=9,h=2 witness gave differences (1/21,−1/35,−1/35,1/7,2/7). Replay: python3 -I /workspace/review_math.py 1. Minor documentation overstatement: the frozen checker explicitly asserts only the third coefficient list, although it checks the sign cells for all pairs. My independent subset check reproduced all three lists; no change to the theorem is needed.

## originality

PASS

The supported distinct claim is the minimum common census and all three profile intervals for two strict depth-order reversals. Exact PD expectation and changes in site rankings under rarefaction were already known. The closest primary and published catalogue comparisons do not settle this specific multiple-crossing boundary.

## value

PASS

A three-tip tree is the first rooted ultrametric shape with a shared internal edge. The result pinpoints when that edge can cause a double reversal even without unequal censuses or missing taxa, contrasting with the closest expected-richness single-crossing result. The sharp finite cutoff, exact windows and endpoint behavior give a sensitive benchmark for sampling-depth comparisons and for any proposed general crossing bound.

The dated certificate retains the supplied scientific assessment, sources and limitations.
