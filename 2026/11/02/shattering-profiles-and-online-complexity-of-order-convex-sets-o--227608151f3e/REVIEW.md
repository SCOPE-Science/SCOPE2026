# Independent mathematical audit

## correctness

PASS

PASS: Every nonempty convex subset C of [2]x[n] has unique canonical downclosure J and I=J\C; J and I are ideals and maximal J elements lie outside I. Summing two-row row-prefix ideals gives N_n=(n^4+4n^3+17n^2+14n+12)/12. For an arbitrary poset a support is shattered iff it contains no strict 3-chain: convex hull of each trace is its up/down closure intersection. Two-row three- and four-point chain-free support counts yield the polynomial and VCdim 2,3,4 by n. Independent brute convex enumeration plus full trace checks passed n<=6. Two incomparable row strips support independent endpoint threshold trees, giving lower Ldim 4log2 n-O(1), while |C| gives 4log2 n+O(1). The submitted exact n<=10 Ldim table comes from a mathematically exhaustive exact version-space recursion with inspected verifier and stored witness certificate; independent executable replay this run covered n<=6, not 7..10. Larger-n exact Ldim not claimed.

## originality

PASS

A directly relevant overlooked 2015 full-text primary paper by Queyranne–Wolsey already proves the ideal-difference characterization of convex subsets of ANY finite poset (Lemma 1). That is expressly prior, not new. Its results are convex-set optimization and polyhedral formulations, not VC shattering polynomial or online Littlestone ranks for [2]x[n]. Other metric/geodesic convex learning papers use different objects. Best-of-knowledge originality rests only on new enumeration and learning results.

## value

PASS

PASS: The object is the entire natural order-convex concept class of the minimal non-chain product [2]x[n], not an arbitrary slice. A sharp static VC cutoff, complete shattering polynomial, and unbounded adaptive Ldim with exact log coefficient distinguish batch from online learning. Exact small-n ranks and anomalous saturation furnish useful finite benchmarks. The general ideal-difference representation is credited as prior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
