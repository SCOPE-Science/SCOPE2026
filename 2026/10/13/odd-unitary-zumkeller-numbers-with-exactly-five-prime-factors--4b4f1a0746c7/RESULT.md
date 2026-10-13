# Odd unitary Zumkeller numbers with exactly five prime factors
## Finding
Let \(n\) be odd and have exactly five distinct prime factors. Then \(n\) is unitary Zumkeller if and only if it belongs to one of these families:

\[
3\cdot5\cdot7\cdot r\cdot s,
\]
where \(r=11\) and \(s\) is prime with \(13\le s\le383\); or \(r=13\) and \(s\) is prime with \(17\le s\le61\); or
\[
(r,s)\in\{(17,19),(17,23),(17,29),(19,23)\};
\]
and the three nonsquarefree cases
\[
3\cdot5\cdot7\cdot11\cdot s^2,\qquad s\in\{13,17,19\}.
\]
There are exactly \(90\) such integers. As a corollary, every odd unitary Zumkeller number has at least five distinct prime factors, and the least one is
\[
15015=3\cdot5\cdot7\cdot11\cdot13.
\]

## Assumptions and scope
A divisor \(d\mid n\) is unitary when \(\gcd(d,n/d)=1\). Write \(\sigma^*(n)\) for the sum of unitary divisors. An integer is unitary Zumkeller when its unitary divisors can be split into two disjoint subsets having equal sum. The theorem concerns all odd positive integers having exactly five distinct prime divisors, with arbitrary positive exponents.

## Proof
Suppose
\[
n=p_1^{a_1}p_2^{a_2}p_3^{a_3}p_4^{a_4}p_5^{a_5},
\qquad 3\le p_1<\cdots<p_5,
\]
with every \(a_i\ge1\). In an equal-sum partition, the side containing \(n\) has sum \(\sigma^*(n)/2\), so necessarily \(\sigma^*(n)\ge2n\). Since
\[
\frac{\sigma^*(n)}n=\prod_{i=1}^5\left(1+\frac1{p_i^{a_i}}\right),
\]
replacing any exponent by \(1\) can only increase this ratio.

The five smallest possible primes show successively that \(p_1=3\), \(p_2=5\), and \(p_3=7\), because
\[
\frac65\frac87\frac1211\frac1413\frac1817=\frac{20736}{12155}<2,
\]
\[
\frac43\frac87\frac1211\frac1413\frac1817=\frac{4608}{2431}<2,
\]
and
\[
\frac43\frac65\frac1211\frac1413\frac1817=\frac{24192}{12155}<2.
\]
Put \(r=p_4\), \(s=p_5\). With all exponents temporarily set to \(1\), the necessary abundancy inequality becomes
\[
\frac6435\frac2019\frac2019\ge2,
\]
equivalently
\[
32(r+s+1)\ge3rs,
\qquad
s\le\frac{32(r+1)}{3r-32}.
\]
Since \(s>r\), this forces \(r\in\{11,13,17,19\}\). Substitution yields precisely
\[
\begin{array}{c|c}
r & s\\ \hline
11 & 13\le s\le383\text{ prime}\\
13 & 17\le s\le61\text{ prime}\\
17 & s\in\{19,23,29\}\\
19 & s=23.
\end{array}
\]
Thus there are \(87\) possible squarefree supports.

No exponent among \(3,5,7,11\) can exceed \(1\): even on the maximal support \(3,5,7,11,13\), squaring each of these four prime powers gives respective upper bounds
\[
\frac{256}{143},\quad\frac{512}{275},\quad\frac{1920}{1001},\quad\frac{15616}{7865},
\]
all below \(2\). If \(r\ge13\) and the exponent of \(s\) is at least \(2\), the maximal case already satisfies
\[
\frac43\frac65\frac87\frac{14}{13}\frac{290}{289}=\frac{7424}{3757}<2.
\]
Hence a repeated fifth prime requires \(r=11\). There the first four factors contribute \(768/385\), so
\[
\frac{768}{385}\left(1+\frac1{s^{a_5}}\right)\ge2
\]
forces \(s^{a_5}\le384\). Since \(s\ge13\), the only repeated-prime possibilities are \(a_5=2\) and \(s\in\{13,17,19\}\). This proves that the displayed \(90\) candidates are exhaustive.

It remains to prove that all \(90\) candidates really are unitary Zumkeller. Put
\[
\Delta(n)=\frac{\sigma^*(n)}2-n.
\]
The equal-partition condition is equivalent to expressing \(\Delta(n)\) as a sum of distinct proper unitary divisors: adjoining \(n\) to that subset gives one half of all unitary divisors, and the complement gives the other half. The file `witnesses.json` contains such an exact subset for each of the \(90\) candidates, while `verify.py` regenerates every candidate, checks every listed divisor is unitary and proper, and checks its sum is exactly \(\Delta(n)\). This is a finite exhaustive certificate after the preceding bound-free reduction.

Finally, an odd integer with at most four distinct prime factors has
\[
\frac{\sigma^*(n)}n\le\frac43\frac65\frac87\frac{12}{11}=\frac{768}{385}<2,
\]
so no such integer can be unitary Zumkeller. For \(15015\), the certificate gives \(\sigma^*(15015)=32256\) and \(\Delta(15015)=1113\), establishing the sharp least case.

## Verification
Run `python verify.py` in the directory containing `verify.py` and `witnesses.json`. The expected terminal line is `VERIFY_OK candidates=90 witnesses=90 least=15015`. The verifier uses exact integer and rational arithmetic; no numerical tolerance is involved. The universal part of the theorem is the symbolic support-and-exponent reduction above, while the finite certificate supplies sufficiency for the resulting \(90\) candidates.

## Relationship to prior work
Das defines and studies unitary Zumkeller numbers, proves general necessary criteria and low-support results, and explicitly calls for investigation of forms with several prime-power factors. The checked paper does not state the odd five-prime-support classification above or the sharp least-odd result. OEIS A290466 records the object and initial examples but does not provide this classification. A published database result classifying even unitary Zumkeller numbers with exactly three distinct prime factors concerns a disjoint parity/support slice and does not imply this theorem.

## Limitations
The theorem classifies only the exact five-distinct-prime odd stratum. It does not classify odd unitary Zumkeller numbers with six or more distinct prime factors, nor does it classify even cases beyond prior work. Originality was checked against the focal paper, OEIS A290466, targeted database searches for equivalent formulations, and the closest published three-prime-support classification; obscure or differently phrased literature remains a residual risk.

## References
1. B. Das, “On unitary Zumkeller numbers,” *Notes on Number Theory and Discrete Mathematics* 30(2) (2024), 436–442, DOI: 10.7546/nntdm.2024.30.2.436-442.
2. OEIS Foundation Inc., A290466, “Unitary Zumkeller numbers,” first public author date 2017-08-03.
3. published-finding corpus record `2026/10/4/SCOPE-three-prime-support-classification-of-even-unitary-zumkeller-num--cd908a294237`, “Three-prime-support classification of even unitary Zumkeller numbers.”
