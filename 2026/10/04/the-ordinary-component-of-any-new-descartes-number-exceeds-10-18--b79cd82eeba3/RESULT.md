# The ordinary component of any new Descartes number exceeds \(10^{18}\)

## Finding
A positive Descartes number in the sense relevant here has the form
\[
D=pq,
\]
where \(p\) is an odd composite number treated as a pseudo-prime, \(q\) is an odd positive integer, and
\[
\sigma(q)(p+1)=2pq.
\]
Tóth proved in 2021 that, apart from Descartes' classical example, the ordinary component satisfies \(q>10^{12}\).

The bound can be strengthened to
\[
q>10^{18}.
\]
More precisely, among all \(q\le10^{18}\) compatible with an odd pseudo-prime parameter, the only nontrivial solution of the defining divisor-sum equation is
\[
q=9018009=3003^2,
\qquad
p=22021=19^2\cdot61,
\]
which is exactly Descartes' classical example
\[
D=198585576189.
\]

## Assumptions and scope
The result concerns positive Descartes numbers of the form used by Tóth: one positive odd composite factor \(p\) is treated as if prime, while \(q\) contributes its ordinary divisor sum. It does not classify the broader signed or repeated-base spoof factorizations studied in later generalizations.

No claim is made beyond the finite cutoff \(10^{18}\), and no claim is made that another positive Descartes number exists.

## Proof
Suppose
\[
\sigma(q)(p+1)=2pq
\]
with \(p\) and \(q\) odd. The right-hand side has exactly one factor of \(2\). Since \(p+1\) is even, it follows that
\[
\nu_2(p+1)=1
\quad\text{and}\quad
\nu_2(\sigma(q))=0.
\]
Thus \(\sigma(q)\) is odd. For an odd integer \(q\), the divisor sum \(\sigma(q)\) is odd if and only if every exponent in the prime factorization of \(q\) is even. Hence
\[
q=m^2
\]
for an odd positive integer \(m\).

If \(q\le10^{18}\), then \(m\le10^9\). Therefore it is enough to inspect the one-dimensional finite range of odd roots
\[
1\le m\le10^9.
\]
For \(q=m^2\), put
\[
d=2q-\sigma(q).
\]
Tóth's defining relation
\[
\frac{2q}{\sigma(q)}-1=\frac1p
\]
is equivalent to
\[
d>0,
\qquad
d\mid\sigma(q),
\qquad
p=\frac{\sigma(q)}d.
\]

The accompanying exact segmented sieve factors every odd \(m\le10^9\). If
\[
m=\prod_i r_i^{e_i},
\]
it computes
\[
\sigma(m^2)=\prod_i\left(1+r_i+\cdots+r_i^{2e_i}\right)
\]
using integer arithmetic, then tests the three conditions above.

Across the complete range there are only two square members of Tóth's set:
\[
(q,p)=(1,1)
\]
and
\[
(q,p)=(9018009,22021).
\]
The first is trivial. The second has
\[
22021=19^2\cdot61
\]
and produces Descartes' known number. Hence no different positive Descartes number can have \(q\le10^{18}\).

## Verification
Compile `verify.cpp` with a C++17 compiler and run the resulting executable. The program sieves the complete odd-root interval \(1\le m\le10^9\) in fixed-size segments, so it does not rely on random sampling or a stored candidate list.

The sieve uses all primes through \(31623>\sqrt{10^9}\). For each root it reconstructs the exact prime exponents and computes \(\sigma(m^2)\) in 128-bit unsigned integer arithmetic. It then tests positivity of \(2m^2-\sigma(m^2)\), exact divisibility, and the resulting pseudo-prime parameter.

A successful replay prints `VERIFY_OK` and exactly the two pairs
\[
(1,1),
\qquad
(9018009,22021).
\]
The file `scan_output.txt` contains the replay output generated from the packaged source.

## Relationship to prior work
Tóth's 2021 paper introduced the computational set used here and exhaustively searched odd \(q\) through \(10^{12}\), obtaining the published lower bound \(q>10^{12}\) for every non-Descartes example.

A public 2023 computation on Mathematics Stack Exchange observed the square restriction for odd deficient-perfect cases and reported no second odd example through \(10^{16}\). That is the closest located numerical precursor. The present computation extends that public cutoff by a factor of \(100\), and Tóth's peer-reviewed cutoff by a factor of \(10^6\).

The 2020/2022 work on odd spoof perfect factorizations studies a broader algebraic notion, including signed and nonclassical factorizations. Its stated classification by number of bases does not give a larger lower bound for the positive ordinary component \(q\) in Tóth's setting.

Current OEIS entries for the relevant deficient-perfect sequence record the square property and Descartes' \(q=9018009\), but do not state a verified \(10^{18}\) exclusion range. Exact web and semantic-index searches for a \(10^{18}\) Descartes-component bound found no covering result.

## Limitations
This is a finite verification, not a proof that Descartes' example is unique. The conclusion stops at the exact cutoff \(q=10^{18}\).

The search concerns positive Descartes numbers with one odd composite pseudo-prime factor. It does not apply to signed spoof factorizations, spoof multiperfect numbers, or other generalized notions.

Search non-detection is not a proof of novelty. The principal residual originality risk is an unindexed computation exceeding the located public \(10^{16}\) range.

## References
1. László Tóth, “On the Density of Spoof Odd Perfect Numbers,” arXiv:2101.09718v1, first posted 24 January 2021; *Computational Methods in Science and Technology* 27 (2021), 25–28.
2. BYU Computational Number Theory Group, “Odd, spoof perfect factorizations,” arXiv:2006.10697v1, first posted 18 June 2020; *Journal of Number Theory* 234 (2022), 31–47.
3. OEIS A271816, deficient-perfect numbers.
4. Mathematics Stack Exchange, “Are all elements in this sequence even?”, public discussion and computation posted 1 February 2023.
