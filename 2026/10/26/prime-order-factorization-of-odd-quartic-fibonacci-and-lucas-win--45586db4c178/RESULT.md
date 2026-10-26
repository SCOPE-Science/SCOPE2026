# Prime-order factorization of odd quartic Fibonacci and Lucas window GCDs

## Finding
Let \(F_0=0,F_1=1\) and \(L_0=2,L_1=1\), with the common recurrence \(X_{n+2}=X_{n+1}+X_n\). Define, for each positive integer \(k\),
\[G_X(k)=\gcd_{n\ge0}\left(\sum_{j=1}^{k}X_{n+j}^{4}\right),\qquad X\in\{F,L\}.\]
For each prime \(p\ge7\), define the finite quadratic algebra
\[A_p=\mathbb F_p[t]/(t^2+3t+1),\qquad r_p=\operatorname{ord}_{A_p^\times}(t).\]
The element \(t\) is invertible since its minimal polynomial has constant term one. **Theorem.** For every positive odd \(k\) satisfying \(5\nmid k\),
\[\boxed{G_F(k)=G_L(k)=2^{\mathbf1_{3\mid k}}\prod_{\substack{p\mid k,\,p\ge7\\r_p\mid k}}p^{\nu_p(k)}.}\]
The product is over distinct prime divisors \(p\) of \(k\); an empty product equals one. For example, the odd lengths \(k=21,91,153,703\) give respective values \(2,13,34,37\).

## Assumptions and scope
All greatest common divisors are positive. The index \(n\) ranges over all nonnegative integers and each window contains exactly \(k\) consecutive positive-indexed terms. The theorem covers both standard initial conditions, all positive odd lengths relatively prime to five, and no even length or length divisible by five. The order \(r_p\) is that of the residue class of \(t\) in the full unit group even when the quadratic algebra is split. The indicator \(\mathbf1_{3\mid k}\) is one precisely when three divides \(k\).

## Proof
**Five distinct spectral modes.** Let \(\alpha,\beta\) be roots of \(z^2-z-1\), so that \(\alpha\beta=-1\). In the quadratic extension of the rationals, the Binet formulas give
\[25F_n^4=L_{4n}-4(-1)^nL_{2n}+6,\qquad L_n^4=L_{4n}+4(-1)^nL_{2n}+6.\]
Put \(\rho=-\alpha^2\), whence \(\rho^{-1}=-\beta^2\) and \(\rho^2=\alpha^4\), \(\rho^{-2}=\beta^4\). The two fourth-power sequences are therefore linear combinations of the five exponential modes
\[1,\ \rho^n,\ \rho^{-n},\ \rho^{2n},\ \rho^{-2n}.\]
Their common integral characteristic polynomial is
\[(z-1)(z^2+3z+1)(z^2-7z+1)=z^5-5z^4-15z^3+15z^2+5z-1.\]
In particular every translated window-sum sequence satisfies this order-five recurrence. Its constant coefficient is a unit, and all its terms are integral, so the GCD of all translated windows equals the GCD of the first five.

**Odd primes at least seven.** Fix \(p\ge7\), and \(e\ge1\). Work in the unramified quadratic \((\mathbb Z/p^e\mathbb Z)[\alpha]/(\alpha^2-\alpha-1)\); the discriminant five is a unit. The five bases above have distinct reductions modulo \(p\): indeed \(\rho\) has order at least five, because orders one, two, three and four would force respectively \(p\mid5\), the impossible equation \(1=0\), \(p\mid2\), or \(p\mid3\). Thus their Vandermonde matrix on five consecutive indices is invertible modulo \(p^e\). All five Binet coefficients are units modulo \(p\), including the constant coefficients \(6/25\) and \(6\). Consequently \(p^e\) divides every length-\(k\) window sum for either sequence if and only if it divides the five geometric sums \(\sum_{j=1}^{k}\lambda^j\) for \(\lambda\in\{1,\rho,\rho^{-1},\rho^2,\rho^{-2}\}\).

The constant mode imposes \(p^e\mid k\). Since \(\rho-1\) is invertible for \(p\ge7\), the \(\rho\)-sum vanishes if and only if \(\rho^k=1\pmod{p^e}\). This condition also forces vanishing of the remaining nonconstant sums: \(\rho^{\pm k}=\rho^{\pm2k}=1\), and all relevant denominators \(\rho^{\pm1}-1\) and \(\rho^{\pm2}-1\) are units. Therefore the necessary and sufficient condition is
\[p^e\mid k\quad\text{and}\quad\rho^k\equiv1\pmod{p^e}.\]
Reducing the second condition modulo \(p\) gives \(r_p\mid k\). Conversely, if \(r_p\mid k\), then \(\rho^{r_p}=1+p u\) in the unramified integral quadratic algebra. Since the order \(r_p\) divides the order of a finite unit group modulo \(p\), and this group has order prime to \(p\), one has \(p\nmid r_p\). Writing \(k=r_p h\), repeated binomial expansion gives \((1+pu)^h\equiv1\pmod{p^{1+\nu_p(h)}}\). Hence \(\rho^k\equiv1\pmod{p^e}\) for every \(e\le\nu_p(k)\). Thus
\[\nu_p(G_F(k))=\nu_p(G_L(k))=\nu_p(k)\mathbf1_{r_p\mid k}\qquad(p\ge7).\]

**The prime three.** Modulo three, fourth powers are exactly indicators of nonzero residues. For Fibonacci numbers the zero-indicator occurs exactly at indices divisible by four; for Lucas numbers it occurs exactly at indices congruent to two modulo four. If all length-\(k\) windows vanished modulo three, subtraction of successive windows would force \(X_{n+k+1}^4=X_{n+1}^4\pmod3\) for all \(n\ge0\). Its zero positions form a nontrivial residue class modulo four, so this forces \(4\mid k\). As \(k\) is odd, this is impossible. No factor three occurs.

**The prime five.** As \(5\nmid k\), the Fibonacci fourth powers modulo five, which are zero exactly at multiples of five and one otherwise, cannot have \(k\) as a period; hence all windows cannot vanish modulo five. In the Lucas case, \(L_n^4\equiv1\pmod5\) for every \(n\) (its residues repeat \(2,1,3,4\)), so every window is congruent to \(k\not\equiv0\pmod5\). No factor five occurs.

**The prime two.** For both sequences, terms are even precisely when their index is divisible by three. For odd \(k\), fourth powers modulo four therefore mark the indices not divisible by three. If \(3\mid k\), every length-\(k\) interval contains exactly \(2k/3\) odd terms, and since \(k/3\) is odd, each window is exactly two modulo four. Thus the common 2-adic valuation is one. If \(3\nmid k\), the counts of nonmultiples of three in the translated windows vary in parity, so some window is odd and the 2-adic valuation vanishes.

Combining these primewise results establishes both asserted equalities. \(\square\)

## Verification
The standalone Python file `artifacts/verify.py` computes the order \(r_p\) using exact finite-algebra multiplication; for each odd \(k<1200\) with \(5\nmid k\), it independently constructs the first five translated quartic windows for both initial conditions and compares their exact integer GCD with the formula. All 960 comparisons passed. Five windows are exhaustive for each fixed length because of the proved order-five recurrence. The verifier also reports sample orders. No finite experiment is used to assert the unbounded theorem.

## Relationship to prior work
Guyer and Mbirika, arXiv:2104.12262, determine GCDs for consecutive first powers. Mbirika and Spilker, arXiv:2204.12626, determine the squared version and discuss higher powers in their Section 6, Question 6.1, mainly for even window lengths. Their results do not imply the quartic odd-window prime-order factorization. Existing cubic odd-window classifications concern a different characteristic polynomial and do not imply a fourth-power assertion. Standard fourth-power summation identities express individual windows but do not classify the common divisors of *all* translations. The novelty claim is restricted to the formula and its proof under the stated hypotheses.

## Limitations
The restriction \(5\nmid k\) excludes the discriminant prime from the analysis; no claim is made for odd multiples of five or for even window lengths. The formula need not extend to arbitrary generalized Fibonacci initial conditions. Prior publication under an alternative guise, especially a more general recurrence-and-order theorem, cannot be ruled out without exhaustive bibliographic discovery. No independent external mathematical audit has been performed.

## References
Mbirika, aBa, and Jürgen Spilker, “GCD of sums of k consecutive squares of generalized Fibonacci numbers,” arXiv:2204.12626, first posted 2022-04-26, Section 6, Question 6.1; open full text at https://arxiv.org/pdf/2204.12626.

Guyer, Dan, and aBa Mbirika, “GCD of sums of k consecutive Fibonacci, Lucas, and generalized Fibonacci numbers,” arXiv:2104.12262, first posted 2021-04-25; open full text at https://arxiv.org/pdf/2104.12262.
