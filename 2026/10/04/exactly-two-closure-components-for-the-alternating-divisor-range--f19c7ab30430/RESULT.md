# Exactly two closure components for the alternating divisor range at parameter two
## Finding
Let \(s_{-2}\) be the multiplicative arithmetic function defined by
\[
s_{-2}(p^\alpha)=\sum_{j=0}^{\alpha}(-p^{-2})^j
\]
for every prime \(p\) and integer \(\alpha\ge 0\). Then
\[
\overline{s_{-2}(\mathbb N)}=
\left[\frac{6}{\pi^2},\frac{73}{81}\right]
\cup
\left[\frac{9}{\pi^2},1\right].
\]
The two intervals are disjoint. In particular, the closure of the range of \(s_{-2}\) has exactly two connected components.

## Assumptions and scope
The domain is the set \(\mathbb N\) of positive integers. The bar denotes topological closure in \(\mathbb R\). The result concerns the single parameter value \(r=2\) in the alternating divisor-function family introduced by Defant. No assertion is made here for other values of \(r\).

Write the primes as \(p_1=2,p_2=3,p_3=5,\ldots\), and set
\[
F_m=s_{-2}(p_m^2)\prod_{i=1}^m(1-p_i^{-2}).
\]
Also put
\[
L=\prod_{p\ge 5}(1-p^{-2})=\frac{9}{\pi^2}.
\]

## Proof
First consider integers coprime to \(6\). Defant's density criterion for the alternating divisor range is proved by a greedy logarithmic construction that depends only on the ordered prime factors under consideration. Applying the same argument to the tail \(5,7,11,\ldots\), its range is dense in \([L,1]\) provided
\[
s_{-2}(p_m^2)\ge \prod_{i>m}(1-p_i^{-2})
\]
for every \(m\ge 3\), equivalently \(F_m\ge 6/\pi^2\).

At \(r=2\), the monotonicity argument in the proof of Defant's Theorem 2.3 gives \(F_3>F_4\), and gives a strictly decreasing sequence \((F_m)_{m\ge5}\) with limit \(6/\pi^2\). It therefore remains only to check \(F_4>6/\pi^2\). Direct simplification gives
\[
F_4=\frac{1807104}{2941225}>\frac{39}{64}.
\]
The classical bound \(\pi>3.14\) implies \(\pi^2>128/13\), so
\[
\frac{6}{\pi^2}<\frac{39}{64}<F_4.
\]
Hence
\[
\overline{\{s_{-2}(m):(m,6)=1\}}=[L,1]=\left[\frac{9}{\pi^2},1\right].
\]

Now write uniquely \(n=2^a3^b m\) with \((m,6)=1\). Put \(c_{a,b}=s_{-2}(2^a)s_{-2}(3^b)\). For every fixed pair \((a,b)\), the corresponding closure is
\[
[c_{a,b}L,c_{a,b}].
\]
If \((a,b)\ne(0,0)\), then the largest possible positive-exponent local factor is attained at exponent \(2\). Thus
\[
c_{a,b}\le s_{-2}(3^2)=\frac{73}{81}.
\]
So every value contributed by an integer divisible by \(2\) or \(3\) lies at or below \(73/81\).

It remains to show that no holes occur below that endpoint. The eight pairs \((a,b)\in\{0,1,2\}^2\setminus\{(0,0)\}\) give, in increasing order, the constants
\[
\frac23,\quad \frac{73}{108},\quad \frac{13}{18},\quad
\frac{949}{1296},\quad \frac34,\quad \frac{13}{16},\quad
\frac89,\quad \frac{73}{81}.
\]
For consecutive constants \(c<c'\) in this list, the smallest ratio \(c/c'\) is \(117/128\). Since \(\pi>3.14\) also gives
\[
L=\frac{9}{\pi^2}<\frac{117}{128},
\]
we have \(c'L\le c\) for every consecutive pair. Therefore the eight intervals \([cL,c]\) overlap in a chain. Their union is exactly
\[
\left[\frac23L,\frac{73}{81}\right]
=
\left[\frac{6}{\pi^2},\frac{73}{81}\right].
\]

Finally, the classical bound \(\pi<22/7\) gives
\[
\frac{73}{81}<\frac{9}{\pi^2},
\]
so the two displayed intervals are disjoint. Combining the coprime-to-\(6\) tail with the lower chain proves the stated closure formula.

## Verification
The accompanying script `verify.py` checks all exact rational constants used in the finite overlap argument, checks the implications of the classical bounds \(3.14<\pi<22/7\), computes \(F_4\) exactly, and directly evaluates \(s_{-2}(n)\) for every \(1\le n\le 200000\) to confirm that no sampled value enters the proved gap. The finite computation is corroborative; the interval identity is established by the proof above.

## Relationship to prior work
Defant introduced this family and proved a necessary-and-sufficient criterion for density of the range in \(((\zeta(r))^{-1},1]\). For \(1<r\le2\), the criterion is reduced to three prime-index checks, and the paper identifies the transition value \(\eta_A\approx1.9011618\). Thus \(r=2\) is known there to lie on the non-dense side. The final section asks more generally for those \(r\) for which the closure is a disjoint union of exactly \(L\) intervals. The present result answers that component-count question at the natural integer point \(r=2\), with exact endpoints.

Exact-phrase and endpoint searches for the constants \(73/81\) and \(9/\pi^2\), together with searches for an exact two-component description of the \(s_{-2}\) range, did not identify a published statement equivalent to the theorem above.

## Limitations
The proof determines only the parameter \(r=2\). It does not classify a neighborhood of \(2\), determine the component count for other non-dense parameters, or assert that the same finite overlap pattern persists as \(r\) varies. The numerical sweep in `verify.py` is not used to prove density or exhaust an infinite range.

## References
1. Colin Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128v1 (2015), especially Definition 1.1, Theorems 2.2--2.4, and the final open problem.
