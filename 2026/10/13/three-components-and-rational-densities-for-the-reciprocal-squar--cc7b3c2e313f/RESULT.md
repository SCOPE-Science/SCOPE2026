# Three components and rational densities for the reciprocal-square divisor sum on cube-free integers

## Finding

Let \(\mathcal C=\{n\ge1:p^3\nmid n\text{ for every prime }p\}\), the set of cube-free positive integers, and let
\[
\sigma_{-2}(n)=\sum_{d\mid n}\frac{1}{d^2}.
\]
Then the closure in \(\mathbb R\) of the restricted range has **exactly three** connected components:
\[
\boxed{\overline{\sigma_{-2}(\mathcal C)}
=\left[1,\frac{9720}{91\pi^4}\right]
\cup\left[\frac{10}{9},\frac{120}{\pi^4}\right]
\cup\left[\frac54,\frac{315}{2\pi^4}\right].}
\]
These intervals are pairwise disjoint. Moreover, if \(I_1,I_2,I_3\) are the displayed intervals in order, then the conditional natural densities among cube-free positive integers are, respectively,
\[
\boxed{\lim_{X\to\infty}\frac{\#\{n\le X:n\in\mathcal C,\ \sigma_{-2}(n)\in I_j\}}{\#\{n\le X:n\in\mathcal C\}} =\left(\frac{36}{91},\frac{16}{91},\frac{39}{91}\right)_j.}
\]
Thus the corresponding absolute natural densities are \(36/(91\zeta(3))\), \(16/(91\zeta(3))\), and \(39/(91\zeta(3))\).

## Assumptions and scope

No bound on the size or number of prime factors is imposed. Every prime exponent is restricted to \(0,1,2\). The closure, rather than the discrete set of actual values, is classified. The prime-distribution input is the classical Nagura bound: for every integer \(x\ge25\), a prime lies strictly between \(x\) and \(6x/5\) [3]. Euler's product and the standard evaluations \(\zeta(2)=\pi^2/6\), \(\zeta(6)=\pi^6/945\) are used. For strict rational comparisons we use Archimedes' bounds \(223/71<\pi<22/7\).

## Proof

**1. Prime-local options and the full maximum.** For every prime \(p\), define
\[
A_p=1+p^{-2},\quad B_p=1+p^{-2}+p^{-4},\quad D_p=\{1,A_p,B_p\}.
\]
Multiplicativity and unique factorization show that the restricted range consists of finite products choosing one factor from \(D_p\) for each prime. As \(\sum_p \log B_p\) converges, its closure is precisely the set of convergent infinite products with the same three options. The maximum over all choices equals
\[
W=\prod_p B_p
=\prod_p\frac{1-p^{-6}}{1-p^{-2}}
=\frac{\zeta(2)}{\zeta(6)}=\frac{315}{2\pi^4}.
\tag{1}
\]

**2. The entire prime tail from \(5\) upward fills one interval.** Write the increasing primes at least \(5\) as \(q_1,q_2,\ldots\) and set \(a_i=\log A_{q_i}\), \(b_i=\log B_{q_i}\). Their three possible logarithmic increments are \(0,a_i,b_i\). Because \(B_p<A_p^2\), the larger of the two successive gaps between these increments is \(a_i\). We prove, for every prime \(p\ge5\),
\[
\log(1+p^{-2})\le\sum_{q>p\atop q\text{ prime}}\log(1+q^{-2}+q^{-4}).
\tag{2}
\]
For \(p=5,7,11,13,17,19,23\), a finite product already exceeds \(1+p^{-2}\). Exact witnessing lists of later primes, respectively, are
\[
(7,11,13,17,19),\ (11,13,17,19),\ (13,17),\ (17,19),\ (19,23),\ (23,29),\ (29,31).
\]
Every one of the seven strict rational product inequalities is reproduced by `verify.py`.

For \(p\ge29\), let \(p_1,p_2,\ldots\) be the successive primes after \(p\). Nagura's bound, applied at each prime, gives \(p_j<(6/5)^j p\). The elementary function \(\log(1+x+x^2)-x\) has derivative \(x(1-x)/(1+x+x^2)\ge0\) for \(0\le x\le1\), hence \(\log(1+x+x^2)\ge x\) on that interval. Therefore
\[
\sum_{q>p\atop q\text{ prime}}\log B_q
\ge\sum_{j\ge1}p_j^{-2}
>p^{-2}\sum_{j\ge1}(5/6)^{2j}
=\frac{25}{11p^2}>\log(1+p^{-2}),
\]
proving (2) uniformly.

To see that (2) implies an interval, put \(s_i=\sum_{j>i}b_j\). The three translated intervals \([0,s_i]\), \([a_i,a_i+s_i]\), \([b_i,b_i+s_i]\) cover \([0,b_i+s_i]\), because \(s_i\ge a_i\ge b_i-a_i\). Starting from any target in \([0,\sum_i b_i]\), choose one of these three increments recursively, leaving a remainder in the corresponding subsequent-tail interval. Those remainder lengths tend to zero; hence the target is an infinite sum of permitted increments. Exponentiating shows that the closure of products using primes \(p\ge5\) is exactly
\[
[1,T],\qquad T=\prod_{p\ge5}B_p
=\frac{W}{(21/16)(91/81)}
=\frac{9720}{91\pi^4}.
\tag{3}
\]
The converse inclusion is immediate from positivity and the Euler product.

**3. Exactly nine candidate intervals, merging into three.** The local factors for \(p=2\) are \(1,5/4,21/16\), and for \(p=3\) they are \(1,10/9,91/81\). The closure is therefore the union of nine intervals \([c,cT]\), whose left endpoints in increasing order are
\[
1,\quad\frac{10}{9},\quad\frac{91}{81},\quad\frac54,\quad
\frac{21}{16},\quad\frac{25}{18},\quad\frac{455}{324},\quad
\frac{35}{24},\quad\frac{1911}{1296}.
\tag{4}
\]
The exact rational comparisons \(223/71<\pi<22/7\) imply
\[
\frac{200}{189}<T<\frac{10}{9},
\qquad \frac{120}{\pi^4}<\frac54.
\tag{5}
\]
The second and third candidate intervals overlap: the ratio of their left endpoints is \(91/90<200/189\). The six candidate intervals beginning at \(5/4\) overlap successively: their five successive left-endpoint ratios are \(21/20\), \(200/189\), \(91/90\), \(27/26\), and \(91/90\), all at most \(200/189<T\). By (5), the first interval is strictly separated from the second, and the merged second block is strictly separated from the third block. The right endpoint of the second block is \((91/81)T=120/\pi^4\); the right endpoint of the last block is \((1911/1296)T=W\). This proves the asserted three exact intervals and strict gaps.

**4. Conditional natural densities.** For a fixed prime \(p\), among cube-free integers the probability of exponent \(a\in\{0,1,2\}\), interpreted as a natural density, is
\[
\frac{(1-p^{-1})p^{-a}}{1-p^{-3}}
=\frac{p^{-a}}{1+p^{-1}+p^{-2}}.
\]
For distinct fixed primes these exponent distributions are independent in the density limit; one may justify this using the Chinese remainder theorem and the absolutely convergent Euler product for the cube-free indicator \(\sum_{d^3\mid n}\mu(d)\). Accordingly the conditional exponent weights are \((4/7,2/7,1/7)\) at \(2\) and \((9/13,3/13,1/13)\) at \(3\). By the disjoint interval classification, membership of the first component is equivalent to \(v_2(n)=v_3(n)=0\); membership of the second is equivalent to \(v_2(n)=0\) and \(v_3(n)\in\{1,2\}\); membership of the third is equivalent to \(v_2(n)\in\{1,2\}\). Multiplication of the local weights gives
\[
\frac47\frac9{13}=\frac{36}{91},\qquad
\frac47\frac4{13}=\frac{16}{91},\qquad
\frac37=\frac{39}{91}.
\]
Finally, cube-free integers have density \(\zeta(3)^{-1}\); multiplying yields the absolute densities.

## Verification

Run `python3 verify.py` using Python's standard library. It checks all seven small-prime inequalities as exact rational inequalities; computes and orders all nine prime-local rational multipliers; checks both gaps and all prescribed overlaps using only rational bounds for \(\pi\); and verifies the three density fractions. It also performs a separate finite illustration through \(100000\) integers (not used to establish the infinite theorem). Expected output starts with `EXACT_CERTIFICATE_OK` and states `components=3` and `conditional_weights=36/91,16/91,39/91`.

## Relationship to prior work

Defant introduced the restricted-domain functions \(\sigma_{t,k}\) and their connectedness thresholds, and asked for exact component counts for various integer exponent cutoffs \(k\) and real parameters [1]. Here \(k=2\), \(t=-2\). Sanna classified the **unrestricted** reciprocal-square divisor-sum closure as three different intervals and calculated their densities [2]. Its unrestricted domain has infinitely many possible exponents at each prime; the three-component classification there cannot establish that restricting every exponent to at most two still fills each interval. The present exact endpoints and conditional cube-free densities differ from Sanna's unrestricted values. The argument above proves the restricted tail-filling assertion independently. Later studies of unrestricted divisor-function ranges likewise do not determine the cube-free restriction [4,5].

## Limitations

The result applies to exponent cutoff two and reciprocal-square weight only, and classifies a closure rather than identifying which individual points of each interval occur at finite integers. It does not determine a function of the cutoff \(k\) or exponent \(r\), nor does it claim that no earlier unindexed derivation exists. The infinite tail proof depends on the published Nagura prime-interval theorem; finite tests alone do not establish that step. The provided code is a reproducibility check, not a separate formal proof.

## References

[1] Colin Defant, *On the Density of Ranges of Generalized Divisor Functions with Restricted Domains*, arXiv:1507.02663 (first publicly available 2015-07-09), especially Section 2 and final open problem. https://arxiv.org/abs/1507.02663

[2] Carlo Sanna, *On the closure of the image of the generalized divisor function*, arXiv:1507.08091 (2015-07-29), Sections 1 and 5. https://arxiv.org/abs/1507.08091

[3] Jitsuro Nagura, *On the Interval Containing At Least One Prime Number*, Proc. Japan Acad. 28 (1952), 177–181, DOI:10.3792/pja/1195570997.

[4] Nina Zubrilina, *On the Number of Connected Components of Ranges of Divisor Functions*, arXiv:1711.02871 (2017). https://arxiv.org/abs/1711.02871

[5] Niven Achenjang and Aaron Berger, *On Gaps in the Closures of Images of Divisor Functions*, arXiv:1808.07550 (2018). https://arxiv.org/abs/1808.07550
