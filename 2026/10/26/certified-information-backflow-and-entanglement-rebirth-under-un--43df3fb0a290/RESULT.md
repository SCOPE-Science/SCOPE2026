# Certified information backflow and entanglement rebirth under uniform-history quantum resetting

## Finding

For the quantum resetting-with-memory model of de Mauro, Kulkarni and Majumdar [1], fix the two-level Hamiltonian \(H=\Omega\sigma_z/2\) with \(\Omega>0\) and uniform-history Poisson reset rate \(r=\Omega/3\). Its known off-diagonal coherence multiplier \(f\) obeys the **strict certified** bounds
\[
|f(\Omega,8/\Omega)|<\frac3{50},\qquad
|f(\Omega,10/\Omega)|>\frac{11}{100}.
\]
Consequently, the trace distance between the images of antipodal equatorial qubit states increases by more than \(1/20\) between these two times. The dynamical family is therefore not positive-divisible on this interval (and in particular not CP-divisible).

The same interval realizes complete entanglement death followed by rebirth. If an inert reference qubit is initially paired with the moving qubit in
\[
\rho_\eta(0)=\eta|\Phi^+\rangle\langle\Phi^+|+(1-\eta)I_4/4,
\qquad |\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2,
\]
then for the entire open range \(50/61<\eta<25/28\), the state under \(\Lambda_t\otimes\operatorname{id}\) is strictly separable at \(8/\Omega\) and strictly NPT entangled at \(10/\Omega\). In particular \(\eta=25/29\) has negativity greater than \(3/232\) at the latter time. Here \(\Lambda_t\) is the reduced qubit channel induced by the uniform-history resetting protocol.

## Assumptions and scope

The protocol evolves the ensemble density matrix according to [1, Eq. (5)]
\[
\frac{d\rho}{dt}=-\mathrm{i}[H,\rho]-r\rho+\frac r t\int_0^t\rho(s)\,ds,
\quad t>0,\quad \rho(0)=\rho_0.
\]
Units have \(\hbar=1\). The resetting clock samples a past instant uniformly in the elapsed history, not a fresh fixed state. The known solution [1, Eqs. (12)--(13)] is, for any nonzero Bohr frequency \(\omega\),
\[
\rho_{mn}(t)=\rho_{mn}(0)f(\omega,t),\qquad
f(\omega,t)={}_1F_1\left(\frac{\mathrm{i}\omega}{r+\mathrm{i}\omega};1;-(r+\mathrm{i}\omega)t\right).
\]
Diagonal elements do not change. The already established random-operational-time representation in [1, Appendix B] makes \(\Lambda_t\) an average of unitary phase rotations and hence a CPTP channel for every fixed time. This permits its ordinary tensor-product extension with an inert reference system. We assert **no** divisibility or revival criterion for other reset rates or arbitrary inputs.

## Proof

**1. Exact rational hypergeometric certificate.** Put \(\tau=\Omega t\), \(r/\Omega=1/3\), and \(a=(9+3\mathrm{i})/10\). Then
\[
f(\Omega,\tau/\Omega)={}_1F_1(a;1;-(1/3+\mathrm{i})\tau)
=\sum_{k=0}^{\infty}\frac{(a)_k[-(1/3+\mathrm{i})\tau]^k}{(k!)^2}.
\]
For \(\tau=8,10\), \(|a|<1\), \(|-(1/3+\mathrm{i})\tau|<11\), and \(|a+k|\le k+1\) for all integers \(k\ge0\). Hence each summand has modulus at most \(11^k/k!\). Set \(P_{80}(\tau)\) to be the sum over \(0\le k\le80\). The remainder at either time has the rigorous bound
\[
|f-P_{80}|\le\epsilon_{80}:=
\frac{11^{81}/81!}{1-11/82}<\frac1{1000}.
\]
Every coefficient of \(P_{80}(8)\) and \(P_{80}(10)\) lies in \(\mathbb Q(\mathrm{i})\). Exact rational arithmetic in the enclosed executable `verify.py` proves
\[
|P_{80}(8)|^2<(59/1000)^2,\qquad
|P_{80}(10)|^2>(111/1000)^2.
\]
By the triangle inequalities, \(|f(8)|<59/1000+1/1000=3/50\) and \(|f(10)|>111/1000-1/1000=11/100\). No floating-point estimate enters these decisions.

**2. Information backflow.** For the initial antipodal states \(\rho_\pm=(I\pm\sigma_x)/2\), their evolved population differences vanish and their off-diagonal difference acquires the factor \(f\). Thus their trace distance \(\frac12\|\Lambda_t(\rho_+)-\Lambda_t(\rho_-)\|_1\) equals \(|f(\Omega,t)|\). The bounds prove a growth exceeding \(11/100-3/50=1/20\). Every positive trace-preserving map contracts the trace distance of states, so no positive propagator can take the two earlier images into their later images simultaneously. This is the standard distinguishability-backflow witness of [2], applied here to [1].

**3. Entanglement loss and rebirth.** Under \(\Lambda_t\otimes\operatorname{id}\), the diagonal entries of \(\rho_\eta\) remain \((1+\eta)/4,(1-\eta)/4,(1-\eta)/4,(1+\eta)/4\), in computational ordering, while \(\rho_{00,11}(t)=\eta f(\Omega,t)/2\) up to irrelevant complex conjugation. The partial transpose has eigenvalues \((1+\eta)/4\) (twice) and
\[
\frac{1-\eta}{4}\pm\frac\eta2|f(\Omega,t)|.
\]
By the necessary-and-sufficient PPT criterion for two qubits [3], the evolved state is separable iff
\[
|f(\Omega,t)|\le\frac{1-\eta}{2\eta}.
\]
If \(50/61<\eta<25/28\), its threshold belongs strictly to \((3/50,11/100)\), so the earlier state is interior to the PPT (separable) side and the later state is NPT. Continuity gives genuine time intervals of disappearance and reappearance. For \(\eta=25/29\), the threshold is \(2/25\), and the negativity at the later time is
\[
\frac\eta2|f(\Omega,10/\Omega)|-\frac{1-\eta}{4}
>\frac{3}{232}.
\]
This proves the stated finite-time phenomenon.

## Verification

Run `python3 verify.py` with only the Python standard library. The script performs the finite \(80\)-term sums with exact rational real and imaginary parts, checks both strict square-modulus inequalities, and proves the factorial-majorant tail bound by exact integer arithmetic. It also checks the isotropic-state threshold and the implication of the certified interval. Independent high-precision evaluations are approximately \(|f(\Omega,8/\Omega)|=0.058517134592752596\) and \(|f(\Omega,10/\Omega)|=0.111101945588866145\), but these approximate values are illustrative, not evidence for strict inequalities. The proof remains analytical apart from a finite, replayable, exact-arithmetic certificate.

## Relationship to prior work

De Mauro--Kulkarni--Majumdar [1] already established the uniform-history density evolution, its general Kummer-function solution, the qubit example, the random-operational-clock representation, and algebraically damped coherence with logarithmic phase oscillations. These are **not** claimed new. An oscillating complex phase does not alone show revival of the modulus or distinguishability. The contribution is the certified modulus reversal, its trace-distance consequence, and the open interval of isotropic-state entanglement death/rebirth in precisely that dynamical model.

Breuer--Laine--Piilo [2] established the trace-distance information-backflow criterion; Peres and the Horodeckis [3] established the PPT separability criterion; Bellomo--Lo Franco--Compagno [4] studied entanglement revival for different non-Markovian reservoir dynamics. Those general notions and demonstrations are not claimed new. The inspected source and nearest related studies did not state the present time-window theorem. Implicit coverage by additional dephasing-channel results or by further consequences of [1] remains a possibility; the originality determination is not independent.

## Limitations

The bounds are proved for the specified finite-time window and the single reset-to-splittings ratio \(r/\Omega=1/3\), with a two-dimensional isolated Hamiltonian and an inert reference. They imply a nonempty entanglement-revival parameter interval but no optimal revival rate, maximal amount, infinitely many revivals, or robustness to arbitrary stochastic modifications. The source's exact coherence solution makes these deductions possible, so the mathematical novelty is restricted to their rigorous quantitative model-specific consequences. A finite-sum certificate plus rigorous uniform tail is sufficient here because the theorem concerns two fixed real times, not a global characterization of an entire time axis.

## References

[1] G. de Mauro, M. Kulkarni, and S. N. Majumdar, *Quantum resetting with memory*, arXiv:2608.02297v1 (first publicly posted 2026-08-03), https://arxiv.org/abs/2608.02297 .

[2] H.-P. Breuer, E.-M. Laine, and J. Piilo, *Measure for the Degree of Non-Markovian Behavior of Quantum Processes in Open Systems*, Physical Review Letters **103**, 210401 (2009), https://doi.org/10.1103/PhysRevLett.103.210401 .

[3] A. Peres, *Separability Criterion for Density Matrices*, Physical Review Letters **77**, 1413 (1996), https://doi.org/10.1103/PhysRevLett.77.1413 ; M. Horodecki, P. Horodecki, and R. Horodecki, *Separability of mixed states: necessary and sufficient conditions*, Physics Letters A **223**, 1–8 (1996).

[4] B. Bellomo, R. Lo Franco, and G. Compagno, *Non-Markovian Effects on the Dynamics of Entanglement*, Physical Review Letters **99**, 160502 (2007), https://doi.org/10.1103/PhysRevLett.99.160502 .
