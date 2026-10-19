# Sharp reciprocal-ancestor constant for Carleson-packed averaging kernels

## Finding

Let \((X,\Sigma,\nu)\) be a measure space and \(\mathcal F\) a finite or countable **nested** family of distinct measurable sets, each with strictly positive finite measure. Nested means that for every two members \(P,Q\), either they are disjoint or one is contained in the other. Suppose that, for a given real \(\Lambda\ge1\),
\[
\sum_{Q\in\mathcal F:\,Q\subseteq\Omega}\nu(Q)
\le \Lambda\nu(\Omega)
\quad\text{for every measurable }\Omega\subseteq X.
\]
For \(S\in\mathcal F\) put
\[
\mathcal K_{\mathcal F}(S)=\sum_{P\in\mathcal F:\,P\supseteq S}\frac{1}{\nu(P)}.
\]
Then the **optimal universal constant**, with no restrictions on atoms or on the geometry of the nested family, is
\[
\boxed{\ \nu(S)\mathcal K_{\mathcal F}(S)\le C_*(\Lambda),\qquad
C_*(\Lambda)=\begin{cases}
1,&\Lambda=1,\\
 n+\dfrac{\Lambda(\Lambda-1)}{n},&\Lambda>1,\quad n=\lfloor\Lambda\rfloor.
\end{cases}\ }
\]
For every \(\Lambda>1\), finite nested families whose **least** Carleson constant is exactly \(\Lambda\) make the left side approach \(C_*(\Lambda)\) arbitrarily closely. In particular, for all \(\Lambda\ge1\),
\[
 C_*(\Lambda)\le 2\Lambda-1\le\Lambda^2,
\]
with equality in the first inequality at positive integer \(\Lambda\). This replaces a quadratic dependence on the Carleson packing constant by an optimal piecewise-quadratic expression of linear growth.

## Assumptions and scope

The family is a set of **distinct** measurable members; equality modulo null sets does not identify two distinct members. The Carleson condition counts each member once. All members have \(0<\nu(Q)<\infty\); the measure may have atoms, and neither \(\nu(X)<\infty\) nor nonatomicity is required. All inclusions are actual set inclusions, not merely inclusions modulo null sets. The assertion concerns **ancestor reciprocal masses** and the associated positive averaging-kernel estimate, not the operator norm of an arbitrary integral operator. The formula is a best constant for *all* such spaces and nested families, not an assertion that each individual family achieves it.

## Proof

**Step 1: Enumeration of the ancestors.** Fix \(S\in\mathcal F\). Since the family is nested, the members containing \(S\) form an inclusion chain. Moreover, if \(P\supseteq S\) has finite measure, there are only finitely many members \(Q\) with \(S\subseteq Q\subseteq P\). Indeed, if there were \(N\) of them, their masses would contribute at least \(N\nu(S)\) to the Carleson sum over \(\Omega=P\), while that sum is at most \(\Lambda\nu(P)\). Therefore the ancestors can be ordered as either a finite chain or a sequence
\[
S=P_0\subsetneq P_1\subsetneq\cdots,
\]
with no missing intermediate family members. Normalize their masses by
\[
x_j=\frac{\nu(P_j)}{\nu(S)},\qquad x_0=1.
\]
The sequence is nondecreasing. Applying Carleson packing at \(P_j\), then discarding all descendants not on the chosen chain, gives the necessary inequalities
\[
 x_0+\cdots+x_j\le\Lambda x_j\quad(j\ge0).
\]
For \(\Lambda>1\) this implies, for \(j\ge1\),
\[
 x_j\ge \max\left\{x_{j-1},\frac{x_0+\cdots+x_{j-1}}{\Lambda-1}\right\}.
\]

**Step 2: The coordinatewise minimal sequence.** Set \(y_0=1\), and for every integer \(j\ge1\) define
\[
 y_j=\max\left\{y_{j-1},\frac{y_0+\cdots+y_{j-1}}{\Lambda-1}\right\}.
\]
Induction on \(j\), using monotonicity of both arguments of the maximum in the preceding coordinates, shows that \(x_j\ge y_j\) for every existing index \(j\). Thus any finite ancestor sum is bounded termwise by the corresponding sum of reciprocals of the \(y_j\). For an infinite chain the same follows by taking monotone limits.

**Step 3: Exact solution of the recursion.** Let \(n=\lfloor\Lambda\rfloor\), so \(n\le\Lambda<n+1\). Directly from the recurrence,
\[
 y_0=\cdots=y_{n-1}=1,
 \qquad y_n=\frac{n}{\Lambda-1}>1.
\]
Indeed the first \(n\) terms can remain equal to one, whereas the next cannot: \(n/(\Lambda-1)>1\). The Carleson constraint binds at index \(n\):
\[
\sum_{i=0}^{n}y_i=\Lambda y_n.
\]
It continues to bind thereafter. To check this, if \(\sum_{i=0}^{j}y_i=\Lambda y_j\), then the second argument in the recurrence at \(j+1\) equals \(\Lambda y_j/(\Lambda-1)>y_j\). Hence
\[
 y_{n+k}=\frac{n}{\Lambda-1}
 \left(\frac{\Lambda}{\Lambda-1}\right)^k
 \quad\text{for every integer }k\ge0.
\]
The reciprocal sum is therefore the exact geometric-series value
\[
 \sum_{j\ge0}\frac1{y_j}
 = n+\frac{\Lambda-1}{n}\sum_{k\ge0}
 \left(\frac{\Lambda-1}{\Lambda}\right)^k
 = n+\frac{\Lambda(\Lambda-1)}{n}.
\]
This proves the asserted upper bound for \(\Lambda>1\).

**Step 4: The endpoint \(\Lambda=1\).** If there were two distinct nested members \(S\subsetneq P\), the Carleson inequality at \(\Omega=P\) would give at least \(\nu(S)+\nu(P)>\nu(P)\), a contradiction. Hence \(S\) is its only ancestor and the bound is exactly one.

**Step 5: Exact sharpness with finite families.** Fix \(\Lambda>1\) and a positive integer \(N\ge n\). Use the finite measurable space \(X_N=\{0,1,\ldots,N\}\) with the full power-set sigma-algebra. Give its singleton \(\{0\}\) mass \(1\) and, for \(j\ge1\), singleton \(\{j\}\) mass \(y_j-y_{j-1}\ge0\). Let
\[
 P_j=\{0,1,\ldots,j\}\quad(0\le j\le N),
 \qquad\mathcal F_N=\{P_0,\ldots,P_N\}.
\]
Then \(\nu(P_j)=y_j>0\). The recurrence ensures that \(\sum_{i=0}^{j}\nu(P_i)\le\Lambda\nu(P_j)\) for every index. For any measurable \(\Omega\), the members \(P_j\) contained in \(\Omega\) either form the empty set or an initial segment ending at \(P_k\). In the latter case,
\[
 \sum_{P_j\subseteq\Omega}\nu(P_j)
 =\sum_{i=0}^k y_i\le\Lambda y_k\le\Lambda\nu(\Omega),
\]
so the full Carleson condition holds. Equality at \(j=n\) gives that the least possible Carleson constant of \(\mathcal F_N\) is **exactly** \(\Lambda\). At \(S=P_0\), the reciprocal-ancestor expression equals \(\sum_{j=0}^N 1/y_j\), which increases to \(C_*(\Lambda)\) as \(N\to\infty\). Each witness is a finite family on a finite measure space; no limit construction is needed to realize arbitrarily small deficits.

**Step 6: Linear simplification and sharp integer behavior.** Write \(\Lambda=n+\delta\) with \(0\le\delta<1\). Elementary algebra gives
\[
 (2\Lambda-1)-C_*(\Lambda)=\frac{\delta(1-\delta)}{n}\ge0.
\]
The remaining inequality follows from \(2\Lambda-1\le\Lambda^2\), which is equivalent to \((\Lambda-1)^2\ge0\). For integer \(\Lambda=n\), the deficit vanishes, and the finite constructions prove that the factor \(2n-1\) cannot be lowered.

## Verification

The included standalone program `verify.py` uses exact rational arithmetic. For 35 rational values of \(\Lambda\) it tests the greedy recurrence, its explicit geometric tail, and the comparison with \(2\Lambda-1\) and \(\Lambda^2\). For each nonendpoint parameter it checks the Carleson condition over **every subset** of a finite eight-atom witness space and independently enumerates rational feasible four-mass sequences to verify coordinatewise minimality. It returns `VERIFY_OK` when all tests pass. These finite checks are diagnostics; the quantifiers over every real parameter and arbitrary nested families are established by Steps 1–6, not by enumeration.

## Relationship to prior work

Conde Alonso, Monti and Rizzo, *Almost sparse operators and Bergman projectors on trees* (arXiv:2610.08211v1, first posted 2026-10-06), Proposition 1.2, proved the general reciprocal-ancestor estimate with \(\Lambda^2\). Its full text and argument concern exactly the nested family and Carleson convention used here. The contribution here is the optimal **universal** constant, proved by an extremal one-dimensional recurrence and finite atomic witnesses; the original \(\Lambda^2\) inequality does not itself yield that best constant.

The full texts of Honig–Lorist, *Optimization algorithms for Carleson and sparse collections of sets* (arXiv:2501.07943), and Hänninen, *Equivalence of sparse and Carleson coefficients for general sets* (arXiv:1709.10457), were also compared. They concern Carleson/sparse equivalence, algorithmic computation of a given family’s Carleson constant, and duality; neither gives the above universal reciprocal-ancestor optimization. This comparison is restricted to the inspected sources and is not a proof that no other equivalent result exists.

## Limitations

The bound is for the scalar positive reciprocal ancestor sum. It does not determine the best \(L^p\) operator norm of a general sparse averaging operator, a Bergman projector, or a weighted two-weight inequality. The attaining sequence of **finite** families has limits approaching the sharp constant; a fixed finite family need not attain the limiting constant. An unindexed older sharp bound could exist and would require further bibliographic checking. Scientific independent validation has not been performed.

## References

1. J. M. Conde Alonso, M. Monti, E. Rizzo, *Almost sparse operators and Bergman projectors on trees*, arXiv:2610.08211v1 (2026), Proposition 1.2. https://arxiv.org/html/2610.08211v1
2. E. A. Honig, E. Lorist, *Optimization algorithms for Carleson and sparse collections of sets*, arXiv:2501.07943 (2025; version dated May 2026), Sections 1–3. https://arxiv.org/pdf/2501.07943
3. T. S. Hänninen, *Equivalence of sparse and Carleson coefficients for general sets*, arXiv:1709.10457 (2017), Sections 1–2. https://arxiv.org/pdf/1709.10457
