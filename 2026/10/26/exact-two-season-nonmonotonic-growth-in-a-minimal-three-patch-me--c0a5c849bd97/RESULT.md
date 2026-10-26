# Exact two-season nonmonotonic growth in a minimal three-patch metapopulation

## Finding
Consider the continuous-time, three-patch linear population equation \(\dot z(t)=(L+R(t/T))z(t)\) with a period-one environmental profile that switches between two equally long seasons. Let
\[
L=\begin{pmatrix}-12&0&2\\12&-2&0\\0&2&-2\end{pmatrix},\qquad
R_1=\operatorname{diag}(-4,8,10),\quad R_2=\operatorname{diag}(3,-5,-1).
\]
The fixed migration matrix \(L\) is irreducible, has nonnegative off-diagonal entries, and has zero column sums; all its edges point around a three-patch cycle. The season generators are \(A_i=L+R_i\), and the per-time principal Floquet growth exponent is
\[
\Lambda(T)=\frac1T\log\rho\!\left(e^{TA_2/2}e^{TA_1/2}\right),\qquad T>0.
\]
The exact strict inequality
\[
\boxed{\Lambda(2)>\Lambda(8)}
\]
holds. In particular, population growth is not generally increasing with environmental period even when migration is fixed in time and only **two** distinct environmental regimes occur. Both the number of patches and the number of regimes are minimal in the following sense: with one regime the exponent is period-independent; for any two-patch irreducible conservative migration matrix, the exponent is nondecreasing with period in the same class of piecewise-constant seasonal growth environments.

## Assumptions and scope
Population densities are nonnegative column vectors. The environmental profile repeats \(R_1\) during the first half of each period and \(R_2\) during the second half. Migration conserves total population, is independent of the environment and time, and is irreducible. No stochastic switching or density dependence is assumed. The assertion about two patches applies to any positive off-diagonal migration rates and any finite piecewise-continuous periodic diagonal growth-rate profile, by the symmetric-migration monotonicity result and approximation.

## Proof
**Step 1: remove scalar shifts.** Directly,
\[
A_1=\begin{pmatrix}-16&0&2\\12&6&0\\0&2&8\end{pmatrix},\qquad
A_2=\begin{pmatrix}-9&0&2\\12&-7&0\\0&2&-3\end{pmatrix}.
\]
Set \(B_1=A_1+16I\) and \(B_2=A_2+9I\); both are entrywise nonnegative. For any \(T>0\), define \(Q_T=e^{TB_2/2}e^{TB_1/2}\). The two exponential shifts yield
\[
\Lambda(T)=-\frac{25}{2}+\frac1T\log\rho(Q_T).
\]
Thus \(\Lambda(2)>\Lambda(8)\) is equivalent to \(\rho(Q_2)^4>\rho(Q_8)\).

**Step 2: exact spectral-radius certificate.** Fix \(v=(276,629,1000)^\mathsf T>0\), the positive integers \(a=778\cdot10^{11}\), \(b=356\cdot10^{53}\), and \(N=430\). The following two strict entrywise inequalities hold:
\[
Q_2v>av,\qquad Q_8v<bv.
\]
These assertions are certified using integer arithmetic, without floating-point decisions. Define \(S_N(M)=\sum_{k=0}^{N}M^k/k!\), \(J\) the all-ones three-by-three matrix, and \(\epsilon=10^{-12}\). For each \(M\) in \(\{B_1,B_2,4B_1,4B_2\}\), put \(r=\|M\|_\infty\). The verified integer inequality
\[
10^{12}\,r^{431}\cdot432<431!\,(432-r)
\]
proves \(0\le e^M-S_N(M)\le \epsilon J\) entrywise: sum the exponential tail and dominate each entry of \(M^k\) by \(r^k\). The included program constructs \(430!S_N(M)\) by integer-only Horner evaluation, and directly checks
\[
S_N(B_2)S_N(B_1)v>av,
\]
\[
\bigl(S_N(4B_2)+\epsilon J\bigr)\bigl(S_N(4B_1)+\epsilon J\bigr)v<bv.
\]
Because all matrices and \(v\) are nonnegative, these are valid lower and upper bounds on the respective exact exponentials. Their products are strictly positive, so the Collatz–Wielandt bounds yield \(\rho(Q_2)>a\) and \(\rho(Q_8)<b\). Finally the exact integer comparison \(a^4>b\) gives \(\rho(Q_2)^4>\rho(Q_8)\) as asserted.

**Step 3: sharp patch and regime counts.** One regime gives \(\Lambda(T)=s(L+R_1)\), the spectral abscissa of a constant matrix, independent of \(T\). One patch is scalar and likewise period-independent. For two patches, write the off-diagonal elements of \(L\) as \(\alpha,\beta>0\), so \(L=\bigl(\begin{smallmatrix}-\beta&\alpha\\\beta&-\alpha\end{smallmatrix}\bigr)\). A fixed positive diagonal similarity sends the two off-diagonal entries to \(\sqrt{\alpha\beta}\), while the resulting diagonal corrections are constant in time. This transforms the equation to one having the symmetric conservative migration matrix \(\bigl(\begin{smallmatrix}-\sqrt{\alpha\beta}&\sqrt{\alpha\beta}\\\sqrt{\alpha\beta}&-\sqrt{\alpha\beta}\end{smallmatrix}\bigr)\) and a modified diagonal seasonal growth matrix. The standard symmetric-dispersal monotonicity theorem implies that its principal Floquet exponent is nondecreasing with period; similarity does not change that exponent. Piecewise-constant profiles follow by approximating the coefficients with continuous periodic functions and taking pointwise limits of their fundamental matrices and spectral radii. Hence at least three patches and two seasons are necessary, and the displayed example attains both lower bounds.

## Verification
Run `python3 verify.py` with Python 3 and arbitrary-precision integer arithmetic. Successful completion prints `CERT_OK`. It constructs the shifted matrices, verifies column conservation for \(L\), checks four exponential-remainder inequalities by exact integers, evaluates all polynomial matrices using exact Horner arithmetic, checks the two strict spectral comparisons componentwise, and verifies \(a^4>b\). No numerical integration, floating-point approximation, or finite-sample inference is used in accepting the inequalities. Approximate values, solely for orientation, are \(\Lambda(2)\approx3.492981\) and \(\Lambda(8)\approx3.488470\).

## Relationship to prior work
Benaïm, Lobry, Sari, and Strickler (first arXiv posting 2023-11-08, arXiv:2311.04706) formulated the question of monotonicity in period for fixed, possibly asymmetric migration. Monmarché, Schreiber, and Strickler (arXiv:2408.11179) **already disproved the unrestricted monotonicity expectation** with a nonmonotone construction using three patches and three environmental regimes; their general asymptotic and comparison results are prior art. Their example does not itself imply the existence of a two-regime construction, as collapsing or removing one regime changes the monodromy. The present result contributes the two-regime exact arithmetic witness and the simultaneous minimal counts, not the first discovery of nonmonotonicity. Benaïm and coauthors' arXiv:2407.07553 explicitly recognizes the earlier counterexample. Related symmetric-dispersal theorems establish why two patches cannot supply such a counterexample.

## Limitations
The explicit witness concerns three patches, two equally long seasons, and one fixed directed cycle of migration. It proves a strict pairwise period reversal, not uniqueness of any optimal period or an all-parameter classification. The minimality claim concerns patch and regime counts in the specified conservative fixed-migration class, not minimal coefficient magnitudes. Independent validation and exhaustive publication-priority verification have not been performed.

## References
1. M. Benaïm, C. Lobry, T. Sari, and É. Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706 (initial version 2023-11-08), https://arxiv.org/abs/2311.04706.
2. P. Monmarché, S. J. Schreiber, and É. Strickler, *Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth: Slow- and Fast-Limit Approximations of Lyapunov Exponents for Periodic and Random Environments*, arXiv:2408.11179 (initial version 2024-08-20), https://arxiv.org/abs/2408.11179.
3. M. Benaïm, C. Lobry, T. Sari, and É. Strickler, *Dispersal-induced growth or decay in a time-periodic environment. The case of reducible migration matrices*, arXiv:2407.07553 (initial version 2024-07-10), https://arxiv.org/abs/2407.07553.
