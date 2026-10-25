# A single-logarithm small-ball lower bound for the Kloosterman process

## Finding
For \(L\ge 1\), there is a constant \(C_L>0\) such that for every target \(g\) specified below, and every \(0<\varepsilon\le1/4\),
\[\mathbb P(\|K-g\|_\infty<\varepsilon)\ge\exp\{-C_L\varepsilon^{-2}\log(2/\varepsilon)\}.\]
The estimate removes one logarithm from Theorem 1.2 of Kyselov (2026), without changing the target class.

## Assumptions and scope
Put \(e(u)=\exp(2\pi iu)\) and let \((X_h)_{h\in\mathbb Z}\) be mutually independent real variables of the Sato--Tate law with density \(\rho(x)=\sqrt{4-x^2}/(2\pi)\) for \(|x|\le2\) and zero otherwise. Define the almost surely uniformly convergent Fourier process
\[K(t)=tX_0+\sum_{h\ne0}\frac{e(ht)-1}{2\pi ih}X_h,\qquad0\le t\le1.\]
The continuous target \(g:[0,1]\to\mathbb C\) satisfies \(g(0)=g(1)=0\),
\[|g(t)-g(s)|\le L|t-s|^{1/2},\qquad \beta_h:=2\pi i h\widehat g(h)\in[-1,1]\ (h\ne0),\]
where \(\widehat g(h)=\int_0^1g(t)e(-ht)\,dt\). The density condition is only used inside the fixed compact interval \([-5/4,5/4]\). Constants are uniform over all such targets for a fixed \(L\).

## Proof
**Step 1: deterministic approximation and independent tail.** Fix \(\varepsilon\) and set \(\ell=\log(2/\varepsilon)\). Choose \(M=\lceil A_L\varepsilon^{-2}\ell\rceil\), where \(A_L\) is sufficiently large. Set \(b_h=(1-|h|/(M+1))\beta_h\) for \(0<|h|\le M\) and
\[q_M(t)=\sum_{0<|h|\le M}\frac{e(ht)-1}{2\pi ih}b_h.\]
By the Fejér-kernel argument for \(1/2\)-Hölder periodic functions, \(\|q_M-g\|_\infty\le cL/\sqrt M<\varepsilon/6\). Indeed, \(q_M=\sigma_Mg-\sigma_Mg(0)\); the kernel bound \(F_M(u)\ll\min(M,(Mu^2)^{-1})\), integrated against \(L\sqrt{|u|}\), proves this inequality. For the independent upper-frequency tail \(R_M\), the centered bounded-coefficient dyadic maximal estimate gives
\[\mathbb E\|R_M\|_\infty\le c\sqrt{\log(2M)/M}<\varepsilon/12.\]
To reconstruct this estimate, in any block \(H<|h|\le2H\) apply Hoeffding to real and imaginary parts on a grid of \(O(H)\) points and use the Bernstein derivative inequality for degree-\(2H\) trigonometric polynomials. The block's expected supremum is \(O(\sqrt{\log(2H)/H})\), and summing geometric blocks yields the display. Markov then gives \(\mathbb P(\|R_M\|_\infty<\varepsilon/3)\ge3/4\). The tail is independent of the remaining events.

**Step 2: a centered conditional window.** There are absolute constants \(d\in(0,1/8)\) and \(c_0>0\) such that for each \(b\in[-1,1]\) and \(0<\delta\le d\) there is an interval \(I(b,\delta)\subset[b-\delta,b+\delta]\) of length \(\delta\) for which
\[\mathbb E[X\mid X\in I(b,\delta)]=b,\quad\mathbb P(X\in I(b,\delta))\ge c_0\delta,\quad |X-b|\le\delta\text{ on }I.\]
Indeed, slide the length-\(\delta\) interval continuously from \([b-\delta,b]\) to \([b,b+\delta]\). Its conditional mean moves continuously from strictly below \(b\) to strictly above \(b\); the intermediate-value theorem supplies the required center. The Sato--Tate density has a positive lower bound on \([-5/4,5/4]\), proving its mass estimate. Conditional laws of different coefficients remain independent.

**Step 3: geometric windows and a low-frequency random sum.** Put \(J=\lceil\log_2M\rceil\), set \(\delta_j=d\,2^{-3(J-j)/4}\) for \(0\le j\le J\), and partition \(0<|h|\le M\) into blocks \(B_0=\{h:|h|=1\}\) and \(B_j=\{h:2^{j-1}<|h|\le\min(2^j,M)\}\) for \(1\le j\le J\). Condition on
\[E=\bigcap_{j=0}^J\bigcap_{h\in B_j}\{X_h\in I(b_h,\delta_j)\}.\]
Under this conditioning, \(Y_h=X_h-b_h\) are independent, centered, and satisfy \(|Y_h|\le\delta_j\) for \(h\in B_j\). The small-ball cost is
\[-\log\mathbb P(E)\le\sum_{j=0}^J|B_j|\log\frac1{c_0\delta_j}\le C\sum_{j=0}^J2^j(1+J-j)\le C'2^J\le 2C'M.\]
Here \(\sum_{r\ge0}2^{-r}(1+r)<\infty\) is essential; a uniform shrinking window would instead cost \(M\log M\).

Write the conditional error process as \(Z=\sum_jZ_j\),
\[Z_j(t)=\sum_{h\in B_j}\frac{e(ht)-1}{2\pi ih}Y_h.\]
For each fixed \(j\), Hoeffding's inequality for the centered real variables on a trigonometric grid of \(O(2^j)\) points, combined with Bernstein's inequality, gives
\[\mathbb E(\|Z_j\|_\infty\mid E)\le C\delta_j\sqrt{\frac{j+1}{2^j}}.\]
The bound also holds for \(j=0\) after increasing \(C\). In detail, each pointwise complex sum has real/imaginary subgaussian variance proxy at most \(C\delta_j^2/2^j\); a grid union bound and integration yield \(C\delta_j\sqrt{(j+1)/2^j}\), while the \(-1\) in the numerator multiplies the supremum by at most two. Summing the blocks,
\[\begin{aligned}\mathbb E(\|Z\|_\infty\mid E)&\le Cd\sum_{j=0}^J2^{-3(J-j)/4}\sqrt{\frac{j+1}{2^j}}\\&\le C'd\sqrt{\frac{J+1}{2^J}}\sum_{r=0}^\infty2^{-r/4}\\&\le C''d\sqrt{\frac{\log(2M)}{M}}<\varepsilon/12,\end{aligned}\]
by enlarging \(A_L\). Therefore \(\mathbb P(\|Z\|_\infty<\varepsilon/3\mid E)\ge3/4\).

**Step 4: conclude.** Independently require \(|X_0|<\varepsilon/6\), an event of probability at least \(c\varepsilon\), and \(\|R_M\|_\infty<\varepsilon/3\). On their intersection with \(E\) and \(\|Z\|_\infty<\varepsilon/3\), the triangle inequality yields
\[\|K-g\|_\infty<\varepsilon/6+\varepsilon/6+\varepsilon/3+\varepsilon/3=\varepsilon.\]
The events use disjoint coefficients except that \(E\) and the low-frequency norm share coefficients, for which the conditional probability was calculated. Hence
\[\mathbb P(\|K-g\|_\infty<\varepsilon)\ge c'\varepsilon\exp(-C M)\ge\exp(-C_L\varepsilon^{-2}\log(2/\varepsilon)),\]
where the last inequality uses \(M\le C_L\varepsilon^{-2}\log(2/\varepsilon)\) and absorbs \(\log(1/\varepsilon)\). This proves the assertion for every stated target and every \(\varepsilon\) in range.

## Verification
The conditional-window lemma was checked directly by the continuity and sign of conditional means on the two endpoint intervals. The dyadic-cost sum and dyadic-subgaussian sum were independently reduced to convergent geometric series. Exact coefficient normalization, the separate zero frequency, and the independence of the tail were accounted for. The proof is analytic; no finite computation is used to certify an infinite claim. The tail/Fejér bounds are reproduced from the explicit arguments in Kyselov's Section 4 and follow from the cited classical inequalities.

## Relationship to prior work
Kyselov, *Space-filling curves and small-ball probabilities for the Kloosterman process*, arXiv:2610.22645v1 (first public October 15, 2026), Theorem 1.2, proves a bound with \(\varepsilon^{-2}\log^2(2/\varepsilon)\). Its proof uniformly pins all low-frequency coefficients within a tolerance of order \(\varepsilon/\log M\), which incurs \(M\log M\) in logarithmic probability. The present result instead centers each conditional coefficient and allocates errors by dyadic scale, retaining subgaussian cancellation. The 2017 Kowalski--Sawin support theorem gives qualitative support rather than the present uniform numerical lower bound. Targeted searches did not identify an earlier result implying the stated single-logarithm estimate.

## Limitations
This is a lower bound, not a matching small-ball asymptotic or an optimality theorem. It uses a fixed strict interior margin \(\beta_h\in[-1,1]\) within the Sato--Tate support; endpoints \(\pm2\) are outside the proof. The constant depends on the Hölder constant \(L\). A broader pre-existing small-deviation theorem might implicitly imply the estimate; this literature risk is not eliminated.

## References
1. D. Kyselov, *Space-filling curves and small-ball probabilities for the Kloosterman process*, arXiv:2610.22645v1, October 15, 2026, especially Theorem 1.2, Lemma 4.1 and Remark 4.2, https://arxiv.org/html/2610.22645v1.
2. E. Kowalski and W. Sawin, *On the support of the Kloosterman paths*, arXiv:1709.05192, 2017, https://arxiv.org/abs/1709.05192.
3. W. Hoeffding, *Probability inequalities for sums of bounded random variables*, Journal of the American Statistical Association 58 (1963), 13–30 (classical concentration inequality).
