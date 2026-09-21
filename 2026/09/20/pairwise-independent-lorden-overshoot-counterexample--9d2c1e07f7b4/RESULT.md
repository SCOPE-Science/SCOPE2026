# Pairwise independence does not preserve Lorden's mean-overshoot bound

## Statement

For i.i.d. nonnegative increments \(X_1,X_2,\ldots\), Lorden's classical inequality bounds the overshoot
\[
R_b=S_{\tau_b}-b,\qquad
S_n=\sum_{i=1}^n X_i,\qquad
\tau_b=\inf\{n\ge 1:S_n>b\},
\]
by
\[
\mathbb E R_b\le \frac{\mathbb E X_1^2}{\mathbb E X_1}.
\]

The mutual-independence hypothesis cannot be weakened to pairwise independence while keeping this same marginal-only bound.

### Theorem

For every prime \(q\ge 11\), there is a sequence \(X_1,X_2,\ldots\) of pairwise independent, identically distributed, positive integer-valued random variables such that
\[
\mathbb P(X_n=2q)=\frac1q,\qquad
\mathbb P(X_n=1)=1-\frac1q
\]
for every \(n\), but at the boundary \(b=q-1\),
\[
\mathbb E R_b
=
\frac{3q}{2}-1+\frac{3}{2q}
>
\frac{\mathbb E X_1^2}{\mathbb E X_1}
=
\frac{4q^2+q-1}{3q-1}.
\]

More precisely,
\[
\mathbb E R_b-\frac{\mathbb E X_1^2}{\mathbb E X_1}
=
\frac{(q-1)(q^2-10q+3)}{2q(3q-1)},
\]
which is positive for every \(q\ge 11\). Along primes \(q\to\infty\),
\[
\frac{\mathbb E R_b}{\mathbb E X_1^2/\mathbb E X_1}\longrightarrow \frac98.
\]

Thus pairwise independence, identical marginals, positivity, bounded support, and finite second moment do not suffice for Lorden's classical mean-overshoot constant.

## Construction

Work first with the first \(q\) coordinates. Let \(U,V\) be independent and uniform on the finite field \(\mathbb F_q\). Enumerate the \(q\) field elements by
\[
1,2,\ldots,q
\]
with \(q\) interpreted as \(0\pmod q\), and define
\[
B_i=\mathbf 1\{U+iV=0\},\qquad 1\le i\le q.
\]

For distinct \(i,j\), the linear map
\[
(U,V)\mapsto (U+iV,U+jV)
\]
has nonzero determinant \(j-i\) in \(\mathbb F_q\), hence is a bijection of \(\mathbb F_q^2\). Therefore \(B_i\) and \(B_j\) are independent Bernoulli variables with success probability \(1/q\). So \(B_1,\ldots,B_q\) are pairwise independent and identically distributed.

For \(n>q\), let \(B_n\) be mutually independent Bernoulli\((1/q)\) variables, independent of \((U,V)\) and of one another. Then the infinite sequence \((B_n)\) is pairwise independent and identically distributed.

Set
\[
X_n=1+(2q-1)B_n.
\]
Each \(X_n\) therefore equals \(2q\) with probability \(1/q\) and \(1\) otherwise, and the sequence is pairwise independent.

## Exact overshoot computation

Take
\[
b=q-1.
\]
Because every increment is at least \(1\), the crossing occurs among the first \(q\) increments, so the continuation after coordinate \(q\) is irrelevant to the overshoot.

The \((U,V)\) outcomes split into three cases.

### 1. \(V=0,\ U=0\)

All \(B_i=1\). The first increment already crosses the boundary, and
\[
R_b=2q-(q-1)=q+1.
\]
There is one such pair \((U,V)\).

### 2. \(V=0,\ U\ne0\)

All \(B_i=0\). The first \(q-1\) unit increments reach the boundary exactly, and the \(q\)-th unit increment crosses it. Hence
\[
R_b=1.
\]
There are \(q-1\) such pairs.

### 3. \(V\ne0\)

The equation \(U+iV=0\) has exactly one solution \(J\in\mathbb F_q\), corresponding to one index \(J\in\{1,\ldots,q\}\). Thus exactly one of the first \(q\) increments equals \(2q\). The crossing occurs at that index. Before it the partial sum is \(J-1\), so
\[
R_b=(J-1)+2q-(q-1)=q+J.
\]

For every fixed \(J\), there are exactly \(q-1\) choices of \(V\ne0\), with the unique compatible value \(U=-JV\). Therefore each \(J\) occurs \(q-1\) times among the \(q(q-1)\) outcomes with \(V\ne0\).

Averaging over all \(q^2\) equiprobable pairs \((U,V)\),
\[
\begin{aligned}
\mathbb E R_b
&=
\frac{(q+1)+(q-1)
 +(q-1)\sum_{j=1}^q(q+j)}{q^2}\\
&=
\frac{3q}{2}-1+\frac{3}{2q}.
\end{aligned}
\]

## Comparison with the Lorden constant

The common marginal law gives
\[
\mathbb E X_1
=
\frac{q-1}{q}+\frac{2q}{q}
=
\frac{3q-1}{q},
\]
and
\[
\mathbb E X_1^2
=
\frac{q-1}{q}+\frac{4q^2}{q}
=
\frac{4q^2+q-1}{q}.
\]
Hence
\[
\frac{\mathbb E X_1^2}{\mathbb E X_1}
=
\frac{4q^2+q-1}{3q-1}.
\]

Subtracting,
\[
\mathbb E R_b-\frac{\mathbb E X_1^2}{\mathbb E X_1}
=
\frac{(q-1)(q^2-10q+3)}{2q(3q-1)}.
\]
For \(q\ge11\), the quadratic \(q^2-10q+3\) is positive, proving the strict violation.

Finally,
\[
\mathbb E R_b\sim \frac32q,\qquad
\frac{\mathbb E X_1^2}{\mathbb E X_1}\sim \frac43q,
\]
so the violation ratio tends to \(9/8\).

## Why pairwise independence is not enough

The stopping index depends on the joint pattern of many increments, not only on one- and two-dimensional marginals. In the finite-field block, pairwise independence coexists with a strong global constraint: when \(V\ne0\), exactly one large increment occurs in the first \(q\) positions, while one exceptional outcome makes all of them large. This higher-order dependence changes the law at the first-passage time even though every pair of increments has the same joint law as under mutual independence.

The example therefore isolates a boundary between results that depend only on low-order moments and first-passage inequalities whose stopping mechanism can detect higher-order dependence.

## Relation to prior literature

Lorden's 1970 paper establishes the classical uniform mean-overshoot bound in the independent renewal setting. Later work extends or refines overshoot inequalities in other directions: Chang treats overshoot inequalities including higher moments; Spouge allows independent summands with differing distributions; Svensson studies a random-environment generalization; and Kalimulina and Zverkina study dependent, non-identically distributed renewal-type processes under comparison assumptions and an additional renewal-measure domination condition.

Pairwise independence is known to preserve some classical limit results but not others. In particular, explicit counterexamples show that the central limit theorem can fail for pairwise independent identically distributed variables. The present theorem addresses a different first-passage question: it gives an explicit bounded, positive, two-point marginal for which the classical Lorden constant itself fails under pairwise independence.

## Limitations

- The constructed sequence is pairwise independent and identically distributed but is not claimed to be strictly stationary.
- The theorem only disproves the direct replacement of mutual independence by pairwise independence in the classical marginal-only Lorden bound. It does not rule out different overshoot bounds under pairwise independence, nor bounds under stronger dependence hypotheses.
- The construction uses a deliberately structured higher-order dependence among an initial finite block. Additional assumptions such as conditional-law domination, mixing, stationarity, or regenerative structure may restore useful bounds.
- Originality is asserted only to the best of our knowledge. The construction is elementary finite-field probability, so an equivalent counterexample could exist under different terminology.

## References

1. G. Lorden, “On Excess over the Boundary,” *Annals of Mathematical Statistics* 41 (1970), 520–527. https://doi.org/10.1214/aoms/1177697092
2. J. T. Chang, “Inequalities for the Overshoot,” *Annals of Applied Probability* 4 (1994), 1223–1233. https://doi.org/10.1214/aoap/1177004913
3. J. L. Spouge, “Inequalities on the Overshoot beyond a Boundary for Independent Summands with Differing Distributions,” *Statistics & Probability Letters* 77 (2007), 1486–1489. https://doi.org/10.1016/j.spl.2007.02.013
4. D. Svensson, “A Random Environment Generalization of Lorden's Renewal Inequality,” *Markov Processes and Related Fields* 8 (2002), 637–649. https://math-mprf.org/journal/articles/id952/
5. E. Yu. Kalimulina and G. A. Zverkina, “On Lorden's Inequality and Renewal-Type Processes with Dependent Inter-Renewal Times,” arXiv:2501.18329, revised 2026. https://arxiv.org/abs/2501.18329
6. B. Avanzi, G. Boglioni Beaulieu, P. Lafaye de Micheaux, F. Ouimet, and B. Wong, “A counterexample to the existence of a general central limit theorem for pairwise independent identically distributed random variables,” *Journal of Mathematical Analysis and Applications* 499 (2021), 124982. https://doi.org/10.1016/j.jmaa.2021.124982
