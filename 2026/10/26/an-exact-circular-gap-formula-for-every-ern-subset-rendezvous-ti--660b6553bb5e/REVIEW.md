# Independent mathematical audit

## correctness

PASS

PASS. The compressed block ba^{n-1} applies max(j-1,0) to representatives. After rotating a chosen occupied x to 0, n-g(x)-1 blocks reduce all images into {0,1}, and final b merges them. The lower bound uses F(T)=n(n-1)+1-max_{x in T}(n g_T(x)-r(x)); under a all nonwrapping scores increase only by one, under b moving 0 or deleting it when 1 exists adds at most one, and the only nonsingleton-to-singleton transition {0,1}-> {1} has F=1. Thus each letter reduces F by at most one. Independent exhaustive reverse-BFS checked all 8177 nonempty subsets across n=2..12; finite check corroborative, all-n proof is potential.

## originality

PASS

PASS, qualified. The best related source Behague–Johnson defines individual k-set synchronizing times but concentrates on size-wise extrema, not a closed labeled-subset distance for every size and n. Previously known full-state reset and some pair distances are included but are not claimed new. Cardoso 2014 doctoral thesis is a relevant uninspected full text that might state the exact formula or an equivalent potential.

## value

PASS

PASS. The prescribed-initial-subset reset time is a fundamental natural synchronization invariant. A closed exact all-subset min-over-circular-gaps formula and optimal word eliminate exponential shortest-path search for the classical extremal family, and the 1-Lipschitz potential is a reusable structural certificate beyond known full-set or pair-only numbers.

The dated certificate retains the supplied scientific assessment, sources and limitations.
