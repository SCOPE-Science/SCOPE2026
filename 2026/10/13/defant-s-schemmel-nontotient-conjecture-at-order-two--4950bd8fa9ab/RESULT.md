# Defant's Schemmel nontotient conjecture at order two
## Finding
Let \(S_2\) be the second Schemmel totient function and let
\[
G_2=\mathbb{Z}_{>0}\setminus S_2(\mathbb{Z}_{>0}).
\]
Define
\[
M=1620742097628261335
\]
and
\[
C=206033543146003779.
\]
Then every prime \(p>M\) in the arithmetic progression
\[
p\equiv C\pmod M
\]
satisfies
\[
3^\alpha p\in G_2
\]
for every integer \(\alpha\ge0\).

Since \(\gcd(C,M)=1\), Dirichlet's theorem gives infinitely many primes in this progression. Therefore Conjecture 4.1 of Defant's *On Schemmel Nontotient Numbers* holds for \(r=2\).

## Assumptions and scope
For a prime \(\ell\) and integer \(e\ge1\), the second Schemmel totient is
\[
S_2(\ell^e)=
\begin{cases}
0,&\ell\le2,\\
\ell^{e-1}(\ell-2),&\ell>2,
\end{cases}
\]
extended multiplicatively.

Defant's Lemma 2.2 states that if \(r+1\) and \(p\) are prime, then
\[
(r+1)^\alpha p\in G_r
\]
if and only if, for every integer \(t\) with \(0\le t\le\alpha\),
\[
p\ne(r+1)^t+r
\]
and
\[
(r+1)^tp+r
\]
is composite.

For \(r=2\), it therefore suffices to construct infinitely many primes \(p\) such that
\[
p\ne3^t+2
\]
and
\[
3^tp+2
\]
is composite for every \(t\ge0\).

## Proof
Use the following ten congruence classes in the exponent \(t\). The third column records a prime \(q\) for which \(\operatorname{ord}_q(3)\) is the modulus in the second column, and the fourth column gives the imposed residue of \(p\) modulo \(q\).

\[
\begin{array}{c|c|c|c}
t\text{ residue}&\text{modulus}&q&p\text{ residue mod }q\\
\hline
0&3&13&11\\
3&4&5&4\\
4&6&7&3\\
1&8&41&13\\
8&12&73&57\\
13&16&17&14\\
5&16&193&54\\
2&24&6481&1440\\
14&48&97&49\\
38&48&577&187
\end{array}
\]

The ten exponent classes cover every residue modulo \(48\). The order equalities are
\[
\operatorname{ord}_{13}(3)=3,\quad
\operatorname{ord}_5(3)=4,\quad
\operatorname{ord}_7(3)=6,\quad
\operatorname{ord}_{41}(3)=8,
\]
\[
\operatorname{ord}_{73}(3)=12,\quad
\operatorname{ord}_{17}(3)=16,\quad
\operatorname{ord}_{193}(3)=16,\quad
\operatorname{ord}_{6481}(3)=24,
\]
\[
\operatorname{ord}_{97}(3)=48,\qquad
\operatorname{ord}_{577}(3)=48.
\]

For a row with exponent residue \(a\), modulus \(m\), prime \(q\), and residue \(c\), direct modular arithmetic gives
\[
3^ac+2\equiv0\pmod q.
\]
Hence if
\[
t\equiv a\pmod m
\]
and
\[
p\equiv c\pmod q,
\]
then the order condition gives
\[
3^tp+2\equiv3^ac+2\equiv0\pmod q.
\]

The Chinese remainder theorem applied to the ten \(p\)-congruences gives exactly one residue class modulo the product of the ten primes. That product is
\[
M=1620742097628261335,
\]
and the least nonnegative solution is
\[
C=206033543146003779.
\]
Moreover
\[
\gcd(C,M)=1.
\]
Thus Dirichlet's theorem supplies infinitely many primes
\[
p\equiv C\pmod M.
\]
Restrict to those with \(p>M\).

Fix such a prime \(p\) and any \(t\ge0\). Choose a row whose exponent class contains \(t\). The corresponding prime \(q\) divides \(3^tp+2\). Since
\[
3^tp+2>p>M\ge q,
\]
the integer \(3^tp+2\) is composite.

It remains to exclude
\[
p=3^s+2.
\]
The \(q=41\) row forces
\[
p\equiv13\pmod{41}.
\]
If \(p=3^s+2\), then
\[
3^s\equiv11\pmod{41}.
\]
But \(\operatorname{ord}_{41}(3)=8\), and the eight powers of \(3\) modulo \(41\) are
\[
1,3,9,27,40,38,32,14,
\]
none of which is \(11\). Thus
\[
p\ne3^s+2
\]
for every \(s\ge0\).

Defant's Lemma 2.2 now applies for every \(\alpha\ge0\), yielding
\[
3^\alpha p\in G_2.
\]
Since infinitely many primes \(p\) occur, the \(r=2\) case of Conjecture 4.1 follows.

## Verification
The accompanying `cover_certificate.json` contains the ten rows, the exact modulus \(M\), and the exact CRT residue \(C\).

The accompanying `verify.py` checks, by exact integer arithmetic, that:

1. every listed \(q\) is prime;
2. every listed multiplicative order is exact;
3. every exponent residue row gives
\[
3^ac+2\equiv0\pmod q;
\]
4. the ten exponent classes cover all \(48\) residues;
5. the product of the ten primes is \(M\), the CRT solution is \(C\), and \(\gcd(C,M)=1\);
6. \(11\) is not a power of \(3\) modulo \(41\).

No finite computation is used to infer infinitude. The infinite step is Dirichlet's theorem on primes in arithmetic progressions, while Defant's Lemma 2.2 supplies the exact Schemmel-nontotient criterion.

## Relationship to prior work
Defant's paper proves a general sufficient theorem when \(r+1\) is a prime that is not Mersenne and an additional equal-order condition is available. It then explicitly states Conjecture 4.1 for every \(r\) such that \(r+1\) is prime.

The present theorem treats
\[
r=2,\qquad r+1=3,
\]
which is excluded from Defant's Theorem 2.1 precisely because \(3\) is a Mersenne prime. The proof replaces the source's power-of-two order construction by an explicit finite covering of exponent classes using orders
\[
3,4,6,8,12,16,24,48.
\]

Targeted searches for Conjecture 4.1, the \(r=2\) case, the family \(3^\alpha p\), and the equivalent condition that \(3^tp+2\) be composite for every \(t\) located no later proof of this parameter case. Indexed research-record searches likewise returned no equivalent statement.

## Limitations
This proves only the \(r=2\) case of Defant's conjecture, not Conjecture 4.1 for every prime \(r+1\).

The constructed arithmetic progression is explicit but not claimed to have minimal modulus or minimal covering size. The argument establishes infinitude, not an asymptotic count beyond what follows immediately from Dirichlet's theorem for the displayed progression.

The originality search covered the primary full text, its journal bibliographic record, exact-phrase web searches, and indexed semantic research records. An unindexed independent proof remains a residual risk.

## References
1. C. Defant, “On Schemmel Nontotient Numbers,” arXiv:1412.3089v1, first public 9 December 2014; later *Journal of Combinatorics & Number Theory* 8 (2016), 233–239.
2. P. G. L. Dirichlet, theorem on primes in arithmetic progressions.
