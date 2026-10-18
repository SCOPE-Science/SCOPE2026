# Sharp \(1260\)-conductor for the early odd-greedy length profile of twice prime reciprocals

## Finding

Let \(p>3\) be a prime, and run the odd-greedy Egyptian-fraction algorithm on \(2/p\): at each positive rational remainder choose the reciprocal of the **least positive odd integer** whose reciprocal does not exceed that remainder. Let \(L(p)\) be the resulting number of terms if the process terminates, and \(L(p)=\infty\) otherwise. Then the exact four-way early stopping profile is

\[
L(p)=\begin{cases}
2,&p\equiv1\pmod4,\\
4,&p\equiv7\pmod{20},\\
6,&p\equiv3\pmod4,\ p\not\equiv7\pmod{20},\text{ and }\bigl(p\bmod9\in\{1,2,4,5\}\text{ or }p\equiv4\pmod7\bigr),\\
\ge8\text{ or }\infty,&\text{otherwise}.
\end{cases}
\]

Here the last row is **not** a claim of termination. The four categories depend only on \(p\bmod1260\), and **\(1260\) is the least positive modulus** for which every prime greater than three has its category determined by its residue class modulo that modulus. Among primes, the four categories have respective natural densities \(1/2\), \(1/8\), \(13/48\), and \(5/48\). In particular, the last density is for primes with **no termination within seven terms**; it does not assert infinitely many nonterminating inputs.

## Assumptions and scope

The input is a reduced positive fraction \(2/p<2/3\) with \(p>3\) prime. In this range, allowing versus forbidding repeated odd denominators or the denominator \(1\) does not change the algorithm. All indicated congruences are ordinary integer congruences. The term \(L(p)=\infty\) is allowed because termination for every rational with odd denominator remains open. The natural density of a prime set \(\mathcal P\) is \(\lim_{x\to\infty}\#\{p\le x:p\in\mathcal P\}/\pi(x)\), where it exists.

## Proof

**Parity.** A finite sum of \(t\) reciprocals of odd integers has, when placed over their odd product, a numerator with parity \(t\). Reduction cannot change this parity. Since the reduced numerator of \(2/p\) is even, a terminating expansion has **even** length. A one-step expansion is impossible because \(p>3\).

**First two steps.** When \(p\equiv1\pmod4\), put \(d=(p+1)/2\). This is odd, is the least odd integer at least \(p/2\), and \(2/p-1/d=1/(pd)\). The second and last greedy denominator is \(pd\), so \(L(p)=2\).

Now assume \(p\equiv3\pmod4\), and set \(d=(p+3)/2\), \(M=pd\). The first greedy subtraction is
\[
\frac2p-\frac1d=\frac3M.
\]
As \(p\ne3\), one has \(M\equiv5\pmod6\). Consequently \(e=(M+4)/3\) is the least odd integer at least \(M/3\); put \(D=Me\). The second subtraction is
\[
\frac3M-\frac1e=\frac4D.
\]
For any odd \(M\), \(M(M+4)\equiv5\pmod8\). Division by \(3\) modulo \(8\) gives \(D\equiv7\pmod8\). Thus \(f=(D+5)/4\) is the least odd integer at least \(D/4\), \(B=Df\) is odd, and the third subtraction gives
\[
\frac4D-\frac1f=\frac5B.
\]
For primes \(p\equiv3\pmod4\), reduction of the three expressions modulo \(5\) shows that \(B\equiv0\pmod5\) exactly when \(p\equiv2\pmod5\); otherwise \(B\equiv4\pmod5\). (Indeed \(M=p(p+3)/2\), \(D=M(M+4)/3\), and \(B=D(D+5)/4\); their residues can be evaluated with inverses of \(2,3,4\) modulo \(5\).) In the first case, \(5/B=1/(B/5)\) ends the expansion at length four. Intersecting \(p\equiv3\pmod4\) with \(p\equiv2\pmod5\) gives \(p\equiv7\pmod{20}\).

**The sixth-term split.** Continue in the complementary case. Since \(B\equiv4\pmod5\) is odd, it is \(9\pmod{10}\), and \(u=(B+6)/5\) is the least odd integer at least \(B/5\). With \(C=Bu\), the fourth subtraction is
\[
\frac5B-\frac1u=\frac6C,\qquad C=\frac{B(B+6)}5.
\]
For every odd \(B\), \(B(B+6)\equiv3\pmod4\); hence \(C\equiv3\pmod4\). Also \(u\equiv2B\pmod3\), so \(3\mid C\) precisely when \(3\mid B\). In this case \(6/C=2/(C/3)\), where \(C/3\equiv1\pmod4\); the earlier two-step argument ends the expansion at length six.

To identify this case, reduce \(M=p(p+3)/2\) modulo \(9\). For the six nonzero prime residues \(p\bmod9\in\{1,2,4,5,7,8\}\), the corresponding residues of \(M\bmod9\) are \(2,5,5,2,8,8\). Since \(B=D(D+5)/4\) and \(D=M(M+4)/3\), one obtains \(3\mid B\) exactly for \(M\equiv2,5\pmod9\). Thus the first six-term branch is exactly \(p\bmod9\in\{1,2,4,5\}\).

Finally suppose \(3\nmid B\). Then \(C\equiv2\pmod3\) and \(C\equiv3\pmod4\), so \(C\equiv11\pmod{12}\). The fifth greedy denominator is the odd integer \(v=(C+7)/6\), and the fifth subtraction is \(6/C-1/v=7/(Cv)\). The next (sixth) term ends the expansion if and only if \(7\mid Cv\), equivalent to \(7\mid C\) because \(v\equiv6^{-1}C\pmod7\).

Modulo \(7\), the expression \(C=B(B+6)/5\) vanishes exactly when \(B\equiv0\) or \(1\). The latter is impossible: \(B=D(D+5)/4\equiv1\) would imply \(D^2+5D-4\equiv0\pmod7\), whose discriminant \(41\equiv6\pmod7\) is not a square. For prime residues \(p\bmod7\in\{1,2,3,4,5,6\}\), the corresponding values of \(D\bmod7\) are \(4,1,4,0,6,6\). Hence \(B\equiv0\pmod7\) exactly when \(p\equiv4\pmod7\). If neither six-term branch applies, the fifth remainder has reduced numerator \(7\), not \(1\), so termination has not occurred after six steps. The parity argument rules out exactly seven terms. This proves all four alternatives, including the possibility of nontermination in the last category.

**Densities and sharp conductor.** The criterion is constant on reduced residue classes modulo \(1260=4\cdot5\cdot9\cdot7\). Of the \(\varphi(1260)=288\) unit classes, exact Chinese-remainder counting gives \(144\), \(36\), \(78\), and \(30\) in the four categories. Equivalently, the first two densities are \(1/2\) and \((1/2)(1/4)=1/8\). The remaining \(3/8\) splits: four of six unit classes modulo \(9\) end at six terms, and one of six classes modulo \(7\) ends at six terms within the other two modulo \(9\). This gives \((3/8)[4/6+(2/6)(1/6)]=13/48\) and residual \((3/8)(2/6)(5/6)=5/48\). The prime number theorem in arithmetic progressions (or Dirichlet together with the corresponding prime-distribution theorem) supplies these natural densities.

For least modulus, the following are pairs of unit classes modulo \(1260\), with different stopping categories but equal residues modulo the respective divisor: \((1,631)\) modulo \(630\); \((19,439)\) modulo \(420\); \((11,767)\) modulo \(252\); and \((43,403)\) modulo \(180\). Therefore no modulus \(1260/\ell\), for \(\ell\in\{2,3,5,7\}\), and hence no proper divisor of \(1260\), determines the category. More generally, suppose any positive modulus \(m\) determines the category for all sufficiently large primes. For unit residue classes modulo \(1260\) agreeing modulo \(\gcd(m,1260)\), choose a common unit residue modulo \(m\) compatible with both; the generalized Chinese remainder theorem and Dirichlet's theorem produce primes in each intersection. Their categories must agree. Consequently \(\gcd(m,1260)\) would also be sufficient, forcing \(1260\mid m\). This proves minimality over **all** positive moduli.

## Verification

The standalone program `verify.py` independently implements the greedy recurrence using exact integer fractions, compares its first seven steps against the four-case classification for every prime \(5\le p\le100000\), checks the \(288\) unit classes, independently verifies the category counts, and checks the four minimal-modulus witnesses. Its expected and observed terminal message is `VERIFY_OK primes=9590 unit_classes=288 counts={2: 144, 4: 36, 6: 78, 8: 30} minimal_divisor_period=1260`. These finite calculations are consistency checks; the congruence proof, Dirichlet's theorem, and the prime number theorem in arithmetic progressions establish the general statements.

## Relationship to prior work

Pihko's 2001 and 2010 papers study numerator transitions and the open termination problem for odd-greedy expansions. Louwsma and Martino's 2023 preprint (Theorem 2.3) and 2025 paper (Corollary 5, Example 6) already characterize two-term expansions, including the \(2/p\) case, so the length-two branch above is **not** new. Earlier finite-horizon periodicity work already implies that bounded stopping questions have some congruence description and established the four-term behavior for arbitrary odd denominators; the four-term branch above is background. The specific new result is the **six-term prime-residue criterion, exact four-way prime density, and proof of the least possible modulus \(1260\)**, none of which follows as an explicit value from the generic periodicity statement or the two-term classification. Chen–Elsholtz–Jiang's 2011 work is a dated archival study of Egyptian fractions with restrictions but does not discuss this prime odd-greedy stopping profile.

## Limitations

The last category mixes expansions that terminate at eight or more terms with any that might fail to terminate; it is not a classification of eventual termination. The two- and four-term subcases are acknowledged prior knowledge. The new quantitative claim is a low-horizon exact result, and its novelty remains exposed to a differently formulated or unindexed prior congruence table. The proof uses the prime number theorem in arithmetic progressions for densities; Dirichlet's theorem alone proves infinitude of classes but not their density values. No independent audit or external validation has been performed.

## References

1. J. Pihko, *Remarks on the “Greedy Odd” Egyptian Fraction Algorithm*, Fibonacci Quarterly 39 (2001), 221–227. Full text: https://www.fq.math.ca/Scanned/39-3/pihko.pdf .
2. J. Pihko, *Remarks on the “Greedy Odd” Egyptian Fraction Algorithm II*, Fibonacci Quarterly 48 (2010), 202–208. Full text: https://www.fq.math.ca/Scanned/48-3/pihko.pdf .
3. Y.-G. Chen, C. Elsholtz and L.-L. Jiang, *Egyptian Fractions with Restrictions*, arXiv:1108.6118v1 (first submitted 2011-08-31). https://arxiv.org/abs/1108.6118 .
4. J. Louwsma and J. Martino, *Rational numbers with odd greedy expansion of fixed length*, arXiv:2309.07280v1 (2023). https://arxiv.org/abs/2309.07280 .
5. J. Louwsma and J. Martino, *Rational Numbers with Two-Term Odd Greedy Expansion*, Integers 25 (2025), A46. https://math.colgate.edu/~integers/z46/z46.pdf .
