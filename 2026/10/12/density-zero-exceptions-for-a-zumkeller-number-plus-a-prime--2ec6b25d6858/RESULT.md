# Density-zero exceptions for a Zumkeller number plus a prime

## Finding
A positive integer is **Zumkeller** when its positive divisors admit a partition into two classes with equal sums. Let \(E(X)\) be the number of positive integers \(n\le X\) for which no identity \(n=z+p\) exists with \(z\) Zumkeller and \(p\) prime. Then
\[
\boxed{\lim_{X\to\infty}\frac{E(X)}{X}=0.}
\]
More precisely, for every positive integer \(r\), the argument supplies a finite set of \(r\) pairwise coprime odd Zumkeller moduli and a threshold \(B_r\) such that all nonrepresentable \(n>B_r\) occupy residue classes of total proportion strictly below \((3/4)^r\).

## Assumptions and scope
All integers in the summands are positive; the prime \(p\) is any ordinary rational prime. Natural density is relative to all positive integers. The prime-block construction used below is the published Lemma 3.3 of Somu, Kukla and Tran [1]: with \(p_k\) denoting the \(k\)-th prime and \(f(k)\) the least index for which
\[
\prod_{j=k}^{f(k)}\left(1+\frac1{p_j}\right)\ge2,
\]
the squarefree block \(A_k=\prod_{j=k}^{f(k)}p_j\) is Zumkeller for every sufficiently large \(k\). This theorem is an input, not a new result. Such \(f(k)\) exists since the sum of prime reciprocals diverges. We use only indices \(k\ge2\), so the constructed blocks are odd.

## Proof
**1. Coprime closure.** If \(z\) is Zumkeller and \(w\ge1\) is coprime to \(z\), then \(zw\) is Zumkeller: every divisor of \(zw\) factors uniquely into a divisor of \(z\) times a divisor of \(w\). Multiplying both parts of a balanced divisor partition of \(z\) by each divisor of \(w\) yields two equal-sum parts of the divisors of \(zw\). This also proves the closure property quoted as Lemma 2.1 of [1]. In particular, for every \(t\ge0\),
\[
z(1+zt)=z+z^2t\quad\text{is Zumkeller.}\]

**2. A fixed-modulus prime representation lemma.** Fix a Zumkeller integer \(z\). In every residue class \(a\pmod{z^2}\) with \(\gcd(a,z)=1\), Dirichlet's theorem supplies a prime \(q_a\) satisfying
\[
q_a\equiv a-z\pmod{z^2},
\]
because \(\gcd(a-z,z^2)=1\). Choose one such prime for each of the finitely many reduced classes and let \(B_z=z+\max_a q_a\). For any integer \(n>B_z\) with \(\gcd(n,z)=1\), take \(a\equiv n\pmod{z^2}\). Then \(n-q_a=z+z^2t\) for an integer \(t\ge0\), and Step 1 makes \(n-q_a\) Zumkeller. Therefore every sufficiently large integer coprime to each fixed Zumkeller modulus \(z\) has a Zumkeller-plus-prime representation. No bound uniform in \(z\) is asserted.

**3. Many independent odd moduli.** Choose integers \(k_1<k_2<\cdots\) sufficiently large that \(k_{i+1}>f(k_i)\), and put \(z_i=A_{k_i}\). By the cited prime-block lemma, the \(z_i\) are odd Zumkeller numbers, squarefree and pairwise coprime. Set
\[
R_i=\prod_{j=k_i}^{f(k_i)}\left(1+\frac1{p_j}\right).
\]
Minimality of the final prime in the block gives
\[
2\le R_i<2\left(1+\frac1{p_{f(k_i)}}\right)\le\frac83.
\]
As all primes in the block are odd,
\[
\prod_{p\mid z_i}(1-p^{-2})\ge\prod_{m=3}^{\infty}(1-m^{-2})=\frac23.
\]
The last infinite product telescopes. Consequently,
\[
\frac{\varphi(z_i)}{z_i}=\frac{\prod_{p\mid z_i}(1-p^{-2})}{R_i}>\frac14.
\]

**4. A density squeeze.** Fix any \(r\ge1\) and put \(B_r=\max_{1\le i\le r}B_{z_i}\). By Step 2, if an integer \(n>B_r\) has no required representation, then \(\gcd(n,z_i)>1\) for *every* \(1\le i\le r\). The \(z_i\) are pairwise coprime, so the Chinese remainder theorem says that the set of integers satisfying all these divisibility conditions is periodic modulo \(z_1\cdots z_r\), with exact natural density
\[
\prod_{i=1}^r\left(1-\frac{\varphi(z_i)}{z_i}\right)<\left(\frac34\right)^r.
\]
Ignoring the finite exceptional initial segment therefore gives
\[
0\le\limsup_{X\to\infty}\frac{E(X)}X\le\left(\frac34\right)^r
\quad\text{for every }r\ge1.
\]
Letting \(r\to\infty\) proves the stated limit.

## Verification
The proof's critical deductions are exact: divisors of a coprime product factor uniquely; the Dirichlet residue is reduced; the prime choice is bounded for each fixed modulus because there are finitely many reduced classes; odd prime blocks have uniformly bounded reciprocal-prime Euler products; and the Chinese remainder theorem gives the stated product of residue proportions. The published prime-block Zumkeller lemma [1, Lemma 3.3] is used with its full eventual-index hypothesis. The accompanying finite checker replays small modular and partition examples but is not used as an infinite certificate.

## Relationship to prior work
Somu, Kukla and Tran [1] prove the prime-block Zumkeller lemma and the coprime-multiplier closure; they also exhibit infinitely many integers *not* expressible as a Zumkeller number plus a prime (Theorem 4.19). Their Conjecture 4.21 explicitly predicts that the exceptional set nevertheless has density zero. The theorem above settles exactly that **prime-summand half**; it is consistent with the published infinite exceptional family. Proposition 4.12 covers several specific congruence classes, but does not yield a density-one conclusion. Their practical-summand result has a different second summand. The OEIS record [2] catalogs finite values and cites the known coexistence of infinitely many representable and nonrepresentable integers, without asserting this limiting density. The substantive additional bridge is the fixed-modulus Dirichlet lemma applied to an unbounded coprime family, followed by a uniform totient-ratio CRT squeeze.

## Limitations
The argument does **not** establish that all sufficiently large integers are representable: the motivating authors prove infinitely many exceptions. It gives neither an explicit rate of decay for \(E(X)/X\) nor an effective universal bound on \(B_r\). It does not prove the corresponding density-zero conjecture for Zumkeller-plus-square representations. The claim of originality is relative to the checked sources and mathematical-record searches, not an independent literature certification.

## References
[1] S. T. Somu, A. Kukla, D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (first publicly submitted 2023-10-22); see v2 (2023-11-27), Lemmas 2.1 and 3.3, Proposition 4.12, Theorem 4.19, Conjecture 4.21. https://arxiv.org/html/2310.14149v2

[2] OEIS A368082, *Positive integers which can be written as a sum of a Zumkeller number and a prime number*. https://oeis.org/A368082

[3] Y. Peng and K. P. S. Bhaskara Rao, *On Zumkeller numbers*, Journal of Number Theory 133 (2013), 1135–1155. The coprime-multiplier property is restated in [1].
