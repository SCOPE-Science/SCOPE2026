# A digit-theoretic classification of the binomial-GCD minimum at six times a prime

## Finding
For every integer \(n\ge4\), let
\[
f(n)=\min_{2\le k\le \lfloor n/2\rfloor}\gcd\!\left(n,{n\choose k}\right).
\]
For a prime \(p\ge7\), let \(E_3(p)\) mean that every digit of the usual base-three expansion of \(p\) lies in \(\{0,1\}\), and let \(E_2(p)\) mean that no two consecutive digits of the usual base-two expansion of \(p\) are both one. Then
\[
 f(6p)=\begin{cases}
 2,&E_3(p),\\
 3,&\neg E_3(p)\ \text{and}\ E_2(p),\\
 6,&\neg E_3(p)\ \text{and}\ \neg E_2(p).
 \end{cases}
\]
The excluded prime \(p=5\) satisfies \(f(30)=6\). Examples of the three cases are \(f(78)=2\), \(f(102)=3\), and \(f(42)=6\), corresponding to primes \(13,17,7\). Furthermore, with \(\varphi=(1+\sqrt5)/2\) and \(\alpha=\log_2\varphi<1\),
\[
 \#\{p\le X:\ p\text{ prime},\ p\ge7,\ f(6p)\ne6\}=O(X^{\alpha}).
\]
In particular, the value six occurs for a relative density-one set of primes. The primes in the value-two case number \(O(X^{\log_3 2})\) up to \(X\).

## Assumptions and scope
The minimization is over integers \(k\) with \(2\le k\le3p\). All congruences are over ordinary integers; \(p\) denotes a prime greater than three, and the three-case theorem assumes \(p\ge7\) to avoid the exceptional factor \(p\mid\binom63\) at \(p=5\). The assertion is a complete classification of this fixed two-small-prime, three-prime-support family and makes no claim for arbitrary \(n\).

## Proof
**Digit divisibility lemma.** Lucas's theorem says that for prime \(\ell\), \(\binom nk\not\equiv0\pmod\ell\) exactly when each base-\(\ell\) digit of \(k\) is at most the corresponding digit of \(n\). Therefore, if \(\ell\mid n\) and \(\ell\nmid\binom nk\), then \(\ell\mid k\), since the units digit of \(n\) is zero.

**A uniform upper bound.** Choose \(k=p\). Modulo \(p\), Lucas's theorem gives \(\binom{6p}{p}\equiv\binom61=6\not\equiv0\pmod p\) for \(p\ge7\). Both two and three divide the binomial coefficient by the digit divisibility lemma, since neither divides \(p\). Because \(6p\) is squarefree, this proves \(\gcd(6p,\binom{6p}{p})=6\) and hence \(f(6p)\le6\).

**Exclusion of one.** If the gcd at some \(k\) were one, the digit divisibility lemma with \(\ell=2,3,p\) would force \(6p\mid k\), impossible for \(2\le k\le3p\).

**The value two.** If the gcd is two, both three and \(p\) do not divide the binomial coefficient. The lemma forces \(3p\mid k\), so \(k=3p\). At that index the central binomial coefficient \(\binom{6p}{3p}\) is even. Lucas's theorem modulo \(p\) gives \(\binom{6p}{3p}\equiv\binom63=20\not\equiv0\pmod p\), for all primes \(p\ge7\). For the remaining prime, use the identity that \(\binom{6p}{3p}\) is nonzero modulo three precisely when \(\binom{2p}{p}\) is nonzero modulo three: multiplication by three simply appends a zero digit to both inputs in base three. By the base-three carry criterion (Kummer's theorem), \(\binom{2p}{p}\) is nonzero modulo three exactly when adding \(p+p\) creates no carry, i.e. every base-three digit of \(p\) is zero or one. Thus a gcd equal to two occurs if and only if \(E_3(p)\).

**The value three.** If the gcd is three, both two and \(p\) do not divide the coefficient. The lemma forces \(2p\mid k\), so \(k=2p\). Lucas modulo \(p\) gives \(\binom{6p}{2p}\equiv\binom62=15\not\equiv0\pmod p\), for \(p\ge7\). Three divides this binomial coefficient because \(3\mid6p\) but \(3\nmid2p\). Applying Lucas modulo two, the parity of \(\binom{6p}{2p}\) equals that of \(\binom{3p}{p}\), since both inputs were doubled. Kummer's theorem says that this latter coefficient is odd exactly when adding \(p+2p\) in base two has no carries. This is equivalent to \(p\mathbin{\&}(2p)=0\), equivalently no adjacent ones in the binary expansion of \(p\), which is \(E_2(p)\). Hence a gcd three occurs precisely when \(E_2(p)\).

The only divisors of the squarefree number \(6p\) less than six are one, two, and three; one is impossible, and two and three occur by the two digit conditions. Their minimum and the universal witness of value six give the claimed trichotomy. The \(p=5\) case follows directly by testing \(2\le k\le15\), as independently implemented in `verify.py`.

**Density bound.** Among binary strings of length at most \(L\), those without consecutive ones number at most a constant times \(\varphi^L\) (the Fibonacci recurrence). Thus integers below \(X\) satisfying \(E_2\) number \(O(X^{\log_2\varphi})\). Likewise at most \(2^L\) base-three strings of length \(L\) avoid digit two, so integers below \(X\) satisfying \(E_3\) number \(O(X^{\log_3 2})\). Exceptional primes are a subset of this union; the first bound dominates, giving the power-saving estimate. Dividing by \(\pi(X)\sim X/\log X\) proves the relative density-one claim.

## Verification
Run `python3 verify.py`. The verifier independently calculates every integer binomial coefficient in the defining minimum for all 34 primes from five through 151, and separately computes the prime-factor support of these gcds using base-digit Lucas tests for all 165 primes from seven through 997. It checks the special value at 30. The output is `VERIFY_OK` with counts and representative primes. These finite tests corroborate, but do not replace, the unrestricted proof above.

## Relationship to prior work
Erdős and Szekeres introduced the minimum-gcd problem and recorded \(f(30)=6\) in 1978; their work provides the motivating problem, not the full six-times-prime digit classification. Bergman's 2008 paper investigates common divisors of multinomial and binomial coefficients, especially the gcd of two distinct interior binomial coefficients; that different minimization does not imply the present three-way formula. The open problem is cataloged as Erdős Problem 700. The proof uses classical Lucas and Kummer criteria, which are not new. A literature search found no existing theorem with this exact implication, but elementary equivalent reformulations or unlocated results remain a genuine possibility.

## Limitations
No assertion is made about primes \(p\in\{2,3\}\), about numbers outside the family \(6p\), or about infinitude of primes in either exceptional digit class. The bound \(O(X^{\alpha})\) is an elementary *upper* bound, not an asymptotic count of either exceptional prime set. Novelty has been checked against identified relevant sources but not independently certified; potential prior derivations from Lucas/Kummer theory are a residual literature risk.

## References
1. P. Erdős and G. Szekeres, *Some Number Theoretic Problems on Binomial Coefficients*, Australian Mathematical Society Gazette **5** (1978), 97–99, publicly available at https://www.renyi.hu/~p_erdos/1978-46.pdf. The precise original 1978 release day was not verified.
2. George M. Bergman, *On common divisors of multinomial coefficients*, arXiv:0806.0607v1, first posted June 3, 2008, https://arxiv.org/abs/0806.0607.
3. *Erdős Problem 700*, https://www.erdosproblems.com/700.
4. E. Lucas, theorem on binomial coefficients modulo primes (classical); E. Kummer, theorem on prime valuations and base-\(p\) carries (classical).
