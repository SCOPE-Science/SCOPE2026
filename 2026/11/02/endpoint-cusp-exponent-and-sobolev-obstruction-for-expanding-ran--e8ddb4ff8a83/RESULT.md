# Endpoint cusp exponent and Sobolev obstruction for expanding random interval maps

## Finding

An expanding two-full-branch cusp family has an unavoidable endpoint singularity in its stationary density, even when its cusp is weaker than the square-root cusp for which stronger response estimates have been established. The exponent and leading coefficient are explicit and persist under arbitrary finite Bernoulli mixtures with a common cusp exponent.

**Theorem.** Fix \(1/2<\alpha<1\), a positive integer \(m\), parameters \(1<\theta_j<2\) and weights \(\pi_j\ge0\) for \(1\le j\le m\), with \(\sum_j\pi_j=1\). Set \(c=1/2\) and
\[
 A_j=2^\alpha(1-\theta_j/2)>0,
 \qquad f_j(c\pm t)=1-\theta_jt-A_jt^\alpha \quad(0\le t\le c).
\]
For each \(j\), let \(\mathcal L_j\) be the Lebesgue Perron--Frobenius operator of \(f_j:[0,1]\to[0,1]\), and let \(\mathcal L=\sum_j\pi_j\mathcal L_j\). For **every** nonnegative normalized stationary density \(h\in BV([0,1])\), meaning \(\int_0^1h(x)\,dx=1\) and \(\mathcal Lh=h\) almost everywhere, the canonical representative is continuous and strictly positive on \((0,1)\), and
\[
 h(1-z)=C_{\alpha,\pi,\theta}\,z^\gamma+o(z^\gamma)
 \quad(z\downarrow0), \qquad
 \gamma=\frac{1-\alpha}{\alpha}\in(0,1),
\]
where
\[
 C_{\alpha,\pi,\theta}=\frac{2h(c)}{\alpha}\sum_{j=1}^{m}\pi_j A_j^{-1/\alpha}>0.
\]
Consequently the stationary mass near the cusp image satisfies
\[
 \int_{1-z}^1h(x)\,dx\sim
 2h(c)\left(\sum_j\pi_jA_j^{-1/\alpha}\right)z^{1/\alpha}.
\]
The exact one-sided pointwise Hölder exponent of \(h\) at \(1\) is \(\gamma\). In particular,
\[
 h\notin W^{1,p}(0,1)\quad\text{for every}\quad
 p\ge p_{\mathrm{obs}}:=\frac{\alpha}{2\alpha-1},
\]
including \(p=\infty\); hence \(h\notin W^{2,1}(0,1)\). The asserted Sobolev threshold is an **exclusion bound**, not a claim of membership below it.

## Assumptions and scope

The maps are continuous on \([0,1]\), have exactly two monotone full branches onto \([0,1]\), and are differentiable away from their shared turning point \(c\). Indeed \(f_j(c)=1\) and \(f_j(0)=f_j(1)=0\), while on either branch
\[
 |f'_j(c\pm t)|=\theta_j+\alpha A_jt^{\alpha-1}
 \ge 2\alpha+(1-\alpha)\theta_j>1.
\]
Their unique normalized invariant densities for individual maps are standard consequences of bounded-variation expanding-map theory; for mixtures, the theorem is formulated for every normalized stationary BV density and does not claim a new existence or uniqueness theorem. All nonzero mixture weights are allowed, including deterministic cases. No random-in-time sample-path regularity or parameter differentiability is asserted. In terms of the customary cusp exponent \(\beta=\alpha-1\), the range is \(-1/2<\beta<0\).

## Proof

**(1) Exact inverse branches and expansion.** Given \(x=1-z\), \(0<z<1\), the two preimages under map \(f_j\) are \(c\pm t_j(z)\), where \(t_j(z)\in(0,c)\) is uniquely defined by
\[
 z=\theta_jt_j(z)+A_jt_j(z)^\alpha.
\]
The inverse derivative weight for either branch is
\[
 w_j(z)=\bigl(\theta_j+\alpha A_jt_j(z)^{\alpha-1}\bigr)^{-1}.
\]
Since \(\alpha<1\), as \(z\downarrow0\),
\[
 t_j(z)\sim (z/A_j)^{1/\alpha},\qquad
 w_j(z)\sim \frac{A_j^{-1/\alpha}}{\alpha}z^{(1-\alpha)/\alpha}.
\]
These are genuine positive asymptotic equivalences, including all multiplicative constants.

**(2) No interior jumps for stationary BV densities.** Each branch weight is continuous on its image \((0,1)\) and has supremum at most \(\rho_j=\bigl(2\alpha+(1-\alpha)\theta_j\bigr)^{-1}<1\). Let \(J(v)\) be the sum of absolute sizes of all jumps of the canonical regulated representative of a BV function \(v\) at points of \((0,1)\). A jump of \(v\) away from \(c\) propagates under each \(\mathcal L_j\) to only one branch image, with size at most \(\rho_j\) times its old size. A jump at \(c\) can affect only the endpoint \(1\), not the interior. Distinct jump images can cancel, so the triangle inequality gives
\[
 J(\mathcal Lv)\le \sum_j\pi_j\rho_j J(v)\le \rho J(v),
 \quad \rho:=\max_j\rho_j<1.
\]
For a stationary BV function, equality almost everywhere identifies its canonical one-sided limits, hence \(J(h)=J(\mathcal Lh)\le\rho J(h)\). Thus \(J(h)=0\). A BV function without jumps is continuous in the interior; choosing the continuous representative, the stationarity equation holds pointwise on \((0,1)\), because its right-hand side is also continuous there.

**(3) Strict interior positivity.** Suppose \(h(x_0)=0\) at an interior point. The transfer equation is a nonnegative sum. Select any \(j\) with \(\pi_j>0\): both inverse images of \(x_0\) under \(f_j\) must have density zero. Iterating shows that \(h\) vanishes at all \(n\)-step inverse images of \(x_0\) under \(f_j\), for every \(n\). Because this map has two uniformly contracting inverse branches with images covering \([0,1]\), its cylinder intervals have uniformly shrinking lengths and cover \([0,1]\) at every level; the inverse images of \(x_0\) are dense. Continuity then implies \(h\equiv0\) in \((0,1)\), contradicting normalization. Therefore \(h(c)>0\) and indeed \(h(x)>0\) for all interior \(x\).

**(4) Endpoint asymptotics.** Applying the pointwise stationary equation at \(x=1-z\) gives
\[
 h(1-z)=\sum_j\pi_j w_j(z)
 [h(c-t_j(z))+h(c+t_j(z))].
\]
The bracket tends to \(2h(c)>0\), while step (1) gives the weight asymptotics, proving the claimed exact constant and power. In particular the continuous endpoint extension is \(h(1)=0\). Integrating the positive asymptotic gives the mass formula and its constant, since \(\gamma+1=1/\alpha\).

**(5) Pointwise sharpness and Sobolev obstruction.** The positive finite limit \(\lim_{z\downarrow0}h(1-z)/z^\gamma=C_{\alpha,\pi,\theta}\) establishes exactly the one-sided pointwise Hölder exponent \(\gamma\), with no larger exponent possible. If \(h\in W^{1,p}(0,1)\) for finite \(p\ge\alpha/(2\alpha-1)=1/(1-\gamma)>1\), the absolutely continuous representative has endpoint trace zero and Hölder's inequality forces
\[
 |h(1-z)|\le z^{1-1/p}
 \left(\int_{1-z}^1|h'(x)|^p\,dx\right)^{1/p}
 =o(z^{1-1/p})=o(z^\gamma),
\]
a contradiction. For \(p=\infty\), Lipschitz continuity similarly contradicts \(0<\gamma<1\). Finally, the one-dimensional embedding \(W^{2,1}\hookrightarrow C^1\) on a compact interval implies Lipschitz regularity, again impossible. This proves every asserted exclusion.

## Verification

The analytical proof above proves the asymptotic for every \(m\), every permitted parameter set, and every normalized stationary BV density. The bundled standalone `check.py` uses 70-decimal arithmetic on a two-map example \(\alpha=3/4\), \(\theta_1=6/5\), \(\theta_2=17/10\), and weights \((2/5,3/5)\). It checks geometry, inverse equations, five asymptotic scales, and the exclusion exponent \(p_{\mathrm{obs}}=3/2\), producing 19 finite consistency assertions. It checks the transfer kernel on a smooth test input, **not** a constructed stationary density; the finite experiment does not prove the infinite statement.

## Relationship to prior work

Oltiboev--Rakhimov--Ruziboev (2026, arXiv:2608.26969) analyze random systems with cusps and state strong Sobolev-space spectral properties in the stronger-cusp parameter range \(\beta<-1/2\). Oltiboev--Vafoyev (2026, arXiv:2610.23180) develop critical-cusp cancellation and analytic response at \(\beta=-1/2\); their PDF gives the same two-full-branch family in that critical regime. Oltiboev (2025, arXiv:2505.17462) studies single-map cusp response with hypotheses that do not include \(-1/2<\beta<0\). The classical cusp family in Antoniou--Shkarin--Yarevsky (2001, arXiv:nlin/0106039) has another formula and a smooth explicit invariant density. This theorem isolates the **opposite-side** cusp range, the exact endpoint coefficient, a strictly sub-Lipschitz exponent, and a sharp necessary Sobolev exclusion. Those are not implications of the accessed statements in the cited papers. Priority against unindexed specialized density-regularity literature is not established.

## Limitations

The result requires a nonnegative normalized stationary density of bounded variation; it is not an existence result for arbitrary random mixture models. It does not establish Sobolev membership for exponents below \(p_{\mathrm{obs}}\), nor any linear-response conclusion, nor the limiting exponent \(\alpha=1/2\) or the smooth endpoint \(\alpha=1\). Full text of arXiv:2608.26969 was not accessible for inspection during preparation; its publicly indexed abstract and the later 2026 paper were used for the stated prior-art comparison. Independent review of mathematical novelty and generalizability remains appropriate.

## References

1. D. Oltiboev, K. Rakhimov, M. Ruziboev, *Linear response for random systems with a cusp*, arXiv:2608.26969v1 (first posted 2026-08-27). https://arxiv.org/abs/2608.26969
2. D. Oltiboev, N. Vafoyev, *Critical cusp cancellation and analytic response for a Bernoulli random interval map*, arXiv:2610.23180v1 (2026). https://arxiv.org/abs/2610.23180
3. D. Oltiboev, *Linear response for systems with a cusp*, arXiv:2505.17462v1 (2025). https://arxiv.org/abs/2505.17462
4. I. Antoniou, S. Shkarin, E. Yarevsky, *Resonances of the cusp family*, arXiv:nlin/0106039v1 (2001). https://arxiv.org/abs/nlin/0106039
5. M. Rychlik, *Bounded variation and invariant measures*, Studia Mathematica 76 (1983), 69–80.
