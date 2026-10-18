# Reentrant equilibrium stability and a pinched imaginary-axis crossing in the Dong hidden-attractor flow

## Finding

For the Dong quadratic flow
\[
\dot x=a(y-x)+kxz,\qquad \dot y=-cy-xz,\qquad \dot z=xy-b,
\]
with \(a,b,c>0\) and real \(k\), a complete spectral stability partition of both symmetry-related equilibria depends **only** on \(a/c\) and \(k\), not on \(b\). Define
\[
 k_A=\frac{a(c-a)}{c^2},\qquad k_B=-\frac{a}{a-c}\quad(a\ne c).
\]
There are exactly two equilibria if \(k<a/c\) and none if \(k\ge a/c\). In the equilibrium region:

1. If \(a<c\), both equilibria are exponentially asymptotically stable precisely for \(k<k_A\).
2. If \(a=c\), both are exponentially asymptotically stable precisely for \(k<0\).
3. If \(a>c\) and \(a\ne2c\), both are exponentially asymptotically stable precisely for \(\min(k_A,k_B)<k<\max(k_A,k_B)\); they have exactly two eigenvalues with positive real part outside that open interval.
4. If \(a=2c\), no equilibrium is spectrally asymptotically stable for any \(k\). The isolated parameter \(k=-2\) has eigenvalues \(-2c,\,\pm2i\sqrt b\); for every other \(k<2\), both equilibria have two eigenvalues with positive real part.

In cases 1–3 the nonhyperbolic interval endpoints have a simple imaginary conjugate pair and one strictly negative real eigenvalue, and for all other admissible parameters outside the stable regions there are exactly two eigenvalues with positive real part. At every simple endpoint the real parts of the imaginary pair cross zero transversely. In contrast, at the pinched point \(a=2c,k=-2\), the real part of the branch approaching the positive imaginary eigenvalue has the exact two-sided quadratic law
\[
\operatorname{Re}\lambda_+(k)=\frac{bc}{64(b+c^2)}(k+2)^2+O((k+2)^3),
\qquad k\to-2.
\]
In particular, varying \(k\) cannot create a linearly stable equilibrium at \(a=2c\), although there is a unique nonhyperbolic parameter. For example, for any \(b>0\), choosing \(a=3,c=1\) gives a stable interval \(-6<k<-3/2\) and index-two instability on either side.

## Assumptions and scope

The ambient space is \(\mathbb R^3\); parameters \(a,b,c\) are strictly positive and \(k\) ranges through the real numbers. An equilibrium is **spectrally stable** here exactly when all Jacobian eigenvalues have negative real part (which implies local exponential asymptotic stability by the standard linearization theorem). The **unstable index** is the algebraic multiplicity of eigenvalues with positive real part. At a purely imaginary pair, no claim of nonlinear Lyapunov stability or existence, number, direction or criticality of nearby periodic solutions is made. The theorem does not classify all nonstationary or unbounded dynamics.

## Proof

**Equilibria.** Since \(xy=b>0\) at an equilibrium, neither \(x\) nor \(y\) vanishes. Solving \(y=b/x\) and \(z=-cy/x\) together with the first equation gives
\[
 x^2=\frac{b(a-ck)}a,\quad y=\frac b x,\quad
 z=-\frac{ac}{a-ck}.
\]
These yield exactly two real equilibria if and only if \(a-ck>0\). Both have the same characteristic polynomial by the rotational symmetry \((x,y,z)\mapsto(-x,-y,z)\).

**Exact Jacobian polynomial.** At either equilibrium, the matrix
\[
 J=\begin{pmatrix}-a+kz&a&kx\\-z&-c&-x\\y&x&0\end{pmatrix}
\]
has characteristic polynomial \(p(\lambda)=\lambda^3+Q\lambda^2+R\lambda+S\), where
\[
 Q=\frac{a^2+ac-c^2k}{a-ck},\qquad
 R=\frac{b[a-(a+c)k]}a,\qquad
 S=2b(a-ck).
\]
For \(k<a/c\), \(Q>0\) and \(S>0\). The third Routh determinant factors **exactly** as
\[
\Delta=QR-S=-\frac{b}{a(a-ck)}
  (a^2-ac+c^2k)(a+(a-c)k).
\]
The first Routh-column signs, when \(\Delta\ne0\), are those of \(1,Q,\Delta/Q,S\). Consequently \(\Delta>0\) implies all three roots have negative real part; \(\Delta<0\) gives two roots with positive real part and one root with negative real part. This also proves there are no other nonhyperbolic parameters inside the equilibrium region. When \(\Delta=0\), the polynomial factors
\[
 p(\lambda)=(\lambda+Q)(\lambda^2+R),\qquad
 R=S/Q>0,
\]
so the spectrum is exactly \(\{-Q,\pm i\sqrt R\}\).

**Parameter partition.** The first linear factor of \(\Delta\) vanishes at \(k_A\). If \(a\ne c\), the second vanishes at \(k_B\). When \(a<c\), \(k_A\in(0,a/c)\) whereas \(k_B>a/c\), hence the sign criterion leaves precisely \(k<k_A\) stable. When \(a=c\), the second factor equals \(a>0\), and stability is precisely \(k<0\). When \(a>c\), both roots are negative; their ordering separates precisely one open interval with opposite factor signs and \(\Delta>0\). The roots coincide if and only if \((a-c)^2=c^2\), which here is exactly \(a=2c\). This proves the complete classification, including the fact that \(b\) scales \(\Delta\) by a positive factor without affecting its sign.

**Transverse boundaries and pinching.** Write the cubic exactly as
\[
 p(\lambda)=(\lambda+Q)(\lambda^2+R)-\Delta.
\]
At any simple zero \(r\) of \(\Delta\), analytic perturbation of the simple eigenvalue \(i\sqrt{R(r)}\) gives the real-part crossing speed
\[
 \left.\frac{d}{dk}\operatorname{Re}\lambda_+(k)\right|_{k=r}
 =-\frac{\Delta'(r)}{2(Q(r)^2+R(r))}\ne0.
\]
The two crossings have opposite directions when \(a>c,a\ne2c\). At \(a=2c\), one has the exact identity
\[
\Delta=-\frac{bc(k+2)^2}{2(2-k)}.
\]
At \(k=-2\), \(Q=2c,R=4b,S=8bc\), giving the stated eigenvalues. Expanding the simple imaginary eigenvalue near \(k=-2\), the first real correction is \(-\Delta/[2(Q^2+R)]+O(\Delta^2)\). Since \(\Delta=-bc(k+2)^2/8+O((k+2)^3)\) and \(Q^2+R=4(c^2+b)+O(k+2)\), the stated coefficient \(bc/[64(b+c^2)]\) follows. Its strict positivity confirms quadratic contact without exchange of spectral stability.

## Verification

The standalone `verify.py` derives the characteristic polynomial and factored Routh determinant directly from the substituted three-dimensional Jacobian using exact symbolic algebra, independently checks the double-root specialization and exact quadratic coefficient, and checks the Routh unstable index against numerical eigenvalue counts at nineteen additional parameter points. Run `python verify.py` with Python 3, SymPy and NumPy installed. Its expected final output is `PASS exact characteristic, Routh determinant, double tangency; numerical cases: 19`. These finite tests are diagnostics: the parameter-uniform conclusions follow from the exact polynomial identities, inequalities and Routh theorem in the proof.

## Relationship to prior work

Chengwei Dong's 2022 original work [1], particularly Section 2 and Section 3.4, introduced the system, gave the equilibria and Jacobian and studied coexistence and parameter-dependent chaotic behavior; it discussed Routh–Hurwitz for the fixed \((a,b,c)=(10,100,11.2)\) and numerical scans of \(k\), without deriving the factored complete stability partition for arbitrary positive \((a,b,c)\), the reentrant \(a>c\) window, or the isolated quadratic imaginary-axis contact at \(a=2c\). The older Yang–Wei–Chen construction [2] corresponds to the unmodified \(k=0\) system and does not imply this two-threshold \(k\)-dependent classification. Classical Routh–Hurwitz [3] supplies the root-counting implication, not the system-specific factorization or its pinching geometry.

## Limitations

This is a complete **linearized equilibrium spectral** result for the parameter family, not a general global attractor theorem. Imaginary-axis conditions are called spectral crossings, not proven nonlinear Hopf bifurcations; no first Lyapunov coefficient, periodic-orbit existence or nonlinear behavior at the exceptional parameters is established. Exact factorization is symbolic; no numerical simulation is used as an infinite-domain certificate. Earlier unindexed or unexamined proofs of an equivalent stability factorization remain a priority risk.

## References

[1] C. Dong, *Dynamics, Periodic Orbit Analysis, and Circuit Implementation of a New Chaotic System with Hidden Attractor*, Fractal and Fractional **6** (2022), article 190, first published March 30, 2022, DOI: 10.3390/fractalfract6040190. https://www.mdpi.com/2504-3110/6/4/190

[2] G. Yang, S. Wei and G. Chen, *An Unusual 3D Autonomous Quadratic Chaotic System with Two Stable Node-Foci* (2010). Earlier \(k=0\) source cited in [1] as its reference 51.

[3] Classical Routh–Hurwitz criterion for real cubics, in any standard text on linear stability and differential equations.
