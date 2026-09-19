# A skewness–kurtosis phase diagram for flat signed Gaussian-chaos maxima

## Main result

Let \(p\to\infty\), \(L=\log p\), and let \(R=R_p\to\infty\). Choose signs
\(s_{1,R},\ldots,s_{R,R}\in\{-1,+1\}\), write
\[
\delta_R=\frac1R\sum_{i=1}^R s_{i,R}\in[-1,1],
\]
and for \(j=1,\ldots,p\) let
\[
Q_{j,R}=\frac1{\sqrt{2R}}\sum_{i=1}^R s_{i,R}(G_{ji}^2-1),
\qquad G_{ji}\stackrel{\rm iid}{\sim}N(0,1).
\]
The coordinates \(Q_{j,R}\) are independent, centered and variance one. Their flat signed spectrum has
\[
r_4=\frac{(\sum_i s_{i,R}^2)^2}{\sum_i s_{i,R}^4}=R,
\qquad
\kappa_3(Q_{j,R})=\frac{2\sqrt2\,\delta_R}{\sqrt R},
\qquad
\kappa_4(Q_{j,R})=\frac{12}{R}.
\]
Thus the fourth effective rank determines the fourth cumulant but does not record the sign imbalance \(\delta_R\), equivalently the third spectral moment.

Let
\[
M_{p,R}=\max_{j\le p}Q_{j,R},\qquad
M_p^G=\max_{j\le p}Z_j,
\quad Z_j\stackrel{\rm iid}{\sim}N(0,1),
\]
and let \(b_p=\Phi^{-1}(1-p^{-1})\), \(c_p=b_p^{-1}\). Suppose
\[
\frac{R}{L^{5/3}}\longrightarrow\infty.
\]
Define the signed Cramér correction
\[
\Theta_p=
\frac{4}{3}\,\delta_R\frac{L^{3/2}}{\sqrt R}
+(2-4\delta_R^2)\frac{L^2}{R}.
\]
If \(\Theta_p\to\theta\in\mathbb R\), then for every fixed \(x\),
\[
\boxed{
\Pr\!\left(\frac{M_{p,R}-b_p}{c_p}\le x\right)
\longrightarrow
\Lambda(x-\theta),
\qquad
\Lambda(x)=e^{-e^{-x}}.
}
\]
The Gaussian comparator satisfies
\[
\Pr\!\left(\frac{M_p^G-b_p}{c_p}\le x\right)\to\Lambda(x).
\]
Consequently, if \(\theta\ge0\),
\[
\boxed{
 d_K(M_{p,R},M_p^G)
 \longrightarrow
 D(\theta):=(1-e^{-\theta})
 \exp\!\left[-\frac{\theta}{e^\theta-1}\right],
}
\]
with the continuous convention \(D(0)=0\). If \(\Theta_p\to+\infty\), then
\[
\boxed{d_K(M_{p,R},M_p^G)\to1.}
\]
Thus the sharp extreme-value Gaussianization scale depends on the first nonzero Cramér correction, not on \(r_4\) alone.

### Two canonical regimes

If \(\delta_R\to\delta>0\), the cubic/skewness term dominates. Under the weaker standing condition \(R/L\to\infty\),
\[
R/L^3\to\infty \implies d_K(M_{p,R},M_p^G)\to0,
\]
while at the critical scale \(R/L^3\to c\in(0,\infty)\),
\[
\boxed{
\frac{M_{p,R}-b_p}{c_p}\Rightarrow \Lambda(\,\cdot-a_3\,),
\qquad
a_3=\frac{4\delta}{3\sqrt c},
}
\]
so \(d_K\to D(a_3)>0\). If \(R/L^3\to0\) but \(R/L\to\infty\), then \(d_K\to1\).

If the spectrum is exactly sign-balanced, \(R\) is even and \(\delta_R=0\), the cubic term vanishes and the quartic term is leading. Then
\[
R/L^2\to\infty \implies d_K(M_{p,R},M_p^G)\to0,
\]
whereas at \(R/L^2\to c\in(0,\infty)\),
\[
\boxed{
\frac{M_{p,R}-b_p}{c_p}\Rightarrow \Lambda(\,\cdot-a_4\,),
\qquad
a_4=\frac{2}{c},
}
\]
and \(d_K\to D(a_4)>0\). If \(R/L^2\to0\) but \(R/L\to\infty\), then \(d_K\to1\).

The crossover is visible directly in \(\Theta_p\): sign imbalance of order
\(\delta_R\asymp\sqrt{L/R}\) makes the cubic and quartic corrections comparable.

## Same-effective-rank separation

Take \(R_p\sim(\log p)^{5/2}\), rounded to a multiple of four. Consider two flat indefinite spectra with the same \(|\lambda_i|=1\), hence the same
\[
r_4=R_p,\qquad \kappa_4=12/R_p.
\]
For the first, take \(3R_p/4\) positive and \(R_p/4\) negative eigenvalues, so \(\delta_R=1/2\). For the second, take exactly \(R_p/2\) positive and \(R_p/2\) negative eigenvalues, so \(\delta_R=0\). Then
\[
\boxed{
 d_K(M_{p,R}^{\rm unbalanced},M_p^G)\to1,
 \qquad
 d_K(M_{p,R}^{\rm balanced},M_p^G)\to0.
}
\]
The two arrays have identical fourth effective rank and identical fourth cumulant at every \(p\), yet opposite Gaussianization behavior for their maxima. The distinguishing statistic is the third spectral moment: it is of order \(R^{-1/2}\) in the unbalanced family and exactly zero in the balanced family.

This does not contradict a sufficient effective-rank theorem. It shows instead that fourth effective rank cannot by itself be the *sharp* phase coordinate for signed quadratic-chaos maxima.

## Proof

For one coordinate, put
\[
Y_i=\frac{s_{i,R}(G_i^2-1)}{\sqrt2},
\qquad Q_R=R^{-1/2}\sum_{i=1}^R Y_i.
\]
The average cumulant generating function is exactly
\[
K_{\delta}(t)
=-\frac{\delta t}{\sqrt2}
-\frac{1+\delta}{4}\log(1-\sqrt2t)
-\frac{1-\delta}{4}\log(1+\sqrt2t).
\]
Around the origin,
\[
K_{\delta}(t)
=\frac{t^2}{2}+\frac{\sqrt2\delta}{3}t^3
+\frac12t^4+\frac{2\sqrt2\delta}{5}t^5+O(t^6).
\]
Let \(I_\delta(a)=\sup_t\{at-K_\delta(t)\}\). Solving \(K_\delta'(t)=a\) by power series and substituting gives
\[
\boxed{
I_\delta(a)
=\frac{a^2}{2}-\frac{\sqrt2\delta}{3}a^3
+(\delta^2-\tfrac12)a^4+O(a^5).
}
\]

A standard conjugate-measure argument gives the needed precise moderate deviation in this special analytic family. If \(x\to\infty\), \(x=o(\sqrt R)\), and \(t\) solves \(K_\delta'(t)=x/\sqrt R\), exponential tilting yields
\[
\Pr(Q_R>x)
=e^{-RI_\delta(x/\sqrt R)}
\mathbb E_t[e^{-\lambda W}\mathbf 1_{\{W\ge0\}}],
\]
where \(W\) is the centered tilted sum normalized to variance one and
\(\lambda=t\sqrt{RK_\delta''(t)}\). Since \(t\to0\), the tilted third absolute moments are uniformly bounded. Berry--Esseen under the tilted law, followed by integration by parts, therefore gives the usual saddlepoint prefactor with relative error \(o(1)\); comparing it with Mills' ratio gives, uniformly for \(x\asymp\sqrt L\),
\[
\boxed{
\log\frac{\Pr(Q_R>x)}{\bar\Phi(x)}
=
\frac{\sqrt2\delta_R}{3}\frac{x^3}{\sqrt R}
+\left(\frac12-\delta_R^2\right)\frac{x^4}{R}
+O\!\left(\frac{x^5}{R^{3/2}}+\frac{x}{\sqrt R}+x^{-2}\right).
}
\]
The displayed remainder is \(o(1)\) at the Gaussian extreme scale under \(R/L^{5/3}\to\infty\).

For \(x=b_p+c_py\) with fixed \(y\),
\[
p\bar\Phi(x)\to e^{-y},\qquad b_p\sim\sqrt{2L}.
\]
Substituting \(x\sim\sqrt{2L}\) in the preceding expansion gives
\[
\log\frac{\Pr(Q_R>x)}{\bar\Phi(x)}=\Theta_p+o(1).
\]
Hence, if \(\Theta_p\to\theta\),
\[
p\Pr(Q_R>b_p+c_py)\to e^{\theta-y},
\]
and independence of the \(p\) coordinates gives the shifted Gumbel limit. Continuous-limit convergence is uniform at the CDF level, so the Kolmogorov-distance limit is the supremum distance between \(\Lambda(x-\theta)\) and \(\Lambda(x)\). Maximizing
\(e^{-u}-e^{-e^\theta u}\) over \(u>0\) gives
\[
D(\theta)=(1-e^{-\theta})e^{-\theta/(e^\theta-1)}.
\]
If \(\Theta_p\to\infty\), evaluating the two maxima at a moving Gumbel coordinate of order \(\Theta_p/2=o(L)\) makes the Gaussian maximum CDF tend to one and the chaos-maximum CDF tend to zero, proving \(d_K\to1\). The two canonical regimes and the same-rank separation follow by substitution.

## Relation to recent and classical literature

Cai and Hu (2026, arXiv:2609.20529v1) introduce the fourth effective rank
\[
r_{4,j}=\frac{(\sum_r\lambda_{jr}^2)^2}{\sum_r\lambda_{jr}^4}
\]
for high-dimensional canonical order-two U-statistics and prove a general signed-chaos-to-Gaussian comparison. Their theorem gives the sufficient condition
\(r_{4,\min}/(\log p)^6\to\infty\) for Gaussianization of the chaos maximum, and they explicitly describe the resulting phase curve as schematic. The present calculation does not challenge that sufficient bound: it resolves a flat-spectrum benchmark sharply and shows that a single fourth-effective-rank scale cannot be necessary and sufficient across sign patterns.

The positive-flat specialization is a centered chi-square maximum. Gamma triangular-array maxima were studied by Bose, Dasgupta and Maulik (2008, arXiv:0803.3518), who for shape \(\alpha_n/\log n\to\infty\) obtained a Gumbel limit with an implicit Cramér-corrected centering. Expanding that centering already contains the cubic correction underlying the positive-skew branch above. More generally, Anderson, Coles and Hüsler (1997, DOI 10.1214/aoap/1043862420) developed Cramér-series methods for maxima of triangular arrays, and Cramér/Petrov moderate-deviation expansions are classical. Accordingly, the conjugate-measure method and the existence of cumulant corrections are not claimed as new.

The new claim is restricted to the explicit signed-flat specialization motivated by the 2026 effective-rank phase theorem: the two-term skewness--kurtosis correction \(\Theta_p\), the exact critical Kolmogorov gap, the \((\log p)^3\) versus \((\log p)^2\) sign-balance split, and especially the construction of two *indefinite* flat spectra with the same \(r_4\) and the same fourth cumulant but opposite maximum-Gaussianization limits. Searches did not locate these statements or an equivalent effective-rank counterexample.

## Verification

`artifacts/verify_flat_chaos.py` symbolically checks the rate-function expansion. It also evaluates the positive-flat maximum from the exact chi-square CDF and the balanced maximum from the exact Bessel density of a difference of two gamma variables. The accompanying output shows convergence toward the predicted critical Gumbel shifts. Numerical checks support the algebra and asymptotics but are not used in place of the proof.

## Limitations

The sharp phase diagram here is for independent coordinates and flat spectra with eigenvalues of common magnitude. It is not a general necessary-and-sufficient theorem for arbitrary spectra or cross-coordinate dependence. The two-term crossover statement assumes \(R/(\log p)^{5/3}\to\infty\); lower ranks can require higher Cramér-series terms. The conclusion concerns the Gaussian-chaos target itself, not the separate finite-sample approximation from a U-statistic to that target. The full text of Anderson--Coles--Hüsler (1997) was not inspected; its generic triangular-array Cramér theory is a concrete originality risk and may imply parts of the displayed expansion after specialization. Bose--Dasgupta--Maulik (2008) was inspected and already covers the positive gamma maximum with its own implicit centering. Originality is therefore asserted only to the best of our knowledge for the signed-flat phase synthesis and same-effective-rank separation.

## References

- L. Cai and Q. Hu, *Approximation Theorems for High-Dimensional Canonical U-Statistics: Gaussian Chaos and Phase Transition*, arXiv:2609.20529v1 (2026). https://arxiv.org/abs/2609.20529
- A. Bose, A. Dasgupta and K. Maulik, *Maxima of Dirichlet and triangular arrays of gamma variables*, Statistics & Probability Letters 78 (2008), 2811--2820. https://arxiv.org/abs/0803.3518
- C. W. Anderson, S. G. Coles and J. Hüsler, *Maxima of Poisson-like variables and related triangular arrays*, Annals of Applied Probability 7 (1997), 953--971. https://doi.org/10.1214/aoap/1043862420
- Y. Koike, *High-dimensional central limit theorems for homogeneous sums*, Journal of Theoretical Probability 36 (2023), 1--45. https://arxiv.org/abs/1902.03809
- L. V. Rozovsky, *On the Cramér series coefficients*, Theory of Probability and Its Applications 43 (1999), 152--157. https://doi.org/10.1137/S0040585X97976763
