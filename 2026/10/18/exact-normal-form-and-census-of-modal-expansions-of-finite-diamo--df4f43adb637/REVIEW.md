# Independent mathematical audit

## correctness

PASS

For z=Box(0), t=Diamond(0), the Dunn test at x=1 gives Box≤Diamond; together with monotonicity and top preservation, only cross-tests on distinct atoms are left. A meet map with z=1 is constant; with atomic z at most one atom can map to 1 and the rest map to z; with z=0 the nonzero images are an injective partial assignment of atoms, or one image 1 and the rest 0. For (z,t)=(1,1), (atomic,≥z), (0,1), (0,atomic), (0,0), the contributions are respectively 1, n(2n+1+2^n), P_n+n, n[(n+1)2^n+n²(n−1)+n], and (n+2)^n+2n^(n+1)+Q_n+n. In (0,atomic t), at most one exceptional Box image outside {0,t} is possible, and it forces all other Diamond atom-values to t; counting the optional extra image t gives the n²(n−1) term per t. With both bottoms zero, two or more active atomic images preclude top at an active Diamond value; inactive Diamond values may be zero or an unused atom, which gives Q_n. Rank one and the unique top-image cases have the separately stated counts. Thus the cases exhaust all maps without double counting. Re-evaluating the sums gives 574, 5054, 70834 and 1332432. Independent exhaustive Python 3 replay: /workspace/branches/6cdb05a3-2239-47e5-9be2-ac8dcf3d9a75/independent_check.py 3 (or 4). It checks all top-preserving maps against the defining tests and explicitly counts fixed pairs under conjugation. For n=3 the counts by cycle type (1³),(2,1),(3) are 574,52,13; for n=4 the counts for (1⁴),(2,1²),(2²),(3,1),(4) are 5054,316,86,62,16. Burnside gives 126 and 325. The uploaded script was inspected, not run. Only n=3,4 are exhaustively computed and only these have a claimed orbit count; the all-n case argument is necessary for the labelled formula.

## originality

PASS

The distinct contribution is the complete normal form and exact census of the fixed diamond carriers for the specified pair of operations. Existing axiomatics and duality are credited. Related indexed censuses on the same carrier use different operations or impose different axioms, and the closely matching Dunn census uses chains. This is a bounded comparison and not an exhaustive priority conclusion.

## value

PASS

The diamonds are a canonical first nondistributive test family for modal lattices. The complete classification explains how interaction constraints depend on the two bottom images, gives exact labelled counts for all widths, and supplies small isomorphism censuses useful for finite-model comparisons or verifier benchmarks. The contribution is not an isolated small instance or a new name for the known duality.

The dated certificate retains the supplied scientific assessment, sources and limitations.
