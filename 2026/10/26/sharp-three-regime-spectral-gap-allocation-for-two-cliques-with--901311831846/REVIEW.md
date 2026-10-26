# Scientific review: biclique-gateway spectral-gap allocation

## Correctness — PASS

The claim concerns the unrestricted simplex of nonnegative conductances with total \(B>0\) on two \(K_{k+u}\) layers connected by all \(k^2\) edges between their \(k\)-vertex gateway sets. Concavity of the Rayleigh minimum makes averaging over graph automorphisms legitimate, not a restriction of the optimization problem. The graph's four invariant subspaces give the full Laplacian spectrum. In particular the smaller odd equitable eigenvalue lies strictly below the nongateway fluctuation eigenvalue, making all nongateway--nongateway weights expendable. A prescribed target \(\lambda>0\) yields an exact minimum-budget expression \(\lambda F(t)\), including the comparison showing that any excess cross-edge weight is more expensive than a compensating within-gateway weight. The involution \(t\mapsto1/(2t)\) and the strictly convex active branch establish the global, three-regime scalar optimum. For each orbit assigned zero by the invariant optimizer, averaging and nonnegativity force zero conductance in every unrestricted optimizer. These steps are proved in RESULT.md, not inferred from sampling.

The supplied verification script reproduced the theorem on 189 complete finite graph instances and compared against 2,430 genuinely asymmetric feasible samples; symbolic identities separately checked the quotient characteristic polynomial, stationary equation, and involution. The tests substantiate implementation but are not substitutes for the all-parameter proof. No external or independent validation has been performed.

## Originality — PASS, with residual risk

Relevant published literature was compared by implication rather than by title. Ghosh and Boyd (2006), *Upper bounds on algebraic connectivity via convex optimization*, prove a general symmetry/convexity device and work out cut and block bounds, but do not give this exact biclique-gateway budget allocation or the two intralayer edge-support thresholds. Shakeri and coauthors (2015 preprint, arXiv:1510.06785v1) consider one-to-one interlayer links with **fixed** layer Laplacians. Tavasoli and coauthors (2024, DOI 10.1017/nws.2024.9) allow general interconnection patterns, including \(k\)-to-\(k\), but their problem likewise optimizes **only interlayer weights**, not every edge from a single global budget. Their results therefore do not determine the co-optimized intralayer class weights here.

A directly related matching-gateway problem has only \(k\) cross edges rather than \(k^2\). It is not equivalent by parameter substitution: for \((k,u)=(5,2)\) at unit budget, the present optimum equals \(2/23\), strictly above the matching-gateway optimum \(0.0769326244\ldots\); the within-gateway support also differs. Published-source searches for all-to-all gateway clique networks, possible stronger graph-design theorems, and exact formula aliases yielded no directly covering result. Absence from a finite search is not proof of global novelty; an unindexed specialized classification remains a residual risk.

## Mathematical value — PASS

This is a natural two-community diffusion/consensus design problem in which all intracommunity and cross-community connections compete for one fixed resource. The solution gives a **complete infinite-family exact resource allocation**, not just a numerical maximum. The two structural thresholds distinguish (i) a simple \(2B/(k+9u)\) regime, (ii) an active equitable constraint with gateway-interior edges still eliminated, and (iii) a regime where every optimum must invest some weight in gateway-interior edges. The forced-zero property for every asymmetric optimum and the non-equivalence to matching gateways are practically interpretable consequences. These are not arbitrary finite slices or textbook plug-in eigenvalues.

## Closest literature and scientific limits

The relevant primary full-text materials are Ghosh and Boyd (2006), DOI `10.1016/j.laa.2006.03.006`; Shakeri et al. (2015), `arXiv:1510.06785v1` including its supplemental material; and Tavasoli et al. (2024), DOI `10.1017/nws.2024.9` including its mathematical appendices. The first supplies the broad optimization framework; the latter two supply multilayer-network comparisons with intralayer structures held fixed. No assertion of exhaustive coverage of every unpublished or unindexed source is made.

The theorem does not treat unequal clique sizes, partial cross bicliques, row-stochastic fastest-mixing constraints, or a complete classification of nonsymmetric optimal weights. The support law for the high-gateway regime concerns positive **total** within-gateway weight, not positivity of every such edge.

Self-review: passed. Independent audit: not yet performed.
