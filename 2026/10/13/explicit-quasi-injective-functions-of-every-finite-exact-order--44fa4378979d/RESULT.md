# Explicit quasi-injective functions of every finite exact order

## Finding
Fix an integer \(m\ge2\). A function \(f:\mathbb N\to\mathbb N\) is called quasi-injective when
\[
f(an)=f(bn)\quad\text{for every }n\ge1
\]
implies \(a=b\). It is quasi-injective of order \(r\) when
\[
f,f^{(2)},\ldots,f^{(r)}
\]
are all quasi-injective.

There is an explicit function \(f_m:\mathbb N\to\mathbb N\) that is quasi-injective of order \(m-1\) but not of order \(m\).

Put
\[
L=2m-1.
\]
Define \(g_m:\mathbb N_0\to\mathbb N_0\) by
\[
g_m(0)=0,
\]
by the two finite chains
\[
1\longmapsto2\longmapsto\cdots\longmapsto m-1\longmapsto0
\]
and
\[
m\longmapsto m+1\longmapsto\cdots\longmapsto2m-2\longmapsto0,
\]
and, for every \(e\ge L\), by
\[
g_m(e)=
\begin{cases}
1,&e\text{ is a square},\\
m,&e\text{ is not a square}.
\end{cases}
\]
For \(n=2^e u\) with \(u\) odd, define
\[
f_m(n)=2^{g_m(e)}u.
\]

Then for every
\[
1\le k<m,
\]
the iterate \(f_m^{(k)}\) is quasi-injective, while
\[
f_m^{(m)}(2^L n)=f_m^{(m)}(2^{L+1}n)
\]
for every \(n\ge1\). Since \(2^L\ne2^{L+1}\), the \(m\)-th iterate is not quasi-injective.

Thus Question 17 of Pongsriiam has an affirmative answer for every \(m\ge2\).

## Assumptions and scope
The construction uses the definition of quasi-injectivity from Pongsriiam's 2021 paper. No multiplicativity, additivity, or monotonicity is assumed in Question 17, which asks for a function \(f:\mathbb N\to\mathbb N\).

The functions constructed here are explicit and computable but intentionally nonmultiplicative. Their role is to realize every finite exact quasi-injectivity order.

## Proof
Let \(n=2^e u\) with \(u\) odd. By construction, applying \(f_m\) changes only the exponent of \(2\) and preserves the odd part. Hence, by induction,
\[
f_m^{(k)}(n)=2^{g_m^{(k)}(e)}u
\]
for every \(k\ge1\).

For every \(e\ge L\) and every \(1\le k<m\), the two chains give
\[
g_m^{(k)}(e)=
\begin{cases}
k,&e\text{ is a square},\\
m+k-1,&e\text{ is not a square}.
\end{cases}
\]
These two values are distinct. Also,
\[
g_m^{(m)}(e)=0
\]
for every \(e\ge L\).

We first prove quasi-injectivity of every iterate before the \(m\)-th. Fix \(k<m\), and suppose
\[
f_m^{(k)}(an)=f_m^{(k)}(bn)
\]
for every \(n\ge1\). Write
\[
a=2^rA,\qquad b=2^sB,
\]
where \(A\) and \(B\) are odd. Taking \(n=2^e\) gives
\[
2^{g_m^{(k)}(r+e)}A
=
2^{g_m^{(k)}(s+e)}B
\]
for every \(e\ge0\). Unique factorization first gives
\[
A=B
\]
and then
\[
g_m^{(k)}(r+e)=g_m^{(k)}(s+e)
\]
for every \(e\ge0\).

Assume, for contradiction, that \(r<s\), and put
\[
d=s-r>0.
\]
The displayed equality says
\[
g_m^{(k)}(E)=g_m^{(k)}(E+d)
\]
for every sufficiently large \(E\). Choose a square
\[
E=t^2
\]
so large that \(E\ge L\) and \(E+d\) is not a square. Such squares exist arbitrarily far out: if
\[
t^2+d=u^2,
\]
then
\[
d=(u-t)(u+t),
\]
so for fixed \(d\) only finitely many integers \(t\) can occur. For the chosen \(E\), the tail formula gives
\[
g_m^{(k)}(E)=k
\]
and
\[
g_m^{(k)}(E+d)=m+k-1,
\]
a contradiction. The case \(s<r\) is symmetric. Therefore \(r=s\), and with \(A=B\) we obtain \(a=b\). Thus \(f_m^{(k)}\) is quasi-injective for every \(k<m\).

Finally, let
\[
a=2^L,\qquad b=2^{L+1}.
\]
For arbitrary \(n=2^e u\) with \(u\) odd, both exponents \(L+e\) and \(L+1+e\) lie in the tail, so
\[
g_m^{(m)}(L+e)=g_m^{(m)}(L+1+e)=0.
\]
Consequently
\[
f_m^{(m)}(an)=u=f_m^{(m)}(bn)
\]
for every \(n\ge1\), although \(a\ne b\). Hence \(f_m^{(m)}\) is not quasi-injective.

This completes the construction for every \(m\ge2\).

## Verification
The accompanying `verify.py` instantiates the construction for every
\[
2\le m\le12.
\]
It checks the two chain formulas, the collapse
\[
g_m^{(m)}(e)=0
\]
through a long tail interval, and the explicit non-quasi-injectivity witness
\[
f_m^{(m)}(2^L n)=f_m^{(m)}(2^{L+1}n)
\]
for many values of \(n\).

For every \(k<m\), it also searches all shifts \(1\le d\le80\) and verifies on a large exponent window that a square/non-square discrepancy is found and is detected by \(g_m^{(k)}\). These finite checks are regression evidence only. The all-\(m\) proof is the symbolic argument above.

## Relationship to prior work
Pongsriiam introduced quasi-injectivity for arithmetic functions and proved, among other results, that the divisor-counting function and Jordan totients are quasi-injective to arbitrarily high order, while several standard functions fail even first-order quasi-injectivity.

The paper then asks in Question 17 whether, for each \(m\ge2\), there exists any function \(f:\mathbb N\to\mathbb N\) that is quasi-injective of order \(m-1\) but not of order \(m\). The construction above answers that existence question for every \(m\) by encoding a non-eventually-periodic square indicator into the \(2\)-adic valuation and then collapsing two finite chains exactly at the prescribed iterate.

Targeted searches for the exact phrase “quasi-injective of order”, for Question 17, for later work citing the 2021 paper, and for an explicit exact-order construction did not locate an implication-equivalent result. The closest published result found concerns sufficient conditions and concrete arithmetic functions that remain quasi-injective under iteration, which does not provide a function whose quasi-injectivity fails for the first time at a prescribed iterate.

## Limitations
The functions \(f_m\) are designed existence examples rather than familiar multiplicative or additive arithmetic functions. The construction therefore does not answer whether such exact-order behavior occurs within a narrower natural class.

The square set can be replaced by many other subsets of \(\mathbb N_0\) whose indicator is not eventually periodic under any nonzero shift; no classification of all such constructions is claimed.

The principal originality risk is an unindexed later note or informal solution to Question 17 that was not surfaced by the targeted searches.

## References
1. Prapanpong Pongsriiam, “Quasi-Injectivity of Some Arithmetic Functions,” Journal of Integer Sequences 24 (2021), Article 21.10.1, published 8 November 2021.
2. Prapanpong Pongsriiam, “Product of Some Polynomials and Arithmetic Functions,” Journal of Integer Sequences 26 (2023), Article 23.9.1.
