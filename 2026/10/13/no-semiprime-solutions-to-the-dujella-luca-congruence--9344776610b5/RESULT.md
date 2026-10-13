# No semiprime solutions to the Dujella–Luca congruence
## Finding
Let \(\varphi\) be Euler's totient function, let \(\sigma\) be the sum-of-divisors function, and let \(\Omega(n)\) count prime factors with multiplicity. Then
\[
n\varphi(n)\equiv2\pmod{\sigma(n)},\qquad \Omega(n)\le2,
\]
holds exactly for
\[
n=1,
\]
for every prime \(n\), and for
\[
n=9.
\]
In particular, no squarefree semiprime satisfies the congruence, and \(9\) is the unique composite solution in the complete multiplicity layer \(\Omega(n)\le2\).

## Assumptions and scope
Congruences modulo \(1\) are interpreted in the usual way, so \(n=1\) satisfies the displayed congruence. For \(n>1\), the condition \(\Omega(n)\le2\) leaves only three shapes:
\[
n=p,\qquad n=p^2,\qquad n=pq
\]
with primes \(p<q\).

The result concerns the congruence
\[
n\varphi(n)\equiv2\pmod{\sigma(n)}
\]
studied by Dujella and Luca. It is distinct from Subbarao's original congruence with \(\sigma\) and \(\varphi\) interchanged.

## Proof
Every prime is a solution. Indeed, for prime \(p\),
\[
p\varphi(p)-2
=
p(p-1)-2
=
(p+1)(p-2),
\]
so
\[
p\varphi(p)\equiv2\pmod{p+1}
\]
and \(\sigma(p)=p+1\).

Now let
\[
n=p^2.
\]
Then
\[
\sigma(p^2)=p^2+p+1=:D
\]
and
\[
p^3\equiv1\pmod D
\]
because
\[
p^3-1=(p-1)D.
\]
Hence
\[
n\varphi(n)=p^3(p-1)\equiv p-1\pmod D.
\]
The required congruence is therefore equivalent to
\[
D\mid p-3.
\]
Since \(D>|p-3|\) for every prime \(p\), this forces
\[
p=3.
\]
Thus the unique prime-square solution is
\[
n=9.
\]

It remains to exclude squarefree semiprimes
\[
n=pq,\qquad p<q.
\]
Here
\[
\sigma(n)=(p+1)(q+1),\qquad
\varphi(n)=(p-1)(q-1).
\]

First suppose
\[
p=2.
\]
Reduction modulo \(q+1\) gives
\[
2q(q-1)-2\equiv2\pmod{q+1}.
\]
Thus the congruence would force
\[
q+1\mid2,
\]
which is impossible because \(q\ge3\).

Now suppose \(p\) and \(q\) are both odd. Reduction modulo \(q+1\) gives
\[
q+1\mid2(p^2-p-1),
\]
and reduction modulo \(p+1\) gives
\[
p+1\mid2(q^2-q-1).
\]
For every odd integer \(r\), the number
\[
r^2-r-1
\]
is odd. Therefore the right side of each divisibility has exact \(2\)-adic valuation \(1\). Since \(p+1\) and \(q+1\) are even, it follows that
\[
\nu_2(p+1)=\nu_2(q+1)=1,
\]
so
\[
p\equiv q\equiv1\pmod4.
\]

Consequently
\[
16\mid pq(p-1)(q-1)=n\varphi(n),
\]
and hence
\[
\nu_2\bigl(n\varphi(n)-2\bigr)=1.
\]
But
\[
\nu_2(\sigma(n))
=
\nu_2(p+1)+\nu_2(q+1)
=
2.
\]
Therefore \(\sigma(n)\) cannot divide \(n\varphi(n)-2\), a contradiction.

All possibilities with \(\Omega(n)\le2\) have now been exhausted.

## Verification
The attached `verify.py` independently checks every integer
\[
1\le n\le2{,}000{,}000
\]
with
\[
\Omega(n)\le2.
\]
It verifies that the solutions are exactly \(1\), all primes in the range, and \(9\), with no squarefree-semiprime hit.

The script also checks the exact prime-square reduction
\[
p^2+p+1\mid p-3
\]
on a finite prime sample and checks the two congruence reductions used for odd semiprimes.

The finite replay is corroborative only. The theorem for all integers follows from the complete three-shape proof above.

## Relationship to prior work
Dujella and Luca study exactly
\[
n\varphi(n)\equiv2\pmod{\sigma(n)}.
\]
Their paper reports the earlier prime-power classification: the only nonprime prime powers satisfying the congruence are \(8\) and \(9\). It proves that only finitely many solutions can use primes from any fixed finite set, and it determines the fixed support \(\{2,3\}\) exactly as
\[
1,2,3,8,9.
\]
The paper explicitly says that its effective method quite likely extends to every fixed two-prime support, but that the details were not worked out.

The present result is different from a fixed-support theorem. It lets both primes vary and completely resolves the first global multiplicity layer. The prime-square part specializes the published prime-power classification; the new structural step is the uniform exclusion of every squarefree semiprime.

Bujačić later proves that the solutions with prime support contained in \(\{2,5\}\) are exactly
\[
1,2,5,8.
\]
That theorem excludes the single semiprime \(10\) inside its fixed support, but it does not imply the uniform exclusion for arbitrary prime pairs.

Targeted statement searches using the exact congruence, the phrases “semiprime,” “squarefree semiprime,” “two prime factors,” and the equivalent \(\Omega(n)\le2\) formulation did not locate a same or stronger classification.

## Limitations
The theorem says nothing about composite solutions with
\[
\Omega(n)\ge3.
\]
In particular, it does not classify numbers supported on two primes when one or both exponents make the total multiplicity at least \(3\). The published example \(8\) already lies at multiplicity \(3\).

The semiprime obstruction is elementary, so an equivalent argument could occur in an unindexed problem note or discussion. The closest inspected papers instead treat fixed prime supports and do not state the variable-prime semiprime exclusion.

## References
1. A. Dujella and F. Luca, “On a variation of a congruence of Subbarao,” *Journal of the Australian Mathematical Society* 93 (2012), 85–90, DOI 10.1017/S1446788712000614; first published online 4 February 2013.
2. S. Bujačić, “A variation of a congruence of Subbarao for \(n=2^{\alpha}5^{\beta}\),” arXiv:1607.01258v1, 5 July 2016; later *Periodica Mathematica Hungarica* 75 (2017), 66–79.
