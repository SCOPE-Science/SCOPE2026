# Sharp three-regime spectral-gap allocation for two cliques with a biclique gateway

## Finding

Fix integers \(k\ge2\), \(u\ge1\), set \(n=k+u\), and let \(B>0\). Take two disjoint copies of the complete graph \(K_n\). In each copy mark \(k\) gateway vertices, leaving \(u\) other vertices. Add **every** one of the \(k^2\) cross edges joining the two gateway sets, and no other cross edges. Assign arbitrary nonnegative undirected conductances to **all** graph edges, with total conductance \(B\). Let \(\lambda_2\) be the second-smallest eigenvalue of the resulting combinatorial weighted Laplacian.

Define
\[
 r=\frac{u}{k},\qquad \tau_k=\frac1{\sqrt{2(k+1)}},\qquad
 r_c(k)=\frac1{3+\sqrt{2(k+1)}+\sqrt{2/(k+1)}}.
\]
For \(0<r<1/6\) also define
\[
 t_-(r)=\frac{2r}{1-3r+\sqrt{1-6r+r^2}}.
\]
Set
\[
 t_*=
 \begin{cases}
 \frac12,&r\ge\frac16,\\[2pt]
 t_-(r),&r_c(k)\le r<\frac16,\\[2pt]
 \tau_k,&0<r<r_c(k).
 \end{cases}
\]
The formulas agree at the regime boundaries. For \(t>0\) let
\[
 H(t)=\frac12+r\left(t+\frac32+\frac1{2t}\right),\qquad
 F(t)=\frac n2+\frac{u}{2t}+2u(t+1)+(k-1)\max\{0,1-H(t)\}.
\]
**Theorem.** The exact unrestricted optimum is
\[
 \boxed{\max\lambda_2=\frac{B}{F(t_*)}.}
\]
A unique optimizer invariant under the natural gateway and nongateway permutations and exchange of the two cliques is obtained by putting \(\lambda_*=B/F(t_*)\) and giving every edge in each indicated class the following conductance:
\[
 \begin{array}{c|c}
 \text{edge class}&\text{conductance}\\ \hline
 \text{gateway--gateway within either clique}&
 a=\dfrac{\lambda_*}{k}\max\{0,1-H(t_*)\}\\[5pt]
 \text{nongateway--nongateway within either clique}&c=0\\[3pt]
 \text{gateway--nongateway within either clique}&d=\dfrac{\lambda_*(1+t_*)}{k}\\[5pt]
 \text{every cross-gateway edge}&b=\dfrac{\lambda_*[(n/k)(1+t_*)-1]}{2kt_*}.
 \end{array}
\]
Moreover, in **every** globally optimal allocation, even an asymmetric one, all nongateway--nongateway edges carry zero weight. If \(r\ge r_c(k)\), every optimum also assigns zero to all gateway--gateway edges within either clique. If \(0<r<r_c(k)\), every optimum assigns **positive total weight** to the latter edge class (not necessarily to each individual edge).

In the first regime the value simplifies to
\[
 \lambda_* = \frac{2B}{k+9u} \qquad(r\ge1/6).
\]
The three regimes really occur in the integer family: \((k,u)=(6,1)\) is on the first boundary, \((7,1)\) is in the middle regime, and \((8,1)\) is in the interior-gateway-edge regime.

## Assumptions and scope

The graph is a finite, simple, undirected, two-layer graph with two cliques of equal order and a **complete bipartite gateway** between the marked sets. The numbers \(k,u\) are positive integers as specified above; no distinguished cross matching is selected. Conductances may be zero. The budget counts each undirected edge once. The Laplacian is \(L=\sum_{\{i,j\}}w_{ij}(e_i-e_j)(e_i-e_j)^{\mathsf T}\), with no degree normalization. The optimization is over the full nonnegative edge-weight simplex, not merely over class-constant allocations. The claim concerns \(\lambda_2(L)\), not stochastic-matrix mixing or an effective-resistance objective.

## Proof

**1. Symmetry reduction is globally valid.** For fixed graph, \(\lambda_2(L)=\min_{x\perp\mathbf1,\|x\|=1}x^{\mathsf T}Lx\) is concave in the edge conductances. Averaging any feasible allocation over the graph automorphisms preserves the budget and cannot decrease \(\lambda_2\). Independent permutations of gateways and nongateways in each layer, together with interchange of layers, produce precisely the four edge classes \(a,c,d,b\) displayed above. Their edge counts, respectively, are \(k(k-1)\), \(u(u-1)\), \(2ku\), and \(k^2\), so the budget is
\[
 B=k(k-1)a+u(u-1)c+2ku d+k^2b.\tag{1}
\]
It suffices to optimize this four-parameter form and then transfer zero-class conclusions back to every allocation by nonnegative symmetry averaging.

**2. All spectral constraints.** Decompose the \(2n\)-dimensional vector space into constants on the two gateway and two nongateway sets, gateway-coordinate fluctuations (zero sum within each gateway set), and nongateway-coordinate fluctuations. The two constant-on-sets modes even under layer swap have eigenvalues \(0\) and \(nd\). The odd modes are represented in gateway/nongateway coordinates by
\[
 Q_- = \begin{pmatrix}ud+2kb&-ud\\-kd&kd\end{pmatrix}.
\]
Its eigenvalues \(\mu_-\le\mu_+\) obey
\[
 \mu^2-(nd+2kb)\mu+2k^2bd=0.\tag{2}
\]
Each gateway-fluctuation eigenvalue is \(ka+ud+kb\), with multiplicity \(2(k-1)\); each nongateway-fluctuation eigenvalue is \(kd+uc\), with multiplicity \(2(u-1)\), when \(u>1\). The dimensions exhaust \(2n\). For \(b,d>0\), substituting \(\mu=kd\) into the polynomial in (2) gives \(-kud^2<0\), so \(0<\mu_-<kd<nd\). Consequently,
\[
 \lambda_2=\min\{\mu_-,\ ka+ud+kb\},\tag{3}
\]
and \(c\) cannot improve \(\lambda_2\). Thus minimum budget for a positive prescribed gap always uses \(c=0\).

**3. Minimum budget for a prescribed gap.** Fix a target \(\lambda>0\). Feasibility of \(\mu_-\ge\lambda\) requires \(kd>\lambda\). Write \(kd=\lambda(1+t)\), \(t>0\). The lower bound on the cross weight from (2) is
\[
 b\ge b_0=\frac{\lambda[(n/k)(1+t)-1]}{2kt}.\tag{4}
\]
The gateway-fluctuation constraint is \(ka+ud+kb\ge\lambda\). Any excess \(b-b_0\) can be replaced by the same increase in \(a\), preserving this latter constraint while reducing the budget by \(k(b-b_0)\): cross weight is costlier per unit of gateway-fluctuation eigenvalue, since its multiplicity is \(k^2\) instead of \(k(k-1)\). Hence an optimal minimum-budget solution uses exactly \(b=b_0\), and then the minimum admissible gateway-interior weight is
\[
 a=\frac\lambda k \max\{0,1-H(t)\},\qquad
 H(t)=\frac{ud+kb_0}{\lambda}=\frac12+r\left(t+\frac32+\frac1{2t}\right).\tag{5}
\]
Combining (1), (4), and (5) gives **exactly**
\[
 B_{\min}(\lambda,t)=\lambda F(t),\qquad
 F(t)=\frac n2+\frac u{2t}+2u(t+1)+(k-1)(1-H(t))_+.\tag{6}
\]
The monotonicity argument in the replacement step proves no unexamined higher cross weight can improve this bound. Conversely, the displayed choices meet both spectral constraints and budget (6), so this lower bound is attainable. By homogeneity the desired optimum is \(B/\min_{t>0}F(t)\).

**4. Exact one-dimensional minimization.** Let \(F_0(t)=n/2+u/(2t)+2u(t+1)\). It has unique global minimizer \(t=1/2\). The map \(t\mapsto1/(2t)\) leaves \(H\) unchanged and satisfies
\[
 F(t)-F\left(\frac1{2t}\right)=u\left(t-\frac1{2t}\right).
\]
Thus any minimizer lies in \(0<t\le1/\sqrt2\). In this interval \(H\) is strictly decreasing. If \(r\ge1/6\), then \(H(1/2)=1/2+3r\ge1\). Therefore \(F(1/2)=F_0(1/2)\), the absolute lower bound, proving the first regime.

Suppose \(0<r<1/6\). Since \(H(1/2)<1\), the equation \(H(t)=1\) has a unique root \(t_-(r)\in(0,1/2)\). It is the smaller root of \(2rt^2+(3r-1)t+r=0\), giving precisely the formula above. On \((0,t_-]\), \(F=F_0\) and strictly decreases. On \([t_-,1/\sqrt2]\), the penalty is active and direct differentiation yields
\[
 F'(t)=u\left(1+\frac1k-\frac1{2kt^2}\right),\qquad
 F''(t)=\frac{u}{kt^3}>0.
\]
The stationary point is \(\tau_k\); hence the unique minimizing point is \(t_* =\max\{t_-(r),\tau_k\}\). The transition \(t_-=\tau_k\) is equivalent to \(H(\tau_k)=1\), namely \(r=r_c(k)\). This proves all three regimes, their endpoints, and the explicit optimal weights.

**5. Statements about all optimizers.** The scalar function has a unique minimum in every regime, so the symmetry-invariant optimizer is unique. Every arbitrary optimizer averages to that optimizer, by step 1. Nonnegative weights cannot average to zero on an edge orbit unless all original weights on that orbit are zero. This proves the universal zero-edge conclusions. When \(r<r_c(k)\), the unique average has \(a>0\); thus every original optimum must have positive **aggregate** weight on the gateway-interior edge orbit. This does not assert that every gateway-interior edge is positive under arbitrary asymmetric optimization. \(\square\)

## Verification

Run `python3 VERIFY.py` with NumPy and SymPy available. The included output `verification_output.txt` records 189 full-matrix eigenvalue/budget comparisons (all \(3\le n\le20\), \(2\le k<n\), plus one harmless \(k=1\) baseline), 2,430 randomly generated asymmetric allocations, a symbolic reduced characteristic-polynomial identity, and exact symbolic scalar derivative/involution identities. The recorded numerical comparisons have explicit tolerances in the script. Their purpose is to check assembly and formulas, not to prove the infinite family.

A diagnostic comparison illustrates why the full biclique is not merely a renamed matching: at \((k,u)=(5,2)\), \(B=1\), the biclique-gateway optimum is exactly \(2/23\), whereas the matching-bridge graph with the same marked sets has optimum approximately \(0.0769326244\). The latter uses positive within-gateway clique weights; the biclique optimum uses none. This diagnostic is not needed for the proof.

## Relationship to prior work

Ghosh and Boyd (2006) provide the general Laplacian-convexity and symmetry framework, including upper bounds for graphs constrained by cuts. This framework justifies symmetry reduction but does not state the biclique-gateway edge-budget formula or its three support regimes.

Shakeri, Albin, Darabi Sahneh, Poggi-Corradini, and Scoglio (2015 preprint) optimize one-to-one interlayer link weights while the individual layer Laplacians are fixed. Tavasoli, Shakeri, Ardjmand, and Rahman (2024) extend interconnection design to general admissible interlinks, including \(k\)-to-\(k\) couplings, but their layer-edge weights are still fixed in the optimization. Their results therefore do not imply a joint intra-/interlayer total-budget allocation or the present forced deletion of particular intralayer edge orbits. In particular, a fixed-intralayer formulation cannot be directly substituted into (1), where every within-layer weight is a variable paid from the same budget.

The corresponding **matching**-gateway problem is a different graph: a matching has only \(k\) cross edges, while this graph has \(k^2\). Its gateway fluctuation eigenvalues and optimal support differ. The present claim is not a corollary of the matching-gateway case; the explicit \((k,u)=(5,2)\) comparison shows strict improvement in the optimized value under biclique completion.

## Limitations

The claim requires two equal-size cliques and a complete bipartite cross-gateway on equally many marked vertices. It does not classify partial cross bicliques, unequal clique sizes, directed weights, degree-normalized Laplacians, stochastic-matrix fastest mixing, or all asymmetric optimizers. The structural assertions concerning arbitrary optima specify which orbits must carry zero or positive **total** weight, not a full parameterization of nonsymmetric solutions. Broad graph-theoretic or optimal-design literature not indexed in the examined searches may contain an equivalent result; independent assessment has not been performed.

## References

1. A. Ghosh and S. Boyd, *Upper bounds on algebraic connectivity via convex optimization*, Linear Algebra and its Applications **418** (2006), 693–707, DOI `10.1016/j.laa.2006.03.006`. Available online 5 May 2006. Full PDF: https://web.stanford.edu/~boyd/papers/pdf/eigbounds_laplacian.pdf.
2. H. Shakeri, N. Albin, F. Darabi Sahneh, P. Poggi-Corradini, and C. Scoglio, *Maximizing Algebraic Connectivity in Interconnected Networks*, arXiv:`1510.06785v1`, first posted 22 October 2015. https://arxiv.org/html/1510.06785v1.
3. A. Tavasoli, H. Shakeri, E. Ardjmand, and S. Rahman, *The art of interconnections: Achieving maximum algebraic connectivity in multilayer networks*, Network Science **12** (2024), 261–288, DOI `10.1017/nws.2024.9`, open article: https://www.cambridge.org/core/journals/network-science/article/art-of-interconnections-achieving-maximum-algebraic-connectivity-in-multilayer-networks/67B428A634B2BF0741AFD0B350F8AB4E.
