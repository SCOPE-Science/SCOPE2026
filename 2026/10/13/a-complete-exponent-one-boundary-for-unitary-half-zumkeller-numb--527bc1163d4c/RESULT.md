# A complete exponent-one boundary for unitary half-Zumkeller numbers on \(\{2,3,q\}\)

## Finding
A positive integer \(n\) is *unitary half-Zumkeller* if its proper unitary positive divisors admit a bipartition into equal-sum nonempty sets. Here \(d\) is a unitary divisor of \(n\) when \(d\mid n\) and \(\gcd(d,n/d)=1\).

**Theorem.** For every prime \(q>3\) and positive integers \(a,b,c\) with \(\min(a,b)=1\), put \(n=2^a3^bq^c\). Then \(n\) is unitary half-Zumkeller **if and only if**
\[
 n=6q^c\quad\text{or}\quad n\in\{60,84,90,120,168,240\}.
\]
Among the satisfying integers in this domain, the unitary half-Zumkeller numbers **which are not unitary Zumkeller** are exactly
\[
 \{84,120,168,240\}.
\]
In particular, the infinite branch permits every prime \(q>3\) and every exponent \(c\ge1\), while each of the six sporadic integers has exponent \(c=1\).

## Assumptions and scope
The prime factors \(2,3,q\) are distinct. The exponents \(a,b,c\) are positive and at least one of \(a,b\) equals \(1\); the theorem makes no assertion about \(a,b\ge2\). A *unitary Zumkeller* number admits an equal-sum partition of **all** its unitary divisors, including itself; this is a different property. For three prime-power blocks, the proper unitary divisors are exactly the seven numbers listed below.

## Proof
Write \(A=2^a\), \(B=3^b\), and \(C=q^c\), so \(C\ge5\). The proper unitary divisors of \(n=ABC\) are
\[
 \{1,A,B,AB,C,AC,BC\}.
\]
A bipartition of these seven numbers into equal sums exists precisely when there are signs \(\epsilon_0,\ldots,\epsilon_3,\delta_0,\ldots,\delta_2\in\{-1,1\}\) such that
\[
 N+CD=0,\quad N=\epsilon_0+\epsilon_1A+\epsilon_2B+\epsilon_3AB,\quad D=\delta_0+\delta_1A+\delta_2B. \tag{1}
\]
This reformulation is exact: the positive and negative signs are the two parts, and any zero signed sum of positive summands has nonempty parts.

First suppose \(a=1\), so \(A=2\). If \(b\ge2\), then \(B\ge9\), every possible \(D\) is nonzero, and
\[
 |D|\ge B-3,\qquad |N|\le3(B+1).
\]
Equation (1) and \(C\ge5\) force \(5(B-3)\le3(B+1)\), hence \(B\le9\). Therefore \(B=9\), and the same bound gives \(5\le C\le5\). Since \(C=q^c\), this is precisely \(n=2\cdot9\cdot5=90\). If \(a=b=1\), no bound is needed: for arbitrary \(C=q^c\), the partition
\[
 \{1,2,3,C,2C\}\quad\text{and}\quad\{6,3C\}
\]
has the common sum \(6+3C\), proving that every \(6q^c\) qualifies.

Now suppose \(b=1\) and \(a\ge2\), so \(B=3\). When \(a\ge3\), we have \(A\ge8\), and every possible \(D\) satisfies
\[
 |D|\ge A-4,\qquad |N|\le4(A+1).
\]
Thus \(5(A-4)\le4(A+1)\), giving \(A\le24\), hence \(a\in\{3,4\}\). At \(a=3\), the sharper bound \(C\le4(9)/4=9\) leaves \(C\in\{5,7\}\), since \(C\) is a power of a prime \(q>3\). At \(a=4\), the bound is \(C\le4(17)/12<6\), leaving only \(C=5\).

For \(a=2\), where \(A=4\), the possible \(D\) are \(0,\pm2,\pm6,\pm8\). In the case \(D=0\), we cannot have \(N=0\): writing \(N=\pm12+(\pm1\pm4\pm3)\), the latter parenthesis has absolute value at most \(8\). Thus \(D\ne0\) in every solution, and (1) gives \(C\le(1+4+3+12)/2=10\). The only prime powers \(q^c\le10\) with \(q>3\) are \(5\) and \(7\). This exhausts all possible cases.

To establish sufficiency for the six isolated possibilities, the table lists a subset of the proper unitary divisors summing to **half** their total. Its complement supplies the other half; all listed subsets are nonempty and proper.

| \(n\) | Subset of proper unitary divisors | Half of their sum |
| ---: | :--- | ---: |
| \(60\) | \(\{1,4,5,20\}\) | \(30\) |
| \(84\) | \(\{3,7,28\}\) | \(38\) |
| \(90\) | \(\{45\}\) | \(45\) |
| \(120\) | \(\{8,40\}\) | \(48\) |
| \(168\) | \(\{1,3,56\}\) | \(60\) |
| \(240\) | \(\{1,3,80\}\) | \(84\) |

Finally, \(6C\) is unitary Zumkeller: in the full eight-divisor set the parts \(\{1,2,3,6C\}\) and \(\{6,C,2C,3C\}\) both sum to \(6+6C\). Both \(60\) and \(90\) are unitary perfect, because \(\sigma^*(60)=120\) and \(\sigma^*(90)=180\); their unitary proper divisors sum to the integer itself. For \(84,120,168,240\) the respective unitary divisor sums are \(160,216,288,408\), each less than twice its argument. No such integer can be unitary Zumkeller, since its largest unitary divisor would exceed half the total sum. This proves the final classification. \(\square\)

## Verification
Run `python3 verify.py` with Python \(3\) and its standard library, from the directory containing this file. The program independently enumerates proper unitary divisors and all subset partitions for \(2277\) parameter tuples, cross-checks the seven-sign characterization, enumerates coefficient quotients in the boundary cases, checks all six exceptional witnesses, and tests the four unitary-Zumkeller exclusions. The captured output is in `verification_output.txt`. Finite tests are not being used to infer the theorem for unlimited exponents or primes; the inequalities and signed-sum argument above establish those quantifiers.

## Relationship to prior work
Das (2024), Sections 2–3, develops unitary Zumkeller and unitary half-Zumkeller numbers, proves general criteria and gives examples including \(84\) and \(120\), but does not provide the present complete exponent-one three-prime classification. OEIS A290467 lists all six exceptional integers and initial members of \(6q^c\), but its finite table does not exclude additional solutions with arbitrarily large parameters. A published classification of even **unitary Zumkeller** numbers with exactly three distinct prime factors gives \(6q^c\) and \(60,70,90\); that stronger *full-divisor* property does not cover the four half-only integers \(84,120,168,240\), nor rule out other proper-divisor partitions. Here the missing exclusion and the precise half-only boundary are proved directly.

## Limitations
No assertion is made for \(n=2^a3^bq^c\) when \(a,b\ge2\), for other choices of three prime factors, or for four or more distinct prime factors. The computational verification is bounded and is supplementary to the symbolic proof. No claim of priority over inaccessible or unindexed equivalent literature is made.

## References
1. B. Das, *On unitary Zumkeller numbers*, Notes on Number Theory and Discrete Mathematics **30** (2024), 436–442, DOI: 10.7546/nntdm.2024.30.2.436-442; open full text: https://nntdm.net/papers/nntdm-30/NNTDM-30-2-436-442.pdf (online first 16 July 2024).
2. OEIS A290467, *Unitary half-Zumkeller numbers*: https://oeis.org/A290467; finite table: https://oeis.org/A290467/b290467.txt.
3. OEIS A290466, *Unitary Zumkeller numbers*: https://oeis.org/A290466.
4. *Three-prime-support classification of even unitary Zumkeller numbers* (2026), public mathematical record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-three-prime-support-classification-of-even-unitary-zumkeller-num--cd908a294237.
