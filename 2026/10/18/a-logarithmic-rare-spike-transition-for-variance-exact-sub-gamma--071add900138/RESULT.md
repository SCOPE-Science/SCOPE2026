# A logarithmic rare-spike transition for variance-exact sub-gamma scales

## Finding

Let \(J_0\) be any nonnegative random variable with \(0\le J_0\le K<\infty\) almost surely and \(v_0=\mathbb E[J_0^2]>0\). As \(B\to\infty\), choose \(h_B>0\) with
\[
\frac{h_B}{\log B}\longrightarrow\infty,\qquad \frac{h_B}{B}\longrightarrow0.
\]
Set \(q_B=e^{-h_B}\), and let \(J_B\) equal \(J_0\) with probability \(1-q_B\), and equal \(B\) with probability \(q_B\), independently of its other randomness. Write \(N\sim\operatorname{Poisson}(1)\) and
\[
X_B=\sum_{i=1}^{N}J_{B,i}-\mathbb E[J_B],\qquad V_B=\operatorname{Var}(X_B)=\mathbb E[J_B^2].
\]
The empty sum is zero. Define, for every \(t>0\),
\[
L_B(t)=\frac{2\log\mathbb E[e^{tX_B}]}{V_Bt^2},\qquad
\Psi_B(t)=\frac{1-L_B(t)^{-1}}{t}.
\]
For each fixed \(s\in\mathbb R\), let
\[
t_B(s)=\frac{h_B-2\log(B/h_B)+s}{B}.
\]
This argument is strictly positive for all sufficiently large \(B\). The exact limiting transition is
\[
L_B(t_B(s))\longrightarrow1+\frac{2e^s}{v_0},\qquad
\frac{h_B}{B}\Psi_B(t_B(s))\longrightarrow\frac{2e^s}{v_0+2e^s}.
\]
Let \(c_B\) be the infimum over \(c\ge0\) for which the variance-exact, right-sided sub-gamma bound
\[
\log\mathbb E[e^{tX_B}]\le\frac{V_Bt^2}{2(1-ct)}
\quad\text{for every }0\le t<1/c
\]
holds, interpreting \(1/0=\infty\). Then
\[
\boxed{\displaystyle\frac{h_B}{B}c_B\longrightarrow1,}\qquad c_B\longrightarrow\infty.
\]
Yet \(X_B\) converges weakly and in every fixed nonnegative integer moment to the centered compound Poisson variable \(X_0\) with rate one and jumps \(J_0\), and its limiting optimal scale is finite. In the canonical case \(J_0=1\), \(X_0=N-1\) has optimal scale exactly \(1/3\). For all sufficiently large \(B\) in this case, \(\Psi_B'(0+)<0\), although its global maximum occurs at a strictly positive argument and diverges.

## Assumptions and scope

The variable \(J_0\) is fixed as \(B\to\infty\), nonnegative, bounded, and has nonzero second moment. The spike mixture is independent for each compound Poisson jump. There is no assertion for jumps with negative support, varying base laws, unbounded base jumps, or other rare-event regimes. Only fixed \(s\) is asserted in the transition formula; no uniformity over diverging \(s\) is claimed. For the explicit origin-curvature and exactly \(1/3\) assertions, the base law is \(J_0=1\).

## Proof

**Exact remainder representation.** Introduce the entire function
\[
G(z)=\mathbb E[e^{zU}]=2\int_0^1(1-u)e^{zu}\,du
=\frac{2(e^z-1-z)}{z^2},\qquad G(0)=1,
\]
where \(U\) has the \(\operatorname{Beta}(1,2)\) distribution. For a rate-one centered compound Poisson sum with any bounded nonnegative jump \(J\), its cumulant generating function is
\[
K(t)=\mathbb E[e^{tJ}-1-tJ]=\frac{t^2}{2}\mathbb E[J^2G(tJ)].
\]
Indeed, \(e^z-1-z=z^2G(z)/2\), with the identity also valid at \(z=0\). Put
\[
G_0(t)=\frac{\mathbb E[J_0^2G(tJ_0)]}{v_0},\qquad
w_B=\frac{q_BB^2}{V_B},\quad V_B=(1-q_B)v_0+q_BB^2.
\]
Direct substitution, without an approximation, gives
\[
L_B(t)=(1-w_B)G_0(t)+w_BG(Bt).
\tag{1}
\]
Here \(0\le w_B\le1\), \(L_B(t)\ge1\), and \(w_B\to0\) because \(h_B/\log B\to\infty\).

**Exact optimization.** For an arbitrary \(c\ge0\), feasibility is equivalent to \(L_B(t)\le(1-ct)^{-1}\) for all \(0<t<1/c\). If \(c\) is feasible, then \(\Psi_B(t)\le c\) for \(t<1/c\); for \(t\ge1/c\), the same bound follows from \(0\le\Psi_B(t)\le1/t\). Conversely, putting \(C=\sup_{t>0}\Psi_B(t)\), the inequality \(\Psi_B(t)\le C\) rearranges to the required bound for \(0<t<1/C\). The number \(C\) is finite because \(\Psi_B(t)\) has a finite limit at zero and \(\Psi_B(t)\le1/t\) at infinity. Consequently,
\[
c_B=\sup_{t>0}\Psi_B(t).
\tag{2}
\]
This variational identity is a known general result, explicitly attributed below to Chen, and is only used here as an input to the asymptotic calculation.

**Transition layer.** For fixed \(s\), set \(z_B=h_B-2\log(B/h_B)+s\). The assumptions give \(z_B/h_B\to1\), \(z_B\to\infty\), and \(t_B(s)=z_B/B\to0\). Thus \(G_0(t_B(s))\to1\), while \(G(z)\sim2e^z/z^2\) as \(z\to\infty\). By the exact identity (1),
\[
w_BG(z_B)\sim\frac{2q_BB^2e^{z_B}}{V_Bz_B^2}
=\frac{2e^s}{V_B}\left(\frac{h_B}{z_B}\right)^2
\longrightarrow\frac{2e^s}{v_0}.
\]
This proves the limit for \(L_B\). The limit for \(\Psi_B\) follows because \(h_B/(Bt_B(s))=h_B/z_B\to1\).

**Global supremum, upper bound.** Fix \(0<\varepsilon<1\) and let \(a_B=(1-\varepsilon)h_B/B\). Since \(J_0\le K\) and \(0\le U\le1\), the elementary inequality \((e^{tr}-1)/t\le r e^{tr}\) for \(r,t\ge0\), together with (1), yields for \(0<t\le a_B\),
\[
\Psi_B(t)\le\frac{L_B(t)-1}{t}
\le K e^{Kt}+w_B B e^{Bt}
\le K e^{Ka_B}+\frac{B^3}{V_B}e^{-\varepsilon h_B}.
\]
The right side is bounded independently of \(B\), since \(a_B\to0\), \(V_B\to v_0>0\), and \(\varepsilon h_B-3\log B\to\infty\). For \(t\ge a_B\), \(\Psi_B(t)\le1/t\le B/[(1-\varepsilon)h_B]\). Because \(B/h_B\to\infty\), (2) implies
\[
\limsup_{B\to\infty}\frac{h_Bc_B}{B}\le\frac{1}{1-\varepsilon}.
\]

**Global supremum, lower bound.** At \(t=(1+\varepsilon)h_B/B\), the positive term in (1) obeys
\[
w_BG((1+\varepsilon)h_B)
\sim\frac{2B^2e^{\varepsilon h_B}}{V_B(1+\varepsilon)^2h_B^2}\longrightarrow\infty.
\]
Thus \(L_B(t)\to\infty\), \(\Psi_B(t)\sim1/t\), and
\[
\liminf_{B\to\infty}\frac{h_Bc_B}{B}\ge\frac{1}{1+\varepsilon}.
\]
Letting \(\varepsilon\downarrow0\) completes the sharp optimal-scale asymptotic.

**All-moment invisibility.** For every fixed integer \(r\ge1\),
\[
\mathbb E[J_B^r]=(1-q_B)\mathbb E[J_0^r]+q_BB^r\longrightarrow\mathbb E[J_0^r],
\]
using \(r\log B-h_B\to-\infty\). The order-one compound Poisson cumulants satisfy \(\kappa_r(X_B)=\mathbb E[J_B^r]\) for \(r\ge2\); their means are zero. Moment-cumulant identities therefore yield convergence of every fixed nonnegative integer moment of \(X_B\) to its \(X_0\) counterpart. Weak convergence follows also by bounded test functions and the vanishing probability that any jump in the finite Poisson collection is a spike.

**An interior peak hidden from local cumulants.** When \(J_0=1\), the limiting remainder is \(G(t)=\sum_{n\ge0}2t^n/(n+2)!\), whose coefficients satisfy \(a_{n+1}/a_n=1/(n+3)\le1/3\). For \(0<t<3\), \(G(t)\le(1-t/3)^{-1}\), showing \(c(X_0)\le1/3\); the \(t\downarrow0\) limit of \(\Psi_0(t)\) equals \(1/3\), showing equality. For any finite bounded nonnegative jump law, Taylor expansion gives
\[
\Psi_B(t)=\frac{\mathbb E[J_B^3]}{3V_B}
+\left(\frac{\mathbb E[J_B^4]}{12V_B}
-\frac{(\mathbb E[J_B^3])^2}{9V_B^2}\right)t+O_B(t^2).
\]
All displayed moment ratios converge to one for \(J_0=1\), so the derivative coefficient tends to \(1/12-1/9=-1/36<0\). For large \(B\), the origin is therefore a strict one-sided local maximum of the continuous extension of \(\Psi_B\). But its global supremum tends to infinity, and \(\Psi_B(t)\to0\) as \(t\to\infty\), forcing attainment at a positive argument. This completes the proof.

## Verification

All identities used in the proof are algebraic or follow from dominated convergence and the explicitly stated asymptotic conditions. The accompanying standalone standard-library checker exercises exact rational Beta-kernel identities, coefficients for the base law, moment-to-cumulant identities, and numerically cross-checks the finite-parameter profile for several bounded-jump instances. These finite checks are diagnostic rather than proofs of the limiting statements. The proof's inequalities above establish the universal limit.

## Relationship to prior work

Chen (2026) establishes the canonical Beta-transform and exact variational characterization for the full class of spectrally positive infinitely divisible laws, as well as fixed two-point jump examples exhibiting interior optimizers. Those facts are acknowledged as prior work; they alone do not state the moving-parameter logarithmic transition with unbounded spike size, its universal profile, or the all-moment/optimal-scale discontinuity. The present finding obtains those consequences through the uniform two-regime maximization argument and a matched asymptotic calculation. Leskelä and Välimaa (2026) study a distinct optimal variance-proxy notion for sub-Poisson laws, principally unit-jump models. Arbel, Marchal and Nguyen (2020) study optimal sub-Gaussian variance proxies for bounded variables rather than fixed-variance sub-gamma scales. These differences are claim-based, not title-based.

## Limitations

The scale concerns only the right-hand sub-gamma inequality with the quadratic coefficient fixed at the **true variance**. It is not the optimum among freely varying pairs of variance and scale. The profile is pointwise for fixed \(s\); no second-order expansion for \(c_B\), location expansion for its optimizer, or uniform \(s\)-range is asserted. The result follows in part from a powerful existing variational formula; the possibility that another general concentration result implicitly contains the rare-spike asymptotic remains a priority risk. No independent scientific validation has been performed.

## References

1. Y. Chen, *Optimal Sub-Gamma Scales for Spectrally Positive Infinitely Divisible Laws*, arXiv:2610.00032v1 (first public 2026-09-02), https://arxiv.org/html/2610.00032v1.
2. L. Leskelä and A. Välimaa, *Sub-Poisson Distributions: Concentration Inequalities, Optimal Variance Proxies, and Closure Properties*, arXiv:2508.12103; Sankhya A (2026), https://link.springer.com/article/10.1007/s13171-026-00444-x.
3. J. Arbel, O. Marchal and H. D. Nguyen, *On strict sub-Gaussianity, optimal proxy variance and symmetry for bounded random variables*, ESAIM: Probability and Statistics 24 (2020), https://www.numdam.org/articles/10.1051/ps/2019018/.
