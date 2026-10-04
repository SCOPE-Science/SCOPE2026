# Exact finite-block formulas in a commuting correlated zero-Stein-rate family
## Finding
Let \(\rho=|\phi\rangle\langle\phi|\) be a pure state on a finite-dimensional Hilbert space and let \(\omega\) be faithful, with \([\rho,\omega]=0\) and \(\rho\ne\omega\). Fix \(0<c<1\), define
\[
q=\langle\phi|\omega|\phi\rangle\in(0,1),\qquad
\zeta_k=c\rho^{\otimes k}+(1-c)\omega^{\otimes k},
\]
and let \(\mathcal F_n\) be the correlated alternative family from Example 24 of Gao--Ji--Liu: partition the \(n\) labeled sites into blocks and assign to every block of size \(k\) either \(\zeta_k\) or \(\omega^{\otimes k}\), then take the convex hull. Put
\[
g_n=c+(1-c)q^n.
\]
Then, for every integer \(n\ge1\),
\[
\sup_{\sigma\in\mathcal F_n}\langle\phi|^{\otimes n}\sigma|\phi\rangle^{\otimes n}=g_n,
\]
and hence
\[
\inf_{\sigma\in\mathcal F_n}D(\rho^{\otimes n}\|\sigma)
=D_{\max}(\rho^{\otimes n}\|\mathcal F_n)
=-\log_2 g_n.
\]
For every \(0\le\varepsilon<1\), the optimal fixed-error type-II coefficient is
\[
\beta_{\varepsilon,n}=(1-\varepsilon)g_n.
\]
For the paper's trace-preserving smoothing specialized to states, for every \(0\le\delta\le2\),
\[
Z_n^\delta=\log_2\max\left\{1,\frac{1-\delta/2}{g_n}\right\}.
\]
In particular, \(Z_n^\delta=0\) exactly when \(\delta\ge2(1-g_n)\). The finite-block quantities therefore converge to nonzero constants while their normalized rates vanish:
\[
-\log_2 g_n\longrightarrow-\log_2 c,\qquad
\beta_{\varepsilon,n}\longrightarrow c(1-\varepsilon).
\]

## Assumptions and scope
The Hilbert space is finite-dimensional. The state \(\omega\) is positive definite, \(\rho\) is rank one, and the extra assumption beyond Example 24 is commutation \([\rho,\omega]=0\). Faithfulness and \(\rho\ne\omega\) then imply \(0<q<1\). The logarithms are base two. The testing convention is that an effect \(0\le Q\le I\) must satisfy \(\operatorname{Tr}(Q\rho^{\otimes n})\ge1-\varepsilon\), and the worst-case alternative acceptance is minimized. The smoothing radius uses the full trace norm in the state specialization; this is the one-dimensional-input reduction of the paper's diamond norm. The statement is finite-block and does not require an asymptotic limit.

## Proof
Because \([\rho,\omega]=0\), the target ray \(|\phi\rangle\) is an eigenvector of \(\omega\) with eigenvalue \(q\). Hence \(|\phi\rangle^{\otimes k}\) is an eigenvector of \(\zeta_k\) with eigenvalue
\[
g_k=c+(1-c)q^k.
\]
For an extreme point of \(\mathcal F_n\), the target overlap factors over its blocks. Replacing a block \(\omega^{\otimes k}\) by \(\zeta_k\) strictly increases that factor because \(g_k>q^k\). Moreover, for positive integers \(a,b\),
\[
g_{a+b}-g_ag_b=c(1-c)(1-q^a)(1-q^b)\ge0.
\]
Thus merging two \(\zeta\)-blocks cannot decrease the overlap. Repeated replacement and merging show that every extreme point has target overlap at most \(g_n\), while the single-block state \(\zeta_n\) attains \(g_n\). Convexity preserves the bound.

Every \(\sigma\in\mathcal F_n\) commutes with \(\rho^{\otimes n}\). If its target overlap is \(p\), then the target ray is an eigenvector of \(\sigma\) with eigenvalue \(p\), and therefore
\[
D(\rho^{\otimes n}\|\sigma)=-\log_2 p.
\]
Minimizing gives \(-\log_2g_n\). Likewise, \(\rho^{\otimes n}\le\lambda\sigma\) forces \(1\le\lambda p\), so \(\lambda\ge1/g_n\). The choice \(\sigma=\zeta_n\) satisfies \(\rho^{\otimes n}\le g_n^{-1}\zeta_n\), proving the same exact value for the optimized max-relative entropy.

Write
\[
\zeta_n=g_n\rho^{\otimes n}+(1-g_n)\nu_n,
\]
where \(\nu_n\) is a state supported orthogonally to the target ray. For any feasible test \(Q\),
\[
\operatorname{Tr}(Q\zeta_n)\ge g_n\operatorname{Tr}(Q\rho^{\otimes n})\ge g_n(1-\varepsilon),
\]
so \(\beta_{\varepsilon,n}\ge g_n(1-\varepsilon)\). Conversely, the effect \(Q=(1-\varepsilon)\rho^{\otimes n}\) is feasible and has acceptance at most \((1-\varepsilon)g_n\) on every free state, proving equality.

For smoothing, let \(L\) be any state with \(\|L-\rho^{\otimes n}\|_1\le\delta\), and suppose \(L\le\lambda\sigma\) for some \(\sigma\in\mathcal F_n\). Since \(L-\rho^{\otimes n}\) has trace zero,
\[
\langle\phi|^{\otimes n}L|\phi\rangle^{\otimes n}\ge1-\delta/2.
\]
The target-overlap bound then gives \(1-\delta/2\le\lambda g_n\); trace preservation also forces \(\lambda\ge1\). Hence
\[
Z_n^\delta\ge\log_2\max\left\{1,\frac{1-\delta/2}{g_n}\right\}.
\]
For the reverse inequality, set
\[
s=\min\left\{1,\frac{\delta}{2(1-g_n)}\right\},\qquad
L_s=(1-s)\rho^{\otimes n}+s\zeta_n.
\]
Orthogonality gives \(\|L_s-\rho^{\otimes n}\|_1=2s(1-g_n)\le\delta\). With \(\alpha=1-s(1-g_n)\), the target eigenvalue of \(L_s\) is \(\alpha\), while its orthogonal part is \(s\) times that of \(\zeta_n\). Therefore
\[
L_s\le\max\left\{1,\frac{\alpha}{g_n}\right\}\zeta_n.
\]
If \(\delta<2(1-g_n)\), then \(\alpha=1-\delta/2\); if \(\delta\ge2(1-g_n)\), choose \(s=1\) and \(L_s=\zeta_n\). This matches the lower bound and proves the formula.

## Verification
The proof is symbolic and covers all finite dimensions satisfying the stated commutation assumption. The accompanying checker enumerates all block-size compositions and \(\zeta/\omega\) assignments through \(n=8\) on several parameter grids, verifies the merge identity numerically, and checks that the explicit smoothing construction attains the lower bound. These computations are corroborative only; the universal statements follow from the algebra above.

## Relationship to prior work
Gao, Ji, and Liu introduced exactly this correlated family in Example 24 of arXiv:2609.30762v1 to demonstrate that persistent correlations can force zero Stein rate even when the pure target lies outside the one-use free set. Their displayed finite-block conclusions are the inequalities \(0\le E_n\le\log_2(1/c)\), \(\beta_{\varepsilon,n}\ge c(1-\varepsilon)\), and the vanishing regularized rate. The formulas above strictly sharpen those bounds on the natural commuting subfamily and additionally determine the optimized max-relative entropy and its full trace-preserving smoothing profile.

Frenkel, Mosonyi, Vrana, and Weiner study composite i.i.d. quantum hypothesis testing and emphasize exact single-copy behavior in the finite-dimensional commuting classical case. Their setting does not contain the partition-generated correlated family above, and their results do not imply the finite-block overlap, testing, or smoothing formulas here. Kanazawa and Yamasaki analyze probabilistic mixtures of i.i.d. null sources asymptotically; that mixed-source problem is structurally different from a fixed pure target tested against the present correlated composite alternative family.

## Limitations
The exact reduction uses \([\rho,\omega]=0\). No corresponding formula is claimed for the noncommuting version of Example 24. The result concerns the specific partition-generated family \(\mathcal F_n\); it does not assert a universal formula for correlated composite hypotheses. The finite enumeration in the checker is not part of the proof. Older classical non-i.i.d. hypothesis-testing literature may contain equivalent overlap observations under different language, although the checked sources and database searches did not reveal this exact family or the joint entropy/testing/smoothing profile.

## References
1. M. Gao, Z. Ji, and C. Liu, “A Generalized Stein Lemma for Quantum Channels,” arXiv:2609.30762v1, 25 September 2026. Example 24 and the definition of trace-preserving smoothed max-relative entropy are the direct source context.
2. P. E. Frenkel, M. Mosonyi, P. Vrana, and M. Weiner, “Error bounds for composite quantum hypothesis testing and a new characterization of the weighted Kubo-Ando geometric means,” arXiv:2503.13379v1, 17 March 2025.
3. H. Kanazawa and H. Yamasaki, “Generalized quantum Stein's lemma for mixed sources,” arXiv:2605.20776v1, 20 May 2026.
