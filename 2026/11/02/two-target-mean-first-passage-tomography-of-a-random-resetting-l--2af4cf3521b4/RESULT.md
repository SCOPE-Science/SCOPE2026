# Two-target mean-first-passage tomography of a random resetting law

## Finding

An arbitrary probability law governing independently resampled Brownian reset locations is identified **exactly** by two ideal mean-first-passage-time (MFPT) curves, measured against two distinct absorbing targets while varying the Poisson resetting rate. A single target is generally reflection-blind; finitely many target/rate measurements are never universally identifying. The complete two-target curves give uniqueness but no uniform total-variation stability on any bounded positive rate interval.

Fix the diffusivity \(D>0\) and experimental initial position \(x_0\), neither a target. For each target \(c\), write the unknown resetting-source transform
\[
\Phi_c(s)=\int_{\mathbb R}e^{-s|y-c|}\,\mu(dy),\qquad s>0.
\]
The exact population mean at rate \(r=Ds^2\) is
\[
M_c(Ds^2)=\frac{1-e^{-s|x_0-c|}}{Ds^2\Phi_c(s)}.
\]
Consequently, measuring \(M_c\) determines \(\Phi_c\); the new inverse conclusion uses **two distinct** target locations \(a\ne b\).

## Assumptions and scope

The motion between resets has generator \(D\partial_{xx}\) on the entire real line. Resetting times form an independent Poisson process of positive rate \(r\). Immediately after each reset, draw a fresh independent location from the same unknown probability law \(\mu\), which may have arbitrary atoms, unbounded support, and no finite moments. Absorption is instantaneous on reaching the target, whether continuously or directly at a reset. Experiments for the two known sites \(a\ne b\) restart the process from one known deterministic \(x_0\notin\{a,b\}\). The diffusion coefficient and initial position are calibrated externally; these are not reconstructed. All observations are exact ensemble means at positive rates, not finite-trajectory estimates.

The two target-rate sets need not be identical, but each must have an accumulation point **within** the positive real half-line. A boundary accumulation only at zero or infinity is not asserted to suffice. No assumption of symmetrical \(\mu\), one-sided support, smoothness, or compact support is required for the uniqueness statement.

## Proof

**1. Exact renewal identity.** For Brownian motion starting at \(x\), the Laplace transform of the no-reset point-hitting time \(H_c\) is \(f_c(x)=\mathbb E_x e^{-rH_c}=e^{-\sqrt{r/D}|x-c|}\). The probability the point is hit before an independent exponential reset equals \(f_c(x)\). The expected duration of one attempt is \((1-f_c(x))/r\). A fresh reset draws \(Y\sim\mu\). If \(T_\mu\) denotes the expected additional time after a fresh reset, the renewal equation is
\[
T_\mu=\frac{1-\Phi_c(s)}r+(1-\Phi_c(s))T_\mu,
\qquad T_\mu=\frac{1-\Phi_c(s)}{r\Phi_c(s)}.
\]
As \(\Phi_c(s)>0\), this is finite without assumptions on the tails of \(\mu\). Starting from \(x_0\) instead gives \(M_c(r)=(1-f_c(x_0))/(r\Phi_c(s))\). This forward formula is an established resetting-renewal identity; the inverse assertions below are the contribution assessed here.

**2. From means to folded laws.** Rearrangement yields
\[
\Phi_c(s)=\frac{1-e^{-s|x_0-c|}}{Ds^2 M_c(Ds^2)}.
\]
For the pushforward \(\rho_c=(y\mapsto|y-c|)_*\mu\), this is its Laplace transform on \([0,\infty)\). It is holomorphic on \(\Re s>0\) by dominated differentiation on compact subsets, even if \(\mu\) has no moments. The complex identity theorem extends equality from any sequence of positive \(s\) with an interior limit point to the entire half-plane. Uniqueness of Laplace transforms for finite Borel measures identifies \(\rho_c\).

**3. Two-target uniqueness, including singular sources.** Let \(\mu,\nu\) have identical folded laws at both sites, and set the finite signed measure \(\eta=\mu-\nu\). Folding at target \(c\) vanishes for \(\eta\) precisely when the reflected pushforward obeys \(R_{c*}\eta=-\eta\), where \(R_c(y)=2c-y\). The composition \(R_bR_a\) translates by \(2(b-a)\ne0\), so the two antisymmetries imply translation invariance of \(\eta\) under a nonzero shift. A finite signed measure invariant under nonzero translation must vanish: its total variation is translation invariant, and translating any bounded set of positive total variation far enough gives infinitely many disjoint equally weighted sets, contradicting finite mass. Thus \(\mu=\nu\).

There is also a constructive Fourier prescription. Recover \(\rho_a,\rho_b\) by Laplace inversion and define
\[
C_c(k)=\int_{0}^{\infty}\cos(kt)\rho_c(dt),\qquad \varphi(k)=\int_{\mathbb R}e^{iky}\mu(dy)=U(k)+iV(k).
\]
Since \(C_c(k)=U(k)\cos(kc)+V(k)\sin(kc)\), the two linear equations give
\[
U(k)=\frac{C_a(k)\sin(kb)-C_b(k)\sin(ka)}{\sin(k(b-a))},
\quad V(k)=\frac{C_b(k)\cos(ka)-C_a(k)\cos(kb)}{\sin(k(b-a))}.
\]
These hold whenever \(\sin(k(b-a))\ne0\). The apparent singularities form a discrete frequency set and are uniquely filled by continuity of characteristic functions; \(\varphi\) determines the full Borel probability law.

**4. Exactly what one target misses.** At one target \(c\), the data depend only on \(\rho_c\). If \(\rho_c((0,\infty))>0\), a measurable splitting of every distance \(t>0\) between the points \(c+t\) and \(c-t\) yields many different sources with the same \(\rho_c\). In particular, reflecting a nonsymmetric source about \(c\) preserves the entire curve. With the a priori constraint that all mass lies on one known side of \(c\), a single view would suffice; without support priors it does not identify all laws. Degenerate \(\delta_c\) is a single-view exception.

**5. No finite collection of scalar readings identifies all laws.** Given \(m\) arbitrary measurement pairs \((c_j,r_j)\), their MFPTs determine only \(m\) integrals \(\int e^{-\sqrt{r_j/D}|y-c_j|}\mu(dy)\). Choose any \(m+2\) distinct candidate source points, and construct the real \((m+1)\)-by-\((m+2)\) matrix consisting of those \(m\) kernels and one mass-normalization row. A nonzero null vector exists and has both signs because its entries sum to zero. Small positive and negative perturbations of the strictly positive uniform weights yield distinct probability sources with all \(m\) readings equal. At targets \(0,1\) and rate \(r=D\), a concrete null vector on \((-1,0,1,2)\) is \((-1,e^{-1},-e^{-1},1)\).

**6. Quantified absence of uniform total-variation stability.** Restrict sources to \([0,1]\), select targets \(a=0\) and \(b=1\), and choose any fixed \(\varepsilon\in(0,1)\). For each integer \(n\ge1\), the probability densities \(f_n^\pm(y)=1\pm\varepsilon\sin(2\pi n y)\) have fixed total-variation separation \(2\varepsilon/\pi\). Let \(k_n=2\pi n\). Their transforms satisfy
\[
\Phi_0^\pm(s)=\frac{1-e^{-s}}s\pm\varepsilon\frac{k_n(1-e^{-s})}{k_n^2+s^2},\quad
\Phi_1^\pm(s)=\frac{1-e^{-s}}s\mp\varepsilon\frac{k_n(1-e^{-s})}{k_n^2+s^2}.
\]
On any fixed compact interval \(0<r_{\min}\le r\le r_{\max}<\infty\), the base transform is bounded below and the difference is uniformly \(O(1/n)\). The MFPT transformation divides by this positive transform, hence the two MFPT response pairs also differ uniformly by \(O(1/n)\), despite their source measures remaining \(2\varepsilon/\pi\) apart in total variation.

## Verification

The standalone standard-library Python file `verify.py` computes the exact renewal transform, tests reconstruction of a discrete source characteristic function at nonresonant frequencies, checks one-target reflection ambiguity and the finite-measurement null vector, confirms the sine-density transform formulas and their separation, and independently simulates hitting and resetting using the exact Brownian first-passage distribution. Run `python verify.py`. The recorded execution passed 95 numerical and probabilistic assertions. The analytic steps in Sections 1–6, rather than simulation or a finite test suite, establish the quantified measure-theoretic conclusions.

## Relationship to prior work

Méndez, Flaquer-Galmés and Campos (arXiv:2401.01125) study Brownian first-passage under random-position Poisson resetting, obtain the forward mean formula and analyze optimal rates, spatial source families and first-passage fluctuations. That forward formula is **not** presented as new. Toledo-Marín and Boyer (arXiv:2206.14387) develop broad forward distributed-resetting first-passage and entropy calculations, including parity-dependent reset sources. Julián-Salgado, Dagdug and Boyer (arXiv:2311.11897) study multiple resetting points and forward search optimization, not reconstruction of an unknown law from distinct target responses. Abundo (arXiv:2410.16889) investigates inverse first-passage specifications for random initial positions and random reset points; its inverse targets prescribed exit-time laws rather than determining an arbitrary repeatedly resampled reset-source law from two site-indexed rate sweeps. Those papers supply essential context and may furnish the general renewal identity used here, but the inspected statements do not establish the two-target all-measure identifiability theorem and its sharp one-target, finite-data and stability boundaries.

The characteristic-function reconstruction uses classical Fourier/Laplace uniqueness; these are mathematical tools, not independently novel techniques. Broader inverse-source tomography results could imply the two-view theorem under reformulation. Full publication-priority verification remains outstanding.

## Limitations

The full identification requires ideal complete rate sweeps or exact values on sets having interior accumulation points, two distinct accessible point targets, a fixed source law shared by experiments, calibrated \(D\) and \(x_0\), and a fresh independent reset draw at each jump. There is no claim about noisy-data stability, finite-sample statistical consistency, rate calibration, multidimensional inversion, target geometry other than points on the line, or recovery from finitely many observables. Strong nonidentifiability for finite measurements and total-variation ill-conditioning are proved explicitly. The mathematical claims do not cover noisy or incomplete-data estimators.

## References

1. V. Méndez, R. Flaquer-Galmés and D. Campos, *First-passage time of a Brownian searcher with stochastic resetting to random positions*, arXiv:2401.01125, first posted 2024-01-02.
2. J. Q. Toledo-Marín and D. Boyer, *First passage time and information of a one-dimensional Brownian particle with stochastic resetting to random positions*, arXiv:2206.14387 (2022).
3. S. Julián-Salgado, L. Dagdug and D. Boyer, *Diffusion with two resetting points*, arXiv:2311.11897 (2023).
4. M. Abundo, *Inverse first-passage problems of a diffusion with resetting*, arXiv:2410.16889, first posted 2024-10-22.
