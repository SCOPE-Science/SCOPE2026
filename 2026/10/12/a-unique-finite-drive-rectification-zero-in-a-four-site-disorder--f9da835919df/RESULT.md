# A unique finite-drive rectification zero in a four-site disordered exclusion chain

## Finding

Consider the boundary-driven site-disordered symmetric exclusion process of Sakai and Akimoto [1] on four sites, with site waiting times \( (\tau_1,\tau_2,\tau_3,\tau_4)=(1,4,2,1)\), reservoir exchange time \(\tau_{\mathrm r}=1\), mean reservoir density \(1/2\), and reservoir density difference \(d\in[-1,1]\). Let \(J(d)\) be the unique stationary particle current, positive from left to right. Then

\[
J(d)=\frac{d\left(13777968+1394687d+351342d^2-6089d^3-1014d^4\right)}{D(d)},
\]
where
\[
D(d)=900d^6+7884d^5-326323d^4-2101164d^3-478618d^2+30025544d+285870765.
\]

Define the *current-reversal asymmetry* \(E(d)=J(d)+J(-d)\). There is a unique \(d_*\in(0,1)\) with \(E(d_*)=0\), and
\[
E(d)<0\quad(0<d<d_*),\qquad E(d)>0\quad(d_*<d\le 1).
\]
Specifically \(d_*\approx0.962445260153269\). Although the zero-bias equilibrium profile is spatially asymmetric, \((1/2,4/5,2/3,1/2)\), currents at the nonzero contrast \(d_*\) have exactly equal and opposite values. The sign reversal and a positive-contrast zero also occur in a nonempty open neighborhood of the indicated pair of bulk departure rates \((1/4,1/2)\), with equal boundary departure rates and reservoir contact times kept fixed.

## Assumptions and scope

There are four occupation variables \(\eta_i\in\{0,1\}\), and exclusion blocks attempted hops into occupied neighboring sites. A particle at site \(i\) jumps to each available nearest neighbor at rate \(1/(2\tau_i)\). At site 1 an empty site fills from the left reservoir at rate \((1+d)/4\), and an occupied site empties to that reservoir at rate \((1-d)/4\). At site 4 an empty site fills at rate \((1-d)/4\), and an occupied site empties at rate \((1+d)/4\). Thus the reservoir densities are \(\rho_{\mathrm L}=(1+d)/2\) and \(\rho_{\mathrm R}=(1-d)/2\), as in [1]. Rates and current use physical time, with no mean-field closure. All statements about uniqueness of the zero concern this specified four-site realization and this one-parameter reservoir drive; no uniqueness is claimed for arbitrary disorders.

For \(-1<d<1\), every boundary injection and extraction rate is positive. Together with positive interior hopping rates, this yields an irreducible continuous-time Markov chain on all \(16\) configurations and hence a unique stationary distribution. The rational formula also extends continuously to \(d=\pm1\), where it is finite.

## Proof

**Exact stationary-current identity.** Index each configuration by \(s=\sum_{j=1}^4 2^{j-1}\eta_j\), so \(s\in\{0,\ldots,15\}\). Introduce the *twice-physical-rate* generator \(Q(d)\): its off-diagonal entry for a permitted internal hop from site \(i\) is \(1/\tau_i\), its left injection and extraction rates are \((1+d)/2\) and \((1-d)/2\), respectively, and its right injection and extraction rates are reversed. The diagonal entry is minus the sum of the outgoing rates. Set \(A(d)\) equal to \(Q(d)^\mathsf T\) with row indexed 15 replaced by sixteen ones, and let \(e_{15}\) be the corresponding coordinate vector. The stationary probability column is the unique solution \(A(d)p(d)=e_{15}\).

For the bond between sites 2 and 3, the **physical** stationary current is
\[
J(d)=\frac12\sum_{s=0}^{15}p_s(d)\left[\frac14\eta_2(1-\eta_3)-\frac12\eta_3(1-\eta_2)\right].
\]
Exact rational Gaussian elimination in the indicated \(16\)-dimensional system gives the displayed rational expression for \(J(d)\). This is a finite algebraic identity, independently reproducible by the included verifier, which rebuilds the generator, solves its symbolic stationary equations, checks the rational identity, and checks stationary normalization and balance. In particular, this is an exact stationary current rather than a truncated perturbation series or a finite-sample estimate.

**Denominator and current signs.** For every \(|d|\le1\), the triangle inequality gives
\[
D(d)\ge285870765-(7884+326323+2101164+478618+30025544)=252931232>0.
\]
The factor multiplying \(d\) in the numerator of \(J(d)\) is at least \(13777968-6089-1014>0\) when \(0\le d\le1\). Consequently \(J(d)>0\) for \(0<d\le1\), and \(J(-d)<0\) for the same range: at argument \(-d\), the same numerator factor is at least \(13777968-1394687-1014>0\). Therefore the sign of \(E(d)\) is also the sign of the difference between the two *absolute* opposing currents.

**Exact asymmetry and its unique root.** Expanding the two rational terms gives
\[
E(d)=\frac{2d^2P(d^2)}{D(d)D(-d)},
\]
where
\[
P(z)=2514276z^4-1658361577z^3+207843423093z^2
+15992346284053z-14990744789037.
\]
The identities follow by exact polynomial multiplication; the verifier checks that the cleared numerator vanishes identically. For \(0\le z\le1\),
\[
P'(z)=10057104z^3-4975084731z^2+415686846186z+15992346284053
\ge15992346284053-4975084731>0.
\]
Furthermore, \(P(0)=-14990744789037<0\) and \(P(1)=1207789070808>0\). Thus exactly one \(z_*\in(0,1)\) satisfies \(P(z_*)=0\); put \(d_*=\sqrt{z_*}\). Strict monotonicity proves every asserted sign and uniqueness statement.

**Asymmetry of the equilibrium profile.** At \(d=0\), detailed balance assigns independent site occupations with odds proportional to the respective waiting times. Therefore the four equilibrium occupancies are \((1/2,4/5,2/3,1/2)\), which are not preserved by spatial reflection. For chains of two or three sites with equal boundary waiting times, reflection fixes every possible bulk waiting-time profile; hence four is the shortest chain in this boundary model in which equilibrium-profile reflection asymmetry can occur.

**Robustness to perturbing the disorder.** The verifier establishes the following strictly opposite rational values:
\[
E(1/2)=-\frac{2788493690453}{41358464106269436}<0,
\]
\[
E(99/100)=\frac{2742563650189250089505856910104}{127791761309188514069321932127433175}>0.
\]
The stationary current of an irreducible finite-state continuous-time Markov chain depends continuously on its positive transition rates. Both inequalities persist for all positive bulk departure-rate pairs in a sufficiently small open neighborhood of \((1/4,1/2)\). The intermediate-value theorem then provides at least one nonzero cancellation point between those two drives in each such nearby model. This argument does not claim that the point stays unique under arbitrary perturbations.

## Verification

The standalone `verify.py` uses exact SymPy arithmetic. It constructs every allowed transition on all sixteen bit-string configurations; checks the generator row sums, normalized stationary equations and the rational current identity for a symbolic reservoir contrast; checks the polynomial identity for \(E\), strict positivity bounds and both exact sign witnesses; and verifies the four-site equilibrium Bernoulli product distribution at zero contrast. Run `python verify.py` after installing the dependency in `requirements.txt`. An actual run of the packaged checker returned `VERIFY_OK`. Analytic monotonicity and continuity arguments, not numerical root sampling, establish the infinite-family sign assertions.

## Relationship to prior work

Sakai and Akimoto [1] introduced this boundary-driven *site*-disordered exclusion model, gave the exact reflection argument showing that symmetric equilibrium profiles force antisymmetric currents, and developed Galerkin/mean-field approximations for nonlinear rectification. Their discussion explicitly allows cancellation of nonlinear contributions despite an asymmetric profile, but does not derive the present exact finite-drive cancellation, sign reversal, unique contrast, or open-neighborhood persistence. The departure-site disorder and boundary-density driving are precisely those in [1]. Their earlier article [2] analyzes a *periodic* exclusion system under an *external bulk bias*, rather than this open reservoir-driven model; its reported restoration of bias-reversal symmetry at extreme external drive is a different mechanism and does not imply this finite reservoir-contrast root. General exact finite-state stationary-distribution methods are standard and are used here as a computational proof technique, not claimed as new.

## Limitations

This is an exact four-site counterexample to the stronger assertion that a reflection-asymmetric equilibrium profile yields unequal opposing current magnitudes at **every** nonzero drive. It is **not** a counterexample to the weaker conjecture that every such profile yields some rectifying drive: this sample rectifies away from its isolated cancellation point. A unique root is established only for the stated waiting times and mean reservoir density. The open-set extension guarantees existence but not uniqueness. No thermodynamic-limit behavior, disordered-ensemble probability, or generic magnitude estimate is claimed. The result is for steady-state mean currents, not current-fluctuation statistics.

## References

[1] I. Sakai and T. Akimoto, “Sample-specific rectification-like response in a boundary-driven exclusion process,” arXiv:2609.03560v1, first made public 3 September 2026, Sections II, IV.2–IV.4, VI, Appendix A. https://arxiv.org/html/2609.03560v1

[2] I. Sakai and T. Akimoto, “Symmetry breaking of current response in disordered exclusion processes,” arXiv:2512.03316v2, Sections II, III, Appendices C and E. https://arxiv.org/html/2512.03316v2
