# Exact dyadic 2-adic spikes in the reciprocal-binomial factorial sum

## Finding

For each integer \(m\ge4\), let \(N=2^m\) and define the rational sum
\[
b_N=\sum_{k=1}^N\frac{2^k}{k}.
\]
Then the **exact** valuation is
\[
\boxed{\nu_2(b_{2^m})=2^m+2m-2}.
\]
Equivalently, define the integer sequence
\[
a_n=\sum_{j=0}^{n-1}j!(n-1-j)!=\frac{n!}{2^n}b_n\quad(n\ge1).
\]
For every integer \(m\ge4\),
\[
\boxed{\nu_2(a_{2^m})=2^m+2m-3}.
\]
Thus \(a_{2^m}\) contains exactly \(3m-2\) more factors of \(2\) than \((2^m-1)!\). The initial cases \(m=1,2,3\) are excluded; their valuations of \(a_{2^m}\) are \(1,4,12\), respectively.

## Assumptions and scope

All series below are interpreted in the field \(\mathbb Q_2\) of \(2\)-adic numbers, with \(\nu_2(2)=1\). The integer \(m\) is arbitrary and satisfies \(m\ge4\). A rational series with terms whose valuations tend to infinity converges \(2\)-adically. The power series \(\log(1-z)=-\sum_{k\ge1}z^k/k\) and \(\operatorname{Li}_s(z)=\sum_{k\ge1}z^k/k^s\), for \(s=2,3\), converge at \(z=2\).

## Proof

**1. Two cancellations.** The \(2\)-adic logarithm is a homomorphism on \(1+2\mathbb Z_2\). Therefore \(2\log(-1)=\log(1)=0\), hence \(\log(-1)=0\) and
\[
\sum_{k\ge1}\frac{2^k}{k}=-\log(1-2)=0.
\]
The power-series dilogarithm reflection identity
\[
\operatorname{Li}_2(z)+\operatorname{Li}_2\!\left(\frac z{z-1}\right)
=-\frac12\log^2(1-z)
\]
holds on \(\nu_2(z)\ge1\). It can be checked *without invoking a named analytic continuation theorem*: differentiate both sides, using \(\operatorname{Li}_2'(z)=-\log(1-z)/z\) and \(\log(1-z/(z-1))=-\log(1-z)\), and note that both sides vanish at \(z=0\). Evaluating at \(z=2\) gives \(2\operatorname{Li}_2(2)=0\), so
\[
\sum_{k\ge1}\frac{2^k}{k^2}=0.
\]
Both identities are exact equalities in \(\mathbb Q_2\).

**2. The leading cubic coefficient.** Put
\[
H_0=\sum_{j\ge1}\frac{2^{j-1}}{j^3}.
\]
The term \(j=4\) has valuation \(-3\), and **every other term has strictly greater valuation**. Indeed the termwise valuation is \(j-1-3\nu_2(j)\); it equals \(-2\) at \(j=2,8\), is nonnegative at \(j=1,3\), and is at least \(2\) for every remaining \(j\ge5\) except \(j=8\). Consequently
\[
\nu_2(H_0)=-3.
\]

**3. A uniform comparison at powers of two.** Fix \(m\ge4\), let \(N=2^m\), and set
\[
H_N=\sum_{j\ge1}\frac{2^{j-1}}{j^2(j+N)}.
\]
Then
\[
H_N-H_0=-N\sum_{j\ge1}\frac{2^{j-1}}{j^3(j+N)}.
\]
We prove that each term on the right has valuation at least \(-1\). Write \(h=\nu_2(j)\). If \(h<m\), then \(\nu_2(j+N)=h\), giving valuation \(m+j-1-4h\). When \(h=0,1,2,3\) this is at least \(m-5\ge-1\); for \(h\ge4\), the inequality \(j\ge2^h\) gives an even larger lower bound because \(2^h\ge4h\).

If \(h>m\), then \(\nu_2(j+N)=m\), giving valuation \(j-1-3h\ge2^h-1-3h\ge16\).

If \(h=m\), write \(j=Nu\) with positive odd \(u\). The valuation is
\[
j-1-3m-\nu_2(u+1).
\]
Since \(\nu_2(u+1)\le u\) and \(j=2^m u\), this is at least \((2^m-1)u-1-3m\ge2\) for \(m\ge4\). Therefore
\[
\nu_2(H_N-H_0)\ge-1>-3=\nu_2(H_0),
\]
and the ultrametric property gives \(\nu_2(H_N)=-3\).

**4. Reconstruct the finite sum.** Define
\[
F(N)=\sum_{j\ge1}\frac{2^{j-1}}{j+N}.
\]
The two cancellations in Step 1 and the rational identity
\[
\frac1{j+N}-\frac1j+\frac N{j^2}=\frac{N^2}{j^2(j+N)}
\]
give \(F(N)=N^2H_N\). Hence \(\nu_2(F(N))=2m-3\). Since the infinite logarithmic sum vanishes,
\[
b_N=-\sum_{k>N}\frac{2^k}{k}=-2^{N+1}F(N).
\]
It follows that \(\nu_2(b_N)=N+1+2m-3=N+2m-2\). Finally \(\nu_2(N!)=N-1\) for \(N=2^m\); applying \(a_N=N!2^{-N}b_N\) yields \(\nu_2(a_N)=N+2m-3\), as claimed. \(\square\)

## Verification

Run `python3 verify.py` with Python 3, using only its standard library. It constructs \(a_n\) both from the recurrence \(2a_n=na_{n-1}+2(n-1)!\) and from the independent integer factorial convolution, and checks every dyadic index through \(2^{12}\) and all preceding exceptional cases. The finite tests do not replace Steps 1–4, which prove the result for all \(m\ge4\).

## Relationship to prior work

Farhi (2022, arXiv:2204.10136) defined the rational recurrence, related it to the Genocchi numbers, and gave a general digit-sum valuation lower bound. His follow-up arXiv:2204.12760 gave the factorial convolution and stronger general valuation bounds. Dubickas (2024) established \(\nu_2(b_n)\ge n+1-\log_2(n+1)\), with equality exactly for \(n=2^k-1\); his sharpness claim concerns those indices, **not the distinct endpoints \(n=2^m\) studied here**. Farhi (2023) gave general prime-adic bounds for symmetrized truncated logarithms. The present exact dyadic formula is not implied by those lower bounds, by the known factorial convolution, or by any OEIS values inspected. No earlier exact formula for this infinite dyadic subsequence was found among the inspected references and indexed mathematical records.

## Limitations

No exact valuation formula is asserted for arbitrary \(n\), or for primes other than \(2\). The first three dyadic indices do not obey the displayed law. The literature comparison does not prove uniqueness or priority in unindexed sources; independent scholarly review has not been performed.

## References

1. B. Farhi, *On a curious integer sequence*, arXiv:2204.10136v1, first public April 21, 2022. https://arxiv.org/abs/2204.10136
2. B. Farhi, *The integrality of the Genocchi numbers obtained through a new identity and other results*, arXiv:2204.12760v1 (2022). https://arxiv.org/abs/2204.12760
3. A. Dubickas, *On a sequence of rational numbers with unusual divisibility by a power of 2*, Miskolc Math. Notes 25 (2024), 203–208. DOI: 10.18514/MMN.2024.4276.
4. B. Farhi, *Nontrivial lower bounds for the p-adic valuation of certain rational numbers*, Journal of Integer Sequences 26 (2023), Article 23.6.1. https://cs.uwaterloo.ca/journals/JIS/VOL26/Farhi2/farhi42.pdf
5. OEIS A003149, factorial reciprocal-binomial sum. https://oeis.org/A003149
6. D. Kruchinin and V. Kruchinin, *A family of generating functions for reciprocal binomial coefficients and its applications*, arXiv:2602.07822 (2026). https://arxiv.org/abs/2602.07822
