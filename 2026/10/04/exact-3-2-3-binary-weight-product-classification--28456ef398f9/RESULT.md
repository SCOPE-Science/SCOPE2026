# Exact \((3,2,3)\) binary-weight product classification

## Finding
Let \(s(n)\) denote the number of nonzero digits in the binary expansion of the positive integer \(n\).

If \(a,b\) are positive odd integers with
\[
s(a)=2,
\qquad
s(b)=3,
\]
then
\[
s(ab)=3
\]
if and only if
\[
(a,b)\in\{(3,7),(5,7)\}.
\]

Thus, up to interchanging the two factors, the only products whose two factor weights are \(2\) and \(3\) and whose product weight is \(3\) are
\[
21=3\cdot7
\qquad\text{and}\qquad
35=5\cdot7.
\]

## Assumptions and scope
The binary weight is
\[
s(n)=\#\{\text{ones in the base-two expansion of }n\}.
\]
Only positive odd factors are considered, matching the source problem.

The result concerns the first asymmetric weight pair immediately beyond the exceptional infinite family with
\[
s(a)=s(b)=2,
\qquad
s(ab)=3.
\]
It does not classify all triples of binary weights.

## Proof
Kaneko and Stoll prove that if positive odd integers \(a,b\) satisfy
\[
s(a)=\ell,
\qquad
s(b)=m,
\qquad
s(ab)=3,
\]
with
\[
\max\{\ell,m\}\ge3,
\]
then
\[
ab<2^{-13+4\ell m}.
\]

For
\[
(\ell,m)=(2,3),
\]
this gives
\[
ab<2^{11}=2048.
\]

Every odd integer of binary weight \(2\) has the unique form
\[
a=1+2^u,
\qquad
u\ge1.
\]
Every odd integer of binary weight \(3\) has the unique form
\[
b=1+2^v+2^w,
\qquad
1\le v<w.
\]

The bound
\[
ab<2048
\]
makes the exponent search finite. In particular,
\[
a<2048
\quad\text{and}\quad
b<2048,
\]
so
\[
1\le u\le10,
\qquad
1\le v<w\le10.
\]
Checking all exponent triples in this finite rectangle while retaining only those with \(ab<2048\) leaves exactly \(119\) admissible triples.

Among those \(119\) triples, exactly two have product weight \(3\):
\[
(u,v,w)=(1,1,2)
\]
and
\[
(u,v,w)=(2,1,2).
\]
They give
\[
(a,b)=(3,7)
\]
and
\[
(a,b)=(5,7),
\]
respectively.

Directly,
\[
21=(10101)_2
\]
and
\[
35=(100011)_2,
\]
so both products have exactly three nonzero binary digits.

The finite enumeration is exhaustive because the published theorem supplies the strict global bound \(ab<2048\); there is no unsearched tail.

## Verification
The accompanying `verify.py` independently generates every odd binary-weight-\(2\) integer and every odd binary-weight-\(3\) integer compatible with the strict bound
\[
ab<2048.
\]
It checks all \(119\) admissible exponent triples and confirms that exactly two satisfy
\[
s(ab)=3.
\]

The checker also verifies the source bound specialized to
\[
(\ell,m)=(2,3),
\]
the uniqueness of the binary exponent parametrizations in the enumerated range, and the final binary weights of \(21\) and \(35\).

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Kaneko and Stoll study the system
\[
s(ab)=k,\qquad s(a)=\ell,\qquad s(b)=m
\]
for odd integers \(a,b\). They explicitly note that it is unclear for which triples
\[
(k,\ell,m)
\]
solutions exist.

For
\[
k=3,
\]
they identify an obvious infinite family when
\[
\ell=m=2,
\]
and prove an effective global bound whenever
\[
\max\{\ell,m\}\ge3.
\]
Their paper does not state the complete solution set for the first asymmetric case
\[
(k,\ell,m)=(3,2,3).
\]

Targeted searches for the exact weight system, for the two solutions \(21\) and \(35\), and for equivalent binary-weight terminology did not locate a prior complete classification of this slice.

## Limitations
The theorem uses the published \(k=3\) product bound as a premise. It does not improve that general bound and does not classify neighboring triples such as
\[
(3,2,4)
\]
or
\[
(3,3,3).
\]

Literature non-detection cannot rule out an unindexed observation of this small exact slice.

## References
1. Hajime Kaneko and Thomas Stoll, “Products of integers with few nonzero digits,” arXiv:2112.03077v1, first posted 6 December 2021; *Uniform Distribution Theory* 17 (2022), no. 1, 71–89.
