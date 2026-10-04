# The first multiplicity layer of quadriperfect numbers
## Finding
Let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with
multiplicity. Every quadriperfect number
\[
\sigma(n)=4n
\]
satisfies
\[
\Omega(n)\ge8.
\]
Moreover,
\[
\Omega(n)=8
\quad\Longleftrightarrow\quad
n=32760=2^3\cdot3^2\cdot5\cdot7\cdot13.
\]

## Assumptions and scope
The ordinary divisor sum is
\[
\sigma(n)=\sum_{d\mid n}d,
\]
and the abundancy index is
\[
I(n)=\frac{\sigma(n)}n.
\]
Thus a quadriperfect, or \(4\)-perfect, number satisfies \(I(n)=4\).

If
\[
n=\prod_{i=1}^r p_i^{e_i},
\]
then
\[
\Omega(n)=\sum_{i=1}^r e_i
\]
and
\[
I(n)=\prod_{i=1}^r
\left(1+\frac1{p_i}+\cdots+\frac1{p_i^{e_i}}\right).
\]

The theorem concerns total prime-factor multiplicity. It is distinct from
classical results stated in terms of \(\omega(n)\), the number of distinct
prime factors.

## Proof
For fixed \(e\ge1\), define
\[
A_e(p)=1+\frac1p+\cdots+\frac1{p^e}.
\]
This is strictly decreasing as the prime \(p\) increases.

Fix an unordered exponent partition
\[
e_1+\cdots+e_r=m.
\]
For any assignment of these exponents to \(r\) distinct primes, replacing the
ordered primes by the first \(r\) primes while preserving the exponent
assignment can only increase the abundancy. Hence the maximum abundancy for
that exponent partition is obtained by checking the finitely many assignments
of its exponents to
\[
2,3,5,7,\ldots.
\]

Performing this exact finite comparison over all exponent partitions gives the
following maximum possible abundancy for each total multiplicity
\(1\le m\le7\):
\[
\begin{array}{c|ccccccc}
m&1&2&3&4&5&6&7\\
\hline
\max I&
\frac32&
2&
\frac{12}{5}&
\frac{14}{5}&
\frac{16}{5}&
\frac{192}{55}&
\frac{208}{55}
\end{array}
\]
and every displayed value is strictly less than \(4\). Therefore
\[
\Omega(n)\ge8
\]
for every quadriperfect number.

Now put \(\Omega(n)=8\). There are twenty-two exponent partitions of \(8\).
The same exact maximum test shows that all but the following three have
maximum abundancy below \(4\):
\[
(3,2,1,1,1),\qquad
(3,1,1,1,1,1),\qquad
(2,2,1,1,1,1).
\]
Their exact maximal abundancies are respectively
\[
\frac{312}{77},\qquad
\frac{576}{143},\qquad
\frac{224}{55}.
\]

It remains to classify prime assignments for these three patterns. This is a
finite exact search with a monotone stopping certificate.

Suppose some increasing primes and exponents have already been chosen, with
partial abundancy \(R\), and let the remaining exponent multiset be \(E\).
For a proposed next prime \(p\), let
\[
q_1<\cdots<q_t
\]
be the first \(t=|E|\) primes larger than \(p\). Define
\[
U=
R\,A_e(p)\,
\max_{\pi}
\prod_{j=1}^t A_{\pi_j}(q_j),
\]
where the maximum is over the distinct permutations of the remaining
exponents. Every completion of this branch has abundancy at most \(U\),
because replacing any later prime by a smaller available prime only increases
every factor. If \(U<4\), the branch is impossible. Moreover the same is true
for every larger proposed next prime, since both the proposed factor and the
optimistic future factors decrease monotonically.

Applying this exact bound recursively to the three surviving exponent patterns
gives
\[
(3,2,1,1,1):
\quad
(2^3,3^2,5,7,13)
\]
as the unique assignment with abundancy \(4\), and gives no assignment for
the other two patterns. Therefore
\[
n=2^3\cdot3^2\cdot5\cdot7\cdot13=32760.
\]
Conversely,
\[
\frac{\sigma(32760)}{32760}
=
\frac{15}{8}\frac{13}{9}\frac65\frac87\frac{14}{13}
=4,
\]
so \(32760\) is indeed quadriperfect and has
\[
\Omega(32760)=3+2+1+1+1=8.
\]

## Verification
The packaged checker recomputes every exponent-partition maximum using exact
rational arithmetic. It verifies the seven lower-layer maxima, identifies
exactly the three exponent partitions of \(8\) whose optimistic abundancy can
reach \(4\), and reruns the monotone branch-and-bound classification from
scratch.

The checker reports exactly one solution,
\[
2^3\cdot3^2\cdot5\cdot7\cdot13,
\]
and directly verifies
\[
\sigma(32760)=4\cdot32760.
\]
No numerical floating-point comparison is used in the certificate.

## Relationship to prior work
Classical work on multiply perfect numbers is usually organized by the number
of distinct prime factors. Zhou's historical survey records Carmichael's
classification through five distinct prime factors: among the
quadriperfect cases it includes
\[
30240=2^5\cdot3^3\cdot5\cdot7
\]
at four distinct primes and
\[
32760=2^3\cdot3^2\cdot5\cdot7\cdot13
\]
at five distinct primes. The same survey distinguishes explicitly between
\(\omega(n)\) and \(\Omega(n)\).

Broughan and Zhou prove strong restrictions for odd quadriperfect numbers,
including a lower bound of twenty-two distinct prime factors. Those results
are much stronger on the odd branch but do not classify the smallest total
prime-factor multiplicity among all quadriperfect numbers.

The Multiply Perfect Numbers database records \(8\) as the fewest prime
factors among its abundance-\(4\) entries, and OEIS A027687 lists \(32760\)
among the first quadriperfect numbers. These records corroborate the extremal
value but do not supply an unrestricted proof that an arbitrarily large
quadriperfect number with fewer total prime factors cannot exist.

The result here is stated and proved in the intrinsic total-multiplicity
parameter \(\Omega\): it closes every exponent pattern below \(8\) and
classifies all exponent patterns at equality.

## Limitations
The theorem does not classify quadriperfect numbers with
\(\Omega(n)\ge9\), nor does it settle whether the presently known
quadriperfect numbers form a complete list.

Some early multiply-perfect literature is not available in searchable full
text. An equivalent low-multiplicity observation could therefore exist under
older terminology.

The earliest directly relevant sources inspected are older than the exact-day
date used in the metadata, but their public bibliographic evidence resolves
only to a year or month. The metadata uses the earliest directly relevant
primary source for which an exact public calendar date was verified.

## References
1. K. A. Broughan and Q. Zhou, "Odd multiperfect numbers of abundancy four",
   *Journal of Number Theory* 128 (2008), 1566--1575,
   DOI 10.1016/j.jnt.2007.02.001.
2. Q. Zhou, *Multiply Perfect Numbers of Low Abundancy*, Ph.D. thesis,
   University of Waikato, 2010, handle 10289/4138.
3. H.-J. Chen and H. Luo, "Odd multiperfect numbers",
   *Bulletin of the Australian Mathematical Society* 87 (2013), 510--519,
   DOI 10.1017/S0004972712000858; published online 6 November 2012.
4. A. Flammenkamp, "Multiply Perfect Numbers", computational database and
   record tables.
5. OEIS Foundation, A027687, "4-perfect (quadruply-perfect) numbers".
