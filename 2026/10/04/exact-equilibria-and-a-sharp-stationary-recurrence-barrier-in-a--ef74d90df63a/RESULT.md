# Exact equilibria and a sharp stationary recurrence barrier in a four-dimensional hyperchaotic flow
## Finding
Consider the smooth flow
\[
\dot x=ax-yz+w,\qquad
\dot y=xz-by,\qquad
\dot z=xy-cz,\qquad
\dot w=-y+d,
\]
with \(b>0\), \(c>0\), and \(a,d\in\mathbb R\). Its complete equilibrium set and a sharp stationary recurrence law are:

* If \(d=0\), the equilibria form the full line \(\{(\xi,0,0,-a\xi):\xi\in\mathbb R}\).
* If \(d\ne0\), there are exactly two equilibria,
\[
E_\sigma=\left(\sigma\sqrt{bc},\ d,\ \sigma d\sqrt{b/c},\ \sigma\sqrt{bc}\left(\frac{d^2}{c}-a\right)\right),
\qquad \sigma\in\{-1,1\}.
\]
* The involution \(T(x,y,z,w)=(-x,-y,z,-w)\) conjugates the flow with parameter \(d\) to the flow with parameter \(-d\).
* For every compactly supported invariant probability measure \(\mu\) and \(d\ne0\),
\[
\int y\,d\mu=d,
\qquad
c\int z^2\,d\mu=b\int y^2\,d\mu,
\]
and therefore
\[
\int z^2\,d\mu
=\frac{b}{c}\left(d^2+\operatorname{Var}_\mu(y)\right)
\ge \frac{bd^2}{c}.
\]
Equality holds exactly for probability measures supported on the two equilibria. In particular, every non-equilibrium ergodic invariant measure and every nonconstant periodic orbit satisfies the strict inequality.

The introducing article prints a different fourth equilibrium coordinate in its Eq. (4). Direct substitution shows that the printed point has first-component residual \((1-d)s\), where \(s=\sqrt{bd^2/c}\), so it is not an equilibrium except when \(d=1\). The same article also states that the parameters are positive but uses the baseline \(d=-0.1\); the exact conjugacy above shows that changing the sign of \(d\) is dynamically a state reflection, not a new dynamical regime.

## Assumptions and scope
The result is for the vector field exactly as printed in Eq. (1) of the cited article. The only sign assumptions are \(b>0\) and \(c>0\). The parameter \(a\) is arbitrary real. Both signs of \(d\), and the singular case \(d=0\), are treated explicitly.

The invariant-measure statement is restricted to compactly supported invariant Borel probability measures. This guarantees that the polynomial observables used below and their Lie derivatives are integrable and that the stationary generator identities are legitimate. No assertion is made here about existence, uniqueness, ergodicity, or physicality of non-equilibrium invariant measures.

The primary classification is MSC2020 \(37\mathrm{C}10\), dynamics induced by flows and semiflows.

## Proof
At an equilibrium the fourth equation gives \(y=d\). If \(d=0\), the third equation gives \(z=0\), the second equation is then automatic, and the first equation gives \(w=-ax\). This yields exactly the stated line.

Now suppose \(d\ne0\). From the second and third equilibrium equations,
\[
xz=bd,
\qquad
xd=cz.
\]
Eliminating \(z\) gives \(x^2=bc\). Hence \(x=\sigma\sqrt{bc}\), \(z=\sigma d\sqrt{b/c}\), and the first equation uniquely forces
\[
w=-ax+dz
=\sigma\sqrt{bc}\left(\frac{d^2}{c}-a\right).
\]
Thus the two points displayed above are the complete equilibrium set for \(d\ne0\).

For the sign conjugacy, let \(f_d\) denote the vector field at parameter \(d\). Since \(DT=\operatorname{diag}(-1,-1,1,-1)\), direct substitution gives
\[
f_{-d}(Tq)=DT\,f_d(q)
\]
for every state \(q\). Therefore \(T\circ\phi_t^d=\phi_t^{-d}\circ T\) whenever the flows are defined.

Let \(\mu\) be a compactly supported invariant probability measure. Invariance gives \(\int L_f g\,d\mu=0\) for every smooth observable \(g\) used below. Taking \(g=w\) gives
\[
0=\int(-y+d)\,d\mu,
\]
so \(\int y\,d\mu=d\). Taking \(g=y^2-z^2\) gives
\[
L_f(y^2-z^2)
=2y(xz-by)-2z(xy-cz)
=-2by^2+2cz^2,
\]
and hence \(c\int z^2\,d\mu=b\int y^2\,d\mu\). Decomposing the second moment around the mean proves the displayed variance identity and lower bound.

It remains to characterize equality. Equality is equivalent to \(\operatorname{Var}_\mu(y)=0\), so the support of \(\mu\) lies in the closed hyperplane \(y=d\). Invariance of the support then forces every trajectory in the support to stay in that hyperplane. Along such a trajectory, \(\dot y=0\) gives \(xz=bd\), while \(\dot w=0\) makes \(w\) constant. Since \(d\ne0\), neither \(x\) nor \(z\) vanishes. Differentiating \(xz=bd\) and substituting the equations yields
\[
x^4+(a-c)b x^2+bwx-b^2d^2=0.
\]
For fixed \(w\) this is a nonzero quartic polynomial, so its real root set is finite. The continuous function \(x(t)\) must therefore be constant on a connected time interval; then \(z=bd/x\), \(y=d\), and \(w\) are all constant. Every support trajectory is consequently an equilibrium. Conversely, any probability measure supported on the two equilibria is invariant and attains equality.

For a nonconstant periodic orbit, normalized time measure is ergodic only when the orbit is taken with its natural cyclic measure, but the equality characterization alone is enough: equality would force the orbit to consist of equilibria, a contradiction. Thus every nonconstant periodic orbit satisfies the strict bound.

## Verification
The accompanying `verify.py` performs exact symbolic checks of the two equilibrium formulas, the \(d=0\) equilibrium line, the sign conjugacy, the Lie-derivative identities, the quartic used in the equality case, and the residual of the equilibrium coordinate printed in the source. It also evaluates the source's baseline parameters \(a=8\), \(b=40\), \(c=15\), \(d=-0.1\).

At that baseline, the corrected equilibrium corresponding to the source's positive \(z\)-branch is approximately
\[
(-24.4948974278,\ -0.1,\ 0.1632993162,\ 195.9428494910),
\]
whereas the source's printed fourth coordinate is approximately \(196.1224787388\). Substitution of the printed point leaves first-component residual approximately \(0.1796292478\), while the corrected point has zero residual symbolically.

## Relationship to prior work
Benkouider et al. introduce this exact vector field, state that it has two equilibria for their nonzero parameter choice, and print the coordinates in Eq. (4). Their printed fourth coordinate is inconsistent with their own first differential equation except at \(d=1\), and their equilibrium discussion does not treat \(d=0\). The source's Jacobian is independent of \(w\), so correcting the fourth coordinate does not by itself invalidate numerical eigenvalues evaluated at the same \((x,y,z)\).

The literature on variable/offset boosting, including Li and Sprott's 2016 work, already explains coordinate-offset mechanisms in chaotic flows. The present claim does not treat generic offset boosting as new. Its new mathematical content is the complete equilibrium classification for this specific flow, the exact \(d\leftrightarrow-d\) state-reflection conjugacy, and the sharp invariant-measure second-moment barrier with its equality classification.

Searches of the introducing article, its open-access mirror, exact equation strings, the corrected equilibrium formula, the DOI combined with correction/erratum terms, and a semantic index of published mathematical findings did not locate a statement implying these results. The closest indexed stationary-balance results concern different vector fields and do not specialize to this system.

## Limitations
The stationary law constrains compact recurrent statistics but does not prove that a chaotic or hyperchaotic invariant measure exists for any parameter choice. It does not certify the numerical Lyapunov spectra, attractor diagrams, encryption performance, or global boundedness claims in the source article. The originality search cannot exclude unindexed notes or later analyses that were not discoverable under the tested aliases and equations.

The sign conjugacy is a smooth state reflection and is structurally elementary once noticed; its value here is in resolving the source's sign convention and reducing the parameter-sign analysis. The stronger contribution is the exact equilibrium correction together with the sharp stationary second-moment identity and equality case.

## References
1. K. Benkouider, A. Sambas, T. Bonny, W. Al Nassan, I. A. R. Moghrabi, I. M. Sulaiman, B. A. Hassan, and M. Mamat, “A comprehensive study of the novel 4D hyperchaotic system with self-exited multistability and application in the voice encryption,” *Scientific Reports* 14, 12993 (2024), DOI: 10.1038/s41598-024-63779-1. Published 2024-06-06.
2. C. Li and J. C. Sprott, “Variable-boostable chaotic flows,” *Optik* 127 (2016), 10389–10398, DOI: 10.1016/j.ijleo.2016.08.046.
3. MSC2020, \(37\mathrm{C}10\): Dynamics induced by flows and semiflows.
