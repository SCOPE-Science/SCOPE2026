# Prime-power odd parts in initial-divisor sums

Let the positive divisors of an integer \(n>1\) be
\[
1=d_1<d_2<\cdots<d_{\tau(n)}=n.
\]
Call \(n\) an **initial-divisor-sum number** if
\[
d_1+\cdots+d_k=n
\]
for some \(k<\tau(n)\). This is the property defining OEIS A064510. An **Erdős–Nicolas number** is a nonperfect instance for which one may take \(k<\tau(n)-1\); these form OEIS A194472.

We study the two-prime-support family
\[
n=2^a p^b,\qquad a,b\ge1,
\]
with \(p\) an odd prime.

## Main results

### Theorem 1: complete classification when the odd part is prime

For \(a\ge1\) and odd prime \(p\), the number \(2^a p\) is an initial-divisor-sum number if and only if exactly one of the following holds:

1. \((a,p)=(3,3)\), giving \(n=24\); or
2. \(p=2^{a+1}-1\), in which case \(p\) is a Mersenne prime and \(2^a p\) is an even perfect number.

In the second case the equality uses all proper divisors. Hence
\[
\boxed{24\text{ is the unique Erdős–Nicolas number of the form }2^a p.}
\]

### Theorem 2: no prime-square odd part

For every \(a\ge1\) and every odd prime \(p\),
\[
\boxed{2^a p^2\notin\mathrm{A064510}.}
\]
In particular, no Erdős–Nicolas number has the form \(2^a p^2\).

### Theorem 3: a large-prime obstruction for all exponents

For arbitrary \(b\ge1\), if \(p>2^a\), then
\[
2^a p^b\in\mathrm{A064510}
\quad\Longleftrightarrow\quad
b=1\text{ and }p=2^{a+1}-1.
\]
Thus the only initial-divisor-sum numbers in the region \(p>2^a\) are the classical even perfect numbers.

### Theorem 4: finite reduction for every higher odd-prime exponent

Suppose \(b\ge3\) and \(2^a p^b\in\mathrm{A064510}\). Put
\[
M=2^{a+1}-1,\qquad v=v_p(M).
\]
Then necessarily
\[
\boxed{
 a\ge4,\qquad p\mid M,\qquad p\le2^a,\qquad
 b\text{ is odd},\qquad 3\le b\le a+v-1.
}
\]
Consequently, for each fixed \(a\), all possible higher-exponent cases reduce to a finite list obtained from the prime divisors of \(2^{a+1}-1\).

Together, Theorems 1--4 leave only the narrow finite-per-\(a\) regime in Theorem 4 as a possible source of further two-prime-support Erdős–Nicolas numbers.

## Proof of Theorem 1

Assume a prefix ending at a cutoff \(x\) sums to \(n=2^a p\). The prefix must contain a multiple of \(p\), since a sum using only powers of two is odd. Let
\[
r=\max\{i:2^i\le x\},\qquad
s=\max\{i:p2^i\le x\}.
\]
Because \(p\ge3\), and because the largest divisor \(n\) itself cannot occur in a prefix summing to \(n\), one has \(s<r\). The prefix sum is therefore
\[
(2^{r+1}-1)+p(2^{s+1}-1)=2^a p,
\]
so
\[
p=\frac{2^{r+1}-1}{2^a-2^{s+1}+1}. \tag{1}
\]
Write \(D=2^a-2^{s+1}+1\).

If \(r\le a-2\), then \(s\le r-1\), and the numerator of (1) cannot exceed \(D\): indeed
\[
2^{r+1}+2^{s+1}\le 2^{r+1}+2^r\le3\cdot2^{a-2}<2^a+2.
\]
Thus \(p>1\) is impossible.

If \(r=a-1\), the numerator is \(N=2^a-1\). Since \(D\mid N\), also \(D\mid N-D=2^{s+1}-2\). For \(s=0\) this gives \(N=D\), hence \(p=1\). For \(s\ge1\), using \(s\le a-2\),
\[
0<N-D\le2^{a-1}-2<D,
\]
again impossible.

Hence \(r=a\). Now \(N=2^{a+1}-1\). If \(s=a-1\), then \(D=1\), so
\[
p=2^{a+1}-1,
\]
and the prefix consists of all proper divisors of the corresponding even perfect number.

It remains to take \(s\le a-2\). Since \(D\mid N\),
\[
D\mid N-2D=2^{s+2}-3.
\]
Moreover
\[
0<2^{s+2}-3<2D,
\]
so necessarily \(2^{s+2}-3=D\). Therefore
\[
3\cdot2^{s+1}=2^a+4. \tag{2}
\]
If \(s=0\), (2) gives \(a=1\), incompatible with \(s\le a-2\). If \(s=1\), it gives \(a=3\), and then (1) yields \(p=3\). If \(s\ge2\), the left side of (2) is divisible by \(8\), whereas the right side is \(4\pmod8\), because \(a\ge s+2\ge4\). Thus the only exceptional solution is
\[
24=2^3\cdot3,
\]
with
\[
1+2+3+4+6+8=24.
\]
This proves Theorem 1.

## Proof of Theorem 2

Let \(x\) be a prefix cutoff for \(n=2^a p^2\), and let \(s\in\{0,1,2\}\) be the largest exponent of \(p\) occurring among included divisors. Each nonempty \(p\)-adic layer contributes
\[
p^j(1+2+\cdots+2^{r_j})=p^j(2^{r_j+1}-1),
\]
an odd integer. Since \(n\) is even, the number of nonempty layers, \(s+1\), must be even. Hence \(s=1\), so \(x<p^2\).

Each of the two included layers has sum strictly less than \(2x\). Therefore
\[
2^a p^2=n<4x<4p^2,
\]
which forces \(a=1\). But then every divisor below \(p^2\) is among
\[
1,2,p,2p,
\]
whose total is \(3(p+1)<2p^2\) for every odd prime \(p\). This contradiction proves Theorem 2.

## Proof of Theorem 3

Assume \(p>2^a\). Then for every \(j\ge0\),
\[
2^a p^j<p^{j+1},
\]
so the divisors occur in complete \(p\)-adic blocks
\[
\{p^j,2p^j,\ldots,2^a p^j\}
\]
before the next block begins.

Any prefix summing to \(n\) must enter the \(j=1\) block, so the entire \(j=0\) block is present. Reducing the prefix sum modulo \(p\) gives
\[
p\mid 2^{a+1}-1=M.
\]
Since \(p>2^a\) and \(M<2p\), this forces \(p=M\).

Let \(t\) be the largest \(p\)-adic block touched by the prefix. If \(t<b\), even the sum of all blocks through \(t\) is
\[
p(1+p+\cdots+p^t)
<\frac{p}{p-1}p^{t+1}
<\frac{p+1}{2}p^{t+1}
=2^a p^{t+1}
\le n,
\]
where \(2p<(p-1)(p+1)=p^2-1\) for \(p\ge3\). Hence \(t=b\).

The top block is only partial, because its last divisor is \(n\). If its partial binary coefficient is \(C=2^{r+1}-1\) with \(r\le a-1\), the prefix equation is
\[
p(1+p+\cdots+p^{b-1})+Cp^b=2^a p^b. \tag{3}
\]
For \(b\ge2\), the first term on the left of (3) has exact \(p\)-adic valuation \(1\), while the other two terms are divisible by \(p^b\), a contradiction. Thus \(b=1\). Equation (3) then gives \(C=2^a-1\), so the prefix is exactly the set of all proper divisors. This proves Theorem 3.

## Proof of Theorem 4

Let \(x\) be the cutoff and, for \(0\le j\le s\), let \(r_j\) be the largest exponent such that \(2^{r_j}p^j\le x\). Thus \(s\) is the largest \(p\)-adic layer touched by the prefix and
\[
2^a p^b=
\sum_{j=0}^{s}p^j(2^{r_j+1}-1). \tag{4}
\]

We first show that \(r_0=a\). Suppose instead that \(r_0<a\). Then \(x<2^{r_0+1}\le2^a\), and every nonempty layer in (4) has sum less than \(2x\).

If \(s=b\), then
\[
2^a p^b<2(b+1)2^a,
\]
so \(p^b<2(b+1)\), impossible for \(p\ge3\) and \(b\ge3\).

If \(s<b\), then also \(x<p^{s+1}\), giving
\[
2^a p^{b-s-1}<2(s+1).
\]
But \(p^s\le x<2^a\), hence
\[
p^{b-1}<2(s+1)\le2b,
\]
again impossible for \(b\ge3\). Thus \(r_0=a\).

Reducing (4) modulo \(p\) now gives
\[
p\mid M=2^{a+1}-1.
\]
Theorem 3 excludes \(p>2^a\), so \(p\le2^a\).

Let \(v=v_p(M)\), and let \(h\) be the last index for which \(r_h=a\), i.e. the last completely included binary block. We claim \(h\le v-1\). If \(h=s\), then the whole prefix has \(p\)-adic valuation exactly \(v\), so \(b=v\); combined with \(h=s\le b\) and \(h\ge v\), this forces \(h=s=b\), which would include the divisor \(n\) itself. If \(h<s\), the complete-block contribution
\[
M(1+p+\cdots+p^h)
\]
has valuation \(v\), while every later term is divisible by \(p^{h+1}\). If \(h\ge v\), the full prefix again has valuation \(v\), so \(b=v\le h<s\le b\), impossible. Hence \(h\le v-1\).

Once a layer is not complete, the binary exponents strictly decrease: if \(r_j<a\), then
\[
r_{j+1}\le r_j-1,
\]
for otherwise \(p^{j+1}2^{r_j}\le x<p^j2^{r_j+1}\) would imply \(p<2\). Therefore
\[
s-h\le a,
\qquad s+1\le a+v. \tag{5}
\]

For \(a\ge4\), suppose \(s<b\). As above,
\[
2^a p^{b-s-1}<2(s+1)\le2(a+v).
\]
Since \(p^v\le M<2^{a+1}\) and \(p\ge3\), one has \(v\le a\). Thus
\[
2^a p^{b-s-1}<4a\le2^a,
\]
a contradiction. Hence \(s=b\). Equation (4) is a sum of \(b+1\) odd layer-sums and is even, so \(b\) is odd. Finally, (5) and \(h\le v-1\) give
\[
b=s\le h+a\le a+v-1.
\]

It remains only to exclude \(a\le3\) for \(b\ge3\). For \(a=1,2\), the divisibility \(p\mid2^{a+1}-1\) gives respectively \(p=3\) or \(p=7\), both lying in the region \(p>2^a\) already excluded by Theorem 3 for \(b\ge2\).

For \(a=3\), one has \(p\mid15\), so \(p=3\) or \(5\), and \(x\ge8\). If \(p=3\), divide (4) by \(3\) and reduce modulo \(3\): the first partial layer must satisfy
\[
2^{r_1+1}-1\equiv1\pmod3.
\]
Thus \(r_1+1\) is odd. The cutoff \(x\ge8\) rules out \(r_1=0\), so \(r_1=2\), whence \(12\le x<24\). This includes the \(p^2=9\) layer but excludes \(p^3=27\), so exactly three layers are nonempty; their odd sums cannot total the even number \(n\).

If \(p=5\), reducing the divided equation modulo \(5\) gives
\[
2^{r_1+1}-1\equiv2\pmod5,
\]
so \(r_1=2\). Then \(20\le x<40\), which includes \(25\) but excludes \(125\), again leaving exactly three odd layers and the same parity contradiction. Therefore \(a\ge4\), completing the proof.

## Exact finite verification

The accompanying standalone Python program performs two exact checks using integer arithmetic only.

First, it directly enumerates sorted divisor prefixes for all
\[
1\le a\le20,\quad b\in\{1,2\},\quad p\le100000,
\]
with \(p\) odd prime: 383,640 parameter triples. It finds six A064510 hits (five even perfect numbers in the tested prime range plus \(24\)), one genuine Erdős–Nicolas hit, and zero mismatches with Theorems 1 and 2.

Second, Theorem 4 reduces all \(b\ge3\) cases with \(4\le a\le30\) to 661 exact candidates. Exhausting those candidates gives zero hits. Consequently, for \(1\le a\le30\), every initial-divisor-sum number of the form \(2^a p^b\) is either \(24\) or one of the even perfect numbers arising from a Mersenne prime \(2^{a+1}-1\). This bounded corollary is computational; the structural theorems above are proved without a cutoff.

## Context and originality

Erdős and Nicolas introduced the equality underlying these numbers in their 1975 paper *Répartition des nombres superabondants*. In the final section they list the nonperfect examples below \(10^6\), beginning with \(24,2016,8190\). The present theorem addresses a different question: an exact structural classification and effective reduction inside the two-prime-support family \(2^a p^b\).

The current OEIS entries A064510 and A194472 record examples, programs, and general comments; A194472 still asks, for example, whether every Erdős–Nicolas number is even. Jean-Marie De Koninck's 2009 book *Those Fascinating Numbers* also records the Erdős–Nicolas sequence. Targeted searches for the exact form \(2^a p^b\), prime or prime-square odd part, Mersenne specializations, initial-divisor sums, and synonymous partial-divisor-sum formulations did not locate Theorems 1--4 or a stronger theorem implying them.

Accordingly, originality is asserted only **to the best of our knowledge**. The principal residual risk is older or poorly indexed problem literature about divisor partial sums. No concrete prior statement matching the classification or finite-reduction theorem was found.

## Limitations

The result does **not** complete the classification of \(2^a p^b\) for \(b\ge3\). It proves that every such unresolved case must lie in the finite-per-\(a\) set of Theorem 4. The exact computation through \(a=30\) is a bounded corollary, not evidence that the remaining family is empty in general.

## References

1. P. Erdős and J.-L. Nicolas, *Répartition des nombres superabondants*, Bulletin de la Société Mathématique de France **103** (1975), 65--90. DOI: https://doi.org/10.24033/bsmf.1793 ; author-hosted scan: https://www.renyi.hu/~p_erdos/1975-37.pdf
2. J.-M. De Koninck, *Those Fascinating Numbers*, AMS, 2009. https://www.ams.org/bookpages/mbk-64
3. OEIS A064510, *Numbers m such that the sum of the first k divisors of m is equal to m for some k*. https://oeis.org/A064510
4. OEIS A194472, *Erdős-Nicolas numbers*. https://oeis.org/A194472
