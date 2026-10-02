# Sharp dyadic-quantile calibration and lattice phase at the critical power-log boundary

## Final claim

For \(\kappa\ge0\), let
\[
f_\kappa(x)=Z_\kappa^{-1}\frac{1-x^2}{[\log(e/(1-x^2))]^\kappa}\mathbf 1_{\{|x|<1\}},
\]
and let \(\omega_\kappa\) be the inverse Hellinger modulus of its location family, with the convention
\[
H^2(P,Q)=\frac12\int(\sqrt{dP}-\sqrt{dQ})^2.
\]
Write \(a_\kappa=2/Z_\kappa\). The critical Hellinger behavior at the endpoint power \(1\) is prior input: for \(\kappa<1\),
\[
H^2(f_{\kappa,0},f_{\kappa,2r})\sim \frac{a_\kappa}{1-\kappa}r^2[\log(1/r)]^{1-\kappa},
\]
for \(\kappa=1\),
\[
H^2(f_{1,0},f_{1,2r})\sim a_1r^2\log\log(1/r),
\]
and for \(\kappa>1\) the family has finite Fisher information and ordinary quadratic Hellinger behavior. The contribution here is the sharp behavior of the dyadic quantile functional introduced by Wang--Gao and its fixed-grid phase effect.

Let \(q_\kappa\) be the quantile function of \(f_\kappa\), and for \(0<p\le1/4\) define
\[
\Delta_\kappa(p)=\left(\sum_{j\ge0:\,2^jp\le1/4}
\frac{2^j}{[q_\kappa(2^{j+1}p)-q_\kappa(2^jp)]^2}\right)^{-1/2}.
\]
Then for every \(0\le\kappa<1\),
\[
\Delta_\kappa(p)\sim(\sqrt2-1)
\sqrt{\frac{2^{1-\kappa}(1-\kappa)\log2}{a_\kappa}}
\sqrt p\,[\log(1/p)]^{-(1-\kappa)/2},
\]
while at \(\kappa=1\),
\[
\Delta_1(p)\sim(\sqrt2-1)\sqrt{\frac{\log2}{a_1}}
\sqrt{\frac{p}{\log\log(1/p)}}.
\]
Consequently, throughout the infinite-information side \(0\le\kappa\le1\),
\[
\boxed{\frac{\Delta_\kappa(p)}{\omega_\kappa(p)}\longrightarrow(\sqrt2-1)\sqrt{\log2}.}
\]
Thus the dyadic functional has a universal sharp ratio to the inverse Hellinger modulus on this critical family, strengthening the constant-factor comparison in Wang--Gao.

The fixed dyadic grid need not have a single sharp constant in the regular finite-information regime. For the standard Laplace density \(f(x)=e^{-|x|}/2\), one has \(\omega(p)=\sqrt{2p}+o(\sqrt p)\), while
\[
\liminf_{p\downarrow0}\frac{\Delta(p)}{\sqrt p}=\sqrt2\log2,
\qquad
\limsup_{p\downarrow0}\frac{\Delta(p)}{\sqrt p}=2\log2.
\]
Equivalently,
\[
\liminf_{p\downarrow0}\frac{\Delta(p)}{\omega(p)}=\log2,
\qquad
\limsup_{p\downarrow0}\frac{\Delta(p)}{\omega(p)}=\sqrt2\log2.
\]
The oscillation is a genuine dyadic lattice phase rather than numerical noise.

## Proof

Put \(s=1-x\). Near the right endpoint,
\[
f_\kappa(1-s)\sim a_\kappa\frac{s}{[\log(1/s)]^\kappa}.
\]
Hence the endpoint mass satisfies
\[
F_\kappa(-1+s)\sim \frac{a_\kappa}{2}\frac{s^2}{[\log(1/s)]^\kappa}.
\]
Inverting this regularly varying relation gives, uniformly for fixed \(c>0\),
\[
q_\kappa(cp)-q_\kappa(p)
\sim(\sqrt c-1)\sqrt{\frac{2^{1-\kappa}p}{a_\kappa}}
[\log(1/p)]^{\kappa/2}.
\]
For \(c=2\), the \(j\)-th dyadic gap therefore has the leading form
\[
(\sqrt2-1)\sqrt{\frac{2^{1-\kappa}2^jp}{a_\kappa}}
[\log(1/(2^jp))]^{\kappa/2}.
\]
After substitution into the defining energy for \(\Delta_\kappa\), the factors \(2^j\) cancel. The remaining sum is a Riemann sum over the logarithmic dyadic scale. For \(\kappa<1\),
\[
\sum_{0\le j\le J}[\log(1/p)-j\log2]^{-\kappa}
\sim\frac{[\log(1/p)]^{1-\kappa}}{(1-\kappa)\log2},
\]
and for \(\kappa=1\) it is asymptotic to \((\log\log(1/p))/\log2\). Taking inverse square roots yields the displayed formulas. Combining them with the prior sharp Hellinger asymptotics gives the universal ratio.

For the standard Laplace law, the left-tail quantile is exactly
\[
q(u)=\log(2u),\qquad0<u\le1/2.
\]
Every dyadic gap below the median is therefore \(\log2\). If
\[
J(p)=\left\lfloor\log_2\frac1{4p}\right\rfloor,
\]
then
\[
\Delta(p)=\frac{\log2}{\sqrt{2^{J(p)+1}-1}}.
\]
Writing \(2^{J(p)}p\in(1/8,1/4]\) gives the stated liminf and limsup. The Hellinger expansion for a regular location family gives \(\omega(p)=\sqrt{2p}+o(\sqrt p)\), which yields the ratio interval.

## Prior boundary and limitations

The alpha-one power-log Hellinger trichotomy is not claimed as new here; it was already published on 18 September 2026. Wang--Gao introduced the dyadic quantile functional and proved its constant-factor equivalence to the inverse Hellinger modulus over their shape-constrained class. Their power-log example uses endpoint power strictly below one and does not state the sharp critical-alpha-one dyadic constants above.

The sharp ratio proved here is specific to this critical power-log family and the Wang--Gao dyadic functional. The Laplace calculation shows that a fixed dyadic grid can retain a nonvanishing phase in a regular model; it does not claim that phase oscillation occurs for every finite-Fisher location family.

## References

1. Q. Wang and C. Gao, *Instance-Optimal Adaptive Location Estimation via Multiscale Mid-Summaries*, arXiv:2609.20749 (2026).
2. *Critical power-log Hellinger transition in compact-support location families*, published 18 September 2026, https://github.com/Resultary/2026/tree/main/2026/9/18/SCOPE-critical-power-log-location-hellinger-transition--92a2596e06eb.
