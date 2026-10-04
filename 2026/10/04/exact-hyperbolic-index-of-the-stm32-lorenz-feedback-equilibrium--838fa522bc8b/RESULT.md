# Exact hyperbolic index of the STM32 Lorenz-feedback equilibrium
## Finding
Consider the autonomous flow
\[
\dot x=40(y-x)+w,\qquad
\dot y=10x+25y-xz,\qquad
\dot z=xy-3z,\qquad
\dot w=dx,
\]
with real parameter \(d>0\). The origin is the unique equilibrium. Its exact characteristic polynomial is
\[
\chi_d(\lambda)=(\lambda+3)\bigl(\lambda^3+15\lambda^2-(1400+d)\lambda+25d\bigr).
\]
For every \(d>0\), the cubic factor has exactly one root in each of \(( -\infty,-40)\), \((0,25)\), and \((25,\infty)\). Consequently the origin is hyperbolic for every \(d>0\), with exactly two negative and two positive real eigenvalues. Its stable and unstable manifold dimensions are therefore both two throughout the entire positive-parameter family.

At \(d=15\), the eigenvalues are approximately
\[
-45.9630825821,\quad -3,\quad 0.2657797580,\quad 30.6973028241.
\]
The source preprint and journal article instead print the parameter-independent list \(-40,25,-3,0\). The exact factorization shows that the zero eigenvalue is spurious and that the local unstable dimension is two, not one.

## Assumptions and scope
The result concerns the exact continuous-time vector field written above and assumes only \(d>0\). The statement is local to the unique equilibrium and makes no assertion that trajectories are globally bounded, that an attractor exists for every \(d\), or that the tangent Lyapunov spectrum along a non-equilibrium invariant set equals the equilibrium spectrum.

The classification uses MSC2020 \(37C10\), “Dynamics induced by flows and semiflows,” because the object is a smooth autonomous flow and the claim concerns the local dynamics of its equilibrium.

## Proof
At an equilibrium, the fourth equation gives \(dx=0\). Since \(d>0\), this forces \(x=0\). Then the second equation gives \(25y=0\), so \(y=0\); the third gives \(-3z=0\), so \(z=0\); and the first gives \(w=0\). Thus the origin is the unique equilibrium.

The Jacobian at the origin is
\[
J_d=
\begin{pmatrix}
-40&40&0&1\\
10&25&0&0\\
0&0&-3&0\\
d&0&0&0
\end{pmatrix}.
\]
Direct expansion of \(\det(\lambda I-J_d)\) gives
\[
\chi_d(\lambda)=(\lambda+3)q_d(\lambda),\qquad
q_d(\lambda)=\lambda^3+15\lambda^2-(1400+d)\lambda+25d.
\]
For \(d>0\),
\[
q_d(-40)=16000+65d>0,\qquad q_d(0)=25d>0,\qquad q_d(25)=-10000<0.
\]
Because the leading term of \(q_d\) is \(\lambda^3\), one has \(q_d(\lambda)\to-\infty\) as \(\lambda\to-\infty\) and \(q_d(\lambda)\to+\infty\) as \(\lambda\to+\infty\). The intermediate value theorem therefore supplies one root in each of the three disjoint intervals
\[
(-\infty,-40),\qquad (0,25),\qquad (25,\infty).
\]
A cubic has exactly three complex roots counted with multiplicity, so these are all its roots. They are real, distinct, and nonzero. The extra factor contributes the distinct negative root \(-3\), since \(q_d(-3)=4308+28d>0\). Hence the origin is hyperbolic with exactly two positive and two negative eigenvalues.

## Verification
The standalone script `verify.py` reconstructs the Jacobian symbolically, factors \(\det(\lambda I-J_d)\), verifies the exact sign evaluations at \(-40\), \(0\), \(25\), and \(-3\), and numerically evaluates the roots at \(d=15\). Running it from the package directory prints `VERIFY_OK`.

The proof itself is exact and does not depend on the numerical root approximations. The numerical values are included only as a check against the source's displayed parameter choice.

## Relationship to prior work
The earliest verified public source is the Research Square preprint posted 23 November 2023, DOI 10.21203/rs.3.rs-3637346/v1. It gives the same four-dimensional system, its Jacobian at the origin, and the printed eigenvalue list \(-40,25,-3,0\). The later Scientific Reports article, DOI 10.1038/s41598-024-71338-x, repeats the same system, Jacobian, and eigenvalue list while varying \(d\) in its numerical dynamical study.

A 2021 paper cited as the antecedent, DOI 10.1155/2021/6771261, studies a three-dimensional fractional-order modified Lorenz system and synchronization; it does not contain the four-dimensional feedback equation \(\dot w=dx\) or the characteristic polynomial proved here. Searches by the exact vector field, title, equilibrium spectrum, and characteristic-polynomial formulation did not locate a prior statement of the factorization or the all-\(d>0\) hyperbolic index-two classification. The closest published semantic matches concern other Lorenz-type or dissipative flows and do not imply this system-specific determinant identity.

## Limitations
This result corrects only the local equilibrium spectrum. It does not validate or invalidate the source's numerical claims about chaos, hyperchaos, periodicity, quasi-periodicity, cryptographic performance, or global boundedness. A hyperbolic equilibrium with a two-dimensional unstable manifold does not by itself prove hyperchaos of any attractor.

The literature comparison is limited by ordinary indexing and retrieval coverage. No claim of exhaustive bibliographic uniqueness is made beyond the inspected source lineage, exact-system searches, and published semantic-index checks described in the review record.

## References
1. X. Cheng, H. Zhu, J. Liu, “A new hyperchaotic system with dynamical analysis and its application in image encryption based on STM32,” Research Square, posted 23 November 2023, DOI 10.21203/rs.3.rs-3637346/v1.
2. X. Cheng, H. Zhu, L. Liu, K. Mao, J. Liu, “Dynamic analysis of a novel hyperchaotic system based on STM32 and application in image encryption,” Scientific Reports 14, 20452 (2024), DOI 10.1038/s41598-024-71338-x.
3. J. Liu, X. Cheng, P. Zhou, “Circuit Implementation Synchronization between Two Modified Fractional-Order Lorenz Chaotic Systems via a Linear Resistor and Fractional-Order Capacitor in Parallel Coupling,” Mathematical Problems in Engineering (2021), DOI 10.1155/2021/6771261.
4. MSC2020 database, class 37C10, “Dynamics induced by flows and semiflows,” American Mathematical Society.
