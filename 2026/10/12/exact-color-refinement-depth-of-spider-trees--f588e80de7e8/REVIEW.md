# Independent mathematical audit

## correctness

PASS

For d>=3 center is unique degree d; round1 splits center, degree1 leaves and degree2 interiors. At radius r>=1 the refinement partition is determined by clipped distance to both ends of each arm: a leaf (leaf,min(L,r)), internal (internal,min(x,r),min(L-x,r)). Induction follows unique oriented neighbors toward center and leaf once boundary types separate. Within longest leg the unresolved middle interval disappears at r=ceil(Lmax/2); among different lengths the last leaf-class distinction occurs at r=L_second_distinct+1, while internal cross-length pairs separate at most one round earlier. Thus the max formula holds for all multisets and multiplicities. For fixed N,d, total arm length N-1 bounds Lmax<=N-d and 2S+1<=N-d, and constructive arm multisets attain floor((N-d)/2)+1; n=d+1 star boundary checked. Independent genuine 1-WL partition simulation for 182 spider lengths (d=3,4, each length<=6) matched formulas. General induction not derived from finite enumeration.

## originality

PASS

Published Krebs–Verbitsky 2014 full PDF develops color refinement and universal-cover lower bounds on general graph families, no spider/starlike/specific arm-length formula. Related Resultary spider results are for Ricci flow, curvature, power domination, etc., not color refinement. Prior almost-equilateral spider special case cannot imply arbitrary distinct arm lengths with two-statistic collapse; best-of-knowledge new exact classification plus fixed-order extremal theorem.

## value

PASS

Ordinary 1-WL stabilization is a central finite-graph invariant; spiders are natural trees with one branching vertex. The formula explains how longest and second-largest distinct legs—not all leg multiplicities—govern exact depth, and maximizes it sharply at fixed order, a reusable canonical family benchmark beyond ad hoc tiny instances.

The dated certificate retains the supplied scientific assessment, sources and limitations.
