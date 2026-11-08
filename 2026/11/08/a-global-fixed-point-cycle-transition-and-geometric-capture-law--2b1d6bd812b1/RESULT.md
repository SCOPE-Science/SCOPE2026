# A global fixed-point–cycle transition and geometric capture law in a trace-free border-collision map

## Finding
For each \(d>0\), consider the continuous piecewise-affine planar map
\[
F_d(x,y)=\begin{cases}(1+y,0),&x\le0,\\(1+y,-dx),&x>0.\end{cases}
\]
Its global periodic and attracting dynamics have three sharply different regimes at the natural unit-determinant threshold \(d=1\).

For \(0<d<1\), every point in \(\mathbb R^2\) approaches the unique fixed point \(E_d=(u_d,-du_d)\), where \(u_d=1/(1+d)\), and there are no other periodic orbits.

For \(d=1\), every planar orbit enters the square \(Q=[0,1]\times[-1,0]\) after finitely many iterations. The square is invariant and \(F_1^2(x,y)=(1-x,-1-y)\) for every \((x,y)\in Q\). All of \(Q\setminus\{(1/2,-1/2)\}\) consists of primitive period-four points, while its center is fixed.

For \(d>1\), there are precisely three periodic orbits: the repelling fixed point \(E_d\), the attracting primitive four-cycle
\[
C_d:\quad(1,0)\mapsto(1,-d)\mapsto(1-d,-d)\mapsto(1-d,0)\mapsto(1,0),
\]
and the saddle primitive four-cycle
\[
P_d:\quad (u_d,0)\mapsto(1,-du_d)\mapsto(u_d,-d)\mapsto(1-d,-du_d)\mapsto(u_d,0).
\]
At the points of \(P_d\), the four-step multipliers are \(0\) and \(d^2\), whereas the derivative of the four-step return at \(C_d\) is nilpotent (both multipliers zero). The set of initial states not captured by \(C_d\) in finitely many steps consists of \(E_d\) together with backward preimages of \(P_d\). It is a subset of a countable union of affine lines and therefore has planar Lebesgue measure zero.

Moreover, define the open section interval and its repelling center by
\[
I_d=\left(\frac{d-1}{d^2},\frac1d\right),\qquad u_d=\frac1{1+d}.
\]
For every \(u\in I_d\), the four-step section map is \(R_d(u)=1-d+d^2u\). The initial values that complete at least \(n\) four-step returns within \(I_d\) form precisely
\[
I_{d,n}=u_d+d^{-2n}(I_d-u_d),\qquad |I_{d,n}|=d^{-2n-2},\qquad n\ge0.
\]
For Lebesgue-uniform initial \(u\) conditioned on \(I_d\), the number \(K\ge1\) of four-step returns until first exit obeys
\[
\Pr(K>n)=d^{-2n},\qquad\Pr(K=k)=(1-d^{-2})d^{-2(k-1)},\qquad\mathbb E K=\frac{d^2}{d^2-1}.
\]
Thus the mean near-saddle residence time diverges as \(1/[2(d-1)]\) when \(d\downarrow1\), even though outside the null exceptional set all supercritical trajectories are eventually captured by \(C_d\).

## Assumptions and scope
The map is the specialization \(\mu=1\), \(\delta_L=0\), \(\tau_L=\tau_R=0\), \(\delta_R=d\) of the continuous planar border-collision normal form. The parameter \(d\) varies over all positive real numbers; the switching convention at \(x=0\) is immaterial because the branch formulas agree there. Period means *least positive period* under \(F_d\). Convergence is in the Euclidean topology. Lebesgue probabilities are one-dimensional and conditional on the indicated open section interval, not probabilities under an invariant measure of the planar map. The event \(K>n\) means that \(R_d^j(u)\in I_d\) for every \(0\le j\le n\); in particular \(K\ge1\) almost surely.

## Proof
**Step 1: Right-branch dynamics.** Write \(F_R(x,y)=(1+y,-dx)\) and \(F_L(x,y)=(1+y,0)\). The unique right-branch fixed point is \(E_d=(u_d,-du_d)\) and
\[
F_R^2(z)-E_d=-d(z-E_d),\qquad z\in\mathbb R^2.
\]
For \(d>1\), any nonfixed point whose entire future follows the right branch must eventually have a nonpositive first coordinate: otherwise both even and odd subsequences of first coordinates remain positive despite alternating, expanding deviations \((-d)^n\) from \(u_d>0\), which is impossible. For \(0<d<1\), every infinite right-only orbit converges to \(E_d\). For \(d=1\), a right-only orbit lies in \(Q\), since positivity of its first four right-branch coordinates forces \(0<x<1\) and \(-1<y<0\).

**Step 2: Every left hit becomes a one-dimensional problem.** On entering \(x\le0\), the next iterate lies on the section \(\Sigma=\{(u,0):u\in\mathbb R\}\). If \(u\le0\), then \(F_d(u,0)=(1,0)\). If \(u>0\), its first two iterates are
\[
(u,0)\mapsto (1,-du)\mapsto(1-du,-d).
\]
When \(u\ge1/d\), its next two iterates reach \((1-d,0)\) and \((1,0)\) if \(d>1\). If \(0<u<1/d\), the next two iterates are
\[
(1-d,-d(1-du))\mapsto (1-d+d^2u,0).
\]
For \(d>1\), this four-step return stays in \((0,1)\) exactly when \(u\in I_d=((d-1)/d^2,1/d)\); at or below its lower endpoint it next reaches \((1,0)\), and at or above the upper endpoint it also reaches \((1,0)\) within boundedly many steps. On \(I_d\), the four-step map \(R_d(u)=1-d+d^2u\) has unique fixed point \(u_d\), satisfying \((d-1)/d^2<u_d<1/d\). Because \(R_d(u)-u_d=d^2(u-u_d)\), for \(u\ne u_d\) repeated returns leave the bounded interval \(I_d\) after finitely many steps. At \(u=u_d\) they trace the displayed saddle four-cycle. Thus every nonfixed planar orbit which reaches the left half-plane is eventually on either \(C_d\) or \(P_d\), and the only orbit confined to the right half-plane for \(d>1\) is \(E_d\). Periodic points must belong to those three cycles.

**Step 3: Stability and negligible exceptional set.** Along the strict four-cycle \(P_d\), the section derivative of \(F_d^4\) is \(d^2\); an intermediate left step has rank one, so the second multiplier is zero. Near \(C_d\), two successive left steps make \(F_d^4\) locally constant, so its multipliers both vanish. Right-branch multipliers at \(E_d\) have modulus \(\sqrt d>1\). The special section point \(u_d\) has only countably many finite-time preimages under the finitely many affine branch words. Each admissible nondegenerate preimage of its section condition is contained in an affine line because right-branch matrices are invertible and left-branch matrices have rank one. There cannot be an open preimage of \(P_d\): the constant value after consecutive left steps is \((1,0)\in C_d\), not in \(P_d\). Hence the exceptional basin is planar Lebesgue null.

**Step 4: The subcritical and critical regimes.** For \(0<d<1\), the rectangle \(B_d=(0,1]\times[-d,0]\) is invariant under \(F_R\), and the right-branch double-iterate contracts by \(d\). A left hit sends the orbit to the section; from any section point it enters \(B_d\) within at most four further steps (use the displayed two-step formula and \(1-d>0\)). An orbit with no left hit converges to \(E_d\). Therefore every orbit converges to \(E_d\), excluding any other periodic orbit. When \(d=1\), the same section calculation shows every left-hit orbit enters \(Q\) in finitely many steps, and right-only orbits are already in \(Q\). Directly on \(Q\), \(F_1^2(x,y)=(1-x,-1-y)\) including at switching boundaries. Its unique fixed point is \((1/2,-1/2)\), also fixed by \(F_1\). Every other point has least period four.

**Step 5: Exact residence law.** For \(d>1\), the points of \(I_d\) surviving \(n\) four-step returns are \(R_d^{-n}(I_d)\). As \(R_d\) has fixed point \(u_d\) and slope \(d^2\), the interval is exactly \(I_{d,n}=u_d+d^{-2n}(I_d-u_d)\). Because \(|I_d|=d^{-2}\), the length is \(d^{-2n-2}\). Dividing by \(|I_d|\) yields \(\Pr(K>n)=d^{-2n}\), the geometric distribution and its expectation. Finally \(d^2/(d^2-1)\sim1/[2(d-1)]\) as \(d\downarrow1\). This is a probability law on section starting points, not a statement that a randomly selected planar trajectory samples this section uniformly.

## Verification
The bundled standalone `verify.py` uses Python rational arithmetic to check branch formulas, both primitive four-cycles, the section-return identity, the length of the nested survivor intervals, invariant-rectangle entry, and critical-square involution on multiple exact test inputs. Run `python3 verify.py`. It is a supplementary finite check; Steps 1–5 supply the proof for every real \(d>0\), not just the sampled rational parameters.

## Relationship to prior work
Simpson's 2024 preprint [1] introduces and studies the same zero-determinant normal form, including the right fixed point and local stability (its Proposition 4.1), periodicity regions, and numerical bifurcation structures. Its cited earlier polygon literature [3] addresses geometric mode locking. Simpson's 2026 first-return paper [2] establishes general return-time partitions and the induced one-dimensional map when \(d>1\) and the right fixed point is a repelling focus; specializing that return-map framework can recover portions of the section-branch algebra here. Neither inspected primary article presents the exact global three-regime classification including the entire neutral square at \(d=1\), only three periodic orbits for every \(d>1\), finite-time full-measure capture, and the sharp geometric residence-time distribution in this trace-free family as a single result. The pre-existing return-map theorem is credited rather than represented as new.

## Limitations
This is a trace-free one-parameter specialization, not a classification for arbitrary traces or determinants. The geometric waiting-time distribution assumes uniform initial section coordinates on \(I_d\). No claim is made about a physical distribution of initial conditions, structural persistence of the continuum at nonzero traces, nor external independent validation. Formulae for complicated parameters in the full normal form may exhibit other attractors. The closest 2026 source develops more general return-map formulas, so a prior derivation of some individual ingredients is an overlap risk even though the combined global phase-and-capture theorem was not located.

## References
[1] D. J. W. Simpson, *The two-dimensional border-collision normal form with a zero determinant*, arXiv:2408.04790 (first public August 8, 2024), later SIAM J. Applied Dynamical Systems, DOI 10.1137/24M1683548. https://arxiv.org/abs/2408.04790

[2] D. J. W. Simpson, *One-dimensional first return maps for the two-dimensional border-collision normal form with a zero determinant*, arXiv:2606.08901 (2026), DOI 10.1007/s12346-026-01576-z. https://link.springer.com/article/10.1007/s12346-026-01576-z

[3] R. Szalai and H. M. Osinga, *Arnol'd tongues arising from a grazing-sliding bifurcation*, SIAM J. Applied Dynamical Systems 8 (2009), 1434–1461, DOI 10.1137/080726679.
