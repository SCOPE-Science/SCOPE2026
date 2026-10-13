# Root concavity and a unique size-class peak in circular random geometric graphs

## Finding
Let \(n\ge3\) and \(2\le k\le n-1\) be integers. On the unit circle, sample \(n\) independent uniform positions and connect vertices separated by geodesic distance at most \(r\in(0,1/2)\). Write \(C_{n,k}(r)\) for the number of connected components containing precisely \(k\) vertices, and put \(p_{n,k}(r)=\mathbb E[C_{n,k}(r)]/n\). Then
\[
p_{n,k}(r)=\sum_{j=0}^{k-1}(-1)^j\binom{k-1}{j}\bigl(1-(j+2)r\bigr)_+^{n-1},\qquad (x)_+=\max\{x,0\}.
\]
**Size-class peak theorem.** The positive function \(p_{n,k}(r)^{1/(n-1)}\) is concave over the entire interval \((0,1/2)\). It has a unique maximizing radius \(r_{n,k}\in(0,1/2)\), also the unique maximizer of \(\mathbb E[C_{n,k}(r)]\). For each fixed \(k\ge2\),
\[
\lim_{n\to\infty}n r_{n,k}=\log\frac{k+1}{2},\qquad
\lim_{n\to\infty}p_{n,k}(c/n)=e^{-2c}(1-e^{-c})^{k-1}\quad(c>0).
\]
The displayed exact expectation follows from classical spacings laws and is provided to normalize the shape theorem, not as a claim of historical novelty.

## Assumptions and scope
The model uses a unit-circumference circle and pairwise *shorter circular arc distance*, not directed arcs. Positions are iid uniform, so distinctness and absence of exact threshold ties hold with probability one. The assumptions \(2\le k<n\) exclude the singleton count (which is monotone) and the full-graph component count (which has a different boundary behavior). The radius always satisfies \(0<r<1/2\). The power-concavity assertion concerns the normalized expectation \(p_{n,k}\), not sample-path component counts, distributions, variances, or other geometric domains.

## Proof
**1. Geometric reduction and normalization.** Choose a uniformly random sampled point as the first vertex, list the positions clockwise from that anchor, and let \(G_1,\ldots,G_n\) be the successive cyclic gaps, with \(\sum_iG_i=1\). Their joint law is uniform on the \((n-1)\)-dimensional simplex
\[
\Delta_{n-1}=\{g_i\ge0:\sum_{i=1}^n g_i=1\}.
\]
A clockwise run of exactly \(k\) consecutive vertices forms a proper connected component if and only if its \(k-1\) internal gaps are at most \(r\), and its two bordering gaps exceed \(r\). Indeed, its internal short-gap edges connect the run. No edge can cross an exterior gap longer than \(r\) in either direction of the circle. Conversely every proper component must be such a run. Let \(K_r\subset\Delta_{n-1}\) be the simplex slice specified by two fixed bordering coordinates \(g_0,g_k\ge r\) and fixed internal coordinates \(g_1,\ldots,g_{k-1}\le r\). By cyclic exchangeability, \(\mathbb E C_{n,k}(r)=n\operatorname{vol}_{n-1}(K_r)/\operatorname{vol}_{n-1}(\Delta_{n-1})\). The labels of the other gaps do not matter. Shifting the two borders by \(r\), then applying inclusion-exclusion to the upper bounds on the internal gaps, gives the exact formula above. It also shows that \(K_r\) has positive relative volume for every \(r\in(0,1/2)\).

**2. Root concavity.** For \(r,s\in(0,1/2)\) and \(\theta\in[0,1]\), all slice inequalities are affine in the gap vector and radius, so
\[
(1-\theta)K_r+\theta K_s\subseteq K_{(1-\theta)r+\theta s}.
\]
The Brunn–Minkowski inequality for measurable convex bodies in the affine \((n-1)\)-space \(\sum_i g_i=1\) now implies
\[
p_{n,k}((1-\theta)r+\theta s)^{1/(n-1)}\ge(1-\theta)p_{n,k}(r)^{1/(n-1)}+\theta p_{n,k}(s)^{1/(n-1)}.
\]
This is a stronger statement than ordinary log-concavity.

**3. Existence and uniqueness.** The probability tends to zero as \(r\downarrow0\) because at least one internal gap must be \(\le r\); it tends to zero as \(r\uparrow1/2\) because two different gaps must each exceed \(r\). Continuity and positivity imply at least one interior maximizer. Concavity makes its maximizing set an interval. To exclude any nontrivial plateau, fix an open interval avoiding the finitely many breakpoints \(r=1/(j+2)\), for \(0\le j\le k-1\). There \(p_{n,k}\) is a polynomial
\[
P_J(r)=\sum_{j=0}^J(-1)^j\binom{k-1}{j}(1-(j+2)r)^{n-1},\quad 0\le J\le k-1.
\]
If \(P_J\) were constant, its derivatives of orders \(1,\ldots,J+1\) at zero would vanish. Because \(n-1\ge k\ge J+1\), these derivative equations say that the nonzero coefficient vector \(\bigl((-1)^j\binom{k-1}{j}\bigr)_{j=0}^J\) is in the kernel of the square matrix \(\bigl((j+2)^\ell\bigr)_{1\le\ell\le J+1,0\le j\le J}\). That matrix is invertible: it is a Vandermonde matrix multiplied by nonzero column factors. Contradiction. Every nonempty interval contains an open subinterval disjoint from the breakpoints, so no plateau exists. The maximizer is unique.

**4. Sparse-scale peak location.** For fixed \(k\ge2\) and \(c>0\), the finite inclusion-exclusion formula gives, uniformly on compact \(c\)-intervals,
\[
p_{n,k}(c/n)\longrightarrow f_k(c):=e^{-2c}(1-e^{-c})^{k-1}.
\]
The strictly positive function \(f_k\) has a unique critical point \(c_k=\log((k+1)/2)\), which is its global maximum, since
\[
\frac{d}{dc}\log f_k(c)=-2+\frac{k-1}{e^c-1}.
\]
To keep maximizing radii on a compact \(c=nr\) scale, a Dirichlet marginal-density bound on the \(k-1\) internal gaps gives \(p_{n,k}(c/n)\le c^{k-1}\). Requiring a particular bordering gap to exceed \(r\) gives \(p_{n,k}(c/n)\le(1-c/n)^{n-1}\le e^{-c/2}\) for \(n\ge2\). These bounds exclude \(c\downarrow0\) and \(c\uparrow\infty\) for maximizing sequences because \(f_k(c_k)>0\). Uniform convergence on the remaining compact set and the unique maximum of \(f_k\) force \(nr_{n,k}\to c_k\).

## Verification
Run `python3 checker.py` with standard Python 3. The checker independently evaluates the exact alternating sum with rational arithmetic, tests root concavity on a grid, simulates circular spacings by normalizing independent exponentials, and checks finite-sample convergence toward the sparse-limit profile. These finite checks corroborate the identities but do not replace the all-parameter analytic Brunn–Minkowski and Vandermonde arguments.

## Relationship to prior work
Huillet (2003, Section 4.1, Lemma 6 and Section 4.2) gives the joint gap-pattern probabilities and joint physical component-length transform for equal random arcs on the circle. This earlier work includes stronger raw spacing information from which the exact expectation formula above is an elementary consequence. That formula, circular gap exchangeability and sparse exponential spacing limits are not asserted to be new. The present result concerns the stronger \((n-1)\)-root concavity for **each prescribed component vertex count**, the unique global finite-sample peak, and its explicit scale. Decreusefond–Ferraz (arXiv:1008.5140v1) derive whole-cluster-count laws for Poisson points in an interval and on a circle; their Section 4.2 does not give this fixed-\(n\), vertex-size-resolved shape classification. Penrose–Yang (arXiv:2209.14758) study k-component counts in high-intensity and sparse asymptotic regimes in Euclidean domains, rather than an all-radius finite-sample root-concavity law on a circle.

## Limitations
No new assertion is made about joint component-count distributions, higher-dimensional geometric graphs, unequal node intensities, or the full-graph cluster. The asymptotic location assumes **fixed** \(k\) as \(n\to\infty\); it does not address \(k\) growing with sample size. Classical joint spacing identities cover the expectation formula. While the inspected sources do not state the root-concavity/unique-optimum classification, a broader classical treatment of convex-section inequalities or a less accessible earlier source may contain an implicit equivalent. No independent historical-priority audit is claimed.

## References
1. T. Huillet, “Random covering of the circle: the size of the connected components,” *Advances in Applied Probability* 35 (2003), 563–582. DOI: 10.1239/aap/1059486818. Inspected author-posted complete text, especially Lemma 6 and Sections 4.1–4.2.
2. L. Decreusefond and E. Ferraz, “On the One dimensional Poisson Random Geometric Graph,” arXiv:1008.5140v1 (first posted 2010-08-30), Section 4.2.
3. M. D. Penrose and X. Yang, “On k-clusters of high-intensity random geometric graphs,” arXiv:2209.14758v1 (first posted 2022-09-29), Sections 1 and 3–6.
4. The classical Brunn–Minkowski inequality for volumes of convex subsets of Euclidean affine spaces.
