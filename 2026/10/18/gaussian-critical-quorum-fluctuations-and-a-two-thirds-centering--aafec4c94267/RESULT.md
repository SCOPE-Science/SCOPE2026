# Gaussian critical-quorum fluctuations and a two-thirds centering boundary

## Finding

For the harmonic Zipf weighted coupon collector, the centered quorum time has a universal Gaussian fluctuation scale and an additional sharp threshold in the accuracy of its explicit first-order centering. The model is defined below. Let \(A_N\) solve the exact deterministic mean equation in (1). For every fixed \(0<\theta<1\) and \(\lambda>0\),

\[
\sqrt{A_N}\left(\frac{\lambda\tau_{N,\theta}}{H_N A_N}-1\right)
\ \Longrightarrow\ \mathcal N(0,1/2).
\tag{2}
\]

Define \(K_\theta=\exp((\theta-2)\gamma)\) and \(B_N=K_\theta N^\theta\), where \(\gamma\) is Euler's constant. Then

\[
\frac{A_N}{B_N}-1=\frac{B_N}{N}
+O_\theta\!\left(B_N^{-1}+(B_N/N)^2+N^{-1}\right).
\tag{3}
\]

Consequently, the explicitly centered variable \(W_N=\sqrt{B_N}(\lambda\tau_{N,\theta}/(H_N B_N)-1)\) has the following *complete centering trichotomy*:

\[
\begin{cases}
W_N\Longrightarrow\mathcal N(0,1/2),&0<\theta<2/3,\\[2pt]
W_N\Longrightarrow\mathcal N(K_\theta^{3/2},1/2),&\theta=2/3,\\[2pt]
W_N\longrightarrow+\infty\text{ in probability},&2/3<\theta<1.
\end{cases}
\tag{4}
\]

In particular, the same first-order law has a nontrivial *shifted Gaussian* transition exactly when the first finite-catalogue correction is as large as the random fluctuation.

## Assumptions and scope

Fix \(\theta\in(0,1)\) and a total arrival rate \(\lambda>0\). For each integer \(N\ge2\), let \(H_N=\sum_{i=1}^N i^{-1}\). Type \(i\) is independently first discovered at time \(T_i\sim\operatorname{Exp}(\lambda/(iH_N))\); every type has quorum weight \(1/(iH_N)\). Define

\[
\tau_{N,\theta}=\inf\left\{t\ge0:\sum_{i=1}^N\frac{{\mathbf1}_{\{T_i\le t\}}}{iH_N}>\theta\right\}.
\]

All clocks are independent and \(\theta,\lambda\) do not vary with \(N\). Define \(F_N(A)=\sum_{i=1}^N (1-e^{-A/i})/i\). It is continuous and strictly increasing from zero to \(H_N\); hence there is a unique \(A_N>0\) with

\[
F_N(A_N)=\theta H_N.\tag{1}
\]

The primary mathematical assertion is the fluctuation law (2) together with the exact-root/external-centering distinction (3)-(4). The first-order constant \(K_\theta\) itself is established prior work.

## Proof

**1. A sharp deterministic root expansion.** Introduce \(F_\infty(A)=\sum_{i\ge1}(1-e^{-A/i})/i\), which converges for fixed \(A>0\). Differentiation for \(A>0\) gives

\[
F_\infty'(A)=\sum_{i\ge1}\frac{e^{-A/i}}{i^2}.
\]

The integral over the positive axis of \(f_A(x)=e^{-A/x}/x^2\) is \(1/A\). The function \(f_A\) increases to its unique maximum at \(x=A/2\) and then decreases; its total variation is \(O(A^{-2})\). Comparing the sum with the integral therefore yields \(F_\infty'(A)=A^{-1}+O(A^{-2})\).

To identify the additive constant, split \(F_\infty(A)\) at \(i=\lfloor A\rfloor\) and compare the two remainder sums with integrals. Their difference tends to

\[
-\int_1^\infty \frac{e^{-u}}{u}\,du
+\int_0^1\frac{1-e^{-u}}{u}\,du=\gamma.
\]

Together with \(H_{\lfloor A\rfloor}=\log A+\gamma+o(1)\), this gives the constant \(2\gamma\). Integrating the derivative error sharpens it to

\[
F_\infty(A)=\log A+2\gamma+O(A^{-1}).\tag{5}
\]

For \(A/N\to0\), Taylor's theorem and the two convergent power tails give

\[
\sum_{i>N}\frac{1-e^{-A/i}}{i}
=\frac{A}{N}+O\!\left(\frac{A}{N^2}+\frac{A^2}{N^2}\right).
\]

Thus, uniformly for \(A\to\infty\) with \(A/N\to0\),

\[
F_N(A)=\log A+2\gamma-\frac{A}{N}
+O\!\left(A^{-1}+A/N^2+(A/N)^2\right).\tag{6}
\]

Use \(H_N=\log N+\gamma+O(N^{-1})\) in equation (1), first with fixed multiples of \(B_N=K_\theta N^\theta\), to see that \(A_N/B_N\to1\). Subtract the equation at \(B_N\) from the equation at \(A_N\) using (6), expand the logarithm, and absorb the error terms. This proves (3), including its positive leading coefficient.

**2. Variance and a triangular-array central limit theorem.** At operational time \(A=\lambda t/H_N\), write \(S_N(A)=\sum_{i=1}^N i^{-1}{\mathbf1}_{\{T_i\le H_N A/\lambda\}}\). Its mean is \(F_N(A)\) and its variance is

\[
V_N(A)=\sum_{i=1}^N\frac{e^{-A/i}(1-e^{-A/i})}{i^2}.
\]

Equation (5) at \(A\) and \(2A\), after differentiation, implies

\[
V_N(A)=\frac{1}{2A}+O(A^{-2}+A/N^2),\tag{7}
\]

provided \(A\to\infty\) and \(A/N\to0\). In particular, \(AV_N(A)\to1/2\). The centered weighted indicators form an independent triangular array. To verify Lindeberg at scale \(\sqrt A\), fix \(\varepsilon>0\). Terms with \(i>\sqrt A/\varepsilon\) have absolute centered scaled contribution at most \(\varepsilon\). For \(i\le\sqrt A/\varepsilon\), an unobserved type has probability at most \(e^{-\varepsilon\sqrt A}\), and the sum of their rescaled variances is bounded by \(A\sum_{i\ge1}i^{-2}e^{-\varepsilon\sqrt A}\to0\). Thus, along any sequence \(A\asymp N^\theta\),

\[
\sqrt A\bigl(S_N(A)-F_N(A)\bigr)\Longrightarrow\mathcal N(0,1/2).\tag{8}
\]

**3. Inversion at the random stopping time.** The derivative estimate also yields \(AF_N'(A)\to1\) for \(A\asymp N^\theta\). For fixed \(h\in\mathbb R\), set \(A=A_N(1+h/\sqrt{A_N})\). Taylor's theorem gives

\[
\sqrt{A_N}\,[F_N(A)-\theta H_N]\longrightarrow h.
\]

The event \(\{\lambda\tau_{N,\theta}/H_N\le A\}\) is exactly \(\{S_N(A)>\theta H_N\}\), including possible equality of the total weight and the threshold, because the stopping rule is strict. Apply (8) at \(A\) to obtain the distribution-function limit \(\Phi(\sqrt2 h)\), where \(\Phi\) denotes the standard-normal CDF. This proves (2).

**4. The two-thirds boundary.** Let \(B_N=K_\theta N^\theta\). Rearranging the definition of \(W_N\) gives

\[
W_N=\sqrt{B_N}\left(\frac{A_N}{B_N}-1\right)
+\sqrt{\frac{A_N}{B_N}}\sqrt{A_N}\left(\frac{\lambda\tau_{N,\theta}}{H_N A_N}-1\right).
\]

The second term converges to \(\mathcal N(0,1/2)\). By (3), the first term is

\[
\frac{B_N^{3/2}}{N}\,(1+o(1))
=K_\theta^{3/2}N^{3\theta/2-1}(1+o(1)).
\]

It vanishes below \(\theta=2/3\), tends to \(K_\theta^{3/2}\) at equality, and diverges to positive infinity above equality. Slutsky's theorem proves (4).

## Verification

Run `python3 verification/verify_critical_zipf.py` from the package root. Its standard-library-only code solves the actual finite mean equation, evaluates both exact finite variance and mean derivative, compares deterministic-root shifts to the finite-catalogue asymptotic, and independently simulates first-arrival order statistics. Finite numerical checks are supporting evidence, not proofs of (2)-(4). The infinite-array Lindeberg condition, sharp expansion (6), and stopping-time inversion above establish the universal statements.

## Relationship to prior work

Müller and Šebek, *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1, Section 6, establish the harmonic critical first-order normalization \(K_\theta H_N N^\theta/\lambda\) and a variance **upper bound** for the discovered mass. Their final discussion explicitly lists next-order behavior and critical fluctuation theory as an open direction. Here their first-order constant is an input to a Gaussian fluctuation theorem and a new \(2/3\) centering classification; the variance constant, inversion, and finite-size bias are separately proved.

Chebunin and Zuyev, *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability 35 (2022), treat **fixed summable infinite-urn frequencies** under regular-variation assumptions. Their general Gaussian machinery provides conceptual background but does not state the finite-triangular harmonic profile, its inverse quorum time, or its \(2/3\) finite-catalogue centering boundary. Standard Lindeberg-Feller and inverse-distribution arguments themselves are not claimed as new.

## Limitations

The threshold \(\theta\) is fixed strictly between zero and one, the exponent is exactly the harmonic critical value, first-arrival clocks are independent, and arrival-rate and quorum-weight profiles coincide. Results do not assert convergence in a moving-threshold window, under dependent clocks, or for generic regularly varying profiles. The explicitly centered fluctuation variable diverges at \(\theta>2/3\); the exact-root-centered normal law remains valid there. An independent priority assessment is still necessary; this result does not claim priority over unidentified general occupancy limit theorems.

## References

1. S. Müller and S. Šebek (2026), *Weighted-threshold Coupon Collection*, arXiv:2607.08551v1, especially Sections 2, 3, 6 and 9. https://arxiv.org/abs/2607.08551
2. M. Chebunin and S. Zuyev (2022), *Functional Central Limit Theorems for Occupancies and Missing Mass Process in Infinite Urn Models*, Journal of Theoretical Probability 35, 1–19, DOI:10.1007/s10959-020-01053-6. https://doi.org/10.1007/s10959-020-01053-6
3. S. Karlin (1967/1968), *Central Limit Theorems for Certain Infinite Urn Schemes*, Indiana University Mathematics Journal 17, 373–401, DOI:10.1512/iumj.1968.17.17020 (historical background, not asserted to have a covering theorem).
