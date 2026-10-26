# Uniform BPR-equilibrium discrepancy, sharp high-demand rate, and eventual regime stabilization

## Finding
Let \(R\) be a finite nonempty resource set and \(H\) a finite nonempty commodity set. Each commodity \(h\) has a finite nonempty set \(S_h\) of nonempty subsets of \(R\) as strategies. Resource costs are
\[
c_r(u)=a_r+b_r u^p,\quad p\in\{1,2,\ldots\},\quad a_r\ge0,\quad b_r>0.
\]
For a nonnegative demand vector \(\mu\), denote the unique aggregate Wardrop resource load by \(X(\mu)\) and the unique load in the homogeneous comparison game with costs \(c^0_r(u)=b_r u^p\) by \(X_0(\mu)\). Define \(q=(p+1)/p\), \(b_*=\min_r b_r\), and \(C=(\|a\|_q/b_*)^{1/p}\). Then **uniformly over all demand vectors**,
\[
\|X(\mu)-X_0(\mu)\|_{p+1}\le C. \tag{1}
\]
For every nonzero fixed direction \(d\ge0\), \(X_0(td)=tX_0(d)\) for all \(t>0\), and the exact set of minimum-cost strategies for every commodity at \(td\) eventually stays constant as \(t\) increases. This latter assertion allows degenerate cost ties; it is not a claim that positive-flow path supports are unique.

For **singleton games**, i.e. each strategy is one resource, put \(R_+(d)=\bigcup_{h:d_h>0}S_h\), identifying singleton sets with their resources, and \(\eta=\min_{r\in R_+(d)}X_{0,r}(d)\). Then \(\eta>0\), and for all \(t>0\) satisfying \(t\ge2C/\eta\),
\[
\|X(td)-tX_0(d)\|_2\le \frac{\|a\|_2}{p b_*(\eta/2)^{p-1}}t^{1-p}. \tag{2}
\]
The exponent \(1-p\) cannot be improved in general, already for a single commodity on two parallel links.

## Assumptions and scope
The number of resources, commodities, and strategies is arbitrary but finite. Costs are separable and share one positive integer exponent. Strategy cost is the sum of its resource costs, and each commodity chooses only minimum-cost available strategies at Wardrop equilibrium. Every demand component is nonnegative. The global bound and eventual minimum-cost-strategy stabilization hold for **all** such finite congestion games; the sharper rate (2) is restricted to singleton games. All norms are ordinary finite-dimensional \(\ell^s\) norms on resource coordinates. Homogeneous loads scale linearly only along proportional demand rays.

## Proof
**Existence and uniqueness of aggregate loads.** Let \(\mathcal X(\mu)\) be the convex compact polytope of resource loads induced by nonnegative strategy flows summing to \(\mu_h\) for each commodity. The Beckmann characterization identifies Wardrop resource loads with minimizers on \(\mathcal X(\mu)\) of
\[
\Psi_a(x)=\sum_{r\in R}\left(a_rx_r+\frac{b_r}{p+1}x_r^{p+1}\right).
\]
Strict convexity of every \(x_r^{p+1}\) on nonnegative loads ensures a unique minimizing load vector, although individual strategy flows may not be unique. The homogeneous minimizer is the unique minimizer of \(\Psi_0(x)=\sum_r b_rx_r^{p+1}/(p+1)\) on the same feasible polytope.

**Global uniform perturbation bound.** Write \(x=X(\mu)\), \(y=X_0(\mu)\), \(\Delta=x-y\). First-order variational inequalities give
\[
\langle a+bx^p,y-x\rangle\ge0,\qquad \langle by^p,x-y\rangle\ge0,
\]
where powers and products are componentwise. Subtracting yields
\[
\sum_r b_r(x_r^p-y_r^p)(x_r-y_r)\le-\langle a,\Delta\rangle\le \|a\|_q\|\Delta\|_{p+1}.
\]
For any nonnegative \(u,v\) and \(p\ge1\), superadditivity \((v+s)^p\ge v^p+s^p\) shows
\[
(u^p-v^p)(u-v)\ge |u-v|^{p+1}.
\]
Consequently \(b_*\|\Delta\|_{p+1}^{p+1}\le\|a\|_q\|\Delta\|_{p+1}\). Canceling the norm when nonzero proves (1), including at zero demand. This is independent of topology and demand magnitudes.

**Homogeneous scaling and sharp singleton rate.** Rescale feasible strategy flows to obtain \(\mathcal X(td)=t\mathcal X(d)\) and \(\Psi_0(tx)=t^{p+1}\Psi_0(x)\); uniqueness gives \(X_0(td)=tX_0(d)\). In the homogeneous singleton game, every resource available to a positive-demand commodity has positive equilibrium load: otherwise its zero cost would be strictly smaller than the positive cost of any resource actually used by that commodity. Thus \(\eta>0\).

Set \(z_t=X(td)/t\), \(z_0=X_0(d)\). They minimize, respectively, \(\Psi_0(z)+t^{-p}\langle a,z\rangle\) and \(\Psi_0(z)\) on \(\mathcal X(d)\). Bound (1) gives \(\|z_t-z_0\|_{p+1}\le C/t\). If \(t\ge2C/\eta\), all coordinates in \(R_+(d)\) of both \(z_t,z_0\) are at least \(\eta/2\); the other coordinates are identically zero. Applying the two variational inequalities and the mean-value theorem on positive coordinates yields
\[
pb_*(\eta/2)^{p-1}\|z_t-z_0\|_2^2\le t^{-p}\|a\|_2\|z_t-z_0\|_2.
\]
Thus \(\|z_t-z_0\|_2\le\|a\|_2t^{-p}/[pb_*(\eta/2)^{p-1}]\), and multiplication by \(t\) gives (2).

**Rate sharpness.** For two available links with costs \(u^p\) and \(1+u^p\), the homogeneous equilibrium gives equal loads \(t/2\). For \(t>1\), both links have positive Wardrop load, written \(x_1=t/2+\delta_t\), \(x_2=t/2-\delta_t\), where \(\delta_t>0\) uniquely solves
\[
(t/2+\delta_t)^p-(t/2-\delta_t)^p=1.
\]
Since \(\delta_t=o(t)\) and the mean-value theorem yields \(1=2p(t/2)^{p-1}\delta_t(1+o(1))\),
\[
\delta_t\sim\frac{2^{p-2}}p t^{1-p}.
\]
The exponent in (2) is therefore optimal for all integer exponents \(p\ge1\). In the standard fourth-power case the exact equation is \(t^3\delta_t+4t\delta_t^3=1\), yielding \(\delta_t=t^{-3}+O(t^{-11})\).

**Eventual active-regime stabilization.** Fix any \(d\ge0\). Introduce finite strategy-flow variables \(f_{hs}\), resource-load variables \(x_r\), and minimum-strategy-cost variables \(\lambda_h\). The conditions
\[
 f_{hs}\ge0,\quad \sum_{s\in S_h}f_{hs}=td_h,\quad x_r=\sum_{h,s:r\in s}f_{hs},
\]
\[
 c_s(x)-\lambda_h\ge0,\quad f_{hs}[c_s(x)-\lambda_h]=0\quad(h,s),
\]
with \(c_s(x)=\sum_{r\in s}(a_r+b_rx_r^p)\), are polynomial equalities and inequalities in the unknowns and \(t\). The resulting set is semialgebraic; its projection by the Tarski–Seidenberg theorem is semialgebraic. For each commodity-strategy pair \((h,s)\), add the equality \(c_s(x)=\lambda_h\). Its projection to the positive \(t\)-axis is therefore semialgebraic. Existence and uniqueness of the equilibrium resource loads and hence \(\lambda_h=\min_{s\in S_h}c_s(X(td))\) make the projected set exactly the demands at which \(s\) is a minimum-cost strategy. A semialgebraic subset of the real line has finitely many connected components, so each such membership indicator is constant beyond a finite threshold. Finiteness of all \((h,s)\) gives one common threshold. This proves eventual active-regime stabilization without assuming generic strict inequalities. It does **not** prove that complete higher-dimensional regime boundaries stay a bounded Euclidean distance from straight lines.

## Verification
The standalone program `verify.py` independently computes two-link Wardrop solutions for several exponents and demands, checks the demand-uniform norm bound, tests the fundamental scalar monotonicity inequality on a finite grid, and tests the exact fourth-power cubic for its high-demand asymptotic. The analytical variational and semialgebraic proofs, not these finite tests, establish the universal assertions. Execute `python verify.py` with SciPy installed.

## Relationship to prior work
Cominetti, Dose and Scarsini (2023/2024, arXiv:2308.00434) prove monotonicity of singleton equilibrium resource loads, classify cost-order regions, and explicitly raise a conjecture concerning the asymptotic geometry of BPR active-regime boundaries; see especially §6. Their Theorem 12(c) already treats straight hyperplanes separating certain *subregions within fixed cost-order classes*, which is acknowledged and is not claimed here. The present result is distinct: it gives a **demand-uniform quantitative comparison with a homogeneous benchmark**, the exact high-demand rate and its optimal exponent, and the **eventual nonrecurrence of the entire minimum-cost active regime along each fixed proportional ray**. The latter is weaker than their full multidimensional geometric conjecture. Cominetti, Dose and Scarsini (2021) prove a finite-breakpoint result for affine single-commodity routing, and exhibit general smooth-cost examples with infinitely many transitions; this does not imply the polynomial multi-commodity statement. Their 2023 phase-transition work establishes differentiability and slope comparisons but does not assert the present universal quantitative bounds or polynomial stabilization. All uses of Beckmann convexity, scalar monotonicity and Tarski–Seidenberg are classical ingredients, not novel mathematical tools.

## Limitations
All resource costs must have the *same integer monomial exponent* and strictly positive leading coefficient. The sharp ray rate relies on singleton strategies and a fixed nonzero direction; its constant depends on the smallest limiting positive load and need not be uniform over demand directions. The method does not bound the number or location of active-regime changes effectively, distinguish zero-flow shortest strategies, establish a global asymptote of every multidimensional regime boundary, or apply to arbitrary non-polynomial smooth costs. Priority in the larger variational-inequality and semialgebraic-optimization literature may affect claims of novelty; no independent external review has occurred.

## References
1. R. Cominetti, V. Dose, M. Scarsini, “Monotonicity of Equilibria in Nonatomic Congestion Games,” arXiv:2308.00434v1 (public August 1, 2023), version 2 January 7, 2024. https://arxiv.org/html/2308.00434v2
2. R. Cominetti, V. Dose, M. Scarsini, “Phase Transitions of the Price-of-Anarchy Function in Multi-Commodity Routing Games,” arXiv:2305.03459v1 (May 5, 2023), Transportation Research Part B (2024). https://arxiv.org/abs/2305.03459
3. R. Cominetti, V. Dose, M. Scarsini, “The Price of Anarchy in Routing Games as a Function of the Demand,” Mathematical Programming, published September 8, 2021, DOI:10.1007/s10107-021-01701-7. https://link.springer.com/article/10.1007/s10107-021-01701-7
4. M. J. Beckmann, C. B. McGuire, C. B. Winsten, *Studies in the Economics of Transportation*, Yale University Press (1956). Classical potential formulation.
5. Tarski–Seidenberg theorem, standard semialgebraic projection result; no novel foundational claim is made.
