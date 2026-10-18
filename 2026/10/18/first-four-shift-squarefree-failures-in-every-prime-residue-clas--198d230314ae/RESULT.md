# First four-shift squarefree failures in every prime residue class modulo \(36\)

## Finding
For each reduced residue class \(r\) modulo \(36\), let \(M(r)\) denote the **least prime** \(p\equiv r\pmod{36}\) such that **none** of the four positive integers \(p-1\), \(p-2\), \(p-4\), and \(p-8\) is squarefree. The complete set of twelve exact minima is:

| \(r\) | \(M(r)\) | \(f(r)\) | \((q_0,q_1,q_2,q_3)\), with \(q_a^2\mid M(r)-2^a\) |
|---:|---:|---:|:---|
| 1 | 280729 | 1 | (2, 41, 5, 7) |
| 5 | 439601 | 1 | (2, 23, 109, 11) |
| 7 | 4851151 | 0 | (5, 409, 7, 53) |
| 11 | 5051 | 1 | (5, 3, 7, 41) |
| 13 | 6421 | 2 | (2, 7, 3, 11) |
| 17 | 6029 | 2 | (2, 7, 5, 3) |
| 19 | 1052083 | 1 | (3, 43, 7, 5) |
| 23 | 6165527 | 0 | (17, 5, 7, 19) |
| 25 | 236329 | 1 | (2, 7, 5, 29) |
| 29 | 6329 | 2 | (2, 3, 5, 7) |
| 31 | 418783 | 1 | (13, 11, 3, 5) |
| 35 | 45179 | 1 | (7, 37, 5, 3) |

Here \(f(r)\) is the number of distinct offsets \(h\in\{1,2,4,8\}\) for which \(p-h\) is **automatically** divisible by \(4\) or \(9\) throughout the class \(p\equiv r\pmod{36}\). It is computed directly from the congruences \(r\equiv h\pmod 4\) or \(r\equiv h\pmod9\); it is included to display the natural local structure. Classes \(7\) and \(23\) have no such forced obstruction and both have minima above four million, whereas classes \(13,17,29\) have two forced offsets and minima below seven thousand. The four-coordinate square-divisor certificates give explicit upper bounds; an **exhaustive prime census with exact square-divisibility predicates** proves every corresponding lower bound, without an assumed upper bound on a hypothetical earlier counterexample other than the stated exhibited witness.

## Assumptions and scope
A positive integer \(n\) is *squarefree* when no prime square divides \(n\); by convention \(1\) is squarefree. The primes \(p\) in the definition must have all four shifted remainders positive, so \(p>8\). This is harmless for the minima: the only primes not exceeding \(8\) in reduced residue classes modulo \(36\) are \(5\) and \(7\), and both admit a squarefree remainder among the first four shifts (respectively \(5-2=3\) and \(7-2=5\)). All statements concern exactly \(a\in\{0,1,2,3\}\), not all exponents.

The modulus \(36\) is the least common multiple of \(4\) and \(9\), which encode the elementary small-prime square obstructions for this four-shift problem. A prime in a reduced class is odd and different from \(3\); its possible forced divisibilities by \(4\) or \(9\) in the four remainders depend only on its class modulo \(36\). These are therefore twelve natural local-arithmetic strata, rather than arbitrary numerical intervals.

## Proof
**1. Exhaustive bound.** Let \(B=6{,}165{,}527\), the largest displayed witness, and \(H=\{1,2,4,8\}\). The included `verify.py` constructs a Boolean prime table for every integer between \(0\) and \(B\), inclusive, using the sieve of Eratosthenes. Every composite \(n\le B\) has a prime factor at most \(\sqrt n\le\sqrt B\), and the sieve crosses out its multiples, beginning at the square of that prime. Consequently its prime table is exact, not heuristic.

**2. Exact squarefree test.** For each prime \(q\le\lfloor\sqrt B\rfloor\), the program marks each multiple of \(q^2\) not exceeding \(B\). A positive integer \(n\le B\) is marked if and only if it is not squarefree: the reverse implication uses the fact that every repeated prime factor of \(n\) has square at most \(n\le B\). The program then scans **every prime \(p\le B\)**, recording the first \(p>8\) in each reduced class for which all four marked predicates \(p-h\), \(h\in H\), are true. It asserts equality with the displayed twelve values. Since a displayed witness occurs at or before \(B\) for every class, the absence of any smaller successful prime proves each unrestricted minimality statement.

**3. Independent arithmetic checks.** Within the same program a second predicate tests whether a positive integer \(n\) is divisible by \(q^2\) for any prime \(q\le\sqrt n\), by integer remainder rather than consulting the precomputed squareful table. A second full prime scan reproduces all twelve minima. For each displayed witness, a separate trial division by **all** integers \(2\le d\le\lfloor\sqrt p\rfloor\) independently confirms primality, and the program constructs four explicit prime-square divisors, reported in the table. These checks are logically bounded and deterministic; they do not extrapolate from finite data to an infinite density claim.

**4. No omitted small case.** A prime \(p\le8\) with a unit residue modulo \(36\) is \(p=5\) or \(p=7\); the squarefree remainders noted above rule out exceptions. Hence the search's restriction to \(p>8\) does not discard a smaller qualifying prime. The enumeration and the twelve upper-bound witnesses establish the theorem.

The arithmetic also explains why a fourfold failure is restrictive: the distinct offsets in \(H\) differ by at most \(7\). For any prime \(q\ge3\), \(q^2\ge9\) cannot divide two different shifted remainders; and for odd \(p\), the factor \(4\) can occur only in \(p-1\) among these remainders. Thus four distinct prime-square witnesses are necessary. This separation does **not**, by itself, give the twelve minima; the exhaustive certificate provides that step.

## Verification
Execute `python3 verify.py` with Python 3 and its standard library only. The program prints twelve rows with the first prime and a four-component square-divisor witness, then ends with `VERIFY_OK; 12 residue-class minima; bound 6165527`. The file `certificate_output.txt` gives the expected exact output. The verification requires neither external packages nor probabilistic primality tests. The sieve and trial predicates are described above so that the finite calculation is transparently connected to the theorem's quantifiers.

## Relationship to prior work
Harman and Paquin's 2026 preprint [1] treats primes congruent to \(7\) modulo \(36\), proves an asymptotic density for failures of the same first four exponents in that class, and describes a computation for primes below \(10^8\). The present result concerns a different **exact first-occurrence invariant simultaneously for all twelve reduced classes**; the cited asymptotic theorem and its abstract do not supply the complete twelve-class minimum table. The possible overlap of the \(r=7\) row with the preprint's numerical data is acknowledged.

Hercher's 2025 paper [2], especially its full Sections 3–4 and Table 3, verifies the existence of squarefree-power-of-two representations for odd integers below \(2^{50}\), with positive exponents \(a\ge1\), and gives first odd integer failures for increasing initial positive-exponent windows. Neither its broad existence conclusion nor its reported table implies the exact minima for **primes in each class modulo \(36\)** with the additional exponent \(a=0\). Sequence A257545 [3] tabulates different consecutive shifts \(p-1,p-2,\ldots,p-k\), where the entry \(5051\) coincides with one table value but the defining conditions differ. No assertion of universal mathematical novelty follows from database absence alone.

## Limitations
The result is an exact, finite computation-backed classification of a natural minimum-prime invariant. It does **not** prove an asymptotic for other congruence classes, classify all exceptional primes, or resolve Erdős' one-power conjecture. The current comparison with [1] had access to its verified abstract and secondary synopsis but **not its complete primary PDF**, so an unobserved appendix table remains a residual originality risk, especially for the \(r=7\) row. The independent correctness test uses separate divisibility logic but shares the enumerated prime list; the correctness argument for that list is the elementary sieve proof supplied above.

## References
1. S. Harman and D. Paquin, *The One-Power Erdős Conjecture for Primes* \(p\equiv7\pmod{36}\), arXiv:2610.07214, first posted 2026-10-05. https://arxiv.org/abs/2610.07214
2. C. Hercher, *On the Sum of a Squarefree Integer and a Power of Two*, Journal of Integer Sequences 28 (2025), Article 25.3.1. https://cs.uwaterloo.ca/journals/JIS/VOL28/Hercher2/hercher24.pdf
3. The On-Line Encyclopedia of Integer Sequences, A257545, *Least prime with consecutive preceding nonsquarefree shifts*. https://oeis.org/A257545
