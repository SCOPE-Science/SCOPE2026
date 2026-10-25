# Logarithmic low-temperature allocation of a fixed magnetic-field budget in an XX dimer

## Finding

Let \(J>0\), \(R>0\), and \(\beta>0\). Two longitudinal fields \(h_1,h_2\in\mathbb R\) obey the **quadratic budget** \((h_1^2+h_2^2)/2=R^2\). Among the Gibbs states of the spin-\(1/2\) XX dimer defined below, maximize Wootters concurrence \(\mathcal C_\beta\). Write \(B=(h_1+h_2)/2\), \(b=(h_1-h_2)/2\), so \(B^2+b^2=R^2\).

**Sharp low-temperature allocation threshold.** If \(0<R<J\), then for all sufficiently large \(\beta\) every maximizer has \(b=0\), \(|B|=R\), and its concurrence tends to \(1\). If \(R\ge J\), put \(s=\sqrt{(J^2+R^2)/2}\). For **every** choice of global maximizer (no finite-temperature uniqueness assertion),
\[
|B|=s-\frac{\log(2\beta s)}{2\beta}+o(\beta^{-1}),
\qquad
\max\mathcal C_\beta=\frac Js\left[1-\frac{\log(2\beta s)+1}{2\beta s}+o(\beta^{-1})\right].
\]
Furthermore, \(b^2\to(R^2-J^2)/2\); on the critical budget \(R=J\), \(b^2\sim J\log(2\beta J)/\beta\). In particular the optimized concurrence tends to \(\min\{1,\sqrt2J/\sqrt{J^2+R^2}\}\). The logarithm is a singular thermal allocation layer next to the crossing of a separable state and an entangled state, rather than a fixed-temperature symmetry argument.

## Assumptions and scope

Use units \(k_B=1\) and the Pauli matrices \(\sigma_x,\sigma_y,\sigma_z\). The Hamiltonian is
\[
H=\frac J2(\sigma_x\otimes\sigma_x+\sigma_y\otimes\sigma_y)
 +\frac12\bigl[h_1\sigma_z\otimes I+h_2 I\otimes\sigma_z\bigr].
\]
The canonical state is \(\rho_\beta=e^{-\beta H}/\operatorname{tr}(e^{-\beta H})\); concurrence is the standard Wootters two-qubit concurrence. The budget is an equality constraint, the local fields are collinear with the quantization axis, and the coupling \(J\) and budget \(R\) stay fixed while \(\beta\to\infty\). Signs \((B,b)\mapsto(\pm B,\pm b)\) do not affect concurrence. Statements about maximizers concern all allowed real pairs and only sufficiently low, finite positive temperatures unless a limit is explicitly written.

## Proof

**Exact reduction.** In the even-parity basis \(|00\rangle,|11\rangle\), the energies are \(B,-B\). In the odd-parity basis \(|01\rangle,|10\rangle\), the Hamiltonian block is \(\left(\begin{smallmatrix}b&J\\J&-b\end{smallmatrix}\right)\), with energies \(E,-E\) for \(E=\sqrt{J^2+b^2}\). The two nonzero off-diagonal entries of the Gibbs density matrix lie in the odd block, and the geometric mean of its even diagonal entries is \(1/Z\), where \(Z=2(\cosh\beta E+\cosh\beta B)\). The exact X-state concurrence formula gives
\[
\mathcal C_\beta(B,b)=\frac{\bigl[(J/E)\sinh(\beta E)-1\bigr]_+}{\cosh(\beta E)+\cosh(\beta B)}.
\tag{1}
\]
For all sufficiently large \(\beta\), the bracket is strictly positive uniformly on the compact budget circle because \(J\le E\le\sqrt{J^2+R^2}\).

Put \(t=|B|\in[0,R]\), \(E(t)=\sqrt{J^2+R^2-t^2}\), and \(\Delta(t)=E(t)-t\). Multiplying numerator and denominator in (1) by \(2e^{-\beta E}\) yields the exact expression
\[
F_\beta(t)=\frac{J}{E(t)}
\frac{1-e^{-2\beta E(t)}-(2E(t)/J)e^{-\beta E(t)}}
{1+e^{-2\beta E(t)}+e^{-\beta(E(t)-t)}+e^{-\beta(E(t)+t)}}.
\tag{2}
\]
Notice \(E'(t)=-t/E(t)\) and \(\Delta'(t)=-1-t/E(t)<0\).

**Subcritical budget \(R<J\).** Here \(\Delta(t)\ge J-R=:\delta>0\). Group the exponentially small terms of (2) as \(F_\beta(t)=(J/E(t))(1+\eta_\beta(t))\). Elementary differentiation, using \(E'(t)=-t/E(t)\), \(\sinh(\beta t)\le\beta t\cosh(\beta t)\), and \(E(t)-t\ge\delta\), gives constants depending only on \(J,R\) with
\[
\sup_{0\le t\le R}|\eta_\beta(t)|\le C e^{-\beta\delta},
\qquad
|\eta_\beta'(t)|\le C(1+\beta)^2 t e^{-\beta\delta}.
\]
All terms are smooth at \(t=0\), with \(\eta_\beta'(0)=0\) because the expression is even in \(t\). Since \((J/E)'=Jt/E^3\), the exact derivative \(F'_\beta(t)\) is strictly positive for \(0<t\le R\) when \(\beta\) is large enough. Thus \(t=R\) is the unique maximizing magnitude, implying \(b=0\). Formula (1) then gives \(\mathcal C_{\max}=[\sinh(\beta J)-1]/[\cosh(\beta J)+\cosh(\beta R)]\to1\).

**Critical and supercritical budget \(R\ge J\).** Now \(s=\sqrt{(J^2+R^2)/2}\le R\), and \(\Delta(s)=0\). For each fixed \(t<s\), formula (2) converges to \(J/E(t)\); for each \(t>s\), it converges to zero; at \(t=s\) it converges to \(J/(2s)\). Choose \(t_\beta=s-\beta^{-1/2}\), which lies in \((0,R)\) for large \(\beta\); then \(t_\beta\to s\), \(\beta\Delta(t_\beta)\to+\infty\), and \(F_\beta(t_\beta)\to J/s\).

Compactness and the exact formula show that every sequence of maximizing magnitudes must converge to \(s\): any accumulation point strictly below \(s\) gives a smaller limit \(J/E(t)<J/s\), and any point strictly above \(s\) gives zero. If along a maximizing sequence \(\beta\Delta(t)\) stayed bounded above, the limiting normalized logistic factor in (2) would be strictly below one, contradicting the trial value \(J/s\). Therefore every maximizer has \(t\to s\), \(\beta\Delta(t)\to+\infty\), and eventually \(0<t<s\), so is an interior stationary point of \(F_\beta\).

Near \(s\), expression (2) and its first derivative differ exponentially from the logistic approximation \((J/E)/(1+e^{-\beta\Delta})\). Differentiating the logarithm at any maximizing \(t\) gives
\[
0=\frac{t}{E^2}+\frac{\beta\Delta'(t)}{1+e^{\beta\Delta(t)}}+O(\beta e^{-c\beta}),
\]
for some \(c>0\) depending on \(J,R\). As \(t,E\to s\), \(\Delta'\to-2\), whence
\[
e^{\beta\Delta(t)}\sim2\beta s,\qquad
\beta\Delta(t)=\log(2\beta s)+o(1).
\]
Using \(E(t)^2+t^2=2s^2\), one has \(t=s-\Delta/2+O(\Delta^2)\). This proves the asserted field allocation. In (2), the prefactor has expansion \((J/s)[1-\Delta/(2s)+O(\Delta^2)]\), and the logistic correction is \(e^{-\beta\Delta}\sim1/(2\beta s)\). Combining them proves the maximum-concurrence expansion. Finally, \(b^2=R^2-t^2\); when \(R=J\), this yields \(b^2\sim J\log(2\beta J)/\beta\).

## Verification

The standalone program `verify_fixed_budget.py` constructs the full four-by-four Gibbs state and computes concurrence directly from the Wootters spin-flip eigenvalues; it independently compares this answer with (1) over a seeded sample of positive \(J,R,\beta\) and feasible fields. It also solves finite-temperature one-dimensional optimizations, checking the exact subcritical endpoint and the logarithmic allocation and value asymptotics in critical and supercritical parameter regimes. The numerical tests do not prove the global, all-parameter statements; those follow from the analysis above.

## Relationship to prior work

Sun, Chen and Chen (2003) calculate thermal concurrence for the two-spin XY model under nonuniform fields. Asoudeh and Karimipour (2004 preprint; 2005 journal) and Zhang and Li (2005) analyze field inhomogeneity, eigenstates and entanglement thresholds in Heisenberg dimers. The exact Gibbs block and concurrence formula used here are standard and are **not** claimed as new. Kuwahara and Hatano (2011) study optimizing two-qubit thermal entanglement when the local Hamiltonian is freely adjustable; their objective and admissible field set differ from the quadratic equality-budget problem. The stated finding is restricted to the sharp \(R=J\) budget transition and the full leading and first correction to low-temperature optimal allocation and concurrence. A relevant original Sun et al. article could not be inspected in full, so complete historical priority is not established.

## Limitations

The result is for two spins with fixed-sign XX exchange, pure longitudinal static local fields, an exact quadratic budget, and a canonical thermal state. It makes no claim about temperature-uniform optimizer uniqueness, other entanglement measures, general XYZ couplings, arbitrary field orientations, interacting spin chains, or laboratory control noise. Concurrence is computed in exact arithmetic symbolically in the proof; finite numerical checks have ordinary floating-point limitations. The inaccessible original full text of Sun, Chen and Chen (2003) leaves residual priority uncertainty despite the statement-level comparison available from its abstract and later full texts.

## References

1. Y. Sun, Y. Chen and H. Chen, *Thermal entanglement in the two-qubit Heisenberg XY model under a nonuniform external magnetic field*, Phys. Rev. A **68**, 044301 (2003), DOI: 10.1103/PhysRevA.68.044301; published 2003-10-06.
2. M. Asoudeh and V. Karimipour, *Thermal entanglement of spins in an inhomogeneous magnetic field*, arXiv:quant-ph/0407073 (public 2004), Phys. Rev. A **71**, 022308 (2005), DOI: 10.1103/PhysRevA.71.022308.
3. G.-F. Zhang and S.-S. Li, *Thermal entanglement in a two-qubit Heisenberg XXZ spin chain under an inhomogeneous magnetic field*, arXiv:quant-ph/0509009 (2005), Phys. Rev. A **72**, 034302 (2005), DOI: 10.1103/PhysRevA.72.034302.
4. T. Kuwahara and N. Hatano, *Maximization of thermal entanglement of arbitrarily interacting two qubits*, arXiv:1104.0485 (2011), Phys. Rev. A **83**, 062311 (2011), DOI: 10.1103/PhysRevA.83.062311.
