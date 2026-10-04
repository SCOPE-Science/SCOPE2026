# Exact recurrence shell in the Wang–Dong–Li variable-boostable flow
## Finding
Consider the three-dimensional flow
\[
\dot x=a(y-x),\qquad \dot y=-cy-xz,\qquad \dot z=y^2-b+kxy,
\]
with \(a,b,c,k>0\). Define
\[
H(x,z)=-z+\frac{k+2}{2a}x^2.
\]
Along every classical solution,
\[
\dot H=b-(k+1)x^2-\frac{\dot x^2}{a^2}.
\]
Therefore every compactly supported invariant probability measure \(\mu\) satisfies the exact recurrence shell
\[
(k+1)\int x^2\,d\mu+\frac{1}{a^2}\int \dot x^2\,d\mu=b.
\]
In particular,
\[
\int x^2\,d\mu\leq \frac{b}{k+1}.
\]
Equality holds exactly for invariant measures supported on the two equilibria
\[
E_\pm=\left(\pm\sqrt{\frac{b}{k+1}},\pm\sqrt{\frac{b}{k+1}},-c\right).
\]
Hence every non-equilibrium ergodic compact invariant measure, and every nonconstant periodic orbit, obeys the strict bound \(\int x^2\,d\mu<b/(k+1)\).

For the parameters used for the hidden chaotic attractor in Wang, Dong, and Li, \(a=12\), \(b=100\), \(c=10\), and \(k=23/5\), this specializes to
\[
\langle x^2\rangle+\frac{5}{4032}\langle \dot x^2\rangle=\frac{125}{7}.
\]
Thus the equilibrium RMS amplitude \(\sqrt{125/7}\) is a sharp ceiling for \(x\) in every compact recurrent statistical state, with a strictly smaller RMS for every non-equilibrium ergodic state.

## Assumptions and scope
The statement concerns the autonomous flow printed in Wang, Dong, and Li (2022), with positive parameters as in that article. The invariant-measure statement is for compactly supported invariant Borel probability measures. Periodic-orbit averages are included by taking normalized arclength in time along the orbit. The result is an RMS/time-average constraint; it is not a pointwise bound on \(x(t)\), and it does not assert existence or uniqueness of any chaotic attractor.

## Proof
Differentiate \(H\) and substitute the vector field:
\[
\begin{{aligned}}
\dot H
&=-\dot z+\frac{k+2}{a}x\dot x\\
&=-(y^2-b+kxy)+(k+2)x(y-x)\\
&=b-y^2+2xy-(k+2)x^2\\
&=b-(k+1)x^2-(y-x)^2.
\end{{aligned}}
\]
Since \(\dot x=a(y-x)\), this is exactly
\[
\dot H=b-(k+1)x^2-\frac{\dot x^2}{a^2}.
\]
If \(\mu\) is compactly supported and invariant, then \(H\) is bounded on its support and \(\int L H\,d\mu=0\), where \(L\) is the flow generator. Integrating the pointwise identity gives the recurrence shell.

The shell implies \(\int x^2\,d\mu\leq b/(k+1)\). If equality holds, then \(\int \dot x^2\,d\mu=0\), so \(\dot x=0\) on the support of \(\mu\). Hence \(y=x\) there. Invariance of the support forces \(\dot y=0\) and \(\dot z=0\) along supported trajectories. The possibility \(x=y=0\) is incompatible with compact invariance because then \(\dot z=-b\neq0\). Therefore \(x\neq0\), \(z=-c\), and \((k+1)x^2=b\), giving precisely \(E_+\) and \(E_-\). Conversely, any convex combination of the two equilibrium point masses is invariant and attains equality. This proves the equality characterization and the strict inequality for every non-equilibrium ergodic invariant measure.

For a nonconstant periodic orbit, integrating \(\dot H\) over one period gives the same shell; equality would force \(\dot x\equiv0\), which by the preceding argument makes the orbit an equilibrium, a contradiction.

## Verification
The accompanying checker expands the polynomial coboundary identity exactly using rational arithmetic and verifies the source-parameter specialization \(1/(a^2(k+1))=5/4032\) and \(b/(k+1)=125/7\). It also verifies the equilibrium coordinates algebraically. The mathematical proof above, rather than numerical sampling, establishes the invariant-measure and equality-rigidity statements.

## Relationship to prior work
Wang, Dong, and Li introduce exactly this vector field, derive its two equilibria and a Routh–Hurwitz stability condition, and numerically study hidden/coexisting attractors and unstable periodic orbits. Their paper supplies the motivating recurrent objects but does not state the polynomial coboundary or the resulting invariant-measure RMS shell. The 2012 Wei–Yang generalized Sprott-C predecessor is the \(k=0\) ancestor of the construction and does not contain the added \(kxy\) term that produces the \(k\)-dependent shell. Searches by exact equation, source DOI/title, invariant-measure terminology, stationary-moment terminology, and equivalent RMS formulations did not locate a published statement implying the result.

A 2026 paper titled “Dynamics and integrability of a modified Sprott C system” is plausibly related by family name, but the accessible metadata does not identify the same vector field; its unavailable full text is retained as a residual literature risk rather than treated as negative evidence.

## Limitations
The result constrains compact recurrent statistical states but does not prove that the numerically reported chaotic set is invariant in a rigorous computer-assisted sense. It gives no pointwise amplitude bound, no basin-size estimate, and no classification of all invariant measures. The literature comparison cannot exclude an unindexed or inaccessible source that independently records the same coboundary.

## References
1. J. Wang, C. Dong, and H. Li, “A New Variable-Boostable 3D Chaotic System with Hidden and Coexisting Attractors: Dynamical Analysis, Periodic Orbit Coding, Circuit Simulation, and Synchronization,” *Fractal and Fractional* 6 (2022), 740. DOI: 10.3390/fractalfract6120740.
2. Z. Wei and Q. Yang, “Dynamical analysis of the generalized Sprott C system with only two stable equilibria,” *Nonlinear Dynamics* 68 (2012), 543–554. DOI: 10.1007/s11071-011-0235-8.
3. S. Hussein, R. H. Salih, and I. Ahmad, “Dynamics and integrability of a modified Sprott C system,” *Physica D* 490 (2026), 135160. DOI: 10.1016/j.physd.2026.135160.
