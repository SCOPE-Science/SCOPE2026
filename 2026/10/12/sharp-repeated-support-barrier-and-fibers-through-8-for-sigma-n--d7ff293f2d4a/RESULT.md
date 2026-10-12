# Sharp repeated-support barrier and fibers through \(8\) for \(\sigma(n)+\varphi(n)-2n\)
## Finding
Define
\[
z(n)=\sigma(n)+\varphi(n)-2n.
\]

For every integer \(n>1\), the complete fibers through \(8\) are
\[
z(n)=0\iff n\text{ is prime},
\]
\[
z(n)=1\iff n=p^2\text{ for a prime }p,
\]
\[
z(n)=2\iff n=pq\text{ for distinct primes }p,q,
\]
and
\[
z^{-1}(3)=\{8\},
\qquad
z^{-1}(4)=\{27\},
\qquad
z^{-1}(5)=\varnothing,
\]
\[
z^{-1}(6)=\{125\},
\qquad
z^{-1}(7)=\{16\},
\qquad
z^{-1}(8)=\{12,343\}.
\]

Structurally, every integer with exactly two distinct prime factors that is not squarefree satisfies
\[
z(n)\ge8,
\]
with equality uniquely at
\[
n=12.
\]
Every integer with at least three distinct prime factors satisfies
\[
z(n)\ge20.
\]

## Assumptions and scope
The functions are the ordinary sum-of-divisors function \(\sigma\) and Euler's totient \(\varphi\).

A useful normalized form is
\[
\rho(n)=\frac{z(n)}{n}
=
\frac{\sigma(n)}{n}
+
\frac{\varphi(n)}{n}
-2.
\tag{1}
\]

For
\[
n=\prod_i p_i^{a_i},
\]
one has
\[
\frac{\sigma(n)}{n}
=
\prod_i
\left(
1+\frac1{p_i}+\cdots+\frac1{p_i^{a_i}}
\right)
\]
and
\[
\frac{\varphi(n)}{n}
=
\prod_i
\left(1-\frac1{p_i}\right).
\tag{2}
\]

The theorem classifies exactly the fibers from \(0\) through \(8\). No claim is made about arbitrary higher fibers.

## Proof
For a prime power,
\[
n=p^a,
\]
direct calculation gives
\[
z(p^a)
=
1+p+p^2+\cdots+p^{a-2},
\tag{3}
\]
where the sum is empty, hence \(0\), when \(a=1\).

Thus
\[
z(p)=0,
\qquad
z(p^2)=1.
\]
For \(a=3\),
\[
z(p^3)=p+1,
\]
so the values at most \(8\) are
\[
z(8)=3,\quad
z(27)=4,\quad
z(125)=6,\quad
z(343)=8.
\]
For \(a=4\),
\[
z(p^4)=1+p+p^2,
\]
which is at most \(8\) only for \(p=2\), giving
\[
z(16)=7.
\]
If \(a\ge5\), then
\[
z(p^a)\ge1+2+4+8=15.
\]
This completely settles prime powers through the target range.

Now consider integers with at least two distinct prime factors. First observe that for every composite \(n\),
\[
z(n)
=
\sum_{\substack{d\mid n\\1<d<n}}
\bigl(d-\varphi(d)\bigr)
>0.
\tag{4}
\]
Indeed,
\[
\sigma(n)-n
=
\sum_{\substack{d\mid n\\d<n}}d
\]
and
\[
n-\varphi(n)
=
\sum_{\substack{d\mid n\\d<n}}\varphi(d),
\]
and subtraction gives (4).

For a fixed set of prime divisors, increasing any exponent strictly increases the first product in (2), while the second product remains unchanged. Hence \(\rho(n)\) strictly increases. Since both \(n\) and \(\rho(n)\) are then positive and increase, \(z(n)=n\rho(n)\) strictly increases as well.

Let
\[
n=p^aq^b,
\qquad
p<q
\]
be supported on two distinct primes.

If \(a=b=1\), then
\[
z(pq)
=
(p+1)(q+1)+(p-1)(q-1)-2pq
=
2.
\tag{5}
\]

Suppose the support is not squarefree. By the fixed-support monotonicity just proved, its minimum occurs when exactly one exponent is raised from \(1\) to \(2\). The two possibilities are
\[
z(p^2q)=q+2p+1
\tag{6}
\]
and
\[
z(pq^2)=p+2q+1.
\tag{7}
\]
Since \(p<q\), expression (6) is smaller. Therefore
\[
z(n)\ge q+2p+1\ge3+2\cdot2+1=8.
\]
Equality forces
\[
p=2,\qquad q=3,
\]
and the smaller repeated-prime shape is
\[
n=2^2\cdot3=12.
\]
Directly,
\[
z(12)=28+4-24=8.
\]
Thus \(12\) is the unique nonsquarefree two-prime-support integer on the boundary.

Finally suppose \(n\) has at least three distinct prime factors. For a fixed support, the squarefree radical minimizes \(z\). For three distinct primes,
\[
z(pqr)
=
(p+1)(q+1)(r+1)
+
(p-1)(q-1)(r-1)
-
2pqr
=
2(p+q+r).
\]
Hence
\[
z(pqr)\ge2(2+3+5)=20.
\tag{8}
\]

If a new prime \(r\) is adjoined to a squarefree integer \(m\), then
\[
z(mr)
=
r\,z(m)+\sigma(m)-\varphi(m)
>
r\,z(m),
\tag{9}
\]
so squarefree support larger than three cannot decrease the value. Repeated exponents increase it further by the fixed-support monotonicity. Therefore every integer with at least three distinct prime factors has \(z(n)\ge20\).

Equations (3), (5), the sharp two-support barrier, and (8) exhaust every factorization shape and prove all displayed fibers through \(8\).

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes the prime factorization, \(\sigma(n)\), \(\varphi(n)\), and \(z(n)\) exactly.

It verifies the complete classifications
\[
z^{-1}(3)=\{8\},
\quad
z^{-1}(4)=\{27\},
\quad
z^{-1}(5)=\varnothing,
\quad
z^{-1}(6)=\{125\},
\]
\[
z^{-1}(7)=\{16\},
\quad
z^{-1}(8)=\{12,343\},
\]
and independently checks that every nonsquarefree two-prime-support integer has value at least \(8\), with equality only at \(12\), while every input with at least three distinct prime factors has value at least \(20\).

The finite replay is corroborative only. The unrestricted theorem follows from formulas (3), (6), (7), fixed-support monotonicity, and the squarefree-support argument.

## Relationship to prior work
The public Puzzle 76 page introduced
\[
z(n)=\sigma(n)+\varphi(n)-2n
\]
in November 1999 and already recorded the formulas
\[
z(p)=0,\qquad
z(p^2)=1,\qquad
z(pq)=2,
\]
the prime-power formula (3), and
\[
z(pqr)=2(p+q+r)
\]
for distinct primes.

OEIS A051709 is the exact database sequence. Its comments state the \(0\)- and \(2\)-fiber characterizations, and a later comment states the \(1\)-fiber characterization and conjectures that every fiber
\[
z(n)=k,\qquad k\ge3,
\]
is finite. The inspected entry does not state the fibers \(3\) through \(8\) or the repeated-support barrier.

OEIS A278373 records the range of \(z\), and OEIS A278374 records the smallest preimage of each attained value. These tables show that \(3,4,6,7,8\) occur and that \(5\) is absent from the displayed range. OEIS A056996 likewise lists \(5\) among values not represented. These database facts do not establish uniqueness of the preimages for the attained values, nor do they exclude arbitrarily large additional solutions.

Broughan and Zhou study the related divisibility
\[
\varphi(n)\mid\sigma(n)
\]
for integers with few prime factors. Their full paper has primary Mathematics Subject Classification \(11A25\) and gives low-support structural results for a different predicate. It does not state the low fibers of \(z\).

Targeted searches for the exact sequence identifier, the defining formula, fibers \(3\) through \(8\), prime-power aliases, squarefree-semiprime aliases, and repeated-support bounds found no theorem equivalent to or stronger than the classification above.

## Limitations
The theorem determines only the fibers through \(8\). It does not prove the database conjecture that every fiber
\[
z(n)=k,\qquad k\ge3,
\]
is finite.

Several component formulas used in the proof, including the prime-power and squarefree triple formulas, were already publicly recorded. The new content is the complete uniqueness classification of the next six fibers and the sharp repeated-support barrier that excludes all other factorization shapes in that range.

An equivalent elementary observation could exist in an unindexed discussion of the puzzle or sequence.

## References
1. C. Rivera and J. McCranie, “Puzzle 76: \(z(n)=\sigma(n)+\varphi(n)-2n\),” Prime Puzzles and Problems Connection, November 1999; the defining reply is dated 10 November 1999.
2. OEIS Foundation, A051709, \(a(n)=\sigma(n)+\varphi(n)-2n\).
3. OEIS Foundation, A278373, range of A051709.
4. OEIS Foundation, A278374, smallest preimage for each value in the range of A051709.
5. OEIS Foundation, A056996, positive integers not represented by A051709.
6. K. A. Broughan and Q. Zhou, “On the Ratio of the Sum of Divisors and Euler's Totient Function II,” *Journal of Integer Sequences* 17 (2014), Article 14.9.2.
