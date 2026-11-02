# Antithetic time-step pairing suppresses harmonic-midpoint phase dispersion by seven powers

## Finding

Consider the planar harmonic oscillator integrated by implicit midpoint with positive randomized step lengths. Pairing consecutive uniform step perturbations with opposite signs retains **every individual step-length law** and exactly preserves the oscillator's quadratic energy, yet changes the sharp terminal ensemble-dispersion exponent. More generally, for step width \(\delta=\kappa h^\alpha\), \(\alpha>1\), and fixed target time \(T\), the independent-step and complementary-pair constructions obey

\[
\lim_{h\to0}\frac{\operatorname{Var}(\Phi_{\mathrm{iid}})}{h^{2\alpha-1}}
=\lim_{h\to0}\frac{D_{\mathrm{iid}}}{h^{2\alpha-1}}=\frac{T\kappa^2}{3},\qquad
\lim_{h\to0}\frac{\operatorname{Var}(\Phi_{\mathrm{anti}})}{h^{4\alpha+1}}
=\lim_{h\to0}\frac{D_{\mathrm{anti}}}{h^{4\alpha+1}}=\frac{T\kappa^4}{90}.
\]

Here \(\Phi\) is the real, unwrapped terminal rotation angle, and \(D=\mathbb E\|Y(T)-\mathbb EY(T)\|^2/\|Y(0)\|^2\) is the actual normalized endpoint ensemble variance. For the midpoint-relevant step perturbation width \(\delta=\kappa h^{5/2}\), these powers are \(h^4\) versus \(h^{11}\), so \(D_{\mathrm{anti}}/D_{\mathrm{iid}}\sim\kappa^2h^7/30\). In addition, for every finite positive admissible step size, complementary pairing is the **unique** minimum-variance coupling for the unwrapped two-step phase among all two-step couplings with the prescribed uniform marginals, when blocks are independent. This finite-step phase optimality is not claimed for the circular endpoint dispersion over arbitrary couplings.

## Assumptions and scope

Fix \(T>0\), \(\kappa>0\), \(\alpha>1\), and a deterministic nonzero vector \(y_0\in\mathbb R^2\). Let \(J=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)\) and solve \(y'=Jy\). For each integer \(m\ge1\), set \(h=T/(2m)\) and \(\delta=\kappa h^\alpha\). All sufficiently large \(m\) have \(0<\delta<h\), giving strictly positive step lengths. Denote \(\theta(s)=2\arctan(s/2)\).

The independent construction uses \(2m\) independent \(U_k\sim\mathrm{Unif}[-1,1]\) and step lengths \(H_k=h+\delta U_k\). The complementary construction uses independent \(U_j\sim\mathrm{Unif}[-1,1]\) **across** \(m\) blocks and step lengths \((H_{2j},H_{2j+1})=(h+\delta U_j,h-\delta U_j)\). Each of the \(2m\) step lengths has precisely the same marginal distribution in both constructions. The complementary construction has the exact total step length \(\sum_k H_k=T\), whereas the independent construction has only expected total step length \(T\). Both use exactly \(2m\) implicit-midpoint updates.

For either method define \(\Phi=\sum_k\theta(H_k)\in\mathbb R\), without reduction modulo \(2\pi\); let \(Y(T)\) designate the endpoint after \(2m\) numerical steps at nominal target time \(T\). The endpoint dispersion is \(D=\mathbb E\|Y(T)-\mathbb EY(T)\|^2/\|y_0\|^2\). The limit runs over \(m\to\infty\), hence \(h\to0\) with \(T\) fixed.

## Proof

**1. Exact rotation and finite-size identities.** Implicit midpoint with a positive step \(s\) has matrix \(Q(s)=(I-sJ/2)^{-1}(I+sJ/2)\). Since \(J^2=-I\), the matrix \(Q(s)\) is the planar rotation of angle \(\theta(s)\), whence \(Q(s)^\mathsf TQ(s)=I\) for every \(s\). Consequently both randomized trajectories preserve \(\|y_0\|^2\) exactly. All rotations commute. Put \(X=\theta(h+\delta U)\) and \(Z=\theta(h+\delta U)+\theta(h-\delta U)\) for a generic uniform \(U\). Independence between blocks gives

\[
\operatorname{Var}(\Phi_{\mathrm{iid}})=2m\operatorname{Var}(X),\quad
\operatorname{Var}(\Phi_{\mathrm{anti}})=m\operatorname{Var}(Z),
\]
\[
D_{\mathrm{iid}}=1-|\mathbb E e^{iX}|^{4m},\qquad
D_{\mathrm{anti}}=1-|\mathbb E e^{iZ}|^{2m}.
\]

Both phase means equal \(2m\mathbb EX\), exactly, by the equality of the individual step-length marginals.

**2. Unique optimal two-step phase coupling.** For fixed admissible \(h,\delta\), the function \(f(u)=\theta(h+\delta u)\) is continuously differentiable and strictly increasing for \(u\in[-1,1]\); indeed \(f'(u)=\delta/(1+(h+\delta u)^2/4)>0\). For any joint law of \(U,V\), each uniform on \([-1,1]\), the two-step phase variance is \(2\operatorname{Var}f(U)+2\operatorname{Cov}(f(U),f(V))\). The marginal means and variances are fixed, so minimizing the total variance is equivalent to minimizing \(\mathbb Ef(U)f(V)\). For all interior thresholds \(s,t\), the elementary union bound gives the sharp lower Fréchet bound

\[
\Pr(U>s,V>t)\ge\max\{0,-(s+t)/2\},
\]

and equality holds for every \(s,t\) if \(V=-U\). Expanding \(f(x)=f(-1)+\int_{-1}^1 f'(s)\mathbf1_{\{x>s\}}\,ds\) proves that this bound minimizes \(\mathbb Ef(U)f(V)\). Because \(f'>0\) everywhere, equality of the integral forces equality of all joint survival probabilities by continuity, which characterizes the countermonotone law \(V=-U\); uniqueness follows. For independent two-step blocks, minimizing each block's variance minimizes the unwrapped total phase variance. This is a direct application of classical countermonotone coupling, not a new rearrangement theorem.

**3. Independent-step sharp variance.** Differentiating gives \(\theta'(h)=(1+h^2/4)^{-1}\) and \(\theta''(h)=-(h/2)(1+h^2/4)^{-2}\). Since \(\delta=o(h)\), uniform Taylor expansion yields \(X=\theta(h)+\theta'(h)\delta U+O(\delta^2)\). Therefore \(\operatorname{Var}(X)=\delta^2\theta'(h)^2/3+o(\delta^2)\). With \(2m=T/h\),

\[
\operatorname{Var}(\Phi_{\mathrm{iid}})=\frac{T\kappa^2}{3}h^{2\alpha-1}(1+o(1)).
\]

**4. Complementary-pair sharp variance.** The odd Taylor terms cancel, while \(\sup_{|s-h|\le\delta}|\theta^{(4)}(s)|=O(h)\) for \(\delta=o(h)\). Hence, uniformly for \(|U|\le1\),

\[
Z=2\theta(h)+\theta''(h)\delta^2U^2+O(h\delta^4).
\]

The uniform distribution satisfies \(\mathbb EU^2=1/3\) and \(\operatorname{Var}(U^2)=1/5-1/9=4/45\). Since \(\theta''(h)\sim-h/2\), the remainder is negligible relative to the leading centered term and

\[
\operatorname{Var}(Z)=\frac{h^2\delta^4}{45}(1+o(1)),\qquad
\operatorname{Var}(\Phi_{\mathrm{anti}})=\frac{T\kappa^4}{90}h^{4\alpha+1}(1+o(1)).
\]

The coefficients are positive because \(\kappa,T>0\). This fourth-power residual comes from the curvature of the midpoint rotation angle and **not** from the total random time, which is identically \(T\) in each complementary construction.

**5. Actual endpoint-variance constants.** Let \(W\) be either the one-step angle \(X\) or one independent two-step block angle \(Z\), and let \(K\) be the number of independent instances (respectively \(2m\) or \(m\)). All centered moments of \(W\) shrink uniformly; in particular \(|W-\mathbb EW|=o(1)\) uniformly in the underlying uniform draw. The identity

\[
1-|\mathbb Ee^{iW}|^2=\mathbb E[1-\cos(W-W')]
\]

with an independent copy \(W'\), together with \(1-\cos t=t^2/2+o(t^2)\), gives \(1-|\mathbb Ee^{iW}|^2=\operatorname{Var}(W)(1+o(1))\). Further, \(K\operatorname{Var}(W)\to0\) by Steps 3 and 4, so \(1-|\mathbb Ee^{iW}|^{2K}=K\operatorname{Var}(W)(1+o(1))\). Combine this with the exact dispersion identities in Step 1 to obtain both positive constants. Their ratio is \(\kappa^2h^{2\alpha+2}/30\,(1+o(1))\), and choosing \(\alpha=5/2\) gives the claimed seven-power separation. This completes the proof.

## Verification

The supplied `VERIFY.py` evaluates exact finite-block phase variance and circular output dispersion from high-precision one-dimensional quadrature, checks the explicit derivative identities, tests the two different power normalizations and samplewise norm preservation, and checks strict phase-variance optimality against independent and comonotone alternatives. Its rational-moment identities use \(\mathbb EU^2=1/3\) and \(\mathbb EU^4=1/5\). Numerical checks are **not** substitutes for the proof of all admissible \(m\), \(\alpha\), \(T\), and \(\kappa\).

## Relationship to prior work

Abdulle and Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first dated public arXiv posting January 4, 2018), provide the positive i.i.d. random-time-step framework, a uniform step-length example, and geometric conservation of a randomized implicit-midpoint method. Their original construction assumes independent successive step lengths; sections 2, 6 and 8 do not give this complementary two-step coupling or its exact harmonic-oscillator phase and endpoint dispersion constants. Their technical-report cover is dated December 2017 but supplies no verified day of its public release; the first verified full date here is the arXiv record, rather than an asserted publication date for that report.

Lie, Stahn and Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, Calcolo 59 (2022), analyze independent centered randomization and strong error; their considered randomization is an additive state perturbation rather than a complementary positive-time-step coupling. Classical antithetic variates and the Fréchet–Hoeffding lower bound already yield the finite-two-step optimal-coupling principle for strictly monotone observables. The present new calculation is the **particular sharp two-exponent phase/output-variance law** for the geometric randomized midpoint solver, including a closed leading coefficient for the curvature-driven residual. No new general theorem about antithetic variates is claimed.

## Limitations

The sharp laws concern one planar constant-frequency oscillator, uniform bounded perturbations, fixed \(T\), \(\alpha>1\), and independent pairs. They do not yield nonlinear phase-error estimates, adaptive-step guarantees, general Hamiltonian behavior, or universal optimality of the coupling across all time blocks. Complementary pairing violates the independent-step hypothesis of the motivating paper, while preserving each marginal. Mean unwrapped phases coincide, but the mean vector endpoints need not coincide. Small ensemble dispersion is not necessarily better calibrated uncertainty: the deterministic midpoint phase error persists at order \(h^2\). An equivalent specialized antithetic-time-stepping derivation elsewhere remains a literature-priority risk; independent validation is not performed.

## References

1. Assyr Abdulle and Giacomo Garegnani, *Random time step probabilistic methods for uncertainty quantification in chaotic and geometric numerical integration*, arXiv:1801.01340 (first posted 2018-01-04), https://arxiv.org/abs/1801.01340 . Full open technical report: https://infoscience.epfl.ch/record/270787/files/Report-28.2017_AA-GG.pdf?ln=en .
2. Han Cheng Lie, Martin Stahn, and T. J. Sullivan, *Randomised one-step time integration methods for deterministic operator differential equations*, Calcolo 59, article 13 (2022), https://doi.org/10.1007/s10092-022-00457-6 .
3. Classical Fréchet–Hoeffding lower coupling bound / antithetic-variates principle; a complete argument needed for the present assertion is supplied in Proof Step 2.
