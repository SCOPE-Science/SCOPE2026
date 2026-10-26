# Uniform dimensional crossover of the imperfect Bose-gas saddle point

## Finding

In the leading low-temperature, periodic-boundary regime of the \(d\)-dimensional imperfect Bose gas, set \(d=3-\epsilon\), \(\delta=\epsilon/2\), \(L_\mu=(a/\mu)^{1/d}\) for \(\mu>0\), \(X=\lambda^{d-1}D/L_\mu^d\), and write the stationary point as \(\bar{s}=-x\) with \(x>0\). For the reduced saddle equation \(X=\operatorname{Li}_{1-\delta}(e^{-x})\), the joint limit \(\delta\downarrow0\) and \(X\to\infty\) obeys \[x=\left(1+\frac{\delta X}{1-\gamma_E\delta}\right)^{-1/\delta}\bigl(1+O(\delta)\bigr).\] Consequently \(-\log x\sim X\) when \(\delta X\to0\), while \(x\sim[\Gamma(\delta)/X]^{1/\delta}\) when \(\delta X\to\infty\), yielding a uniform crossover between the \(d=3\) exponential scale and the \(d<3\) power-law scale.

The crossover variable is \(\delta X=(3-d)X/2\): it identifies the boundary layer in which the fixed-dimension power law ceases to be a uniform approximation as \(d\) approaches three. The statement concerns the saddle point that controls the force asymptotics; it does not assert a new exact formula for the force at arbitrary temperature or width.

## Assumptions and scope

Consider the periodic-boundary imperfect (mean-field) Bose gas in a slab of size \(L^{d-1}\times D\), in the quantum-critical hierarchy \(L\gg\lambda\gg D\gg l_{\mathrm{mic}}\). Here \(a>0\) is the mean-field coupling, \(\mu>0\) the chemical potential, \(\lambda\) the thermal de Broglie wavelength, and \(L_\mu=(a/\mu)^{1/d}\). The lateral thermodynamic limit is taken first. The source's stationary-point equation contains a finite-temperature term proportional to \(-\bar{s}/(a\beta)\); the reduced equation used here is the leading low-temperature approximation in which that term is negligible relative to \(\mu/a\). Write \(\bar{s}=-x\), \(x>0\), \(\delta=(3-d)/2\), and \(X=\lambda^{d-1}D/L_\mu^d\). The regime of interest has \(X\to\infty\) and \(0<\delta\to0\). Treating \(d\) as continuous is the analytic continuation used in the imperfect-gas calculation, not a claim that a physical sample has fractional spatial dimension.

## Proof

The reduced saddle equation is
\[
X=\operatorname{Li}_{1-\delta}(e^{-x}).
\]
For \(x\downarrow0\), Jonquière's expansion of the polylogarithm gives, uniformly for \(\delta\) near zero,
\[
\operatorname{Li}_{1-\delta}(e^{-x})=\Gamma(\delta)x^{-\delta}+\zeta(1-\delta)+O(x).
\]
The Laurent expansions at \(\delta=0\) are
\[
\Gamma(\delta)=\delta^{-1}-\gamma_E+O(\delta),\qquad
\zeta(1-\delta)=-\delta^{-1}+\gamma_E+O(\delta),
\]
where \(\gamma_E\) is Euler's constant. Set \(y=x^{-\delta}\ge1\). Substitution yields
\[
X=(y-1)(\delta^{-1}-\gamma_E)+O\bigl(\delta(y+1)+x\bigr).
\]
Solving this relation gives
\[
y=1+\frac{\\(\delta X\)}{1-\gamma_E\delta}+O(\delta^2y).
\]
Because the error is relative \(O(\delta^2)\) on the scale of \(y\), taking logarithms and dividing by \(\delta\) gives
\[
\log x=-\frac1\delta\log\left(1+\frac{\\(\delta X\)}{1-\gamma_E\delta}\right)+O(\delta),
\]
which is equivalent to the claimed relative asymptotic formula. If \(\delta X\to0\) while \(X\to\infty\), the logarithm expansion gives \(-\log x/X\to1\). If \(\delta X\to\infty\), the formula reduces to \(x\sim[\Gamma(\delta)/X]^{1/\delta}\) as \(\delta\to0\), matching the small-\(\delta\) form of the fixed-d power law. The two endpoint laws therefore arise from one joint asymptotic rather than from an unjustified interchange of limits.

## Verification

The critical analytic identity is the standard polylogarithm expansion \(\operatorname{Li}_s(z)=\Gamma(1-s)(\log(1/z))^{s-1}+\sum_{k\ge0}\zeta(s-k)(\log z)^k/k!\), valid for \(|\log z|<2\pi\) and nonintegral positive \(s\) as used here; the relevant form and domain are given in NIST DLMF §25.12, equation 25.12.12. The cancellation of the \(\pm\delta^{-1}\) poles is explicit above. The proof is asymptotic and analytic; no finite numerical experiment is used as proof. The low-temperature reduction, thermodynamic limit, and periodic boundary condition are essential assumptions. No independent audit or independent validation is claimed.

## Relationship to prior work

Jakubczyk, Napiórkowski, and Sęk derive the same reduced saddle equation and give separate asymptotics at \(d=3\) and at fixed \(2<d<3\). Their equations (16), (21), (26), and (34) provide the endpoint forms, but the inspected text does not state the joint \(\delta X\)-crossover or retain the cancelling Gamma/zeta poles to obtain a uniform formula. The present result is a focused asymptotic extension of that model, not a new Hamiltonian or a claim that the endpoint laws themselves are new.

Napiórkowski, Jakubczyk, and Nowak analyze the imperfect Bose gas's bulk criticality and Casimir scaling in the thermal regime; their finite-width treatment uses \(D/\lambda\gg1\), unlike the \(\lambda\gg D\) hierarchy here. Diehl and Rutkevich determine broad scaling functions for ideal and imperfect Bose gases, but the inspected scope emphasizes the opposite \(\lambda_{\mathrm{th}}\ll D\) limit and explicitly points to the 2016 quantum-critical work for \(\lambda_{\mathrm{th}}\gg D\). Łebek and Jakubczyk study dimensional crossover induced by anisotropic lattice dispersion, a different mechanism from analytic continuation in \(d\). The published-finding corpus searches and the accessible current-week ledger produced no matching claim for this joint asymptotic; this absence is supporting evidence, not a proof of novelty.

## Limitations

The formula applies only to the reduced saddle equation in the stated low-temperature regime. It does not control finite-volume corrections, the discarded finite-\(\beta\) term, other boundary conditions, the ideal Bose gas, or the force away from the source's Regime-II asymptotics. The relative error is \(1+O(\delta)\) for the saddle variable; no uniform finite-parameter error bound is asserted. The crossover is a mathematically defined joint limit in continuously varying \(d\), and physical relevance is through the way it reconciles the two analytic continuations, not through a literal fractional-dimensional sample. A non-indexed derivation in a paper, thesis, or monograph remains a residual novelty risk.

## References

1. P. Jakubczyk, M. Napiórkowski, and T. Sęk, “Repulsive Casimir forces at quantum criticality,” *Europhysics Letters* **113** (2016), 30006. First public version: 20 January 2016. arXiv:1601.05435. DOI: 10.1209/0295-5075/113/30006.
2. M. Napiórkowski, P. Jakubczyk, and K. Nowak, “The imperfect Bose gas in \(d\) dimensions: critical behavior and Casimir forces,” *Journal of Statistical Mechanics: Theory and Experiment* (2013), P06015. arXiv:1305.4643.
3. H. W. Diehl and S. B. Rutkevich, “Fluctuation-induced forces in confined ideal and imperfect Bose gases,” *Physical Review E* **95** (2017), 062112. arXiv:1704.00507. DOI: 10.1103/PhysRevE.95.062112.
4. M. Łebek and P. Jakubczyk, “Dimensional crossovers and Casimir forces for the Bose gas in anisotropic optical lattices,” arXiv:2003.07458 (2020). DOI: 10.1103/PhysRevA.102.013324.
5. NIST Digital Library of Mathematical Functions, §25.12, equation 25.12.12, polylogarithm expansion: https://dlmf.nist.gov/25.12.E12.
