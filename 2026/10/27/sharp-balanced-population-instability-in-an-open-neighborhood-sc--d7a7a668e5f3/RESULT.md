# Sharp balanced-population instability in an open-neighborhood Schelling swap game

## Finding
Fix an integer \(n\ge2\) and two classes of \(n\) vertices joined by every cross edge, so the interaction graph is \(K_{n,n}\). Fill all \(2n\) positions with exactly \(b\) red agents and \(2n-b\) blue agents, where \(1\le b\le2n-1\). Each agent prefers a one-half proportion of its own color among its **open** neighbors. Suppose the common payoff is any function \(p:[0,1]\to\mathbb R\) satisfying \(p(s)=p(1-s)\) and strictly decreasing with \(|s-1/2|\). Two agents exchange positions only if both strictly gain.

Let \(k\) be the number of red agents in the first class. Then every placement is a pure swap equilibrium whenever \(b\ne n\). At the exactly balanced population \(b=n\), a placement is a pure swap equilibrium **if and only if**
\[\left|k-\frac n2\right|\le\frac12.\]
Consequently, the number of equilibrium red-vertex subsets (not distinguishing individual agents of the same color) is
\[E(n,b)=\begin{cases}\binom{2n}{b},&b\ne n,\\\binom{n}{n/2}^2,&b=n\text{ and }n\text{ even},\\2\binom{n}{(n-1)/2}^2,&b=n\text{ and }n\text{ odd}.\end{cases}\]
In particular, changing the red population from \(n-1\) to \(n\) changes the stable fraction of placements from \(1\) to \(\Theta(n^{-1/2})\); changing from \(n\) to \(n+1\) restores it to \(1\). The balanced fractions are asymptotically \(2/\sqrt{\pi n}\) for even \(n\) and \(4/\sqrt{\pi n}\) for odd \(n\).

## Assumptions and scope
The network has all \(n^2\) cross-class edges and no within-class edges. Neighborhoods explicitly exclude the agent herself. Payoffs depend only on same-color **open-neighbor** fractions and are strictly ordered by distance from \(1/2\), so the conclusion holds for all utility functions specified above, not only piecewise-linear ones. Individual red agents are interchangeable for equilibrium counting, and likewise blue agents. Swaps require two strict individual gains, including when the exchanged positions are adjacent. There are no vacancies, distance costs, conformity rewards, or private preferences. The count is over labeled vertices with unlabeled same-color agent identities.

## Proof
Write \(A,B\) for the two classes, \(k=|A\cap R|\), \(h=|B\cap R|=b-k\). A swap of identical colors changes no coloring and is never strictly beneficial. An opposite-color swap *within* one class leaves the opposite class unchanged; both agents face the same open-neighbor composition before and after moving, and neither gains.

Consider a red agent at \(A\) and a blue agent at \(B\); this direction is feasible only when \(k\ge1\) and \(h\le n-1\). Before exchanging, the red's own-color fraction is \(h/n\) and the blue's is \((n-k)/n\). After exchanging, the red at \(B\) sees fraction \((k-1)/n\), and the blue at \(A\) sees \((n-h-1)/n\). Using the symmetry of \(p\) and strict distance ordering, the two strict improvements are equivalent to
\[|2(k-1)-n|<|2h-n|,\qquad |2(h+1)-n|<|2k-n|.\]
Squaring and factoring yields
\[(k-h-1)(b-n-1)<0,\qquad (k-h-1)(b-n+1)>0.\]
Because \(b-n\) is an integer, both inequalities hold exactly when \(b=n\) and \(k-h>1\), equivalently \(2k-n>1\). By color-class interchange, swapping a red agent at \(B\) with a blue at \(A\) is profitable exactly when \(b=n\) and \(2h-n>1\), equivalently \(2k-n<-1\). Whenever either inequality holds at \(b=n\), feasibility is automatic: \(2k-n>1\) implies \(k\ge1\) and \(h=n-k<n\); similarly for the reverse direction. Thus there is no profitable swap if \(b\ne n\); for \(b=n\), stability holds exactly when \(-1\le2k-n\le1\). This is the asserted structural classification.

For each permissible \(k\), there are \(\binom nk\binom n{b-k}\) colorings. If \(b\ne n\), all count by Vandermonde's identity to \(\binom{2n}{b}\). At \(b=n\), only the one central value of \(k\) when \(n\) is even, or the two adjacent central values when \(n\) is odd, contribute. This proves the exact formulas. Divide by \(\binom{2n}{n}\) and apply Stirling's asymptotic \(\binom{2m}{m}\sim4^m/\sqrt{\pi m}\) to obtain the parity-specific fractions. Every step is valid at \(n=2\) and the population endpoints \(b=1,2n-1\).

## Verification
The accompanying `verify.py` independently evaluates both participants' utilities **after moving to the opposite vertex** (not the utilities of their former vertices) for every opposite-color pair in every two-color placement on \(K_{n,n}\) for \(2\le n\le6\), and compares results with the theorem's equilibrium membership condition and exact counts. The checker uses exact integer distances to one-half and asserts every comparison. Its finite enumeration supports, but does not replace, the all-\(n\) factorization proof above.

## Relationship to prior work
Agarwal–Elkind–Gan–Voudouris, *Swap Stability in Schelling Games on Graphs* (arXiv:1909.02421, publicly posted 2019-09-05), develop swap games with **open-neighbor** fractions but monotone own-type preferences, not this symmetric middle-peaked payoff. Bilò–Bilò–Lenzner–Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games* (arXiv:2204.12599, publicly posted 2022-04-26), introduce symmetric single-peaked preferences but define the fraction on **closed** neighborhoods (including oneself); their general swap identity and their broader existence/welfare theorems do not instantiate this different open-neighbor game. The present result isolates how removing self-counting changes strict two-sided swap incentives, yielding an exact combinatorial equilibrium census and a discontinuity at precisely equal color populations. No priority or novelty is claimed for the pre-existing swap model, the complete bipartite graph, the symmetric payoff function, or central-binomial asymptotics; the stated equilibrium phase diagram is the contribution.

## Limitations
The classification is not for closed-neighbor single-peaked games, arbitrary bipartite graphs, three or more colors, unequal bipartition sizes, vacancies, or weakly profitable swaps. The strictly decreasing-on-distance hypothesis matters: plateaus can add equilibria. Mathematical correctness is proved by direct algebra, but originality is assessed against inspected accessible references and search results, not certified by an exhaustive survey. A separately performed independent audit does not yet exist.

## References
1. A. Agarwal, E. Elkind, J. Gan, A. A. Voudouris, *Swap Stability in Schelling Games on Graphs*, arXiv:1909.02421 (initial release 2019-09-05), https://arxiv.org/abs/1909.02421.
2. D. Bilò, V. Bilò, P. Lenzner, L. Molitor, *Tolerance is Necessary for Stability: Single-Peaked Swap Schelling Games*, arXiv:2204.12599 (initial release 2022-04-26), https://arxiv.org/abs/2204.12599.
