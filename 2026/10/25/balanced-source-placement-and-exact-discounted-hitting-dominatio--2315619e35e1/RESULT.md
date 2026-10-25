# Balanced source placement and exact discounted hitting domination on wheel graphs

## Finding
For every wheel \(W_n=K_1\vee C_n\), with \(n\ge4\) rim vertices, every discount \(0<\lambda<1\) and uniform threshold \(0<\tau\le1\), the discounted hitting domination number has the explicit arithmetic formula below. More strongly, among all source sets with a fixed number of rim sources and a fixed choice of whether to include the hub, a maximizer of the minimum discounted hitting potential is obtained by spacing the rim sources as evenly as possible. The result is valid at exact threshold equalities, and no integrality condition is imposed on \(\lambda\) or \(\tau\).

Define \(p_0=0\), \(p_1=1\), and for \(j\ge1\)
\[
p_{j+1}=\frac{3}{\lambda}p_j-p_{j-1}.
\]
For \(1\le m\le n\), set
\[
\psi_m=\frac{p_{\lfloor m/2\rfloor}+p_{\lceil m/2\rceil}}{p_m},\qquad
D_m=m-1-\frac{2}{p_m}\sum_{j=1}^{m-1}p_j.
\]
Thus \(\psi_1=1\) and \(D_1=0\). For \(1\le k\le n\), write
\[
q=\lfloor n/k\rfloor,\quad r=n-kq,\quad M=\lceil n/k\rceil,\quad
D_{n,k}=(k-r)D_q+rD_{q+1},
\]
where the last term is interpreted as zero if \(r=0\). Define
\[
X_{n,k}=\frac{\lambda(n-D_{n,k})}{n-\lambda^2D_{n,k}/(3-2\lambda)},\qquad
B_{n,k}=\frac{\lambda X_{n,k}}{3-2\lambda},\qquad
R_{n,k}=\min\{X_{n,k},\ B_{n,k}+(1-B_{n,k})\psi_M\}.
\]
Let \(t=\lambda/(3-2\lambda)\), and set
\[
H_{n,0}=t,\qquad H_{n,k}=t+(1-t)\psi_{\lceil n/k\rceil}\quad(1\le k\le n).
\]
Then the exact domination number is
\[
\boxed{\delta_{\lambda,\tau}(W_n)=\min\Big(\{k:1\le k\le n,\ R_{n,k}\ge\tau\}\ \cup\ \{k+1:0\le k\le n,\ H_{n,k}\ge\tau\}\Big).}
\]
Here \(R_{n,k}\) and \(H_{n,k}\) are, separately, the optimal **minimum-vertex** support with exactly \(k\) selected rim vertices and respectively excluding or including the hub. The displayed finite sets always include \(n+1\) through \(H_{n,n}=1\).

At \(n=4\), \(\lambda=3/5\) and \(\tau=2/5\), the optimum has size two and excludes the hub. Opposite selected rim vertices produce minimum support \(21/47\), whereas selecting the hub and any single rim vertex produces only \(9/23\), and the hub alone produces \(1/3\). Thus hub-first source placement can be strictly suboptimal despite the hub's maximum degree.

## Assumptions and scope
The graph is finite, simple and undirected, with hub \(c\), rim \(v_0,\ldots,v_{n-1}\) and edges \(cv_i\) and \(v_iv_{i+1\bmod n}\). The assumption \(n\ge4\) excludes the complete-graph case \(W_3\), already covered by earlier formulas. For nonempty \(S\subseteq V(W_n)\), define \(h_v^S=\mathbb E_v[\lambda^{T_S}]\), where \(T_S\) is the hitting time of \(S\) for a simple random walk, with \(\lambda^{\infty}=0\); equivalently \(h_v^S=1\) for \(v\in S\) and \(h_v^S=\lambda\sum_{w\sim v}h_w^S/\deg(v)\) otherwise. The latter system has a unique solution because \(0<\lambda<1\). Put \(\delta_{\lambda,\tau}(W_n)=\min\{|S|:\min_v h_v^S\ge\tau\}\). All minimax statements concern arbitrary subsets, not just periodic subsets. Balanced means that the \(k\) positive cyclic distances between successive selected rim vertices differ by at most one.

## Proof
**1. Segment transfer.** Suppose a selected-rim pair bounds a gap of \(m\ge1\) rim edges, with intermediate unselected rim vertices \(v_1,\ldots,v_{m-1}\), and the hub has support \(x\in[0,1]\). On each internal vertex,
\[
h_j=\frac\lambda3(h_{j-1}+h_{j+1}+x),\qquad h_0=h_m=1.
\]
The constant particular solution is \(b(x)=\lambda x/(3-2\lambda)\). The homogeneous Dirichlet solution expressed by the recurrence \(p_j\) gives
\[
h_j=b(x)+(1-b(x))\frac{p_{m-j}+p_j}{p_m},\qquad 0\le j\le m.
\]
The least potential in the gap occurs at either middle vertex, and equals \(b(x)+(1-b(x))\psi_m\). The sum over all vertices in this gap, counting the first boundary source but not the last, is \(m-(1-b(x))D_m\). These identities follow by substituting the recurrence and boundary values. The positivity \(p_m>0\) is immediate from \(p_m=\sinh(m\theta)/\sinh\theta\), where \(\cosh\theta=3/(2\lambda)>1\).

**2. Hub not selected.** Let \(k\ge1\) rim sources have cyclic gap lengths \(m_1,\ldots,m_k\), summing to \(n\), and let \(D=\sum_iD_{m_i}\). Summing the segment identity once around the rim gives \(\sum_{j=0}^{n-1}h_{v_j}=n-(1-b(x))D\). The hub equation is
\[
x=\frac\lambda n\left(n-\left(1-\frac{\lambda x}{3-2\lambda}\right)D\right).
\]
Its unique solution is
\[
x=\frac{\lambda(n-D)}{n-\lambda^2D/(3-2\lambda)}.
\]
Each \(D_m\) is a sum of \(m-1\) strictly smaller-than-one interior deficits, so \(0\le D<n\); the denominator is positive. Writing \(a=\lambda^2/(3-2\lambda)<1\), differentiation shows \(\lambda(n-D)/(n-aD)\) strictly decreases as \(D\) increases. The worst-vertex support equals the minimum of this hub value and the worst gap-middle value.

**3. Discrete convexity and balancing.** Put \(\rho=e^{-\theta}\in(0,1)\). A geometric-series calculation applied to the preceding transfer gives
\[
D_m=m-1-\frac{2\rho}{1-\rho}+\frac{2(1+\rho)}{1-\rho}\frac{\rho^m}{1+\rho^m}.
\]
The function \(s\mapsto1/(1+e^{\theta s})\) has strictly positive second derivative on \(s>0\), so \(D_m\) is strictly discretely convex for integers \(m\ge1\). Consequently, among positive integers \(m_1,\ldots,m_k\) with sum \(n\), the deficit \(D=\sum_iD_{m_i}\) is minimized exactly by gaps differing by at most one (apply the elementary exchange \((u,v)\mapsto(u+1,v-1)\) when \(v-u\ge2\)). Such gaps yield exactly \(D_{n,k}\), and they maximize the hub potential.

The middle-gap attenuation \(\psi_m\) strictly decreases with \(m\). Indeed, from the hyperbolic representation,
\[
\psi_{2a}=\frac{1}{\cosh(a\theta)}\quad(a\ge1),\qquad
\psi_{2a+1}=\frac{\cosh(\theta/2)}{\cosh((a+1/2)\theta)}\quad(a\ge0),
\]
and the interleaved sequence is strictly decreasing for \(m\ge1\): comparing an even term with the next odd term uses \(\cosh((a+1/2)\theta)=\cosh(a\theta)\cosh(\theta/2)+\sinh(a\theta)\sinh(\theta/2)\), whereas comparing an odd term with the next even term uses \(\cosh((a+1)\theta)\cosh(\theta/2)=[\cosh((a+3/2)\theta)+\cosh((a+1/2)\theta)]/2>\cosh((a+1/2)\theta)\). Any \(k\)-source placement has largest gap at least \(M=\lceil n/k\rceil\); a balanced placement simultaneously minimizes the deficit and attains longest gap \(M\). Since \(b(x)\) increases with \(x\), and \(b+(1-b)\psi_m\) increases with \(b\) and with \(\psi_m\), the balanced placement maximizes both the hub support and the least rim support, and hence their minimum. Substituting the balanced deficit and largest gap gives exactly \(R_{n,k}\).

**4. Hub selected.** The hub support is fixed at \(x=1\), so each gap has middle minimum \(t+(1-t)\psi_m\), independent of other gaps. For \(k\ge1\), minimizing the largest gap gives the optimal floor \(H_{n,k}\). If no rim source is selected, all rim potentials solve the constant equation \(h=\lambda(2h+1)/3\), giving \(H_{n,0}=t\).

**5. Selecting the optimum.** Every nonempty source set either contains the hub with exactly \(k\) rim sources or excludes the hub with \(k\ge1\) rim sources. The preceding maximization covers both disjoint cases for every possible cardinality; threshold comparison \(\ge\tau\) and minimization therefore give the displayed exact formula. For rational \(\lambda\) and \(\tau\), the recurrence, partial sums and at most \(2n+1\) threshold comparisons yield an exact \(O(n)\)-arithmetic-operation algorithm, with standard rational arithmetic and no exhaustive source-set enumeration. The real-parameter formula is exact as an identity without a specified floating-point certification method.

## Verification
The supplied independent verifier `verify_wheel.py` constructs each wheel from adjacency lists, solves the discounted Dirichlet equations by exact rational Gaussian elimination for every nonempty source subset on rim sizes \(3\) through \(8\), and compares with the derived gap formulas. The independent direct method evaluates \(3006\) nonempty source-set instances, \(216\) fixed-cardinality maximin floors, and \(126\) threshold optima at discounts \(\{1/3,3/5,4/5\}\) and seven thresholds. All comparisons passed. An additional exact calculation verifies \(W_4\)'s hub-exclusion example. The verifier prints `VERIFY_OK`; its recorded output is embedded in `verifier_output.txt`. Finite computations corroborate but do not replace the proof of the unrestricted theorem.

## Relationship to prior work
Allagan, Pereyra and Massey (2026) define discounted hitting domination, establish its general submodularity/complexity properties and derive path-gap transfer tools and spider-tree algorithms. Their source describes complete graphs and stars but does not establish the wheel maximin placement theorem or the all-parameter wheel formula. The present proof adapts the one-dimensional transfer to a global hub-feedback equation and proves the new convex-gap optimization needed to solve that coupling. The paper's distance-domination recovery at special parameter regimes can yield some wheel special cases; it does not imply the full continuous threshold-dependent formula here. Li, Yu, Huang and Cheng (2013) optimize fixed-cardinality finite-horizon random-walk objectives, not the minimum cardinality subject to a discounted worst-vertex floor. Guo and collaborators (2024) study group-hitting probability pairwise evaluation and top-\(k\) ranking relative to one starting vertex, not a common worst-vertex threshold for minimum-cardinality target sets. A related exact result for complete bipartite graphs is not applicable to wheels \(W_n\) for \(n\ge4\). The originality comparison is about mathematical implications, not shared terminology.

## Limitations
This theorem applies to one hub joined to a simple cycle and homogeneous \(\lambda\); it does not classify arbitrary cones, weighted walks or heterogeneous discounts. Balance provides an optimizer but is not asserted to characterize *all* maximizers: ties, especially for extreme thresholds or larger source counts, may occur. Publication priority remains subject to unindexed or differently named results in random-walk facility location and pinned-consensus literature; no claim of definitive novelty or independent validation is made.

## References
1. J. D. Allagan, K. Pereyra and W. A. Massey, *Discounted Hitting Domination on Graphs with Submodularity, Complexity and Exact Algorithms*, arXiv:2609.31535v1 (public 2026-09-25), https://arxiv.org/abs/2609.31535.
2. R.-H. Li, J. X. Yu, X. Huang and H. Cheng, *Random-walk domination in large graphs: problem definitions and fast solutions*, arXiv:1302.4546v1 (2013), https://arxiv.org/abs/1302.4546.
3. Q. Guo, D. Lin, S. Wang, R. C.-W. Wong and W. Lin, *Efficient Algorithms for Group Hitting Probability Queries on Large Graphs*, IEEE Transactions on Knowledge and Data Engineering 36 (2024), 2995–3008, doi:10.1109/TKDE.2023.3349164.
