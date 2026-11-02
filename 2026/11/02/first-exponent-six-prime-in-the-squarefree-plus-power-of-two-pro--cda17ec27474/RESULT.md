# The first exponent-six prime in the squarefree-plus-power-of-two problem

## Finding

For every prime \(p\equiv7\pmod{36}\), let \(a_{\min}(p)\) be the least nonnegative integer \(a\) such that \(p-2^a\) is a positive squarefree integer. The definition is used only for primes for which such an exponent exists.

**Theorem.** Among primes \(p\equiv7\pmod{36}\) with \(p\le10^9\), exactly two have no representation \(p=2^a+m\) with \(0\le a\le5\) and positive squarefree \(m\). They are
\[
189954151\quad\text{and}\quad998649907.
\]
Both have \(a_{\min}(p)=6\). In particular, the least prime in this residue class requiring exponent at least six is exactly \(189954151\).

## Assumptions and scope

A positive integer \(m\) is squarefree when there is no prime \(q\) with \(q^2\mid m\). The theorem concerns only prime arguments \(p\equiv7\pmod{36}\), up to and including \(10^9\), and only the first usable exponent. This is an exhaustive finite classification, not a proof of the unrestricted Erdős representation conjecture.

## Proof

Write \(p=36k+7\), with \(k\ge0\). Since \(p\equiv3\pmod4\), the positive integer \(p-1\) is \(2\pmod4\), and all \(p-2^a\) for \(a\ge1\) are odd. Thus none of the positive remainders for \(a\in\{0,1,2,3,5\}\) has a factor \(4\). Also \(p\equiv7\pmod9\), whereas \(2^a\pmod9\) is respectively \(1,2,4,8,5\) for those five exponents. Hence none has a factor \(9\). But \(2^4=16\equiv7\pmod9\), so every positive \(p-16\) is divisible by \(9\), and exponent \(4\) never works. The exceptional small prime \(p=7\) has \(p-1=6\) squarefree; all other primes in this class are at least \(43\), so the remainders through exponent five are positive.

It remains to determine which primes in the class have a squared factor \(q^2\) dividing each of the five remainders \(p-2^a\), for \(a\in A=\{0,1,2,3,5\}\). Such squared factors necessarily have prime base \(q\ge5\). For each \(q\le\lfloor\sqrt{10^9}\rfloor\) and each \(a\in A\), the congruence
\[
q^2\mid36k+7-2^a
\]
has exactly one solution modulo \(q^2\), because \(\gcd(36,q^2)=1\). Explicitly,
\[
k\equiv(2^a-7)\,36^{-1}\pmod{q^2}.
\]
To ensure the positive remainder actually contains \(q^2\), the sieve marks only indices satisfying \(36k+7-2^a\ge q^2\). Scanning every prime \(5\le q\le\lfloor\sqrt{10^9}\rfloor\) is exhaustive, since a positive nonsquarefree integer at most \(10^9\) has a squared prime divisor with \(q\le\lfloor\sqrt{10^9}\rfloor\).

The standalone exact-integer verifier `verify.py` implements this five-bit arithmetic-progression sieve for every index \(0\le k\le\lfloor(10^9-7)/36\rfloor\). The resulting list of **all integers**, prime or composite, in this progression with all five squared-factor obstructions is precisely
\[
\begin{gathered}
9976579,\ 87018271,\ 189954151,\ 360530683,\ 530060227,\\
861270307,\ 949293907,\ 978131779,\ 998649907.
\end{gathered}
\]
The same verifier uses deterministic trial division by every prime up to \(\lfloor\sqrt{10^9}\rfloor\) to test the primality of each of these nine integers; precisely \(189954151\) and \(998649907\) are prime. Consequently these are exactly the primes in the desired class and range with \(a_{\min}(p)\ge6\), provided the exponent exists.

Finally, both sixth remainders are squarefree, with complete factorizations
\[
189954151-64=3\cdot63318029,
\qquad
998649907-64=3\cdot47\cdot431\cdot16433,
\]
in which each displayed factor is prime and no factor repeats. The same deterministic factorization routine verifies this assertion. Thus both smallest usable exponents equal six, completing the proof.

For an additional direct certificate at the least example, squared-prime obstructions for \(a=0,1,2,3,4,5\) are respectively \(5^2,11^2,29^2,31^2,3^2,47^2\), all dividing \(189954151-2^a\). The corresponding squared-prime obstructions for \(998649907\) at those exponents are \(37^2,11^2,23^2,13^2,3^2,5^2\), respectively.

## Verification

Run `python3 verify.py` with Python 3 (no third-party libraries). The program enumerates \(27{,}777{,}778\) integers in the residue progression through \(10^9\), processes exactly the primes from \(5\) through \(\lfloor\sqrt{10^9}\rfloor\), and uses exact modular inverses, bit masks, trial division, and integer factorization. It asserts both the nine-element complete obstruction set and the two-element prime set, and checks all six failed exponents plus the successful exponent six for each survivor. This is a reproducible complete finite proof when combined with the arithmetic-progression exhaustiveness argument above; the script's printed success line alone is not a substitute for the argument.

## Relationship to prior work

Harman and Paquin (arXiv:2610.07214, first public October 5, 2026; primary MSC 11A67) established the arithmetic reduction and classified all primes in the same class below \(10^8\), none of which required exponent six. Their Section 7 explicitly identifies finding the first such prime beyond that range as a future computational question. Their result alone does not imply the exact first example or the complete \(10^9\) census here.

Hercher (arXiv:2411.01964, first public November 4, 2024; subsequently *Journal of Integer Sequences* 28 (2025), Article 25.3.1) verified representability of all odd integers up to \(2^{50}\), and tabulated least odd integers needing successively higher exponents. The available full treatment gives a broader existence computation, not an exact prime-restricted \(7\pmod{36}\) first-exponent-six list. Thus this result does not claim novelty of the existence of representations under Hercher's bound. A previously unreleased or unindexed specialized table remains a priority risk.

## Limitations

This finite theorem does not show every prime in the residue class has a representation or make claims beyond \(10^9\). Its novelty and value are tied to identifying the exact first prime with least exponent six and completing the natural first \(10^9\) range following the explicit \(10^8\) classification. The computation must be rerun or independently checked before external certification; no independent audit has been performed.

## References

1. Shen Harman and Dana Paquin, *The One-Power Erdős Conjecture for Primes \(p\equiv7\pmod{36}\)*, arXiv:2610.07214v1 (October 5, 2026), https://arxiv.org/html/2610.07214.
2. Christian Hercher, *On the Sum of Squarefree Integers and a Power of Two*, arXiv:2411.01964v1 (November 4, 2024), https://arxiv.org/abs/2411.01964; journal version *Journal of Integer Sequences* 28 (2025), Article 25.3.1, https://cs.uwaterloo.ca/journals/JIS/VOL28/Hercher2/hercher24.html.
3. OEIS A377587, least odd integers requiring higher powers of two, https://oeis.org/A377587.
