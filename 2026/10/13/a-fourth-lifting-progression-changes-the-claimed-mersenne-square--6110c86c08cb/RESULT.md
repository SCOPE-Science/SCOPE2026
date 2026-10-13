# A fourth lifting progression changes the claimed Mersenne squarefreeness density
## Finding
For a positive integer \(m\), let \(M_m=2^m-1\), and define the exponent set
\[
\mathcal S=\{m\in\mathbb Z_{\ge1}: M_m\text{ is not squarefree}\}.
\]
Then
\[
\boxed{\liminf_{X\to\infty}\frac{1}{X}\#\{1\le m\le X:m\in\mathcal S\}\ge\frac{262}{1155}>\frac{47}{210}.}
\]
In particular, the value \(47/210\) asserted as the exact natural density for this exponent set in the public abstract of Laniewski's 2026 preprint cannot be the exact density. The result makes no assertion that the natural density of the full set \(\mathcal S\) exists.

## Assumptions and scope
There are no unproved hypotheses. Squarefree means not divisible by \(p^2\) for any prime \(p\); \(1\) is squarefree. The density lower bound concerns positive **exponents** \(m\), not the integers \(M_m\) ordered by magnitude. Let
\[
\mathcal A=\{m:6\mid m\text{ or }20\mid m\text{ or }21\mid m\},
\qquad\mathcal B=\{110k:k\ge1,\ \gcd(k,6)=1\}.
\]
We prove the periodic, disjoint containment \(\mathcal A\mathbin{\dot\cup}\mathcal B\subseteq\mathcal S\).

## Proof
**1. Four prime-square lifting families.** Direct modular exponentiation gives
\[
2^6\equiv1\pmod{3^2},\quad
2^{20}\equiv1\pmod{5^2},\quad
2^{21}\equiv1\pmod{7^2},\quad
2^{110}\equiv1\pmod{11^2}.
\]
These four are finite, independently reproducible exact congruences. For any positive integers \(t,k\), \(2^t-1\mid2^{tk}-1\) follows from the geometric-series factorization. Therefore every positive multiple of each of \(6,20,21,110\) belongs to \(\mathcal S\).

**2. Exact density of the first three progressions.** By inclusion-exclusion and elementary least common multiples, the periodic set \(\mathcal A\) has density
\[
\frac16+\frac1{20}+\frac1{21}-\frac1{60}-\frac1{42}-\frac1{420}+\frac1{420}
=\frac{47}{210}.
\]
This evaluates the three-progressions density without making any assertion about all nonsquarefree Mersenne exponents.

**3. A strictly new progression family.** Write \(m=110k\). Since \(\gcd(110,6)=2\), \(\gcd(110,20)=10\), and \(\gcd(110,21)=1\), the conditions \(6\mid m\), \(20\mid m\), and \(21\mid m\) become, respectively, \(3\mid k\), \(2\mid k\), and \(21\mid k\). Thus
\[
\{m:110\mid m\}\setminus\mathcal A
=\{110k:k\ge1,\gcd(k,6)=1\}=\mathcal B.
\]
The multiples of \(110\) are counted by \(1/110\) of all integers, and the proportion of integers \(k\) relatively prime to \(6\) is \(\varphi(6)/6=1/3\). Consequently \(\mathcal B\) has exact density \(1/330\) and is disjoint from \(\mathcal A\).

**4. Density comparison.** Since \(\mathcal A\mathbin{\dot\cup}\mathcal B\subseteq\mathcal S\),
\[
\liminf_{X\to\infty}X^{-1}\#(\mathcal S\cap[1,X])
\ge\frac{47}{210}+\frac1{330}
=\frac{262}{1155}.
\]
The strict positive gap \(1/330\) rules out \(47/210\) as the natural density of the full exponent set, independently of contributions from any other primes.

## Verification
Run `python3 verification/verify_mersenne.py` using the Python 3 standard library. It checks the four prime-square congruences, the least common multiple \(4620\), and all \(4620\) residue classes. There are \(1034\) classes in \(\mathcal A\), \(1048\) classes in the four-period union, and exactly \(14\) new classes, agreeing with \(14/4620=1/330\). These finite checks verify all arithmetical inputs. The infinite density assertion follows independently from exact periodicity and the elementary density of residue classes.

## Relationship to prior work
The public abstract of R. Laniewski, *Radical defects, Wieferich primes, and the abc conjecture*, arXiv:2609.00039v1 (September 2026), connects the \(\varepsilon=0\) Mersenne case to nonsquarefree values of \(2^m-1\) and asserts exponent density \(47/210\). The latter is precisely the density of the first three lifting progressions above, not a possible exact density once the independent \(11^2\)-lifting progression at exponent \(110\) is included. The arithmetic argument here is self-contained and does not rely on any conjecture about the \(abc\) problem. The full text of that preprint could not be inspected; the specific comparison is therefore to its publicly accessible abstract, not to an unseen theorem or proof.

## Limitations
The lower bound need not be sharp: additional prime-square divisibility progressions may increase it. This does not prove existence or give the exact value of the natural density of \(\mathcal S\), and it does not assess any other assertion in the motivating preprint. The precise overlap of this observation with unpublished or unindexed discussions cannot be excluded.

## References
R. Laniewski, *Radical defects, Wieferich primes, and the abc conjecture*, arXiv:2609.00039v1 (first publicly indexed September 2, 2026), abstract at `https://academ.us/article/2609.00039/`.

Elementary facts used: geometric-series divisibility and inclusion-exclusion on periodic integer sets.
