# Sharp feedback-gain boundary and cubic collapse of a three-node stability tongue

## Finding

Consider the signed, directed three-node linear flow \(\dot z=J_{a,t,\rho}z\), where \(a>0\), \(t\geq0\), \(\rho>0\), and
\[
J_{a,t,\rho}=\begin{pmatrix}
-a-t/2&1&0\\
-1&-a-t/2&1\\
-\rho&0&-a+t
\end{pmatrix}.
\]
Its two negative feedback cycles have lengths two and three, with gains \(-1\) and \(-\rho\). The diagonal heterogeneity has zero mean and therefore leaves the average intrinsic decay \(-a\) unchanged.

Set
\[
B(a,t)=1+3a^2-\frac34t^2,\qquad T_B(a)=\frac2{\sqrt3}\sqrt{1+3a^2},
\]
\[
\rho_-(a,t)=t+\frac14t^3-a^3-a\left(1-\frac34t^2\right),
\quad
\rho_+(a,t)=t+\frac14t^3+8a^3+2a\left(1-\frac34t^2\right).
\]
**Exact stability tongue:** for every such triple \((a,t,\rho)\), all eigenvalues of \(J_{a,t,\rho}\) have strictly negative real part if and only if
\[
0\le t<T_B(a),\qquad \rho_-(a,t)<\rho<\rho_+(a,t).
\]
Within \(t<T_B(a)\), the boundary \(\rho=\rho_+\) has the simple imaginary pair \(\pm i\sqrt{B(a,t)}\) and the third eigenvalue \(-3a\). The boundary \(\rho=\rho_-\) has a simple zero eigenvalue and two strictly left-half-plane eigenvalues.

Define \(t_0=t_0(\rho)>0\) by \(t_0+t_0^3/4=\rho\), and put
\[
\rho_* = \frac8{3\sqrt3},\quad t_* = \frac2{\sqrt3},\quad
v=1-\frac34t_0^2,\quad s=1+\frac34t_0^2.
\]
As damping \(a\downarrow0\) with \(\rho\) fixed, the complete classification of possible **disorder-induced stabilization** is:

* If \(0<\rho<\rho_*\), for all sufficiently small \(a>0\) the *entire* stability set in \(t\ge0\) is a single interval \((t_H,t_Z)\), where
  \[
  t_H=t_0-\frac{2v}{s}a+O(a^2),\quad
  t_Z=t_0+\frac{v}{s}a+O(a^2),\quad
  t_Z-t_H=\frac{3v}{s}a+O(a^2).
  \]
* If \(\rho=\rho_*\), there remains exactly one stability interval, but it is **cubically narrow**:
  \[
  t_H=t_*-4a^3+O(a^4),\quad
  t_Z=t_*+\tfrac12a^3+O(a^4),\quad
  t_Z-t_H=\tfrac92a^3+O(a^4).
  \]
  Its oscillatory boundary frequency is \(\sqrt3a+O(a^2)\).
* If \(\rho>\rho_*\), no value of \(t\ge0\) stabilizes the system for all sufficiently small positive \(a\).

In the first two cases the homogeneous system \(t=0\) is unstable for sufficiently small \(a\). Thus \(\rho_*\) is a sharp two-loop/three-loop gain threshold for stabilization by zero-mean diagonal heterogeneity in the weak-damping regime. In the singular limit \(a=0\), the threshold point \((t,\rho)=(t_*,\rho_*)\) has characteristic polynomial \(\lambda^3\): the cubic narrowing is organized by a nilpotent triple-zero degeneracy.

## Assumptions and scope

The model is a real linear autonomous ODE on \(\mathbb R^3\). Stability means exponential asymptotic stability of its zero equilibrium, equivalently strict Hurwitz stability. All parameters and quantifiers are explicit above. The theorem makes no claim of global nonlinear bifurcations or of ecological persistence for arbitrary nonlinear completions. The equality surfaces are spectral, not assertions of nonlinear Hopf bifurcations.

A concrete rational certificate is \(\rho=1\), \(a=1/4\), \(t=3/4\). The characteristic polynomial at this heterogeneous point is
\[
\lambda^3+\frac34\lambda^2+\frac{49}{64}\lambda+\frac{39}{128}.
\]
Its strict cubic Hurwitz determinant is \(69/256>0\). At equal diagonal rates \(t=0\), the same model has polynomial \(\lambda^3+3\lambda^2/4+19\lambda/16+81/64\), whose Hurwitz determinant is \(-3/8<0\), so the homogeneous equilibrium is unstable.

## Proof

**1. Characteristic polynomial and exact tongue.** Direct expansion gives
\[
\det(\lambda I-J)=(\lambda+a)^3+\left(1-\frac34t^2\right)(\lambda+a)+\rho-t-\frac14t^3
=\lambda^3+3a\lambda^2+B\lambda+C,
\]
where
\[
C=a^3+a\left(1-\frac34t^2\right)+\rho-t-\frac14t^3=\rho-\rho_-.
\]
The final cubic Hurwitz determinant is
\[
H=3aB-C=8a^3+2a\left(1-\frac34t^2\right)+t+\frac14t^3-\rho=\rho_+-\rho.
\]
For a monic real cubic with quadratic coefficient \(3a>0\), Routh–Hurwitz gives strict stability precisely when \(B>0\), \(C>0\), and \(H>0\). These are exactly the three displayed inequalities. At \(C=0\), the polynomial factors \(\lambda(\lambda^2+3a\lambda+B)\). At \(H=0\), it factors \((\lambda+3a)(\lambda^2+B)\). When \(B>0\), these are the claimed simple zero and imaginary-pair boundaries.

**2. Unique interval at weak damping.** For fixed \(\rho>0\), write
\[
q(t)=\rho-t-\frac14t^3,\quad b_0(t)=1-\frac34t^2,
\quad C=q(t)+a b_0(t)+a^3,\quad H=-q(t)+2a b_0(t)+8a^3.
\]
For every sufficiently small \(a>0\), \(H(0)=8a^3+2a-\rho<0\) and \(C(0)>0\). Moreover
\[
C'(t)=-1-\frac34t^2-\frac32at<0,
\quad H'(t)=1+\frac34t^2-3at=\frac34(t-2a)^2+1-3a^2>0
\]
whenever \(0<a<1/\sqrt3\). Thus \(H\) has a unique positive root \(t_H\), \(C\) has a unique positive root \(t_Z\), and simultaneous positivity is possible only when \(t_H<t<t_Z\). Both roots approach the unique zero \(t_0\) of \(q\), as \(a\downarrow0\).

**3. Subcritical gain.** If \(\rho<\rho_*\), then \(t_0<t_*\) and \(v=b_0(t_0)>0\). Since \(q'(t_0)=-s\), the implicit-function theorem applied separately to \(H=0\) and \(C=0\) gives
\[
t_H=t_0-2va/s+O(a^2),\qquad t_Z=t_0+va/s+O(a^2).
\]
Their ordering is strict for small \(a\), and \(B(a,t)>0\) throughout the interval because its endpoints approach \(t_0<t_*\). The interval is therefore exactly the stability set.

**4. Critical gain and cubic scale.** If \(\rho=\rho_*\), then \(t_0=t_*\), \(b_0(t_*)=0\), and \(s=2\). Near \(t_*\), the implicit equations are
\[
H=2(t-t_*)+8a^3+O((t-t_*)^2+a|t-t_*|),
\quad C=-2(t-t_*)+a^3+O((t-t_*)^2+a|t-t_*|).
\]
Consequently \(t_H=t_*-4a^3+O(a^4)\) and \(t_Z=t_*+a^3/2+O(a^4)\). Throughout this interval \(B(a,t)=3a^2+O(a^3)>0\). At the Hopf boundary \(\sqrt{B}=\sqrt3a+O(a^2)\). At \(a=0,t=t_*,\rho=\rho_*\), all three polynomial coefficients vanish except the cubic term.

**5. Supercritical gain and genuinely induced stability.** If \(\rho>\rho_*\), then \(v<0\), and the same implicit expansions give \(t_H=t_0-2va/s+O(a^2)>t_Z=t_0+va/s+O(a^2)\) for all sufficiently small \(a\). Hence \(H>0\) and \(C>0\) cannot simultaneously occur for any nonnegative \(t\), regardless of \(B\). Finally, at \(t=0\) let \(u>0\) solve \(u^3+u=\rho\). The three roots of \(\mu^3+\mu+\rho\) are one negative real root \(-u\) and a conjugate pair with real part \(u/2\); shifting by \(-a\) shows that the equal-diagonal flow is unstable whenever \(0<a<u/2\).

**6. Direction of the two crossings.** At the lower boundary \(H=0\), implicit differentiation of the characteristic equation gives for the imaginary-pair branch
\[
\frac{d}{dt}\operatorname{Re}\lambda\Big|_{t_H}=-\frac{H'(t_H)}{2(B(a,t_H)+9a^2)}<0.
\]
At \(C=0\) the simple real eigenvalue has derivative \(\lambda'(t_Z)=-C'(t_Z)/B(a,t_Z)>0\). For all sufficiently small \(a\) in the subcritical and critical cases, the lower boundary therefore crosses *into* stability and the upper one crosses *out of* stability, with different spectral mechanisms.

## Verification

The companion standalone `verify.py` uses exact fractions to check the two rational Hurwitz certificates and symbolic coefficient identities by finite polynomial operations, and independently brackets both stability endpoints numerically for gains below, at, and above \(\rho_*\). It also tests the predicted first- and third-order window asymptotics. Execute `python3 verify.py` from a directory containing that file. The infinite quantified assertions, root uniqueness, and asymptotic error orders are proved above; numerical root bracketing is supplemental only.

## Relationship to prior work

Montanari, Zanin and Motter (2026) establish the general mechanism by which non-Hermitian network coupling can make disorder favorable to linear stability, including ecological networks. This theorem does not claim that mechanism as new: it isolates a minimal signed network with *two competing negative feedback cycles*, gives the **complete** stability region for its two tunable gains, and discovers a sharp weak-damping gain threshold with a new cubic-versus-linear stabilization-window dichotomy. Their main text and supplementary stability analyses do not supply these specific transition constants or the zero-Hopf/triple-zero limiting geometry.

Kinkhabwala (2015) gives general network-topology representations of Routh–Hurwitz determinants for arbitrary reaction networks. Its general cycle formula is a prior method, not an exact statement of the present damping-singular threshold and its asymptotic stability-tongue geometry. Our coefficient computation is an application of that classical framework, while the feedback-gain classification and cubic cusp require the additional singular-limit argument. The 2024 review by Chen, Wang and Liu discusses the classical secant criterion for a *single* negative cyclic feedback loop; our motif contains overlapping length-two and length-three negative loops and is not the single-loop configuration covered by that criterion.

## Limitations

The theorem is an exact linear spectral classification of a specified three-node signed network. Other graph motifs, nonlinear large-amplitude dynamics, resilience to finite perturbations, and applications to real ecological time series are not established. The exact condition and asymptotic threshold depend on the zero-mean diagonal perturbation direction and the normalization of the two feedback loops. Historical novelty remains provisional against unindexed small-network control literature.

## References

1. A. N. Montanari, P. Zanin, A. E. Motter, *Disorder-promoted stability*, Science **393** (2026), 1241–1249. DOI: 10.1126/science.aeg3946; public September 17, 2026; preprint arXiv:2609.25226.
2. A. Kinkhabwala, *Implications of Network Topology on Stability*, PLOS ONE **10** (2015), e0122150. DOI: 10.1371/journal.pone.0122150.
3. C. Chen, X.-W. Wang and Y.-Y. Liu, *Stability of Ecological Systems: A Theoretical Review*, Physics Reports **1088** (2024), 1–41.
4. E. J. Routh, *A Treatise on the Stability of a Given State of Motion* (1877); A. Hurwitz, *On the Conditions Under Which an Equation Has Only Roots with Negative Real Parts* (1895). Classical cubic Hurwitz criterion.
