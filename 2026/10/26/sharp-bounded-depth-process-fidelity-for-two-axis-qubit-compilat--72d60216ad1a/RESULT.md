# Sharp bounded-depth process fidelity for two-axis qubit compilation

## Finding
Fix two nonparallel qubit-control axes meeting at an acute angle \(0<\theta\leq\pi/2\). For a nonnegative integer \(m\), let \(\mathcal C_m\) consist of all alternating gate products with \(m\) uses of the tilted axis and freely chosen rotations about the first axis at both ends. The **sharp finite-depth process fidelity** to every target \(W\in SU(2)\), and the complete Haar-target distribution of that fidelity, are explicit.

Write \(\beta(W)=2\arcsin|W_{21}|\in[0,\pi]\) in the computational basis of the first control axis, and put \(c_m=\min\{2m\theta,\pi\}\). Then
\[
\max_{V\in\mathcal C_m}\frac{|\operatorname{tr}(W^*V)|^2}{4}
=\cos^2\left(\frac{(\beta(W)-c_m)_+}{2}\right).
\]
Here \((r)_+=\max(r,0)\). In particular, exact synthesis is possible exactly when \(\beta(W)\leq c_m\). For a Haar-distributed target \(W\), let the displayed maximum be \(F_m\). It has an atom of mass \(\sin^2(c_m/2)\) at \(F_m=1\), and, for \(\sin^2(c_m/2)\leq f\leq1\),
\[
\mathbb P(F_m\geq f)=\sin^2\left(\frac{c_m}{2}+\arccos\sqrt f\right).
\]
Outside this interval the survival probability is one below the interval and zero above it. The exact mean optimal process infidelity is
\[
\mathbb E(1-F_m)
=\frac{1+\cos c_m}{4}-\frac{(\pi-c_m)\sin c_m}{8}.
\]
As \(c_m\uparrow\pi\), the mean optimal infidelity vanishes **quartically**, while the worst-case optimal infidelity vanishes quadratically:
\[
\mathbb E(1-F_m)=\frac{(\pi-c_m)^4}{96}+O((\pi-c_m)^6),
\qquad\sup_W(1-F_m(W))=\sin^2\left(\frac{\pi-c_m}{2}\right).
\]
The law gives an exact average-case-versus-worst-case performance benchmark for alternating two-Hamiltonian qubit-gate compilation with a prescribed number of tilted-control segments.

## Assumptions and scope
Let \(\sigma_x,\sigma_z\) be Pauli matrices, and define the full-angle one-parameter subgroups
\[
A(\alpha)=\exp(-i\alpha\sigma_z/2),\qquad
B_\theta(\gamma)=\exp[-i\gamma(\sin\theta\,\sigma_x+\cos\theta\,\sigma_z)/2].
\]
Angles \(\alpha,\gamma\) are arbitrary real numbers modulo \(4\pi\), including negative values. The controlled circuit family is
\[
\mathcal C_m=\{A(\alpha_0)B_\theta(\gamma_1)A(\alpha_1)\cdots
 B_\theta(\gamma_m)A(\alpha_m):\alpha_j,\gamma_j\in\mathbb R\}.
\]
For \(m=0\), this is just the first-axis subgroup. All gates, including the target and approximant, belong to \(SU(2)\). The score \(|\operatorname{tr}(W^*V)|^2/4\) is the phase-insensitive **process (entanglement) fidelity** of ideal unitary channels; it is not the ordinary average qubit-state gate fidelity (which equals \((2F+1)/3\)). The Haar distribution is normalized Haar measure on \(SU(2)\). The depth is the count of tilted-axis segments in this specifically stated first-axis-ended architecture, not the globally shortest unrestricted two-axis word and not elapsed physical control time.

## Proof
**1. Exact reachable-set cap.** Let \(n\) denote the north pole of the Bloch sphere corresponding to the ray of \(|0\rangle\), let \(R_U\in SO(3)\) be the action of a unitary \(U\), and let \(\beta(U)=d(n,R_Un)\), with \(d\) the great-circle distance. This agrees with \(2\arcsin|U_{21}|\).

Rotations \(A(\alpha)\) preserve colatitude. The tilt-axis unit vector \(b=(\sin\theta,0,\cos\theta)\) satisfies \(d(n,R_{B_\theta(\gamma)}n)\leq2\theta\). By the triangle inequality and invariance of spherical distance, applying one tilted-axis rotation changes the colatitude of any state by at most \(2\theta\). Therefore every product in \(\mathcal C_m\) satisfies \(\beta(U)\leq c_m\).

For the converse, prove inductively that the reachable Bloch vectors form the entire north-polar cap of radius \(c_m\). For \(m=0\), only the north pole is reached. The reachable colatitudes for \(m+1\) form an interval: the image of the connected torus of pulse parameters under the continuous colatitude map is connected, and the identity pulses give zero. If \(c_m+2\theta\leq\pi\), take a previously reachable vector on the meridian opposite \(b\) at colatitude \(c_m\); a half-turn about \(b\) sends it to colatitude \(c_m+2\theta\). If \(c_m+2\theta\geq\pi\), a previously reachable vector at colatitude \(\pi-2\theta\) on that meridian is sent to the south pole by the same half-turn. Since the leading \(A\)-pulse can rotate every reachable Bloch vector through any azimuth, all colatitudes between zero and \(\min\{c_m+2\theta,\pi\}\) and all azimuths are attained.

Finally, if two \(SU(2)\) matrices send the ray of \(|0\rangle\) to the same ray, their relative product fixes that ray and hence belongs to the \(A\)-subgroup. The freely adjustable rightmost \(A\)-pulse realizes every lift over an attainable Bloch vector. Thus the exact gate set is
\[
\mathcal C_m=\{U\in SU(2):\beta(U)\leq c_m\}.
\]

**2. Exact distance to the reachable set.** Write \(u=W|0\rangle\) and \(v=V|0\rangle\). The special-unitary matrix identity \(\operatorname{tr}(W^*V)=2\operatorname{Re}\langle u,v\rangle\) holds in the standard special-unitary parametrization. For any fixed ray \([v]\), right multiplication of \(V\) by an \(A\)-rotation changes the phase of its first column without changing its Bloch vector. It can therefore attain \(|\operatorname{tr}(W^*V)|/2=|\langle u,v\rangle|\). The Bloch-ray overlap is \(|\langle u,v\rangle|^2=(1+n_u\cdot n_v)/2=\cos^2(d(n_u,n_v)/2)\). Among vectors in the cap of radius \(c_m\), the closest one to the target vector at colatitude \(\beta(W)\) lies on the same meridian, at colatitude \(\min(\beta(W),c_m)\). Its distance is \((\beta(W)-c_m)_+\). This proves the first boxed formula globally, including boundary targets and the pole cases.

**3. Haar distribution and moment.** Normalized Haar measure on \(SU(2)\) pushes forward under \(W\mapsto W|0\rangle\) to uniform surface measure on the Bloch sphere. Thus the target colatitude has density \(\frac12\sin\beta\) on \([0,\pi]\). Perfect compilation is possible for the cap of area fraction \((1-\cos c_m)/2=\sin^2(c_m/2)\), giving the atom. For \(f\) between the smallest and largest achievable fidelity, the event \(F_m\geq f\) is exactly
\[
\beta\leq c_m+2\arccos\sqrt f.
\]
Integrating its colatitude density gives the stated survival law. Likewise
\[
\mathbb E(1-F_m)=\frac12\int_{c_m}^{\pi}
\sin\beta\,\sin^2\left(\frac{\beta-c_m}{2}\right)\,d\beta
=\frac{1+\cos c_m}{4}-\frac{(\pi-c_m)\sin c_m}{8}.
\]
Putting \(\delta=\pi-c_m\) and Taylor-expanding gives \(\delta^4/96-\delta^6/1440+O(\delta^8)\). The largest distance from the cap occurs at the south pole and equals \(\delta\), yielding the stated worst-case infidelity. Every displayed optimum is attained by compactness and by the explicit ray projection just constructed.

## Verification
The standalone `verify.py` numerically tests the analytic process-fidelity formula against direct optimization of actual products of Pauli-matrix rotations for several target angles and one- and two-tilt depths; it separately checks the Haar mean against numerical quadrature and tests the predicted Haar cumulative law using independently sampled Haar qubit matrices. Run with `python verify.py` using Python 3, NumPy and SciPy. These finite checks corroborate, but do not replace, the all-parameter geometric proof.

## Relationship to prior work
Garbaravičius and Wolf (arXiv:2610.17826v1, October 13, 2026) ask for universal switch-count upper bounds for a fixed Hamiltonian pair and mean bounds when the **basis pair** is drawn at random. Their qubit related-work discussion quotes the two-axis worst-case exact rotation-count formula. The present result instead fixes the axis pair and derives an optimal **approximation-fidelity profile over Haar-random target gates at fixed tilt depth**. It does not assert a new universal exact-generation count.

Hamada (arXiv:1401.0153; Royal Society Open Science, 2014) proves the stronger pointwise theorem for the globally minimal number of exact rotations about two arbitrary axes, and gives constructive decompositions. In particular, his spherical-distance inequalities and alternating construction underpin the exact-synthesis cap used in step 1; that cap and the exact switching bound are **not claimed to be novel here**. The evaluated extension is the optimal trace-fidelity distance to the bounded-depth reachable family, its full Haar-target law and exact quadratic-versus-quartic worst/mean infidelity separation. Time-optimal two-control work by Aiello and collaborators uses physical execution time rather than a fixed maximum number of tilted-axis factors. Peterson, Bishop and Javadi-Abhari optimize approximate **two-qubit XX-gate** compilations, not this one-qubit two-axis geometry.

## Limitations
The control angles are unrestricted in sign and duration; the result is not valid verbatim for pulse-length limits, positive bounded times, noisy pulses, unknown Hamiltonian axes, higher-dimensional qudits or architectures with a different allowed word pattern. The use of freely adjustable beginning and ending \(A\)-rotations is essential. Near-threshold quartic convergence concerns **mean optimal process infidelity across Haar targets**, not worst-case error. The derivation of the cap uses classical two-axis geometry, so the novelty rests on the combined optimal-fidelity and Haar-profile evaluation, not on a new exact-synthesis reachability theorem. The literature comparison is best-knowledge and does not certify global priority; independent audit has not been performed.

## References
1. M. Garbaravičius and M. M. Wolf, *How many switches does two-Hamiltonian universality require?*, arXiv:2610.17826v1 (first public October 13, 2026), https://arxiv.org/html/2610.17826v1.
2. M. Hamada, *The minimum number of rotations about two axes for constructing an arbitrarily fixed rotation*, Royal Society Open Science **1**, 140145 (2014), arXiv:1401.0153; https://doi.org/10.1098/rsos.140145.
3. C. D. Aiello et al., *Algebraic Synthesis of Time-Optimal Unitaries in SU(2) with Alternating Controls*, Quantum Information Processing **14**, 3233–3249 (2015), https://doi.org/10.1007/s11128-015-1045-6.
4. E. C. Peterson, L. S. Bishop and A. Javadi-Abhari, *Optimal synthesis into fixed XX interactions*, Quantum **6**, 696 (2022), https://doi.org/10.22331/q-2022-04-27-696.
