# A certified \(2.741607\) lower bound for the rough-prime-gap constant

## Finding
Let \(c\) be the nonnegative local singular-series constant of Gafni and Tao for prime gaps containing no integer whose least prime factor is at least the gap length. The exact local contributions through even gap length \(64\) give
\[
\sum_{\substack{4\le h\le64\\ 2\mid h}}\frac{|\Omega_h|}{\prod_{2<p<h}(p-2)}
=\frac{61370211356863231369}{29555095284933631875}.
\]
Consequently the deterministic constant satisfies the unconditional, strict inequality
\[
\boxed{c>2.741607}.
\]
This is a bound on the explicitly defined constant, **not** an unconditional prime-gap counting asymptotic.

## Assumptions and scope
For each even integer \(h\ge4\), let \(P_h=\prod_{p<h}p\), with products taken over primes. Let \(A_h\) consist of residue classes \(b\bmod P_h\) satisfying \(\gcd(b(b+h),P_h)=1\). Let \(\Omega_h\subseteq A_h\) consist of classes such that \(\gcd(b+i,P_h)>1\) for **every** integer \(1\le i<h\). Define
\[
\mathfrak S_2=2\prod_{p>2}\left(1-\frac{1}{(p-1)^2}\right),\qquad
c=\mathfrak S_2\sum_{\substack{h\ge4\\2\mid h}}
\frac{|\Omega_h|}{\prod_{2<p<h}(p-2)}.
\]
The known identity for \(c\) is from the cited primary literature. No conjecture is needed to define it or prove the lower bound, because all summands are nonnegative.

The previously published exact table ends at \(h=36\). The following fourteen counts are exact, computed using CRT dynamic programming and integer arithmetic:

| \(h\) | \(|\Omega_h|\) |
| ---: | ---: |
| 38 | 7381190 |
| 40 | 10176048 |
| 42 | 363563276 |
| 44 | 5319950268 |
| 46 | 3066631938 |
| 48 | 270657148848 |
| 50 | 101307938184 |
| 52 | 25051650260 |
| 54 | 4828555093560 |
| 56 | 952248263928 |
| 58 | 747162295398 |
| 60 | 49562298435088 |
| 62 | 673737239242910 |
| 64 | 870323053429248 |

## Proof
Since \(h\) is even, the endpoint condition modulo \(2\) forces \(b\) odd; every interior **odd** offset is therefore divisible by \(2\). It remains to determine whether at least one interior **even** offset \(i\in\{2,4,\ldots,h-2\}\) survives every odd prime below \(h\).

Represent a subset of these even offsets by a bitmask \(S\), initially containing every such offset. For each odd prime \(p<h\), enumerate exactly the residues \(b_p\in\{0,\ldots,p-1\}\) with \(b_p\not\equiv0,-h\pmod p\). Remove from \(S\) each offset \(i\) for which \(b_p+i\equiv0\pmod p\). A dictionary records the number of residue tuples producing each resulting survivor mask. By induction over processed primes, every dictionary multiplicity counts exactly the corresponding tuples; there are no collisions between different CRT tuples. The Chinese remainder theorem makes these tuples bijective with \(A_h\). Thus the multiplicity of the empty survivor mask after all odd primes \(p<h\) is exactly \(|\Omega_h|\). This proves that the finite enumeration in `certify.py` is exhaustive, with no search cutoff on CRT classes and no floating-point arithmetic.

The executable certificate verifies all 31 values \(h=4,6,\ldots,64\) against the explicitly encoded integers; an independently derived inclusion-exclusion calculation cross-checks every value through \(h=44\). It forms the displayed finite sum with exact reduced rational arithmetic and verifies its numerator and denominator.

For a strictly rational bound on \(\mathfrak S_2\), initialize \(L=2\cdot10^{18}\), and at each odd prime \(p\le10^6\) replace \(L\) with
\[
\left\lfloor L\frac{(p-1)^2-1}{(p-1)^2}\right\rfloor.
\]
All multipliers are positive and less than one, so integer flooring at every stage proves that the truncated product is at least \(L/10^{18}\). The exact calculation yields \(L=1320323721179642234\). For primes \(p>10^6\), use the elementary product inequality and the integral bound
\[
\prod_{p>10^6}\left(1-\frac1{(p-1)^2}\right)
\ge1-\sum_{n\ge10^6}\frac1{n^2}
\ge1-\frac1{999999}=\frac{999998}{999999}.
\]
Hence, using only rational inequalities and positivity of omitted gap contributions,
\[
 c\ge \frac{61370211356863231369}{29555095284933631875}
\cdot\frac{1320323721179642234}{10^{18}}
\cdot\frac{999998}{999999}
=\frac{1841554176617798769290824758236675208498257}{671706039314507885031093750000000000000000}
>\frac{2741607}{10^6}.
\]
Every inequality is rigorous, irrespective of the uncomputed infinite tail.

## Verification
Run `python3 certify.py` using Python 3.9 or later (standard library only). The program recomputes all 31 local counts with exact CRT arithmetic; independently recomputes the first 21 counts through \(h=44\) with inclusion-exclusion; verifies the exact 64-cutoff rational sum and floor-certified prime-product bound; and prints `SUCCESS: c > 2.741607`. Output and finite enumerations are deterministic. The proof above establishes completeness of the finite-state recurrence; the code supplies its actual evaluated integers.

## Relationship to prior work
Gafni and Tao, *Rough numbers between consecutive primes* (2025), introduce the constant and give exact small-gap data through \(h=18\). Uğurdoğan, *Multiplicity constants for rough numbers in prime gaps* (6 October 2026), gives a corrected exact local table through \(h=36\), establishes the finite-sum lower value \(2.7413688\ldots\), and estimates the larger-gap contribution by Monte Carlo, suggesting \(c\approx2.7416\) but not certifying it. The present exact finite enumeration extends the tabulated range to \(64\) and rigorously certifies the stronger threshold \(2.741607\), without identifying the infinite sum exactly.

## Limitations
No upper bound as close as \(2.741607\), no exact value of \(c\), and no asymptotic formula for the number of exceptional prime gaps are proved here. The bound comes entirely from a finite lower partial sum plus a rigorous Euler-product lower factor. Existence or frequency of prime gaps represented by individual CRT residue patterns remains governed by distinct prime-tuples questions. Independent audit has not been performed.

## References
1. A. Gafni and T. Tao, *Rough numbers between consecutive primes*, arXiv:2508.06463v1, 8 August 2025, Section 4 and Table 1.
2. B. Uğurdoğan, *Multiplicity constants for rough numbers in prime gaps*, arXiv:2610.10582v1, 6 October 2026, Remark 1.3 and Section 4.1, Table 1.
