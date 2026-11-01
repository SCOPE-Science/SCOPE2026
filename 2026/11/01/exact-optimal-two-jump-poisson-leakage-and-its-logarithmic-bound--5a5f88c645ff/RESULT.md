# Exact optimal two-jump Poisson leakage and its logarithmic boundary law

## Finding

For each integer \(N\ge1\), every \(0\le\rho<1\), and every \(0<\ell<2\pi\), let \(\Phi_{N,\ell}(e^{i\theta})\) equal \(+1\) when \(N\theta\pmod{2\pi}\in[0,\ell)\), and \(-1\) otherwise. Let \(\mathcal P_\rho\) be the Poisson convolution on the circle, with kernel \(K_\rho(t)=(1-\rho^2)/(1-2\rho\cos t+\rho^2)\) and normalization \(dt/(2\pi)\). Define the **unnormalized** boundary defect
\[
E_{N,\rho}(\ell)=\int_0^{2\pi}|\Phi_{N,\ell}(e^{i\theta})-(\mathcal P_\rho\Phi_{N,\ell})(e^{i\theta})|\,d\theta.
\]
Then \(E_{N,\rho}(\ell)=E_{1,\rho^N}(\ell)\) and its exact second derivative is
\[
\frac{d^2}{d\ell^2}E_{N,\rho}(\ell)=-\frac4\pi K_{\rho^N}(\ell)<0.
\]
Consequently the **unique** maximizing proportion is \(\ell=\pi\). Its sharp value for every \(N\) and \(\rho\) is
\[
\max_{0\le\ell\le2\pi} E_{N,\rho}(\ell)=2\pi-\frac8\pi\bigl(\operatorname{Li}_2(\rho^N)-\operatorname{Li}_2(-\rho^N)\bigr),
\]
where \(\operatorname{Li}_2(w)=\sum_{j\ge1}w^j/j^2\) for \(|w|\le1\). Equality occurs only at a half-circle per period, up to rotations and null-set changes. More quantitatively,
\[
E_{N,\rho}(\pi)-E_{N,\rho}(\ell)\ge\frac2\pi\frac{1-\rho^N}{1+\rho^N}(\ell-\pi)^2,
\]
with a **best possible** quadratic coefficient, witnessed by \(\ell\to\pi\). For \(\varepsilon=1-\rho\downarrow0\) and integers \(N=N(\varepsilon)\ge1\) such that \(N\varepsilon\to0\),
\[
E_{N,\rho}(\pi)\sim\frac8\pi N\varepsilon\log\frac1{N\varepsilon}.
\]
In particular, this is an exact leading constant for the sign-wave Poisson defect used in the cited recent Hardy–Littlewood equivalence argument.

## Assumptions and scope

Angles use Lebesgue arc length in radians on \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\). The kernel is normalized by \((2\pi)^{-1}\int_0^{2\pi}K_\rho(t)dt=1\). Values at jumps are immaterial. The case \(\rho=0\) is included, while \(\rho=1\) is not (its identity-operator defect is zero). The equal-arc optimizer is asserted only in this periodic two-jump-per-cell binary family, not among arbitrary measurable or multi-jump traces.

## Proof

**Step 1: Scaling.** The Fourier coefficients of \(F(N\theta)\) are supported at multiples of \(N\), with coefficient \(\widehat F(k)\) at frequency \(Nk\). The Poisson multiplier is \(\rho^{|Nk|}\), so \(\mathcal P_\rho[F(N\cdot)](\theta)=(\mathcal P_{\rho^N}F)(N\theta)\). By periodicity and change of variables, the unnormalized \(L^1\) defect is invariant under this frequency rescaling. It suffices to analyze \(N=1\) with \(\lambda=\rho^N\).

**Step 2: Exact arc leakage and concavity.** Put \(A=[0,\ell)\subset\mathbb T\) and \(F=2\mathbf1_A-1\). Since \(\mathcal P_\lambda F\in[-1,1]\), the absolute-value signs can be removed separately on \(A\) and \(A^c\). By Fubini and symmetry,
\[
E_{1,\lambda}(\ell)=\frac2\pi\int_A\int_{A^c}K_\lambda(x-y)\,dy\,dx
=4\ell-\frac4\pi\int_0^\ell(\ell-t)K_\lambda(t)\,dt.
\]
The last identity follows by representing \(\int_A\int_A K_\lambda(x-y)dydx=2\int_0^\ell(\ell-t)K_\lambda(t)dt\) and using \(\int_\mathbb T K_\lambda=2\pi\). Differentiation gives
\[
E'_{1,\lambda}(\ell)=4-\frac4\pi\int_0^\ell K_\lambda(t)dt,
\qquad E''_{1,\lambda}(\ell)=-\frac4\pi K_\lambda(\ell)<0.
\]
Evenness and total mass imply \(\int_0^\pi K_\lambda(t)dt=\pi\), so \(\ell=\pi\) is the unique maximum. Since \(K_\lambda(t)\ge K_\lambda(\pi)=(1-\lambda)/(1+\lambda)\) everywhere,
\[
E_{1,\lambda}(\pi)-E_{1,\lambda}(\ell)=\frac4\pi\int_0^{|\ell-\pi|}(|\ell-\pi|-u)K_\lambda(\pi+u)du
\ge\frac2\pi\frac{1-\lambda}{1+\lambda}(\ell-\pi)^2.
\]
Taylor's theorem at \(\ell=\pi\) gives the stated sharpness of the coefficient.

**Step 3: Exact maximum by Fourier series.** At \(\ell=\pi\), \(F=\pm1\) has zero mean and \(|\widehat F(k)|^2=4/(\pi^2k^2)\) for odd nonzero \(k\), zero otherwise. Since \(|F-\mathcal P_\lambda F|=1-F\mathcal P_\lambda F\) pointwise, Parseval gives
\[
E_{1,\lambda}(\pi)=2\pi-\int_\mathbb T F\mathcal P_\lambda F
=2\pi-\frac{16}\pi\sum_{j\ge0}\frac{\lambda^{2j+1}}{(2j+1)^2}.
\]
The odd-index sum equals \((\operatorname{Li}_2(\lambda)-\operatorname{Li}_2(-\lambda))/2\), establishing the closed form, also at \(\lambda=0\) by continuity.

**Step 4: Sharp logarithmic regime.** Write \(S(\lambda)=\sum_{j\ge0}\lambda^{2j+1}/(2j+1)^2\). For \(0<\lambda<1\),
\[
S'(\lambda)=\frac{\operatorname{artanh}\lambda}{\lambda}
=\frac12\log\frac1{1-\lambda}+O(1)
\quad(\lambda\uparrow1).
\]
Also \(S(1)=\pi^2/8\). Integrating over \([\lambda,1]\) yields \(S(1)-S(\lambda)\sim\frac12(1-\lambda)\log\frac1{1-\lambda}\). The maximum is therefore asymptotic to \((8/\pi)(1-\lambda)\log(1/(1-\lambda))\). Since \(1-\rho^N\sim N(1-\rho)\) whenever \(N(1-\rho)\to0\), substitution completes the uniform-in-sequence assertion.

## Verification

The derivation establishes each identity analytically for all quantified parameters; no finite sample is used as proof. The standalone `verify.py` checks the independent integral and Fourier representations numerically at three kernel parameters, verifies the expected symmetry, and tests the local sharp quadratic coefficient; this is a reproducibility check rather than an infinite certificate.

## Relationship to prior work

Chen, Chen, Hamada and Li (2026, arXiv:2610.31132v1, especially Lemmas 2.8–2.9 and Claim 2.1 on pp. 19–22) used the equally spaced sign traces \(\operatorname{sgn}(\sin N\theta)\) to obtain a one-sided logarithmic *lower estimate* for their Poisson \(L^1\) defect. Their displayed statement does not provide its all-parameter exact defect, leading constant, or optimal unequal duty-cycle classification. The result here gives these for that exact witness family, not a new solution to the source's main majorant-equivalence theorem. Existing Poisson heat-content results for Euclidean balls and prior sharp Poisson operator-norm estimates concern different optimization domains or functionals, and no implication to this complete two-jump profile was identified in the inspected material.

## Limitations

The optimality is restricted to a single connected positive arc and its complement in each periodic cell. It does not classify traces with more than two jumps per cell or nonbinary amplitudes, nor sharpen the full Hardy–Littlewood equivalence theorem itself. A historical equivalent computation in the wider circle heat-content literature cannot be ruled out by the searches; independent mathematical and priority review remain outstanding.

## References

1. J. L. Chen, S. L. Chen, H. Hamada and Q. Y. Li, *The Hardy-Littlewood-type equivalence problem and its applications*, arXiv:2610.31132v1, first posted 2026-10-22, particularly §2, Lemmas 2.8–2.9 and Claim 2.1. https://arxiv.org/abs/2610.31132
2. L. Acuña Valverde, *On the heat content for the Poisson kernel over the unit ball in the euclidean space*, Bull. Lond. Math. Soc. 52 (2020), 1093–1104, DOI:10.1112/blms.12384 (related context; abstract inspected, not a full-text exclusion test).
