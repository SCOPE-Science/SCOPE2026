# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proposed family can be checked by exact exponent arithmetic alone.

For \(n\ge2\), let
\[
r=\frac83,\qquad x_1=\frac14,\qquad x_2=\cdots=x_n=\frac1{16}.
\]
Then \(r x_1=2/3\) and \(r x_i=1/6\) for \(i\ge2\). Writing
\[
Q=\prod_i x_i^{r x_i},\qquad P=\prod_i x_i,
\]
gives
\[
Q=2^{-(2n+2)/3},\qquad P=2^{-(4n-2)}.
\]
Therefore
\[
\frac{\sum_iP^{r x_i}}{Q}
=4^{1-n}+2(n-1).
\]
The conjectured left side, divided by \(Q\), equals \(n\). Their difference in
the reverse direction is
\[
4^{1-n}+2(n-1)-n=4^{1-n}+n-2>0
\]
for every \(n\ge2\). Thus the inequality fails strictly. The parameter is
admissible because
\[
e>1+1+\frac12+\frac16=\frac83.
\]
For \(n=1\), both sides of the conjectured inequality are identically equal,
so the dimension-wise conclusion is complete.

The stated two-level reduction was also checked directly: for
\(x_1=b\), \(x_2=\cdots=x_n=a\), and \(d=r(b-a)\), division by
\(b^{rb}a^{ra(n-1)}\) yields exactly
\[
n\ge a^{(n-1)d}+(n-1)b^{-d}.
\]
No numerical approximation is required anywhere in the proof.

## Originality

The 2014 source states Conjecture 3.3 in the form reviewed above. Matejíčka
(2016) explicitly says that Conjectures 3.1 and 3.2 from that paper are not
valid and prints a counterexample for a cyclic power-exponential inequality;
it does not state that Conjecture 3.3 is resolved.

The literature check included the numbered conjecture, the exact authors and
title, equivalent product notation, and later papers citing the 2014 work.
Hassani--Nishizawa (2023) concerns two-variable functions of a different
form and poses different conjectures. Kyriakis (2026) cites the 2014 paper in
a current collection of power-exponential inequalities. No source located in
these searches states the fixed family
\[
(1/4,1/16,\ldots,1/16),\quad r=8/3,
\]
or an equivalent family resolving every \(n\ge2\).

There is an important priority limitation: direct substitution indicates that
the rational point printed by Matejíčka (2016), although presented against a
different cyclic inequality, also violates Conjecture 3.3 for \(n=3\).
Accordingly, the present claim is deliberately not “the first counterexample.”
The claimed contribution is the exact uniform family for all \(n\ge2\), plus
the complete dimension-wise falsification and the two-level mechanism.
A differently worded or non-indexed prior all-dimensional construction remains
possible.

## Value

Conjecture 3.3 is the only one of the three sequence conjectures in the 2014
Section 3 not explicitly listed as invalid in Matejíčka's 2016 correction.
The result settles its universal validity in the strongest possible
dimension-wise sense: it is trivially true for \(n=1\) and false for every
\(n\ge2\), using one fixed admissible exponent and two fixed coordinate
values. The reduction to a scalar two-level condition also shows that the
failure is robust rather than isolated.

## Limitations

The result does not classify all tuples or exponents for which the inequality
holds, and the two-level condition is not necessary for failure. The
originality check cannot exclude a differently phrased or poorly indexed
all-dimensional family. Independent audit has not been performed.
