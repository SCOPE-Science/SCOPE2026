# All-rank sharpness of the small-noise cumulant cutoff in bounded diffusions

## Finding
For every state dimension \(d\ge1\), time horizon \(T>0\), and symmetric positive-definite matrix \(\Sigma\in\mathbb R^{d\times d}\) with strictly positive entries, there exists a smooth, globally bounded-coefficient small-noise diffusion with independent Brownian observations for which, simultaneously for all ranks \(r\ge2\), all coordinate tuples \(i_1,\ldots,i_r\in\{1,\ldots,d\}\), and every \(0<t\le T\),
\[
\operatorname{cum}(X_{i_1,t}^{\epsilon},\ldots,X_{i_r,t}^{\epsilon}\mid\mathcal Y_t)
=\epsilon^{2r-2}t^{r-1}\sum_{\tau\in\mathcal T_r}
 \prod_{\{a,b\}\in E(\tau)}\Sigma_{i_ai_b}+O(\epsilon^{2r}).
\]
The sum is over all labelled trees on \(\{1,\ldots,r\}\). The leading coefficient is strictly positive in **every** tensor component. In dimension one with \(\Sigma=(1)\), the coefficient is \(r^{r-2}t^{r-1}\).

Therefore the general vanishing threshold \(k<2r-2\) for the coefficient of \(\epsilon^k\) in rank-\(r\) conditional cumulants cannot be raised, at any rank, even under globally bounded smooth coefficients. This is a sharpness statement for **cumulant rank**, not a lower bound for the number of ODE variables in a particular representation.

## Assumptions and scope
Fix \(d\ge1\), \(T>0\), and a real symmetric positive-definite \(\Sigma\) with \(\Sigma_{ij}>0\) for all indices. Let \(L\) be a real matrix satisfying \(LL^{\mathsf T}=\Sigma\); let \(V\) be standard \(d\)-dimensional Brownian motion and let \(W\) be an independent standard scalar Brownian motion. Choose \(\chi\in C_c^\infty(\mathbb R)\) satisfying \(\chi(x)=x\) on \([1/2,2]\). With \(X_0^\epsilon=(1,\ldots,1)\), define
\[
 dX_{i,t}^\epsilon=\epsilon\chi(X_{i,t}^\epsilon)\sum_{j=1}^d L_{ij}\,dV_{j,t},\qquad dY_t=dW_t.
\]
All drift/diffusion coefficients, their spatial derivatives of every order, and their parameter derivatives are bounded uniformly for \(|\epsilon|<1\); the observation covariance is the identity. The observation sigma-field \(\mathcal Y_t=\sigma(Y_s:0\le s\le t)\) is independent of the state, so conditional and ordinary cumulants coincide. The assertion concerns each fixed finite rank and time; it does not assert error bounds uniform as rank tends to infinity or uniform as \(t\downarrow0\).

## Proof
**1. A solvable comparison diffusion.** Let \(B=LV\). Define
\[
 Z_{i,t}^\epsilon=\exp\!\left(\epsilon B_i(t)-\frac12\epsilon^2t\Sigma_{ii}\right).
\]
The strong solution of \(dZ_{i,t}^\epsilon=\epsilon Z_{i,t}^\epsilon dB_i(t)\), \(Z_{i,0}^\epsilon=1\), agrees with \(X_{i,t}^\epsilon\) until the first coordinate of either process exits \([1/2,2]\), by pathwise uniqueness. For \(0\le s\le T\), an exit of \(Z\) requires a Gaussian supremum of order \(\epsilon^{-1}\), since the deterministic logarithmic correction is \(O(\epsilon^2)\). The Brownian reflection bound implies, for sufficiently small nonzero \(\epsilon\),
\[
 \Pr\left[\max_i\sup_{s\le T}|\log Z_{i,s}^\epsilon|\ge\log2\right]\le C\exp(-c/\epsilon^2),
\]
where \(C,c>0\) depend only on the fixed \(d,T,\Sigma\). For each fixed positive integer \(p\), the moments of \(\sup_{s\le T}|Z_{i,s}^\epsilon|\) stay uniformly bounded for small \(|\epsilon|\), by exponential Brownian maximum estimates; the same holds for \(X\) because \(\chi\) is bounded and the martingale integrands are bounded (Burkholder–Davis–Gundy). Cauchy–Schwarz and the exit bound therefore show that all fixed joint moments of \(X_t^\epsilon\) and \(Z_t^\epsilon\) differ by \(O(e^{-c'/\epsilon^2})\). Since a cumulant is a finite polynomial in joint moments, their fixed-rank cumulants differ by this same superpolynomial order. Thus their complete Taylor coefficients at \(\epsilon=0\) agree.

**2. Exact connected-graph formula.** For labelled positions \(a=1,\ldots,r\), write \(Z_a=Z_{i_a,t}^\epsilon\) and \(w_{ab}=\exp(\epsilon^2t\Sigma_{i_ai_b})-1\). For each nonempty subset \(A\subseteq\{1,\ldots,r\}\), the Gaussian moment-generating identity gives
\[
 \mathbb E\prod_{a\in A}Z_a
 =\exp\!\left(\epsilon^2t\sum_{\{a,b\}\subset A}\Sigma_{i_ai_b}\right)
 =\prod_{\{a,b\}\subset A}(1+w_{ab}).
\]
Expand each product over simple graphs on vertex set \(A\). The moment-to-cumulant identity,
\[
 \operatorname{cum}(Z_1,\ldots,Z_r)
 =\sum_{\pi\in\Pi_r}(-1)^{|\pi|-1}(|\pi|-1)!
 \prod_{A\in\pi}\mathbb E\prod_{a\in A}Z_a,
\]
retains precisely the connected simple graphs: for each graph the partition sum over coarsenings of its component partition is one if the graph is connected and zero otherwise. Consequently, **exactly for every real** \(\epsilon\),
\[
 \operatorname{cum}(Z_1,\ldots,Z_r)
 =\sum_{G\text{ connected on }[r]}\prod_{\{a,b\}\in E(G)}w_{ab}.
\]

**3. Lowest order and strict positivity.** Every connected graph on \(r\) labelled vertices has at least \(r-1\) edges; the connected graphs with exactly \(r-1\) edges are the labelled trees. Since \(w_{ab}=\epsilon^2t\Sigma_{i_ai_b}+O(\epsilon^4)\), their contributions give the displayed coefficient at order \(2r-2\), while every additional edge contributes at least two further powers of \(\epsilon\). Each tree weight is strictly positive by the entrywise positivity of \(\Sigma\). For \(d=1\) and \(\Sigma=(1)\), Cayley's labelled-tree count is \(r^{r-2}\), including the value one for \(r=2\). Transfer the coefficients from \(Z\) to the globally bounded-coefficient diffusion \(X\) by Step 1 and use observation independence to conclude.

## Verification
The standalone `verify_cumulant_towers.py` reproduces the coefficient in two independent finite calculations: exact rational moment–cumulant partition inversion, and Prüfer-code summation over all labelled trees. It passed 107 exact comparisons for ranks \(2\le r\le6\) in dimensions one through three, using positive and signed covariance examples; the scalar cases verify \(r^{r-2}\). The program checks finitely many instances and does not prove the theorem for all ranks; the preceding argument does.

## Relationship to prior work
Kurisaki (2026), arXiv:2610.21986v1, Theorem 4.6 proves the upper vanishing bound \(k<2r-2\) and the degreewise finite-tower cutoff, but the inspected main statements, examples and the unconditional-cumulant section do not supply the above simultaneous all-rank sharpness construction with bounded coefficients. Kurisaki (2026), arXiv:2609.18229v1, gives earlier finite recursions without this boundary example. The connected-graph cumulant expansion is a classical combinatorial identity; the contribution here is its explicit all-rank sharpness application within the smooth bounded-coefficient filtering framework, including a rigorous cutoff transfer. The proof does not claim that the connected-graph expansion itself is new.

## Limitations
The observation carries no information about the state; this establishes a universal obstruction but does not imply that the boundary is attained in every informative filtering model. Entrywise positive covariance is sufficient, not necessary, for strict positivity in all components. The result does not prove a lower bound on minimal filtering-recursion dimension, computational complexity, or the optimality of the source's entire equation hierarchy. Equivalence to an application hidden in broader Gaussian-diagram or cumulant literature remains possible; independent validation has not been performed.

## References
- M. Kurisaki, *Finite Cumulant Towers for Small-System-Noise Expansions in Nonlinear Filtering*, arXiv:2610.21986v1 (first submitted 2026-10-15), especially Theorem 4.6, Section 2, and Section 7. https://arxiv.org/html/2610.21986v1
- M. Kurisaki, *Finite-Dimensional Recursions for Small-Noise Expansions in Nonlinear Filtering*, arXiv:2609.18229v1 (first submitted 2026-09-16). https://arxiv.org/html/2609.18229v1
- G. Peccati and M. S. Taqqu, *Wiener Chaos: Moments, Cumulants and Diagrams* (2011), cited in the first paper for connected pairing-diagram machinery.
