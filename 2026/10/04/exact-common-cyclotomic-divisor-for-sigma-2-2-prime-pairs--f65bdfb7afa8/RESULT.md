# Exact common cyclotomic divisor for \(\sigma_{2,2}\) prime pairs

## Finding
Let \(p<q\) be odd primes satisfying
\[
p\mid q^2+q+1,
\qquad
q\mid p^2+p+1.
\]
Such a pair is called a \(\sigma_{2,2}\) pair.

Let
\[
t_1=t_2=1,
\qquad
t_{k+2}=5t_{k+1}-t_k-1.
\]
The complete quasisolution classification gives a unique index \(n\ge3\) such that
\[
p=t_n,\qquad q=t_{n+1}.
\]

Then
\[
\gcd\!\left(p^2+p+1,\ q^2+q+1\right)
=
3^{\varepsilon_3}7^{\varepsilon_7},
\]
where
\[
\varepsilon_3=
\begin{cases}
1,&n\equiv1\pmod3,\\
0,&\text{otherwise},
\end{cases}
\qquad
\varepsilon_7=
\begin{cases}
1,&n\equiv8\pmod{14},\\
0,&\text{otherwise}.
\end{cases}
\]

Consequently,
\[
\gcd\!\left(p^2+p+1,\ q^2+q+1\right)\mid21
\]
and this gcd is always squarefree.

For the three currently known prime pairs, the gcds are
\[
1,\quad3,\quad21.
\]

## Assumptions and scope
The result concerns \(\sigma_{2,2}\) prime pairs, not arbitrary pairs of primes. It uses the published complete quasisolution classification: every positive-integer solution of the reciprocal divisibility conditions is a consecutive pair in the sequence \((t_k)\).

The theorem does not prove that either individual integer
\[
p^2+p+1
\quad\text{or}\quad
q^2+q+1
\]
is squarefree. It only determines their common divisor exactly.

## Proof
For the quasisolution chain one has
\[
t_kt_{k+2}=t_{k+1}^2+t_{k+1}+1.
\]
Hence, with \(p=t_n\) and \(q=t_{n+1}\),
\[
p^2+p+1=t_{n-1}t_{n+1},
\]
and
\[
q^2+q+1=t_nt_{n+2}.
\]

Consecutive terms are coprime. Indeed, if an integer \(d>1\) divided both \(t_k\) and \(t_{k+1}\), then from
\[
5t_kt_{k+1}=t_k^2+t_{k+1}^2+t_k+t_{k+1}+1
\]
one would obtain
\[
0\equiv1\pmod d,
\]
a contradiction.

Therefore
\[
\gcd\!\left(p^2+p+1,\ q^2+q+1\right)
=
\gcd(t_{n-1},t_{n+2}).
\]
Put
\[
i=n-1,
\qquad
x=t_{i+1}.
\]
The linear recurrence gives
\[
t_{i+3}=24x-5t_i-6.
\]
Let
\[
g=\gcd(t_i,t_{i+3}).
\]
Also,
\[
t_i\mid x^2+x+1.
\]

Let \(\ell\) be a prime divisor of \(g\). Since every \(t_k\) is odd, \(\ell\ne2\). If \(\ell\ne3\), then
\[
24x\equiv6\pmod\ell,
\]
so
\[
4x\equiv1\pmod\ell.
\]
Combining this with
\[
x^2+x+1\equiv0\pmod\ell
\]
gives
\[
0
\equiv
16(x^2+x+1)
\equiv
1+4+16
=
21
\pmod\ell.
\]
Thus every prime divisor of \(g\) belongs to
\[
\{3,7\}.
\]

Neither prime can occur to the second power in \(g\).

If \(9\mid g\), then
\[
9\mid t_i
\quad\text{and}\quad
9\mid t_{i+3}.
\]
The second divisibility gives
\[
6x\equiv6\pmod9,
\]
hence
\[
x\equiv1\pmod3.
\]
Thus \(x\equiv1,4,\) or \(7\pmod9\), and in every case
\[
x^2+x+1\equiv3\pmod9,
\]
contradicting \(9\mid t_i\mid x^2+x+1\).

If \(49\mid g\), then
\[
24x\equiv6\pmod{49},
\]
so
\[
4x\equiv1\pmod{49}.
\]
Multiplying \(x^2+x+1\) by \(16\) gives
\[
16(x^2+x+1)
\equiv
1+4+16
=
21
\not\equiv0
\pmod{49},
\]
again contradicting \(49\mid t_i\mid x^2+x+1\).

Thus \(g\) is a squarefree divisor of \(21\).

It remains to decide exactly when \(3\) and \(7\) occur.

Modulo \(3\), the recurrence is periodic with period \(3\):
\[
1,1,0,\ 1,1,0,\ldots.
\]
Therefore
\[
3\mid t_j
\quad\Longleftrightarrow\quad
j\equiv0\pmod3.
\]
Since \(g=\gcd(t_i,t_{i+3})\),
\[
3\mid g
\quad\Longleftrightarrow\quad
i\equiv0\pmod3
\quad\Longleftrightarrow\quad
n\equiv1\pmod3.
\]

Modulo \(7\), the recurrence has period \(14\):
\[
1,1,3,6,5,4,0,2,2,0,4,5,6,3,
\]
and then returns to the state \((1,1)\). Hence
\[
7\mid t_j
\quad\Longleftrightarrow\quad
j\equiv7\ \text{or}\ 10\pmod{14}.
\]
Both \(t_i\) and \(t_{i+3}\) are divisible by \(7\) exactly when
\[
i\equiv7\pmod{14},
\]
equivalently
\[
n\equiv8\pmod{14}.
\]

This proves the stated formula.

## Verification
The accompanying `verify.py` checks the recurrence identities exactly, verifies the complete periods modulo \(3\) and \(7\), confirms the common-gcd formula for the first \(500\) chain positions, and evaluates the three prime pairs listed in the primary source.

The finite replay is not the proof of the all-index statement. Exhaustiveness comes from the quasisolution classification plus the algebraic reduction showing that every prime divisor of the common gcd is \(3\) or \(7\), with neither square dividing it.

A successful replay prints `VERIFY_OK`.

## Relationship to prior work
Bibby, Vyncke, and Zelinsky completely classify the positive-integer quasisolutions and use them to study \(\sigma_{2,2}\) pairs. Their paper emphasizes that such pairs are a principal obstruction in arguments about large prime divisors of odd perfect numbers. It also conjectures that
\[
p^2+p+1
\quad\text{and}\quad
q^2+q+1
\]
are individually squarefree for every \(\sigma_{2,2}\) pair.

The same source proves that a square of one member of a \(\sigma_{2,2}\) pair cannot divide the other cyclotomic value, but it does not state the exact gcd of the two full cyclotomic values.

A prior finite verification establishes the source's squarefreeness conjecture for all \(\sigma_{2,2}\) prime pairs inside the source's reported search range below \(10^{4000}\). That bounded result is logically different: the theorem here is unconditional in the chain index and determines the exact common gcd for every \(\sigma_{2,2}\) pair, including any future pair outside that search range.

OEIS A101368 records the complete quasisolution chain, and OEIS A264611/A264612 record the currently known prime pairs. These database entries do not state the exact common-gcd formula proved here.

Targeted searches for the common gcd, for the bound \(21\), for distance-three gcds in A101368, and for shared prime divisors of the two cyclotomic values did not locate a prior statement of this theorem.

## Limitations
The result controls only the overlap between the two integers
\[
p^2+p+1
\quad\text{and}\quad
q^2+q+1.
\]
It does not control square factors occurring in only one of them, so it does not resolve the squarefreeness conjecture.

Literature non-detection is not a proof that an unindexed or unpublished equivalent statement does not exist.

## References
1. Sean Bibby, Pieter Vyncke, and Joshua Zelinsky, “On the third largest prime divisor of an odd perfect number,” arXiv:1908.09420v1, first posted 26 August 2019; later published in *Integers* 22 (2022).
2. OEIS A101368, the complete quasisolution sequence for the reciprocal divisibility equations.
3. OEIS A264611 and A264612, the smaller and larger primes in known \(\sigma_{2,2}\) pairs.
