# Binary-exponent rigidity for bi-unitary harmonic two-prime squares

## Finding
For **every pair of distinct primes** \(p,q\) and **every integer** \(t\ge2\), the perfect square
\[
N=p^2q^{2^t}
\]
is **not** bi-unitary harmonic. Equivalently,
\[
\sigma^{**}\bigl(p^2q^{2^t}\bigr)\nmid
p^2q^{2^t}\tau^{**}\bigl(p^2q^{2^t}\bigr).
\]
Here \(\sigma^{**}\) and \(\tau^{**}\) are respectively the sum and count of bi-unitary divisors. The conclusion is unconditional in both primes and in \(t\).

## Assumptions and scope
A divisor \(d\mid N\) is *bi-unitary* when the greatest common **unitary** divisor of \(d\) and \(N/d\) is \(1\). A positive integer \(N\) is *bi-unitary harmonic* if \(\sigma^{**}(N)\mid N\tau^{**}(N)\). The two functions are multiplicative on coprime inputs. For a prime \(r\) and an even exponent \(e=2b\), their prime-power formulas are
\[
\sigma^{**}(r^{2b})=\sum_{j=0}^{2b}r^j-r^b
=\frac{(r^b-1)(r^{b+1}+1)}{r-1},\qquad
\tau^{**}(r^{2b})=2b.
\]
Consequently, putting \(e=2^t\) and \(b=2^{t-1}\) (which is even because \(t\ge2\)), the hypothesized divisibility would be
\[
(p^2+1)\,B\mid 2e\,p^2q^e,
\qquad B=\frac{(q^b-1)(q^{b+1}+1)}{q-1}.
\tag{1}
\]
The statement specifically concerns two-prime squares with one exponent equal to two and the other a power of two at least four. The case with the second exponent equal to one is already classified in prior literature; the exponent-two case is also governed by earlier unitary-harmonic results and is not claimed as new here.

## Proof
**Step 1: a forced square divisor.** As \(b\) is even, modulo \(q+1\) one has
\[
1+q+\cdots+q^{b-1}\equiv 1-1+\cdots+1-1\equiv0,
\qquad q^{b+1}+1\equiv(-1)^{b+1}+1\equiv0.
\]
These are the two integer factors of \(B\). Hence
\[
(q+1)^2\mid B.\tag{2}
\]
Also \(B\equiv1\pmod q\); \(p^2+1\) is coprime to \(p\). Any prime factor of the two factors in the left side of (1) must therefore lie in \(\{2,p,q\}\).

**Step 2: a prime cannot be two.** If \(q=2\) and \(p\) is odd, \(p^2+1\equiv2\pmod8\), so \((p^2+1)/2\) is an odd integer greater than one. Its prime divisors are neither \(2\) nor \(p\), contradicting (1). If \(p=2\) and \(q\) is odd, the factor \(p^2+1=5\) in (1) forces \(q=5\). But (2) then forces \(3\mid B\), while the right side of (1) has only primes \(2\) and \(5\). This is impossible. Thus \(p,q\) are both odd.

**Step 3: both primes odd force a single pair.** For odd \(p\), \(p^2+1\equiv2\pmod8\), so it has an odd prime divisor. By (1) this divisor must be \(q\), giving \(p^2\equiv-1\pmod q\). The residue of \(p\) thus has multiplicative order four modulo \(q\), and \(q\equiv1\pmod4\).

Write \(m=(q+1)/2\), an odd integer at least three. From (2) and (1), \(m^2\mid2e\,p^2q^e\). The integer \(m\) is odd and coprime to \(q\), while \(2e\) is a power of two; hence \(m^2\mid p^2\). This forces \(m=p\), or
\[
q=2p-1.\tag{3}
\]
Since \(q\mid p^2+1\), multiplying by four and using (3) yields
\[
0\equiv4(p^2+1)=(q+1)^2+4\equiv5\pmod q.
\]
Thus \(q=5\) and \(p=3\).

**Step 4: the forced pair is impossible.** For \(p=3,q=5\), the integer \(5^{b+1}+1\) divides \(B\), so by (1) it divides \(2e\,3^2 5^e\). It is coprime to five, and because \(b+1\) is odd,
\[
5^{b+1}+1\equiv5+1\equiv6\pmod8,
\]
so its two-adic valuation is exactly one. Thus all its prime factors must come from \(2\) and \(3\), with valuations at most one and two respectively: \(5^{b+1}+1\le2\cdot3^2=18\). But \(b\ge2\), so \(5^{b+1}+1\ge5^3+1=126\), a contradiction. All cases have been excluded.

## Verification
The accompanying `verify.py` uses only the Python standard library. It constructs the bi-unitary divisor sum by directly excluding the middle divisor of even prime powers, checks the factorization and the square factor \((q+1)^2\) for prime inputs, and tests the complete divisibility obstruction for all ordered distinct prime pairs below \(160\) and \(1\le t\le7\). Executing `python3 verify.py` prints a `VERIFY_OK` summary. These finite checks are corroborative; the four-step proof establishes the unlimited result. The first exponent level in the verifier is a supplementary previously known boundary, not part of the claimed new theorem.

## Relationship to prior work
J. Sándor's 2011 paper introduced these harmonic numbers and their prime-power divisor formulas, studied the cases \(p^3q^2\), \(p^3q^4\), and \(pq^4\), and recorded the isolated \(p^2q=45\). Its Theorem 6 connects bi-unitary and unitary harmonic numbers when all exponents belong to \(\{1,2\}\); accordingly, **we do not claim originality for the case \(p^2q^2\)**. Manea and Minculete (2016) analyze other fixed low-support and exponent patterns, notably \(p^2q^2r\).

Two further public results prove that \(p^{2a}q\) is bi-unitary harmonic only for \(45\), and exclude \(p^3q^{2^{u+1}}\) for all \(u\ge1\). Neither statement implies the present even-even exponent family: the former has a single exponent on \(q\), while the latter has the odd exponent three on \(p\). The new obstruction uses the **square factor \((q+1)^2\)**, which does not arise with the same force in the previously treated odd-even family. Overlap and priority are assessed against these particular published claims rather than through title similarity.

## Limitations
The theorem leaves open other exponent choices, including odd multipliers of powers of two, and does not classify all two-prime bi-unitary harmonic integers. It proves nonexistence for the stated subfamily, not a global density or classification theorem. Prior results settle some neighboring exponent cases; no authorship or independent validation is asserted. A historical source with a stronger, previously unlocated two-prime-square theorem remains a residual priority risk.

## References
1. J. Sándor, *On bi-unitary harmonic numbers*, arXiv:1105.0294v1, first posted 2011-05-02. https://arxiv.org/abs/1105.0294
2. A. Manea and N. Minculete, *Types of integer harmonic numbers (II)*, Bulletin of the Transilvania University of Brașov, Series III, 9(58) (2016), 67–82. https://webbut.unitbv.ro/index.php/Series_III/article/download/1820/1566/3270
3. *Rigidity in a two-prime bi-unitary harmonic family*, public research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-rigidity-in-a-two-prime-bi-unitary-harmonic-family--dec9bad14874
4. *A power-of-two exponent obstruction for bi-unitary harmonic numbers*, public research record (2026). https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-a-power-of-two-exponent-obstruction-for-bi-unitary-harmonic-numb--4cbca30799f8
5. OEIS A286325, *Bi-unitary harmonic numbers*, https://oeis.org/A286325 (tabular corroboration only).
