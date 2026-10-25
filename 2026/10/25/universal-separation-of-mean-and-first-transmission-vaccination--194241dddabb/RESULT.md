# Universal separation of mean and first-transmission vaccination targets on paths

## Finding
Let \(P_n\) be the path with vertices \(1,\ldots,n\) in their natural order, where \(n\ge2\). Vaccinate exactly one vertex \(j\), remove it and its incident edges, choose an infection seed uniformly from the remaining \(n-1\) vertices, and retain each remaining edge independently with probability \(0<p<1\). Let \(X_j(p)\) be the number of vertices in the seed's retained-edge connected component, including the seed. Define \(M_j(p)=\mathbb E X_j(p)\) and \(R_j(p)=\Pr[X_j(p)\ge2]\).

For every \(0<p<1\), the complete optimizer sets are:

- If \(n=2\), both vertices minimize both objectives.
- If \(n=3\), the sole optimizer of both objectives is vertex \(2\).
- If \(n\ge4\), the minimizers of \(M_j(p)\) are the central vertex or central pair, \(\{\lfloor(n+1)/2\rfloor,\lceil(n+1)/2\rceil\}\), while the minimizers of \(R_j(p)\) are exactly \(\{2,n-1\}\).

Therefore \(P_5\) is the smallest path, and in fact the smallest **tree**, on which these two vaccination criteria have disjoint optimal-target sets. This difference holds for every transmissibility \(0<p<1\), not just at a sampled parameter value. It persists on every longer path.

On \(P_5\), center vaccination gives \((M_3,R_3)=(1+p,p)\), while vaccinating vertex \(2\) or \(4\) gives \((M_2,R_2)=(1+p+p^2/2,p-p^2/4)\). Thus paying an additional \(p^2/2\) expected infections reduces the probability of any secondary infection by \(p^2/4\).

## Assumptions and scope
The path is finite, undirected, unweighted and initially completely susceptible except for one perfectly vaccinated and removed vertex. After vaccination the infection source is uniform over the remaining vertices. Each residual edge is open independently with the same transmission probability; the final outbreak is the open cluster of the seed (a Reed–Frost/bond-percolation final-size formulation on a tree). No transmission into or through the vaccinated vertex is possible. The objectives are unconditional over source and edge outcomes; neither is normalized by the number of originally present vertices. Ties are included in optimizer sets.

## Proof
Write \(a=j-1\) and \(b=n-j\). Deleting vertex \(j\) leaves two paths of sizes \(a,b\), allowing an empty path. For a path component of size \(k\), two vertices at distance \(d\) are connected exactly when their unique \(d\) edges all transmit, an event of probability \(p^d\). Define
\[
F_p(k)=\sum_{d=1}^{k-1}(k-d)p^d\quad(k\ge0),
\]
with an empty sum equal to zero. Summing ordered seed–target pairs then gives
\[
M_j(p)=1+\frac{2}{n-1}\big(F_p(a)+F_p(b)\big).
\]
For every integer \(k\ge0\),
\[
F_p(k+1)-F_p(k)=\sum_{d=1}^{k}p^d.
\]
These increments are strictly increasing in \(k\) for \(p>0\). If \(a+1<b\), transferring one vertex from the longer component to the shorter strictly lowers the sum: \(F_p(a+1)+F_p(b-1)<F_p(a)+F_p(b)\). Iteration gives exactly the balanced sizes \(a,b\), differing by at most one; for \(n\ge3\) these are precisely the stated central vaccination vertices. When \(n=2\), both choices are equivalent.

For the second objective, the outbreak exceeds one vertex precisely when at least one open edge meets its seed. An endpoint of a nontrivial residual path has this probability \(p\); an internal vertex has probability \(1-(1-p)^2=2p-p^2\); an isolated vertex has probability zero. The sum of these probabilities over a component of size \(k\) is
\[
L_p(k)=\begin{cases}0,&k\le1,\\2p+(k-2)(2p-p^2),&k\ge2.\end{cases}
\]
Consequently \(R_j(p)=[L_p(a)+L_p(b)]/(n-1)\). For \(n\ge4\), vaccinating vertex \(2\) (or its reflection \(n-1\)) gives numerator \(L_p(n-2)\). Vaccinating an endpoint gives \(L_p(n-1)\), larger by \(2p-p^2>0\). If \(n\ge5\) and both remaining components have at least two vertices, their combined numerator is \(4p+(n-5)(2p-p^2)\), which exceeds \(L_p(n-2)=2p+(n-4)(2p-p^2)\) by exactly \(p^2>0\). These exhaust all possible vaccination locations; hence the second-nearest-to-endpoint positions are exactly the risk minimizers. For \(n=3\), removing vertex \(2\) leaves isolated seeds and uniquely gives \(R=0\). For \(n=2\), either choice leaves one vertex and no transmissible edges.

For \(n\le4\), every tree is a path or (at \(n=4\)) the three-leaf star. Path optimizer sets intersect by the preceding result; on the star, removing the center leaves only isolated vertices, so it uniquely minimizes both objectives for \(0<p<1\). Thus no smaller tree has disjoint minimizer sets, while \(P_5\) does. All assertions are exact for every stated \(n,p\).

## Verification
A standalone Python 3 checker enumerates every residual bond configuration and every source vertex using rational arithmetic, independently of the displayed path formulas. It confirms both objectives and their exact optimizers for every vaccination location on \(P_n\), \(2\le n\le10\), at \(p\in\{1/4,1/2,3/4\}\), totaling 162 vertex–parameter–order cases. The package includes the reproducible program (`verify.py`) and its output (`certificate.json`). At \(n=5,p=1/2\), the center has mean \(3/2\) and first-transmission risk \(1/2\), whereas an adjacent-to-endpoint choice has mean \(13/8\) and risk \(7/16\). These finite checks supplement, but do not replace, the proof for all \(n\) and \(p\).

## Relationship to prior work
Yuan et al. (2015) explicitly contrast vaccine allocations minimizing expected epidemic size with allocations that minimize the probability of exceeding a specified outbreak-size threshold. Their population-level stochastic SIR optimization involves two noninteracting populations, not vertex deletion in a homogeneous path nor an all-parameter characterization of the two optimal positions. Holme (2017) computes node-level vaccination importance on small connected graphs using expected outbreak size in a continuous-time SIR process, and compares that importance with influence maximization and sentinel surveillance; its other criteria are not the probability of at least one secondary infection. The present result isolates and proves a simple exact structural disagreement between the two disease-burden objectives under independently transmissible edges. The apparent absence of the path optimizer classification in inspected sources is not a proof of global novelty.

## Limitations
The all-size optimizer classification concerns only paths and one perfect vaccination with uniformly sampled residual infection source. The bond-percolation final-size law differs from general continuous-time SIR models with correlated outgoing transmissions, recovery-time variation or revisitation effects. The objective \(R\) counts any onward transmission, not a large epidemic or expected infected population. Heterogeneous probabilities, unequal source risks, weighted severity, correlated edges, multiple vaccines, and arbitrary graph structures are not covered. Independent bibliographic validation has not been undertaken.

## References
1. E. C. Yuan, D. L. Alderson, S. Stromberg and J. M. Carlson, “Optimal Vaccination in a Stochastic Epidemic Model of Two Non-Interacting Populations,” *PLOS ONE* **10** (2015), e0115826, first published 17 February 2015, https://doi.org/10.1371/journal.pone.0115826. Especially “Alternate Cost Functions.”
2. P. Holme, “Three faces of node importance in network epidemiology: Exact results for small graphs,” *Physical Review E* **96** (2017), 062305; arXiv:1708.06456, https://arxiv.org/abs/1708.06456. Especially §§II–III.
