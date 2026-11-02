# Rare-event distribution and moments of normalized Euler-totient deficiency

## Finding

Let \(\varphi\) denote Euler's totient and let \(S(n)=\sum_{p\mid n}(p-1)\), summing once over each distinct prime divisor; put \(S(1)=0\). Define the normalized deficiency and its complement by
\[
\Delta(n)=\varphi(n)-1-S(n),\qquad
R(n)=1-\frac{\Delta(n)}{\varphi(n)}=\frac{1+S(n)}{\varphi(n)}.
\]

**Exact positive-threshold distribution.** For every fixed real \(t>0\), the set \(A_t=\{m\ge1:\varphi(m)\le1/t\}\) is finite and, as \(x\to\infty\),
\[
\boxed{\#\{n\le x:R(n)>t\}
=\sum_{m\in A_t}\pi(x/m)+O_t(1)
=H(t)\frac{x}{\log x}+O_t\left(\frac{x}{(\log x)^2}\right),}
\qquad H(t)=\sum_{m\in A_t}\frac1m.
\]
Here \(\pi(y)\) counts primes up to the real number \(y\). The \(O_t(1)\) error is bounded independently of \(x\). Thus, apart from finitely many exceptions depending on \(t\), the integers where \(R(n)>t\) are exactly the prime multiples \(n=mp\), with \(m\in A_t\) and \(p\) prime. The weak inequality in the definition of \(A_t\) is essential at the boundary \(t=1/\varphi(m)\), even though the original threshold is strict.

**Complete fixed integral-moment spectrum.** For every fixed integer \(k\ge1\),
\[
\boxed{\frac1x\sum_{n\le x}R(n)^k
\sim\frac{C_k}{\log x},\qquad
C_k=\sum_{m\ge1}\frac1{m\varphi(m)^k}
=\prod_{p}\left(1+\frac{p^k}{(p-1)^k(p^{k+1}-1)}\right).}
\]
The sum and product converge absolutely. In particular,
\[
\frac1x\sum_{n\le x}\frac{\Delta(n)}{\varphi(n)}
=1-\frac{C_1+o(1)}{\log x},\qquad
C_1=\prod_p\left(1+\frac{p}{(p-1)(p^2-1)}\right).
\]
The empirical distribution of \(\Delta(n)/\varphi(n)\) therefore converges weakly to the point mass at \(1\), and this convergence holds in every fixed positive integral moment of its deviation from \(1\).

## Assumptions and scope

All integers \(n\) and \(m\) are positive, with \(\varphi(1)=1\). The threshold \(t\) and moment order \(k\) are fixed before \(x\to\infty\); the asserted errors and asymptotics are not uniform as \(t\) tends to zero or \(k\) tends to infinity. The prime variable in the formula for \(H(t)\) is distinct from the prime divisors of a fixed multiplier \(m\). No unresolved hypothesis about primes is used: only the classical prime number theorem and elementary multiplicativity of \(\varphi\).

For examples, \(A_1=\{1,2\}\) and \(A_{1/2}=\{1,2,3,4,6\}\), giving \(H(1)=3/2\) and \(H(1/2)=9/4\). For \(t>1\), the set \(A_t\) is empty and only finitely many integers have \(R(n)>t\).

## Proof

**1. Largest-prime decomposition.** If \(n\ge2\), let \(p\) be its largest prime divisor and uniquely write \(n=mp^a\), where \(a\ge1\) and \(p\nmid m\). Since every prime dividing \(m\) is smaller than \(p\),
\[
R(mp^a)=\frac{p+S(m)}{p^{a-1}(p-1)\varphi(m)}
=\frac{1+(1+S(m))/(p-1)}{p^{a-1}\varphi(m)}
\le\frac{2+\omega(m)}{p^{a-1}\varphi(m)},
\]
where \(\omega(m)\) is the number of distinct prime divisors. The elementary bounds \(\omega(m)\le\log_2m\) and \(\varphi(m)\ge\sqrt{m/2}\) imply
\[
\frac{2+\omega(m)}{\varphi(m)}\longrightarrow0
\qquad(m\to\infty).
\]
The latter totient estimate follows prime-power by prime-power: for odd \(q\), \(\varphi(q^b)\ge\sqrt{q^b}\), while \(\varphi(2^b)\ge\sqrt{2^b/2}\). Consequently, \(R(n)>t\) forces \(m\) into a finite set depending only on \(t\). When \(a\ge2\), the same bound forces \(p^{a-1}\) to be bounded, and there are only finitely many possible \((m,p,a)\). Hence all sufficiently large integers with \(R(n)>t\) have \(a=1\).

For any fixed \(m\) and any prime \(p\nmid m\),
\[
R(mp)=\frac1{\varphi(m)}
\left(1+\frac{1+S(m)}{p-1}\right)
>\frac1{\varphi(m)},\qquad
R(mp)\to\frac1{\varphi(m)}\quad(p\to\infty).
\]
Therefore, when \(\varphi(m)\le1/t\), every sufficiently large prime multiple \(mp\) passes the strict threshold, including the equality case. When \(\varphi(m)>1/t\), only finitely many prime multiples pass. Because the eligible multipliers are finite, and two representations with different eligible multipliers could coincide only when at least one corresponding prime is bounded, we obtain the set equality up to a finite symmetric difference and the claimed prime-count formula. Applying \(\pi(y)=y/\log y+O(y/(\log y)^2)\) to finitely many fixed multipliers proves the displayed \(H(t)\) asymptotic.

**2. First moment.** Euler's inequality above also gives
\[
\sum_{n\le x}\frac1{\varphi(n)}\le\sqrt2\sum_{n\le x}n^{-1/2}=O(\sqrt x).
\]
For the additive prime-support contribution, count each pair consisting of an integer and one of its prime divisors. Writing that integer as \(mp^a\) with \(p\nmid m\) gives the exact identity
\[
\sum_{n\le x}\frac{S(n)}{\varphi(n)}
=\sum_{\substack{mp^a\le x\\p\nmid m,\ a\ge1}}
\frac{p^{1-a}}{\varphi(m)}.
\]
For \(a\ge2\), the absolute contribution is at most
\[
O(\sqrt x)\sum_p\sum_{a\ge2}p^{1-3a/2}=O(\sqrt x),
\]
using the preceding bound on the partial sum of \(1/\varphi\). For \(a=1\), dropping the restriction \(p\nmid m\) introduces at most
\[
\sum_{m\le x}\frac{\omega(m)}{\varphi(m)}
=O(\sqrt x\log(2x)).
\]
Thus
\[
\sum_{n\le x}R(n)
=\sum_{m\le x/2}\frac{\pi(x/m)}{\varphi(m)}
+O(\sqrt x\log(2x)).
\]
For \(m>\sqrt x\), \(\pi(x/m)\le x/m\) bounds the sum by \(O(x^{3/4})\). For \(m\le\sqrt x\), the prime number theorem and \(\log(x/m)\ge\frac12\log x\) imply
\[
\frac{\log x}{x}\pi(x/m)\longrightarrow\frac1m
\quad\text{for each fixed }m,
\qquad
0\le\frac{\log x}{x}\pi(x/m)\ll\frac1m.
\]
Because \(\sum_{m\ge1}1/(m\varphi(m))\) converges by the totient bound, dominated convergence yields
\[
\lim_{x\to\infty}\frac{\log x}{x}\sum_{n\le x}R(n)
=\sum_{m\ge1}\frac1{m\varphi(m)}=C_1.
\]

**3. Higher integral moments.** One has \(0<R(n)\le2\) for all \(n\): for composite \(n\) other than twice an odd prime, the Ranjan--Singh inequality gives \(\Delta(n)\ge0\), and for \(n=1\), prime \(n\), or \(n=2p\) the bound follows directly. Fix a positive integer \(B\). The prime multiples \(n=mp\) with \(m\le B\), \(p>B\), and \(p\nmid m\) are distinct; for each fixed \(m\), their \(k\)-th-moment contribution is
\[
\sum_{\substack{p\le x/m\\p>B,\ p\nmid m}}R(mp)^k
=\left(\frac1{\varphi(m)^k}+o(1)\right)\frac{x}{m\log x}.
\]
The total first-moment contribution of all integers *outside* these finitely many families has normalized logarithmic limsup
\[
C_1-\sum_{m\le B}\frac1{m\varphi(m)},
\]
by step 2. On the complement, \(R(n)^k\le2^{k-1}R(n)\). This controls the normalized \(k\)-th-moment remainder by at most \(2^{k-1}\bigl(C_1-\sum_{m\le B}1/(m\varphi(m))\bigr)\). Letting \(B\to\infty\) makes the bound zero. Thus the \(k\)-th moment has coefficient \(C_k\). Multiplicativity of \(1/(m\varphi(m)^k)\) and the geometric prime-power series give the stated Euler product. Finally, \(\Delta(n)/\varphi(n)=1-R(n)\), so the first-moment claim follows, and convergence in probability follows from the positive-threshold counting formula.

## Verification

The standalone program `verifier.py` uses exact Euler-totient and prime-support sieves, and integer-only comparisons, through \(250000\). For six rational thresholds, it independently compares direct counts of \(R(n)>t\) with the finite sum of prime counts; all observed discrepancies have stabilized by \(10000\), consistent with the theorem's \(O_t(1)\) remainder. It additionally compares the first two logarithmically normalized sample moments with partial sums for \(C_1\) and \(C_2\). This is finite corroboration, not a proof of the infinite asymptotics. Execute `python3 verifier.py` with Python 3 and no nonstandard packages.

## Relationship to prior work

Ranjan and Singh [1] prove the unnormalized sign inequality for \(\Delta(n)\) and classify its zero cases. Their statement makes the ratio \(\Delta(n)/\varphi(n)\) a natural object but does not provide its distribution, exceptional-level sets, or moments. Belbachir, Ranjan, and Singh [2] subsequently determine the mean of the **unnormalized** deficiency and explicitly raise the normalized-distribution question (Question 9.4), without establishing the formulas above. The classical work of Alladi and Erdős [3] studies sums of prime factors and their unnormalized average order; these estimates do not yield the normalization-sensitive prime-multiple threshold law as a stated result. In particular, the exact threshold multiplier criterion and the all-integer-moment Euler factors are not consequences of the displayed theorems in these primary sources. Earlier implicit coverage in broader literature has not been excluded by independent priority review.

## Limitations

All asymptotics fix \(t>0\) or the positive integer \(k\). The finite exceptional set in the threshold formula is not uniformly bounded in \(t\); the result does not describe the finer distribution on scales where \(t\) itself tends to zero. No claim is made about a central-limit normalization for typical integers, or uniform high-moment bounds. Finite numerical checks cannot prove a prime number theorem or infinite convergence. Scientific priority remains subject to independent literature review.

## References

1. R. Ranjan and S. N. Singh, *An Inequality for Euler's Phi-Function*, publicly uploaded 21 July 2025, DOI: 10.13140/RG.2.2.34472.69128; https://www.researchgate.net/publication/393870741_AN_INEQUALITY_FOR_EULER%27S_PHI-FUNCTION .
2. H. Belbachir, R. Ranjan, and S. N. Singh, *Infinite families and sporadic solutions of the equation \(\varphi(n)=c+\alpha\sum_{p\mid n}\varphi(p)\)*, arXiv:2610.36260v1 (26 October 2026), Sections 6 and 9; https://arxiv.org/html/2610.36260v1 .
3. K. Alladi and P. Erdős, *On an Additive Arithmetic Function*, Pacific Journal of Mathematics 71 (1977), 275–294; https://msp.org/pjm/1977/71-2/pjm-v71-n2-p01-s.pdf .
