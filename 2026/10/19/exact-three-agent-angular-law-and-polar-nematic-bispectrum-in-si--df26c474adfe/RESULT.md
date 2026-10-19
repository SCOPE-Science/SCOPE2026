# Exact three-agent angular law and polar--nematic bispectrum in signed-copying flocks

## Finding
Consider the stationary annealed orientation-copying model specified below. Its entire three-distinct-agent angular joint law has an exact Fourier classification. For any distinct labels \(i,j,k\) and any integers \(r,s,t\), put
\[
G_{r,s,t}=\mathbb E\bigl[e^{\mathrm i(r\theta_i+s\theta_j+t\theta_k)}\bigr].
\]
Define \(q=2p-1\), \(\omega=a+c(1-q)\), and the two exact pair correlations
\[
R_{\mathrm o}=\frac{cq}{N\omega+cq},\qquad R_{\mathrm e}=\frac{c}{Na+c}.
\]
The complete result is:

1. If \(r+s+t\ne0\), then \(G_{r,s,t}=0\). If all three indices vanish, then \(G_{0,0,0}=1\).
2. If exactly one index vanishes and the other two are opposite nonzero integers, the answer is \(R_{\mathrm o}\) for odd indices and \(R_{\mathrm e}\) for even indices.
3. If all three indices are nonzero and sum to zero, then exactly zero or two of them are odd. In the all-even case,
\[
G_{r,s,t}=E_N=\frac{2c^2}{(Na+c)(Na+2c)}.
\]
In the two-odd case,
\[
G_{r,s,t}=M_N=\frac{(2c/N)\bigl[qR_{\mathrm e}+(q+1)R_{\mathrm o}\bigr]}{3a+2c(1-q)+(2c/N)(2q+1)}.
\]
In particular \(\operatorname{sgn} M_N=\operatorname{sgn}(2p-1)\), with \(M_N=0\) exactly at \(p=1/2\), whereas \(E_N>0\) is independent of \(p\). The family with two odd exponents includes the distinct-agent polar--nematic bispectrum \(\mathbb E[e^{\mathrm i(\theta_i+\theta_j-2\theta_k)}]\); **every** such neutral mixed-parity three-agent harmonic has the same value. Fourier uniqueness on the three-torus shows these formulas determine the complete stationary joint law of three distinct agents, including any singular components.

For fixed \(a,c>0\) and \(p\in[0,1]\), the nontrivial three-distinct-agent correlations are of exact order at most \(N^{-2}\). More precisely,
\[
\lim_{N\to\infty}N^2E_N=\frac{2c^2}{a^2},\qquad
\lim_{N\to\infty}N^2M_N=\frac{2c^2q}{3a+2c(1-q)}\left[\frac1a+\frac{1+q}{a+c(1-q)}\right].
\]
The natural empirical polar--nematic product \(\mathbb E[m_1^2\overline{m_2}]\), with \(m_h=N^{-1}\sum_j e^{\mathrm ih\theta_j}\), obeys the exact collision decomposition
\[
\mathbb E[m_1^2\overline{m_2}]=\frac{1+(N-1)(R_{\mathrm e}+2R_{\mathrm o})+(N-1)(N-2)M_N}{N^2}.
\]
Consequently the raw empirical bispectrum includes one- and two-agent collision terms and need not itself have the sign of \(M_N\).

## Assumptions and scope
The integer \(N\ge3\) is finite. The microscopic orientations \(\theta_j\) belong to the circle \(\mathbb R/(2\pi\mathbb Z)\). Each labeled agent independently resets its angle to an independent uniform angle at rate \(a>0\). Independently, each labeled agent updates at rate \(c>0\): it chooses a uniformly random partner among **all \(N\) labels, including itself**, copies that partner's orientation with probability \(p\in[0,1]\), and copies its antipodal orientation with probability \(1-p\). The alignment/antialignment choice is redrawn independently at every update (annealed, not fixed by agent). All expectations refer to the unique invariant probability measure for this continuous-time process. Positive refreshing rates imply uniqueness: with positive probability all labels independently refresh during an interval without a copy event, providing a common product-uniform minorization.

The theorem concerns three distinct labeled agents and all integer Fourier coefficients, not a distributional approximation or any quenched-role dynamics. Formulae continue to the parameter endpoints \(p=0\) and \(p=1\).

## Proof
Write \(z_j=e^{\mathrm i\theta_j}\), \(\Gamma_h=p+(1-p)(-1)^h\). The stationary measure is invariant under simultaneous rotation, since this symmetry commutes with the generator and the stationary law is unique. This proves the nonneutral zero statement. Exchangeability likewise follows from uniqueness.

First, take any nonzero integer \(h\) and two distinct labels \(i,j\). The invariant correlation \(R_h=\mathbb E[z_i^h z_j^{-h}]\) is real by label exchange and complex conjugation. A uniform reset of either label kills the expectation. An update of either label replaces its nonzero Fourier factor by \(\Gamma_h z_l^{\pm h}\), averaged over a uniform partner. Exactly one partner selection coincides with the other displayed label, yielding the identity
\[
0=-2(a+c)R_h+\frac{2c\Gamma_h}{N}\bigl[1+(N-1)R_h\bigr].
\]
Solving gives
\[
R_h=\frac{c\Gamma_h}{N[a+c(1-\Gamma_h)]+c\Gamma_h}.
\]
The denominator is strictly positive: for even \(h\) it equals \(Na+c\); for odd \(h\) it equals \(Na+c[N-(N-1)q]\), which is at least \(Na+c\). The parity values of \(\Gamma_h\) yield \(R_{\mathrm o}\) and \(R_{\mathrm e}\).

For three distinct indices and nonzero Fourier exponents \(r,s,t\) with \(r+s+t=0\), let \(G=G_{r,s,t}\). A reset of any one label kills the product; all three resets contribute \(-3aG\). For a copy update on label \(i\), a partner outside the three designated labels (\(N-3\) choices) or the focal label itself (one choice) returns the original Fourier product multiplied by \(\Gamma_r\), giving \((N-2)\Gamma_rG\) in the partner sum. A partner coinciding with label \(j\) collapses the two exponents to \(r+s=-t\), giving \(R_t\), while a partner coinciding with label \(k\) gives \(R_s\). Accounting for the outgoing copy loss gives
\[
0=-3(a+c)G+\frac cN\sum_{\ell\in\{r,s,t\}}\Gamma_\ell\left[(N-2)G+\sum_{m\in\{r,s,t\}\setminus\{\ell\}}R_m\right].
\]
Equivalently,
\[
G=\frac{(c/N)\bigl[\Gamma_r(R_s+R_t)+\Gamma_s(R_r+R_t)+\Gamma_t(R_r+R_s)\bigr]}{3(a+c)-(c/N)(N-2)(\Gamma_r+\Gamma_s+\Gamma_t)}.
\]
The denominator is at least \(3a+6c/N>0\), since each \(\Gamma_\ell\le1\). Because the three integer exponents sum to zero, the number of odd exponents must be even. For all three even, substitute \(\Gamma_\ell=1\) and \(R_\ell=R_{\mathrm e}\); simplifying yields \(E_N\). For precisely two odd and one even, substitute two \(\Gamma=q,R=R_{\mathrm o}\) and one \(\Gamma=1,R=R_{\mathrm e}\); simplifying yields \(M_N\), independently of the actual nonzero harmonics. This proves the complete trichotomy of nonzero triple exponents. The case of one zero exponent is exactly the proven pair formula, and the all-zero case is immediate, exhausting every integer Fourier triple.

For the sign assertion, use
\[
qR_{\mathrm e}+(q+1)R_{\mathrm o}=q\left[R_{\mathrm e}+\frac{c(q+1)}{N\omega+cq}\right].
\]
The expression in square brackets is strictly positive, since \(R_{\mathrm e}>0\), \(q+1\ge0\), and all denominators are positive. The triple denominator is positive, so \(M_N\) has exactly the sign of \(q\). The two limiting formulas follow by multiplying the finite expressions by \(N^2\) and taking ordinary rational limits. Finally, expanding the three sums in \(m_1^2\overline{m_2}\) into all-equal, exactly-two-equal, and three-distinct labeled index configurations gives the displayed collision decomposition with multiplicities \(N\), \(N(N-1)\), and \(N(N-1)(N-2)\).

## Verification
Run the included standalone `verify.py` using Python with `numpy` and `scipy`. It calculates the stationary distribution of an **independently constructed finite-state generator** on uniform even-root angular alphabets with \(N=3,4\), compares the distinct-agent Fourier observables against their closed formulas, and separately checks exact rational identities and the strict mixed-parity sign classification for additional \(N\) and parameters. The script completed **400 assertions/comparisons** on the packaged version. The finite alphabet is chosen sufficiently fine that every checked nonzero harmonic remains nonaliased; the script explicitly skips aliased exponents. Such finite checks support but do not replace the above all-integer analytical generator proof.

## Relationship to prior work
Chunming Zheng, *Mesoscopic theory of flocking with alignment and antialignment copying*, arXiv:2604.20251 (first posted 22 April 2026), establishes the annealed and quenched microscopic models, exact mode-level master dynamics, and second-order mesoscopic polarization and nematic approximations. Its observation that even Fourier modes are independent of the alignment mixture is prior knowledge. The theorem above does **not** claim either the model or even-mode invariance as new; it instead derives a complete exact stationary **three-distinct-agent joint Fourier law**, including a parity-universal signed mixed-harmonic correlation and the exact distinction between that correlation and the raw empirical bispectrum.

Khalil and Toral's *The noisy voter model under the influence of contrarians* (arXiv:1807.03176) treats binary opinions, in which nonzero even angular harmonics collapse to constants. Its finite-population moment calculations therefore do not directly yield the displayed continuous-angle three-harmonic classification. Herrerías-Azcué and Galla's *Consensus and diversity in multistate noisy voter models* (arXiv:1903.09198) analyzes multistate copying plus mutation and stationary marginals, but does not explicitly state an antipodal-copy signed three-agent Fourier law. General genealogical coalescent techniques may still implicitly recover some statements; the claim of originality is relative to the material inspected and is not a proof of global uniqueness.

## Limitations
The update partner is drawn with replacement; exclusion of self would change finite-\(N\) denominators. Uniform spontaneous turning and a positive rate \(a\) are necessary to the stationarity and rotational arguments used. The result excludes fixed quenched aligner/anti-aligner identities, network geometry, and spatially moving agents. The three-agent Fourier classification determines their joint law mathematically but does not assert an absolutely continuous density. A sufficiently general genealogical multi-point correlation theorem may imply these results; comparison against such a theorem remains the main originality risk.

## References
1. C. Zheng, *Mesoscopic theory of flocking with alignment and antialignment copying*, arXiv:2604.20251v1 (2026-04-22), revised arXiv:2604.20251v2 (2026-10-09); *Physical Review E* **114**, 044115 (2026), doi:10.1103/xp24-5rj6. Full text: https://arxiv.org/html/2604.20251v2 .
2. N. Khalil and R. Toral, *The noisy voter model under the influence of contrarians*, arXiv:1807.03176 (2018), *Physica A* **515**, 81–92 (2019), doi:10.1016/j.physa.2018.09.178.
3. F. Herrerías-Azcué and T. Galla, *Consensus and diversity in multistate noisy voter models*, arXiv:1903.09198 (2019), *Physical Review E* **100**, 022304, doi:10.1103/PhysRevE.100.022304.
