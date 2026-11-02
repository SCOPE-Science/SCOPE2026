# Exact cascade reliability and sharp seed counts on a two-rail social network

## Finding

For each integer \(n\geq2\), place \(2n\) agents on a two-rail network \(L_n=P_n\mathbin{\square}K_2\), where adjacent agents on the same rail and opposite agents on the same rung are linked. An initial set of agents adopts irreversibly, and every other agent subsequently adopts as soon as at least two neighbors have adopted. Call an initial set *successful* if eventual adoption is universal. Define the polynomial
\[
Q_n(y)=\sum_{A\subseteq V(L_n):\ A\text{ successful}}y^{2n-|A|}.
\]
The exact size-resolved cascade generating function is
\[
\boxed{\sum_{n\geq1}Q_n(y)z^n
 =\frac{z\bigl(1+(y+2y^2)z\bigr)}
 {\bigl(1-yz-2y^3z^2\bigr)
  \bigl(1-(1+2y)z-(y^2+2y^3)z^2\bigr)}.}
\]
The auxiliary \(n=1\) term is \(Q_1(y)=1\); all substantive statements concern \(n\geq2\). Consequently, under independent initial adoption probability \(p\in(0,1]\), the exact universal-adoption probability is \(p^{2n}Q_n((1-p)/p)\).

The smallest successful seed set has \(k+1\) agents for \(n=2k\) (\(k\geq1\)), and \(k+2\) agents for \(n=2k+1\) (\(k\geq1\)). The numbers of successful sets attaining these minima are, respectively,
\[
\boxed{\begin{cases}k2^k,&n=2k,\\2^{k-1}(k+1)(3k+2),&n=2k+1.\end{cases}}
\]
The total number of successful initial sets satisfies the sharp asymptotic
\[
\boxed{Q_n(1)\sim\frac{\sqrt{21}}7
 \left(\frac{3+\sqrt{21}}2\right)^n.}
\]
In particular, for uniformly chosen initial subsets, the success probability is asymptotic to \(\frac{\sqrt{21}}7((3+\sqrt{21})/8)^n\), which decays exponentially in \(n\). These are mathematical properties of the specified deterministic social-transmission model, not estimates of empirical adoption.

## Assumptions and scope

Each network is a finite simple graph with vertices \((j,r)\), where \(1\leq j\leq n\) and \(r\in\{0,1\}\). An edge joins \((j,0)\) to \((j,1)\) and joins \((j,r)\) to \((j+1,r)\) whenever both are defined. Adoption is permanent, simultaneous update rounds are used, and the activation threshold is *two neighbors*, independent of node degree. All subsets of the labeled vertices count separately. Endpoint vertices have degree two; other vertices have degree three. No random contact, memory decay, heterogeneity, or threshold proportional to degree is assumed. The symbolic variables \(z\) and \(y\) are formal generating-function indeterminates.

## Proof

**1. Exact obstruction characterization.** Let \(W\) be the complement of the initial adopters. Adoption fails precisely when \(W\) contains a nonempty subgraph \(S\) in which every vertex has at least \(\deg_{L_n}(v)-1\) neighbors in \(S\): this is the set of nonadopters at the eventual fixed point, and conversely any such set remains inactive forever. Thus an interior vertex of \(S\) needs two neighbors in \(S\), whereas a vertex at either end rung needs one. If a connected component of \(S\) contains a cycle, it contains a full pair of adjacent rungs: any cycle in the two-rail ladder traverses both rails between two distinct rungs and therefore contains the four vertices in two neighboring rungs. If the component is acyclic, it is a finite tree whose vertices in interior rungs have degree at least two within the component, so all leaves lie on the two end rungs. At least two leaves exist. If they lie on the same end rung, both end-rung vertices are in \(W\); if on opposite end rungs, \(W\) contains a path joining those rungs. Conversely, each of these three patterns contains a stable nonadopter set: a fully vacant end rung, a fully vacant adjacent pair of rungs, or a vacant path joining both ends. Hence a set succeeds exactly when its vacant complement avoids all three patterns.

**2. Finite-state transfer.** Encode the vacancies on a rung by a bit mask \(v\in\{0,1,2,3\}\), with bit 1 or 2 representing the vacant vertex on a particular rail. Track whether these vacancies connect through vacant vertices to the left end rung. Since a vacant rung's two vertices are adjacent, the reachability mask \(r\) is either \(0\) or \(v\). The only necessary states, ordered as written, are
\[
(0,0),(1,0),(1,1),(2,0),(2,2),(3,0),(3,3).
\]
Initial weights for the first rung form \(\mathbf i=(1,0,y,0,y,0,0)\); the full first rung is excluded. From \((v,r)\) to the next rung mask \(w\), exclude \(v=w=3\) (a permanently vacant adjacent-rung square), and set \(r'=w\) if \(r\mathbin{\&}w\neq0\), otherwise \(r'=0\). The transition has weight \(y^{\operatorname{popcount}(w)}\). Here \(\mathbin{\&}\) is bitwise intersection. The last-rung terminal vector is \(\mathbf f=(1,1,0,1,0,0,0)^{\mathsf T}\): accept only a non-full rung without a vacant path from the first rung. If \(M(y)\) is the \(7\)-by-\(7\) transition matrix so defined, the obstruction characterization proves the exact identity
\[
\sum_{n\geq1}Q_n(y)z^n
 =z\mathbf i\bigl(I-zM(y)\bigr)^{-1}\mathbf f.
\]
Exact rational matrix elimination simplifies the right side to the factored expression in the finding. The complete matrix is generated directly by the standalone checker using the seven listed states and transitions; no omitted state or external data is required.

**3. Sharp minimum seed counts.** For \(n=2k\), the maximum power of \(y\) in \(Q_n(y)\) is \(3k-1\); for \(n=2k+1\), it is \(3k\). To obtain both claims and their leading coefficients simultaneously, substitute \(y=\epsilon^{-2}\), \(z=t\epsilon^3\) in the exact generating function and expand about \(\epsilon=0\):
\[
\sum_{n\geq1}Q_n(\epsilon^{-2})t^n\epsilon^{3n}
 =\epsilon^2\frac{2t^2}{(1-2t^2)^2}
 +\epsilon^3\frac{t(1+4t^2)}{(1-2t^2)^3}
 +O(\epsilon^4).
\]
This identity is understood coefficientwise in \(t\); the even and odd powers have the stated first nonzero \(\epsilon\)-orders. Indeed, the \(\epsilon^2t^{2k}\) coefficient is \(k2^k\), and the \(\epsilon^3t^{2k+1}\) coefficient is \(2^{k-1}(k+1)(3k+2)\). The transformation makes the corresponding maximal vacant-set sizes and hence the minimum seed counts immediate. Their coefficients are strictly positive, establishing attainability as well as necessity for every integer \(k\geq1\).

**4. Total-count asymptotics.** At \(y=1\), the exact generating function reduces to
\[
F(z)=\frac{z(1+3z)}{(1+z)(1-2z)(1-3z-3z^2)}.
\]
Its unique smallest-modulus pole is \(\rho=(\sqrt{21}-3)/6=2/(3+\sqrt{21})\), and the coefficient of \((1-z/\rho)^{-1}\) in its partial fractions is exactly \(\sqrt{21}/7\). All other poles have strictly greater modulus. Coefficient extraction therefore gives \(Q_n(1)\sim(\sqrt{21}/7)\rho^{-n}\), proving the asymptotic. Dividing by \(2^{2n}\) gives the uniform-initial-subsets probability.

## Verification

Run `python artifacts/check.py` with Python 3.9 or newer and SymPy installed. The checker independently simulates all \(349{,}520\) initial configurations over \(n=2,\ldots,9\), compares each fixed point with the obstruction test, and checks every coefficient against a separately implemented state-transfer recurrence. The successful-set totals for \(n=2,\ldots,9\) are \(7,30,125,491,1902,7285,27775,105606\). Exact symbolic inversion verifies the entire two-variable rational resolvent identity over \(\mathbb Q(y,z)\), not merely at sampled points; exact finite checks verify the minimum seeds and their multiplicities through \(n=25\), and exact pole algebra checks the asymptotic leading factor. These computations complement the mathematical arguments; finite enumeration alone does not prove the infinite-family statements.

## Relationship to prior work

Wang, Tang, Zhang and Lai (2015) analyze non-redundant social contagion with behavioral thresholds on large networks, motivating the irreversible adoption interpretation. Marcilon and Sampaio (2015) analyze two-neighbor bootstrap percolation on grid graphs and the maximum time to universal activation, not the seed-size reliability polynomial on fixed-width ladder graphs. Balogh and Pittel (2007) analyze random regular graphs and initial-infection phase transitions, not exact finite ladder enumeration. The present claim is the exact simultaneous census of all successful seed-set sizes, the sharp multiplicities at the minimal seed budgets, and the explicit asymptotic for the two-rail family. General transfer-matrix computability does not itself imply this closed rational form or its consequences. These comparisons are not an assertion that no earlier equivalent counting result exists.

## Limitations

The result applies only to the labeled, unweighted two-rail ladder and absolute two-neighbor irreversible adoption. It does not cover other network widths, heterogeneous or fractional thresholds, adaptive contacts, stochastic repeated exposures, or socially realistic individual behavior. An older unlocated equivalent enumeration or an uninspected broad theorem could reduce the originality claim; historical priority has not been independently certified. Independent mathematical validation has not been performed.

## References

1. W. Wang, M. Tang, H.-F. Zhang and Y.-C. Lai, *Dynamics of social contagions with memory of non-redundant information*, arXiv:1507.04062, first public 2015-07-15. https://arxiv.org/abs/1507.04062
2. T. B. Marcilon and R. M. Sampaio, *The maximum time of 2-neighbour bootstrap percolation in grid graphs and some parameterized results*, arXiv:1508.06847, first public 2015-08-27. https://arxiv.org/abs/1508.06847
3. J. Balogh and B. G. Pittel, *Bootstrap percolation on the random regular graph*, Random Structures & Algorithms 30 (2007), 257–286. https://doi.org/10.1002/rsa.20158
