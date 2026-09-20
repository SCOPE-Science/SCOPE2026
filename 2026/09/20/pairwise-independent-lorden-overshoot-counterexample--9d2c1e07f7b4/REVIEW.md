# Review — Pairwise independence does not preserve Lorden's mean-overshoot bound

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

The counterexample can be checked entirely by finite counting.

For distinct \(i,j\in\mathbb F_q\), the map
\[
(U,V)\mapsto(U+iV,U+jV)
\]
is invertible because its determinant is \(j-i\ne0\). Consequently the indicators
\[
B_i=\mathbf 1\{U+iV=0\}
\]
are pairwise independent Bernoulli\((1/q)\). Appending independent Bernoulli\((1/q)\) coordinates preserves pairwise independence and the common marginal law.

At boundary \(b=q-1\), positivity forces crossing within the first \(q\) coordinates. The three exhaustive cases \(V=0,U=0\), \(V=0,U\ne0\), and \(V\ne0\) yield respectively overshoots \(q+1\), \(1\), and \(q+J\), where \(J\) is uniformly represented over the \(q\) possible root locations. The resulting exact mean is
\[
\mathbb E R_b=\frac{3q}{2}-1+\frac{3}{2q}.
\]

The marginal moments are
\[
\mathbb E X=\frac{3q-1}{q},\qquad
\mathbb E X^2=\frac{4q^2+q-1}{q},
\]
so the classical Lorden right-hand side would be
\[
\frac{4q^2+q-1}{3q-1}.
\]
Symbolic subtraction gives
\[
\frac{(q-1)(q^2-10q+3)}{2q(3q-1)}>0
\]
for \(q\ge11\). Direct enumeration for representative primes agrees with the formulas. The asymptotic ratio is \(9/8\).

Stress checks included the strict-crossing convention \(S_n>b\): in the all-unit case \(S_{q-1}=b\) does not count as a crossing, and the \(q\)-th increment gives overshoot \(1\). This is the convention used in the classical Lorden statement.

## Originality

**PASS, to the best of our knowledge.**

The literature search covered the exact phrases and close variants “Lorden pairwise independent,” “Lorden's inequality pairwise independence,” “overshoot pairwise independent,” “renewal pairwise independent overshoot,” “excess over the boundary pairwise independent,” “dependent increments Lorden counterexample,” and combinations of first passage, renewal, pairwise independence, and overshoot.

The inspected literature establishes nearby but different results:

- Lorden (1970) is the classical independent-renewal source.
- Chang (1994) gives further overshoot inequalities.
- Spouge (2007) extends to independent, non-identically distributed summands.
- Svensson (2002) gives a random-environment generalization.
- Kalimulina and Zverkina (arXiv:2501.18329, revised 2026) explicitly treat dependent and heterogeneous inter-renewal times, but their Lorden-type bound requires a two-sided comparison scheme and an additional renewal-measure domination condition. Their literature discussion lists independent non-identical and random-environment extensions; no pairwise-independence counterexample was located in the inspected text.
- Avanzi et al. (2021) show that pairwise independence is insufficient for a general i.d. central limit theorem, confirming that higher-order dependence can invalidate classical independent-sequence conclusions, but their result does not concern overshoots or Lorden's inequality.

No inspected source stated the present finite-field counterexample, the explicit violation formula, or the \(9/8\) asymptotic factor.

The original 1970 article's repository record and abstract were inspected, while the article PDF itself was not. The classical theorem and its assumptions were independently cross-checked against the explicit restatement in the 2025/2026 dependent-renewal paper. The residual originality risk is that an older renewal/dependence paper may contain an equivalent counterexample under terminology not indexed by the searched phrases.

## Value

**PASS.**

The result marks a sharp qualitative boundary for a standard renewal inequality: even identical positive bounded marginals, finite second moment, and pairwise independence do not preserve the classical Lorden constant. The obstruction is explicit, elementary, and scalable, with a nonvanishing asymptotic gap.

This is useful when weakening independence assumptions in renewal, queueing, sequential analysis, or first-passage arguments. It shows that checking only pairwise independence is insufficient for importing a marginal-moment overshoot bound and motivates identifying stronger structural conditions that control the stopped higher-order dependence.

## Scientific limitations

The construction is not claimed to be stationary or mixing. It does not identify the optimal universal constant under pairwise independence, and it does not address dependent-process bounds with additional conditional or regenerative assumptions. The literature search supports originality only to the best of our knowledge.
