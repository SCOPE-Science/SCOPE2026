# Exact local-stability boundary on the principal four-dimensional laser slice
## Finding
Consider the smooth autonomous system
\[
\dot x_1=\sigma(x_2-x_1),\qquad
\dot x_2=-x_2-\delta x_3+(r-x_4)x_1,
\]
\[
\dot x_3=\delta x_2-x_3,\qquad
\dot x_4=-b x_4+x_1x_2.
\]
On the parameter slice \(\sigma=4\), \(\delta=1/2\), \(b=2\), put \(q=r-5/4\). For every \(r>5/4\), the nonzero equilibria are
\[
E_\pm=\left(\pm\sqrt{2q},\,\pm\sqrt{2q},\,\pm\tfrac12\sqrt{2q},\,q\right).
\]
Their common characteristic polynomial is
\[
p_q(\lambda)=\lambda^4+8\lambda^3+\left(2q+\tfrac{65}{4}\right)\lambda^2+\left(18q+\tfrac{17}{2}\right)\lambda+16q.
\]
The pair \(E_\pm\) is asymptotically stable exactly when
\[
\frac54<r<r_H,\qquad
r_H=\frac{103+\sqrt{10153}}6\approx33.9603493413.
\]
At \(r=r_H\), the spectrum contains a simple imaginary pair \(\lambda=\pm i\omega_H\) with
\[
\omega_H^2=\frac{295+3\sqrt{10153}}8,
\]
and the remaining two eigenvalues have negative real parts. For every \(r>r_H\), each nonzero equilibrium has unstable dimension two.

The source uses this same \(b=2\) slice for its multistability computations and reports initial-condition-dependent switches near \(r=26.8\), \(27.9\), and \(28.1\). Since all three values are below \(r_H\), those switches occur while \(E_\pm\) remain locally asymptotically stable; they therefore cannot be equilibrium-destabilization thresholds.

## Assumptions and scope
The result concerns the exact integer-order vector field printed in Natiq et al. (2019), with \(\sigma=4\), \(\delta=1/2\), and \(b=2\). The statement is a complete linear stability classification of the two nonzero equilibria on that one-parameter slice. It does not classify global attractors or basins, and it does not assert a nonlinear Hopf bifurcation at \(r=r_H\).

For \(r\le5/4\), this note makes no stability claim about a nonzero pair because the two real nonzero equilibria do not exist. The origin remains a separate equilibrium and is not part of the finding.

## Proof
At an equilibrium, the first and third equations give \(x_2=x_1\) and \(x_3=x_1/2\). For a nonzero equilibrium, the second equation then gives \(x_4=r-1-1/4=q\). The fourth equation gives \(x_1^2=2q\). Thus real nonzero equilibria exist exactly for \(q>0\), and they are the displayed \(E_\pm\).

Write \(k=\sqrt{2q}\). At either sign choice, changing \(k\) to \(-k\) does not alter the characteristic polynomial. Direct expansion of \(\det(\lambda I-J)\) gives
\[
p_q(\lambda)=\lambda^4+a_1\lambda^3+a_2\lambda^2+a_3\lambda+a_4,
\]
with
\[
a_1=8,\qquad a_2=2q+\frac{65}4,\qquad a_3=18q+\frac{17}2,\qquad a_4=16q.
\]
For a monic quartic with positive coefficients, the Routh--Hurwitz determinants needed here are
\[
\Delta_2=a_1a_2-a_3=\frac{243-4q}2
\]
and
\[
\Delta_3=a_1a_2a_3-a_3^2-a_1^2a_4
=-\frac34\left(48q^2-1528q-1377\right).
\]
The positive zero of \(\Delta_3\) is
\[
q_H=\frac{191}{12}+\frac{\sqrt{10153}}6,
\]
so \(r_H=q_H+5/4=(103+\sqrt{10153})/6\). Moreover \(q_H<243/4\). Hence for \(0<q<q_H\), all quartic Hurwitz determinants are positive and both equilibria are asymptotically stable.

At \(q=q_H\), substituting \(\lambda=i\omega\) shows that the nonzero imaginary roots must satisfy \(\omega^2=a_3/8\). The identity \(\Delta_3=0\) supplies exactly such a pair, with
\[
\omega_H^2=\frac{295+3\sqrt{10153}}8.
\]
Indeed the polynomial factors exactly as
\[
p_{q_H}(\lambda)
=(\lambda^2+\omega_H^2)
\left(\lambda^2+8\lambda+\frac{269-\sqrt{10153}}{24}\right).
\]
The second quadratic has positive coefficients and therefore both of its roots lie in the open left half-plane. The two factors have no common root, so the imaginary pair is simple.

For \(q_H<q<243/4\), the first column of the Routh array has signs \(+,+,+,-,+\), hence two right-half-plane roots. For \(q>243/4\), it has signs \(+,+,-,+,+\), again giving two right-half-plane roots. At \(q=243/4\), no imaginary-axis crossing occurs: for \(q>0\), a nonzero imaginary root would force \(\Delta_3=0\), whereas \(q=243/4\ne q_H\). Continuity therefore gives the same unstable dimension two at that isolated Routh-array degeneracy. This proves the full classification.

## Verification
The accompanying `verify.py` uses only the Python standard library. It reconstructs \(\det(\lambda I-J)\) by an exact permutation expansion with rational coefficients, reduces \(k^2=2q\), reconstructs \(\Delta_2\) and \(\Delta_3\), checks the radical expressions for \(q_H\), \(r_H\), and \(\omega_H^2\), and checks the exact factorization at the boundary. A successful run prints `VERIFY_OK`.

As a numerical check at the source's representative value \(r=27\), the exact polynomial is
\[
\lambda^4+8\lambda^3+\frac{271}4\lambda^2+472\lambda+412,
\]
whose roots are approximately \(-6.86911\), \(-1.00210\), and \(-0.06439\pm7.73619i\). This numerical calculation is illustrative only; the stability claim rests on the exact Routh--Hurwitz proof.

## Relationship to prior work
Natiq et al. derive the equilibria and Jacobian of this laser flow. Their displayed analytic characteristic polynomial and Routh--Hurwitz calculation are explicitly specialized to \(b=1\). Elsewhere, including the paper's principal chaotic and multistability computations, they use \(b=2\). The source reports coexistence of stable fixed points with periodic or chaotic attractors and initial-condition-dependent transitions on the \(b=2\) slice, but it does not give the exact \(b=2\) local-stability boundary derived here.

Searches for the system name, DOI, \(b=2\) stability, Routh--Hurwitz analysis, the exact radical \(\sqrt{10153}\), and the decimal threshold did not locate a published statement of this boundary. Searches of a semantic database of mathematical findings found local-stability and Hopf-threshold results for other flows, but none covering this vector field or implying this threshold.

## Limitations
This is a local spectral result. It does not prove the existence, uniqueness, or type of any global attractor; it does not compute basin boundaries; and it does not establish the nondegeneracy conditions required for a nonlinear Hopf theorem at \(r=r_H\). The literature search reduces but cannot eliminate the possibility of an unindexed or differently formulated prior derivation.

## References
1. A. Natiq, S. Banerjee, S. He, A. M. Al-Saidi, M. R. M. Said, and A. Kilicman, “Dynamics and Complexity of a New 4D Chaotic Laser System,” *Entropy* 21(1):34 (2019), DOI 10.3390/e21010034, PMCID PMC7514140. Published 2019-01-07.
2. MSC2020, 37C75, “Stability theory for smooth dynamical systems.”
