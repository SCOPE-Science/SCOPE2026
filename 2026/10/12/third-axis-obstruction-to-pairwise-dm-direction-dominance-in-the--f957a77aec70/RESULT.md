# Third-axis obstruction to pairwise DM-direction dominance in the XYZ dimer
## Finding
Consider the two-qubit anisotropic Heisenberg \(XYZ\) Hamiltonian with a single-axis Dzyaloshinskii--Moriya interaction, in the conventions of Li and Cao. Their pairwise conclusion that \(J_x>J_y\) makes an equal-strength \(D_x\) interaction more effective than \(D_y\) is false without a restriction on the third coupling \(J_z\).

For every \(a>0\), set
\[
J_x=0,\qquad J_y=-a,\qquad J_z=a,\qquad D_x=D_y=a,
\]
and compare the two thermal states at the same temperature \(T>0\). Put \(x=a/T\). Then the \(x\)-directed DM model has
\[
C_x(T)=0\qquad\text{for every }T>0,
\]
whereas the \(y\)-directed DM model has
\[
C_y(T)=\frac{\max\{N(x),0\}}{1+e^{2x}+e^{(\sqrt5-1)x}+e^{-(\sqrt5+1)x}},
\]
with
\[
N(x)=e^{2x}-1-e^{(\sqrt5-1)x}-e^{-(\sqrt5+1)x}.
\]
There is a unique constant \(x_* >0\) satisfying
\[
e^{3x_*}-e^{x_*}-e^{\sqrt5 x_*}-e^{-\sqrt5 x_*}=0,
\]
and
\[
C_y(T)>0\quad\Longleftrightarrow\quad 0<T<\frac{a}{x_*}.
\]
Numerically \(x_*\approx0.5825819526285126\), so \(a/x_*\approx1.716496701430875\,a\). Thus an entire temperature interval reverses the published pairwise directional ordering even though \(J_x>J_y\). The strict reversal at, for example, \(T=a\) persists on an open neighborhood of the displayed parameters by continuity.

## Assumptions and scope
The claim uses the Hamiltonians and concurrence convention in arXiv:0807.1457. Only one DM component is nonzero at a time. The comparison fixes the same exchange couplings, the same positive DM magnitude \(a\), and the same positive temperature in the two directions. It corrects the paper's pairwise \(D_x\)-versus-\(D_y\) statement under the hypothesis \(J_x>J_y\); it does not claim to refute the more restrictive statement in which the chosen exchange coefficient is assumed largest among all three coordinates.

## Proof
For the \(D_x\) model, Li and Cao give
\[
w_x=\sqrt{4D_x^2+(J_y+J_z)^2}
\]
and four Wootters quantities proportional to
\[
e^{(J_x+w_x)/T},\ e^{(J_x-w_x)/T},\ e^{(-J_x+J_y-J_z)/T},\ e^{(-J_x-J_y+J_z)/T}.
\]
On the displayed family \(w_x=2a\), so these are proportional to
\[
e^{2x},\ e^{-2x},\ e^{-2x},\ e^{2x}.
\]
Because \(J_y\le J_z\), the source's concurrence branch is the absolute difference of the first and fourth quantities minus the other two, truncated at zero. The first and fourth are identical. Hence \(C_x(T)=0\) for every \(T>0\).

For the \(D_y\) model, the corresponding quantity is
\[
w_y=\sqrt{4D_y^2+(J_x+J_z)^2}=a\sqrt5.
\]
The four Wootters quantities are proportional to
\[
1,\ e^{2x},\ e^{(\sqrt5-1)x},\ e^{-(\sqrt5+1)x}.
\]
Since \(J_x\le J_z\) and \(2>\sqrt5-1\), the source's second \(D_y\) branch gives exactly the displayed formula for \(C_y\).

Multiplication of \(N(x)\) by the positive factor \(e^x\) shows that its sign is the sign of
\[
G(x)=e^{3x}-e^x-e^{\sqrt5 x}-e^{-\sqrt5 x}.
\]
Dividing by the positive factor \(e^{\sqrt5 x}\) gives
\[
H(x)=e^{(3-\sqrt5)x}-e^{(1-\sqrt5)x}-1-e^{-2\sqrt5 x}.
\]
For \(x>0\),
\[
H'(x)=(3-\sqrt5)e^{(3-\sqrt5)x}+(\sqrt5-1)e^{(1-\sqrt5)x}+2\sqrt5 e^{-2\sqrt5 x}>0.
\]
Also \(H(0)=-2\) and \(H(x)\to\infty\) as \(x\to\infty\). Therefore there is exactly one positive zero \(x_*\), and \(N(x)>0\) exactly when \(x>x_*\). Since \(x=a/T\), this is equivalent to \(0<T<a/x_*\).

To see directly that the reversal is already strict at \(T=a\), note that \(\sqrt5<9/4\), \(8/3<e<11/4\), and \(e^{1/4}<4/3\). The latter two bounds follow immediately from the exponential series and geometric tail estimates. Hence
\[
e^3-e>\frac{1751}{108}>\frac{133}{12}>e^{\sqrt5}+e^{-\sqrt5},
\]
so \(N(1)>0\). Continuity of concurrence in the finite-dimensional Hamiltonian parameters then gives an open neighborhood with \(J_x>J_y\) and \(C_y>C_x\).

## Verification
The bundled `verify.py` evaluates both closed forms, brackets the unique zero by bisection, checks the strict \(T=a\) reversal, and checks the source-level four Boltzmann/Wootters weights. It is supplementary: uniqueness and the all-temperature vanishing of \(C_x\) are proved analytically above.

## Relationship to prior work
Li and Cao derive the single-axis concurrence formulas and then state that, for \(J_x>J_y\), equal \(D_x\) has a smaller critical DM value, higher critical temperature, and more entanglement than equal \(D_y\). Their own formulas yield the family above, so the accepted contribution is the explicit correction and exact threshold mechanism, not a new concurrence formula.

Park later gives a detailed analytic treatment of single-axis thermal concurrence, including mixed-sign regimes where a DM-dependent critical temperature can be nonmonotone or vanish. That work makes clear that the third exchange coupling can affect threshold structure, but the inspected text does not state or repair Li and Cao's pairwise \(D_x\)-versus-\(D_y\) ordering, nor does it identify the family and threshold above.

## Limitations
The result is a counterexample family, not a complete classification of which DM direction maximizes concurrence for arbitrary \((J_x,J_y,J_z,D,T)\). The general single-axis concurrence formulas are prior work. The numerical value of \(x_*\) is illustrative; the exact statement is its characterization as the unique positive root of the displayed equation. A later source could conceivably have noted the same correction under different terminology; this remains the main literature risk.

## References
1. D.-C. Li and Z.-L. Cao, “Effect of different Dzyaloshinskii-Moriya interactions on entanglement in the Heisenberg XYZ chain,” arXiv:0807.1457; *International Journal of Quantum Information* 7 (2009), 547–557, DOI 10.1142/S0219749909005146.
2. D. Park, “Thermal entanglement and thermal discord in two-qubit Heisenberg XYZ chain with Dzyaloshinskii–Moriya interactions,” arXiv:1901.06165; *Quantum Information Processing* 18 (2019), 172, DOI 10.1007/s11128-019-2292-8.
