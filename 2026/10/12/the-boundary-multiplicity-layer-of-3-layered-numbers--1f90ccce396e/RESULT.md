# The boundary multiplicity layer of \(3\)-layered numbers
## Finding
A positive integer is called \(3\)-layered when its positive divisors can be partitioned into three disjoint sets having the same sum. Let \(\Omega(n)\) count prime factors with multiplicity. Then every \(3\)-layered integer satisfies
\[
\Omega(n)\ge 5,
\]
and equality holds exactly for
\[
n\in\{120,180,420,660,780\}.
\]
Thus the first multiplicity layer is finite and completely determined.

## Assumptions and scope
All integers are positive. Write \(\sigma(n)\) for the sum of positive divisors and \(I(n)=\sigma(n)/n\) for abundancy. If \(n\) is \(3\)-layered, each layer has sum \(\sigma(n)/3\). Since one layer contains the divisor \(n\), necessarily
\[
I(n)\ge 3.
\]
This necessary inequality is the only external structural input needed in the exclusion argument; it also follows immediately from the definition. No assertion is made here about \(3\)-layered numbers with \(\Omega(n)\ge6\).

## Proof
For a prime \(p\) and \(a\ge0\), put
\[
I(p^a)=1+p^{-1}+\cdots+p^{-a}.
\]
We first record an exchange observation. If \(a>b\ge0\) and \(p<q\) are primes, then
\[
I(p^a)I(q^b)>I(p^b)I(q^a).
\]
Indeed, for \(S_m(x)=1+x+\cdots+x^m\), the ratio \(S_a(x)/S_b(x)\) is strictly increasing on \(0<x<1\). One way to see this is to differentiate logarithmically: \(xS_m'(x)/S_m(x)\) is the weighted mean of \(0,1,\ldots,m\) with weights \(1,x,\ldots,x^m\), and adjoining the terms of degrees \(b+1,\ldots,a\) strictly raises that mean. Taking \(x=1/p>1/q\) proves the exchange inequality. Consequently, for a fixed exponent partition, abundancy is maximized by using the smallest available primes and assigning the largest exponents to the smallest primes.

For \(\Omega(n)\le4\), the exponent partitions give the following maximal abundancies:

| \(\Omega\) | exponent partition | maximal \(I(n)\) |
| --- | --- | --- |
| \(1\) | \((1)\) | \(3/2\) |
| \(2\) | \((2)\) | \(7/4\) |
| \(2\) | \((1,1)\) | \(2\) |
| \(3\) | \((3)\) | \(15/8\) |
| \(3\) | \((2,1)\) | \(7/3\) |
| \(3\) | \((1,1,1)\) | \(12/5\) |
| \(4\) | \((4)\) | \(31/16\) |
| \(4\) | \((3,1)\) | \(5/2\) |
| \(4\) | \((2,2)\) | \(91/36\) |
| \(4\) | \((2,1,1)\) | \(14/5\) |
| \(4\) | \((1,1,1,1)\) | \(96/35\) |

Every entry is less than \(3\), so a \(3\)-layered integer must have \(\Omega(n)\ge5\).

Now suppose \(\Omega(n)=5\). The exponent partitions are
\[
(5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1,1,1,1,1).
\]
The first three have respective maximal abundancies
\[
\frac{63}{32},\qquad \frac{31}{12},\qquad \frac{65}{24},
\]
all below \(3\). For \((3,1,1)\), the maximum is attained uniquely at \(2^3\cdot3\cdot5=120\), where \(I(120)=3\). Hence this pattern contributes only \(120\).

For pattern \((2,2,1)\), the largest value is
\[
I(2^2\cdot3^2\cdot5)=\frac{91}{30}>3.
\]
If the prime set is not \(\{2,3,5\}\), the largest possible value is
\[
I(2^2\cdot3^2\cdot7)=\frac{26}{9}<3.
\]
On the prime set \(\{2,3,5\}\), moving one square from \(3\) to \(5\) gives at most
\[
I(2^2\cdot3\cdot5^2)=\frac{217}{75}<3,
\]
and the remaining assignment is smaller. Thus this pattern contributes only \(180=2^2\cdot3^2\cdot5\).

For pattern \((2,1,1,1)\), the squared prime must be \(2\), because the largest case with another squared prime is
\[
I(2\cdot3^2\cdot5\cdot7)=\frac{104}{35}<3.
\]
Write the remaining odd primes as \(q<r<s\). If \(q\ge5\), then
\[
I(2^2\cdot5\cdot7\cdot11)=\frac{144}{55}<3,
\]
so \(q=3\). If \(r\ge7\), then
\[
I(2^2\cdot3\cdot7\cdot11)=\frac{32}{11}<3,
\]
so \(r=5\). Therefore
\[
I(2^2\cdot3\cdot5\cdot s)=\frac{14}{5}\frac{s+1}{s}\ge3,
\]
which is equivalent to \(s\le14\). The possible primes are \(s\in\{7,11,13\}\), giving \(420,660,780\).

Finally, in the squarefree pattern \((1,1,1,1,1)\),
\[
I(n)\le I(2\cdot3\cdot5\cdot7\cdot11)=\frac{1152}{385}<3.
\]
This proves that the necessary abundancy condition leaves exactly the five displayed integers.

It remains to prove that all five are genuinely \(3\)-layered. The following are complete partitions of their divisor sets; each row has the common sum \(\sigma(n)/3\):

- \(120\): \(\{120\}\); \(\{60,40,20\}\); \(\{30,24,15,12,10,8,6,5,4,3,2,1\}\).
- \(180\): \(\{180,2\}\); \(\{90,60,20,12\}\); \(\{45,36,30,18,15,10,9,6,5,4,3,1\}\).
- \(420\): \(\{420,28\}\); \(\{210,140,84,14\}\); \(\{105,70,60,42,35,30,21,20,15,12,10,7,6,5,4,3,2,1\}\).
- \(660\): \(\{660,12\}\); \(\{330,220,110,11,1\}\); \(\{165,132,66,60,55,44,33,30,22,20,15,10,6,5,4,3,2\}\).
- \(780\): \(\{780,4\}\); \(\{390,260,130,3,1\}\); \(\{195,156,78,65,60,52,39,30,26,20,15,13,12,10,6,5,2\}\).

The three sums are respectively \(120,182,448,672,784\). Thus all five candidates are \(3\)-layered, completing the classification.

## Verification
The accompanying `verify.py` uses exact integer and rational arithmetic. It verifies the displayed extremal abundancy values, checks that each of the five integers has \(\Omega(n)=5\), reconstructs its full divisor set, and verifies that the listed three subsets are disjoint, exhaustive, and have equal sums. Its successful output is

`VERIFY_OK omega_boundary=5 candidates=5 partitions=5`.

This finite replay checks the arithmetic and the explicit certificates; the universal exclusion is the symbolic exponent-partition argument above.

## Relationship to prior work
Jokar's 2022 paper studies \(k\)-layered numbers, records \(120\) as the smallest \(3\)-layered number, and gives the general necessary condition \(I(n)\ge k\). The checked full text does not state a classification by \(\Omega(n)\) at the first possible multiplicity layer. Mahanta, Saikia, and Yaqubi characterize \(k\)-layered numbers with two distinct prime factors; that result does not cover the three- and four-prime-support cases occurring here. OEIS A204830 lists \(3\)-layered numbers and includes all five integers above, but its table is an enumeration by size rather than a proof that these are exactly the members with \(\Omega(n)=5\).

A closely related published-finding corpus record determines the boundary \(\Omega=5\) for triperfect numbers and obtains only \(120\). That statement concerns the stronger equation \(\sigma(n)=3n\); the present classification concerns divisor partitions into three equal sums, for which \(180,420,660,780\) have abundancy strictly greater than \(3\). Thus the triperfect boundary does not imply this result.

## Limitations
The result classifies only the minimum possible multiplicity layer \(\Omega(n)=5\). It does not classify \(3\)-layered integers at larger multiplicity, and it does not claim that the abundancy condition \(I(n)\ge3\) is sufficient in general. The originality assessment is based on targeted searches and inspection of the most directly relevant sources; specialized or unindexed literature remains a residual risk.

## References
1. F. Jokar, *On \(k\)-layered numbers*, arXiv:2207.09053v1, submitted 2022-07-19.
2. P. J. Mahanta, M. P. Saikia, D. Yaqubi, *Some properties of Zumkeller numbers and \(k\)-layered numbers*, Journal of Number Theory 217 (2020), 218–236, DOI:10.1016/j.jnt.2020.05.003.
3. OEIS A204830, *Numbers whose divisors can be partitioned into three disjoint sets whose sums are all \(\sigma(n)/3\)*.
