# Exact defect decomposition for the Bruss–Robertson–Steele inequality
## Finding
Let \(X_1,\ldots,X_n\) be positive random variables satisfying the generalized Bruss–Robertson–Steele setup: their marginal distribution functions \(F_i\) are absolutely continuous, dependence is otherwise arbitrary, and \(s>0\) is a packing budget. Let \(t>0\) satisfy
\[
\sum_{i=1}^n\mathbb E\!\left[X_i\mathbf 1_{\{X_i\le t\}}\right]
=
\sum_{i=1}^n\int_0^t x\,dF_i(x)
=s.
\]
For a realization \(x=(x_1,\ldots,x_n)\), let \(A\) be the indices of a maximum-cardinality feasible subcollection,
\[
S_A:=\sum_{i\in A}x_i\le s,
\qquad
N:=|A|,
\]
and define the threshold set and its mass by
\[
B:=\{i:x_i\le t\},
\qquad
S_B:=\sum_{i\in B}x_i.
\]
Then the threshold dual certificate appearing in Rogers's proof has the exact pathwise defect
\[
|B|+\frac{s-S_B}{t}-N
=
\frac{1}{t}\left(
 s-S_A+
 \sum_{i\in A\triangle B}|x_i-t|
\right).
\]
Taking expectations gives the exact BRS deficit
\[
\sum_{i=1}^nF_i(t)-\mathbb EN
=
\frac1t\,\mathbb E\!\left[
 s-S_A+
 \sum_{i\in A\triangle B}|X_i-t|
\right].
\]
The previously published residual-budget refinement retains only \(\mathbb E(s-S_A)/t\); the second term is an additional nonnegative penalty measuring disagreement between the optimal packing and the deterministic threshold rule.

Because the marginals are absolutely continuous,
\[
\mathbb EN=\sum_{i=1}^nF_i(t)
\quad\Longleftrightarrow\quad
S_B=s\quad\text{almost surely}.
\]
Hence, whenever the truncated variables \(X_i\mathbf 1_{\{X_i\le t\}}\) are independent and at least one is nondegenerate, the BRS inequality is strict.

## Assumptions and scope
All \(X_i\) are positive and have absolutely continuous marginal laws. No independence assumption is imposed for the identity or equality characterization. The threshold \(t\) is any positive solution of the usual BRS budget equation. If a realization has ties among observations, a deterministic tie-breaking rule may be fixed when choosing a maximum-cardinality feasible set; the identity itself is unaffected because an index with \(x_i=t\) contributes zero to the mismatch term. Absolute continuity implies \(\Pr\{X_i=t\}=0\) for each fixed \(t\).

The statement concerns the standard maximum-cardinality packing functional underlying the BRS inequality. It does not claim an improved universal upper bound obtained by replacing the mismatch term with a quantity depending only on the marginal laws.

## Proof
For a fixed realization, Rogers's dual objective at \(\eta=1/t\) is
\[
\Phi_t
=
\sum_{i=1}^n\left(1-\frac{x_i}{t}\right)_+
+
\frac{s}{t}
=
|B|+\frac{s-S_B}{t}.
\]
On the other hand,
\[
N
=
\frac{S_A}{t}
+
\sum_{i\in A}\left(1-\frac{x_i}{t}\right).
\]
Subtracting and separating the indices in \(B\setminus A\) from those in \(A\setminus B\) gives
\[
\begin{aligned}
\Phi_t-N
&=
\frac{s-S_A}{t}
+
\sum_{i\in B\setminus A}\left(1-\frac{x_i}{t}\right)
-
\sum_{i\in A\setminus B}\left(1-\frac{x_i}{t}\right)\\
&=
\frac{1}{t}\left(
 s-S_A
 +\sum_{i\in B\setminus A}(t-x_i)
 +\sum_{i\in A\setminus B}(x_i-t)
\right)\\
&=
\frac{1}{t}\left(
 s-S_A+
 \sum_{i\in A\triangle B}|x_i-t|
\right).
\end{aligned}
\]
Every term on the last line is nonnegative.

The BRS threshold equation gives \(\mathbb ES_B=s\), while absolute continuity gives
\[
\mathbb E|B|=\sum_{i=1}^nF_i(t).
\]
Therefore
\[
\mathbb E\Phi_t
=
\sum_{i=1}^nF_i(t),
\]
and taking expectations in the pathwise identity proves the exact expected-deficit formula.

For equality in the BRS inequality, the nonnegative random variable on the right must vanish almost surely. Hence \(S_A=s\) and \(A=B\) almost surely, which implies \(S_B=s\) almost surely. Conversely, if \(S_B=s\), then \(B\) is feasible and the next-smallest observation outside \(B\), if one exists, is strictly larger than \(t\) almost surely. Thus no feasible set can have more than \(|B|\) members, so \(A=B\) and \(S_A=s\). This proves the equivalence.

Finally, put \(Y_i=X_i\mathbf 1_{\{X_i\le t\}}\). If the \(Y_i\) are independent and at least one has positive variance, then
\[
\operatorname{Var}(S_B)=\sum_{i=1}^n\operatorname{Var}(Y_i)>0,
\]
so \(S_B\) cannot equal \(s\) almost surely. The BRS inequality is therefore strict.

## Verification
The standalone `verify.py` script exhaustively checks the pointwise identity with exact rational arithmetic on more than one hundred thousand finite configurations. For each configuration it constructs the maximum-cardinality packing by sorting the positive item sizes, forms the threshold set, and verifies both the exact defect identity and nonnegativity. It also checks, away from threshold ties, that \(S_B=s\) forces the packing and threshold sets to coincide.

The successful terminal line is of the form
`VERIFY_OK exact_cases=... equality_cases=...`.

The finite checks are regression tests only. The all-realization identity and the expected statement are proved algebraically above.

## Relationship to prior work
Rogers gives a three-page linear-programming proof of the BRS inequality. For any \(\eta>0\), his dual certificate is
\[
\sum_i(1-\eta X_i)_+ + \eta s,
\]
and optimizing at \(\eta=1/t\) yields the classical BRS upper bound. The inspected article does not decompose the slack between that dual certificate and the integral packing optimum, nor does it classify equality.

Bruss's survey derives a pathwise comparison between the optimal set \(A\) and the threshold set \(B\), and its Theorem 3 improves the BRS bound by subtracting
\[
\frac{s-\mathbb ES_A}{t}.
\]
The identity here shows exactly what remains after that refinement: the additional mismatch cost
\[
\frac1t\,\mathbb E\sum_{i\in A\triangle B}|X_i-t|.
\]
Thus the published refinement is not merely sharpened numerically; its missing slack is identified pointwise and equality in the original inequality is characterized by the constant-sum condition \(S_B=s\) almost surely.

Targeted searches using equality, exact-defect, threshold-mismatch, knapsack, and complete-mixability terminology did not locate a published statement of this decomposition or equivalence.

## Limitations
The result identifies the exact slack of the standard threshold dual certificate, but it does not turn the mismatch expectation into a universal marginal-only correction. The equality characterization allows arbitrary dependence and therefore does not classify which collections of marginals admit a coupling with \(S_B=s\) almost surely. That coupling question is closely related to complete-mixability phenomena for the truncated variables and can be nontrivial.

The literature search did not find an equivalent identity, but a formulation under linear-programming complementary slackness or stochastic knapsack terminology may exist outside the indexed sources inspected.

## References
1. L. C. G. Rogers, *The Bruss–Robertson–Steele inequality*, Journal of Applied Probability 60 (2023), 1112–1114, DOI 10.1017/jpr.2022.122. First published online 2023-03-13.
2. F. Thomas Bruss, *The BRS-inequality and its Applications A Survey*, arXiv:2007.05358v1, first public 2020-07-10; Probability Surveys 18 (2021), 44–76.
3. J. M. Steele, *The Bruss–Robertson inequality: Elaborations, extensions, and applications*, arXiv:1510.00843.
