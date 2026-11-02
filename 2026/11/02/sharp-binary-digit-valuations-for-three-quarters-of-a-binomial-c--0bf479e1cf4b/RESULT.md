# Sharp binary-digit valuations for three quarters of a binomial-convolution sequence

## Finding
For positive integers \(n\), set
\[
S_n=\sum_{k=0}^{n-1}(3k+1)\binom{2k}{k}^{3}16^{n-1-k}.
\]
Write \(s_2(m)\) for the number of ones in the binary expansion of \(m\), with \(s_2(0)=0\). **Theorem.** For every positive \(n\) not divisible by \(4\),
\[
\nu_2(S_n)=\begin{cases}
3s_2(n-1), & n\text{ odd},\\
3s_2(n-1)+1, & n\equiv2\pmod4.
\end{cases}
\]
Thus the precise power of two dividing the natural truncated binomial sum is governed by binary digit weight on three residue classes modulo four, strengthening mere divisibility in this range.

## Assumptions and scope
All binomial coefficients and sums above are ordinary integers, and \(\nu_2\) denotes the valuation at the prime \(2\) of a nonzero integer. The sum is strictly positive. The stated quantifiers are \(n\ge1\) with \(n\equiv1,2,3\pmod4\). No assertion is made for multiples of four. The initial case is \(S_1=1\).

## Proof
For nonnegative \(r\), Legendre's formula gives \(\nu_2\binom{2r}{r}=s_2(r)\). The digit-sum subadditivity \(s_2(a+b)\le s_2(a)+s_2(b)\) implies, for \(0\le j\le a\),
\[
s_2(a-j)\ge s_2(a)-s_2(j).
\]
If \(n\) is odd, write the summation index as \(k=n-1-j\), \(0\le j\le n-1\). The \(j=0\) summand is
\[
(3n-2)\binom{2n-2}{n-1}^{3};
\]
its valuation equals \(3s_2(n-1)\), because \(3n-2\) is odd. For each \(j\ge1\), the \(j\)-th summand has valuation at least
\[
4j+3s_2(n-1-j)\ge3s_2(n-1)+4j-3s_2(j)
\ge3s_2(n-1)+j>3s_2(n-1),
\]
using \(s_2(j)\le j\). Therefore the final summand is the unique term of minimum valuation, proving the odd-index assertion without relying on cancellation.

Now suppose \(n\equiv2\pmod4\). The defining convolution gives the exact recurrence
\[
S_n=16S_{n-1}+(3n-2)\binom{2n-2}{n-1}^{3}.
\]
Because \(n-1\) is odd, the established case yields \(\nu_2(16S_{n-1})=4+3s_2(n-2)\). Since \(n-2\) is even, \(s_2(n-1)=s_2(n-2)+1\), making the first valuation \(3s_2(n-1)+1\). On the other hand, \(3n-2\) is divisible by four, so the second summand has valuation at least \(3s_2(n-1)+2\). The two valuations differ and the first controls the sum. This proves the second case, including \(n=2\), and completes the proof.

## Verification
The included standalone Python program `verify.py` evaluates the defining integers by the exact recurrence and independently calculates the predicted digit-weight valuations. It exhaustively compares all qualifying \(n\le1024\), including the boundary cases \(n=1,2,3\), reporting the tested count. This is a finite reproducibility check, not the proof of the infinite theorem.

## Relationship to prior work
Mao and Zhang, *Proof of Sun's conjectures on super congruences and the divisibility of certain binomial sums*, arXiv:1511.05553v1 (first posted 2015-11-17), Theorem 1.1, established for all \(n\ge2\) that \(2n\binom{2n}{n}\) divides \(S_n\). Their result is a divisibility lower bound and does not state the exact binary-digit valuation on the three residue classes proved here. Ni and Pan (2020) studied different weighted binomial sums. Zhang and Yuan (2021) prove a Dwork-type congruence for the related normalized hypergeometric truncations at odd primes, but their stated range excludes the prime two. The present theorem is a direct sharp valuation statement and does not assert novelty of its elementary ingredients.

## Limitations
The method does not determine the valuation when \(n\) is divisible by four, where the two last-stage terms can have equal valuation and cancel. The theorem concerns only the prime two, not odd prime valuations. Although searches found no equivalent precise formula in the checked sources, broader historical coverage cannot be excluded; independent review has not occurred.

## References
1. Guo-Shuai Mao and Tao Zhang, *Proof of Sun's conjectures on super congruences and the divisibility of certain binomial sums*, arXiv:1511.05553v1, 2015-11-17, https://arxiv.org/abs/1511.05553.
2. He-Xia Ni and Hao Pan, *Divisibility of some binomial sums*, Acta Arithmetica 194 (2020), 367–381, https://doi.org/10.4064/aa181114-24-7.
3. Yong Zhang and Peisen Yuan, *Proof of a Dwork-type supercongruence by induction*, AIMS Mathematics 6 (2021), 11568–11583, https://doi.org/10.3934/math.2021671.
4. Legendre's formula and binary digit-sum subadditivity are used in the proof in their elementary standard forms.
