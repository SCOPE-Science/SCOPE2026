# Stationary height balance and Lyapunov-sum law in the Dong–Wang four-dimensional flow
## Finding
Consider the smooth autonomous flow
\[
\dot x=a(y-x)+kxz+w,\qquad
\dot y=-cy-xz,\qquad
\dot z=-b+xy,\qquad
\dot w=-my.
\]
Assume \(b>0\) and \(c>0\). Every compactly supported invariant Borel probability measure \(\mu\) satisfies
\[
\int xy\,d\mu=b,
\qquad
b\int z\,d\mu=-c\int y^2\,d\mu.
\]
Consequently \(\int y^2\,d\mu>0\) and \(\int z\,d\mu<0\). In particular, no compact invariant set of this flow can lie entirely in the closed half-space \(z\ge0\).

If \(\mu\) is also ergodic, then its four Lyapunov exponents, counted with multiplicity, obey the exact sum law
\[
\sum_{j=1}^4\lambda_j
=-a-c-\frac{kc}b\int y^2\,d\mu.
\]
Thus \(k>0\) forces the recurrent mean phase-volume rate strictly below \(-a-c\), \(k=0\) fixes it at \(-a-c\), and \(k<0\) forces it strictly above \(-a-c\).

## Assumptions and scope
The statement concerns invariant probability measures with compact support for the displayed polynomial vector field and, for the Lyapunov-sum conclusion, ergodic such measures. Compact support guarantees the integrability needed for the generator identities and for the derivative cocycle. No existence, uniqueness, mixing, hyperbolicity, or attractor claim is assumed.

The introducing article studies the parameter choice \((a,b,c,k,m)=(10,100,2.7,-0.2,1)\). For those values the theorem gives
\[
\sum_{j=1}^4\lambda_j=-12.7+0.0054\int y^2\,d\mu>-12.7.
\]
Its reported numerical quartet \((0.7796,0.1058,0,-12.7177)\) sums to \(-11.8323\). If that quartet is interpreted as an asymptotic spectrum of one ergodic invariant state, the exact law corresponds to \(\int y^2\,d\mu\approx160.685185\). This numerical back-calculation is a consistency illustration, not part of the proof of existence or hyperchaos.

## Proof
Let \(L\) denote the generator of the flow. For \(Q=y^2+z^2\), direct differentiation gives
\[
LQ
=2y(-cy-xz)+2z(-b+xy)
=-2cy^2-2bz.
\]
The cubic terms cancel exactly. Invariance of a compactly supported probability measure gives \(\int LQ\,d\mu=0\), hence
\[
b\int z\,d\mu=-c\int y^2\,d\mu.
\]
Applying the same invariance identity to the coordinate function \(z\) gives
\[
0=\int Lz\,d\mu
=\int(-b+xy)\,d\mu,
\]
so \(\int xy\,d\mu=b\).

Because \(b>0\), the last identity rules out \(y=0\) almost surely. Therefore \(\int y^2\,d\mu>0\); with \(c>0\), the balance above yields \(\int z\,d\mu<0\).

If a compact invariant set \(K\) were contained in \(z\ge0\), the continuous flow on \(K\) would admit an invariant probability measure supported on \(K\). Such a measure would satisfy \(\int z\,d\mu\ge0\), contradicting the strict negative-mean identity. Hence no compact invariant set is contained in \(z\ge0\).

The divergence of the vector field is
\[
\nabla\!\cdot F=-a-c+kz.
\]
For an ergodic compactly supported invariant measure, Liouville's determinant formula for the variational flow and the ergodic theorem give
\[
\sum_{j=1}^4\lambda_j=\int \nabla\!\cdot F\,d\mu.
\]
Substituting the stationary height balance proves
\[
\sum_{j=1}^4\lambda_j
=-a-c+k\int z\,d\mu
=-a-c-\frac{kc}b\int y^2\,d\mu.
\]
Since \(\int y^2\,d\mu>0\), the trichotomy by the sign of \(k\) follows.

## Verification
The included `verify.py` is a dependency-free exact polynomial replay. It constructs the vector field as a multivariate polynomial over the integers, differentiates \(Q=y^2+z^2\), and checks the identity \(LQ=-2cy^2-2bz\) coefficient by coefficient. It also checks the divergence formula and the exact arithmetic for the source parameter specialization. Running `python3 verify.py` prints `VERIFY_OK`; the captured output is included as `VERIFY_OUTPUT.txt`.

The proof does not use finite-time numerical trajectories as evidence for an infinite-time statement. The source's numerical Lyapunov exponents are used only for the explicitly conditional consistency calculation above.

## Relationship to prior work
Dong and Wang introduce the four-dimensional system and report symmetry, the pointwise divergence \(-a+kz-c\), numerical Lyapunov spectra, bifurcation diagrams, coexisting attractors, unstable periodic orbits, and circuit realization. Their dissipativity discussion is pointwise in \(z\); it does not derive the stationary balance for \(y^2+z^2\), the negative mean-height constraint, the half-space recurrence obstruction, or the invariant-measure Lyapunov-sum formula.

The three-dimensional precursor by Dong has the same \(y,z\) subsystem and therefore the same elementary balance identity for that different flow, but its article likewise analyzes equilibria, divergence, numerical Lyapunov exponents, bifurcations, and periodic-orbit topology rather than this invariant-measure statement. General literature relating the sum of Lyapunov exponents to mean divergence supplies the final general principle, but not the system-specific height balance that makes the formula explicit.

## Limitations
The result gives necessary constraints on compact recurrent statistics. It does not prove that a particular numerical attractor exists, is ergodic, is hyperchaotic, or supports the reported numerical Lyapunov spectrum. It also does not classify compact invariant sets outside the half-space obstruction. The strict sign conclusions require \(b>0\) and \(c>0\); with other signs the exact algebraic identities remain valid when \(b\ne0\), but their sign consequences change.

## References
1. C. Dong and J. Wang, “Hidden and Coexisting Attractors in a Novel 4D Hyperchaotic System with No Equilibrium Point,” *Fractal and Fractional* 6 (2022), 306. DOI: 10.3390/fractalfract6060306. Published 31 May 2022.
2. C. Dong, “Dynamics, Periodic Orbit Analysis, and Circuit Implementation of a New Chaotic System with Hidden Attractor,” *Fractal and Fractional* 6 (2022), 190. DOI: 10.3390/fractalfract6040190. Published 30 March 2022.
3. I. Fouxon, “Evolution to a singular measure and two sums of Lyapunov exponents,” *Journal of Statistical Mechanics: Theory and Experiment* 2011 (2011), L02001. DOI: 10.1088/1742-5468/2011/02/L02001.
4. MSC2020, 37C10: Dynamics induced by flows and semiflows.
