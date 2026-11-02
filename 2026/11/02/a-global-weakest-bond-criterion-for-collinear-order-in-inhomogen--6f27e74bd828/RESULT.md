# A global weakest-bond criterion for collinear order in inhomogeneous frustrated XY rings

## Finding
Let \(N\ge3\) be odd, and let \(J_1,\ldots,J_N>0\) be arbitrary exchange strengths of a classical planar antiferromagnetic ring. Put \(m=\min_iJ_i\), select any index \(j\) with \(J_j=m\), and set
\[
R_j=\sum_{i\ne j}\frac1{J_i},\qquad \rho=mR_j.
\]
The zero-temperature ground-state classification is **exact**:

* If \(\rho\le1\), the only ground state modulo a uniform rotation is collinear: all bonds are antialigned except bond \(j\), whose spins are aligned. Its energy is \(E_*=-\sum_iJ_i+2m\). The selected weakest bond is necessarily unique. This includes equality \(\rho=1\).
* If \(\rho>1\), no collinear configuration is a ground state, and \(E_*<-\sum_iJ_i+2m\). Noncollinear minimizing states exist, and complex conjugation of all spin directions gives a distinct minimizer modulo uniform rotation.

Thus the sharp ground-state transition occurs precisely when the weakest exchange equals the **series-effective stiffness** of all other exchanges: \(m=(\sum_{i\ne j}J_i^{-1})^{-1}\). In the collinear phase, the following quantitative global stability estimate holds for every configuration:
\[
E(\theta)-E_*\ \ge\ (1-\rho)\sum_{i\ne j}J_i[1-\cos\delta_i],
\]
where \(\delta_i\) is the angular deviation from an antialigned bond as defined below. The coefficient \(1-\rho\) is optimal for this inequality. This exact statement concerns **arbitrary positive nonuniform exchanges**, not only a ring with one defective bond.

For example, the five-bond strengths \((1,3,4,5,6)\) give \(\rho=19/20\) and a uniquely collinear ground state, while \((1,2,4,5,6)\) give \(\rho=67/60\) and noncollinear ground states. When \(J_j=\alpha J\) and all other \(N-1\) bonds equal \(J\), the criterion reduces to the previously known single-defect threshold \(\alpha_c=1/(N-1)\).

## Assumptions and scope
There are \(N\ge3\) classical unit-length planar spins \(e^{i\theta_v}\) on the vertices of a cycle; \(N\) is odd and \(\theta_v\in\mathbb R/(2\pi\mathbb Z)\). The spin at \(N+1\) equals the spin at \(1\). Every exchange \(J_i\) is finite and strictly positive; no external field, next-nearest-neighbor interaction, anisotropy, quantum correction, or temperature is included. The Hamiltonian is
\[
E(\theta)=\sum_{i=1}^{N}J_i\cos(\theta_{i+1}-\theta_i).
\]
Define \(\delta_i=\theta_{i+1}-\theta_i-\pi\) modulo \(2\pi\). Since \(N\) is odd, their sum obeys \(\sum_i\delta_i\equiv\pi\pmod{2\pi}\). Conversely, every collection of phase increments with this closure condition arises from a spin configuration, uniquely up to global rotation. Under this gauge the excess energy is
\[
F(\delta)=E(\theta)+\sum_iJ_i=\sum_iJ_i(1-\cos\delta_i).
\]
The collinear reference has \(\delta_j=\pi\) and \(\delta_i=0\) for \(i\ne j\), with \(F=2m\). Its opposite-neighbor spin directions are all determined up to a common rotation.

An equivalent statement holds on a cycle of either parity whose bonds carry phase offsets \(A_i\in\{0,\pi\}\) of odd total parity, with Hamiltonian \(-\sum_iJ_i\cos(\theta_{i+1}-\theta_i-A_i)\). Its deviations have the same \(\pi\)-closure, so the proof applies without change. This is a gauge-equivalence, not a claim about finite-temperature thermodynamics or quantum systems.

## Proof
**1. Exact energy comparison.** Fix the index \(j\) and write \(t=\sum_{i\ne j}\delta_i\), allowing any real representatives. Closure implies \(e^{i\delta_j}=-e^{-it}\), hence \(\cos\delta_j=-\cos t\). Subtracting the collinear reference energy gives the identity
\[
F-2m=\sum_{i\ne j}J_i(1-\cos\delta_i)-m(1-\cos t).\tag{1}
\]
The complex telescoping-product identity, followed by the triangle inequality and weighted Cauchy–Schwarz, gives
\[
\begin{aligned}
|e^{it}-1|&\le\sum_{i\ne j}|e^{i\delta_i}-1|\\
&\le\sqrt{\left(\sum_{i\ne j}\frac1{J_i}\right)
\left(\sum_{i\ne j}J_i|e^{i\delta_i}-1|^2\right)}.
\end{aligned}
\]
Because \(|e^{ix}-1|^2=2(1-\cos x)\), this proves the **global**, not linearized, bound
\[
1-\cos t\le R_j\sum_{i\ne j}J_i(1-\cos\delta_i).\tag{2}
\]
Substituting (2) into (1) proves
\[
F-2m\ge(1-mR_j)\sum_{i\ne j}J_i(1-\cos\delta_i).\tag{3}
\]
When \(mR_j\le1\), (3) proves that the collinear reference minimizes globally.

**2. Uniqueness, including the critical equality.** For \(mR_j<1\), equality in (3) requires \(\delta_i\equiv0\pmod{2\pi}\) for every \(i\ne j\), forcing \(\delta_j\equiv\pi\), so the state is unique modulo rotation. If \(mR_j=1\), equality in (1) requires equality both in the complex triangle inequality and in weighted Cauchy–Schwarz. Since there are at least two other bonds, all with finite strictly positive couplings, equality in Cauchy–Schwarz with a nonzero displacement forces **every** other bond to have nonzero chord length. But at least two nonzero successive chord steps on the unit circle cannot saturate the triangle inequality: equality would require three distinct unit-circle points to lie on a straight line in that order (or a reversal, which has opposite chord orientation). Thus equality requires every other chord to vanish, and the same unique collinear state follows. Moreover, if two indices shared the minimum \(m\), then \(mR_j>1\) because there are at least two indices other than \(j\). Hence the weakest bond is automatically unique in the collinear regime.

**3. Sharpness and the noncollinear regime.** For \(mR_j>1\), take the admissible one-parameter perturbation
\[
\delta_i(\varepsilon)=\frac{\varepsilon}{J_i}\quad(i\ne j),\qquad
\delta_j(\varepsilon)=\pi-\varepsilon R_j.
\]
This respects closure exactly. Expanding the exact identity (1) as \(\varepsilon\to0\),
\[
F(\delta(\varepsilon))-2m
=\frac{\varepsilon^2}{2}R_j(1-mR_j)+O(\varepsilon^4)<0
\]
for sufficiently small nonzero \(\varepsilon\). Thus the collinear reference is not globally minimizing. Every other collinear state has energy at least \(2m\) above \(-\sum_iJ_i\), so **no collinear configuration** is globally minimizing. Compactness of the \(N\)-torus yields a noncollinear minimizer. Reflection \(\theta_i\mapsto-\theta_i\) preserves the Hamiltonian but yields a different configuration modulo rotation unless every relative spin angle belongs to \(\{0,\pi\}\); hence at least a reflected pair of distinct noncollinear ground states exists.

**4. Optimality of the stability coefficient.** Along the same perturbation in the collinear regime,
\[
\frac{F(\delta(\varepsilon))-2m}{\sum_{i\ne j}J_i(1-\cos\delta_i(\varepsilon))}
\longrightarrow 1-mR_j
\]
as \(\varepsilon\to0\). Hence the coefficient in (3) cannot be improved for all configurations. The \(\rho=1\) case is globally rigid despite its vanishing quadratic stiffness; it is not an additional family of degenerate ground states.

## Verification
The accompanying `verify.py` independently minimizes the exact finite-dimensional energy of rings with \(N=3,5,7,9\), using random positive exchanges and repeated numerical starts. It checks 96 random weighted rings and 30 selected parameter sets below, at, and above the analytical threshold, and reports the number of numerically sampled noncollinear cases. It also evaluates exact perturbation directions. Execute with `python verify.py` using NumPy and SciPy. The script is a finite diagnostic; the proof above establishes all dimensions and all admissible positive exchange values. Exact rational examples satisfy \(19/20<1\) and \(67/60>1\) as claimed.

## Relationship to prior work
Baker et al. (2012) give physical and experimental motivation for distinguishing classical and quantum frustration in odd molecular spin rings, including three exchange parameters in experimental fits. Their quantum modeling does not state a sharp arbitrary-positive-coupling global XY criterion. Florek et al. (2014) explicitly report the **single-defect** classical vector-spin transition \(\alpha_c=1/(N-1)\); this is **prior art**, recovered exactly as a specialization, and is not being claimed as new. Kamieniarz, Florek and Antkowiak (2015) analyze quantum-spin ground-state sequences with **one** bond defect; its full text was not accessible during this comparison, so possible historical relations remain a limitation. The assessed addition is the necessary-and-sufficient **arbitrary-disorder global** criterion, its critical-equality rigidity, and the sharp nonlinear stability estimate, rather than a restatement of the single-defect threshold.

## Limitations
This theorem concerns deterministic zero-temperature equilibria of classical planar unit spins on one frustrated cycle. It does not assert uniqueness in the noncollinear phase, give a closed formula for every noncollinear spin angle, describe quantum spectra or finite-temperature transitions, or establish historical priority over every unpublished or inaccessible study. Positive finite exchanges, cycle closure, and exactly one frustrated \(\pi\) holonomy are essential. The relative spectral or dynamical stability of these equilibria under specified spin equations is not addressed. Primary literature and mathematical-results searches reduce but do not eliminate historical-priority uncertainty; the 2015 single-defect paper's complete text and the 2012 paper's supplementary PDF were not inspected.

## References
1. M. L. Baker et al., “A classification of spin frustration in molecular magnets from a physical study of large odd-numbered-metal, odd electron rings,” *Proc. Natl. Acad. Sci. USA* **109** (2012), 19113–19118. First publicly accessible 2012-11-06. https://doi.org/10.1073/pnas.1213127109 ; https://www.pnas.org/doi/10.1073/pnas.1213127109
2. W. Florek, M. Antkowiak, P. Kozłowski and G. Kamieniarz, “Frustration in odd-numbered AFM rings with bond defect,” 2014 conference abstract (entire single-page abstract inspected). https://www.ifmpan.poznan.pl/pm14/abst/608-wojciech_florek_amu_edu_pl-2014-03-06-17-43-56.pdf
3. G. Kamieniarz, W. Florek and M. Antkowiak, “Universal sequence of ground states validating the classification of frustration in antiferromagnetic rings with a single bond defect,” *Phys. Rev. B* **92** (2015), 140411(R). https://doi.org/10.1103/PhysRevB.92.140411
