# Optimal asymptotic tuning of the Hadamard construction for maximal equilateral sets

**Same-model review: passed. Independent audit: not yet performed.**

## Result

For a normed space \(Y\), let \(m(Y)\) denote the minimum cardinality of a maximal equilateral subset of \(Y\). Swanepoel and Villa (2013), Proposition 23, construct maximal equilateral sets from two Hadamard orders \(k_1,k_2\).

For \(1\le p<2\), let \(\mathcal A_p\) be the set of pairs \((k_1,k_2)\) of Hadamard orders satisfying the three hypotheses (12)--(14) of Proposition 23 in Swanepoel--Villa, and define
\[
B_H(p)=\min_{(k_1,k_2)\in\mathcal A_p}2(k_1+k_2).
\]
For \(p\) sufficiently close to \(2\), \(\mathcal A_p\neq\varnothing\). Then
\[
\boxed{
B_H(p)\sim \frac{4}{\,2-2^{p-1}\,}
\sim \frac{2}{(2-p)\ln 2}
\qquad (p\uparrow2).
}
\]

Thus the leading constant obtainable from the full two-Hadamard construction of Proposition 23 is determined exactly. In particular, one may choose the constants in Swanepoel--Villa's Theorem 6 so that
\[
C(p)\le \frac{2+o(1)}{(2-p)\ln2},
\qquad
d_0(p)\le \frac{2+o(1)}{(2-p)\ln2}.
\]
More concretely, for every \(\varepsilon>0\), for all \(p<2\) sufficiently close to \(2\), there is a Hadamard order \(k\) such that Proposition 23 applies with \(k_1=k_2=k\), and
\[
4k<(1+\varepsilon)\frac{4}{2-2^{p-1}}.
\]
Hence, for every \(q\in[1,\infty)\), every normed space \(X\), and every
\[
d\ge 4k-2,
\]
one has
\[
m(\ell_p^d\oplus_q X)\le 4k.
\]

The 2013 proof instead records
\[
C(p),d_0(p)<\frac{16}{4-2^p}
\sim\frac{4}{(2-p)\ln2}.
\]
The estimate above halves that displayed leading constant, and the lower bound below shows that no further constant-factor improvement is possible without leaving Proposition 23's two-Hadamard framework.

## Proof

Put
\[
a_p=2-2^{p-1}.
\]
Then
\[
4-2^p=2a_p.
\]

### Lower bound for every admissible pair

If \((k_1,k_2)\in\mathcal A_p\), hypothesis (12) of Proposition 23 gives
\[
\frac1{k_1}+\frac1{k_2}<4-2^p=2a_p.
\]
On the other hand,
\[
(k_1+k_2)\left(\frac1{k_1}+\frac1{k_2}\right)\ge4
\]
by AM--HM (equivalently, Cauchy--Schwarz). Therefore
\[
2(k_1+k_2)
\ge
\frac{8}{1/k_1+1/k_2}
>
\frac4{a_p}.
\]
Consequently,
\[
B_H(p)>\frac4{a_p}.
\]

### Matching upper bound from asymptotically dense Hadamard orders

Let
\[
x_p=\frac1{a_p}.
\]
Swanepoel--Villa's Lemma 20 states that if \(H(t)\) is the largest Hadamard order below \(t\), then
\[
\frac{H(t)}t\longrightarrow1
\qquad(t\to\infty).
\]
Fix \(0<\varepsilon<1\) and put \(t=(1+\varepsilon)x_p\). Since \(x_p\to\infty\) as \(p\uparrow2\), Lemma 20 implies, for all \(p\) sufficiently close to \(2\),
\[
H((1+\varepsilon)x_p)>x_p.
\]
Set
\[
k=H((1+\varepsilon)x_p).
\]
Then
\[
x_p<k<(1+\varepsilon)x_p<2x_p.
\]

For the symmetric choice \(k_1=k_2=k\), condition (12) of Proposition 23 becomes exactly
\[
a_p<\frac2k<2a_p,
\]
which is equivalent to
\[
x_p<k<2x_p.
\]
Conditions (13) and (14) reduce to the upper inequality as well: their common right-hand side is
\[
\frac{(1-2^{1-p})+1}{k}
=
\frac{2(1-2^{-p})}{k},
\]
so each becomes
\[
(1-2^{-p})a_p
<
\frac{2(1-2^{-p})}{k},
\]
equivalently \(k<2x_p\).

Hence \((k,k)\in\mathcal A_p\), and Proposition 23 gives a maximal equilateral set of size \(4k\) in every \(\ell_p^d\oplus_q X\) with \(d\ge4k-2\). Moreover,
\[
B_H(p)\le4k<4(1+\varepsilon)x_p
=(1+\varepsilon)\frac4{a_p}.
\]
Together with the lower bound,
\[
1<
\frac{B_H(p)}{4/a_p}
<
1+\varepsilon
\]
for all \(p\) sufficiently close to \(2\). Since \(\varepsilon>0\) is arbitrary,
\[
B_H(p)\sim\frac4{a_p}.
\]

Finally, writing \(h=2-p\),
\[
2^{p-1}=2^{1-h}
=2e^{-h\ln2}
=2-2h\ln2+O(h^2),
\]
and therefore
\[
a_p=2h\ln2+O(h^2).
\]
Thus
\[
\frac4{a_p}\sim\frac2{(2-p)\ln2},
\]
as claimed. \(\square\)

## Relation to prior literature

Swanepoel and Villa prove that \(m(\ell_p^d\oplus_q X)\) is bounded independently of \(d\) for each fixed \(1\le p<2\), using Proposition 23 and Hadamard matrices. Their Lemma 20 already supplies the asymptotic density \(H(t)/t\to1\), but their proof of Theorem 6 chooses a Hadamard order near the *upper* endpoint of the admissible interval and records
\[
4k<\frac{16}{4-2^p}.
\]
The argument above instead chooses an order asymptotically just above the lower endpoint and combines this with the reciprocal-sum constraint in Proposition 23 to identify the construction's optimal leading constant.

Searches of the exact asymptotic expressions, Proposition 23, the Hadamard formulation, and later literature on maximal equilateral sets did not locate this sharpening or a stronger statement implying it. The originality claim is therefore to the best of current knowledge.

## Limitations

- The lower bound is an optimality statement only for the two-Hadamard construction encoded by Swanepoel--Villa Proposition 23. It is not a lower bound for \(m(\ell_p^d)\) itself.
- The result improves the leading constant in that construction but does not close the logarithmic gap between the known general upper and lower asymptotic orders near \(p=2\).
- Originality remains subject to residual risk from unindexed, inaccessible, or differently phrased literature.

## Source

Konrad J. Swanepoel and Rafael Villa, *Maximal Equilateral Sets*, Discrete & Computational Geometry **50** (2013), 354--373. DOI: https://doi.org/10.1007/s00454-013-9523-z
