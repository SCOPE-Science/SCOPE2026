# An omitted hyperbolic equilibrium in a sine–cubic chaotic flow
## Finding
For the three-dimensional flow introduced by Zolfaghari-Nejad, Charmi, and Hassanpoor,
\[
\dot x=-p_1x^3+p_2y^3+p_3xz^2,\qquad
\dot y=p_4\sin(xy-z)-p_5x^3,\qquad
\dot z=p_6\sin(xyz)+p_7\sin x,
\]
set
\[
(p_1,p_2,p_3,p_4,p_5,p_6,p_7)=(3.964,7,7,5,4.5,2.9,1),
\]
which is the parameter vector used in the introducing paper to display a chaotic trajectory. There exists an equilibrium in
\[
B=[1.002723,1.004723]\times[0.746237,0.748237]\times[-0.394482,-0.392482].
\]
Every equilibrium in this box is hyperbolic with exactly one eigenvalue of positive real part and two eigenvalues of negative real part. Hence at least one equilibrium lies off the reported family \( (0,0,k\pi) \), and the system at the displayed chaotic parameter set does not have only nonhyperbolic equilibria.

## Assumptions and scope
The vector field and parameters are exactly those printed in the source. The claim concerns existence and linear type of at least one equilibrium in the single box \(B\). It does not claim uniqueness in \(B\), does not enumerate all equilibria, and does not infer whether the paper's plotted chaotic set is hidden or self-excited.

The primary MSC2020 classification is \(37C25\), fixed points and local dynamics of smooth dynamical systems. The system is a smooth autonomous flow, and the finding is specifically an equilibrium-existence and equilibrium-type statement.

## Proof
Let \(F=(F_1,F_2,F_3)\) denote the displayed vector field and let
\[
A=10^-6
\begin{pmatrix}
10175&-90707&-63282\\
126889&-119762&217899\\
68180&-75210&586802
\end{pmatrix}.
\]
Its determinant is the nonzero rational number
\[
\det A=\frac{1236309158097179}{250000000000000000}.
\]
Thus \(G=AF\) has exactly the same zeros as \(F\).

On each pair of opposite faces of \(B\), the packaged verifier subdivides the two free coordinates into a \(10\times10\) grid and evaluates \(G\) by rational interval arithmetic. Sine and cosine are enclosed by alternating Taylor bounds; all trigonometric arguments lie in \([-6/5,6/5]\), where the required monotonicity is elementary. The worst certified face bounds are
\[
\begin{aligned}
G_1&\le -9.2196760649\times10^-4 &&\text{on the lower \(x\)-face},\\
G_1&\ge  9.2540098815\times10^-4 &&\text{on the upper \(x\)-face},\\
G_2&\le -4.7820581636\times10^-4 &&\text{on the lower \(y\)-face},\\
G_2&\ge  4.8476736849\times10^-4 &&\text{on the upper \(y\)-face},\\
G_3&\le -5.5399824283\times10^-4 &&\text{on the lower \(z\)-face},\\
G_3&\ge  5.5879562791\times10^-4 &&\text{on the upper \(z\)-face}.
\end{aligned}
\]
The Poincaré–Miranda theorem therefore gives a zero of \(G\), hence a zero of \(F\), in \(B\).

For the Jacobian \(J=DF\), write its characteristic polynomial as
\[
\det(\lambda I-J)=\lambda^3+a_1\lambda^2+a_2\lambda+a_3.
\]
A single rational-interval evaluation on all of \(B\) gives
\[
6.68634227576<a_1<6.78591554336,
\]
\[
95.2302893036<a_2<97.7690775639,
\]
and
\[
-206.560786859<a_3<-197.871424412.
\]
Hence at the certified equilibrium \(a_1>0\), \(a_2>0\), and \(a_3<0\). Descartes' rule of signs gives exactly one positive real root. The remaining two roots have positive product and negative sum; if real they are both negative, while if conjugate their common real part is negative. None is on the imaginary axis. The equilibrium is therefore hyperbolic with one unstable and two stable directions.

## Verification
Run `python verify_equilibrium.py`. The script uses only the Python standard library and exact rational arithmetic for interval endpoints. It verifies the rational preconditioner determinant, covers all six faces by \(600\) interval cells, checks the strict Poincaré–Miranda sign conditions, and verifies the coefficient-sign enclosure on the whole box. A successful run prints `VERIFY_OK` together with the certified worst face bounds and coefficient intervals.

The finite computation is exhaustive for the stated face subdivision and interval formulas; it is not being used as a search for an equilibrium. Existence follows from the topological theorem once the certified signs are established.

## Relationship to prior work
The introducing paper states that solving its equilibrium equations gives \(x_*=y_*=0\) and \(z_*=k\pi\), then concludes that its equilibria are nonhyperbolic and located on the \(z\)-axis. The source's Table 1 and conclusion make the “only nonhyperbolic equilibrium points” property part of the stated novelty of the system. The certified box above is disjoint from that axis and contains a hyperbolic equilibrium, so it directly falsifies the completeness of that equilibrium classification for the paper's own displayed chaotic parameter vector.

Searches by exact title, DOI, equation terms, “additional equilibria,” and “hyperbolic equilibrium” found the introducing article and general literature on other nonhyperbolic chaotic systems, but no located source stating or implying this certified off-axis equilibrium. The closest retrieved records concern different vector fields and do not cover the present statement.

## Limitations
Only one omitted equilibrium is proved to exist. The result does not count all equilibria, does not prove that the certified equilibrium is unique inside \(B\), and does not revisit the paper's numerical bifurcation, entropy, encryption, or multistability calculations. It also does not classify any chaotic attractor as hidden or self-excited, because that requires basin information relative to the complete equilibrium set.

The originality search cannot exclude an unindexed correction, erratum, or later analysis not returned by the searched databases. No such covering source was found in the inspected material.

## References
1. M. Zolfaghari-Nejad, M. Charmi, and H. Hassanpoor, “A New Chaotic System with Only Nonhyperbolic Equilibrium Points: Dynamics and Its Engineering Application,” *Complexity* 2022, Article 4488971, first published 12 January 2022, DOI: 10.1155/2022/4488971.
2. MSC2020, \(37C25\): fixed points and periodic points of dynamical systems; fixed-point index theory; local dynamics.
