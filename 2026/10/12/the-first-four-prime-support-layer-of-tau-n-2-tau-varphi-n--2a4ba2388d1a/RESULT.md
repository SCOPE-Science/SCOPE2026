# The first four-prime-support layer of \(\tau(n^2)=\tau(\varphi(n))\)

## Finding
Write \(\omega(n)\) for the number of distinct prime divisors, \(\tau(n)\) for the number of positive divisors, and \(\varphi(n)\) for Euler's totient function. Consider
\[
\mathcal S_4=\{n\ge 2:\omega(n)=4,\ \tau(n^2)=\tau(\varphi(n))\}.
\]
The **least member** of \(\mathcal S_4\), without a squarefreeness assumption, is
\[
\boxed{\min \mathcal S_4=75361=11\cdot13\cdot17\cdot31.}
\]
Among the *squarefree* members of \(\mathcal S_4\), the least possible totient is
\[
\boxed{\min\{\varphi(n):n\in\mathcal S_4,\ n\text{ squarefree}\}=57600=2^8 3^2 5^2,}
\]
and **exactly 37** squarefree four-prime-support integers attain that totient. They are completely listed, with their prime factors, in `minimal_fiber.csv`. The least is \(75361\), followed by \(79849\) and \(82615\). These are connected assertions about the first four-prime-support entry of the same Diophantine equation; no classification of the entire unbounded four-prime-support locus is asserted.

## Assumptions and scope
Every integer under consideration is positive. The least-member statement concerns all \(n\) with exactly four **distinct** prime factors, including nonsquarefree integers. The minimal-totient and 37-element statements concern precisely the squarefree integers with four distinct prime factors. All computations are integer-exact; no conjecture about the distribution of primes is assumed. The natural finite search ceiling \(75361\) in the least-member certificate comes from the explicit qualifying witness, rather than a conjectural upper bound.

## Proof
**1. The totient floor for squarefree four-prime solutions.** If \(n\) is squarefree and \(\omega(n)=4\), then \(\tau(n^2)=3^4=81\). Its totient is the product of the four factors \(p-1\), one for each prime dividing \(n\). At most one such prime is \(2\); the other at least three are odd. Consequently \(\nu_2(\varphi(n))\ge 3\).

Suppose \(\tau(\varphi(n))=81=3^4\). Writing the prime-power exponents of \(\varphi(n)\) as positive integers, the possibilities are the multiplicative partitions of \(81\): the exponent patterns \((80)\), \((26,2)\), \((8,8)\), \((8,2,2)\), and \((2,2,2,2)\). Because the exponent of \(2\) in \(\varphi(n)\) is at least \(3\), the last pattern is impossible; that exponent must be \(8\), \(26\), or \(80\). With distinct odd prime bases of at least \(3\) and \(5\), the least integer among the remaining forms is \(2^8 3^2 5^2=57600\). Specifically, the other lower bounds are \(2^8 3^8\), \(2^{26}3^2\), and \(2^{80}\); all exceed \(57600\). This establishes the lower bound for every squarefree member without an integer-size cutoff.

**2. Exhaustion at the sharp floor.** Set \(D=57600\). If squarefree \(n=p_1p_2p_3p_4\), with \(p_1<p_2<p_3<p_4\) prime, has \(\varphi(n)=D\), then \(p_i-1\mid D\) for every \(i\) and
\[
\prod_{i=1}^4(p_i-1)=D.
\]
Conversely, any four strictly increasing primes satisfying this product give a squarefree \(n\) with \(\varphi(n)=D\), and hence \(\tau(n^2)=81=\tau(D)\). The finite divisor set \(\{d+1:d\mid D,\ d+1\text{ prime}\}\) has exactly \(33\) elements. The exact ordered search in `verify.py` checks every increasing four-element tuple, pruning only when \(p_i-1\) does not divide the remaining factor of \(D\). It finds exactly \(37\) tuples and verifies their primality and totients. Their least product is \(11\cdot13\cdot17\cdot31=75361\), which realizes the lower bound for \(\varphi(n)\). The complete 37-row certificate is `minimal_fiber.csv`.

**3. Extending the least-member conclusion to nonsquarefree integers.** Any four-distinct-prime solution \(n<75361\) can be checked exhaustively: there are exactly \(11386\) integers in this finite range with \(\omega(n)=4\). The deterministic smallest-prime-factor sieve in `verify.py` factors **each one**, computes \(\prod_{p^e\parallel n}(2e+1)=\tau(n^2)\), computes \(\varphi(n)=\prod_{p^e\parallel n}p^{e-1}(p-1)\), factors that totient, and compares its exact divisor count. There are **zero** equalities. This is a finite, fully exhaustive certificate of the global first-entry bound: any counterexample to the asserted minimum would be an integer below the exhibited witness and would therefore be included in the check. At the witness, \(\varphi(75361)=57600\) and \(\tau(75361^2)=81=\tau(57600)\).

## Verification
Run `python3 verify.py --csv minimal_fiber.csv` with Python 3 (standard library only). It deterministically reproduces the 37-element table, checks all prime candidates by trial division up to their square roots, and proves the bounded least-member search complete using exact prime factorizations. `verification_output.txt` contains the expected deterministic output, including 33 candidate primes, 37 minimum-totient solutions, and 11386 four-support integers eliminated below the minimum. A supplementary exact factorization enumeration reproduced the 37 tuples. The symbolic lower bound in Step 1, not the finite scan, proves that no squarefree qualifying four-support integer has a smaller totient.

## Relationship to prior work
Amroune, Bellaouar, and Boudaoud study the same equality and give structural families with at most three distinct prime factors; their Section 5 also supplies certain larger-support examples. Their paper does not present the least four-support member or the complete minimal-totient four-squarefree fiber. A separate published divisor parametrization covers an odd two-prime branch, whose hypotheses exclude the four-prime case. General inverse-totient routines can enumerate preimages of a *specified* totient, but they do not establish the equation-specific sharp lower totient, the four-support first entry, or the reported 37-element fiber without additional comparison and computation. The number \(75361\) and its totient are separately recorded in general integer factorizations; no novelty is claimed for those isolated arithmetic values.

## Limitations
The result does **not** classify all solutions with four distinct prime divisors, nor establish infinitude for that class. The 37-element count is for the first allowable **totient value**, not for the entire unbounded solution set. Exhaustion below \(75361\) is a finite proof of minimality, not a theorem asserting all solutions are below any bound. Existing inverse-totient algorithms may make the finite fiber independently reproducible; the mathematical value claimed here is the exact, motivated boundary and its equation-specific support restriction. An unindexed treatment of the same extremal fiber remains a bibliographic risk.

## References
1. Z. Amroune, D. Bellaouar and A. Boudaoud, *A class of solutions of the equation* \(d(n^2)=d(\varphi(n))\), *Notes on Number Theory and Discrete Mathematics* **29** (2023), 284–309. DOI: 10.7546/nntdm.2023.29.2.284-309. Public online-first date: 2023-05-02. Full text: https://nntdm.net/papers/nntdm-29/NNTDM-29-2-284-309.pdf.
2. *Divisor parametrization of the odd two-prime branch of* \(\tau(n^2)=\tau(\varphi(n))\), publicly indexed research record: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-divisor-parametrization-of-the-odd-two-prime-branch-of-tau-n-2-t--3dbd11634966.
3. S. Yang, *EulerPhiInverse*, Wolfram Function Repository, https://resources.wolframcloud.com/FunctionRepository/resources/EulerPhiInverse/ (general inverse-totient enumeration, not the asserted four-support classification).
4. OEIS A000005, divisor-counting function, https://oeis.org/A000005.
