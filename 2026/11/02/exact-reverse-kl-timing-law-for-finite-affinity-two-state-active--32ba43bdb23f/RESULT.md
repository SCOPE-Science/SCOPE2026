# Exact reverse-KL timing law for finite-affinity two-state active-matter battery charging

## Finding

A finite-affinity, two-state active-matter battery admits a **unique efficiency-optimal stopping time** at every positive housekeeping cost. This time is always later than the maximum stored-charge-power time. It moves strictly and continuously from infinite duration toward the maximum-power time as the maintenance cost grows. Its exact inverse calibration uses the *reverse* Bernoulli relative entropy, not a linear-response approximation.

Write \(F_\infty=D_{\mathrm{KL}}(r\Vert q)\), \(G_\infty=D_{\mathrm{KL}}(q\Vert r)\), and \(B=F_\infty+G_\infty\). The principal sharp limits, for fixed distinct interior populations, are
\[
s_\chi=\log\frac{BG_\infty}{\chi F_\infty}+o(1)\quad(\chi\downarrow0),
\]
\[
\eta_{\max}(\chi)=\frac{F_\infty}{B}-\frac{F_\infty\chi}{B^2}\left[\log\frac{BG_\infty}{\chi F_\infty}+1\right]+o(\chi),
\]
and, for large housekeeping cost,
\[
s_\chi=s_P+\frac{B e^{-s_P}G(s_P)}{\chi[-s_PF''(s_P)]}+O(\chi^{-2}),
\qquad
\eta_{\max}(\chi)=\frac{F(s_P)}{\chi s_P}-\frac{BF(s_P)(1-e^{-s_P})}{\chi^2s_P^2}+O(\chi^{-3}).
\]

## Assumptions and scope

Fix \(0<q<r<1\). In the physical two-state battery of the motivating paper, \(q=[1+\exp(\beta E)]^{-1}\), \(r=[1+\exp(\beta(E-a))]^{-1}\), and dimensionless time is \(s=\lambda_c t\). The physically relevant parameters \(\beta,E,a,\lambda_c>0\) imply \(0<q<1/2<1\), \(q<r<1\); the mathematical theorem also holds for any interior \(q<r\). The maintenance rate is \(\chi=\beta\mathcal P_{\mathrm{hk}}/\lambda_c>0\). There are no time-dependent controls or changes to the two-state relaxation law.

Set \(\Delta=r-q\), \(U(s)=1-e^{-s}\), \(P(s)=q+\Delta U(s)\), \(\operatorname{logit}(p)=\log[p/(1-p)]\), and \(B=\Delta[\operatorname{logit}(r)-\operatorname{logit}(q)]>0\). For \(p,q\in(0,1)\), let \(D_{\mathrm{KL}}(p\Vert q)=p\log(p/q)+(1-p)\log[(1-p)/(1-q)]\) denote Bernoulli divergence in natural logarithms. Define \(F(s)=D_{\mathrm{KL}}(P(s)\Vert q)\) and \(G(s)=D_{\mathrm{KL}}(q\Vert P(s))\). The dimensionless charging efficiency is
\[
\eta_\chi(s)=\frac{F(s)}{B U(s)+\chi s},\qquad s>0.
\]
The stored-charge-power objective is \(F(s)/s\). Limits below are pointwise for fixed \(q,r\), with no uniformity claimed at \(q=0\), \(r=1\), or \(r=q\).

**Theorem.** There is a unique maximum-power time \(s_P\in(0,\infty)\), characterized by \(s_PF'(s_P)=F(s_P)\), with \(F''(s_P)<0\). For every \(\chi>0\), efficiency has a unique global maximizer \(s_\chi>s_P\). The strictly decreasing continuous bijection \(\chi\mapsto s_\chi\) has inverse
\[
\chi=\frac{B e^{-s}G(s)}{F(s)-sF'(s)},\qquad s\in(s_P,\infty).
\]
The asymptotic expansions in the Finding section hold, and \(F_\infty+G_\infty=B\).

## Proof

**1. Derivatives and a one-crossing geometry.** Write \(\Phi(p)=\operatorname{logit}(p)-\operatorname{logit}(q)>0\) for \(p>q\). Since \(P'(s)=\Delta e^{-s}=r-P(s)\), direct differentiation gives
\[
F'(s)=\Delta e^{-s}\Phi(P(s)),\qquad
F''(s)=\Delta e^{-s}\left[-\Phi(P(s))+\frac{\Delta e^{-s}}{P(s)(1-P(s))}\right].
\]
Define
\[
T(s)=\frac{r-P(s)}{P(s)(1-P(s))\Phi(P(s))}.
\]
Factor \(T(s)=[(r-P(s))/(1-P(s))][1/(P(s)\Phi(P(s)))]\). Both positive factors are strictly decreasing in \(P(s)\in(q,r)\), because the first derivative has sign \(r-1<0\) and \(p\Phi(p)\) increases. Thus \(T\) strictly decreases from \(+\infty\) to \(0\). In particular, \(d\log F'/ds=T-1\), so \(F'\) increases and then decreases, exactly once.

Apply the derivative-ratio crossing argument to \(F(s)/s\). Set \(Z_P(s)=sF'(s)-F(s)\), so \(Z_P(0)=0\), \(Z'_P=sF''\); \(Z_P\) first increases and then strictly decreases to \(-F_\infty<0\). It has exactly one positive zero \(s_P\), which maximizes \(F(s)/s\). The zero is on the decreasing branch, so \(F''(s_P)<0\).

**2. Unique efficiency optimizer.** Let \(H(s)=BU(s)+\chi s\), with \(H'(s)=Be^{-s}+\chi>0\), and put
\[
R_\chi(s)=\frac{F'(s)}{H'(s)}=\frac{\Delta\Phi(P(s))}{B+\chi e^s}.
\]
Its logarithmic derivative is
\[
\frac{d}{ds}\log R_\chi(s)=T(s)-\frac{\chi e^s}{B+\chi e^s}.
\]
The first term decreases strictly from infinity to zero, while the second increases strictly toward one. Therefore \(R_\chi\) has exactly one maximum. For \(Z_\chi(s)=H(s)R_\chi(s)-F(s)\), differentiation gives \(Z'_\chi=H R'_\chi\). This function starts at zero, first rises, then strictly decreases to \(-F_\infty\), and thus has precisely one positive zero. Since \(\eta'_\chi=(H'/H^2)Z_\chi\), this zero is the unique global efficiency maximum. The endpoint limits \(\eta_\chi(s)\to0\) at both \(s\downarrow0\) and \(s\to\infty\) guarantee it is interior.

**3. Reverse-KL inverse and ordering.** An elementary two-point divergence identity yields
\[
(P-q)\Phi(P)=D_{\mathrm{KL}}(P\Vert q)+D_{\mathrm{KL}}(q\Vert P).
\]
Hence \(F'(s)U(s)-F(s)U'(s)=e^{-s}G(s)\), and the unnormalized efficiency derivative is
\[
H(s)^2\eta'_\chi(s)=B e^{-s}G(s)+\chi[sF'(s)-F(s)].
\]
At \(s_P\) it is strictly positive, proving \(s_\chi>s_P\). For \(s>s_P\), \(F(s)-sF'(s)>0\) and the stationary equation is exactly
\[
\chi=\frac{Be^{-s}G(s)}{F(s)-sF'(s)}.
\]
The right side is continuous, diverges as \(s\downarrow s_P\), and tends to zero as \(s\to\infty\). The preceding uniqueness theorem shows it assumes any positive value exactly once. Thus it is strictly decreasing and its inverse \(\chi\mapsto s_\chi\) is continuous and strictly decreasing, with range \((s_P,\infty)\).

**4. Sharp weak-housekeeping expansion.** At \(s\to\infty\), Taylor expansion at \(r\) gives \(F(s)=F_\infty-Be^{-s}+O(e^{-2s})\), \(G(s)=G_\infty+O(e^{-s})\), and \(F(s)-sF'(s)=F_\infty+O(se^{-s})\). Therefore the inverse law implies
\[
e^{-s_\chi}=\frac{\chi F_\infty}{B G_\infty}[1+o(1)],\qquad
s_\chi=\log\frac{BG_\infty}{\chi F_\infty}+o(1).
\]
Also
\[
\eta_\chi(s)=\frac{F_\infty}{B}-\frac{G_\infty}{B}e^{-s}-\frac{F_\infty}{B^2}\chi s+O(e^{-2s}+\chi s e^{-s}+\chi^2s^2).
\]
Since \(s_\chi=O(\log(1/\chi))\) and \(e^{-s_\chi}=O(\chi)\), substituting the inverse law gives the stated \(\chi\log(1/\chi)\) leading loss and its exact order-\(\chi\) constant.

**5. Sharp strong-housekeeping expansion.** Set \(Q(s)=e^{-s}G(s)\) and \(J(s)=F(s)-sF'(s)\). Around \(s_P\), \(J(s)=(-s_PF''(s_P))(s-s_P)+O((s-s_P)^2)\). Since \(-s_PF''(s_P)>0\) and \(Q(s_P)>0\), the inverse law gives
\[
s_\chi=s_P+\frac{B Q(s_P)}{\chi[-s_PF''(s_P)]}+O(\chi^{-2}).
\]
Finally, uniformly near fixed \(s_P\),
\[
\eta_\chi(s)=\frac{F(s)}{\chi s}-\frac{B F(s)U(s)}{\chi^2s^2}+O(\chi^{-3}).
\]
The first quotient has zero derivative at \(s_P\), so the \(O(\chi^{-1})\) displacement of \(s_\chi\) changes its value only at order \(\chi^{-3}\). This proves the displayed two-term efficiency expansion. The identity \(B=F_\infty+G_\infty\) is the divergence identity from step 3 at \(P=r\). \(\square\)

## Verification

A standalone Python 3 standard-library program, `verify_optimum.py`, checks the inverse calibration, the maximum-power ordering, local and global finite-window comparisons, housekeeping monotonicity, and asymptotic predictions across six interior pairs of populations and multiple housekeeping strengths. The finite checks do **not** establish uniqueness or asymptotic quantifiers; those follow from the preceding analytic argument. Run `python3 verify_optimum.py` from a directory containing that standalone file.

## Relationship to prior work

Lin and collaborators, *Active-Matter Battery* (arXiv:2610.00428v1, submitted 2026-09-30), derive the two-state relaxation, work and information accounting. Their Appendix B optimizes charging efficiency in a **linear-response approximation** and discusses leading weak/strong housekeeping regimes. Here the finite-affinity binary-divergence objective is retained without expanding in the population or affinity gap. The new contribution is a proof of a unique optimum for every admissible finite gap, strict optimal-time comparative statics, an exact reverse-KL calibration, and source-sensitive two-term asymptotics at both maintenance-cost extremes.

Lei and collaborators, *Universal power-efficiency trade-off in battery charging* (Frontiers of Physics, 2025, DOI 10.15302/frontphys.2025.042202), study a charging power/efficiency optimization with an RC battery. That model is not the two-state active-matter battery with explicit steady housekeeping cost. The present proof uses elementary one-variable calculus and relative-entropy identities; no general priority claim is made for those tools themselves.

## Limitations

Only the specified exponential two-state relaxation with a constant positive housekeeping power is treated. Population parameters are fixed in all limits; no boundary-uniformity, changing controls, experimental implementation, or interacting many-state generalization is proved. The exact inverse relation is conditional on the model and does not establish a universal efficiency law. Scientific priority was assessed against identified published work, not independently exhaustively certified.

## References

1. Y.-Q. Lin et al., *Active-Matter Battery*, arXiv:2610.00428v1, publicly submitted 2026-09-30. https://arxiv.org/abs/2610.00428 (particularly the two-state construction and Appendix B).
2. Lei et al., *Universal power-efficiency trade-off in battery charging*, *Frontiers of Physics* (2025), DOI 10.15302/frontphys.2025.042202. https://doi.org/10.15302/frontphys.2025.042202.
