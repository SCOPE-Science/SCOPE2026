# Gaussian threshold and lattice transition for bounded-exponent Robin truncations

## Finding
For every integer \(r\ge1\), let \(\mathcal N_r=\{n\ge1:p^{r+1}\nmid n\text{ for every prime }p\}\). For sufficiently large \(n\), write \(x(n)=\log\log\log n\), and for fixed real \(c\), set
\[
K_c(n)=\lfloor x(n)+c\sqrt{x(n)}\rfloor,\qquad B_c(n)=e^\gamma\sum_{j=0}^{K_c(n)}\frac{x(n)^j}{j!}.
\]
Let \(\Phi\) be the standard normal distribution function, \(\lambda_r=\zeta(r+1)^{-1}\), and \(c_r=\Phi^{-1}(\lambda_r)\). Then
\[
\limsup_{\substack{n\to\infty\\n\in\mathcal N_r}}\frac{\sigma(n)}{nB_c(n)}=\frac{\lambda_r}{\Phi(c)}.
\]
Consequently, the strict truncated Robin-type inequality \(\sigma(n)/n<B_c(n)\) holds for all sufficiently large \(n\in\mathcal N_r\) if \(c>c_r\), while for \(c<c_r\) it fails for every sufficiently large term of the sequence \(N_{r,k}=(p_1p_2\cdots p_k)^r\).

The boundary \(c=c_r\) has a further exact distinction **on these extremal numbers**. Define \(H_r=(4-c_r^2)/6\), \(y_{r,k}=x(N_{r,k})+c_r\sqrt{x(N_{r,k})}\), and \(f_{r,k}=\{y_{r,k}\}\). Uniformly as \(k\to\infty\),
\[
\frac{B_{c_r}(N_{r,k})-\sigma(N_{r,k})/N_{r,k}}{e^\gamma\log\log N_{r,k}}
=\frac{\phi(c_r)}{\sqrt{x(N_{r,k})}}\bigl(H_r-f_{r,k}\bigr)+O_r\!\left(\frac1{x(N_{r,k})}\right).
\]
For \(1\le r\le4\), both strict inequality and strict reverse inequality occur along infinitely many \(N_{r,k}\). For \(r\ge5\), the strict reverse inequality occurs at every sufficiently large \(N_{r,k}\). This boundary statement makes no claim of universal eventual validity on \(\mathcal N_r\) when \(c=c_r\).

## Assumptions and scope
All logarithms are natural; \(n\) is a positive integer tending to infinity inside the \((r+1)\)-power-free class. \(p_i\) is the \(i\)th prime and \(\sigma\) the sum-of-divisors function. The truncated sum is considered only where \(x(n)>0\) and \(K_c(n)\ge0\), automatically true sufficiently far out. \(\phi(t)=e^{-t^2/2}/\sqrt{2\pi}\), \(\{t\}=t-\lfloor t\rfloor\). Each limit fixes \(r,c\) before allowing \(n\to\infty\). No assertion is made about arbitrary integers with unbounded prime exponents.

## Proof
**1. Sharp restricted Gronwall constant.** Write \(P_k=\prod_{i=1}^kp_i\). For \(n\in\mathcal N_r\) with \(\omega(n)=k\), the multiplicative local factor \(\sum_{j=0}^{a}p^{-j}\) increases in \(a\le r\) and decreases in \(p\). Therefore
\[
\frac{\sigma(n)}n\le F_r(k):=\prod_{i=1}^k\frac{1-p_i^{-(r+1)}}{1-p_i^{-1}},\qquad n\ge P_k.
\]
Mertens' product theorem, the convergence of the Euler product \(\prod_p(1-p^{-(r+1)})=\lambda_r\), and the prime number theorem give
\[
F_r(k)=(\lambda_r+o(1))e^\gamma\log p_k,
\qquad \log\log P_k\sim\log p_k.
\]
If \(k=\omega(n)\) stays bounded, \(\sigma(n)/n\) is bounded, so its ratio to \(e^\gamma\log\log n\) vanishes. Otherwise the preceding upper bound applies, using \(n\ge P_k\). Equality in the limit is attained along \(N_{r,k}=P_k^r\) because its normalized divisor sum is exactly \(F_r(k)\) and \(\log\log N_{r,k}=\log(r\vartheta(p_k))\sim\log p_k\). Thus
\[
\limsup_{\substack{n\to\infty\\n\in\mathcal N_r}}\frac{\sigma(n)}{ne^\gamma\log\log n}=\lambda_r.
\]

**2. Optimal Gaussian scale.** If \(Y_x\) is Poisson with mean \(x\), then
\[
\frac{B_c(n)}{e^\gamma\log\log n}=e^{-x}\sum_{j=0}^{\lfloor x+c\sqrt x\rfloor}\frac{x^j}{j!}
=\Pr(Y_x\le x+c\sqrt{x})\longrightarrow\Phi(c)
\]
by the Poisson central limit theorem. Since \(\Phi(c)>0\), divide the restricted Gronwall limsup by this convergent factor. Its strict comparison with \(1\) yields the two open critical ranges; the reverse direction already holds along \(N_{r,k}\).

**3. The first lattice correction.** Stirling's expansion for the Poisson point mass, followed by Euler--Maclaurin summation (including a half-endpoint mass), gives, for each fixed real \(c\),
\[
\Pr(Y_x\le\lfloor x+c\sqrt{x}\rfloor)=\Phi(c)+\frac{\phi(c)}{\sqrt x}
\left[\frac12+\frac{1-c^2}{6}-\{x+c\sqrt x\}\right]+O_c(x^{-1}).\tag{1}
\]
For completeness, in the centered coordinate \(t=(j-x)/\sqrt{x}\), Stirling gives the mass \(\phi(t)x^{-1/2}[1+(t^3-3t)/(6\sqrt{x})]+O(x^{-3/2}(1+|t|^8)e^{-t^2/4})\) in the central region. Sum over lattice mesh \(x^{-1/2}\), bound tails by standard Poisson Chernoff bounds, and use \(\int_{-\infty}^c(t^3-3t)\phi(t)\,dt=(1-c^2)\phi(c)\). The endpoint correction and the fractional-part shift combine to \(1/2-\{x+c\sqrt{x}\}\), proving (1) with a uniform bounded-remainder constant for fixed \(c\).

On \(N_{r,k}\), the effective prime number theorem and the quantitative Mertens estimate give
\[
\frac{\sigma(N_{r,k})/N_{r,k}}{e^\gamma\log\log N_{r,k}}=\lambda_r+O_r\bigl(1/\log p_k\bigr)
=\lambda_r+o\bigl(x(N_{r,k})^{-1/2}\bigr).
\]
In fact this error is \(O_r(x^{-1})\): \(x=\log\log(r\vartheta(p_k))\), so \(\log p_k\) grows exponentially in \(x\); the effective PNT/Mertens remainder is smaller still. Subtract from (1) at \(c=c_r\), where \(\Phi(c_r)=\lambda_r\), obtaining the displayed boundary asymptotic.

**4. The cutoff at exponent four.** The sequence \(c_r\) increases strictly with \(r\). The elementary Mills inequalities \(\frac{2}{5}\phi(2)<1-\Phi(2)<\frac12\phi(2)\), together with \(1/20<\phi(2)<3/50\), show \(0.97<\Phi(2)<0.98\). On one side, \(\lambda_4=1/\zeta(5)<32/33<0.97\); on the other, \(\zeta(6)<51/50\), so \(\lambda_5>50/51>0.98\). Hence \(c_r<2\) for \(r\le4\) and \(c_r>2\) for \(r\ge5\). This proves \(0<H_r<1\) for the former and \(H_r<0\) for the latter.

Finally \(y_{r,k}\) increases without bound, and \(y_{r,k+1}-y_{r,k}\to0\): \(\log N_{r,k}=r\vartheta(p_k)\), successive log-increments are \(r\log p_{k+1}\), and \(\vartheta(p_k)\asymp p_k\). Every subinterval of \((0,1)\) therefore contains fractional parts \(\{y_{r,k}\}\) for infinitely many \(k\). For \(r\le4\), choose fractional parts strictly below or above \(H_r\) and apply the uniform remainder in the boundary asymptotic. For \(r\ge5\), the main term is strictly negative for every fractional part, giving eventual failure along the extremal sequence. This completes the proof.

## Verification
Run `python3 verify.py` using only the Python standard library. It independently checks the normalized primorial divisor products against their predicted limits, the lattice first-order Poisson correction at several nonintegral phases, the transition \(c_4<2<c_5\), and the vanishing mesh of the extremal sequence. The script is supplementary: it does not prove the uniform estimates or the infinite assertions.

## Relationship to prior work
Mishra and Sarkar, arXiv:2609.26787v1 (2026-09-22), prove a finite truncated-exponential arithmetic form of Robin's inequality with cutoff tied to \(\omega(n)\), including an unconditional squarefree case, and explicitly discuss reducing the truncation order. The present theorem instead determines a sharp *moving Gaussian cutoff* within each bounded-exponent class, including a critical lattice transition absent from their stated results. The restricted divisor-sum extremum uses classical Mertens/PNT estimates, while the Gaussian and lattice terms derive from classical Poisson asymptotics. Lagarias, arXiv:math/0008177v2, surveys Robin's inequality and Gronwall's theorem; neither source supplies the combined transition statement. The ingredients are classical, so other equivalent prior syntheses remain possible.

## Limitations
The statement is asymptotic; no explicit all-index cutoff is claimed. At the critical value, the classification applies only to the extremal primorial powers; it does not determine which other bounded-exponent integers satisfy the inequality. The first lattice correction requires standard quantitative prime number theorem/Mertens estimates and the Poisson local expansion, each stated and used explicitly above. No Riemann-hypothesis assumption or independence claim is involved.

## References
1. C. Mishra and R. Sarkar, *A finite arithmetic form of Robin's inequality and its equivalence to the Riemann hypothesis*, arXiv:2609.26787v1, first posted 2026-09-22, https://arxiv.org/abs/2609.26787.
2. J. C. Lagarias, *An Elementary Problem Equivalent to the Riemann Hypothesis*, arXiv:math/0008177v2, https://arxiv.org/abs/math/0008177.
3. F. Mertens, classical product theorem for primes; prime number theorem and standard effective estimates.
4. Classical Stirling, Poisson central-limit and local Edgeworth expansions (the first correction is derived in the proof).
