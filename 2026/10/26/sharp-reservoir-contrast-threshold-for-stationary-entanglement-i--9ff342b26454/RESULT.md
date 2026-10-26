# Sharp reservoir-contrast threshold for stationary entanglement in an exchange-coupled qubit pair

## Finding

Consider two coherently exchange-coupled qubits with independent, locally acting excitation and relaxation channels of equal **total** rate. A nonzero stationary spin-flip coherence, as encountered in the earlier no-go/synchronization model, does not by itself imply entanglement. The complete entanglement-feasibility diagram admits a sharp formula.

Let \(0<p_1,p_2<1\), \(\kappa>0\), and \(\Delta\in\mathbb R\). Write
\[
q=\frac{p_1+p_2}{2},\qquad d=\frac{p_1-p_2}{2},\qquad h=q(1-q),\qquad
 t=\frac{2|J|}{\sqrt{\kappa^2+\Delta^2}}.
\]
With exchange amplitude \(J\in\mathbb R\), the unique steady state has strictly positive two-qubit concurrence for **some** choice of \(J\) if and only if
\[
\boxed{d^2>\frac{h^2}{1-2h}.}
\]
If the inequality is false, no exchange strength or detuning can create stationary entanglement within the stated model. If it is true, positive concurrence occurs at precisely one nonempty **bounded open interval** of the dimensionless exchange strength \(t\), whose endpoints are explicit below. Detuning affects this interval only through the normalization \(\sqrt{\kappa^2+\Delta^2}\).

In the particularly natural case of complementary bath occupations \(p_1+p_2=1\), set \(m=p_1-p_2\). Then the existence condition and entire interval simplify to
\[
\boxed{|m|>\frac1{\sqrt2},\qquad
|m|-\sqrt{2m^2-1}<t<|m|+\sqrt{2m^2-1}.}
\]
Its dimensionless width is **exactly** \(2\sqrt{2m^2-1}\), including arbitrarily close to the threshold, rather than merely asymptotically proportional to a square root.

## Assumptions and scope

Use the computational basis \(\{|00\rangle,|01\rangle,|10\rangle,|11\rangle\}\), with \(n_i=\sigma_i^+\sigma_i^-\). The dynamics is the completely positive, trace-preserving local Lindblad equation
\[
\dot\rho=-i[H,\rho]+\kappa\sum_{i=1}^{2}
\left[p_i\mathcal D[\sigma_i^+]\rho+(1-p_i)\mathcal D[\sigma_i^-]\rho\right],
\quad\mathcal D[L]\rho=L\rho L^\dagger-\tfrac12\{L^\dagger L,\rho\},
\]
with
\[
H=\frac{\Delta}{2}(n_1-n_2)+J(\sigma_1^+\sigma_2^-+\sigma_1^-\sigma_2^+).
\]
The two total local jump rates are both \(\kappa\); the individual excitation/relaxation probabilities need not agree. The strict bounds \(0<p_i<1\) make all four local jump channels available. The statement concerns unconditional two-qubit stationary entanglement, measured by concurrence, without postselection, feedback, or collective bath operators. The Hamiltonian may also contain a diagonal term proportional to \(n_1n_2\), which has no effect on the allowed one-excitation coherence or the populations, but this optional generalization is not needed for the theorem.

## Proof

**1. Unique invariant state and its block structure.** The local raising and lowering matrices on both qubits generate the full matrix algebra. With all four rates strictly positive, the finite-dimensional quantum Markov semigroup has a unique full-rank invariant state; in particular its trace-one stationary equation has one solution. The generator is covariant under simultaneous phase rotation by total excitation number. Uniqueness then implies that the stationary density matrix is an \(X\)-state: its only possible off-diagonal pair is \(\rho_{10,01}=c\), with conjugate at the symmetric position.

Let \(u_i=\operatorname{Tr}(n_i\rho)\), \(w=u_1-u_2\), and \(P_{11}=\langle11|\rho|11\rangle\). Directly applying the specified generator yields
\[
\dot u_1=\kappa(p_1-u_1)-2J\operatorname{Im}c,\qquad
\dot u_2=\kappa(p_2-u_2)+2J\operatorname{Im}c,
\]
\[
\dot c=-(\kappa+i\Delta)c+iJw,\qquad
\dot P_{11}=\kappa(p_1u_2+p_2u_1-2P_{11}).
\]
The sign convention of \(c\) corresponds to the order \(\rho_{10,01}\). From these four closed equations one obtains, with \(z=(1+t^2)^{-1}\),
\[
 w=2dz,\quad u_1=q+dz,\quad u_2=q-dz,\quad
 c=\frac{2iJdz}{\kappa+i\Delta},
\]
\[
P_{11}=q^2-d^2z,\qquad P_{00}=(1-q)^2-d^2z.
\]
In particular \(|c|=|d|\sqrt{z(1-z)}\); this relation holds because \(t\ge0\). The other diagonal entries are \(P_{01}=u_2-P_{11}\) and \(P_{10}=u_1-P_{11}\). These formulae explicitly reconstruct the entire state, not only its spin-flip coherence.

**2. Concurrence criterion.** For this \(X\)-state, the Wootters expression reduces exactly to
\[
C=2\max\{0,|c|-\sqrt{P_{00}P_{11}}\}.
\]
Both populations are positive under the strict jump-rate hypotheses. Therefore \(C>0\) precisely when
\[
F(z)=d^2z(1-z)-[q^2-d^2z][(1-q)^2-d^2z]>0.
\]
Using \(h=q(1-q)\), expand the difference into the strictly concave quadratic
\[
F(z)=-h^2+2d^2(1-h)z-d^2(1+d^2)z^2.
\]
For \(d=0\) it is negative. For \(d\ne0\) its unrestricted maximizer is
\[
z_0=\frac{1-h}{1+d^2}\in(0,1).
\]
Moreover \(F(0)=-h^2<0\) and
\(F(1)=-[q^2-d^2][(1-q)^2-d^2]<0\).
The maximum is positive exactly when
\[
\frac{d^2(1-h)^2}{1+d^2}-h^2>0
\quad\Longleftrightarrow\quad d^2(1-2h)>h^2.
\]
Here \(1-2h>0\) for all \(0<q<1\). Thus failure of the sharp inequality precludes entanglement at every coupling, while strict satisfaction produces two distinct roots in \((0,1)\) and one interval between them.

**3. Exact interval and special symmetry.** When the threshold is satisfied, define
\[
z_\pm=\frac{1-h\pm\sqrt{1-2h-h^2/d^2}}{1+d^2},
\qquad 0<z_-<z_+<1.
\]
Because \(t=\sqrt{(1-z)/z}\) strictly decreases with \(z\), the full positive-concurrence interval is
\[
\boxed{\sqrt{\frac{1-z_+}{z_+}}<t<\sqrt{\frac{1-z_-}{z_-}}.}
\]
No other intervals exist because the concurrence sign is controlled by a quadratic with exactly two roots.

For \(q=1/2\), write \(m=2d\). Multiplying \(F((1+t^2)^{-1})\) by \(16(1+t^2)^2\) gives exactly
\[
-\bigl[t^2-2mt+(1-m^2)\bigr]\bigl[t^2+2mt+(1-m^2)\bigr].
\]
Hence positive concurrence is possible if and only if \(m^2>1/2\), and the two positive boundaries are \(|m|\pm\sqrt{2m^2-1}\). This proves the asserted exact square-root window. All strict endpoint inequalities are essential: the concurrence vanishes at each endpoint and at the threshold itself.

## Verification

The standalone file `check_lindblad.py` constructs the actual complex \(16\times16\) Liouvillian from its local jump operators, solves the trace-one stationary equation directly, and compares it to the reconstructed closed-form state. It also computes Wootters concurrence from the four eigenvalues of the spin-flipped density matrix, independently checks the sharp interval, and tests the balanced-bath square-root boundaries. It requires Python 3 and NumPy. Running `python check_lindblad.py` prints check counts and fails on any detected mismatch. Exact polynomial identities in the proof, not the finite numerical tests, establish the theorem for all parameter values.

## Relationship to prior work

Wang, Qi, Lu, Wu, and Jie (arXiv:2302.00976; first public 2023-02-02) introduced the underlying local gain/loss Heisenberg-qubit setup, proved an uncorrelated stationary state for **equal gain/loss ratios**, and supplied an exact two-qubit spin-flip coherence (their Eq. (7)) to study synchronization. Those source contributions are assumed and not claimed as new. The present result addresses a different question: for unequal occupations, when does *any tunable exchange strength* actually generate entanglement rather than merely coherence? This requires the previously unreported sharp occupation-population competition and optimizes its sign over all exchange strengths.

Wang, Wu, and Wang (arXiv:1812.04799) analyzed related two-qubit entanglement under local bosonic/fermionic reservoirs through a nonsecular Bloch–Redfield generator with system-eigenenergy-dependent bath rates. This is not the independently specified local, equal-total-rate Lindblad generator used here; its equilibrium and nonequilibrium concurrence formulas do not directly give the present threshold. Tacchino, Auffèves, Santos, and Gerace (arXiv:1710.01377) use symmetric/antisymmetric *collective* jump operators, again giving a different Lindbladian. Triana and Fonseca (Frontiers in Optics 2017, JW4A.20) considered the special extreme case of incoherently pumping one qubit while the other decays; the accessible abstract mentions optimizing stationary entanglement in that special configuration. The present general mixed-occupation phase boundary does not follow from that special case. Broader equivalences beyond the inspected literature cannot be categorically excluded.

## Limitations

The result is exact for two qubits with equal **total** local jump rates, strictly positive excitation and relaxation rates, exchange-only coherent mixing, and unconditional steady states. It does not assert the same phase boundary for unequal total dissipation rates, collective baths, non-Markovian dynamics, many-qubit networks, driven coherent pumping, or arbitrary coherent interactions. The result gives existence and the full coupling interval, not a general closed formula for the concurrence-maximizing coupling. Published two-qubit entanglement literature is extensive, so an equivalent formulation outside the sources inspected remains an originality risk. Independent scientific validation has not been performed.

## References

1. Z. Wang, R. Qi, Y. Lu, Z. Wu, J. Jie, *Absence of Correlations in Dissipative Interacting Qubits: a No-Go Theorem*, arXiv:2302.00976 (first public 2023-02-02), https://arxiv.org/html/2302.00976v1 .
2. Z. Wang, W. Wu, J. Wang, *Steady-state entanglement and coherence of the coupled qubit system in equilibrium and nonequilibrium environments*, arXiv:1812.04799 (2018), https://arxiv.org/abs/1812.04799 .
3. F. Tacchino, A. Auffèves, M. F. Santos, D. Gerace, *Steady state entanglement beyond thermal limits*, arXiv:1710.01377 (2017), https://arxiv.org/abs/1710.01377 .
4. J. C. Triana, K. M. Fonseca, *Competition Between Incoherent Pumping and Losses in a System of Two Interacting Qubits*, Frontiers in Optics (2017), JW4A.20, https://opg.optica.org/abstract.cfm?uri=FiO-2017-JW4A.20 .
5. W. K. Wootters, *Entanglement of formation of an arbitrary state of two qubits*, Phys. Rev. Lett. 80, 2245 (1998).
