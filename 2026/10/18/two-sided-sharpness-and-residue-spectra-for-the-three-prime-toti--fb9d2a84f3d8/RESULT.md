# Two-sided sharpness and residue spectra for the three-prime totient discrepancy

## Finding
Let \(T(n)\) be Renshaw's totient, let \(S(n)\) be Schemmel's second totient, and put
\[
D(n)=T(n)-\frac{S(n)-1}{2}
\]
for odd integers \(n>1\). The known three-prime upper bound \(\lvert D(n)\rvert\le 6\) is **optimal on both sides even for squarefree integers**. In fact, for every prime \(r\) in the indicated coprime residue class,
\[
D(65r)=-6\quad\text{if }r\equiv24\pmod{65},\qquad
D(119r)=6\quad\text{if }r\equiv31\pmod{119}.
\]
Both classes contain infinitely many primes by Dirichlet's theorem. The resulting squarefree integers have exactly three distinct prime factors. The two fixed products \(65\) and \(119\) are respectively the smallest products of two distinct odd primes for which a coprime third-prime residue class attains the negative and positive endpoints.

More precisely, as \(r\) ranges over primes coprime to the stated fixed product, the complete residue-class distribution is

| Fixed product \(P\) | Possible \(D(Pr)\) in increasing order | Corresponding numbers of reduced residue classes |
| --- | --- | --- |
| \(65\) | \(-6,-4,-2,0,2,4\) | \(1,5,18,18,5,1\) |
| \(119\) | \(-4,-2,0,2,4,6\) | \(1,10,37,37,10,1\) |

Each count divided by \(\varphi(P)\), respectively \(48\) or \(96\), is also the natural relative density of that value among primes, by the prime number theorem for fixed arithmetic progressions. The extreme classes are unique: \(24\pmod{65}\) and \(31\pmod{119}\).

## Assumptions and scope
For every odd integer \(n>1\), define
\[
T(n)=\#\{m\in\{1,3,\ldots,n\}:\gcd(m,n)=\gcd((m-1)/2,n)=1\},
\]
\[
S(n)=\#\{u\in\{1,\ldots,n\}:\gcd(u,n)=\gcd(u-1,n)=1\}
=n\prod_{p\mid n}(1-2/p).
\]
For an odd integer \(P>1\) and any integer \(a\) coprime to \(P\), set
\[
B_P(a)=\#\{j\in\{1,3,\ldots,P\}:\gcd(j,P)=\gcd(aj-1,P)=1\}.
\]
The prime \(r\) is always odd and coprime to \(P\). The two-sided endpoint and distribution assertions above concern squarefree integers with three distinct odd prime factors, with \(P\) the displayed fixed two-prime product. The finite minimality assertion is about fixed products \(P=pq\) of distinct odd primes, not about the least possible integer \(n\) attaining an endpoint.

## Proof
**1. Fixed-support identity.** Partition \(1\le m\le Pr\) into \(r\) consecutive blocks of length \(P\). The admissibility conditions for \(T\) at primes dividing \(P\) are precisely \(\gcd(m,P)=\gcd(m-1,P)=1\), since \(2\) is a unit modulo \(P\). There are \(S(P)\) admissible residue classes modulo \(P\). As \(P\) and \(r\) are odd, each class contributes \((r-1)/2\) odd representatives, plus one extra if its representative between \(1\) and \(P\) is odd. The number before imposing the conditions at \(r\) is therefore
\[
\frac{r-1}{2}S(P)+T(P).
\]

For the first exclusion, \(r\mid m\), write \(m=rj\) with \(1\le j\le P\). The parity and coprimality conditions are exactly those defining \(B_P(r)\), so this exclusion removes \(B_P(r)\) terms. For the second exclusion, \(r\mid(m-1)\), write \(m=1+rj\) with \(0\le j<P\). Admissible \(m\) is odd exactly when \(j\) is even. Mapping \(j\) to \(P-j\) bijects these terms (the inadmissible \(j=0\) causes no exception) with the set counted by \(B_P(r)\). The two exclusions are disjoint because \(r>1\). Hence
\[
T(Pr)=\frac{r-1}{2}S(P)+T(P)-2B_P(r).
\]
The multiplicativity of Schemmel's function gives \(S(Pr)=(r-2)S(P)\). Subtraction proves the exact identity
\[
\boxed{\displaystyle D(Pr)=\frac{S(P)+1}{2}+T(P)-2B_P(r)}.\tag{1}
\]
In particular \(D(Pr)\) depends only on \(r\bmod P\), not on the magnitude of the prime. The reflection \(j\mapsto P-j\) also yields
\[
B_P(a)+B_P(-a)=S(P),\qquad
D_P(a)+D_P(-a)=2T(P)-S(P)+1,\tag{2}
\]
where \(D_P(a)\) denotes the right side of (1) for a reduced residue \(a\).

**2. Exact endpoint witnesses.** The complete elementary counts are
\[
(S(65),T(65),B_{65}(24))=(33,15,19),
\qquad(S(119),T(119),B_{119}(31))=(75,38,35).
\]
For explicit independently inspectable certificates, the odd representatives counted by the two \(B\)-values are respectively

\(P=65\): `1,3,7,11,17,21,23,27,31,33,37,41,43,47,51,53,57,61,63`;

\(P=119\): `1,3,9,13,15,23,25,27,29,31,37,39,41,43,53,55,57,59,65,67,69,71,73,81,83,87,93,95,97,99,101,107,109,111,115`.

Each list is exactly the odd \(j\) in \([1,P]\) for which both gcd tests in the definition of \(B_P(a)\) equal one. Formula (1) gives \(D_{65}(24)=17+15-38=-6\) and \(D_{119}(31)=38+38-70=6\). Since \(\gcd(24,65)=\gcd(31,119)=1\), Dirichlet's theorem supplies infinitely many primes in both classes, establishing both infinite endpoint families and the optimality of constant \(6\) in Renshaw's bound when \(\omega(n)=3\). Examples are \(r=89\), with \(n=5785\), \(T(n)=1429\), \(S(n)=2871\), and \(r=31\), with \(n=3689\), \(T(n)=1093\), \(S(n)=2175\).

**3. Entire residue spectra.** For each fixed \(P\) in \(\{65,119\}\), enumerate all \(a\) in \(1\le a<P\) with \(\gcd(a,P)=1\). Count the odd \(j\) satisfying the two gcd tests, compute the right side of (1), and group by the resulting integer. This is a complete finite calculation over exactly \(48\) or \(96\) residue classes, not sampled primes. Its exact count tables are displayed in Finding, and executable standard-library code reproduces them. Unique extreme classes follow from the complete same enumeration. Dirichlet's theorem provides infinitely many primes in each class, and the prime number theorem in arithmetic progressions supplies the stated relative frequencies.

**4. Minimal fixed supports.** Enumerate all squarefree products of two distinct odd primes smaller than \(65\); these are \(15,21,33,35,39,51,55,57\). Exact evaluation of (1) over each reduced residue class yields no value \(-6\). Enumerating those smaller than \(119\), namely \(15,21,33,35,39,51,55,57,65,69,77,85,87,91,93,95,111,115\), yields no value \(6\). For reproducibility, the complete \((P,\min D_P,\max D_P)\) table through \(119\) is: `(15,-4,2), (21,0,2), (33,-4,2), (35,-2,4), (39,0,2), (51,-4,2), (55,-2,4), (57,0,2), (65,-6,4), (69,-4,2), (77,-6,4), (85,-2,4), (87,-4,2), (91,-6,4), (93,0,2), (95,-6,4), (111,0,2), (115,-6,4), (119,-4,6)`. These are all possibilities because each odd product below the bound is tested for having exactly two distinct prime divisors, and all its reduced residue classes are tested. The supplied finite checker reproduces these exhaustive conclusions.

## Verification
The standalone Python 3 standard-library program `verification/verify.py` recomputes \(S,T,B\) directly from their definitions; tests identity (1) on numerous independent odd supports and coprime primes; tests reflection identity (2); exhaustively computes the two residue spectra and minimal fixed-support tables; and directly counts the two displayed numerical witnesses. Its execution on the packaged source produced `PASS: 7020 exact integer checks`. These finite checks validate computations and boundary certificates, not the infinitude conclusion; that follows from the proved identity and Dirichlet's theorem. The analytic prime-density statement uses the classical prime number theorem for fixed arithmetic progressions.

## Relationship to prior work
Renshaw, *A Totient Function Associated with Variants of Groups* (arXiv:2603.13939v1, publicly submitted 2026-03-14), introduces \(T\) and proves Theorem 3:
\[
\left|T(n)-\frac{S(n)-1}{2}\right|\le\frac{3^{\omega(n)}-2^{\omega(n)+1}+1}{2}.
\]
For three distinct prime factors the right side is \(6\). His paper does not give the two-sided infinite sharpness progressions, complete reduced-residue spectra, or smallest two-prime fixed supports established above. The result here does not claim that the published bound, the Schemmel product formula, Dirichlet's theorem, or the prime number theorem in progressions are new. Related literature on the parity of the two-prime \(T\)-branch does not imply existence or densities of the three-prime extreme classes.

## Limitations
This result establishes sharpness only for \(\omega(n)=3\), not for every number of prime factors. The exact prime-residue spectra are for the two fixed supports \(P=65\) and \(P=119\); identity (1), however, applies to any odd \(P>1\) with an external coprime odd prime. The two fixed products are minimal for each **sign** within the fixed-support problem, not necessarily the smallest full three-prime integers attaining \(\pm6\). No claim of novelty is made for the classical distribution of primes in arithmetic progressions. A full bibliographic proof of noncoverage by every possible unpublished or older implicit derivation is not asserted.

## References
1. James Renshaw, *A Totient Function Associated with Variants of Groups*, arXiv:2603.13939v1, 2026-03-14, Section 2, Theorem 3 and Corollary 6. https://arxiv.org/html/2603.13939v1
2. V. Schemmel, *Über relative Primzahlen*, Journal für die reine und angewandte Mathematik **70** (1869), 191–192. Cited in Renshaw's reference [7].
3. Dirichlet's theorem and the prime number theorem on primes in fixed reduced arithmetic progressions (standard classical theorems).
