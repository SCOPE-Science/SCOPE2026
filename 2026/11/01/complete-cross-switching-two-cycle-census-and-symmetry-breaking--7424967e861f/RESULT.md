# Complete cross-switching two-cycle census and symmetry-breaking merger in a cubic neuron map

## Finding
For the one-dimensional cubic Courbage–Nekorkin–Vdovin voltage map on its natural reflection-symmetric parameter subfamily, the number of distinct primitive two-cycles crossing the switching point is an explicit piecewise function of both parameters. It can equal **four**. There are two different exact transitions: a symmetry-breaking merger of two asymmetric cycles with a symmetric cycle, and a separate fold of two symmetric cycles. The merger includes an open parameter region with **two simultaneously attracting asymmetric two-cycles**.

Write
\[
 g_{\mu,\beta}(x)=x+\mu x(x-\tfrac12)(1-x)+\tfrac\beta2-\beta H(x-\tfrac12),
 \quad \mu>0,\ \beta>0,
\]
where \(H(y)=0\) for \(y<0\) and \(H(y)=1\) for \(y\ge0\). The parameters correspond to \(a=d=1/2\) and \(\alpha=-\beta/2\) in the published voltage model. We count each unordered two-point orbit once, and count **only** those with one point in \((0,1/2)\) and the other in \((1/2,1)\). This restricted, cross-switching count is denoted \(N_2(\mu,\beta)\).

Define the symmetry-breaking threshold
\[
 \beta_{\mathrm{sb}}(\mu)=\frac{\mu+12}{6\sqrt3},
\]
and, for \(\mu>4\), the fold threshold
\[
 \beta_{\mathrm f}(\mu)=\frac{(\mu+8)^{3/2}}{6\sqrt{3\mu}}.
\]
Let \(S(\mu,\beta)\) be the number of reflection-symmetric cycles. For \(0<\mu\le4\), it equals one when \(0<\beta<2\) and zero when \(\beta\ge2\). For \(\mu>4\), it equals one when \(0<\beta\le2\), two when \(2<\beta<\beta_{\mathrm f}\), one when \(\beta=\beta_{\mathrm f}\), and zero above the fold. Then the **complete exact crossing count** is
\[
 \boxed{N_2(\mu,\beta)=S(\mu,\beta)+2\mathbf1_{\{1<\beta<\beta_{\mathrm{sb}}(\mu)\}}.}
\]
In particular, \(N_2=4\) whenever
\[
 \mu>12(\sqrt3-1),\qquad 2<\beta<\beta_{\mathrm{sb}}(\mu).
\]
The two nonsymmetric cycles are locally attracting for each fixed \(\mu>0\) when \(\beta<\beta_{\mathrm{sb}}(\mu)\) is sufficiently close to the upper endpoint. The merging symmetric cycle is repelling on the immediate lower side and attracting on the immediate upper side (as long as it remains inside the counting interval).

## Assumptions and scope
The Heaviside convention at the switch matters only for orbits that hit \(x=1/2\), which are excluded. No global invariance of \([0,1]\) is assumed or needed: the result concerns exact real-map periodic points that lie strictly within that interval. Local attraction refers to attraction under the second iterate in a sufficiently small neighborhood avoiding the switch. In particular, the result does **not** count all cycles in the full real line, and does not claim a global attractor or neuron-network result.

## Proof
The polynomial part is antisymmetric about \(1/2\). In centered coordinates \(u=x-1/2\), set \(h(u)=(1+\mu/4)u-\mu u^3\). The two branches of the map are \(u\mapsto h(u)+\beta/2\) for \(u<0\), and \(u\mapsto h(u)-\beta/2\) for \(u>0\). Let a crossing two-cycle be \(1/2-r\mapsto1/2+s\mapsto1/2-r\), with \(r,s\in(0,1/2)\). Its equations reduce exactly to
\[
 \frac\beta2=r+s+\mu r(\tfrac14-r^2)
 =r+s+\mu s(\tfrac14-s^2).
\]
Subtracting yields
\[
 \mu(r-s)(\tfrac14-r^2-rs-s^2)=0.
\]
Thus **every** crossing cycle is either symmetric (\(r=s\)) or belongs to the conic \(r^2+rs+s^2=1/4\); there is no third possibility.

**Symmetric branch.** Put \(r=s=u\). The cycle condition becomes
\[
 \beta=B_\mu(u):=(4+\mu/2)u-2\mu u^3,\quad 0<u<1/2.
\]
Its derivative is \(B'_\mu(u)=4+\mu/2-6\mu u^2\). If \(\mu\le4\), this is positive inside the interval, and \(B_\mu\) increases from zero to the unattained endpoint value two. If \(\mu>4\), the unique interior maximum is at \(u_*^2=(\mu+8)/(12\mu)\), of height \(\beta_{\mathrm f}\); the curve then decreases to two at \(u=1/2\), which is excluded. At \(\beta=2\) it has the single admissible root \(u_0=(\sqrt{1+32/\mu}-1)/4\). This proves the complete formula for \(S\), including each boundary case. Because \(B''_\mu(u_*)=-12\mu u_*\ne0\), the fold is nondegenerate, with
\[
 u_\pm=u_*\pm\sqrt{\frac{\beta_{\mathrm f}-\beta}{6\mu u_*}}+O(\beta_{\mathrm f}-\beta).
\]

**Asymmetric branch.** Suppose \(r\ne s\), so \(r^2+rs+s^2=1/4\). Write \(t=r+s\). Then \(rs=t^2-1/4\), and the discriminant of the quadratic with roots \(r,s\) is \(1-3t^2\). Positivity, distinctness, and \(r,s<1/2\) are equivalent to \(1/2<t<1/\sqrt3\). The cycle equations become the single equation
\[
 \beta=C_\mu(t):=2t[1+\mu(t^2-\tfrac14)],
 \quad \tfrac12<t<1/\sqrt3.
\]
Its derivative \(C'_\mu(t)=2[1+\mu(3t^2-1/4)]\) is strictly positive. The limiting endpoint values are \(1\) and \(\beta_{\mathrm{sb}}\), both unattained for distinct strictly interior \(r,s\). Thus exactly one \(t\) exists when \(1<\beta<\beta_{\mathrm{sb}}\), yielding the two **different** cycles
\[
 \{\tfrac12-r,\tfrac12+s\},\qquad
 \{\tfrac12-s,\tfrac12+r\},\quad
 r,s=\tfrac12\bigl(t\pm\sqrt{1-3t^2}\bigr).
\]
At \(\beta\uparrow\beta_{\mathrm{sb}}\), both become the symmetric cycle with \(r=s=1/(2\sqrt3)\); their separation is
\[
 |r-s|\sim \frac{3^{1/4}}{\sqrt{1+3\mu/4}}\sqrt{\beta_{\mathrm{sb}}-\beta}.
\]
At the lower boundary \(\beta\downarrow1\), one of \(r,s\) approaches zero (the switch) and the other approaches \(1/2\) (an endpoint), so no such orbit is counted at equality.

**Stability at the merger.** The branch derivative at \(1/2\pm u\) is \(d(u)=1+\mu(1/4-3u^2)\). Thus the symmetric orbit has two-step multiplier \(d(u)^2\). The symmetry-merger point \(u_c=1/(2\sqrt3)\) has \(d(u_c)=1\), and \(B'_\mu(u_c)=4\), which is positive: the local symmetric branch crosses \(u_c\) as \(\beta\) increases. Consequently it is repelling immediately below \(\beta_{\mathrm{sb}}\) and attracting immediately above it. For an asymmetric orbit, the multiplier can be expressed only in terms of \(t\):
\[
 \Lambda(t)=(1+\mu/4)^2-3\mu(1+\mu/4)(1/2-t^2)+9\mu^2(t^2-1/4)^2.
\]
An exact factorization gives
\[
 \Lambda(t)-1=\frac\mu4(3t^2-1)(12\mu t^2-\mu+4)<0
\]
for all \(1/2<t<1/\sqrt3\). Since \(\Lambda(t)\to1\) as \(t\uparrow1/\sqrt3\), continuity also implies \(\Lambda(t)>-1\) sufficiently close to the endpoint: **both asymmetric cycles are then attracting**. The symmetric fold occurs at \(d(u_*)=-1\), so its two-step multiplier is one; its nondegeneracy follows from the nonzero second derivative of \(B_\mu\). Finally, \(\beta_{\mathrm{sb}}>2\) holds precisely for \(\mu>12(\sqrt3-1)\); on \((2,\beta_{\mathrm{sb}})\) we have two symmetric and two asymmetric crossing cycles. This establishes the four-cycle region and concludes the proof.

## Verification
The supplementary Python program `check.py` reproduces the algebraic reductions in exact SymPy arithmetic, verifies both critical thresholds and multiplier factorizations, and uses certified rational root intervals for representative parameter points. It additionally substitutes computed two-cycle coordinates into both branches. These finite cases are **not** used to infer the universal counts; monotonicity, exact factorization, and positivity arguments above establish them for all real parameters in the stated domain.

## Relationship to prior work
Bartłomiejczyk, Llovera Trujillo and Signerska-Rynkowska introduced and investigated the cubic version of the Courbage–Nekorkin–Vdovin map and established expanding Lorenz-map conditions, periodic-itinerary results, and uniqueness/repulsion of period-two cycles under expansion. Their Section 7 explicitly highlights the importance of dynamics outside the expanding regime. The present result counts all cross-switching primitive two-cycles on a natural reflection-symmetric subfamily **without** assuming expansion, and determines its fold and symmetry-breaking mergers. It neither reclaims the published map nor asserts novelty of elementary one-dimensional fold theory. Other published two-cycle classifications for different neuron maps do not imply these parameter thresholds or crossing counts.

## Limitations
The count excludes cycles that remain on the same side of the switching line, leave \((0,1)\), or touch its boundary; it is not a complete global two-cycle census. The parameter constraint \(a=d=1/2,\alpha=-\beta/2\) is essential to the exact reflection reduction. Local attraction does not imply a globally invariant biological voltage interval. No independent audit, full-parameter extension, or claims about higher periods are provided. Unindexed equivalent results remain a publication-priority risk.

## References
1. P. Bartłomiejczyk, F. Llovera Trujillo and J. Signerska-Rynkowska, *Analysis of dynamics of a map-based neuron model via Lorenz maps*, Chaos **34**, 043110 (2024), DOI: 10.1063/5.0188464. Author's accepted manuscript made publicly available April 2024.
2. F. Llovera Trujillo, J. Signerska-Rynkowska and P. Bartłomiejczyk, *Periodic and chaotic dynamics in a map-based neuron model*, arXiv:2111.14499 (2021). This concerns the different Chialvo map.
3. Relevant public research-record comparators: *Exact prime-two orbit census and coexistence wedge for the rational Rulkov neuron map* (2026) and *Complete prime-period-two spectrum and the sharp sink boundary of the Duffing map* (2026), both on distinct dynamical systems.
