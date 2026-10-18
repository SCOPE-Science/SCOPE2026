# Conditional negative association without real stability in random-cluster and forest measures on cactus graphs

## Finding
Let \(G=(V,E)\) be an arbitrary finite simple cactus graph: every edge belongs to at most one simple cycle. Give every edge a positive activity \(v_e\) and fix \(0<q\leq1\). The free-boundary random-cluster law is
\[
\mu_{q,v}(A)=\frac1{Z_{q,v}}q^{k(A)}\prod_{e\in A}v_e,\quad A\subseteq E,
\]
where \(k(A)\) counts connected components of the spanning subgraph \((V,A)\).

**Theorem.** The full family of edge indicators of \(\mu_{q,v}\) is **conditionally negatively associated under all positive external fields**, abbreviated CNA+. The same conclusion holds for the arboreal-gas law
\[
\mu_{\mathrm{forest},\lambda}(A)=\frac{\mathbf1_{\{(V,A)\text{ acyclic}\}}}{Z_{\mathrm{forest},\lambda}}\prod_{e\in A}\lambda_e,
\qquad\lambda_e>0.
\]
Thus for any distinct disjoint edge sets \(I,J\), any coordinatewise nondecreasing functions \(F(X_I)\) and \(H(X_J)\), any positive external-field tilt, and any positive-probability pinning of other coordinates, one has \(\operatorname{Cov}(F,H)\le0\). Coordinate projections preserve this property.

**Exact cycle covariance.** In a cycle \(C\), let \(r_e=v_e/(q+v_e)\), \(\rho_C=\prod_{e\in C}r_e\), and \(D_C=1-(1-q)\rho_C\). If \(\mathbb E_0\) denotes independent Bernoulli expectation with success probabilities \(r_e\), and \(F,H\) increase on disjoint subsets of \(C\), then
\[
\operatorname{Cov}_{\mu_{q,v}}(F,H)=-\frac{(1-q)\rho_C}{D_C^2}\bigl(F(\mathbf1)-\mathbb E_0F\bigr)\bigl(H(\mathbf1)-\mathbb E_0H\bigr).
\]
The same formula, with \(1-q\) replaced by \(1\), holds in the weighted forest measure with \(r_e=\lambda_e/(1+\lambda_e)\). Different cycles and bridges are mutually independent blocks. For distinct edges \(e,f\) of one cycle,
\[
\operatorname{Cov}(X_e,X_f)=-\frac{(1-q)\rho_C(1-r_e)(1-r_f)}{D_C^2},
\]
strictly negative for \(0<q<1\). For edges in different blocks it is zero.

**Hierarchy boundary.** If \(G\) contains any cycle, these laws for \(0\le q<1\) are **not strongly Rayleigh**: CNA+ does not imply real stability. For \(q=1\), the random-cluster measure is independent Bernoulli and is strongly Rayleigh. The notation \(q=0\) here refers only to the forest block law, not a random-cluster law at fixed positive edge activities.

## Assumptions and scope
All graphs are finite and simple; disconnected cactus graphs are allowed, including isolated vertices and bridges. Positive edge weights are fixed but may be heterogeneous. An external field multiplies the weight of every occupied edge \(e\) by an arbitrary positive number. Pinning means conditioning any designated coordinates to fixed binary values with strictly positive probability. A family is CNA+ when every positive external-field tilt, marginal, and positive-probability pinning is negatively associated. Negative association requires \(\mathbb E[FH]\le\mathbb EF\,\mathbb EH\) for all coordinatewise increasing real functions depending on disjoint sets of coordinates; no nonnegative-value restriction on the functions is imposed. These are finite probability spaces, so all observables are bounded.

## Proof
**1. Factorization on a cactus.** Write \(\mathcal C\) for the edge-disjoint simple cycles of \(G\). Every cycle of a spanning subgraph \((V,A)\) is an entire host cycle. Its cycle rank is therefore \(\sum_{C\in\mathcal C}\mathbf1_{\{C\subseteq A\}}\). The graphic identity gives
\[
k(A)=|V|-|A|+\sum_{C\in\mathcal C}\mathbf1_{\{C\subseteq A\}}.
\]
Thus, up to normalization, \(\mu_{q,v}(A)\) has weight
\[
\prod_{e\in A}(v_e/q)\prod_{C\in\mathcal C}q^{\mathbf1_{\{C\subseteq A\}}}.
\]
Since the host cycles are edge disjoint, each cycle block and every bridge form independent blocks. On a cycle the law is a Bernoulli product, with \(r_e=v_e/(q+v_e)\), reweighted by \(1-(1-q)\mathbf1_{\{X=\mathbf1\}}\), and normalization \(D_C=1-(1-q)\rho_C>0\).

**2. The rank-one covariance identity.** On a single cycle, write \(\delta=1-q\), \(\rho=\Pr_0(X=\mathbf1)\), \(D=1-\delta\rho\), \(u=\mathbb E_0F\), \(w=\mathbb E_0H\), \(f_*=F(\mathbf1)\), and \(h_*=H(\mathbf1)\). Disjoint dependence and independence under \(\Pr_0\) give \(\mathbb E_0FH=uw\). Consequently
\[
\mathbb E F=\frac{u-\delta\rho f_*}{D},\quad
\mathbb E H=\frac{w-\delta\rho h_*}{D},\quad
\mathbb E FH=\frac{uw-\delta\rho f_*h_*}{D}.
\]
Subtracting proves exactly
\[
\operatorname{Cov}(F,H)=-\frac{\delta\rho}{D^2}(f_*-u)(h_*-w)\le0,
\]
since monotonicity gives \(f_*\ge u\) and \(h_*\ge w\). The asserted indicator covariance follows by using \(F=X_e\) and \(H=X_f\).

**3. Products, tilts, pinning, and projections.** The independent product of finitely many negatively associated binary blocks is negatively associated. Indeed, for two blocks, condition first on one block. Disjoint supports in the other give a nonpositive conditional covariance. Conditional expectations are increasing functions of disjoint subsets of the first block, whose covariance is also nonpositive. Iteration proves the assertion. Arbitrary positive external fields only change each Bernoulli parameter of a cycle block and do not change the all-ones penalty \(q\). Fixing any coordinates to zero makes the penalty identically one on that residual block, while fixing only ones leaves the same \(q\)-penalized all-ones event among the residual coordinates. In either case, after normalization the residual block is of the same rank-one form, including when zero or one coordinates remain. All conditioning events considered have positive probability. Hence every tilted-and-pinned measure is a product of negatively associated blocks; taking coordinate marginals preserves negative association. This proves CNA+.

**4. Forest measure.** A subset of a cactus is acyclic exactly when it fails to contain at least one edge of each host cycle. Under independent Bernoulli edge indicators with \(r_e=\lambda_e/(1+\lambda_e)\), the forest law is the product distribution conditioned on no full cycle. Those restrictions are on disjoint edge blocks and therefore factor. A cycle block is the preceding measure with \(\delta=1\), normalizer \(1-\rho_C>0\). The same covariance proof, positive-field and pinning closure, and block-product argument establish CNA+ for arbitrary positive heterogeneous forest weights.

**5. Exact failure of real stability.** For any cycle of length \(m\ge3\), its unnormalized generating polynomial, after positive rescaling of its variables, is
\[
P(z_1,\ldots,z_m)=\prod_{j=1}^m(1+z_j)-\delta\prod_{j=1}^m z_j,
\quad 0<\delta\le1.
\]
Set \(c=\delta^{1/m}\exp(-2\pi i/m)\) and \(z=1/(c-1)\). Because \(\operatorname{Im}(c)<0\), \(\operatorname{Im}(z)>0\). Also \((1+z)/z=c\), so \(P(z,\ldots,z)=z^m(c^m-\delta)=0\). Thus this multivariate polynomial is not real stable. Specializing every edge outside this cycle to zero recovers its polynomial up to a positive scalar; real stability would be inherited by this real specialization. Hence any graph containing a cycle is not strongly Rayleigh under the indicated models. At \(q=1\), \(\delta=0\) and the generating polynomial is a product of linear factors with real nonpositive roots, proving the contrast. \(\square\)

## Verification
The standalone `verify_cactus_na.py` (Python standard library only) recomputes exact rational random-cluster probabilities on a weighted seven-edge cactus with two triangles meeting at one vertex and an additional bridge, at four cluster parameters; compares direct connected-component enumeration with the cycle-block factorization; tests disjoint increasing AND/OR observables; and independently checks rank-one covariances and every monotone Boolean observable on disjoint edge subsets of a four-edge cycle for two further parameters. Running `python verify_cactus_na.py` returned `PASS: 33908 exact rational assertions for two-cycle cactus and rank-one covariance`. All infinite families and all-parameter assertions follow from the analytic argument above, not from finite checks.

## Relationship to prior work
Park, *The \(q<1\) Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence* (first public 9 August 2026), proves conditional negative association for certain wired-tree branch-connectivity indicators and negative association for observables on distinct wired branches, not full edge CNA+ on finite cactus graphs. Çiçeksiz and Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model* (first public 30 September 2026), study edge-pair covariance under different general-graph and complete-graph hypotheses and explain why it does not establish negative association. Earlier series-parallel Potts–Rayleigh results control edge pairs, not arbitrary disjoint increasing functions. The block factorization, exact rank-one covariance for nonlinear increasing observables, conditional/external-field closure, and stability-separation example together constitute the present claim; standard product closure and real-stability definitions are not claimed as new. We found no covering statement in the inspected sources, but an earlier special-class negative-association theorem could imply part of this result.

## Limitations
The graph class is cactus; multiple cycles may share vertices but cannot share edges. The argument fails to factor on general series-parallel graphs with overlapping cycles. We claim neither negative association for every graph nor an infinite-volume limit. Although the measures are CNA+, on a cyclic host they fail the more restrictive strongly Rayleigh condition; pairwise negativity alone would not establish the claimed CNA+ theorem. No independent priority review or independent mathematical audit has been performed.

## References
1. Heehyun Park, *The \(q<1\) Random-Cluster Model on Wired Trees: Uniqueness and Negative Dependence*, arXiv:2608.08565v1 (first public 2026-08-09), https://arxiv.org/html/2608.08565v1 .
2. Recep Altar Çiçeksiz and Mohan Ravichandran, *Negative Correlation for Forests and the \(q<1\) Random-Cluster Model*, arXiv:2610.00549v1 (first public 2026-09-30), https://arxiv.org/html/2610.00549v1 .
3. Grimmett and Winkler, *Negative association in uniform forests and connected graphs*, Random Structures & Algorithms 24 (2004), 444–460, cited for the general forest negative-dependence question; full text not inspected.
4. Borcea, Bränden and Liggett, *Negative dependence and the geometry of polynomials*, JAMS 22 (2009), 521–567, for strong Rayleigh and real stability.
