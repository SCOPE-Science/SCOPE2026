# Stationary derivative-energy law and strict period floor in the generalized Sprott L flow

## Finding
Consider
\[
\dot x=y+\alpha z,\qquad
\dot y=\beta x^2-y,\qquad
\dot z=\gamma-x,
\]
with \(\alpha,\beta,\gamma>0\). Every compactly supported invariant probability measure \(\mu\) satisfies
\[
\mathbb E_\mu[x]=\gamma,\qquad
\mathbb E_\mu[y]=\beta\mathbb E_\mu[x^2],\qquad
\mathbb E_\mu[z]=-\frac{\beta}{\alpha}\mathbb E_\mu[x^2],
\]
and
\[
\mathbb E_\mu[(y+\alpha z)^2]
=\alpha\mathbb E_\mu[(x-\gamma)^2].
\]
If
\[
z_*=-\frac{\beta\gamma^2}{\alpha}
\]
is the height of the unique equilibrium, then
\[
z_*-\mathbb E_\mu[z]
=\frac{\beta}{\alpha}\operatorname{Var}_\mu(x)\ge0.
\]
Equality holds exactly for the equilibrium measure. Any other compact invariant measure gives positive mass to both half-spaces \(x<\gamma\) and \(x>\gamma\).

Every bounded complete trajectory has \(y(t)>0\). Every nonconstant periodic orbit of least period \(P\) satisfies the strict bound
\[
P>\frac{2\pi}{\sqrt{\alpha}},
\]
and crosses \(x=\gamma\) at least twice per least period.

## Assumptions and scope
The phase space is \(\mathbb R^3\). Parameters \(\alpha,\beta,\gamma\) are strictly positive. An invariant probability measure is assumed compactly supported, so polynomial generator identities are integrable. A bounded complete trajectory is a solution defined for all \(t\in\mathbb R\) with bounded image.

The canonical Sprott L parameters are \(\alpha=3.9\), \(\beta=0.9\), and \(\gamma=1\). The theorem is stated for the positive three-parameter family used in later stability work. For the canonical value \(\alpha=3.9\), every nonconstant periodic orbit therefore obeys \(P>3.1816145556\ldots\).

## Proof
Stationarity of the coordinate functions gives
\[
0=\mathbb E_\mu[\dot z]=\gamma-\mathbb E_\mu[x],
\]
\[
0=\mathbb E_\mu[\dot y]
=\beta\mathbb E_\mu[x^2]-\mathbb E_\mu[y],
\]
and
\[
0=\mathbb E_\mu[\dot x]
=\mathbb E_\mu[y]+\alpha\mathbb E_\mu[z].
\]
These are the three first-moment identities.

Set
\[
v=\dot z=\gamma-x,\qquad
w=\dot v=\ddot z=-(y+\alpha z).
\]
Differentiating once more and using the vector field gives
\[
\dot w+w+\alpha v+\alpha z+\beta(\gamma-v)^2=0.
\]
Define the polynomial certificate
\[
C=\frac{w^2}{2}+\frac{\alpha v^2}{2}+\alpha zv
-\frac{\beta}{3}(\gamma-v)^3.
\]
A direct differentiation gives the exact coboundary
\[
\dot C=\alpha v^2-w^2.
\]
Integration against any compactly supported invariant probability measure yields
\[
\mathbb E_\mu[w^2]=\alpha\mathbb E_\mu[v^2].
\]
Since \(w=-(y+\alpha z)\), \(v=\gamma-x\), and \(\mathbb E_\mu[x]=\gamma\), this is the stated derivative-energy law.

The mean-height formula becomes
\[
\mathbb E_\mu[z]
=-\frac{\beta}{\alpha}
\left(\gamma^2+\operatorname{Var}_\mu(x)\right),
\]
which proves the defect identity. If equality holds, then \(x=\gamma\) almost surely. Invariance of the support then forces \(\dot x=0\), \(\dot z=0\), and
\[
y=\beta\gamma^2,\qquad
z=-\frac{\beta\gamma^2}{\alpha},
\]
so the measure is the unique equilibrium measure. Conversely that measure gives equality. If a nonequilibrium invariant measure failed to charge one of \(x<\gamma\) or \(x>\gamma\), its mean \(\gamma\) would force \(x=\gamma\) almost surely, contradicting the equality characterization.

For a bounded complete trajectory, variation of constants in
\[
\dot y+y=\beta x^2
\]
gives
\[
y(t)=\beta\int_0^\infty e^{-s}x(t-s)^2\,ds.
\]
The right-hand side cannot vanish: vanishing would force \(x\) to vanish on an entire backward half-line, which is incompatible with \(\dot z=\gamma-x\) and bounded completeness when \(\gamma>0\). Hence \(y(t)>0\).

Now let a periodic orbit have least period \(P\). The function \(v=\dot z\) has mean zero, and the invariant-measure energy law applied to normalized time average gives
\[
\int_0^P \dot v^2\,dt
=\alpha\int_0^P v^2\,dt.
\]
A nonconstant orbit has \(v\not\equiv0\). Wirtinger's inequality therefore gives
\[
\alpha\ge \left(\frac{2\pi}{P}\right)^2,
\]
so \(P\ge2\pi/\sqrt{\alpha}\).

If equality held, then \(v\) would be a nonzero first harmonic and would satisfy \(\ddot v+\alpha v=0\). The exact jerk relation
\[
\ddot v+\dot v+\alpha v+\alpha z+\beta(\gamma-v)^2=0
\]
would reduce to
\[
\dot v+\alpha z+\beta(\gamma-v)^2=0.
\]
But \(d(\dot v+\alpha z)/dt=\ddot v+\alpha v=0\), so \((\gamma-v)^2\) would be constant. A nonconstant harmonic cannot have constant squared distance from \(\gamma\). Thus equality is impossible and the period inequality is strict.

Finally, a nonconstant periodic \(x\) has time average \(\gamma\), so continuity forces values on both sides of \(\gamma\); a periodic sign-changing function \(x-\gamma\) has at least two zero crossings per least period.

## Verification
The included `verify.py` is dependency-free and uses exact rational sparse-polynomial arithmetic. It reconstructs the vector field, the variables \(v\) and \(w\), the certificate \(C\), and verifies symbolically that
\[
LC=\alpha v^2-w^2.
\]
It also verifies the eliminated jerk relation. Its recorded output is `VERIFY_OK`.

## Relationship to prior work
Sprott's 1994 paper introduced the simple chaotic-flow catalog. Sprott's later parameter-region note gives Case L in a rescaled family and numerically maps stable, periodic, chaotic, and unbounded regions. Erjaee and Alnasr study phase synchronization of coupled Sprott L systems. Mondal's stability/control work uses the positive three-parameter family, identifies its unique equilibrium, proves dissipativity, analyzes local linear stability, and designs feedback control. Mondal, Islam, and Sen's Sprott L synchronization paper is indexed under MSC 37D45.

The inspected same-object sources do not state the compact-invariant-measure derivative-energy law, the exact equilibrium-height defect, the pointwise positivity of \(y\) on bounded complete trajectories, or the strict universal period floor. Targeted published-finding corpus searches returned only analogous period or stationary-balance results for different vector fields, not Sprott L.

## Limitations
The result does not prove existence of a non-equilibrium compact invariant set or periodic orbit for every positive parameter triple, nor does it determine stability, entropy, mixing, basins, or attainability of the period infimum. The original 1994 article establishes the family historically but is not a theorem about invariant measures. The full text of the Bulletin of the Calcutta Mathematical Society synchronization paper was not retrievable from its listed publisher URL during inspection; its metadata and MSC were checked through MaRDI, and the related 2015 thesis chapter was inspected in full. The result therefore retains a bibliographic risk from inaccessible or differently phrased older literature.

## References
1. J. C. Sprott, “Some simple chaotic flows,” *Physical Review E* 50, R647–R650 (1994), DOI: 10.1103/PhysRevE.50.R647.
2. J. C. Sprott, “Dynamic Regions in Simple Chaotic Flows,” technical note, 2013, revised 2014.
3. G. H. Erjaee and M. Alnasr, “Phase Synchronization in Coupled Sprott Chaotic Systems Presented by Fractional Differential Equations,” *Discrete Dynamics in Nature and Society* (2009), DOI: 10.1155/2009/753746.
4. A. Mondal, *Stability and Control Analysis of Some Problems of Chaotic Dynamical Systems*, PhD thesis, University of Calcutta (2015), Chapter 2.2.
5. A. Mondal, N. Islam, and S. Sen, “Unidirectional synchronization of chaotic Sprott model L,” *Bulletin of the Calcutta Mathematical Society* 105(2), 93–102; indexed by MaRDI with MSC 37D45.
