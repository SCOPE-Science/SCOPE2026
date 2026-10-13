# A sharp three-factor obstruction for integral means of \(\varphi(n)\) and \(\sigma(n)\)
## Finding
For an integer \(n>1\), define the arithmetic, geometric, and harmonic means of Euler's totient and the sum-of-divisors function by
\[
M_A(n)=\frac{\varphi(n)+\sigma(n)}2,\qquad
M_G(n)=\sqrt{\varphi(n)\sigma(n)},\qquad
M_H(n)=\frac{2\varphi(n)\sigma(n)}{\varphi(n)+\sigma(n)}.
\]
Let \(\Omega(n)\) denote the number of prime factors of \(n\), counted with multiplicity.

**Theorem.** For every integer \(n>1\), simultaneous integrality of all three means implies
\[
\Omega(n)\ge3.
\]
The bound is sharp. The integers
\[
418=2\cdot11\cdot19,\qquad 477=3^2\cdot53
\]
both satisfy all three integrality conditions, and each has exactly three prime factors counted with multiplicity.

The key stronger fact is independent of primality:

**Integer-pair obstruction.** For all integers \(x,y\ge2\), put
\[
u=(x-1)(y-1),\qquad v=(x+1)(y+1).
\]
The arithmetic mean of \(u,v\) is always \(xy+1\), but their geometric and harmonic means cannot both be integers.

## Assumptions and scope
Throughout, \(\sigma(n)=\sum_{d\mid n}d\) is the ordinary positive-divisor sum and \(\varphi(n)\) is Euler's totient. The three means are the usual means of the two positive integers \(\varphi(n),\sigma(n)\).

OEIS A065146 tabulates precisely those \(n\) for which all three means are integral. This theorem determines the minimum possible multiplicity of a nontrivial index in that sequence, not the complete sequence or its density.

## Proof
We first prove the integer-pair obstruction.

Let \(x,y\ge2\) be integers and set
\[
u=(x-1)(y-1),\qquad v=(x+1)(y+1),
\qquad S=\frac{u+v}{2}=xy+1,\quad T=\frac{v-u}{2}=x+y.
\]
Then \(S>T>0\) and
\[
uv=S^2-T^2.
\tag{1}
\]
Suppose for a contradiction that both the geometric mean \(G=\sqrt{uv}\) and harmonic mean \(H=uv/S\) are integers.

Put \(d=\gcd(S,T)\), \(a=S/d\), and \(c=T/d\). Thus \(\gcd(a,c)=1\), \(a>c\ge1\), and equation (1) says
\[
G^2=d^2(a^2-c^2).
\]
As \(G\) and \(d\) are integers, \(d^2\mid G^2\) implies \(d\mid G\). Write \(G=db\) for a positive integer \(b\). Therefore
\[
a^2=b^2+c^2,\qquad \gcd(a,b)=1.
\tag{2}
\]
The integrality of the harmonic mean yields
\[
H=\frac{G^2}{S}=\frac{db^2}{a}\in\mathbb Z.
\]
Since \(\gcd(a,b)=1\), we must have
\[
a\mid d.
\tag{3}
\]

Define two integers
\[
X=cx-a,\qquad Y=cy-a.
\]
They are strictly positive: indeed
\[
\frac ac=\frac{xy+1}{x+y}<x
\]
because \(x^2>1\), and similarly \(a/c<y\). Moreover, the relation \(c(xy+1)=a(x+y)\) gives
\[
XY=c^2xy-ac(x+y)+a^2=a^2-c^2=b^2.
\tag{4}
\]
For positive integers \(X,Y\), the elementary inequality \((X-1)(Y-1)\ge0\) gives
\[
X+Y\le XY+1=b^2+1.
\tag{5}
\]
On the other hand, by (3), \(d\ge a\), whence
\[
a c^2\le d c^2=c(x+y)=2a+X+Y.
\]
Combining this with (2), (4), and (5) yields
\[
a c^2\le2a+b^2+1=(a+1)^2-c^2,
\]
so
\[
c^2\le a+1.
\tag{6}
\]
But \(b=1\) is impossible in (2): then \((a-c)(a+c)=1\), contradicting \(c\ge1\). Thus \(b\ge2\), and since \(a>b\), equation (2) implies
\[
c^2=(a-b)(a+b)\ge a+b\ge a+2,
\]
contradicting (6). This proves the integer-pair obstruction.

Now suppose \(n>1\) has \(\Omega(n)\le2\). There are exactly three factorization types.

If \(n=p\) is prime, then
\[
\varphi(p)\sigma(p)=(p-1)(p+1)=p^2-1.
\]
As \((p-1)^2<p^2-1<p^2\), the geometric mean is not integral.

If \(n=p^2\) is a prime square, then
\[
\varphi(p^2)+\sigma(p^2)=p(p-1)+(p^2+p+1)=2p^2+1,
\]
so its arithmetic mean is not integral.

Finally, if \(n=pq\) with distinct primes \(p,q\), then
\[
\varphi(pq)=(p-1)(q-1),\qquad
\sigma(pq)=(p+1)(q+1).
\]
The integer-pair obstruction with \(x=p,y=q\) shows that the geometric and harmonic means cannot both be integers.

Thus no \(n>1\) with \(\Omega(n)\le2\) satisfies all three integrality conditions.

For sharpness, the two explicit witnesses have
\[
\begin{array}{c|c|c|c|c|c}
n&\varphi(n)&\sigma(n)&M_A(n)&M_G(n)&M_H(n)\\\hline
418&180&720&450&360&288\\
477&312&702&507&468&432
\end{array}
\]
and \(\Omega(418)=\Omega(477)=3\). All displayed values follow from the standard multiplicative formulas, proving sharpness.

## Verification
The accompanying `verify.py` uses exact integer sieving and arithmetic. It tests every pair of integers
\[
2\le x\le y\le1200
\]
against the integer-pair obstruction, a total of \(719400\) pairs, and tests every integer
\[
2\le n\le1{,}000{,}000.
\]
Within that range, all \(288533\) integers with \(\Omega(n)\le2\) fail the simultaneous-means condition. Including \(n=1\), it finds \(67\) simultaneous-means indices, agrees with the initial exact OEIS table, and records \(418,477\) as the first examples with minimum multiplicity \(3\).

These checks corroborate the theorem; the symbolic proof above is unrestricted.

## Relationship to prior work
OEIS A065146 is the exact database of simultaneous integrality of the three means of \(\varphi(n)\) and \(\sigma(n)\). It lists initial values and computational generation methods, including \(418\) and \(477\), but does not state a global lower bound on \(\Omega(n)\) or the integer-pair obstruction.

OEIS A011257 is the **broader geometric-only** sequence, recording indices where \(\varphi(n)\sigma(n)\) is a square. It contains squarefree semiprimes, for example \(n=14\). The geometric condition alone therefore does not imply the exclusion here. OEIS A065150 imposes the harmonic-only condition and likewise includes squarefree semiprimes, for example \(n=15\). These two broader conditions separately admit semiprimes, while their intersection does not.

Broughan, Ford, and Luca study square values of the same product \(\varphi(n)\sigma(n)\). Their Theorem 1 excludes prime powers from that geometric-only set and bounds indices in each fixed square-root defect class; Theorem 2 estimates the number of such classes. The inspected full text does not impose integral harmonic mean, and neither theorem excludes semiprimes from the intersection. In particular, the semiprime constructions in their introduction show why an additional argument is necessary.

Targeted searches of the exact database identifiers, integral-means formulation, and semiprime/low-multiplicity aliases found no covering theorem. The new contribution is the unrestricted simultaneous obstruction and its sharp prime-factor consequence, not the already tabulated witnesses.

## Limitations
The theorem provides a necessary and sharp prime-factor-count condition; it does not characterize all integers with \(\Omega(n)=3\) satisfying the three integrality requirements. It does not determine the density, asymptotic number, or infinitude of the full sequence.

An equivalent elementary observation might exist in an unindexed discussion of the sequence or the arithmetic of integer means; the searches and inspected sources cannot rule out all unpublished or unindexed observations.

## References
1. OEIS Foundation, A065146, “Numbers n such that the arithmetic, geometric and harmonic means of phi(n) and sigma(n) are all integers,” first authored 18 October 2001.
2. OEIS Foundation, A011257, integers for which the geometric mean of \(\varphi(n)\) and \(\sigma(n)\) is an integer.
3. OEIS Foundation, A065150, integers for which the harmonic mean of \(\varphi(n)\) and \(\sigma(n)\) is an integer.
4. K. Broughan, K. Ford, and F. Luca, “On square values of the product of the Euler totient and sum of divisors functions,” *Colloquium Mathematicum* 130 (2013), 127–137, DOI 10.4064/cm130-1-11.
