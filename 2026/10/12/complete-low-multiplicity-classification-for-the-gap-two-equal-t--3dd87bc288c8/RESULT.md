# Complete low-multiplicity classification for the gap-two equal-totient equation

## Finding

Let \(\Omega(n)\) count prime factors with multiplicity. For every integer \(n\ge1\) satisfying
\[
\Omega(n)\le2,\qquad \Omega(n+2)\le2,
\]
the equality
\[
\varphi(n)=\varphi(n+2)
\]
holds if and only if one of the following occurs.

First, \(n=4\). Second, \(n=7\). Third, there are unique odd integers \(3\le A<B\) such that
\[
r=\frac{AB-A-B+3}2,\qquad
p=\frac{AB+A-B+1}2,\qquad
q=\frac{AB-A+B+1}2,\qquad
s=\frac{AB+A+B+3}2
\]
are all prime, and
\[
n=pq,\qquad n+2=rs.
\]
Conversely, every such pair \((A,B)\) gives a solution.

The parameterization is intrinsic: after ordering the four primes by \(p<q\) and \(r<s\), one has
\[
A=\frac{(s-r)-(q-p)}2,\qquad
B=\frac{(s-r)+(q-p)}2,
\]
so the parameters are uniquely recovered from the solution.

## Assumptions and scope

The theorem concerns positive integers and uses the standard convention
\[
\Omega\!\left(\prod_i p_i^{a_i}\right)=\sum_i a_i.
\]
No size bound is imposed. The low-multiplicity condition applies separately to \(n\) and \(n+2\). The result does not assert that infinitely many parameter pairs \((A,B)\) make all four displayed numbers prime.

## Proof

For \(n\le3\), direct evaluation gives no solution. Suppose first that \(n\) is even. Because \(\Omega(n)\le2\), either \(n=2\), \(n=4\), or \(n=2u\) with \(u\) an odd prime. The first case fails and \(n=4\) gives \(\varphi(4)=\varphi(6)=2\). In the third case,
\[
n+2=2(u+1).
\]
The condition \(\Omega(n+2)\le2\) would force \(u+1\) to be prime, but \(u+1>2\) is even, a contradiction. Hence \(4\) is the only even solution.

Now let \(n\) be odd. An odd integer with \(\Omega\le2\) is a prime, a prime square, or a product of two distinct odd primes. We compare the nine possible type pairs for \(n\) and \(n+2\).

If both are prime, their totients differ by \(2\). If \(n=u\) is prime and \(n+2=v^2\), then
\[
u=v^2-2,\qquad u-1=v(v-1),
\]
so \(v=3\) and \(n=7\). Reversing the types gives
\[
u(u-1)=u^2+1,
\]
which is impossible. Prime--semiprime and semiprime--prime pairs are impossible because the equal-totient identity reduces respectively to \(v+w=4\) and \(u+v=0\). Two prime squares cannot differ by \(2\).

If \(n=u^2\) and \(n+2=vw\) with distinct odd primes \(v,w\), then equal totients give
\[
v+w=u+3,\qquad vw=u^2+2.
\]
But
\[
(u+3)^2=(v+w)^2\ge4vw=4u^2+8,
\]
which is false for every odd prime \(u\ge3\). If \(n=uv\) and \(n+2=w^2\), equal totients gives \(w=u+v+1\), while \(w^2=uv+2\); substituting the first equality makes the second impossible.

It remains only the squarefree-semiprime case. Write
\[
n=pq,\qquad n+2=rs
\]
with odd primes \(p<q\) and \(r<s\). Since
\[
(p-1)(q-1)=(r-1)(s-1)
\]
and \(rs=pq+2\), subtraction gives
\[
r+s=p+q+2.
\]
Put
\[
d=q-p,\qquad e=s-r.
\]
Then
\[
e^2-d^2
=(r+s)^2-4rs-\bigl((p+q)^2-4pq\bigr)
=4(p+q-1)>0.
\]
Thus \(e>d\). Because all four primes are odd, \(d\) and \(e\) are even. Define
\[
A=\frac{e-d}2,\qquad B=\frac{e+d}2.
\]
Then
\[
AB=p+q-1.
\]
The right side is odd, so \(A\) and \(B\) are odd. Also \(0<A<B\); the case \(A=1\) would force \(r=1\), hence \(A\ge3\). Recovering the four primes from their sums and differences gives exactly
\[
r=\frac{AB-A-B+3}2,\quad
p=\frac{AB+A-B+1}2,\quad
q=\frac{AB-A+B+1}2,\quad
s=\frac{AB+A+B+3}2.
\]
This proves necessity and uniqueness.

Conversely, let \(3\le A<B\) be odd and suppose the four displayed integers are prime. Direct algebra gives
\[
rs=pq+2,\qquad r+s=p+q+2.
\]
Therefore
\[
\varphi(rs)=rs-r-s+1=pq-p-q+1=\varphi(pq),
\]
so \(n=pq\) is a solution with \(\Omega(n)=\Omega(n+2)=2\).

## Verification

The accompanying `verify.py` performs two independent finite regression checks. It verifies the algebraic identities for a grid of odd parameter pairs, and it exhaustively factors every \(n\le10^6\), retaining exactly those with \(\Omega(n),\Omega(n+2)\le2\) and equal totients. Every retained value is either \(4\), \(7\), or inverts to the stated unique parameter pair. The finite check is not used to prove the unbounded theorem.

The replay output is stored in `verification_output.txt`.

## Relationship to prior work

Ford studies the fixed-gap equations \(\varphi(n)=\varphi(n+k)\) and \(\sigma(n)=\sigma(n+k)\), and records the long-standing status of the equal-totient problem. His arXiv record gives primary MSC \(11A25\) and first public submission on 2020-02-27.

Graham, Holt, and Pomerance give general prime-generated families and, separately, a four-prime construction. For gap \(k=2\), their displayed four-prime construction is the one-parameter slice \(A=3\) of the parameterization above; it does not state or imply the complete low-\(\Omega\) classification. Their main asymptotic family for \(k=2\) is a different, predominantly even construction.

OEIS A001494 tabulates the solutions of \(\varphi(n)=\varphi(n+2)\), including \(6497\) and \(12317\), but does not classify the \(\Omega\le2\) stratum or give the two-parameter inverse formulas.

## Limitations

The theorem says nothing about solutions for which either endpoint has at least three prime factors counted with multiplicity. It also does not prove the infinitude, or even a density statement, for prime quadruples arising from the parameterization. The originality comparison cannot exclude an obscure or unindexed prior observation of the same elementary low-support reduction.

## References

1. K. Ford, “Solutions of \(\varphi(n)=\varphi(n+k)\) and \(\sigma(n)=\sigma(n+k)\),” arXiv:2002.12155; International Mathematics Research Notices 2022, no. 5, 3561–3570.
2. S. W. Graham, J. J. Holt, and C. Pomerance, “On the Solutions to \(\varphi(n)=\varphi(n+k)\),” in *Number Theory in Progress*, vol. 2, de Gruyter, 1999, 867–882.
3. S. Kim, “On the equations \(\varphi(n)=\varphi(n+k)\) and \(\varphi(p-1)=\varphi(q-1)\),” 2020.
4. OEIS A001494, “Numbers \(k\) such that \(\varphi(k)=\varphi(k+2)\).”
