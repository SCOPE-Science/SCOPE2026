# The printed Monte Carlo validation point has no feasible positive moment equilibrium
## Finding
For the additive-noise Gaussian moment system printed by Yang and Han, the Figure 5 parameter pair
\[
r=\frac{113}{100},\qquad v=\frac{8}{625}
\]
admits no biologically feasible positive equilibrium. Consequently the reported equilibrium near \(\mu^*\approx0.33\), \(s^*\approx0.0006\) cannot be a fixed point of the displayed moment equations at the printed parameters. Thus Figures 5–6 do not provide equilibrium-based Monte Carlo validation of that displayed moment system for the parameter labels shown.

## Assumptions and scope
The source studies the additive-noise logistic difference equation
\[
X_{n+1}=rX_n(1-X_n)+\varepsilon_n,
\]
where \(E[\varepsilon_n]=0\) and \(E[\varepsilon_n^2]=v\). Its Gaussian moment closure uses the mean \(\mu_n\) and variance \(s_n\). A biologically feasible positive equilibrium means \(\mu^*>0\) and \(s^*>0\) and satisfies the source's displayed fixed-point equations.

The conclusion is restricted to the printed moment map and the printed Figure 5–6 parameter labels. It does not identify the parameters actually used by any unavailable simulation code, and it does not rule out transient means, quasi-stationary behavior, or simulations under a different parameter pair.

## Proof
The first component of the displayed moment map is
\[
\mu_{n+1}=r\bigl(\mu_n-\mu_n^2-s_n\bigr).
\]
At a positive fixed point this forces
\[
s^*=\mu^*\left(1-\frac1r-\mu^*\right),
\]
so \(s^*>0\) requires
\[
0<\mu^*<1-\frac1r.
\]
At \(r=113/100\), the feasible interval is therefore
\[
0<\mu^*<\frac{13}{113}\approx0.115044.
\]
In particular, the displayed value \(\mu^*\approx0.33\) is already outside the feasible interval.

To exclude every other feasible positive fixed point at the same printed noise level, use the source's quartic equilibrium equation
\[
Q(\mu;r,v)=H(\mu;r)-rv,
\]
where
\[
H(\mu;r)=2r^3\mu^4-4r^3\mu^3+3r(r^2-1)\mu^2-(r-1)^2(r+1)\mu.
\]
Put \(a=13/113\). For \(0<\mu<a\), the two omitted terms below are strictly negative, while the two positive monomials increase when \(\mu\) is replaced by \(a\). Hence
\[
H(\mu;r)
<2r^3a^4+3r(r^2-1)a^2
=\frac{292201}{22600000}.
\]
On the other hand,
\[
rv=\frac{113}{100}\frac{8}{625}
=\frac{226}{15625},
\]
and the exact gap is
\[
rv-\frac{292201}{22600000}
=\frac{173427}{113000000}>0.
\]
Therefore \(Q(\mu;r,v)<0\) throughout the entire feasible interval, so no biologically feasible positive equilibrium exists at the printed parameter pair.

## Verification
As an independent local consistency check on the rounded equilibrium quoted in the numerical discussion, set \(\mu=33/100\) and \(s=3/5000\). The first moment update gives
\[
r(\mu-\mu^2-s)=\frac{49833}{200000}=0.249165,
\]
so its fixed-point residual is
\[
\frac{49833}{200000}-\frac{33}{100}
=-\frac{16167}{200000}=-0.080835.
\]
This residual is far larger than the displayed rounding scale. The bundled `verify.py` recomputes the feasible endpoint, the exact quartic upper bound, the positive gap, and this direct fixed-point residual using rational arithmetic only.

## Relationship to prior work
Yang and Han explicitly characterize biologically feasible positive equilibria by the same quartic and feasible interval used above, while their Figure 5 caption assigns \(r=1.13\), \(v=0.0128\) to the Monte Carlo/moment-closure comparison and their numerical discussion reports convergence near \(\mu^*\approx0.33\). Their Figure 4 discussion also states that at \(v=0.0128\) two feasible positive equilibria occur only approximately for \(1.65<r<2.75\), which is consistent with the exact contradiction at \(r=1.13\).

Wang and Wang analyze a multiplicative-noise logistic map \(X_{n+1}=rX_n(1-X_n)\varepsilon_n\), with \(E[\varepsilon_n]=1\) and \(E[\varepsilon_n^2]=v>1\). Its moment map and noise parameter are different, so its equilibrium results do not imply the present additive-noise parameter contradiction. Nåsell's earlier stochastic-logistic work explains when moment closure approximates quasi-stationary cumulants, but it does not contain this discrete additive-noise map or the printed Figure 5 parameter pair.

## Limitations
The proof diagnoses consistency of the published formulas and labels only. A typographical error in the figure caption or an unreported parameter used in simulation could explain the discrepancy, but that possibility cannot restore equilibrium consistency at the printed pair. No claim is made that the underlying stochastic logistic process lacks interesting transient or quasi-stationary behavior.

## References
1. Y. Yang and X. Han, “Equilibrium and bifurcation analysis of a stochastic logistic difference equation with additive noise,” *Discrete and Continuous Dynamical Systems - S*, DOI 10.3934/dcdss.2026151. Early access and online publication: 2026-05-18.
2. H. Wang and E. Wang, “Stability and bifurcation of difference equations from stochastic logistic models,” *Mathematical Biosciences and Engineering* 23 (2026), 449–473. DOI 10.3934/mbe.2026018.
3. I. Nåsell, “Moment closure and the stochastic logistic model,” *Theoretical Population Biology* 63 (2003), 159–168. DOI 10.1016/S0040-5809(02)00060-6.
