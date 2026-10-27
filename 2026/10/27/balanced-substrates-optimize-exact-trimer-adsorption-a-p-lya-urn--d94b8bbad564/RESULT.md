# Balanced substrates optimize exact trimer adsorption: a Pólya-urn profile and a Gaussian design window

## Finding
Let \(t\geq1\), and deposit three-site path-shaped adsorbates irreversibly on every undirected length-two path of the complete bipartite graph \(K_{a,3t-a}\), at independent equal positive attempt rates. An attempt succeeds precisely when all three sites are vacant. Write \(f_t(a)\) for the probability that **all** \(3t\) sites eventually become covered, and set it to zero outside \(t\leq a\leq2t\). Its complete exact profile is determined by \(f_1(1)=f_1(2)=1\) and, for \(t\geq2\),
\[
 f_t(a)=\frac{(a-1)f_{t-1}(a-2)+(3t-a-1)f_{t-1}(a-1)}{3t-2},\qquad t\leq a\leq2t.
\]
For fixed \(3t\), the profile is symmetric and strictly increases toward balance; if \(t\) is even its unique maximizer is \(a=3t/2\), and if \(t\) is odd its exactly two maximizers are \(a=(3t-1)/2\) and \(a=(3t+1)/2\). Complete coverage is impossible when \(3\) does not divide the total vertex count, or when a class has fewer than one-third of the vertices.

At the extreme feasible imbalance the exact rare-event probability and its sharp asymptotic are
\[
 f_t(t)=\prod_{j=1}^{t}\frac{2j-1}{3j-2}
 =\frac{\Gamma(1/3)}{\sqrt{\pi}}\frac{\Gamma(t+1/2)}{\Gamma(t+1/3)}\left(\frac23\right)^t
 \sim\frac{\Gamma(1/3)}{\sqrt{\pi}}\left(\frac23\right)^t t^{1/6},
\]
and moving a single vertex inward from this feasibility boundary amplifies the probability by exactly
\[
 f_t(t+1)=\frac{t+2}{3}f_t(t).
\]

The total profile weight is
\[
 S_t:=\sum_{a=0}^{3t}f_t(a)
 =\frac{\Gamma(1/3)\Gamma(t+2/3)}{\Gamma(2/3)\Gamma(t+1/3)}.
\]
Normalize the profile into a probability distribution \(\Pr(A_t=a)=f_t(a)/S_t\). Then \(A_t\) has an exact two-colour balanced Pólya-urn representation, and
\[
 \mathbb E A_t=\frac{3t}{2},\qquad
 \operatorname{Var}(A_t)=\frac{3t+2}{4}-\prod_{j=1}^{t-1}\frac{3j+4}{3j+2},
\]
\[
 \frac{A_t-3t/2}{\sqrt t}\ \xrightarrow{\ d\ }\ \mathcal N(0,3/4).
\]
The last statement is a **weak limit for the normalized profile across graph compositions**, not a pointwise local limit for individual \(f_t(a)\).

## Assumptions and scope
A length-two path is an unordered set of three distinct graph vertices spanning a path with a designated middle vertex. On a complete bipartite graph it consists of two vertices in one bipartition class and one in the other; its middle vertex is the singleton-class vertex, so no path is double-counted. Every such path has its own rate-one Poisson attempt clock; occupied vertices permanently exclude subsequent arrivals. The same eventual jamming law holds at any common strictly positive clock rate. All finite-size formulas concern integer \(t\geq1\) and integers \(0\leq a\leq3t\). Zero-size classes have no available paths and cannot cover a positive number of vertices. The all-vacant initial state is assumed.

The probability \(f_t(a)\) is a *perfect-cover* probability, not the mean coverage fraction, the adsorption duration, or the probability of a maximum matching chosen offline. Accepted adsorbates are vertex-disjoint, and the process ends when no vacant length-two path remains.

## Proof
**1. Reduction to two counts.** Suppose that \(u\) vertices remain vacant in the first class and \(v\) in the second. There are \(\binom u2v\) available paths of type \((2,1)\) and \(u\binom v2\) of type \((1,2)\). Since all path clocks have equal rates, conditional on another success, the respective probabilities are
\[
 \frac{u-1}{u+v-2},\qquad \frac{v-1}{u+v-2},
\]
whenever \(u,v>0\) and \(u+v\geq3\). Each successful arrival removes exactly three vacant vertices. For \(u+v=3t\), conditioning on the first arrival proves the displayed recursion, including its \(t=1\) boundary. If all vertices are covered by \(t\) paths, the numbers of paths of the two types must respectively be \(a-t\) and \(2t-a\); hence feasibility requires \(t\leq a\leq2t\). Conversely, any nonnegative solution of those two counts can be ordered into valid successive adsorptions, so every feasible composition has positive probability.

**2. Optimization at balance.** Swapping classes gives \(f_t(a)=f_t(3t-a)\). Extend the profile by zero outside its support and let \(\delta_t(a)=f_t(a+1)-f_t(a)\). Subtracting neighboring instances of the recursion gives the *difference recursion*
\[
 (3t-2)\delta_t(a)=(a-1)\delta_{t-1}(a-2)
 +(3t-a-2)\delta_{t-1}(a-1).
\]
The base profile at \(t=2\) is \((3/4,1,3/4)\) on its support. Inductively, for \(t\geq3\) and \(t\leq a<\lfloor 3t/2\rfloor\), both coefficients are positive and both indices on the right lie on the nondecreasing half of the preceding symmetric profile; at least one difference is strictly positive. Thus \(\delta_t(a)>0\). Symmetry supplies the decreasing half and, for odd \(t\), the central tie. This proves all maximizers without a continuous approximation.

**3. Extremal rare event and boundary layer.** At \(a=t\), a successful perfect filling must always remove one first-class site and two second-class sites. Consequently
\(f_t(t)=(2t-1)f_{t-1}(t-1)/(3t-2)\), giving the product. The gamma identity follows from the rising-factorial formula, and the gamma-ratio asymptotic gives the exponent \(1/6\). Dividing the recurrence for \(f_t(t+1)\) by that for \(f_t(t)\), induction from \(t=1\) yields the exact ratio \((t+2)/3\).

**4. An urn hidden in the full-cover profile.** Sum the recurrence over every integer \(a\). For each old composition \(x\), the two coefficients of its contributions to the new profile add to \(3t-1\), proving \(S_t=(3t-1)S_{t-1}/(3t-2)\), with \(S_1=2\). This gives the stated gamma formula. Dividing the same recurrence by \(S_t\) constructs the probability process
\[
 A_{k+1}=\begin{cases}A_k+2&\text{with probability }(A_k+1)/(3k+2),\\
 A_k+1&\text{with probability }(3k+1-A_k)/(3k+2),\end{cases}
\]
starting with \(A_1\) uniformly in \(\{1,2\}\). Put \(R_k=A_k+1\), \(B_k=3k+1-A_k\); their sum is \(3k+2\). Drawing red with probability \(R_k/(R_k+B_k)\) adds \((2,1)\) to the red/blue counts, and drawing blue adds \((1,2)\). The initial urn is equally likely to be \((2,3)\) or \((3,2)\). This is exactly the deterministic balanced replacement matrix \(\bigl(\begin{smallmatrix}2&1\\1&2\end{smallmatrix}\bigr)\).

**5. Exact fluctuations and Gaussian window.** Let \(C_k=A_k-3k/2\). The increment \(\xi_k=C_{k+1}-C_k\) is \(+1/2\) or \(-1/2\), with \(\mathbb E(\xi_k\mid C_k)=C_k/(3k+2)\) and \(\xi_k^2=1/4\). Symmetry gives \(\mathbb E C_k=0\), and
\[
 v_{k+1}=\frac{3k+4}{3k+2}v_k+\frac14,\quad v_1=\frac14,
\]
whose exact solution is the stated variance. In particular \(v_k/k\to3/4\).

For completeness the Gaussian claim does not require importing a general urn theorem. With \(m_{r,k}=\mathbb E C_k^r\), symmetry makes all odd moments zero. For every fixed integer \(r\geq1\), expansion of \((C_k+\xi_k)^{2r}\), induction on \(r\), and the identities \(\mathbb E(\xi_k^j\mid C_k)=2^{-j}\) for even \(j\) and \(2^{1-j}C_k/(3k+2)\) for odd \(j\), give
\[
 m_{2r,k+1}=\left(1+\frac{2r}{3k+2}\right)m_{2r,k}
 +\frac{r(2r-1)}4m_{2r-2,k}+O_r(k^{r-2}).
\]
The inductive bounds \(m_{2r,k}=O_r(k^r)\) and this recurrence imply \(m_{2r,k}\sim (2r-1)!!(3/4)^rk^r\) (solve the first-order recurrence using \(2r/3<r\)); the base case is the exact variance. These are precisely the moments of \(\mathcal N(0,3/4)\). Tightness follows from the variance bound, and the Gaussian moment problem is determinate, proving weak convergence.

## Verification
Run `python3 verify_trimers.py` using Python's standard library. The program independently enumerates all labeled vacant-site subsets and all individually available length-two paths of \(K_{a,b}\) for every positive bipartition with total size \(3t\), \(1\leq t\leq4\), then compares full-state hitting probabilities with the two-count recursion using exact fractions. It also checks the support, reflection symmetry, strict optimization, gamma-free product identities, adjacent-boundary ratio, total weight, exact mean and variance at \(1\leq t\leq60\), plus illustrative finite-size Gaussian comparisons. The packaged program passed 514 assertions. No finite computation is presented as proof of the all-size Gaussian limit.

## Relationship to prior work
Penrose and Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs* (arXiv:math/0503519v1, 2005), study monomer blocking and **edge dimer** adsorption on graphs, with finite-order descriptions and infinite-tree analysis. Their stated graph processes do not deposit length-two paths, nor evaluate this complete-bipartite perfect-cover composition profile. Cieśla and Barbasz, *Random sequential adsorption of trimers and hexamers* (arXiv:1309.7021v1, 2013), study *continuum planar* trimer/hexamer adsorption and measure numerical jamming coverage; their full model and results concern a different substrate and observables. Janson's general Pólya-urn limit theory (2004) covers Gaussian limits of suitable small urns; the Gaussian limit of the identified \((2,1)/(1,2)\) urn is accordingly not asserted as new in isolation. The contribution is the specific adsorption-to-urn identity, the evaluated exact perfect-cover profile and extremal probability, strict optimal substrate balance, sharp feasibility-boundary law, and quantified composition window. Bennett and Bohman's 2019 random-greedy hypergraph-matching work gives general asymptotic unmatched-set bounds rather than these evaluated finite composition probabilities.

## Limitations
Only equal path-attempt rates on finite **complete bipartite** graphs and perfect three-site path coverage are considered. The associated physical process differs from continuum RSA of connected geometric trimers. The Gaussian result describes the normalized *across-composition profile*, not a distribution of coverage counts on one fixed graph or a local limit theorem. Exact pointwise large-\(t\) asymptotics at the central maximizing compositions, entire jammed-coverage distributions, unequal path rates, and arbitrary graph families are not established. A historical specialist paper could contain an equivalent evaluated trimer profile; uniqueness or priority is not inferred from unsuccessful searches.

## References
1. M. D. Penrose and A. Sudbury, *Exact and approximate results for deposition and annihilation processes on graphs*, Ann. Appl. Probab. **15** (2005), 853–889; arXiv:math/0503519v1 (first public 2005-03-24), https://arxiv.org/abs/math/0503519.
2. M. Cieśla and J. Barbasz, *Random sequential adsorption of trimers and hexamers*, J. Mol. Model. **19** (2013), 5423–5427; arXiv:1309.7021v1 (first public 2013-09-26), https://arxiv.org/abs/1309.7021.
3. S. Janson, *Functional limit theorems for multitype branching processes and generalized Pólya urns*, Stochastic Process. Appl. **110** (2004), 177–245, https://doi.org/10.1016/j.spa.2003.12.002.
4. P. Bennett and T. Bohman, *A natural barrier in random greedy hypergraph matching*, Combin. Probab. Comput. **28** (2019), 816–825, https://doi.org/10.1017/S0963548319000051.
