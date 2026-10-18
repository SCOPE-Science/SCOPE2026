# Independent mathematical audit

## correctness

PASS

Every monotone 0–1 game corresponds to an antichain of minimal winning coalitions. Independently enumerated and filtered proper antichains for n=1,2,3,4, obtaining labeled counts (1,3,11,80) and class counts (1,2,5,14). Independently computed exact pivotal Shapley coordinates for the three claimed divergent representatives and solved first least-core linear programs using SciPy: {AB,AC} has phi=(2/3,1/6,1/6,0), unique veto A and nucleolus=(1,0,0,0); {AB,AC,BCD} has phi=(5/12,1/4,1/4,1/12), unique least-core x=(1/3,1/3,1/3,0) from three equal excesses; {AB,ACD} has phi=(7/12,1/4,1/12,1/12), unique veto A and nucleolus=(1,0,0,0). Inspected complete package exact-rational script: its exhaustive 14-class nucleolus table is certified by veto/core, tight LP vertices and symmetry in exceptional nonsingleton class (3,13,14), yielding 36 labeled divergences in three size-12 orbits and 24 nondummy divergences. SciPy LP was numerical corroboration, not a replacement for source exact rational certificates.

## originality

PASS

Classical Shapley and nucleolus and algorithms for weighted games are known; the new scope is complete weak player-ranking discordance over all proper simple games through four players, not comparison of raw indices, unrelated power indices, or general cooperative games.

## value

PASS

Properness, minimal number of players, weak ranking and dummy-free distinction are natural voting-theoretic constraints. Exact 36/80 and three orbit types identify the entire earliest ordinal fairness disagreement, an independently useful benchmark for comparing allocation concepts.

The dated certificate retains the supplied scientific assessment, sources and limitations.
