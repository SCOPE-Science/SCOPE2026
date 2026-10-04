# The KCC second-order Liu system contains an exponentially repelling extraneous mode
## Finding
Consider the Liu system
\[
\dot x=a(y-x),\qquad \dot y=bx-kxz,\qquad \dot z=-cz+hx^2,
\]
with \(a,b,k,c,h>0\). Liu and Zhang rewrite it as the pair of second-order equations
\[
\ddot x+a x(kz-b)+a\dot x=0,
\]
\[
\ddot z+c(hx^2-cz)-2hx\dot x=0.
\]
On the full second-order phase space, these equations contain one extra dynamical degree of freedom. If \(v=\dot x\), \(w=\dot z\), and
\[
Q=w+cz-hx^2,
\]
then every solution of the displayed second-order system satisfies
\[
\dot Q=cQ.
\]
Thus the original Liu flow is represented exactly by the invariant hypersurface \(Q=0\), not by the whole four-dimensional SODE phase space. Off that hypersurface, \(Q(t)=Q(0)e^{ct}\), so the added direction is exponentially repelling because \(c>0\).

At the origin, the original \(z\)-direction has eigenvalue \(-c\). The extended SODE has the two normal modes \(e^{-ct}\) and \(e^{ct}\), hence eigenvalues \(-c\) and \(+c\). The source reports the deviation exponent \(\delta_2(E)=c\); this is exactly the growth rate of the extraneous normal mode. Consequently, an unconstrained deviation-vector calculation for the four-dimensional SODE is not, without an additional tangency condition, a calculation of deviations between nearby trajectories of the original three-dimensional Liu flow.

## Assumptions and scope
The statement concerns the classical integer-order Liu system and the specific SODE transformation printed in Liu and Zhang (2024). The parameters satisfy \(a,b,k,c,h>0\), as in that source. No claim is made that every KCC conclusion in the article is false. The result identifies the precise invariant constraint required for equivalence and isolates one nonphysical mode of the unconstrained SODE.

The original flow is recovered from the constrained SODE by
\[
y=x+\frac{v}{a},\qquad w=hx^2-cz.
\]
Conversely, every solution of the original Liu system maps into the hypersurface \(Q=0\) under \(v=a(y-x)\), \(w=-cz+hx^2\).

## Proof
Write the second-order system as a first-order system in \((x,v,z,w)\):
\[
\dot x=v,
\]
\[
\dot v=-ax(kz-b)-av,
\]
\[
\dot z=w,
\]
\[
\dot w=-c(hx^2-cz)+2hxv.
\]
For \(Q=w+cz-hx^2\), direct differentiation gives
\[
\dot Q=\dot w+c\dot z-2hx\dot x.
\]
Substitution of the four equations yields
\[
\dot Q=-c(hx^2-cz)+2hxv+cw-2hxv=c(w+cz-hx^2)=cQ.
\]
Therefore \(Q(t)=Q(0)e^{ct}\). The set \(Q=0\) is invariant, and for \(c>0\) deviations normal to it grow exponentially forward in time.

On \(Q=0\), define \(y=x+v/a\). Then
\[
\dot x=v=a(y-x),
\]
and
\[
\dot y=v+\frac{\dot v}{a}=v-x(kz-b)-v=bx-kxz.
\]
The constraint \(Q=0\) gives \(w=hx^2-cz\), so \(\dot z=-cz+hx^2\). Hence the SODE restricted to \(Q=0\) is smoothly equivalent to the original Liu system. The converse follows by differentiating the original equations, so the restriction is exact.

For a concrete witness that the full SODE is larger, set \(x(t)=0\), \(v(t)=0\). The SODE then permits
\[
z(t)=A e^{ct}+B e^{-ct},\qquad w(t)=cA e^{ct}-cB e^{-ct}.
\]
The original Liu equation with \(x=y=0\) requires \(\dot z=-cz\), which forces \(A=0\). Thus every choice \(A\ne0\) is an explicit SODE solution that is not a Liu trajectory.

Linearizing at the origin makes the same defect visible spectrally. The physical \(z\)-equation contributes only \(-c\), while the extended \(z,w\) block is
\[
\begin{pmatrix}0&1\\ c^2&0\end{pmatrix},
\]
with eigenvalues \(\{-c,+c\}\). The \(x,v\) block has characteristic polynomial \(\lambda^2+a\lambda-ab\), identical to the physical \(x,y\) block. Thus \(+c\) is precisely the added normal eigenvalue.

## Verification
The algebraic checker `verify.py` expands the Lie derivative of \(Q\) under the published SODE and verifies identically that it equals \(cQ\). It also checks the origin characteristic polynomials of the physical and extended systems and the explicit extra solution. The checker was executed from the packaged file contents and returned `VERIFY_OK`.

The critical argument is symbolic and exact; it does not rely on numerical integration, finite-time Lyapunov estimates, or parameter sampling.

## Relationship to prior work
Liu and Zhang (2024) explicitly state that their two SODEs are equivalent to the Liu system and add that eliminating any one variable gives topologically conjugate equations. The same article reports \(\delta_2(E)=c\) in its deviation-vector analysis. The calculation above shows that equivalence holds only after imposing \(Q=0\), and that \(+c\) is the normal growth rate created by the unconstrained extension.

Harko et al. (2015) is a foundational KCC treatment of the Lorenz system and is relevant methodological background because it also reformulates a three-dimensional first-order chaotic system as two second-order equations. Targeted searches of that literature and of indexed mathematical findings did not locate a result stating the Liu-specific constraint \(Q=0\), its exact defect law \(\dot Q=cQ\), or the identification of the reported \(\delta_2(E)=c\) with an extraneous normal mode.

## Limitations
This result does not provide a replacement constrained-KCC theory, nor does it classify Jacobi stability after restricting admissible deviations to the tangent bundle of \(Q=0\). It also does not claim that the source's final label of instability at the origin is wrong: the original Liu linearization already has one positive eigenvalue from \(\lambda^2+a\lambda-ab=0\) when \(a,b>0\). The correction is structural: the full SODE has an extra repelling direction, so unconstrained SODE deviations cannot automatically be interpreted as physical Liu-flow deviations.

A residual originality risk is that an unindexed correction or commentary may have noticed the same hidden constraint; no such source was found in the targeted searches performed for this result.

## References
1. Q. Liu and X. Zhang, “Jacobi Stability Analysis of Liu System: Detecting Chaos,” *Mathematics* 12 (2024), 1981. DOI: 10.3390/math12131981. Published 2024-06-26. Primary MSC: 35Q30.
2. T. Harko, C. Y. Ho, C. S. Leung, and S. Yip, “Jacobi stability analysis of the Lorenz system,” arXiv:1504.02880 (2015).
