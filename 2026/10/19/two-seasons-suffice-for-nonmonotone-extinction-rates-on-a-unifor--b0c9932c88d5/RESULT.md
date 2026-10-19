# Two seasons suffice for nonmonotone extinction rates on a uniform directed cycle

## Finding

There is a fixed, conservative, *uniform* clockwise migration network on four patches and an equal-duration *two*-season environment for which every patch is an isolated sink, but the principal population growth exponent is not monotone in the environmental period. Explicitly, for the system and coefficients below,
\[
\boxed{\Lambda(2/5)<\Lambda(8/5)>\Lambda(16/5).}
\]
Both strict comparisons are rigorously established by rational arithmetic, rather than inferred from an eigenvalue plot. Since an environment with just one seasonal state makes the period immaterial, two states are the minimum possible number of distinct seasonal states for this phenomenon. This does **not** assert the minimal number of habitat patches.

## Assumptions and scope

Let \(x(t)\in\mathbb R_{\ge0}^{4}\) describe four patch populations. The clockwise cyclic permutation is defined by \(Pe_1=e_2\), \(Pe_2=e_3\), \(Pe_3=e_4\), and \(Pe_4=e_1\). Migration is time-independent, conservative, and uniform: \(L=6(P-I)\). During the first and second halves of each environmental period \(T>0\), respectively, the growth-rate vectors are
\[
r^{(1)}=(1,0,2,-8),\qquad r^{(2)}=(-2,-10,-3,-1).
\]
Thus, with column population vectors, the two season generators are
\[
A=\begin{pmatrix}-5&0&0&6\\6&-6&0&0\\0&6&-4&0\\0&0&6&-14\end{pmatrix},\qquad
B=\begin{pmatrix}-8&0&0&6\\6&-16&0&0\\0&6&-9&0\\0&0&6&-7\end{pmatrix}.
\]
The monodromy for one period is \(M(T)=e^{TB/2}e^{TA/2}\). Its entries are strictly positive for \(T>0\); Perron–Frobenius theory therefore identifies the population growth exponent as
\[
\Lambda(T)=\frac{1}{T}\log\rho(M(T)).
\]
The four *isolated* patch average growth rates are \((-1/2,-5,-1/2,-9/2)\), all strictly negative. No assertion is made about population growth for arbitrary periods, or about nonlinear dynamics.

## Proof

**1. Exact positive reduction.** Define \(A_+=A+16I\) and \(B_+=B+16I\), which have entrywise nonnegative integer coefficients:
\[
A_+=\begin{pmatrix}11&0&0&6\\6&10&0&0\\0&6&12&0\\0&0&6&2\end{pmatrix},\qquad
B_+=\begin{pmatrix}8&0&0&6\\6&0&0&0\\0&6&7&0\\0&0&6&9\end{pmatrix}.
\]
Put \(H(T)=e^{TB_+/2}e^{TA_+/2}\). Scalar shifts commute with each generator, so \(H(T)=e^{16T}M(T)\) and
\[
\Lambda(T)=\frac{1}{T}\log\rho(H(T))-16.
\]

**2. Completely rational exponential enclosures.** For any entrywise nonnegative rational \(4\times4\) matrix \(X\), set \(r=\max_i\sum_jX_{ij}\) and \(S_{80}(X)=\sum_{k=0}^{80}X^k/k!\). When \(r<82\), the entrywise inequality
\[
0\le e^X-S_{80}(X)\le\epsilon(X)J,\qquad
\epsilon(X)=\frac{r^{81}}{81!\,(1-r/82)}
\]
holds, with \(J\) the all-ones matrix. Indeed, each entry of \(X^k\) is at most \(r^k\); for \(k\ge81\) the ratio of successive scalar tail terms is at most \(r/82<1\), which gives this geometric upper bound. For \(X=TA_+/2\) and \(X=TB_+/2\) at the three periods \(T\in\{2/5,8/5,16/5\}\), the maximal row sum is at most \(144/5<82\).

Use \(S_{80}\) as a lower bound, \(S_{80}+\epsilon J\) as an upper bound, and multiply the respective nonnegative bounds in season order to obtain rational matrices \(H_-(T)\le H(T)\le H_+(T)\) entrywise.

**3. Certified Perron bounds.** For any positive rational vector \(q\), the Collatz–Wielandt estimates and entrywise monotonicity yield
\[
\min_i\frac{(H_-(T)q)_i}{q_i}\le\rho(H(T))\le
\max_i\frac{(H_+(T)q)_i}{q_i}.
\]
The exact-rational script `verify_two_season.py` evaluates these inequalities with, respectively,
\[
\begin{array}{c|c}
T&q\\\hline
2/5&(31163,14916,23238,30684)\\
8/5&(36440,17177,17764,28619)\\
16/5&(36320,17105,17882,28692)
\end{array}
\]
and proves the strict **integer** bounds
\[
\rho(H(2/5))<263,\qquad
\rho(H(8/5))>7{,}500{,}000{,}000,\qquad
\rho(H(16/5))<55{,}000{,}000{,}000{,}000{,}000{,}000.
\]
The script uses rational matrices and factorials only; decimal printouts are descriptive and play no part in its assertions.

**4. Comparison at the three periods.** The exact integer relations
\[
263^4=4{,}784{,}350{,}561<7{,}500{,}000{,}000
\]
and
\[
(7{,}500{,}000{,}000)^2=56{,}250{,}000{,}000{,}000{,}000{,}000>
55{,}000{,}000{,}000{,}000{,}000{,}000
\]
show \(\rho(H(8/5))>\rho(H(2/5))^4\) and \(\rho(H(8/5))^2>\rho(H(16/5))\). Because \((8/5)/(2/5)=4\) and \((16/5)/(8/5)=2\), taking logarithms, dividing by the respective periods, and canceling the common shift \(-16\) proves the stated strict inequalities for \(\Lambda\). Continuous dependence of matrix exponentials and their Perron eigenvalues on \(T>0\) ensures an interior maximizer on \([2/5,16/5]\). All patch-average sink conditions were verified above. To certify actual extinction (not merely negative isolated-patch means) at the three sampled periods, the script also proves that the degree-80 **scalar** Taylor lower sum \(\sum_{k=0}^{80}(16T)^k/k!\) exceeds, respectively, the rational Perron upper thresholds \(263\), \(8{,}000{,}000{,}000\), and \(55{,}000{,}000{,}000{,}000{,}000{,}000\). Since \(e^{16T}\) is strictly larger than this lower sum and \(\rho(H(T))\) is smaller than its threshold, \(\Lambda(T)<0\) at all three sampled periods.

## Verification

Run `python3 verify_two_season.py` using Python 3 and the standard library. Every matrix operation uses `fractions.Fraction`; the program builds degree-80 Taylor polynomial matrices, explicit rational tail bounds, positive-vector Perron bounds, and asserts the decisive integer comparisons and the three scalar exponential lower bounds. It exits with an error if a bound fails. The certificate proves strict infinite-series inequalities for this exact model; it is not a finite numerical approximation.

## Relationship to prior work

Benaïm–Lobry–Sari–Strickler (arXiv:2311.04706; public 2023-11-08) posed monotonicity questions for the period dependence under fixed nonsymmetric migration. **The broad monotonicity conjecture has already been disproved**: Monmarché–Schreiber–Strickler (arXiv:2408.11179, Section 4.2, Proposition 3 and Figure 4) present a uniform directed *three*-patch cycle with *three* distinct seasonal environments exhibiting nonmonotonicity. The follow-up arXiv:2407.07553 explicitly acknowledges that counterexample in its introduction. Thus the present finding is **not** a new general counterexample to that already-refuted conjecture. Its independently checked distinction is that **two** equally long seasons suffice (with four patches, uniform time-independent migration, all four isolated patches sinks), together with an exact rational proof at three explicit periods. The cited works provide a general Floquet framework and asymptotic expansions; the inspected statements do not entail this two-environment witness.

## Limitations

This is one explicit four-patch construction, not a classification of all two-season systems or proof that four patches are necessary. It proves nonmonotonicity of the growth/extinction **rate**, not population persistence for any specified period; the exhibited rates at the test periods are negative. The switching sequence is deterministic and the patch graph is a directed cycle with equal rates. Although strict inequalities imply perturbative robustness, no global period profile is claimed. Novelty is assessed against the inspected literature and research indices, not guaranteed against unindexed examples or inaccessible variants; independent validation has not been performed.

## References

1. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *When can a population spreading across sink habitats persist?*, arXiv:2311.04706, first posted 2023-11-08. https://arxiv.org/abs/2311.04706
2. P. Monmarché, S. J. Schreiber, E. Strickler, *Impacts of Tempo and Mode of Environmental Fluctuations on Population Growth: Slow- and Fast-Limit Approximations of Lyapunov Exponents for Periodic and Random Environments*, arXiv:2408.11179, first posted 2024-08-20, particularly Section 4.2 and Figure 4. https://arxiv.org/html/2408.11179v1
3. M. Benaïm, C. Lobry, T. Sari, E. Strickler, *Dispersal-induced growth or decay in a time-periodic environment. The case of reducible migration matrices*, arXiv:2407.07553, first posted 2024-07-10, particularly the introduction. https://arxiv.org/html/2407.07553v2
