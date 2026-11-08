# A complete binary phase diagram for weighted LCM recurrences

## Finding
For each fixed integer \(K\ge1\), define positive integers \(A_1=1\) and, for every \(n\ge2\),
\[
 A_n=K A_{n-1}+\operatorname{lcm}(n,A_{n-1})
 =A_{n-1}(K+b_n),\qquad b_n=\frac{n}{\gcd(n,A_{n-1})}.
\]
This theorem classifies **all** indices at which the increment \(b_n\) is even, for **every** positive integer coefficient \(K\).

**Even coefficient.** If \(K\) is even, put \(t=\nu_2(K+2)\ge1\). For every \(n\ge2\),
\[
 \nu_2(A_n)=t\left\lceil\frac{\lfloor\log_2 n\rfloor}{t}\right\rceil.
\]
Moreover, for every \(n\ge2\),
\[
 b_n\text{ is even}\quad\Longleftrightarrow\quad b_n=2\text{ and }n=2^{1+jt}
 \text{ for some integer }j\ge0.
\]
Consequently the number of even increments up to \(X\ge2\) is
\[
 1+\left\lfloor\frac{\lfloor\log_2 X\rfloor-1}{t}\right\rfloor.
\]

**Odd coefficient.** If \(K\) is odd, the even increments consist of \(b_2=2\) and, additionally, \(b_4=2\) **precisely** when \(K\bmod12\in\{1,3,11\}\). Every other increment is odd; for every \(n\ge4\) one also has \(\nu_2(A_n)\ge n-4\). Therefore the even-increment support is finite for odd coefficients, but infinite and logarithmically sparse for even coefficients.

## Assumptions and scope
All coefficients \(K\) are fixed positive integers, and all recurrences are in ordinary positive integers starting at \(A_1=1\). The index \(n\) ranges over every integer at least \(2\). The valuation \(\nu_2\) is taken on positive integers. Claims concern parity of \(b_n\) and valuations of \(A_n\), not primality or exact values of odd increments. The odd-coefficient valuation inequality is a bound, not an asserted equality.

## Proof
**Basic identity.** Because \(b_n=n/\gcd(n,A_{n-1})\), it divides \(n\) and satisfies
\[
 \nu_2(b_n)=\max\{0,\nu_2(n)-\nu_2(A_{n-1})\}.
\]
Also \(A_n=A_{n-1}(K+b_n)\).

**Even \(K\).** Put \(t=\nu_2(K+2)\). Since \(b_2=2\), the base case is \(\nu_2(A_2)=t\). We prove by induction that on the entire dyadic block \(2^r\le n<2^{r+1}\), the valuation is the constant
\[
 V_r=t\left\lceil\frac r t\right\rceil\quad(r\ge1).
\]
Suppose this is true through the end of block \(r\). For its internal indices \(2^r<n<2^{r+1}\), one has \(\nu_2(n)\le r\le V_r\); thus \(b_n\) is odd. Since \(K\) is even, the multiplier \(K+b_n\) is odd, so the valuation remains \(V_r\). At the next boundary \(n=2^{r+1}\), the basic identity gives
\[
 \nu_2(b_n)=\max(0,r+1-V_r).
\]
If \(t\nmid r\), then \(V_r\ge r+1\), so \(b_n\) is odd and the valuation remains \(V_r=V_{r+1}\). If \(t\mid r\), then \(V_r=r\), hence \(\nu_2(b_n)=1\). Since \(b_n\) divides the power \(2^{r+1}\), necessarily \(b_n=2\), and the multiplier has valuation exactly \(t\). Thus \(\nu_2(A_n)=r+t=V_{r+1}\). This proves the block induction, and shows that the even indices are precisely \(n=2^{1+jt}\), including the base \(n=2\). Counting those powers gives the formula for \(X\).

**Odd \(K\).** Every odd index \(j\ge3\) has \(b_j\) odd because \(b_j\mid j\). Consequently \(K+b_j\) is even and raises \(\nu_2(A_j)\) by at least one. For each even \(n\ge6\), there are \((n-2)/2\) odd indices in \([3,n-1]\). Therefore
\[
 \nu_2(A_{n-1})\ge(n-2)/2\ge\nu_2(n),
\]
where the final elementary inequality holds for every even \(n\ge6\). The basic identity then makes \(b_n\) odd. For odd \(n\ge3\), parity was automatic. It remains to inspect \(n=2\) and \(n=4\). At \(n=2\), \(A_2=K+2\) is odd and \(b_2=2\). At \(n=3\), \(b_3=1\) if \(K+2\equiv0\pmod3\), and \(b_3=3\) otherwise. Hence \(A_3=(K+2)(K+b_3)\). The factor \(K+2\) is odd; consequently \(b_4\) is even exactly when \(\nu_2(K+b_3)=1\), in which case \(b_4=2\). Checking the six odd residue classes modulo \(12\) gives \(K\equiv1,3,11\pmod{12}\). Finally every multiplier at \(n\ge5\) is even, so \(\nu_2(A_n)\ge n-4\) for \(n\ge4\). This completes both classifications.

## Verification
A standalone integer-arithmetic verifier accompanies the theorem as `verify.py`, with its observed output in `verification_output.txt`. One implementation evaluates the recurrence in arbitrary-precision integers using \(\gcd\); a second evaluates in residues modulo an integer divisible by every index in its tested range, so its gcd calculations remain exact. Tests cover 320 coefficients through index 700, another 120 coefficients through index 384, targeted powers-of-two valuation parameters through index 2048, and odd coefficients through index 4096. All tests passed. Finite checks corroborate but do not replace the preceding proof.

## Relationship to prior work
Cloitre's *Primes in LCM recurrences* (first posted October 18, 2025) defines the coefficient-\(K\) family and proves a binary staircase **for \(K=2\)** in Proposition 6.5. This known instance agrees exactly with the even-coefficient theorem above when \(t=2\). The contribution here is the **uniform classification for all positive coefficients**: a coefficient-dependent stride \(t\) for every even \(K\), and a qualitatively different finite-support law for all odd \(K\). The source's statements about other coefficients do not assert this joint classification. OEIS A135508 records the corresponding \(K=2\) sequence; that case is not claimed as new. The earlier Ruiz-Cabello study concerns modifications of the original unweighted recurrence and is distinguished from varying the coefficient.

## Limitations
The theorem does not classify the odd values of \(b_n\), settle their primality, or provide exact 2-adic valuations for arbitrary odd \(K\) beyond the stated lower bound. Its coefficient-wide generalization may be implicit in specialist arguments; unindexed equivalent work has not been excluded. The proof does not rely on computational exhaustion.

## References
1. B. Cloitre, *Primes in LCM recurrences*, arXiv:2510.18891 (first posted 2025-10-18), https://arxiv.org/html/2510.18891, Proposition 6.5 and §7.4.
2. OEIS A135508, https://oeis.org/A135508, special-case binary increment sequence.
3. OEIS A135504, https://oeis.org/A135504, related unweighted recurrence.
4. J. C. Ruiz-Cabello, *On the (a(n)) sequence*, arXiv:1504.05041, https://arxiv.org/abs/1504.05041 (related initial-condition question).
