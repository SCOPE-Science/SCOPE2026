# Independent mathematical audit

## correctness

PASS

For fixed d>=k>=3, a shattered support S with m>=3 has a private coordinate for each element, none shared, so m<=k since S lies in a k-face. At m=k all varying coordinates are private, giving unit-vector support up to cube symmetries; trace of two selected unit vectors needs k−2 extra free coordinates, so d>=2k−2. Trace constructions give sufficiency, and unique representation yields exactly 2^d*C(d,k) maximal supports. For Littlestone, after an all-positive path every splitting query introduces a new varying coordinate, giving Ldim<=k+1. When d=2k−1, positive root version space corresponds to k-subsets of 2k−1 coordinate axes and admits depth k by explicit subset queries; negative root version space contains an opposite facet with VCdim k. Hence Ldim=k+1 for d>=2k−1. Independent exhaustive VC support checks returned exactly 64 for (4,3) and 320 for (5,3), and an independently found/replayed depth-four tree for (5,3). Claim explicitly leaves intermediate online range unclassified.

## originality

PASS

The exact-width signed-conjunction system is distinct from all-width conjunctions, subcube partitions, primal partial-cube VC, and unrestricted linear-combination zero sets. The inspected references did not directly give simultaneous sharp VC threshold d=2k−2, maximal support orbit count, universal online ceiling k+1 and attained d>=2k−1 gap. Historical exact-width term VC/online results remain a priority risk.

## value

PASS

Natural finite incidence concept classes of fixed-dimensional cube faces present an explicit, sharp difference between static and sequential shattering; the maximal support classification and count are informative structure rather than a relabeling of broad conjunction VC bounds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
