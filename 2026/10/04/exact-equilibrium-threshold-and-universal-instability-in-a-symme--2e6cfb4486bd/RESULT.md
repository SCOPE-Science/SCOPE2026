# Exact equilibrium threshold and universal instability in a symmetric cubic chaotic flow
## Finding
Consider the three-dimensional autonomous flow
\[
\dot x=y-2xz,\qquad
\dot y=-x+\frac12(1-x^2)y-\frac12yz,\qquad
\dot z=\frac1{10}xy+\nu x^2-\frac45,
\]
with real parameter \(\nu\). Its equilibrium geometry is completely determined by the sign of \(\nu\):

* If \(\nu\le0\), the flow has no equilibrium.
* If \(\nu>0\), there is a unique \(t>0\) satisfying
\[
\nu=\frac{t(t^2+t+5)}{5(t^2+t+1)},
\]
and exactly two equilibria,
\[
E_\pm=\left(\pm\sqrt{1+t+t^{-1}},\ \mp2t\sqrt{1+t+t^{-1}},\ -t\right).
\]
The map \((x,y,z)\mapsto(-x,-y,z)\) exchanges the two equilibria.

Every one of these equilibria is hyperbolic and has unstable dimension two. At either member of the pair the characteristic polynomial is
\[
\chi_t(\lambda)=\lambda^3+a_1(t)\lambda^2+a_2(t)\lambda+a_3(t),
\]
where
\[
a_1(t)=\frac{1-4t^2}{2t},\qquad
a_2(t)=\frac{15-17t-17t^2}{10},\qquad
a_3(t)=\frac{2(t^4+2t^3-t^2+2t+5)}{5t}.
\]
It has exactly two roots with positive real part and one with negative real part for every \(t>0\).

The introducing article gives the necessary equilibrium relations
\[
\widehat y=\frac8{\widehat x}-10\nu\widehat x,\qquad
\widehat z=\frac4{\widehat x^2}-5\nu,
\]
but then treats \(\widehat x\) as though those two relations completed the equilibrium equations. They do not: substituting them into the remaining stationarity equation imposes an additional scalar constraint. Consequently the stable-node equilibrium branch reported for \(\nu\in[-2,2]\) is not a branch of equilibria of the printed vector field. For the positive parameter range used for the article's periodic and chaotic examples, the actual equilibria are always index-two unstable.

## Assumptions and scope
The claim concerns the vector field exactly as printed in Eq. (3) of Qiu, Xu, Jiang, Sun, and Cao. The parameter \(\nu\) is allowed to be any real number. No boundedness, existence of periodic or chaotic attractors, or validity of the source's numerical Lyapunov spectra is assumed.

The statement about unstable dimension is a local linear statement at the exact equilibria. It does not by itself prove that any particular observed attractor is self-excited, nor does it classify global basins.

The primary classification is MSC2020 \(37\mathrm{C}10\), dynamics induced by flows and semiflows.

## Proof
At an equilibrium, the third equation rules out \(x=0\), because then it would equal \(-4/5\). The first equation gives
\[
y=2xz.
\]
Substituting this into the second equation and dividing by the nonzero \(x\) yields
\[
z(1-x^2-z)=1.
\]
In particular \(z\ne0\), and solving for \(x^2\) gives
\[
x^2=1-z-\frac1z.
\]
If \(z>0\), then \(z+z^{-1}\ge2\), so the right-hand side is negative. Hence every equilibrium must have \(z<0\). Write \(t=-z>0\). Then
\[
x^2=1+t+\frac1t.
\]
The third equilibrium equation, after using \(y=2xz\), becomes
\[
x^2\left(\nu+\frac z5\right)=\frac45.
\]
Therefore
\[
\nu=\frac4{5x^2}-\frac z5
=\frac{t(t^2+t+5)}{5(t^2+t+1)}.
\]
This is strictly positive, proving nonexistence for \(\nu\le0\).

Define
\[
\Phi(t)=\frac{t(t^2+t+5)}{5(t^2+t+1)}.
\]
Its derivative is
\[
\Phi'(t)=\frac{P(t)}{5(t^2+t+1)^2},\qquad
P(t)=t^4+2t^3-t^2+2t+5.
\]
For \(0<t<1\), \(P(t)>5-t^2>4\). For \(t\ge1\), \(t^4-t^2\ge0\) and the remaining terms are positive. Thus \(P(t)>0\) for every \(t>0\). Since \(\Phi(t)\to0\) as \(t\downarrow0\) and \(\Phi(t)\to\infty\) as \(t\to\infty\), \(\Phi\) is a bijection from \((0,\infty)\) onto \((0,\infty)\). Hence each \(\nu>0\) determines exactly one \(t>0\), and the two signs of \(x\) give exactly the displayed symmetry pair.

The Jacobians at the two points are similar under the symmetry \((x,y,z)\mapsto(-x,-y,z)\), so they have the same characteristic polynomial. Direct substitution gives the polynomial \(\chi_t\) displayed above. Its constant coefficient is positive because \(P(t)>0\), so zero is never an eigenvalue.

For \(0<t<1/2\), one has \(a_1(t)>0\), \(a_2(t)>0\), and \(a_3(t)>0\). Moreover
\[
a_1(t)a_2(t)-a_3(t)
=\frac{N(t)}{20t},
\]
where
\[
N(t)=60t^4+52t^3-69t^2-33t-25.
\]
On \(0<t<1/2\),
\[
60t^4+52t^3<\frac{60}{16}+\frac{52}8=\frac{41}4<25,
\]
so \(N(t)<0\). The cubic Routh array therefore has first-column signs \(+,+,-,+\), giving exactly two roots in the open right half-plane.

It remains to show that this root count cannot change as \(t\) varies. Suppose \(\lambda=i\omega\), with real \(\omega\ne0\), were a root. Separating real and imaginary parts gives
\[
\omega^2=a_2(t),\qquad a_3(t)=a_1(t)\omega^2.
\]
If \(t\ge1/2\), then \(a_1(t)\le0\) while \(a_3(t)>0\), impossible. If \(0<t<1/2\), the two equations would imply \(a_1a_2-a_3=0\), contradicting \(N(t)<0\). Thus no eigenvalue ever reaches the imaginary axis. Since the coefficients depend continuously on \(t>0\), the number of roots in each open half-plane is constant on the connected interval \((0,\infty)\). It is therefore two unstable and one stable root for every \(t>0\), and all equilibria are hyperbolic.

## Verification
The bundled `verify.py` reconstructs the equilibrium parametrization with exact rational arithmetic, differentiates \(\Phi\), derives the Jacobian characteristic polynomial symbolically, verifies the Routh determinant identity, and checks that the source's displayed two-equation equilibrium formula leaves a nonzero unresolved stationarity condition. It also numerically replays the local spectrum at \(\nu=0.21\), one of the source's displayed chaotic parameter values, obtaining two positive-real-part eigenvalues and one negative-real-part eigenvalue.

A successful replay prints `VERIFY_OK`. The numerical replay is illustrative only; the proof of existence, uniqueness, hyperbolicity, and unstable dimension is analytic for all real \(\nu\).

## Relationship to prior work
Qiu et al. introduce the vector field, state that it has multiple equilibria, derive the two displayed relations for \(\widehat y\) and \(\widehat z\), and report a numerical equilibrium/stability plot over \(\nu\in[-2,2]\) containing both unstable saddle-focus and stable-node branches. The same paper later uses positive values such as \(\nu=0.147\), \(0.156\), \(0.21\), \(0.26\), and \(0.3\) in its dynamical examples.

The present result supplies the omitted scalar stationarity condition and resolves the equilibrium set exactly. Searches by exact equation strings, title/DOI, equilibrium aliases, stability language, and semantic similarity found no prior source giving the sign threshold \(\nu>0\), the one-parameter exact parametrization above, or the all-parameter unstable-dimension-two theorem for this specific flow. The closest indexed findings concern equilibrium corrections or exact stability statements for other vector fields and do not imply this result.

## Limitations
This result does not re-evaluate the source's global bifurcation diagrams, periodic-orbit labels, basin plots, circuit implementation, synchronization controller, or numerical Lyapunov exponents. It only corrects and completes the equilibrium geometry and its linear stability for the printed continuous-time model.

The literature search covered the open-access article, its PubMed/PMC record, direct title/equation searches, and a semantic database of published findings. Unindexed or inaccessible prior observations remain a residual originality risk.

## References
1. H. Qiu, X. Xu, Z. Jiang, K. Sun, and C. Cao, “Dynamical behaviors, circuit design, and synchronization of a novel symmetric chaotic system with coexisting attractors,” *Scientific Reports* 13, 1893 (2023), DOI 10.1038/s41598-023-28509-z.
2. PubMed PMID 36732538 and PubMed Central PMCID PMC9895447, open-access bibliographic and full-text records for the same article.
