# Independent mathematical audit

## correctness

PASS

For clique phase 2 and path word 2^a0 1^b (a>=1,b>=0,n=a+b+1), the source supplies explicit states at 3k,3k+1,3k+2 and the final three-step release. Each transition is checked against open-neighborhood inhibition only when the vertex is color 2 and a neighbor has color 1; clique vertices are held at 2 by the current path blink when the front moves. At time 3b the final 2^(n−1)0 path releases through (0|0^(n−1)1) and (1|1^(n−1)2), reaching (2|2^n) first at 3(b+1)=3(n−a); all prior states visibly use multiple colors. Independent literal vertex-neighbor simulation checked 456 trajectories and 8,712 consecutive graph updates for r=1,2,5,n=3..18 and all a. Removing the whole clique and one internal path vertex, while every cut of size<=r leaves graph connected, gives κ=r+1; path Laplacian orthogonal modes give λ2=r+2−2cos(π/n), all other clique/transverse modes N=r+n. Missing edges (n−1)(n−2)/2 show density→1 for r=n², and delay 3(n−1) grows Θ(√N). These are special initial states, not universal convergence or sharp maximum for every coloring.

## originality

PASS

Lyu introduced the same three-state inhibitory firefly rule and gave path/tree synchronization bounds. Those prior theorems do not transfer to a clique joined to every path vertex because the update of each path and clique vertex changes; the exact traveling-front invariant under those extra edges is separately proved here. Published nearest star/split/bridged-clique examples have different adjacency and bounded conditional delays. Only primary abstract/relevant theorem description was accessible in this run, so an unindexed dense graph construction remains a nonzero priority risk.

## value

PASS

The graph family is canonical (clique join path) and simultaneously has diameter two and connectivity/edge density nearly maximal. The explicit slow yet eventually synchronizing fronts disprove a plausible bound based solely on those bulk connectivity proxies for synchronizing trajectories. It is a motivated boundary counterexample with a transparent exact induction rather than an unmotivated long simulation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
