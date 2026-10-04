# A positive memory half-space and exact stationary transfer law for a six-dimensional memristor flow
## Finding
For the six-dimensional flow
\[
\dot x=-ax+yz+bw+\cos u,\qquad
\dot y=cy\tanh v-xz+k,
\]
\[
\dot z=xy-dz,\qquad
\dot w=xz-ew,\qquad
\dot u=gy,\qquad
\dot v=y^2-v,
\]
assume \(c>0\), \(d>0\), \(g\ne0\), and \(k\ne0\). Every nonempty compact invariant set \(K\) satisfies
\[
\min_K v>0.
\]
Thus the memory coordinate of every compact recurrent regime is separated from the hyperplane \(v=0\).

Every compactly supported invariant Borel probability measure \(\mu\) of the flow satisfies
\[
\langle y\rangle=0,\qquad
\langle v\rangle=\langle y^2\rangle,\qquad
\langle v^2\rangle=\langle vy^2\rangle,
\]
and
\[
0<d\langle z^2\rangle
=c\langle y^2\tanh v\rangle
<c\langle v^2\rangle.
\]
Here \(\langle f\rangle=\int f\,d\mu\).

At the parameter values used for the hidden-attractor computations in the source, \(c=7\), \(d=31\), \(g=1/20\), and \(k=7\), every compact invariant statistical state obeys
\[
0<31\langle z^2\rangle
=7\langle y^2\tanh v\rangle
<7\langle v^2\rangle.
\]

## Assumptions and scope
The statement concerns the classical autonomous ODE printed as system (3) in Guo, Wen, and Mou. The parameters \(a\), \(b\), and \(e\) are unrestricted by the proof; the assumptions \(c>0\), \(d>0\), \(g\ne0\), and \(k\ne0\) are the ones used for the strict positivity conclusion. The invariant measure is assumed to have compact support. No assertion is made for unbounded trajectories, transient numerical segments, or discrete-time DSP approximations.

## Proof
Let a trajectory be complete and bounded. Solving the scalar memory equation backwards gives, for every \(t\),
\[
v(t)=\int_{-\infty}^{t}e^{-(t-s)}y(s)^2\,ds.
\]
The omitted homogeneous term vanishes because the trajectory is bounded as \(s\to-\infty\). Hence \(v(t)\ge0\).

Suppose \(v(t_0)=0\). The nonnegative integral then forces \(y(s)=0\) for every \(s\le t_0\). On that half-line, \(\dot z=-dz\). Since \(d>0\) and the trajectory is bounded backwards, necessarily \(z(s)=0\) for every \(s\le t_0\). The second equation then gives \(\dot y=k\), contradicting \(y(s)=0\) because \(k\ne0\). Thus every bounded complete trajectory has \(v(t)>0\) for all \(t\). A compact invariant set consists of bounded complete trajectories, so continuity and compactness give \(\min_K v>0\).

For an invariant probability measure, the integral of the generator applied to a smooth observable is zero. Applying this to \(u\), \(v\), and \(v^2/2\) yields
\[
g\langle y\rangle=0,
\]
\[
\langle y^2\rangle-\langle v\rangle=0,
\]
and
\[
\langle vy^2\rangle-\langle v^2\rangle=0.
\]
Because \(g\ne0\), the first identity gives \(\langle y\rangle=0\).

Applying the generator to \(y^2/2\) gives
\[
0=c\langle y^2\tanh v\rangle-\langle xyz\rangle+k\langle y\rangle,
\]
while applying it to \(z^2/2\) gives
\[
0=\langle xyz\rangle-d\langle z^2\rangle.
\]
Using \(\langle y\rangle=0\) proves
\[
d\langle z^2\rangle=c\langle y^2\tanh v\rangle.
\]
The support lies in \(v>0\). If \(\langle y^2\rangle=0\), then \(\langle v\rangle=0\), contradicting positivity of \(v\) on the compact support. Hence \(y\ne0\) on a set of positive measure, so \(\langle y^2\tanh v\rangle>0\). Finally, \(0<\tanh v<v\) for \(v>0\), and therefore
\[
\langle y^2\tanh v\rangle<\langle vy^2\rangle=\langle v^2\rangle.
\]
Multiplication by \(c>0\) gives the strict chain.

## Verification
The bundled symbolic checker verifies the two generator identities whose stationary averages produce the transfer law, verifies the memory moment identity, and checks the published numerical substitution \(c=7\), \(d=31\), \(g=1/20\), \(k=7\). The positivity argument is analytic and depends on backward boundedness, \(d>0\), and \(k\ne0\), not on finite numerical integration.

## Relationship to prior work
Guo, Wen, and Mou introduce this exact six-dimensional system, establish the absence of equilibria when \(k\ne0\), and study hidden attractors, bifurcation diagrams, Lyapunov exponents, chaos degradation, offset boosting, and DSP realization. Their analysis does not state the positive-memory half-space theorem or the invariant-measure transfer law above. Searches for the exact model, the memory equation \(\dot v=y^2-v\), stationary balance formulations, and positive-half-space formulations did not locate a published statement implying this result. Nearby memristive-chaos papers use different memory equations and do not yield this source-specific identity.

## Limitations
The theorem does not prove that a compact attractor exists for a given parameter vector, does not establish chaos or hyperchaos, and does not quantify the distance \(\min_K v\) from \(v=0\) without additional information about the particular invariant set. It also does not apply directly to transient trajectories that are not complete and bounded, nor to a numerical discretization viewed as a different dynamical system.

## References
1. Z. Guo, J. Wen, and J. Mou, “Dynamic Analysis and DSP Implementation of Memristor Chaotic Systems with Multiple Forms of Hidden Attractors,” *Mathematics* 11 (2023), 24. DOI: 10.3390/math11010024. Published 21 December 2022.
2. Primary full text: https://www.mdpi.com/2227-7390/11/1/24
