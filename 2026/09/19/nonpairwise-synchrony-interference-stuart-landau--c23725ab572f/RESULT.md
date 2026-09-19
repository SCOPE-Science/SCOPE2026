# Exact synchrony interference law and stability-neutralizing coupling in three Stuart--Landau phases

## Setting

Muolo, Nakao and Bick [1] study three identical Stuart--Landau oscillators with pairwise linear coupling and physical nonpairwise (PN) cubic coupling. For straight isochrones and unit all-to-all weights, their mixed phase reduction keeps the pairwise interaction to second order in its strength \(\varepsilon\) and the asymmetric PN interaction to first order in its independent strength \(\eta\). The PN phase shift is denoted by \(\xi\), while the pairwise phase shift is \(\varrho\). The source fixes \(\xi=0\) in its phase diagrams and explicitly leaves a dedicated analysis of the constructive/destructive interference between physical and emergent nonpairwise harmonics for future work.

Write the phase equation in the source normalization as
\[
\dot\vartheta_j=\omega+\varepsilon f^{(1)}_j+\varepsilon^2 f^{(2)}_j+\eta f^{(\mathrm{PN})}_j,
\]
where \(a>0\) is the Stuart--Landau radial parameter. We consider the source's unit-weight three-oscillator specialization.

## 1. Exact transverse synchrony exponent for the mixed PN--EN model

At full synchrony \(\vartheta_1=\vartheta_2=\vartheta_3\), global phase-shift invariance gives one zero eigenvalue. The remaining two eigenvalues coincide. Direct differentiation of the source's Eqs. (8) and (15) gives the double transverse eigenvalue
\[
\boxed{
\lambda_\perp
=-3\varepsilon\cos\varrho
-\frac{9\varepsilon^2}{2a}\sin^2\varrho
-3\eta\cos\xi .
}
\]
Consequently, within the mixed-order phase model, full synchrony is linearly asymptotically stable in phase-difference space precisely when
\[
\boxed{
\varepsilon\cos\varrho
+\eta\cos\xi
+\frac{3\varepsilon^2}{2a}\sin^2\varrho>0.
}
\]

This resolves the PN--EN interference at the synchrony boundary in closed form. In particular:

- \(\xi=0\) makes positive \(\eta\) maximally stabilizing at linear order;
- \(\xi=\pi\) makes it maximally destabilizing;
- \(\xi=\pi/2\) or \(3\pi/2\) makes the asymmetric PN term invisible to the linear stability of full synchrony, even though it remains present nonlinearly in the phase dynamics.

For \(\varepsilon>0\), the stability boundary connected to the first-order Kuramoto edge can also be written explicitly as
\[
\boxed{
\cos\varrho_c
=\frac{a-\sqrt{a^2+6a\eta\cos\xi+9\varepsilon^2}}{3\varepsilon},
}
\]
whenever the square root is real and this branch lies in \([-1,1]\). If the physically natural mixed scaling \(\eta=q\varepsilon^2\) is imposed, then
\[
\boxed{
\varrho_c
=\frac{\pi}{2}
+\varepsilon\left(\frac{3}{2a}+q\cos\xi\right)
+O(\varepsilon^3).
}
\]
Thus the phase \(\xi\) changes the leading finite-coupling displacement of the synchrony edge, not merely the amplitude of a nonlinear transient.

The \(\eta=0\) part is not claimed as new: after matching coupling and radial-relaxation normalizations, it agrees with the second-order synchrony exponent obtained for pairwise-coupled Stuart--Landau oscillators by Bick, Böhle and Kuehn [2]. The source-specific refinement is the exact PN contribution and its interference with that established emergent correction.

## 2. A stability-neutralizing coupling design

The source also proposes an engineered PN combination, Eqs. (19)--(21), intended to compensate second-order emergent nonpairwise terms. For unit weights its first-order PN phase contribution is
\[
\begin{aligned}
f^{(\mathrm{eng})}_1={}&
-\sin(2\vartheta_2-\vartheta_3-\vartheta_1)
-\sin(2\vartheta_3-\vartheta_2-\vartheta_1)\\
&+\sin(\vartheta_2+\vartheta_3-2\vartheta_1+2\varrho),
\end{aligned}
\]
with cyclic permutations for the other oscillators. Its transverse contribution at synchrony is exactly
\[
6\eta\sin^2\varrho.
\]
Hence the engineered phase model has
\[
\boxed{
\lambda_\perp^{\mathrm{eng}}
=-3\varepsilon\cos\varrho
-\frac{9\varepsilon^2}{2a}\sin^2\varrho
+6\eta\sin^2\varrho.
}
\]

The source chooses
\[
\eta_{\mathrm{harm}}=\frac{\varepsilon^2}{4a}
\]
to cancel one emergent asymmetric harmonic exactly and half of the symmetric harmonic. At synchrony this leaves
\[
\boxed{
\lambda_\perp^{\mathrm{eng}}(\eta_{\mathrm{harm}})
=-3\varepsilon\cos\varrho
-\frac{3\varepsilon^2}{a}\sin^2\varrho.
}
\]
Thus this harmonic-matching design removes one third of the second-order displacement of the synchrony boundary and leaves two thirds of it at linear level.

If the design objective is instead *local synchrony stability*, a different single strength is exact in the truncated model:
\[
\boxed{
\eta_{\mathrm{stab}}=\frac{3\varepsilon^2}{4a}.
}
\]
Indeed,
\[
\boxed{
\lambda_\perp^{\mathrm{eng}}(\eta_{\mathrm{stab}})
=-3\varepsilon\cos\varrho.
}
\]
Therefore \(\eta_{\mathrm{stab}}\) restores the first-order synchrony boundary
\[
\boxed{\varrho_c=\pi/2}
\]
*exactly within the source's second-order engineered phase model*, for every \(\varrho\), rather than merely moving the observed boundary toward it. This stability-targeted strength is exactly three times the source's harmonic-cancellation strength.

The two designs optimize different objects: \(\eta_{\mathrm{harm}}\) cancels selected Fourier motifs, whereas \(\eta_{\mathrm{stab}}\) cancels the total second-order transverse Jacobian at full synchrony. There is no contradiction with the source's statement that a single PN strength cannot cancel the complete second-order phase vector field.

## Verification

A standalone SymPy verifier reconstructs the unit-weight second-order term from the source's Eq. (8), differentiates the mixed and engineered phase equations at synchrony, checks the zero row sum required by global phase-shift invariance, and verifies both design substitutions exactly. Its output is included in `artifacts/verification.txt`.

## Scope and limitations

The result is a theorem about the source's displayed mixed-order and engineered **phase reductions**, not about the full finite-coupling Stuart--Landau system to all orders. Terms of order \(O(\varepsilon^3)\), \(O(\varepsilon\eta)\), and \(O(\eta^2)\), which the source itself identifies as omitted from the mixed reduction, can move the true full-system boundary. The stability-neutralizing choice restores only the local full-synchrony boundary of the truncated phase model; it does not claim to restore the incoherent-state boundary, basin geometry, or the full phase diagram.

General higher-order phase reductions and synchrony-stability corrections are established prior art [2,3]. The originality claim is deliberately restricted to the source-specific PN--EN interference formula above and the distinction between harmonic cancellation and the stability-neutralizing strength for arXiv:2609.20632v1.

## References

1. R. Muolo, H. Nakao, C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1 (2026). https://arxiv.org/abs/2609.20632v1
2. C. Bick, T. Böhle, C. Kuehn, *Higher-Order Network Interactions Through Phase Reduction for Oscillators with Phase-Dependent Amplitude*, Journal of Nonlinear Science **34**, 77 (2024). https://doi.org/10.1007/s00332-024-10053-3
3. I. León, R. Muolo, Y. Zhang, M. Lucas, *Symmetry-based selection rules for higher-order interactions in coupled oscillators*, arXiv:2606.04904 (2026). https://arxiv.org/abs/2606.04904
