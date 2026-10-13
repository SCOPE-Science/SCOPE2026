# Prime-power isolation below the sharp \(12\)-barrier for \(n^2-\varphi(n)\sigma(n)\)
## Finding
Define
\[
F(n)=n^2-\varphi(n)\sigma(n).
\]

For every integer \(n>1\) having at least two distinct prime factors,
\[
F(n)\ge12,
\]
with equality if and only if
\[
n=6.
\]

Hence
\[
F(n)<12
\]
if and only if \(n=p^a\) is a prime power with
\[
p^{a-1}<12.
\]
The complete low spectrum is therefore
\[
F^{-1}(1)=\{\text{primes}\},
\quad
F^{-1}(2)=\{4\},
\quad
F^{-1}(3)=\{9\},
\quad
F^{-1}(4)=\{8\},
\quad
F^{-1}(5)=\{25\},
\]
\[
F^{-1}(6)=\varnothing,
\quad
F^{-1}(7)=\{49\},
\quad
F^{-1}(8)=\{16\},
\quad
F^{-1}(9)=\{27\},
\quad
F^{-1}(10)=\varnothing,
\quad
F^{-1}(11)=\{121\},
\]
and the boundary fiber is
\[
F^{-1}(12)=\{6\}.
\]

## Assumptions and scope
The functions are Euler's totient \(\varphi\) and the ordinary sum-of-divisors function \(\sigma\).

For
\[
n=\prod_i p_i^{a_i},
\]
multiplicativity gives the exact identity
\[
\frac{\varphi(n)\sigma(n)}{n^2}
=
\prod_i\left(1-\frac1{p_i^{a_i+1}}\right).
\tag{1}
\]

The theorem gives a sharp support barrier and the complete fibers through \(12\). It does not classify arbitrary larger fibers.

## Proof
For a prime power
\[
n=p^a,
\]
direct calculation from (1) gives
\[
F(p^a)
=
p^{2a}
\left(1-\left(1-\frac1{p^{a+1}}\right)\right)
=
p^{a-1}.
\tag{2}
\]

Now suppose \(n\) has at least two distinct prime factors. Choose two distinct prime-power blocks
\[
p^a\parallel n,\qquad q^b\parallel n,\qquad p<q,
\]
and write
\[
n=mp^aq^b.
\]
Let
\[
A=1-\frac1{p^{a+1}},
\qquad
B=1-\frac1{q^{b+1}},
\]
and let
\[
D=\prod_{r^c\parallel m}\left(1-\frac1{r^{c+1}}\right).
\]
Then
\[
0<D\le1.
\]
Using (1),
\[
F(n)
=
m^2p^{2a}q^{2b}(1-ABD)
\ge
m^2p^{2a}q^{2b}(1-AB).
\tag{3}
\]
A direct expansion yields
\[
p^{2a}q^{2b}(1-AB)
=
p^{a-1}q^{b-1}
\left(q^{b+1}+p^{a+1}-1\right).
\tag{4}
\]
Since
\[
m\ge1,\qquad
p\ge2,\qquad
q\ge3,\qquad
a,b\ge1,
\]
equations (3) and (4) imply
\[
F(n)
\ge
q^2+p^2-1
\ge
3^2+2^2-1
=
12.
\]

For equality, every inequality above must be an equality. Thus \(m=1\), \(a=b=1\), \(p=2\), and \(q=3\), so
\[
n=6.
\]
Conversely,
\[
F(6)=36-\varphi(6)\sigma(6)=36-2\cdot12=12.
\]

It remains to enumerate the values below \(12\). By the support barrier, every such \(n>1\) is a prime power. By (2), one needs
\[
p^{a-1}<12.
\]
For \(a=1\), every prime gives value \(1\). For \(a=2\),
\[
p\in\{2,3,5,7,11\},
\]
giving \(4,9,25,49,121\). For \(a=3\),
\[
p\in\{2,3\},
\]
giving \(8,27\). For \(a=4\), only \(p=2\) is possible, giving \(16\). If \(a\ge5\), then
\[
p^{a-1}\ge2^4=16,
\]
so no further low values occur. This proves every displayed fiber, including the gaps at \(6\) and \(10\).

## Verification
The attached `verify.py` independently checks every integer
\[
2\le n\le2{,}000{,}000.
\]
It computes the prime factorization, \(\varphi(n)\), \(\sigma(n)\), and \(F(n)\) with exact integer arithmetic.

For every integer with at least two distinct prime factors it asserts
\[
F(n)\ge12
\]
and checks that equality occurs only at \(6\). It independently verifies the complete nonprime sub-\(12\) list
\[
(4,2),(8,4),(9,3),(16,8),(25,5),(27,9),(49,7),(121,11).
\]

The finite replay is corroborative only. The unrestricted theorem follows from the Euler-product identity and inequalities (3)–(4).

## Relationship to prior work
OEIS A069249 is exactly the sequence
\[
F(n)=n^2-\varphi(n)\sigma(n).
\]
Its entry records positivity, the characterization \(F(n)=1\) at primes, and the prime-power formula
\[
F(p^a)=p^{a-1}.
\]
It does not state a sharp lower bound for integers with at least two distinct prime factors or the complete fibers through \(12\).

OEIS A164875 records the record-holders of the same difference and cites the classical positivity of
\[
n^2-\varphi(n)\sigma(n).
\]
It supplies extremal table context but not a support-stratified lower bound.

Broughan, Ford, and Luca study the product \(\varphi(n)\sigma(n)\) in depth. Their full paper uses the same Euler product (1) and investigates when \(\varphi(n)\sigma(n)\) is a square. It does not study the additive difference
\[
n^2-\varphi(n)\sigma(n)
\]
or the sharp \(12\)-barrier.

Targeted searches using the exact database identifier, the difference formula, prime-power aliases, mixed prime support, and the value \(12\) did not locate an equivalent or stronger statement.

## Limitations
The theorem classifies only the low spectrum through the first mixed-support value \(12\). It does not describe the fibers above \(12\), their density, or their maximal multiplicities.

Because the proof is elementary and the defining sequence has been public since 2002, an equivalent short argument may occur in an unindexed note or discussion not surfaced by the searches.

## References
1. OEIS Foundation, A069249, \(a(n)=n^2-\varphi(n)\sigma(n)\), entry authored 13 April 2002.
2. OEIS Foundation, A164875, record holders for \(n^2-\varphi(n)\sigma(n)\).
3. K. A. Broughan, K. Ford, and F. Luca, “On square values of the product of the Euler totient and sum of divisors functions,” *Colloquium Mathematicum* 130 (2013), 127–137, DOI 10.4064/cm130-1-11.
