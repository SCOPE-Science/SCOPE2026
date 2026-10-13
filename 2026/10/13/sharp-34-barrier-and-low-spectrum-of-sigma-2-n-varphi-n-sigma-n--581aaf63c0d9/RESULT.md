# Sharp \(34\)-barrier and low spectrum of \(\sigma_2(n)+\varphi(n)\sigma(n)-2n^2\)
## Finding
Define
\[
H(n)=\sigma_2(n)+\varphi(n)\sigma(n)-2n^2,
\]
where
\[
\sigma_k(n)=\sum_{d\mid n}d^k.
\]

For every integer
\[
n>1,
\]
one has
\[
H(n)<34
\]
if and only if exactly one of the following holds:

\[
n\text{ is prime},\qquad H(n)=0;
\]

\[
n=pq\text{ for distinct primes }p,q,\qquad H(n)=2;
\]

or
\[
(n,H(n))\in
\{(4,3),(9,7),(8,17),(25,21)\}.
\]

The boundary value is also rigid:
\[
H(n)=34
\quad\Longleftrightarrow\quad
n=12.
\]

Equivalently, every integer having at least two distinct prime factors but not being a squarefree semiprime satisfies
\[
H(n)\ge34,
\]
with equality uniquely at
\[
n=12.
\]

Thus the complete set of values below \(34\) is
\[
\{0,2,3,7,17,21\}.
\]

## Assumptions and scope
The theorem concerns all integers \(n>1\).

For a prime power \(p^a\), define
\[
S_{p,a}=\sum_{j=0}^{a-1}p^{2j},
\qquad
R_{p,a}=p^{a-1},
\]
and
\[
h_{p,a}=S_{p,a}-R_{p,a}.
\]
Then
\[
\sigma_2(p^a)=p^{2a}+S_{p,a},
\]
while
\[
\varphi(p^a)\sigma(p^a)=p^{2a}-R_{p,a}.
\]
Hence
\[
H(p^a)=h_{p,a}.
\]

The theorem determines the entire low spectrum through the first repeated-prime mixed-support value. It does not classify arbitrary fibers above \(34\).

## Proof
For a prime power,
\[
H(p^a)
=
\sum_{j=0}^{a-1}p^{2j}-p^{a-1}.
\tag{1}
\]

If \(a=1\), then
\[
H(p)=0.
\]
If \(a=2\), then
\[
H(p^2)=p^2-p+1.
\]
The values below \(34\) occur exactly at
\[
p\in\{2,3,5\},
\]
giving
\[
H(4)=3,\qquad H(9)=7,\qquad H(25)=21.
\]

If \(a=3\), equation (1) reduces to
\[
H(p^3)=1+p^4.
\]
This is below \(34\) only for \(p=2\), giving
\[
H(8)=17.
\]

If \(a\ge4\), put
\[
x=p^{a-1}.
\]
Then
\[
x\ge8
\]
and equation (1) gives the lower bound
\[
H(p^a)\ge x^2-x+1\ge57.
\]
Thus the prime-power classification below \(34\) is complete.

Now let
\[
n=p^aq^b
\]
with distinct primes
\[
p<q.
\]
Using the notation from the scope section and expanding multiplicatively,
\[
H(p^aq^b)
=
q^{2b}h_{p,a}
+
p^{2a}h_{q,b}
+
S_{p,a}S_{q,b}
+
R_{p,a}R_{q,b}.
\tag{2}
\]

If
\[
a=b=1,
\]
then
\[
h_{p,1}=h_{q,1}=0,
\qquad
S_{p,1}=S_{q,1}=R_{p,1}=R_{q,1}=1,
\]
so
\[
H(pq)=2.
\tag{3}
\]

Suppose next that
\[
a\ge2.
\]
Then
\[
h_{p,a}\ge3,
\qquad
q^{2b}\ge9,
\qquad
S_{p,a}\ge5,
\qquad
S_{q,b}\ge1,
\qquad
R_{p,a}\ge2,
\qquad
R_{q,b}\ge1.
\]
Equation (2) yields
\[
H(p^aq^b)\ge27+5+2=34.
\]
Equality forces simultaneously
\[
p=2,\quad a=2,\quad q=3,\quad b=1,
\]
so the unique equality case in this branch is
\[
n=12.
\]

If instead
\[
a=1,\qquad b\ge2,
\]
then \(q\ge3\), and
\[
h_{q,b}\ge7,
\qquad
p^2\ge4,
\qquad
S_{q,b}\ge10,
\qquad
R_{q,b}\ge3.
\]
Equation (2) gives
\[
H(pq^b)\ge28+10+3=41.
\]
Therefore every two-prime-support integer that is not a squarefree semiprime has value at least \(34\), with equality only at \(12\).

It remains to exclude integers with at least three distinct prime factors from the low spectrum.

Let
\[
\gcd(m,p)=1,
\]
with \(m>1\), and consider adjoining a prime-power block \(p^a\). A direct expansion gives
\[
H(mp^a)
=
p^{2a}H(m)
+
S_{p,a}\sigma_2(m)
-
R_{p,a}\varphi(m)\sigma(m).
\tag{4}
\]
Now
\[
\sigma_2(m)>m^2,
\]
while
\[
\frac{\varphi(m)\sigma(m)}{m^2}
=
\prod_{r^c\parallel m}
\left(1-\frac1{r^{c+1}}\right)
<1.
\]
Hence
\[
\sigma_2(m)>\varphi(m)\sigma(m).
\]
Also
\[
S_{p,a}\ge R_{p,a}>0.
\]
Therefore the last two terms in (4) have positive total contribution, and
\[
H(mp^a)>p^{2a}H(m).
\tag{5}
\]

Equation (2) shows that every integer with exactly two distinct prime factors has
\[
H(n)\ge2.
\]
By induction on the number of distinct prime factors, (5) therefore gives
\[
H(n)\ge2
\]
for every integer with at least two distinct prime factors.

If \(n\) has at least three distinct prime factors, remove the block belonging to its largest prime \(p\). Then
\[
p\ge5
\]
and the remaining factor \(m\) still has at least two distinct prime factors. Hence
\[
H(n)>p^{2a}H(m)\ge25\cdot2=50.
\]
Thus no such integer can contribute a value below or equal to \(34\).

Combining the prime-power, two-support, and larger-support cases proves both the full spectrum below \(34\) and the unique boundary equality
\[
H(12)=34.
\]

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes the factorization, \(\sigma(n)\), \(\sigma_2(n)\), \(\varphi(n)\), and \(H(n)\) using exact integer arithmetic.

It verifies that every input with
\[
H(n)<34
\]
is either a prime, a squarefree semiprime, or one of
\[
4,\ 8,\ 9,\ 25,
\]
with exact values
\[
3,\ 17,\ 7,\ 21,
\]
respectively. It also verifies
\[
H^{-1}(34)=\{12\}
\]
through the same range.

The finite replay is corroborative only. The unrestricted theorem follows from equations (1)–(5).

## Relationship to prior work
OEIS A072780 is exactly the sequence
\[
H(n)=\sigma_2(n)+\varphi(n)\sigma(n)-2n^2.
\]
Its entry already records the fundamental facts that
\[
H(n)\ge0,
\]
with equality only at primes and \(1\), and that
\[
H(n)=2
\]
exactly for products of two distinct primes. It does not state a sharp lower bound for nonsquarefree mixed support, nor does it classify the low fibers above \(2\).

The companion OEIS A072779 records the unshifted function
\[
\sigma_2(n)+\varphi(n)\sigma(n)
\]
and the equivalent prime and squarefree-semiprime characterizations. It likewise does not give the \(34\)-barrier or the complete low spectrum.

Broughan, Ford, and Luca study the exact product
\[
\varphi(n)\sigma(n)
\]
and explicitly use the normalized Euler product
\[
\frac{\varphi(n)\sigma(n)}{n^2}
=
\prod_{p^a\parallel n}
\left(1-\frac1{p^{a+1}}\right).
\]
Their paper has primary Mathematics Subject Classification \(11A41\) and studies square values of the product rather than the additive function \(H(n)\). Its inspected full text contains no \(\sigma_2\) term and no statement implying the \(34\)-barrier.

Targeted searches using the exact database identifier, the full defining formula, low-fiber values, prime-power aliases, and mixed-support formulations did not locate an equivalent or stronger theorem.

## Limitations
The theorem determines the spectrum only through the sharp mixed-support boundary \(34\). It does not classify arbitrary larger fibers.

The known fibers \(0\) and \(2\) were already recorded in the exact database; the new content is the sharp repeated-support barrier, its equality case, and the complete intermediate spectrum.

Because the proof is elementary and the database has been public since 2002, an equivalent observation may occur in an unindexed note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A072780, \(a(n)=\sigma_2(n)+\varphi(n)\sigma(n)-2n^2\), entry authored 15 July 2002.
2. OEIS Foundation, A072779, \(a(n)=\sigma_2(n)+\varphi(n)\sigma(n)\), entry authored 15 July 2002.
3. K. A. Broughan, K. Ford, and F. Luca, “On square values of the product of the Euler totient and sum of divisors functions,” *Colloquium Mathematicum* 130 (2013), 127–137, DOI 10.4064/cm130-1-11.
