# Nineteen connected components of the cubic alternating divisor range

## Finding

Let \(s_{-3}\) be Defant's multiplicative alternating divisor function, uniquely defined by
\[
s_{-3}(p^a)=\sum_{j=0}^{a}(-p^{-3})^j\quad(p\text{ prime},\ a\geq0).
\]
Then the closure of its range on the positive integers has **exactly nineteen connected components**, all nondegenerate closed intervals. Let
\[
C=\prod_{p\geq11}(1-p^{-3})=\frac{1}{\zeta(3)}\prod_{p\in\{2,3,5,7\}}(1-p^{-3})^{-1}.
\]
The complete, ordered and pairwise disjoint decomposition is
\[
\overline{s_{-3}(\mathbb N)}=\bigcup_{i=1}^{19}[C L_i,U_i].
\]
Each pair \((L_i,U_i)\) below is exact. In the table the displayed `C*(fraction)` is the complete lower endpoint; `members` counts merged small-prime exponent classes, not distinct interval components.

| Component | Lower endpoint | Upper endpoint | Members |
| ---: | --- | --- | ---: |
| 1 | \(C\cdot\frac{15314}{18375}\) | \(\frac{25426807}{30375000}\) | 2 |
| 2 | \(C\cdot\frac{247}{294}\) | \(\frac{4921}{5832}\) | 2 |
| 3 | \(C\cdot\frac{99541}{117600}\) | \(\frac{13357}{15552}\) | 8 |
| 4 | \(C\cdot\frac{5301}{6125}\) | \(\frac{1818375807}{2100875000}\) | 1 |
| 5 | \(C\cdot\frac{217}{250}\) | \(\frac{108507}{125000}\) | 1 |
| 6 | \(C\cdot\frac{171}{196}\) | \(\frac{117307}{134456}\) | 1 |
| 7 | \(C\cdot\frac{7}{8}\) | \(\frac{7}{8}\) | 1 |
| 8 | \(C\cdot\frac{68913}{78400}\) | \(\frac{6620706313287}{7529536000000}\) | 1 |
| 9 | \(C\cdot\frac{302157}{343000}\) | \(\frac{56439141}{64000000}\) | 2 |
| 10 | \(C\cdot\frac{1767}{2000}\) | \(\frac{883557}{1000000}\) | 1 |
| 11 | \(C\cdot\frac{11115}{12544}\) | \(\frac{427114787}{481890304}\) | 1 |
| 12 | \(C\cdot\frac{9747}{10976}\) | \(\frac{3641}{4096}\) | 2 |
| 13 | \(C\cdot\frac{57}{64}\) | \(\frac{57}{64}\) | 1 |
| 14 | \(C\cdot\frac{122512}{128625}\) | \(\frac{3632401}{3796875}\) | 2 |
| 15 | \(C\cdot\frac{988}{1029}\) | \(\frac{703}{729}\) | 2 |
| 16 | \(C\cdot\frac{42408}{42875}\) | \(\frac{1818375807}{1838265625}\) | 1 |
| 17 | \(C\cdot\frac{124}{125}\) | \(\frac{15501}{15625}\) | 1 |
| 18 | \(C\cdot\frac{342}{343}\) | \(\frac{117307}{117649}\) | 1 |
| 19 | \(C\) | \(1\) | 1 |

## Assumptions and scope

The domain is all positive integers. The closure and connected components use the ordinary topology on \(\mathbb R\); exponent \(a=0\) means the prime is absent. No truncation to bounded integers or primes is assumed. \(\zeta\) is the Riemann zeta function and \(C\) is an exact convergent Euler product, not an estimated decimal.

## Proof

**1. The large-prime tail is precisely one interval.** Set \(w_p=-\log(1-p^{-3})>0\). The decreasing summable weights, restricted to primes \(p\geq11\), satisfy
\[
w_p\leq\sum_{q>p}w_q,
\]
which is equivalent to
\[
(1-p^{-3})\geq\prod_{q>p}(1-q^{-3}).\tag{1}
\]
For \(p=11,13,17,19,23,29\), the exact rational certificate verifies
\[
(1-p^{-3})\prod_{q\leq p}(1-q^{-3})>\zeta(3)^{-1}.
\]
For the subsequent primes, put \(q\) equal to the next prime after \(p\). Nagura's theorem puts \(p<q<6p/5\) when \(p\geq29\). With \(u=p^{-3}\) and \(v=q^{-3}\), we have \(v>(125/216)u\) and \(u\leq 29^{-3}<17/108\), so
\[
2v-v^2>\frac{250}{216}u-u^2>u,
\]
and consequently \((1-v)^2<1-u\). It follows that the sequence
\[
H(p)=(1-p^{-3})\prod_{q\leq p}(1-q^{-3})
\]
strictly decreases for consecutive primes \(p\geq29\) to \(\zeta(3)^{-1}\). This proves (1) for every prime \(p\geq11\). The elementary greedy subsum lemma (a summable sequence of nonnegative weights with each term no larger than its remaining tail fills the whole interval between zero and its total in the closure of finite subsums) now shows that products \(\prod_{p\in S}(1-p^{-3})\), for finite subsets \(S\) of primes \(p\geq11\), have closure exactly \([C,1]\). Since for every exponent \(a\geq0\), \(1-p^{-3}\leq s_{-3}(p^a)\leq1\), all other large-prime products lie in the same interval. Thus the complete multiplicative large-prime tail is exactly \([C,1]\) in closure.

**2. Thirty-two small-prime classes.** For \(p=2\), partition the exponent into four classes: \(a=0\), \(a=1\), \(a=2\), and \(a\geq3\). Their respective (minimum, maximum) values are
\[
(1,1),\quad(7/8,7/8),\quad(57/64,57/64),\quad(455/512,3641/4096).
\]
Indeed, the odd partial sums increase with odd exponent and the even partial sums decrease with even exponent (from exponent \(2\) onward); the extreme values in the final class occur at exponents \(3\) and \(4\). For each \(p\in\{3,5,7\}\), use the two classes \(a=0\) and \(a\geq1\), whose extrema are respectively \((1,1)\) and
\[
(1-p^{-3},\,1-p^{-3}+p^{-6}).
\]
The product of these independent extrema gives rational endpoints \(L,U\) for each of exactly \(4\cdot2^3=32\) classes. Every class has its extreme head values attained by concrete finite exponents. Multiplying one such head value \(h\) by the full large-prime tail gives the interval \([Ch,h]\). Moreover the verifier checks strictly \(C U<L\) for every one of the 32 classes using a rigorous rational upper bound for \(C\). Thus the intervals \([Ch,h]\) for different heads in one class all share the common interval \([CU,L]\), and the closure of the entire class is exactly \([CL,U]\). This is true even though only discrete exponent values themselves are used: their intervals have a common intersection and the two extreme head values are attained.

**3. Exact comparison and merging.** The 32 exact rational \(L,U\) pairs are generated by `verify.py`, ordered by \(L\), then processed from left to right. If the next lower endpoint \(CL\) does not exceed the running upper endpoint, join the intervals; otherwise a strict gap begins. The checker avoids floating point: it certifies
\[
\frac{99819}{100000}<C<\frac{998193}{1000000}
\]
by rational lower and upper bounds on \(\zeta(3)\). At every one of the 31 adjacent merge tests it proves either overlap with the upper bound on \(C\), or a strict gap with the lower bound. There are exactly 13 overlaps and 18 strict gaps, hence 19 components with precisely the endpoints in the table. This completes the argument.

## Verification

Run `python3 verify.py` (Python 3 standard library only). The program certifies the zeta enclosure by finite integer floor sums and an explicit integral-tail bound, the six base prime-tail inequalities, all 32 head-class connectedness conditions, and all 31 exact overlap/gap decisions. Its terminal line must be:

`CERTIFICATE_OK tail_primes 6 head_classes 32 components 19 gaps 18 overlaps 13 zeta_N 20000`

The rational zeta enclosure uses \(N=20000\), \(S=10^{15}\), and
\[
\frac{1}{S}\sum_{n=1}^N\lfloor S/n^3\rfloor
\leq\zeta(3)\leq
\frac{1}{S}\sum_{n=1}^N\lfloor S/n^3\rfloor+\frac NS+\frac{1}{2N^2}.
\]
This is a finite certificate for comparisons; the infinite-prime argument is supplied by the proof above.

## Relationship to prior work

Defant introduced the family \(s_{-r}\) and proved an exact criterion for when its range is dense throughout \([\zeta(r)^{-1},1]\). His concluding open problem asks for the parameters at which the range closure has a prescribed finite number of disjoint intervals. The present theorem resolves the exact finite-component question at the natural first higher integer exponent \(r=3\). A related published computation of precisely two components at \(r=2\) does not imply the exponent-three result. Papers on the ordinary and unitary divisor functions use different local Euler factors and do not by themselves determine this alternating range.

## Limitations

The result treats exactly exponent \(r=3\), not a neighborhood of exponents or a complete parameter classification. Exact rational comparisons are independently executable, but no external independent mathematical audit is asserted. The literature search does not establish global priority over all unindexed sources.

## References

1. Colin Defant, *On Ranges of Variants of the Divisor Functions that are Dense*, arXiv:1507.01128v1 (first public 2015-07-04); *International Journal of Number Theory* 11 (2015), 1905–1912, DOI 10.1142/S1793042115500827. https://arxiv.org/abs/1507.01128
2. J. Nagura, *On the interval containing at least one prime number*, *Proceedings of the Japan Academy* 28 (1952), 177–181. The prime-interval theorem states that a prime lies strictly between \(x\) and \(6x/5\) for \(x\geq25\).
