# Prime-gap verification of the Firoozbakht, Nicholson, and Farhadian conjectures to the 85th record-gap start

## Finding
Let \(p_n\) be the \(n\)-th prime and \(g_n=p_{n+1}-p_n\). Write
\[
(i,g_i^*,p_i^*,n_i^*)
\]
for the \(i\)-th maximal prime gap, where \(g_i^*\) starts at the prime \(p_i^*=p_{n_i^*}\).

Visser proved the Firoozbakht, Nicholson, and Farhadian conjectures for all primes below the 81st maximal-gap start by checking a monotone sufficient inequality at the beginning of each record-gap interval.

Using the now-known 81st through 85th maximal-gap data, the same method proves all three conjectures for every prime
\[
p<101412319996363309069=p_{85}^*.
\]

The new intervals are those beginning at \(i=81,82,83,84\). Their data are
\[
\begin{array}{c|c|c|c}
i&g_i^*&p_i^*&n_i^*\\
\hline
81&1552&18470057946260698231&426181820436140029\\
82&1572&18571673432051830099&428472240920394477\\
83&1676&20733746510561442863&477141032543986017\\
84&1724&68068810283234182907&1524717378371224128.
\end{array}
\]
The next record starts at
\[
p_{85}^*=101412319996363309069.
\]

## Assumptions and scope
The argument uses Visser's sufficient conditions and his interval reduction. For Nicholson and therefore also Firoozbakht, define
\[
F_N(n)=\bigl(\log(n\log n)-1\bigr)\log(n\log n).
\]
For Farhadian, define
\[
F_F(n)=\bigl(\log(n\log n)-1\bigr)
\left(
\log(n\log n)+\log\log n
-\log\log\bigl(n\log(n\log n)\bigr)
\right).
\]
Visser proves that
\[
g_n<F_N(n)
\]
is sufficient for Nicholson and Firoozbakht, while
\[
g_n<F_F(n)
\]
is sufficient for Farhadian in the range relevant here.

The published paper already verifies all primes below \(p_{81}^*\). This note checks only the four newly required record intervals \(i=81,82,83,84\).

## Proof
For every prime \(p_n\) in the interval
\[
p_i^*\le p_n<p_{i+1}^*,
\]
maximality of the record gap gives
\[
g_n\le g_i^*.
\]
Also \(n\ge n_i^*\).

Both sufficient-bound functions are increasing throughout the present range. For \(F_N\) this is immediate from the increase of \(\log(n\log n)\). For \(F_F\), put \(x=\log n\), \(A=x+\log x\), and \(D=x+\log A\). The second factor is
\[
H(x)=x+2\log x-\log D.
\]
Here
\[
H'(x)
=
1+\frac{2}{x}
-
\frac{1+(1+1/x)/A}{D}>0
\]
for \(x>1\), while \(A-1\) is also increasing and positive in the range used. Hence \(F_F\) is increasing.

The exact high-precision evaluations are:
\[
\begin{array}{c|c|c|c}
i&g_i^*&F_N(n_i^*)&F_F(n_i^*)\\
\hline
81&1552&1917.949451223486\ldots&1914.083858863411\ldots\\
82&1572&1918.430543341346\ldots&1914.564828009082\ldots\\
83&1676&1928.099677839286\ldots&1924.231497579769\ldots\\
84&1724&2034.018944617813\ldots&2030.124554377869\ldots.
\end{array}
\]
Thus, for every \(i\in\{81,82,83,84\}\),
\[
g_i^*<F_F(n_i^*)<F_N(n_i^*).
\]
Therefore both sufficient inequalities hold for every prime throughout each interval
\[
[p_i^*,p_{i+1}^*).
\]

Combining these four intervals with Visser's published verification below \(p_{81}^*\) proves all three conjectures for every prime
\[
p<p_{85}^*=101412319996363309069.
\]

## Verification
The accompanying `verify.py` stores the four new record widths and prime indices as exact integers, evaluates both sufficient bounds with 80-digit decimal logarithms, and checks
\[
g_i^*<F_F(n_i^*)<F_N(n_i^*)
\]
for \(i=81,82,83,84\).

The computation is not an exhaustive scan of all intervening primes. The proof that four evaluations suffice is the record-gap interval argument above.

## Relationship to prior work
Visser's 2019 paper proves the three conjectures below the then-unknown 81st maximal-gap start, and gives \(2^{64}\) as an explicit safe frontier. The paper explicitly notes that each newly discovered maximal gap, together with its prime index, can extend the verification by the same method.

Current record-gap tables now contain the starts through the 85th maximal gap. The four additional interval checks above move the common verified frontier to the start of the 85th record gap,
\[
101412319996363309069,
\]
which is more than five times the published explicit \(2^{64}\) scale.

Exact-title, conjecture-name, 84th/85th-record-gap, and endpoint-number searches did not locate an indexed publication stating this updated common frontier for all three conjectures.

## Limitations
This is a finite verification, not a proof of any of the three conjectures for all primes. It depends on the correctness of the published maximal-gap starts, widths, and prime indices.

The argument stops just before \(p_{85}^*\). Extending across the interval beginning at \(p_{85}^*\) would require a certified lower endpoint for the next maximal gap, or another independent gap bound covering that region.

## References
1. Matt Visser, “Verifying the Firoozbakht, Nicholson, and Farhadian conjectures up to the 81st maximal prime gap,” arXiv:1904.00499v1, first posted 31 March 2019; *Mathematics* 7 (2019), 691.
2. OEIS A005250, record gaps between primes.
3. OEIS A002386, lower endpoints of record prime gaps.
4. OEIS A005669 and current record-gap tables for the prime indices of maximal-gap starts.
