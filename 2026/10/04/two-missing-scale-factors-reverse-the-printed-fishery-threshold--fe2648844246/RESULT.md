# Two missing scale factors reverse the printed fishery threshold calibration
## Finding
For the harvesting model in Ding, Yu, Guo, Chen, and Liu, the threshold functional printed immediately before Theorem 3.1 is
\[
\digamma(T,\overline T)=rT-\frac1c\int_{\overline T}^{T}q(t)\,dt.
\]
If \(\overline T^*\) denotes the unique zero assumed in that application, then the exact defining relation is
\[
\int_{\overline T^*}^{T}q(t)\,dt=crT.
\]
Writing
\[
\overline q^*=\frac{1}{T-\overline T^*}\int_{\overline T^*}^{T}q(t)\,dt,
\]
therefore gives
\[
\overline T^*=T\frac{\overline q^*-cr}{\overline q^*}.
\]
The source instead prints \(\overline T^*=(\overline q-cr)/\overline q\), which omits the factor \(T\). Likewise, for fixed \(\overline T\), solving \(\digamma=0\) for the intrinsic growth rate gives
\[
r^*=\frac1{cT}\int_{\overline T}^{T}q(t)\,dt
=\frac{(T-\overline T)\overline q}{cT},
\]
whereas the source prints the same expression without the factor \(1/c\).

These are not harmless normalizations. With \(T=2\), \(c=2\), \(r=1\), \(q(t)\equiv4\), \(G=l=1\), and \(E(t)\equiv2\), the correct closed-season threshold is \(\overline T^*=1\), while the printed expression gives \(1/2\). At \(\overline T=3/4\), the true threshold functional equals \(-1/2\), and the population goes extinct globally. Substituting the printed cutoff into Theorem 3.1 would instead place \(3/4\) above threshold and assert a positive periodic solution.

## Assumptions and scope
The correction uses exactly the harvesting system (3.1) and threshold functional displayed in Section 3.1 of the source. The general identities require only \(T>0\), \(c>0\), \(r>0\), nonnegative continuous \(T\)-periodic \(q\), and existence of the unique root \(\overline T^*\) invoked by the paper. The concrete counterexample uses constant \(q\) and \(E\) and satisfies the source's standing harvesting assumptions: \(E_0=2\ge Gl/c=1/2\), \(q_0=4\ge cr=2\), and \(E_0>q^0lG/(rc^2)=1\).

The finding is deliberately limited to the two explicit threshold calibrations and the associated algebraic equality in the local-stability proof. It does not claim that the abstract switching theorem, formulated in terms of the actual zero of \(\digamma\), is false. It also does not assess separate conditions used elsewhere in the article to establish existence of a root for nonconstant \(q\).

## Proof
At a closed-season threshold, \(\digamma(T,\overline T^*)=0\). Substituting the displayed definition of \(\digamma\) yields
\[
0=rT-\frac1c\int_{\overline T^*}^{T}q(t)\,dt,
\]
which is equivalent to
\[
\int_{\overline T^*}^{T}q(t)\,dt=crT.
\]
Factoring the integral as \((T-\overline T^*)\overline q^*\) gives
\[
(T-\overline T^*)\overline q^*=crT,
\]
and hence
\[
\overline T^*=T-\frac{crT}{\overline q^*}
=T\left(1-\frac{cr}{\overline q^*}\right).
\]
Thus the printed expression is missing a factor of \(T\). For nonconstant \(q\), \(\overline q^*\) itself depends on the unknown endpoint, so this average-value form is implicit; the integral identity is the clean exact characterization.

For fixed \(\overline T\), solving the same equation for \(r\) instead gives
\[
r^*=\frac{1}{cT}\int_{\overline T}^{T}q(t)\,dt
=\frac{(T-\overline T)\overline q}{cT},
\]
so the printed growth-rate threshold is missing \(1/c\).

The source's local-stability proof later lower-bounds an eigenvalue expression by \(rT-c^{-1}\int_{\overline T}^{T}q\). The root relation gives the exact repair
\[
rT-\frac1c\int_{\overline T}^{T}q(t)\,dt
=\frac1c\int_{\overline T^*}^{\overline T}q(t)\,dt.
\]
For \(\overline T>\overline T^*\) this is positive whenever \(q\) is positive on a set of positive measure in that interval. Thus the sign conclusion used for local stability survives, but the printed average-times-length equality is not the correct general identity.

For the exact witness, take \(T=2\), \(c=2\), \(r=1\), and \(q(t)\equiv4\). Then
\[
\digamma(2,\overline T)=2-2(2-\overline T)=2\overline T-2,
\]
so the true root is \(\overline T^*=1\). The printed formula gives
\[
\frac{4-2}{4}=\frac12.
\]
At \(\overline T=3/4\), the closed-season per-capita growth is \(1-u\le1\). During the open season, with \(G=l=1\) and \(E=2\), it is
\[
1-u-\frac8{4+u}.
\]
For every \(u>0\),
\[
1-u-\frac8{4+u}<-1,
\]
because after adding \(1\) and clearing the positive denominator \(4+u\), the numerator is \(-2u-u^2<0\). Therefore over each full period
\[
\log\frac{u(2(n+1))}{u(2n)}
\le \frac34-\frac54=-\frac12,
\]
so
\[
u(2(n+1))\le e^{-1/2}u(2n).
\]
Thus every positive solution tends to zero. This directly contradicts the regime obtained by combining the source's printed \(\overline T^*=1/2\) with the statement of Theorem 3.1, because \(3/4>1/2\).

## Verification
The standalone verifier checks the two corrected formulas and the constant-parameter witness with exact rational arithmetic. It confirms \(\overline T^*=1\), the printed value \(1/2\), \(\digamma(2,3/4)=-1/2\), the correct fixed-\(\overline T\) growth threshold \(5/4\), and the printed value \(5/2\). It also checks that the source's auxiliary inequalities hold for the witness. The global-extinction estimate is analytic and does not rely on finite simulation.

## Relationship to prior work
The 2025 source is a general switching-system paper whose Section 3.1 specializes the theory to seasonal Michaelis–Menten harvesting and explicitly states the two formulas corrected here. Earlier work by Feng, Liu, Ruan, and Yu (2023) studies the same biological class and establishes a closed-season threshold, while later harvesting papers continue to use threshold duration as a management quantity. Those broader works motivate why an explicit calibration matters, but the present claim is source-specific: it identifies two scale factors omitted in the 2025 formulas and shows an admissible parameter point where using the printed cutoff reverses the persistence/extinction classification.

No indexed correction or erratum for DOI 10.1017/S0956792525100065 was found in exact-title, DOI, formula, and threshold searches at the time of review. A highly relevant 2023 predecessor was compared at the abstract and bibliographic level; an attempted full-text retrieval returned unrelated material and was excluded from scientific evidence. That access limitation does not decide the source-specific comparison, because the later 2025 formulas and their contradiction are fully visible in the lawful public full text.

## Limitations
The corrected \(\overline T^*\) relation is generally implicit when \(q\) varies with time; no closed-form inversion is claimed. The result does not establish or refute any additional sufficient conditions for threshold existence outside the constant witness. It does not challenge the general threshold theorems when they are applied using the actual zero of \(\digamma\). No independent audit has been performed.

## References
1. Q. Ding, J. Yu, Z. Guo, Y. Chen, and Y. Liu, “Periodic dynamics of a general switching dynamical system,” European Journal of Applied Mathematics, DOI 10.1017/S0956792525100065. First published online 8 August 2025.
2. Public seminar announcement with the same title and matching abstract, Sun Yat-sen University, dated 22 April 2025: https://mathzh.sysu.edu.cn/zh-hans/article/2254.
3. X. Feng, Y. Liu, S. Ruan, and J. Yu, “Periodic dynamics of a single species model with seasonal Michaelis-Menten type harvesting,” Journal of Differential Equations 354 (2023), 237–263, DOI 10.1016/j.jde.2023.01.014.
4. F. Jiao, K. Zhang, X. Sheng, K. Li, and Y. Liu, “Threshold dynamics of a seasonal switching model with Holling type II predation and linear harvesting,” ZAMM/ZAMP 77 (2026), article 76, DOI 10.1007/s00033-026-02726-8.
