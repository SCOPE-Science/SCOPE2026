# Directed common-ancestor hypergraphs determine joint jumps of multitype inverse-Gaussian subordinators

## Finding

Fix an integer \(d\ge1\), a nonsingular \(M\)-matrix \(B\in\mathbb R^{d\times d}\), a vector \(\eta\in(0,\infty)^d\), and a time \(t>0\). Consider the multitype inverse-Gaussian subordinator \(Z\) defined in Wang–Xu–Zhu (2026) by
\[
\mathbb E\exp(-\langle u,Z_t\rangle)=\exp[-t\,\eta^{\mathsf T}z(u)],\qquad
B^{\mathsf T}z(u)+\tfrac12 z(u)^{\circ2}=u,\quad u\in\mathbb R_+^d,
\]
where \(z(u)\) is the unique nonnegative solution. Draw an arrow \(i\to j\) precisely when \(i\ne j\) and \(B_{ji}<0\); count every vertex as reachable from itself. Let \(i\leadsto j\) mean directed reachability.

**Joint-jump hypergraph theorem.** For every \(r\ge2\) and every sequence of indices \(j_1,\ldots,j_r\in\{1,\ldots,d\}\), possibly with repetitions, the joint cumulant satisfies
\[
\kappa(Z_{t,j_1},\ldots,Z_{t,j_r})>0
\quad\Longleftrightarrow\quad
\exists i\in\{1,\ldots,d\}:\ i\leadsto j_a\ \text{for every }a.
\]
Otherwise the cumulant equals exactly zero; none of these cumulants is negative. If \(\nu\) is the Lévy measure of \(Z\), then for any *distinct* target indices \(j_1,\ldots,j_r\) with \(r\ge2\),
\[
\nu\{x\in\mathbb R_+^d: x_{j_1}>0,\ldots,x_{j_r}>0\}>0
\quad\Longleftrightarrow\quad
\exists i:\ i\leadsto j_1,\ldots,j_r.
\]
Thus the family of coordinate subsets that can jump together is *exactly* the family of subsets with a common directed ancestor.

**Independence classification.** For disjoint nonempty groups \(A,D\subseteq\{1,\ldots,d\}\), the coordinate Lévy processes \((Z_{t,j})_{j\in A}\) and \((Z_{t,k})_{k\in D}\) are independent if and only if no vertex reaches both a coordinate of \(A\) and a coordinate of \(D\). In particular, all \(d\) coordinates are mutually independent if and only if \(B\) is diagonal.

**Strict higher-order obstruction.** There exist six-type examples in which the three coordinates \(4,5,6\) are positively correlated in every pair, yet their three-way mixed cumulant is zero and their Lévy measure never jumps simultaneously in all three. This shows that the pairwise dependence graph does not determine the simultaneous-jump hypergraph.

## Assumptions and scope

A nonsingular \(M\)-matrix means \(B=sI-C\), with \(C\ge0\), \(s>\rho(C)\). This permits reducible matrices, zero interactions, arbitrary positive diagonal entries, and directed cycles. Positivity of every immigration coordinate \(\eta_i\) is essential to the unweighted reachability criterion. The time \(t\) is strictly positive. The theorem is about the particular coupled inverse-Gaussian law defined by the displayed quadratic Laplace exponent, not all distributions bearing the name “multivariate inverse Gaussian.”

For a sequence of *labeled positions* \(S=\{1,\ldots,r\}\), write \(S_1\) for a nonempty proper subset of positions, even when some target indices coincide. Put \(J=(B^{\mathsf T})^{-1}\) and define vectors \(H(S)\in\mathbb R_+^d\) by
\[
H_i(\{a\})=J_{i,j_a},\qquad
H_i(S)=\frac12\sum_{\ell=1}^{d}J_{i\ell}
\sum_{\varnothing\ne S_1\subsetneq S}
H_\ell(S_1)H_\ell(S\setminus S_1)\quad(|S|\ge2).
\]
Then all cumulants have the *finite exact recursion*
\[
\boxed{\ \kappa(Z_{t,j_1},\ldots,Z_{t,j_r})
=t\sum_{i=1}^d\eta_i H_i(S),\quad r\ge1.\ }
\]
The recurrence takes finitely many matrix multiplications and subset splits at every fixed order. The condition \(r\ge2\) is only for simultaneous-jump and joint-dependence claims; for \(r=1\), it gives the mean.

## Proof

**Step 1: analytic derivatives.** As \(B^{\mathsf T}\) is invertible and \(z(0)=0\), the real-analytic implicit-function theorem gives a unique analytic branch near \(u=0\). Multiplication of the quadratic equation by \(J\) yields
\[
z(u)=Ju-\tfrac12J\bigl(z(u)^{\circ2}\bigr).
\]
For labeled positions \(S\) and \(|S|\ge1\), the product rule applied to this identity gives
\[
H_i(S)=(-1)^{|S|-1}
\left.\frac{\partial^{|S|}z_i}{\prod_{a\in S}\partial u_{j_a}}\right|_{u=0},
\]
with the displayed recurrence for \(|S|\ge2\); the factor \(1/2\) compensates for the two orderings of a bipartition. Differentiating \(\log\mathbb E[e^{-\langle u,Z_t\rangle}]=-t\eta^{\mathsf T}z(u)\) gives the cumulant formula. All needed cumulants are finite: derivatives of the nonnegative Laplace transform at the origin give finite moments by monotone convergence, and the analytic branch supplies finite derivatives of every order. Alternatively, the subordinator's Lévy–Khintchine representation and the analytic exponent give these finite mixed moments.

**Step 2: directed paths encode strictly positive inverse entries.** With \(B=sI-C\),
\[
J=\frac1s\sum_{m=0}^{\infty}(C^{\mathsf T}/s)^m.
\]
All entries are nonnegative, \(J_{ii}\ge 1/s>0\), and \(J_{ij}>0\) exactly when there is a directed path \(i\leadsto j\) in the arrow convention above. The sum converges because \(\rho(C)<s\).

**Step 3: exact support of every derivative.** We prove by induction on \(|S|\) the stronger statement
\[
H_i(S)>0\quad\Longleftrightarrow\quad
J_{i,j_a}>0\ \text{for all }a\in S.
\]
For \(|S|=1\), this is the definition. If a summand in the recursion is positive, then \(J_{i\ell}>0\) and both recursively defined factors are positive. The induction hypothesis provides paths from \(\ell\) to every target; concatenation gives paths from \(i\) to every target. Conversely, if \(i\) reaches each target, choose the inner summation term \(\ell=i\) and any nonempty proper split. By induction both factors are strictly positive, and the factor \(J_{ii}>0\) makes that term strictly positive. This proves the biconditional for every order. Since each \(\eta_i>0\), summing the nonnegative \(H_i(S)\) proves the cumulant sign/support theorem.

**Step 4: jump support and independence.** For a nonnegative multivariate Lévy process with Lévy measure \(\nu\), every mixed cumulant of order \(r\ge2\) is
\[
\kappa(Z_{t,j_1},\ldots,Z_{t,j_r})
=t\int_{\mathbb R_+^d\setminus\{0\}}
\prod_{a=1}^r x_{j_a}\,\nu(dx).
\]
The integral is finite by Step 1. Since its integrand is strictly positive exactly where all named coordinates are positive, Step 3 yields the claimed jump-support classification. For two disjoint coordinate groups, vanishing of all cross covariances is equivalent to \(\nu\)-almost every jump being supported in one group or the other (and possibly other unobserved coordinates). The multivariate Lévy–Khintchine exponent then splits between those two projections; their Lévy subprocesses are independent. Conversely, independence forces every cross covariance to vanish and hence forbids a common ancestor. Finally, any off-diagonal negative entry of \(B\) creates an arrow \(i\to j\), and \(i\) is a common ancestor of \(i,j\); the two coordinates are dependent. When \(B\) is diagonal, no different coordinates share an ancestor and all are mutually independent.

**Step 5: explicit six-type obstruction.** Set \(d=6\), \(\eta=(1,1,1,1,1,1)^{\mathsf T}\), \(B=I-C\), with the only positive entries of \(C\) equal to \(1/5\) at
\[
C_{4,1}=C_{5,1}=C_{4,2}=C_{6,2}=C_{5,3}=C_{6,3}=\tfrac15.
\]
Here \(C^2=0\), so \(B\) is nonsingular \(M\), and \(J=I+C^{\mathsf T}\). Types \(4,5\) share ancestor \(1\); types \(4,6\) share ancestor \(2\); types \(5,6\) share ancestor \(3\). No type reaches all three. Exact evaluation of the recurrence gives, for every \(t>0\),
\[
\operatorname{Cov}(Z_{t,4},Z_{t,5})
=\operatorname{Cov}(Z_{t,4},Z_{t,6})
=\operatorname{Cov}(Z_{t,5},Z_{t,6})=t/25,
\qquad \kappa(Z_{t,4},Z_{t,5},Z_{t,6})=0.
\]
Hence \(\nu\{x_4>0,x_5>0,x_6>0\}=0\) even though all three pairwise simultaneous-jump sets have positive measure. A further check gives \(\kappa(Z_{t,1},Z_{t,4},Z_{t,5})=3t/25>0\), so the third-order vanishing is structural, not due to a general symmetry.

## Verification

A reproducible, standard-library-only Python script `cumulant_checker.py` verifies the exact inverse identity, the recursion and its reachability criterion for every ordered target sequence of length \(1\) through \(4\) in the six-type construction. It independently constructs the formal Taylor coefficients of the nonlinear inverse and matches them against the derivative recursion through degree \(4\). It also checks the rational covariance and third- and fourth-order values stated above. Its accompanying `checker_output.txt` records 1,588 exact assertions. These finite checks corroborate, but do not replace, the unrestricted proof in Steps 1–4.

For arbitrary \(B\), pair covariance can also be evaluated without higher derivatives:
\[
\operatorname{Cov}(Z_{t,j},Z_{t,k})
=t\sum_{\ell=1}^d
\biggl(\sum_{i=1}^d\eta_iJ_{i\ell}\biggr)J_{\ell j}J_{\ell k}.
\]
Every term is nonnegative, so numerical approximation need not be used to determine the exact zero pattern.

## Relationship to prior work

Wang, Xu and Zhu (arXiv:2610.10525, first submitted October 7, 2026) introduce the coupled multitype inverse-Gaussian subordinator, establish its quadratic Laplace exponent and convergence from near-critical Hawkes systems, and note independence for diagonal \(B\). Those facts are premises, not claimed as new. The present theorem extracts the complete higher-order mixed-cumulant support and simultaneous-jump hypergraph for **all** nonsingular \(M\)-matrices, including reducible matrices, and proves the reverse direction of full coordinate independence.

Jovanović, Hertz and Rotter (arXiv:1409.5353, 2015) give a rooted-tree interpretation of integrated cumulants for **fixed stable Hawkes point processes**. Their integrated motif criterion is a strong structural antecedent: joint cumulants reflect common branching ancestors. Privault (arXiv:2012.07256, 2020) gives Hawkes cumulant recursions; Achab et al. (arXiv:1607.06333, 2017) employ second/third Hawkes integrated cumulants for causal inference. These do not explicitly supply the all-order quadratic inverse recursion or the Lévy jump-support equivalence for the *new limiting inverse-Gaussian subordinator*. Transfer from fixed-parameter Hawkes cumulants to the nearly critical scaling limit would require moment-level control not contained in weak convergence alone. The underlying branching and nonnegative-motif ideas are therefore attributed to the earlier literature, rather than advertised as invented here.

Chaumont and Marolleau (arXiv:1912.10474, 2019) provide general first-passage field inversion theory, which implies existence of the inverse-Laplace representation. Their available abstract does not settle the specific all-order support classification; the full text was not accessible in this inspection, leaving a clear priority risk.

## Limitations

The result is specific to the quadratic Brownian/inverse-Gaussian exponent, fixed finite dimension, positive immigration on *every* type, and \(t>0\). With zero immigration coordinates, reachability must be weighted by the active immigrant set; the stated unconditional graph criterion would no longer hold. Neither the full density nor the numerical magnitudes of arbitrary joint jumps are derived, only exact positivity/zero support and a finite cumulant recurrence. Higher-order signs do not provide a full independence decomposition beyond the disjoint-group result proved here. Historical priority cannot be certified by a finite literature search; the broader first-passage and Hawkes graph-motif literature may contain equivalent consequences. There has been no independent mathematical audit.

## References

1. Y. Wang, W. Xu, L. Zhu, *A Hawkes Microfoundation for Multitype Inverse Gaussian Subordinators*, arXiv:2610.10525 (initial submission October 7, 2026), Section 2 and Eq. (10)–(11). https://arxiv.org/abs/2610.10525
2. S. Jovanović, J. Hertz, S. Rotter, *Cumulants of Hawkes point processes*, arXiv:1409.5353 (2015), Section IV, Eqs. (44)–(53). https://arxiv.org/abs/1409.5353
3. N. Privault, *Recursive computation of the Hawkes cumulants*, arXiv:2012.07256 (2020). https://arxiv.org/abs/2012.07256
4. M. Achab, E. Bacry, S. Gaiffas, I. Mastromatteo, J.-F. Muzy, *Uncovering Causality from Multivariate Hawkes Integrated Cumulants*, arXiv:1607.06333 (2017). https://arxiv.org/abs/1607.06333
5. L. Chaumont, M. Marolleau, *Fluctuation theory for spectrally positive additive Lévy fields*, arXiv:1912.10474 (2019). https://arxiv.org/abs/1912.10474
