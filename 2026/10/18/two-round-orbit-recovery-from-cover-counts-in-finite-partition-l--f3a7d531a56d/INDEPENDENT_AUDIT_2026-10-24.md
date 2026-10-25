# Independent mathematical audit

## correctness

PASS

The source RESULT.md is a complete all-n reconstruction. For a partition of block sizes s_i, outgoing degree C(k,2) recovers k and incoming degree F=sum_i(2^(s_i-1)-1) recovers a first-round signature. A merge of sizes a,b yields 2(F(Q)-F(P))-1=(2^a-1)(2^b-1). The proof distinguishes off-diagonal pairs by v_2(M-1)=min(a,b), diagonal pairs by v_2(M-1)=a+1 and a size bound excludes diagonal/off-diagonal collisions. The second-round multiset of outgoing first-round colours thus recovers all unordered block-size pairs; counting appearances of each size r and dividing by k-1 recovers its multiplicity. The k=1 case is unique. Symmetric-group relabelling proves equality exactly on orbits. For sharpness the distinct 14-element types (1,1,3,3,3,3) and (2,2,2,2,2,4) both have six blocks and F=12; adding singleton blocks preserves collision. The finite n<=13 threshold is checked by exhaustive integer partitions, not extrapolated to all n. The theorem does not identify the lattice among other structures.

## originality

PASS

Classical partition-type orbits and colour refinement are known separately, but the two-round directed-cover decoding and exact first-round boundary at n=14 are not stated or logically implied by the sources inspected. Best-of-knowledge PASS, with unindexed directed-lattice literature a genuine risk.

## value

PASS

The exact number of counting-refinement rounds needed to recover symmetry orbits of a natural classical finite lattice is a meaningful uniform structural invariant. The sharp n=14 boundary determines a real algorithmic separation, not a renamed Stirling-count formula.

The dated certificate retains the supplied scientific assessment, sources and limitations.
