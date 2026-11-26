# Sharp leading constants for independent tensorized Gaussian probes of rank at least two

## Finding

Let \(M\in\mathbb R^{m\times n}\) have rank \(r\ge2\) and nonzero singular values \(s_1,\dots,s_r\). Let \(\ell\ge1\) be an integer and let all vectors \(u_j\in\mathbb R^m, v_j\in\mathbb R^n\), \(1\le j\le\ell\), be mutually independent standard Gaussian vectors. Write
\[
F=\|M\|_F,\quad X_j=u_j^{\mathsf T}Mv_j,\quad
Q_\ell=\frac{\sqrt\ell F}{(\sum_{j=1}^\ell X_j^2)^{1/2}},\qquad
V_\ell=\frac{\pi^{\ell/2}}{\Gamma(1+\ell/2)}.
\]
For fixed \(M\) and \(\ell\), as \(\tau\to\infty\),
\[
\Pr(Q_\ell>\tau)\sim
V_\ell\ell^{\ell/2}\bigl(F f_M(0)\bigr)^\ell\tau^{-\ell},\qquad
f_M(0)=\frac1\pi\int_0^\infty\prod_{k=1}^r(1+s_k^2t^2)^{-1/2}\,dt.
\]
The inverse-moment boundary is exact: \(\mathbb E Q_\ell^p<\infty\) for \(p>0\) if and only if \(p<\ell\). Thus two probes suffice and are necessary for finite mean, and three suffice and are necessary for a finite second moment.

For fixed rank and Frobenius norm, the coefficient of \(\tau^{-\ell}\) is minimized precisely by matrices with equal nonzero singular values. Its exact minimum is
\[
V_\ell\ell^{\ell/2}\left[\frac{\sqrt r\,\Gamma((r-1)/2)}{2\sqrt\pi\,\Gamma(r/2)}\right]^\ell.
\]
This minimum exceeds the coefficient \(V_\ell(\ell/(2\pi))^{\ell/2}\) obtained using full independent standard Gaussian matrices as probes with the Frobenius inner product. The ratio of the minimum to the full Gaussian coefficient tends to one as \(r\to\infty\). At \(r=\ell=2\) the two coefficients are \(\pi\) and \(1\), respectively.

## Assumptions and scope

The result applies to a separable real residual \(h(z)=\phi(z)M\) with nonzero \(\phi\in L^2(\Omega)\) fixed independently of the validation probes. The factor \(\|\phi\|_{L^2}\) cancels in the norm ratio when the projected measurements are divided by \(\sqrt\ell\). This residual has operator stable rank one as a function of the spatial variable, irrespective of \(r\). The theorem is for independent probe pairs and fixed matrices; it does not establish a uniform asymptotic as a singular value tends to zero, a finite-threshold minimax comparison, or convergence guarantees for algorithms fitted with the validation probes. It is not a result about complex Gaussian probes or full crossed blocks.

## Proof

Orthogonal invariance and the SVD give \(X_j\stackrel{d}=\sum_k s_k G_{jk}H_{jk}\) with independent standard Gaussians. Conditioning on \(G_{jk}\) gives characteristic function \(\prod_k(1+s_k^2t^2)^{-1/2}\). The conditional variance is strictly positive almost surely, so there is no atom at zero. When \(r\ge2\) the characteristic function is integrable by its \(O(|t|^{-r})\) decay, and Fourier inversion yields a bounded continuous density with the strictly positive origin value above. The joint density for the \(\ell\) observations is the product of these densities. Rescaling the ball of radius \(\sqrt\ell F/\tau\) to the unit ball yields the claimed small-ball coefficient by continuity at the origin. The tail integral \(p\int_0^\infty \tau^{p-1}\Pr(Q_\ell>\tau)\,d\tau\) then gives the moment threshold; its part near zero is finite for every \(p>0\).

Put \(w_k=s_k^2/F^2\), so \(\sum w_k=1\). Changing variables gives \(Ff_M(0)=\pi^{-1}\int_0^\infty\prod_k(1+w_kt^2)^{-1/2}\,dt\). For \(t>0\), strict concavity of \(\log(1+wt^2)\) gives \(\sum_k\log(1+w_kt^2)\le r\log(1+t^2/r)\), with equality only at the flat spectrum. This minimizes the integrand and hence the integral. At that spectrum the substitution \(t=\sqrt r\,u\) and the beta integral for \(\int_0^\infty(1+u^2)^{-r/2}\,du\) give the stated gamma ratio. Also, \(\log(1+w_kt^2)<w_kt^2\) gives a strict lower bound \(e^{-t^2/2}\) for the integrand at every \(t>0\). Thus \(Ff_M(0)>1/\sqrt{2\pi}\), the origin density for a variance-one full Gaussian probe, and the ball argument gives the strict comparison. The gamma-ratio asymptotic gives convergence of the flat-spectrum answer to this Gaussian limit.

## Rank-one comparison (not a distinct claim)

At rank one, \(X_j/F\) is a product of two independent standard normals. Its density is \(K_0(|x|)/\pi=\pi^{-1}(\log(1/|x|)+O(1))\) near zero. The independent-row logarithmic asymptotic argument of [5], in its proof for the structured least-squares error, rescales the very same product density. For the validation ratio the radial cutoff is deterministic: setting \(X_j/F=\sqrt\ell\,y_j/\tau\) in the joint density integral over the unit ball gives pointwise convergence of the density product divided by \((\log\tau)^\ell\) to \(\pi^{-\ell}\) away from the coordinate planes. An integrable majorant is a constant times \(\prod_j(1+|\log|y_j||)\). This specialization yields
\[
\Pr(Q_\ell>\tau)\sim
\frac{\ell^{\ell/2}}{\pi^{\ell/2}\Gamma(1+\ell/2)}\,
\frac{(\log\tau)^\ell}{\tau^\ell},
\]
with the same moment boundary. The rank-one mechanism, radial coefficient computation and ensuing moment threshold are included for comparison, not credited as new here.

## Verification

The accompanying `verify.py` can be run with Python 3 and `scipy>=1.10`. It checks finite density and coefficient instances, including spectral imbalance, the full-Gaussian comparison, and small-radius Laplace and product-normal examples. These numerical checks supplement, but do not prove, the fixed-matrix asymptotic. For an exact check at \(M=I_2\), the scalar characteristic function is \((1+t^2)^{-1}\), giving the unit-scale Laplace law and hence the coefficient \(\pi\) at two probes.

## Relationship to prior work

Güttel, Kressner, and Vandereycken [1, §3.3 and Theorem 3.4] study tensorized sketching of matrix-valued functions and give a bound for one probe; the result here is a fixed-residual validation law, not a solution of their general multi-probe approximation problem. Bujanović and Kressner [2, Theorems 2.2 and 3.1] give nonasymptotic norm and trace bounds rather than exact leading coefficients and spectral minimizers. Shao and Nakatsukasa [3, Lemma 2.4 and Remark 2.5] already give the scalar real small-ball bounds and show that rank at least two removes the logarithmic loss. Their full crossed block in Theorem 2.7 contains a subset of independent diagonal probes, used in the proof; the full block reuses factors across entries, and is not the independent diagonal statistic evaluated here. Hu and Paouris [4, Theorem 1.1] give general bounds for projections of a simple random tensor rather than exact coefficients for independent copies of fixed bilinear measurements. The distinct content here is the exact rank-at-least-two law for those copies, with its spectrum-constrained sharp comparison and the resulting moment boundary for that observable.

## References

1. S. Güttel, D. Kressner, and B. Vandereycken, *Randomized sketching of nonlinear eigenvalue problems*, https://arxiv.org/abs/2211.12175.
2. Z. Bujanović and D. Kressner, *Norm and trace estimation with random rank-one vectors*, https://arxiv.org/abs/2004.06433.
3. N. Shao and Y. Nakatsukasa, *Convergence analysis of a nonlinear eigensolver based on rational approximation of the resolvent*, https://arxiv.org/abs/2607.10377.
4. F. Hu and G. Paouris, *Small Ball Probabilities for Simple Random Tensors*, https://arxiv.org/abs/2403.20192.
5. *Sharp inverse-moment thresholds and logarithmic tails for two Gaussian sketching models*, Resultary (2026-10-12), record `d93c1b8eb1d0`, proof paragraph “Independent tensor rows and exact logarithmic tail.”
