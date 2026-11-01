# Universal two-cycle orbit asymptotics under bounded-degree bipartite edge deletion

## Finding
Fix an integer \(R\ge0\). For every integer \(n>2R\), take any bipartite graph \(H_n\subseteq K_{n,n}\) on the two labelled shores with maximum degree at most \(R\), write \(m_n=|E(H_n)|\), and put \(G_n=K_{n,n}\setminus E(H_n)\). Let \(N(G_n)\) count *primitive period-two chip-configuration orbits*, each orbit once, under synchronous degree-threshold parallel chip firing with nonnegative integral chips. Then, as \(n\to\infty\), uniformly over all such \(H_n\),
\[
\frac{N(G_n)}{N(K_{n,n})}=\exp(-2m_n/n)\bigl(1+o_R(1)\bigr),
\qquad
N(G_n)=\frac{\sqrt{\pi n}}4\bigl(1+o_R(1)\bigr)\prod_{v\in V(G_n)}\deg_{G_n}(v).
\]
Choose a primitive period-two orbit uniformly and then choose one of its two phases uniformly. If \(I_n\) is the number of firing vertices on the first shore in that phase, then \(I_n/n\) converges uniformly over \(H_n\) in distribution to the arcsine law \(\operatorname{Beta}(1/2,1/2)\), with distribution function \(t\mapsto(2/\pi)\arcsin\sqrt t\) for \(0\le t\le1\).

For an \(r\)-regular deleted graph \(H_n\) with fixed \(r\), the first formula gives \(N(G_n)/N(K_{n,n})\to e^{-2r}\). In particular deletion of a perfect matching produces the ratio \(e^{-2}\). This is a theorem about existing primitive period-two orbits, not the number or size of their attraction basins and not a claim that every orbit has period two.

## Assumptions and scope
The two shores both have \(n\) labelled vertices; deleted edges have no multiplicities. The parameter \(R\) is fixed independently of \(n\), but \(H_n\) can be irregular, disconnected and chosen adversarially. A vertex with at least its degree in chips fires one chip to every neighbor, with all vertices updating simultaneously. Each finite chip state has nonnegative integer coordinates. Since \(n>2R\), any two vertices in one shore have a common neighbor in \(G_n\), and \(G_n\) is connected. All error estimates are uniform over the graph deletions for a fixed \(R\). The limiting law concerns an orbit chosen uniformly from the finite set of *primitive* two-cycles, with an independently uniform phase.

## Proof
**1. Exact period-two enumeration identity.** Let \(G=(V,E)\) be any connected simple graph of positive degree, \(d_v=\deg_G(v)\), and let \(f(v)\in\{0,1\}\) be the firing indicator at a phase \(c\). Its successor is
\[
U(c)_v=c_v-d_vf(v)+\sum_{w\sim v}f(w).
\]
If \(U^2(c)=c\), the sum of firing indicators in the two rounds is in the kernel of the graph Laplacian and therefore constant across the connected graph. For a primitive two-cycle this constant is one (constants zero and two give fixed states), so the next firing vector is \(1-f\). Put \(o_v(f)=|\{w\sim v:f(w)\ne f(v)\}|\). If \(f(v)=1\), the constraints that \(v\) fires now and waits next round are precisely \(d_v\le c_v\le d_v+o_v(f)-1\). If \(f(v)=0\), the reverse constraints are \(d_v-o_v(f)\le c_v\le d_v-1\). Every such coordinate choice is nonnegative and indeed returns after two rounds. There are exactly \(o_v(f)\) choices for coordinate \(v\), independent over vertices. Dividing by two phases, the exact identity is
\[
N(G)=\frac12\sum_{f\in\{0,1\}^{V}}\prod_{v\in V}o_v(f).
\tag{1}
\]
This exact counting identity and its mass-refined version are established background; the new assertion is the asymptotic stability under arbitrary bounded-degree edge deletion.

**2. Biclique reference measure.** Write \(i\) for the number of left-shore firing vertices and \(j\) for the number on the right. For the complete bipartite graph, the sum of products in (1), grouped by \((i,j)\), is
\[
W_n(i,j)=\binom ni\binom nj (n-j)^i j^{n-i}(n-i)^j i^{n-j}.
\]
Using \(0^0=1\) and setting \(q_n(i,j)=W_n(i,j)/n^{2n}\), this equals the product of two binomial probabilities,
\[
q_n(i,j)=\Pr\{\operatorname{Bin}(n,1-j/n)=i\}\,\Pr\{\operatorname{Bin}(n,1-i/n)=j\}.
\tag{2}
\]
For \(t=i/n\in[\varepsilon,1-\varepsilon]\) and \(j=n-i+u\sqrt n\), Stirling's formula gives the uniform local Gaussian approximation, for bounded \(u\),
\[
q_n(i,j)=\frac{e^{-u^2/[t(1-t)]}}{2\pi n\,t(1-t)}(1+o_\varepsilon(1)).
\tag{3}
\]
Standard exponential binomial tails bound the region of large \(|u|\), uniformly on that interior strip. Summing (3) over \(j\), a Riemann sum of spacing \(n^{-1/2}\), gives
\[
\sum_{j=0}^n q_n(i,j)=\frac{1+o_\varepsilon(1)}{2\sqrt{\pi n\,t(1-t)}}.
\tag{4}
\]
The endpoint restriction can be removed: for any fixed \(i\), bound the first factor of (2) by its maximum over the binomial success parameter and sum the second factor over \(j\) to one. The elementary maximal-binomial-mass estimate yields
\[
\sum_jq_n(i,j)\le\frac{C}{\sqrt{1+\min(i,n-i)}}.
\tag{5}
\]
Thus the combined contribution with \(i<\varepsilon n\) or \(i>(1-\varepsilon)n\) is \(O(\sqrt{\varepsilon n})\). Equations (4)–(5), then \(\varepsilon\downarrow0\), establish
\[
\sum_{i,j}q_n(i,j)\sim\frac{\sqrt{\pi n}}2,
\qquad N(K_{n,n})\sim\frac{\sqrt{\pi n}}4n^{2n}.
\tag{6}
\]
With any bounded continuous test function of \(i/n\), the same argument yields the probability density \(1/[\pi\sqrt{t(1-t)}]\) on \((0,1)\).

**3. Effect of deleted edges.** Fix \((i,j)\) in the interior strip, and independently choose uniformly a firing subset of size \(i\) on the left and size \(j\) on the right. Let \(o^K_v\) denote the opposite-firing-neighbor count in \(K_{n,n}\), and let \(r_v\le R\) be the number of deleted neighbors with opposite firing indicator. The ratio of the cut weights in (1) is
\[
\mathcal R_f=\prod_v\left(1-\frac{r_v}{o^K_v}\right),\quad
X_f=\sum_{uv\in E(H_n)}\mathbf1_{f(u)\ne f(v)}\left(\frac1{o^K_u}+\frac1{o^K_v}\right).
\tag{7}
\]
As \(o^K_v\ge\varepsilon n\), expanding \(\log(1-z)\) gives \(\mathcal R_f=\exp[-X_f+O_R(1/(\varepsilon^2 n))]\) uniformly in the two firing subsets. For one deleted edge with endpoints on opposite shores, the probability of the firing pattern \((1,0)\) is \((i/n)(1-j/n)\) and the associated sum of reciprocals is \(1/(n-j)+1/i\). For pattern \((0,1)\), the corresponding values are \(((n-i)/n)(j/n)\) and \(1/j+1/(n-i)\). Hence **every deleted edge has expected contribution exactly \(2/n\)**, and
\[
\mathbb E[X_f\mid i,j]=2m_n/n.
\tag{8}
\]
For a variance bound, let \(Z_{10}\) count deleted edges whose left endpoint fires and right endpoint waits, and let \(Z_{01}\) count the reversed pattern. Conditional on the chosen left subset, each of these is a weighted fixed-size sample of the right vertices with coefficients bounded by \(R\), so its conditional variance is \(O(R^2n)\) (distinct inclusion indicators have nonpositive covariance). Its conditional mean is a fixed-size sample of the left degrees in \(H_n\), again with variance \(O(R^2n)\). The law of total variance proves \(\operatorname{Var}(Z_{10}),\operatorname{Var}(Z_{01})=O(R^2n)\). Their multipliers in (7) are each \(O(1/(\varepsilon n))\), giving
\[
\operatorname{Var}(X_f\mid i,j)=O_R(1/(\varepsilon^2n)).
\tag{9}
\]
Because \(x\mapsto e^{-x}\) is one-Lipschitz for nonnegative \(x\), (7)–(9) imply
\[
\mathbb E[\mathcal R_f\mid i,j]=e^{-2m_n/n}+o_{R,\varepsilon}(1)
\tag{10}
\]
uniformly in \(H_n,i,j\) on the strip. The weights for deleted-edge graphs are no larger than the complete-biclique weights. By (5), endpoint weights are negligible; (10) and (6) therefore give \(N(G_n)/N(K_{n,n})=e^{-2m_n/n}(1+o_R(1))\), since \(0\le m_n/n\le R\) keeps the leading ratio bounded away from zero. The same stripwise constant reweighting, applied to test functions, preserves the arcsine limit.

**4. Degree normalization.** Every vertex loses at most \(R\) neighbors, and \(\sum_v\deg_{H_n}(v)=2m_n\), so
\[
\log\frac{\prod_v\deg_{G_n}(v)}{n^{2n}}
=\sum_v\log\left(1-\frac{\deg_{H_n}(v)}n\right)
=-\frac{2m_n}n+O_R(n^{-1}).
\]
Combining this with (6) completes the asserted uniform product formula.

## Verification
The accompanying standalone Python program checks the exact complete-biclique and crown-graph formulas (including direct firing-vector sums for small sizes) and compares the crown orbit ratio through \(n=80\) with its predicted limit. The independent C++ program directly simulates two rounds of integer chip firing, checks primitive-two-cycle configurations and compares counts with (1) for complete bicliques, matching deletions and irregular deletions. Run `python checks/verify_formula.py` and compile `checks/verify_independent.cpp` with a C++17 compiler. The stored outputs correspond to those exact source files. These finite computations check the implementation and low-size boundaries; they are not the reason for the uniform all-size theorem, whose proof is above.

## Relationship to prior work
Jiang's 2010 preprint gives the connected-graph firing-count lemma and possible period lengths of complete multipartite systems, not this orbit-count perturbation law. Jiang, Scully and Zhang (2012 preprint; 2015 journal) study admissible firing patterns and the impossibility of clumpy patterns. Ji, Li and Wang (2024) analyze non-stabilization and periods in a chip-count window. The exact general cut-degree orbit enumerator and the exact balanced-complete-bipartite count and arcsine limit are also known; those ingredients, including the unperturbed case, are **not** claimed new. The new assertion is the uniform asymptotic theorem for *every* bounded-degree missing-edge pattern, including irregular choices and the precise edge-deletion exponential correction. These earlier statements do not themselves imply that correction or the law's uniform survival.

## Limitations
This is a fixed-\(R\), \(n\to\infty\) result: it does not cover deleted graphs whose maximum degree grows arbitrarily with \(n\). It counts primitive two-cycle orbits, not initial-state attraction basins, and gives no census of larger-period orbits. The asymptotic error is not optimized, and equality of complete finite-size counts is not asserted. The general-graph counting identity, complete-biclique asymptotic and the arcsine limit with no deleted edges are established prior results. Equivalent work not indexed by the searched databases remains a priority risk; the full text of one later period-two density theorem was not available for inspection, although its accessible statement concerns periods rather than this orbit census.

## References
- T.-Y. Jiang, *On the Period Lengths of the Parallel Chip-Firing Game*, arXiv:1003.0943, initially submitted 2010-03-04; Sections 2–3 examined. https://arxiv.org/abs/1003.0943
- T.-Y. Jiang, Z. Scully, and Y. X. Zhang, *Motors and Impossible Firing Patterns in the Parallel Chip-Firing Game*, arXiv:1211.6786, initially submitted 2012-11-29; journal version SIAM J. Discrete Math. 29 (2015), 615–630, doi:10.1137/130933770. https://arxiv.org/abs/1211.6786
- D. Ji, M. Li, and D. Wang, *Non-Stabilizing Parallel Chip-Firing Games*, arXiv:2408.10508, 2024; introduction and main results examined. https://arxiv.org/abs/2408.10508
- *All parallel chip-firing games with \(2|E|-|V|<|\sigma|<2|E|\) have period \(2\)*, arXiv:2608.04153, 2026; accessible abstract only. https://arxiv.org/abs/2608.04153
