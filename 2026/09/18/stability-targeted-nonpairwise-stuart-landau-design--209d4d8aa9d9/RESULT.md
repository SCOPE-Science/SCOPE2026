# Stability-targeted nonpairwise coupling collapses the synchrony-splay overlap

## Statement

Consider the unweighted all-to-all three-oscillator phase model obtained from the engineered Stuart-Landau system in arXiv:2609.20632v1, specialized as in its coupling-design section to straight isochrones, no self-coupling, and identical pairwise/nonpairwise weights. Retain the source paper's second-order phase vector field and write the engineered physical-nonpairwise strength as \(\eta\). For oscillator 1 the reduced dynamics are Eq. (21) of the source, with cyclic analogues for oscillators 2 and 3.

Let \(\rho\) denote the pairwise coupling phase lag, \(a>0\) the Stuart-Landau radial relaxation parameter, and \(\varepsilon>0\) the pairwise coupling strength. The transverse eigenvalue of full synchrony is
\[
\lambda_{\rm sync}
=-3\varepsilon\cos\rho
+\left(6\eta-\frac{9\varepsilon^2}{2a}\right)\sin^2\rho.
\]
At the three-oscillator splay state \((0,2\pi/3,4\pi/3)\), the two nontrivial eigenvalues form a conjugate pair with
\[
\operatorname{Re}\lambda_{\rm splay}
=\frac32\varepsilon\cos\rho
+6\eta\sin^2\rho
+\frac{9\varepsilon^2}{8a}\cos 2\rho,
\]
\[
\operatorname{Im}\lambda_{\rm splay}
=\mp\frac{3\varepsilon}{4a}
\left(2a+3\varepsilon\cos\rho\right)\sin\rho.
\]
These formulas are exact for the second-order truncated phase model.

If \(\eta=\kappa\varepsilon^2/a\), the two marginal-stability boundaries near the first-order Kuramoto transition \(\rho=\pi/2\) satisfy
\[
\rho_{\rm sync}
=\frac\pi2+\left(\frac32-2\kappa\right)\frac{\varepsilon}{a}
+O\!\left((\varepsilon/a)^2\right),
\]
\[
\rho_{\rm splay}
=\frac\pi2+\left(4\kappa-\frac34\right)\frac{\varepsilon}{a}
+O\!\left((\varepsilon/a)^2\right).
\]
Hence their local stability-overlap width is
\[
\rho_{\rm sync}-\rho_{\rm splay}
=\left(\frac94-6\kappa\right)\frac{\varepsilon}{a}
+O\!\left((\varepsilon/a)^2\right).
\]
The source paper chooses \(\kappa=1/4\), i.e. \(\eta=\varepsilon^2/(4a)\), because that value exactly cancels the asymmetric emergent nonpairwise harmonic and half of the symmetric one. For stability restoration, however, this leaves a leading overlap of
\[
\frac34\frac{\varepsilon}{a}+O((\varepsilon/a)^2),
\]
whereas
\[
\boxed{\eta_{\rm bal}=\frac{3\varepsilon^2}{8a}}
\]
cancels the entire leading-order synchrony-splay overlap.

There is also an exact finite-\(\varepsilon\) one-knob balance inside the same truncated phase model. Setting both marginal conditions to zero and writing \(x=\cos\rho\) eliminates \(\eta\) and gives
\[
2\varepsilon x^2-4ax-3\varepsilon=0.
\]
The weak-coupling root is
\[
\boxed{x_*=\frac{a-\sqrt{a^2+\tfrac32\varepsilon^2}}{\varepsilon}},
\qquad
\boxed{\rho_*=\arccos x_*},
\]
and the corresponding physical-nonpairwise strength is
\[
\boxed{
\eta_*
=\frac{\varepsilon x_*}{2(1-x_*^2)}
+\frac{3\varepsilon^2}{4a}.
}
\]
For sufficiently weak coupling this is positive and satisfies
\[
x_*=-\frac34\frac{\varepsilon}{a}+O((\varepsilon/a)^3),
\quad
\rho_*=\frac\pi2+\frac34\frac{\varepsilon}{a}+O((\varepsilon/a)^3),
\quad
\eta_*=\frac{3\varepsilon^2}{8a}+O(\varepsilon^4/a^3).
\]
Thus a single engineered strength can make the local linear-stability boundaries of synchrony and splay coincide exactly in the second-order phase model, even though a single strength cannot cancel all second-order harmonics.

## Derivation

For full synchrony, permutation symmetry makes the Jacobian have constant diagonal and constant off-diagonal entries. Subtracting an off-diagonal entry from a diagonal entry gives the doubly repeated transverse eigenvalue above. For the splay state, the Jacobian is circulant. If its first row is \((d,p,q)\), the nontrivial eigenvalues are \(d+p\omega+q\omega^2\) and its conjugate, where \(\omega=e^{2\pi i/3}\); hence \(\operatorname{Re}\lambda=d-(p+q)/2\). Substitution of Eqs. (8), (20), and (21) of arXiv:2609.20632v1 yields the displayed expressions.

Near \(\rho=\pi/2\), set \(\rho=\pi/2+\delta\), \(\delta=O(\varepsilon/a)\), and \(\eta=\kappa\varepsilon^2/a\). Expanding the two real stability exponents through order \(\varepsilon^2/a\) gives the stated boundary displacements. For the exact balance, substitute \(x=\cos\rho\), solve the synchrony equation for \(\eta\), and insert into the splay equation. The remaining factor is exactly \(2\varepsilon x^2-4ax-3\varepsilon\).

A related obstruction follows immediately. Keeping the synchronized boundary exactly at \(\rho=\pi/2\) requires \(\eta=3\varepsilon^2/(4a)\), whereas keeping the splay boundary exactly there requires \(\eta=3\varepsilon^2/(16a)\). Therefore no single scalar \(\eta\) can restore both individual boundaries to the first-order transition at second order. The balanced value instead makes the two boundaries meet at a shifted phase lag.

## Interpretation

The source paper's design objective is harmonic cancellation: its choice \(\eta=\varepsilon^2/(4a)\) exactly cancels one emergent nonpairwise harmonic and half of another, and numerically moves both phase-diagram boundaries toward the first-order Kuramoto transition. The calculation above identifies a distinct design objective, local stability matching. Under that objective, \(3/8\) replaces \(1/4\) as the leading coefficient, and the exact \(\eta_*\) gives the finite-coupling correction within the truncated model.

This does not contradict the source paper. Harmonic cancellation and stability-boundary cancellation are different optimization criteria because pairwise second-harmonic and self-interaction corrections also contribute to the Jacobians. The result quantifies that distinction and supplies an analytic one-parameter design rule targeted directly at the synchronized/splay stability diagram.

## Limitations

The exact formulas above concern the source paper's second-order truncated phase model with three identical oscillators, unweighted all-to-all coupling, straight isochrones, and the specific engineered PN motifs of Eq. (19). They do not prove that the full Stuart-Landau system has exactly coincident nonlinear basin boundaries at \(\eta_*\). Higher-order terms \(O(\varepsilon^3)\), \(O(\varepsilon\eta)\), and \(O(\eta^2)\) are omitted by the reduction, and local linear stability does not rule out other attractors or global multistability. The conclusion should therefore be read as a sharp second-order phase-design result and a prediction for weakly coupled physical oscillators.

## Reproducibility

`artifacts/verify_stability_design.py` reconstructs the unweighted Eq. (21) phase vector field symbolically, differentiates it at synchrony and splay, verifies the transverse eigenvalue formulas, eliminates \(\eta\) from the two marginality conditions, and checks the exact and asymptotic balanced design. `artifacts/verification_output.txt` records representative symbolic and numerical output.

## References

1. R. Muolo, H. Nakao, C. Bick, *Physical and emergent nonpairwise interactions in oscillator networks: from higher-order phase reduction to coupling design*, arXiv:2609.20632v1 (2026). https://arxiv.org/abs/2609.20632
2. C. Bick, T. Böhle, C. Kuehn, *Higher-Order Network Interactions Through Phase Reduction for Oscillators with Phase-Dependent Amplitude*, Journal of Nonlinear Science 34 (2024). https://doi.org/10.1007/s00332-024-10053-3
3. C. Bick, P. Ashwin, A. Rodrigues, *Chaos in generically coupled phase oscillator networks with nonpairwise interactions*, Chaos 26, 094814 (2016). https://doi.org/10.1063/1.4958928
4. C. Bick, T. Böhle, C. Kuehn, *Phase Oscillator Networks with Nonlocal Higher-Order Interactions: Twisted States, Stability, and Bifurcations*, SIAM Journal on Applied Dynamical Systems 22 (2023), 1590–1638. https://doi.org/10.1137/22M1500940
