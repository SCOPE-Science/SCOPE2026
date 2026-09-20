# Uniform counterexamples to Coronel–Huancas Conjecture 3.3

## Result

Coronel and Huancas (2014), Conjecture 3.3, asserts that for \(n\in\mathbb N\),
\(x=(x_1,\ldots,x_n)\in(0,1]^n\), and \(r\in[0,e]\),
\[
n\prod_{i=1}^n x_i^{r x_i}
\ge
\sum_{i=1}^n
\left(\prod_{j=1}^n x_j\right)^{r x_i}.
\]

The conjecture is false in every nontrivial dimension \(n\ge2\). In fact, for every
\(n\ge2\), take
\[
r=\frac83,\qquad
x_1=\frac14,\qquad
x_2=\cdots=x_n=\frac1{16}.
\]
Then \(r<e\) and the conjectured inequality is reversed strictly.

Consequently the universal statement in Conjecture 3.3 is valid only in the
trivial one-variable case \(n=1\), where both sides are identically equal.

## Proof

Put
\[
Q=\prod_{i=1}^n x_i^{r x_i},
\qquad
P=\prod_{j=1}^n x_j.
\]
For the displayed choice,
\[
r x_1=\frac23,\qquad r x_i=\frac16\quad(i\ge2),
\]
and hence
\[
Q
=(2^{-2})^{2/3}
 (2^{-4})^{(n-1)/6}
=2^{-(2n+2)/3},
\]
while
\[
P=2^{-2}(2^{-4})^{n-1}=2^{-(4n-2)}.
\]
Therefore
\[
\frac1Q\sum_{i=1}^n P^{r x_i}
=
\frac{P^{2/3}+(n-1)P^{1/6}}{Q}
=
4^{1-n}+2(n-1).
\]
The conjectured left-hand side divided by \(Q\) is simply \(n\). Thus
\[
\frac1Q\left[
\sum_{i=1}^n P^{r x_i}
-
nQ
\right]
=
4^{1-n}+n-2>0
\qquad(n\ge2).
\]
This proves strict failure for every \(n\ge2\).

Finally,
\[
e=\sum_{k=0}^\infty \frac1{k!}
>
1+1+\frac12+\frac16
=\frac83,
\]
so the chosen \(r\) lies strictly inside the conjectured range \([0,e]\).

## A two-parameter mechanism

More generally, for
\[
x_1=b,\qquad x_2=\cdots=x_n=a,\qquad 0<a<b\le1,
\]
and \(d=r(b-a)\), division by
\(b^{rb}a^{ra(n-1)}\) shows that Conjecture 3.3 is equivalent on this
two-level family to
\[
n\ge a^{(n-1)d}+(n-1)b^{-d}.
\]
Hence every choice with
\[
a^{(n-1)d}+(n-1)b^{-d}>n
\]
is a counterexample. The explicit family above has
\(a=1/16\), \(b=1/4\), \(d=1/2\), giving
\(4^{1-n}+2(n-1)>n\). The strict inequality also implies an open
neighborhood of counterexamples around each displayed point.

## Context and literature

Coronel and Huancas (2014) introduced Conjecture 3.3 together with two other
sequence generalizations. Matejíčka (2016) subsequently reported that
Conjectures 3.1 and 3.2, as well as several earlier statements in the 2014
paper, are not valid, but did not state a resolution of Conjecture 3.3.

Later work on power-exponential inequalities continues to cite the 2014 paper.
Hassani and Nishizawa (2023), for example, study two-variable
power-exponential inequalities and introduce different conjectures. A 2026
collection by Kyriakis also cites Coronel–Huancas in its survey of the area.
Searches by the numbered conjecture, its exact authors/title, the product form
above, and later citation chains did not locate a published statement giving
the all-\(n\ge2\) counterexample family or the dimension-wise resolution proved
here.

The 2016 paper prints a numerical/rational data point as a counterexample to a
different cyclic inequality. Direct substitution suggests that the same point
also violates Conjecture 3.3. Accordingly, no claim is made here that this is
the first isolated counterexample ever implicit in the literature; the
contribution is the exact uniform family for every \(n\ge2\) and the resulting
complete dimension-wise falsification of the universal conjecture.

## Limitations

- The result classifies the conjecture only as a universal statement by dimension; it does not characterize the full parameter region where the inequality holds or fails.
- The two-level criterion above is sufficient to generate counterexamples, not a classification of all counterexamples.
- A differently phrased or non-indexed prior all-dimensional family may exist.

## References

1. A. Coronel and F. Huancas, *The proof of three power-exponential inequalities*, Journal of Inequalities and Applications 2014, 509 (2014). DOI: 10.1186/1029-242X-2014-509. arXiv:1409.1968.
2. L. Matejíčka, *On the Cîrtoaje's conjecture*, Journal of Inequalities and Applications 2016, 152 (2016). DOI: 10.1186/s13660-016-1092-2.
3. M. Hassani and Y. Nishizawa, *Some Inequalities Related To The Power Exponential Function*, Applied Mathematics E-Notes 23 (2023), 237–242.
4. A. Kyriakis, *A Collection of Inequalities Involving Power Exponential and Logarithmic Functions*, Earthline Journal of Mathematical Sciences 16(2) (2026), 199–220. DOI: 10.34198/ejms.16226.16.199220.

**Same-model review: passed. Independent audit: not yet performed.**
