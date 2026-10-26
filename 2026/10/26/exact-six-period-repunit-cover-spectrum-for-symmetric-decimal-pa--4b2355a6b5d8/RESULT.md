# Exact six-period repunit-cover spectrum for symmetric decimal padding

## Finding

Put \(Q=(10^6-1)/9=111111\), and let \(R_m=(10^m-1)/9\). For a positive integer \(n\) with \(t\) decimal digits, define the symmetric-padded number
\[
F_t(d,m;n)=dR_m(10^{t+m}+1)+10^m n,
\]
whose decimal expansion consists of \(m\) copies of the digit \(d\), the digits of \(n\), and another \(m\) copies of \(d\). Let \(\mathcal C_t\) be the residues \(r\in\{0,\ldots,Q-1\}\) for which
\[
\gcd(F_t(d,m;r),Q)>1
\quad\text{for every }d\in\{1,3,7,9\}
\text{ and }1\le m\le6.
\]

The six possible residue classes of \(t\) modulo \(6\) give the **exact complete spectrum** below. Counts refer to residues \(r\) modulo \(Q\), rather than integers with a particular number of digits.

| \(t\bmod6\) | \(|\mathcal C_t|\) | \(r\in\mathcal C_t\) with \(3\mid r\) | \(r\in\mathcal C_t\) with \(11\mid r\) |
| ---: | ---: | ---: | ---: |
| 1 | 60 | 60 | 2 |
| 2 | 10121 | 3387 | 10101 |
| 3 | 111 | 111 | 74 |
| 4 | 10121 | 3387 | 10101 |
| 5 | 60 | 60 | 2 |
| 0 | 10101 | 3367 | 10101 |

In particular, every \(r\in\mathcal C_t\) satisfies
\[
3\mid r\quad\text{or}\quad(2\mid t\ \text{and}\ 11\mid r).
\]
Equivalently, if a decimal integer \(n\) is not a multiple of three and is not an even-digit multiple of eleven, there is already some \(d\in\{1,3,9\}\) and \(1\le m\le6\) for which \(F_t(d,m;n)\) is **coprime** to \(111111\). When \(t\equiv0\pmod6\), the cover criterion holds *exactly* when \(11\mid n\). When \(t\equiv2,4\pmod6\), all \(11\)-multiples qualify, together with precisely \(20\) additional residue classes, each divisible by \(3\).

## Assumptions and scope

All integers \(n\) are positive and are written in their ordinary decimal expansion, without leading zeroes. The padding digit \(d\) is between \(1\) and \(9\), and the padding length \(m\) is positive. The statement concerns **the particular covering certificate using prime divisors of \(Q\)**, not the primality of all padded integers. For a valid decimal \(n\), a \(Q\)-cover for the four digits \(1,3,7,9\) also proves compositeness for each of the other five positive padding digits, because they end in an even digit or five. The added padding makes each integer larger than every prime dividing \(Q\).

The prime factors of \(Q\) are exactly \(3,7,11,13,37\), all to the first power. A cover means that for each padding instance *at least one* of these primes divides that instance; the prime may depend on the digit and length. No assertion is made that one prime divides all instances.

## Proof

**1. Reduction from unbounded padding to a finite state space.** We have \(10^6-1=9Q\) and the exact integer identity
\[
R_{m+6}-R_m=10^mQ.
\]
Consequently \(10^{a+6}\equiv10^a\pmod Q\) and \(R_{m+6}\equiv R_m\pmod Q\) for every nonnegative integer \(a\) and positive integer \(m\). The residue of \(F_t(d,m;n)\) modulo \(Q\) therefore depends only on \(t\bmod6\), \(m\bmod6\), \(d\), and \(n\bmod Q\). Thus six checks per digit, over all \(Q\) residues of \(n\), decide the infinite-length cover problem without any untested higher-length cases.

**2. An independent prime-by-prime criterion.** As \(10\) is invertible modulo every \(p\mid Q\), the condition \(p\mid F_t(d,m;r)\) is equivalent to the single residue constraint
\[
r\equiv -dR_m(10^{t+m}+1)(10^m)^{-1}\pmod p.
\]
For each fixed \((t,d,m)\), the criterion \(\gcd(F_t(d,m;r),Q)>1\) is precisely the union of these five single-residue congruence classes. Intersecting the unions for the twenty-four pairs \((d,m)\), with \(d\in\{1,3,7,9\}\) and \(1\le m\le6\), gives exactly \(\mathcal C_t\). This is a fully specified finite Boolean/CRT computation.

**3. A short obstruction certificate.** Let \(Q_0=7\cdot11\cdot13\cdot37=37037\). Suppose \(3\nmid n\). For padding digits \(d=3\) and \(d=9\), the prime \(3\) cannot divide any padded number (its residue is \(n\bmod3\)). Thus those twelve instances must be covered by primes dividing \(Q_0\). Applying the congruence in Step 2 modulo the four primes of \(Q_0\), for all \(m=1,\ldots,6\), gives:

| \(t\bmod6\) | All qualifying residues \(n\bmod Q_0\) for digits \(3,9\) |
| ---: | --- |
| 1 | \(10406,11843\) |
| 2 | exactly the multiples of \(11\) |
| 3 | \(2701,6512,10989,16132\) |
| 4 | exactly the multiples of \(11\) |
| 5 | \(28589,32149\) |
| 0 | exactly the multiples of \(11\) |

For odd \(t\), every one of the eight listed possibilities is eliminated by the padding digit \(d=1\), as follows. Since \(\gcd(Q_0,3)=1\), a residue \(r\bmod Q_0\) has exactly one lift modulo \(Q\) in each specified residue class modulo \(3\). Each table entry displays a padding length \(m\) at which the corresponding lifted number with \(d=1\) has gcd **one** with \(Q\):

| \(t\bmod6\) | \(r\bmod Q_0\) | \(m\) if \(n\equiv1\pmod3\) | \(m\) if \(n\equiv2\pmod3\) |
| ---: | ---: | ---: | ---: |
| 1 | 10406 | 3 | 1 |
| 1 | 11843 | 3 | 3 |
| 3 | 2701 | 2 | 4 |
| 3 | 6512 | 5 | 1 |
| 3 | 10989 | 5 | 1 |
| 3 | 16132 | 2 | 1 |
| 5 | 28589 | 3 | 1 |
| 5 | 32149 | 2 | 1 |

The two small tables follow by the explicit congruence criterion in Step 2. They are checked independently and exhaustively in `verify.py` (the first uses only \(37037\) residue states for each digit-length class). Thus an odd-digit \(Q\)-cover necessarily has \(3\mid n\). For even \(t\), the first table forces \(11\mid n\) whenever \(3\nmid n\), as claimed.

**4. Exact spectrum and sufficient even-length cases.** The first table in the Finding is obtained by applying the explicit gcd condition in the definition to every \(r=0,1,\ldots,Q-1\) for each of the six length classes. The complete program `verify.py` performs this exhaustive check, independently reconstructs every test from the five modular roots, compares the two Boolean answers on **all \(6Q=666666\) states**, and checks every displayed count.

If \(t\) is even and \(11\mid n\), then \(11\mid F_t(d,m;n)\) for every \(d\) and \(m\): modulo \(11\), the factor \(R_m\) is zero when \(m\) is even, whereas \(10^{t+m}+1\) is zero when \(m\) is odd. This also explains the universal even-length subset of \(10101=Q/11\) residue classes. The finite complete census leaves exactly twenty additional classes in each of the length classes \(2\) and \(4\), and no additional class when \(t\equiv0\pmod6\).

## Verification

Run `python3 verify.py` with the standard Python library. The expected output is:

```text
t, qualifying residues, divisible by 3, divisible by 11
1 60 60 2
2 10121 3387 10101
3 111 111 74
4 10121 3387 10101
5 60 60 2
6 10101 3367 10101
VERIFY_OK: all 666666 residue states, two independent criteria
```

The direct branch uses exact integer gcds. The independent branch uses residue roots separately for the primes \(3,7,11,13,37\). A third check enumerates all \(Q_0\) residues to verify the compressed obstruction table and all sixteen explicit odd-length witnesses. Since Step 1 *proves* that these finite states exhaust all possible positive padding lengths and all integers \(n\), this is an exhaustive finite certificate for the stated universal conditional result, not a bounded experiment extrapolated to infinity.

The source's examples \(n=231,420,759\) satisfy the six-period condition; \(n=6363\) does not satisfy this narrower cover, consistent with its use of a longer repunit period.

## Relationship to prior work

Wu (2015, Sections 2 and 4) establishes many symmetric-padding examples by covering primes dividing repunits, states a conjecture that nonstandard universally composite centers must be multiples of \(3\), and reports that the \(4919\) centers found below \(10^7\) are multiples of \(3\). That search observation is not the all-residue, all-digit-length, exact \(Q\)-cover spectrum proved above. The present theorem isolates a **limit of the six-period certificate itself**, rather than proving Wu's conjecture for every possible compositeness argument or longer cover. OEIS A090287 introduced the underlying symmetric-padding prime problem. Grantham, Jarnicki, Rickert, and Wagon (2019) develop coverings for **one-sided** repeated-digit appending; their existence theorem and seed constructions do not classify this two-sided, fixed-\(Q\) intersection.

## Limitations

The failure of a \(Q\)-cover does **not** imply that any padded integer is prime: a prime factor outside \(\{3,7,11,13,37\}\), another repunit length, or a non-covering factorization could still prove compositeness. No claim is made about all covering lengths or about the truth of the broad symmetric-padding conjecture. The counts are for complete residue classes modulo \(Q\), not for numbers below an arbitrary finite bound, nor for an independent distribution of primality. The originality comparison may be incomplete with respect to informal computations or unlocated publications.

## References

1. OEIS Foundation, A090287, *Smallest prime obtained by sandwiching n between a number with identical digits*, initial sequence dated 2003-11-29; https://oeis.org/A090287.
2. Chai Wah Wu, *On a conjecture regarding primality of numbers constructed from prepending and appending identical digits*, first submitted 2015-03-31, arXiv:1503.08883v1; Sections 2–4, https://arxiv.org/html/1503.08883v2.
3. Jon Grantham, Witold Jarnicki, John Rickert, Stan Wagon, *Repeatedly Appending Any Digit to Generate Composite Numbers*, first submitted 2019-03-12, arXiv:1903.05023; https://arxiv.org/abs/1903.05023.
