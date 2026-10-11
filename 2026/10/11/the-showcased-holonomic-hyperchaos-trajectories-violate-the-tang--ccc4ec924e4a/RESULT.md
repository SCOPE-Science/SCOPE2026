# The showcased holonomic hyperchaos trajectories violate the tangent constraint at initialization
## Finding
Li and Cui impose the holonomic sphere constraint
\[
\|q\|^2=L^2
\]
on their six-dimensional Hamiltonian system and explicitly differentiate it to obtain
\[
q\cdot p=0.
\]
Because their constrained equations also have \(\dot q=p\), the actual constrained phase space is
\[
\mathcal M_L=\{(q,p):\|q\|^2=L^2,\ q\cdot p=0\}.
\]
At the numerical value \(L=0.01\), however, none of the three initial states used for the holonomic hyperchaos and sensitivity calculations lies in \(\mathcal M_L\). For the blue state
\[
q=(0,0,0.01),\qquad p=(0.011,0.051,0.051),
\]
and for the magenta state
\[
q=(0,0.01,0),\qquad p=(0.011,0.051,0.051),
\]
one has
\[
q\cdot p=\frac{51}{100000}=5.1\times10^{-4}.
\]
For the green state
\[
q=(0.01,0,0),\qquad p=(0.011,0.051,0.051),
\]
one has
\[
q\cdot p=\frac{11}{100000}=1.1\times10^{-4}.
\]
All three satisfy the position constraint \(\|q\|^2=L^2=10^{-4}\), but all three fail its necessary velocity-level constraint.

Thus the Lyapunov-exponent computation used to declare the holonomic system hyperchaotic, together with the three-trajectory sensitivity illustration and the associated Poincaré calculation from the first state, is initialized outside the stated constrained phase space.

## Assumptions and scope
The claim concerns the holonomic model in Section 3.1 of Li–Cui and the three initial conditions printed immediately after their equation (3.5). The only structural assumptions are the source equations \(\dot q=p\), the sphere constraint \(\|q\|^2=L^2\), and \(L\ne0\). No numerical integration, asymptotic approximation, or assumption about the existence of a chaotic invariant set is used.

The result distinguishes the constrained dynamics from the algebraic six-dimensional formula printed as equation (3.5). That formula can be evaluated away from the sphere, but such an off-sphere evaluation is not a trajectory satisfying the holonomic constraint from which the formula was derived.

## Proof
Define the constraint defect
\[
R(q)=\|q\|^2-L^2.
\]
Since \(\dot q=p\), differentiation gives the exact identity
\[
\dot R=2q\cdot p.
\]
Therefore a differentiable trajectory that remains on \(R=0\) must satisfy \(q\cdot p=0\) at every time, including initially. This is also equation (3.2) in the source.

Substitution of the source's three listed initial conditions gives the exact dot products above. Consequently each has \(R(0)=0\) but \(\dot R(0)>0\). By differentiability, \(R(t)>0\) for all sufficiently small positive \(t\), so integration of the printed vector field from any of those states immediately leaves the sphere.

There is also an exact defect dynamics for the printed equation (3.5). Put
\[
B(q)=\big(-\beta q_1^3+\eta^2q_1-\eta(q_2+q_3),\ -\beta q_2^3-\eta q_1,\ -\beta q_3^3-\eta q_1\big)
\]
and \(S=q\cdot p\). Direct expansion of the three printed numerators \(F_i\) gives
\[
L^2\dot p=L^2B(q)-q\big(q\cdot B(q)+\|p\|^2\big).
\]
Hence
\[
\dot S=\|p\|^2+q\cdot\dot p
       =-\frac{R}{L^2}\big(q\cdot B(q)+\|p\|^2\big).
\]
Together with \(\dot R=2S\), this proves that \(R=S=0\) is invariant and pinpoints the initial tangency defect of the reported trajectories.

## Verification
A dependency-free exact-arithmetic checker accompanies this result. It verifies, as polynomial identities, that all three numerators in equation (3.5) equal
\[
L^2B_i-q_i\big(q\cdot B+\|p\|^2\big),
\]
checks the resulting defect identity after clearing \(L^2\), and evaluates the three source initial conditions using rational arithmetic. The replayed output ends in `VERIFY_OK`.

## Relationship to prior work
Li and Cui explicitly state both the holonomic constraint \(\|q\|^2=L^2\) and its differentiated condition \(q\cdot p=0\), and then report hyperchaos from the initial state \((0,0,0.01,0.011,0.051,0.051)\), followed by two additional sensitivity initial states. Their cited constrained-Hamiltonian reference by Udwadia states that constrained initial data cannot be prescribed arbitrarily and must satisfy the constraint equations at the initial time; its spherical example likewise differentiates a fixed-radius constraint to obtain the tangency condition \(q^Tp=0\).

The closest database comparisons located during the originality check concern different systems in which a hidden constraint, conserved leaf, or extraneous mode changes the interpretation of numerical dynamics. None covers this Li–Cui sphere/tangent mismatch or implies the exact three initial-data calculations here.

## Limitations
This finding does not prove that the correctly initialized constrained system lacks hyperchaos, periodic orbits, or other complicated invariant dynamics. It establishes only that the specific Lyapunov, sensitivity, and Poincaré evidence produced from the three published initial states is off the stated holonomic phase space. It also does not assign physical meaning to the off-sphere continuation of equation (3.5); the defect equations above are an algebraic property of the printed formula and are used only to show what happens if that formula is integrated from the listed inconsistent data.

## References
1. J. Li and N. Cui, “Dynamical behavior and control of a new hyperchaotic Hamiltonian system,” AIMS Mathematics 7(4), 5117–5132. DOI: 10.3934/math.2022285. Published 31 December 2021. See equations (3.1)–(3.5) and the numerical discussion following Table 3.
2. F. E. Udwadia, “Constrained motion of Hamiltonian systems,” Nonlinear Dynamics 84, 1135–1145. DOI: 10.1007/s11071-015-2558-3. See the initial-condition requirement and the spherical-constraint example.
