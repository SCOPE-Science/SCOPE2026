# The sharp seven-prime-support margin in the finite Robin inequality

## Finding

For every integer \(n>5040\) with \(\omega(n)=7\), the gap \(\Delta_7(n)=e^\gamma\sum_{j=0}^{7}(\ln\ln\ln n)^j/j!-\sigma(n)/n\) has a unique global minimum at \(n=367567200=2^5\cdot3^3\cdot5^2\cdot7\cdot11\cdot13\cdot17\), and \(0.1690<\Delta_7(n)<0.1691\) there.

Here \(\sigma(n)\) is the sum of positive divisors, \(\omega(n)\) is the number of distinct prime factors, \(\gamma\) is Euler's constant, and all logarithms are natural. Write \(P_7(t)=\sum_{j=0}^{7}t^j/j!\) and \(C_7(n)=e^\gamma P_7(\ln\ln\ln n)\); the gap is \(\Delta_7(n)=C_7(n)-\sigma(n)/n\).

## Assumptions and scope

The domain is all integers \(n>5040\) with exactly seven distinct prime factors. No Riemann-hypothesis assumption is used. Since \(n>5040\), the triple logarithm is defined and positive. The result is a sharp minimum for this fixed-support layer only; it is not a proof of Robin's inequality for all integers and does not imply the Riemann hypothesis.

## Proof

Let \(q_1,\ldots,q_7=(2,3,5,7,11,13,17)\). If \(n=\prod_{i=1}^7 p_i^{a_i}\), where \(p_1<\cdots<p_7\), define \(n_* = \prod_{i=1}^7 q_i^{a_i}\). Then \(n_*\le n\), and each factor \(1+p_i^{-1}+\cdots+p_i^{-a_i}\) is no larger than its counterpart with \(q_i\). Thus \(\sigma(n_*)/n_*\ge\sigma(n)/n\). The function \(C_7\) is strictly increasing for \(n>5040\), so if the support is not the first seven primes then \(\Delta_7(n_*)<\Delta_7(n)\). It is enough to minimize over exponent tuples on these seven primes.

For every integer with seven distinct prime factors,
\[
\frac{\sigma(n)}{n}<\prod_{q\in\{2,3,5,7,11,13,17\}}\frac{q}{q-1}=\frac{17017}{3072}.
\]
The interval checker proves
\[
C_7(52{,}000{,}000{,}000)>5.7095380290666298>\frac{10960297}{1920000}=\frac{17017}{3072}+0.1691.
\]
Since \(C_7\) is increasing, every \(n\ge52{,}000{,}000{,}000\) has \(\Delta_7(n)>0.1691\).

For smaller candidates, the support reduction leaves the finite set of tuples \((a_1,\ldots,a_7)\in\mathbb Z_{\ge1}^7\) with \(\prod q_i^{a_i}\le52{,}000{,}000{,}000\). The checker enumerates all 2,596 such tuples. It computes \(\sigma(n)/n\) as an exact rational number and encloses the logarithms, exponential, and gap with outward-rounded decimal intervals. The Euler constant is enclosed using the Euler--Maclaurin bounds
\[
H_N-\ln N-\frac1{2N}+\frac1{12N^2}-\frac1{120N^4}<\gamma<H_N-\ln N-\frac1{2N}+\frac1{12N^2},\qquad N=10000,
\]
where \(H_N=\sum_{k=1}^N1/k\). The resulting interval for the candidate gap is contained in \((0.1690,0.1691)\), and each of the other 2,595 tuples has gap strictly greater than \(0.1691\). These comparisons establish uniqueness and exclude the infinite tail by the preceding bound.

At the minimizer, the factorization is \(2^5\cdot3^3\cdot5^2\cdot7\cdot11\cdot13\cdot17\), and the exact divisor ratio is \(\sigma(n)/n=62496/12155\).

## Verification

The standalone artifact `verify_gap.py` uses only the Python standard library (`decimal`, `fractions`, and `math`). It prints `PASS`, confirms 2,596 exponent tuples and 2,595 nonminimizers, and outputs the certified interval bounds used above. Decimal logarithm and exponential values are widened by one representable unit at 80-digit precision; rational divisor ratios and the Euler--Maclaurin constants are rounded outwards. `gap_certificate.txt` records the actual run output. The certificate verifies the finite search and cutoff inequalities, not any statement about all prime-support sizes other than seven.

## Relationship to prior work

Mishra and Sarkar introduce the same truncated inequality and prove it for \(\omega(n)\le6\); they also describe finite candidate checks for hypothetical minimal counterexamples with \(7\le\omega(n)\le20\). Their paper establishes positivity in the relevant layer but does not state the exact minimum gap or identify the unique minimizer of \(\Delta_7\). The present claim is the quantitative extremal refinement, not a new proof of the inequality's positivity. The integer \(367567200\) is already listed as a colossally abundant number; its factorization alone is not claimed as new.

## Limitations

The result is specific to the seven-prime-support layer and the stated truncation. The finite computation is independently reproducible with the included script, but an external audit has not been performed. The source paper references a separate Mathematica notebook for its candidate checks; that notebook was not retrieved, so a residual overlap risk remains if it contains an unreported table of exact gap minima.

## References

1. C. Mishra and R. Sarkar, “A finite arithmetic form of Robin's inequality and its equivalence to the Riemann hypothesis,” arXiv:2609.26787v1, submitted 22 September 2026. https://arxiv.org/abs/2609.26787
2. OEIS Foundation, “A004490: Colossally abundant numbers,” listing \(367567200\). https://oeis.org/A004490
