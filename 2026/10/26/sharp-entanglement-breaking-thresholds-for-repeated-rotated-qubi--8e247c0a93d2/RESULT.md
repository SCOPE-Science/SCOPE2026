# Sharp entanglement-breaking thresholds for repeated rotated qubit dephasing

## Finding
Let \(0<q<1\), and let \(\mathcal D_q\) be qubit phase damping that multiplies off-diagonal matrix entries by \(q\) while preserving diagonal entries. For each qubit unitary \(U\), set \(\Phi_{q,U}=\mathcal D_q\circ\operatorname{Ad}_U\). The *same* unitary \(U\) is used at every application. For an integer \(n\geq1\), let \(M_{q,U,n}\) be the real \(3\times3\) Bloch matrix of \(\Phi_{q,U}^{\,n}\), and define \(F_n(q)=\min_U\|M_{q,U,n}\|_*\), with \(\|\cdot\|_*\) the sum of singular values.

Then the exact optimum is
\[
F_n(q)=\begin{cases}1+2q,&n=1,\\2q+q^2,&n=2,\\3q^{2n/3},&n\geq3.\end{cases}
\]
For every \(n\geq3\), some fixed qubit unitary \(U=U(q,n)\) produces the stronger identity
\[
\Phi_{q,U}^{\,n}(\rho)=q^{2n/3}\rho+(1-q^{2n/3})I_2/2
\]
for every density matrix \(\rho\): a power of the anisotropic rotated dephasing channel is **exactly depolarizing**. The associated sharp finite-step entanglement-breaking conditions are
\[
\begin{aligned}
n=1 &: \quad \text{never for }0<q<1,\\
n=2 &: \quad q\leq\sqrt2-1,\\
n\geq3 &: \quad q\leq3^{-3/(2n)}.
\end{aligned}
\]
Here the decision quantifier is \(\exists U\); the optimizing \(U\) can depend on the specified \(q\) and \(n\), but cannot vary from one application to the next.

## Assumptions and scope
In the Pauli coordinate order \((\sigma_x,\sigma_y,\sigma_z)\), write each state as \(\rho=(I_2+\vec r\cdot\vec\sigma)/2\). Phase damping has Bloch matrix \(D=\operatorname{diag}(q,q,1)\). Unitary conjugation has some rotation \(R\in SO(3)\), and every such rotation is implementable by a qubit unitary, unique up to global phase and double covering. Thus one application has Bloch matrix \(A=DR\), and \(n\) repeated applications have matrix \(A^n\).

An entanglement-breaking channel sends every bipartite state to a separable state when applied to one party. The standard qubit-unital criterion is that a channel with Bloch matrix \(B\) is entanglement breaking if and only if \(\|B\|_*\leq1\). It follows from reducing \(B\) by input/output Bloch rotations to a signed diagonal matrix and applying the two-qubit positive-partial-transpose criterion to its Choi state. This criterion is recalled from the literature, not claimed as new.

The theorem optimizes across *all* qubit rotations, not only a fixed axis or Clifford gates, but restricts the control to one identical rotation reused at each step. It makes no claim about optimality under arbitrary step-dependent controls, nonunitary filters, higher-dimensional systems, or time-dependent dephasing.

## Proof
**The one- and two-step cases.** Rotational invariance of singular values gives \(\|DR\|_*=1+2q\). For two steps, right-multiplication by \(R^{\mathsf T}\) shows that \(\|(DR)^2\|_*=\|DRD\|_*\). Let \(W\) be the plane orthogonal to the dephasing axis. Both \(W\) and \(R^{-1}W\) are two-dimensional subspaces of \(\mathbb R^3\), so they intersect nontrivially. Choose a unit vector \(w\in W\cap R^{-1}W\). Setting \(B=DRD\), the two identities
\[
Bw=q^2Rw,\qquad B^{\mathsf T}(Rw)=q^2w
\]
show that \(q^2\) is a singular value of \(B\). Since \(|\det B|=q^4\), the two remaining singular values have product \(q^2\). Their sum is therefore at least \(2q\) by arithmetic--geometric mean. Hence \(\|(DR)^2\|_*\geq q^2+2q\). A quarter-turn carrying the dephasing axis to an orthogonal axis makes the singular values exactly \(q,q,q^2\), establishing equality.

**The lower bound for all deeper iterates.** For every \(n\geq1\), \(\lvert\det(A^n)\rvert=q^{2n}\). If the singular values of \(A^n\) are \(s_1,s_2,s_3\), the arithmetic--geometric mean inequality yields
\[
s_1+s_2+s_3\geq3(s_1s_2s_3)^{1/3}=3q^{2n/3}.
\]
It remains to show that the bound can be attained by the same rotation at every step when \(n\geq3\).

**Explicit isotropizing rotation.** Fix \(n\geq3\). Define
\[
u=q^{2/3},\quad h=1+2\cos(2\pi/n),\quad L=1+u+u^2,
\quad T=\frac{uh}{L},\quad S=\frac{\sqrt u(1+u)h}{L}.
\]
Because \(n\geq3\), one has \(0\leq h<3\). We construct a rotation \(R\in SO(3)\) satisfying
\[
R_{33}=T,\qquad R_{11}+R_{22}=S.
\]
First, \(0\leq T\leq1\), \(0\leq S\leq2\), and \(S\leq1+T\). For clarity, the three underlying polynomial inequalities, with \(v=\sqrt u\in(0,1)\), are
\[
\begin{aligned}
L-3u&=(1-v)^2(1+v)^2\geq0,\\
2L-3\sqrt u(1+u)&=(1-v)^2(2v^2+v+2)\geq0,\\
L+3u-3\sqrt u(1+u)&=(1-v)^2(v^2-v+1)\geq0.
\end{aligned}
\]
These inequalities establish the stated bounds after replacing \(h\) by its upper bound \(3\). Set
\[
c=(S+T-1)/2,\qquad z^2=(T-c)/(1-c).
\]
They imply \(-1\leq c<1\) and \(0\leq z^2\leq1\). Let \(R\) be the right-handed rotation of angle \(\arccos c\) about the unit axis \((\sqrt{1-z^2},0,z)\). Rodrigues' formula gives \(R_{33}=c+(1-c)z^2=T\) and \(\operatorname{tr}R=1+2c=S+T\), as required.

To calculate the characteristic polynomial of \(A=DR\), use
\[
\operatorname{tr}A=qS+T=uh,\quad
\det A=q^2=u^3,
\]
and
\[
\frac{(\operatorname{tr}A)^2-\operatorname{tr}(A^2)}2
=(\det A)\operatorname{tr}(A^{-1})
=qS+q^2T=u^2h.
\]
The last expression follows from \(A^{-1}=R^{\mathsf T}D^{-1}\) and the explicit \(S,T\). Consequently
\[
\det(\lambda I_3-A)
=\lambda^3-uh\lambda^2+u^2h\lambda-u^3
=(\lambda-u)(\lambda-ue^{2\pi i/n})(\lambda-ue^{-2\pi i/n}).
\]
For \(n\geq3\) the three complex eigenvalues are pairwise distinct, so \(A\) is diagonalizable over \(\mathbb C\). All three eigenvalues raised to the \(n\)-th power equal \(u^n\). Thus
\[
A^n=u^nI_3=q^{2n/3}I_3.
\]
Its three singular values are all \(q^{2n/3}\), attaining the determinant lower bound. Through the Bloch representation, this matrix identity is precisely the depolarizing-channel identity in the finding.

**Sharp breaking thresholds.** The unital qubit criterion \(\|A^n\|_*\leq1\), together with the three exact minimum formulas, gives the stated inequalities. Since a minimum over rotations is realized in each case, these are necessary and sufficient conditions for the existence of a fixed unitary achieving entanglement breaking by the specified step.

For example, the smallest attainable breaking depth for a fixed \(0<q<1\) is \(2\) when \(q\leq\sqrt2-1\), and otherwise is
\[
\max\left\{3,\left\lceil\frac{3\log3}{-2\log q}\right\rceil\right\}.
\]
Here the ceiling formula includes threshold equality.

## Verification
The accompanying `verify.py` implements the axis-angle construction and tests its rotation orthogonality, characteristic coefficients, exact-power identity, determinant, and nuclear norm for six distinct noise parameters and every depth \(3\leq n\leq30\). It also tests the two-step singular spectrum, threshold sign changes, and randomly sampled competitors. Execute `python verify.py` with `numpy>=1.24`. These are finite floating-point corroborations; the uniform exact theorem is justified by the analytic proof above, not by sampling or numerical optimization. Execution of the supplied verification program completed 1673 passing assertions.

## Relationship to prior work
Bhat, Dey and Saha (2026) characterize eventual entanglement breaking for unital channels by eigenvector commutation conditions and supply a framework for existence, but do not identify this all-depth, control-optimized trace-norm formula or give an identical-rotation isotropizing construction. Lami and Giovannetti (2014/2015) introduce entanglement-breaking indices and the role of interspersed filters, including the established qubit-unital singular-value criterion; the result here uses that criterion, but optimizes **entanglement destruction** among a family of rotated phase-damping channels, under the restriction that the rotation itself is constant over iterations. Cuevas and collaborators (2017) examine intermediate unitaries designed to *preserve* entanglement in repeated noisy channels, rather than this sharp destroying-control problem. Wakaura and Tanimae (2026) show that fixed-axis finite-rate dephasing does not itself become entanglement breaking, making rotation-induced finite-depth breaking a meaningful distinct phenomenon. General bounds on breaking times do not automatically imply the exact constructions and thresholds established here.

## Limitations
The direction of optimization is deliberate: it asks for the **most entanglement-destroying** identical unitary rotation, not the filter maximizing entanglement survival. Distinct choices of optimal rotation may be needed for different depths \(n\). The result is specific to the qubit channel with two equal transverse contraction factors \(q\). It does not address arbitrary nonunital noise, all rotations simultaneously across depths, or uniqueness of the optimal unitary. Published-literature priority is assessed on accessible sources; a general previously published contraction-product isotropization result may contain an equivalent special case. Independent validation has not been performed.

## References
1. B. V. R. Bhat, P. Dey, B. Saha, “A complete characterization of eventually entanglement breaking unital quantum channels,” first public 21 September 2026, arXiv:2609.24168, https://arxiv.org/abs/2609.24168.
2. L. Lami, V. Giovannetti, “Entanglement-Breaking Indices,” arXiv:1411.2517 (2014), https://arxiv.org/abs/1411.2517.
3. A. Cuevas et al., “Amending entanglement-breaking channels via intermediate unitary operations,” Phys. Rev. A 96, 022322 (2017), arXiv:1707.00161, https://arxiv.org/abs/1707.00161.
4. H. Wakaura, T. Tanimae, “Markovian dephasing has no entanglement-breaking threshold, and a fixed tolerance will report one anyway,” arXiv:2604.08587 (2026), https://arxiv.org/abs/2604.08587.
5. F. Sakuldee, Ł. Rudnicki, “Bounds on the breaking time for entanglement-breaking channels,” Phys. Rev. A 107, 022430 (2023), https://doi.org/10.1103/PhysRevA.107.022430.
