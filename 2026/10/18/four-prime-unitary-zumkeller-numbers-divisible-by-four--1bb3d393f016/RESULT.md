# Four-prime unitary Zumkeller numbers divisible by four

## Finding

**Theorem.** Let \(n\) be a positive integer with exactly four distinct prime factors and \(4\mid n\). Its unitary divisors can be partitioned into two subsets of equal sum if and only if \(n\) belongs to the disjoint union
\[
\bigl\{60r^e : r>5\text{ prime},\ e\ge1\bigr\}
\ \cup\ \{924,1092,1428,1596,840\}.
\]
Moreover every integer in this classification has its **proper** unitary divisors partitionable into two equal-sum subsets. Equivalently, for integers in the stated domain, unitary abundance \(\sigma^*(n)\ge2n\) is both necessary and sufficient for unitary Zumkeller status. No such integer is divisible by \(16\); the only one divisible by \(8\) is \(840\).

## Assumptions and scope

A unitary divisor \(d\mid n\) satisfies \(\gcd(d,n/d)=1\). If \(n=\prod_{i=1}^s p_i^{e_i}\) is the factorization into distinct prime powers, then its unitary divisors are the \(2^s\) products of arbitrary subsets of these prime powers and
\[
\sigma^*(n)=\prod_{i=1}^s(1+p_i^{e_i}).
\]
An integer is **unitary Zumkeller** if all unitary divisors split into two disjoint equal-sum subsets; it is **unitary half-Zumkeller** if the *proper* unitary divisors (excluding \(n\)) split into two nonempty disjoint equal-sum subsets. The theorem treats exactly four distinct prime factors with at least two factors of \(2\), without an upper bound on the odd exponents. It does not classify integers of \(2\)-adic valuation one, or integers with other numbers of distinct prime factors.

## Proof

**Abundance sieve.** Because one part of an equal-sum unitary partition contains the largest unitary divisor \(n\), a necessary condition is \(\sigma^*(n)\ge2n\). Write
\[
n=2^a u v w,\qquad a\ge2,
\]
where \(u=p^b,\ v=q^c,\ w=r^d\), \(3\le p<q<r\) are odd primes and \(b,c,d\ge1\). The necessary inequality becomes
\[
2\le(1+2^{-a})(1+u^{-1})(1+v^{-1})(1+w^{-1}). \tag{1}
\]
Each factor decreases with its prime-power argument. For \(a\ge4\), the right side is at most
\[
(1+1/16)(1+1/3)(1+1/5)(1+1/7)
=\frac{68}{35}<2,
\]
so \(a\le3\).

When \(a=3\), the odd-factor product in (1) is at least \(16/9\). If \(p\ge5\), the product is at most \((6/5)(8/7)(12/11)<16/9\); if \(p=3\) but \(b\ge2\), it is at most \((10/9)(6/5)(8/7)<16/9\). Hence \(u=3\). If \(q\ge7\), the remaining bound is \((4/3)(8/7)(12/11)<16/9\), so \(q=5\); if \(q=5\) but \(c\ge2\), \((4/3)(26/25)(8/7)<16/9\), thus \(v=5\). Therefore
\[
(1+1/w)\ge\frac{16/9}{(4/3)(6/5)}=\frac{10}{9},
\]
so \(w\le9\). As \(w\) is a power of a prime strictly greater than five, \(w=7\). Hence \(n=840\).

When \(a=2\), the odd-factor product in (1) is at least \(8/5\). If \(p\ge5\) the product is at most \((6/5)(8/7)(12/11)<8/5\); if \(p=3\) and \(b\ge2\), it is at most \((10/9)(6/5)(8/7)<8/5\). Thus \(u=3\), leaving
\[
(1+1/v)(1+1/w)\ge\frac65. \tag{2}
\]
If \(q\ge11\), the left side is at most \((12/11)(14/13)<6/5\), so \(q\in\{5,7\}\). If \(q=5\) and \(c\ge2\), the bound \((26/25)(8/7)<6/5\) contradicts (2). Thus \(v=5\), and every admissible \(w=r^d\) with \(r>5\) is allowed by (2). This gives \(n=60r^d\). If \(q=7\) and \(c\ge2\), then \((50/49)(12/11)<6/5\), again impossible. Thus \(v=7\), and (2) becomes \(1+1/w\ge21/20\), or \(w\le20\). Since \(w=r^d\) for prime \(r>7\), this gives \(w\in\{11,13,17,19\}\), hence \(n\in\{924,1092,1428,1596\}\). This exhausts all candidates satisfying (1).

**Constructing equal-sum unitary partitions.** For \(n=60R\), where \(R=r^e\) and prime \(r>5\), multiplicativity yields \(\sigma^*(n)=120(1+R)\). The distinct unitary divisors \(n\) and \(60\) therefore have sum \(60R+60=\sigma^*(n)/2\). For \(n=84r\) with \(r\in\{11,13,17,19\}\), \(\sigma^*(n)=160(1+r)\), and the difference \(\sigma^*(n)/2-n=80-4r\) has the following explicit representations by distinct proper unitary divisors:
\[
\begin{array}{c|c|c}
r&80-4r&\text{unitary-divisor subset}\\\hline
11&36&1+7+28\\
13&28&28\\
17&12&12\\
19&4&4
\end{array}
\]
Finally, \(\sigma^*(840)=1728\) and \(840+24=864=\sigma^*(840)/2\), with \(24\) unitary in \(840\). In every case the displayed subset, together with \(n\), forms one half; the complement forms the other. All and only candidates are therefore unitary Zumkeller.

**Proper-divisor partitions.** For \(60R\), the four proper unitary divisors \(3R,12R,15R,60\) have sum \(30R+60=(\sigma^*(60R)-60R)/2\). For \(84r\), proper-unitary half-sum certificates are
\[
\begin{array}{c|c|l}
r&\frac{\sigma^*(84r)-84r}{2}&\text{proper unitary divisors}\\\hline
11&498&1,28,77,84,308\\
13&574&3,12,39,156,364\\
17&726&1,17,28,204,476\\
19&802&4,57,76,133,532
\end{array}
\]
For \(840\), the proper unitary divisors \(280,105,56,3\) sum to \(444=(1728-840)/2\). All complementary proper unitary divisors supply the second half. This proves the half-Zumkeller assertion. \(\square\)

## Verification

The standalone Python file `verify.py` independently enumerates all integers \(n\le100000\) with exactly four distinct prime factors and \(4\mid n\), builds their sixteen unitary divisors from the factorization, and tests both equal-sum partition conditions by exact integer subset-sum bitsets. The recorded result is **5,851** tested integers, **274** satisfying the unitary Zumkeller criterion, and **274** satisfying the proper-divisor criterion. Every match agrees with the infinite classification. The program also checks all five exceptional correction and proper-divisor certificates and sample members of the infinite family. Run `python3 verify.py` from the folder containing this file. These finite checks are supplementary; the inequalities and explicit partitions above prove all unbounded cases.

## Relationship to prior work

Bhabesh Das (2024) introduced general unitary-partition criteria, multiplicative construction rules, partial restrictions on prime factors, and the conjecture that every even unitary Zumkeller integer is unitary half-Zumkeller. The present theorem isolates the natural next four-prime-support stratum at \(4\mid n\), where the necessary abundance inequality becomes sufficient and the conjecture can be proved using explicit partitions. The unitary three-prime case has been studied separately; its classification does not imply the extra four-prime exceptional list or exclude every other four-prime configuration. The OEIS listings A290466 and A290467 tabulate individual unitary Zumkeller and unitary half-Zumkeller integers but do not establish the unbounded four-support classification. Classical Zumkeller numbers as treated by Mahanta, Saikia and Yaqubi (2020) use all divisors rather than unitary divisors.

## Limitations

The result applies only to integers having **exactly four distinct prime factors and divisible by four**. It does not settle Das's conjecture for other prime-support sizes or for \(2\)-adic valuation one. No claim of optimality for any broader class is made. The finite program does not replace the infinite proof. Bibliographic comparisons do not rule out equivalent unindexed literature, and no independent validation has been performed.

## References

1. B. Das, “On unitary Zumkeller numbers,” *Notes on Number Theory and Discrete Mathematics* **30** (2024), 436–442, DOI: 10.7546/nntdm.2024.30.2.436-442, online first 16 July 2024. Full text: https://nntdm.net/papers/nntdm-30/NNTDM-30-2-436-442.pdf.
2. P. Mahanta, M. Saikia and D. Yaqubi, “Some properties of Zumkeller numbers and \(k\)-layered numbers,” *Journal of Number Theory* **217** (2020), 218–236, DOI: 10.1016/j.jnt.2020.05.003. Repository: https://orca.cardiff.ac.uk/id/eprint/134550/.
3. *On-Line Encyclopedia of Integer Sequences*, A290466 (unitary Zumkeller integers): https://oeis.org/A290466; A290467 (unitary half-Zumkeller integers): https://oeis.org/A290467.
