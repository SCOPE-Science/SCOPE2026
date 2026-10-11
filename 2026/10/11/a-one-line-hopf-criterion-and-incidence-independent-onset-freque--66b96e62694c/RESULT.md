# A one-line Hopf criterion and incidence-independent onset frequency in a nonlinear-incidence SIRS model
## Finding
Consider the equilibrium-normalized planar SIRS family
\[
\dot x=rac{Kx^p}{1+Bx^q}\left(rac{1}{\widetilde X}-x-syight)-rx,\qquad
\dot y=x-y,
\]
with \(s>0\), \(s<r<s+1\), \(0<\widetilde X<1/(s+1)\), and with \(K\) chosen so that \((1,1)\) remains the positive equilibrium:
\[
K=rac{r(1+B)\widetilde X}{X_1},\qquad X_1:=1-(s+1)\widetilde X.
\]
Define
\[
p_c:=1+rac1r+rac{\widetilde X}{X_1},\qquad q_c:=p-p_c,
\qquad B_H:=rac{q_c}{q-q_c}.
\]
Then the two Hopf alternatives displayed in Proposition 3.1 of arXiv:2609.38874v1 are exactly equivalent to the single criterion
\[
rac1{s+1+sr}<\widetilde X<rac1{s+1},\qquad p>p_c,\qquad q>q_c,
\qquad B=B_H.
\]
At every such point the eigenvalues of the original, un-rescaled vector field are \(\lambda=\pm i\omega_H\), where
\[
\omega_H^2=rac{rs\widetilde X}{X_1}-1
=rac{(s+1+sr)\widetilde X-1}{X_1}>0.
\]
Moreover, along the equilibrium-preserving \(B\)-variation above,
\[
\left.rac{\partial}{\partial B}\operatorname{Re}\lambdaight|_{B=B_H}
=-rac{r(q-q_c)^2}{2q}<0.
\]
Thus the crossing is automatically transversal and increasing the inhibition parameter through \(B_H\) moves the positive equilibrium to the stable side.

Under the paper's reparametrization
\[
p=m,\quad q=n,\quad r=rac{g+1}a,\quad s=rac{1+D}g,
\quad \widetilde X=rac{ag}{(a+1)(g+1)+aD},
\]
one has the exact identity
\[
D=\omega_H^2.
\]
Consequently \(D\), introduced there as an algebraic parameter, is precisely the squared Hopf frequency in the original dimensionless time. The frequency in the paper's subsequently time-rescaled focus system is multiplied by \(1+B_H=n/(a-m+1+n)\), which explains its displayed value \(n\sqrt D/(a-m+1+n)\).

## Assumptions and scope
The statement concerns the smooth planar normalized system and the positive equilibrium \((1,1)\). The parameter \(B\) is varied while \(K\) changes according to the equilibrium relation, exactly as in the source's six-independent-parameter formulation. The result classifies ordinary Hopf points of this normalized family; it does not determine the Lyapunov coefficient, weak-focus order, number of bifurcating cycles, or the still-open codimension-six maximality question.

The incidence-independence statement fixes \((s,r,\widetilde X)\). It does not claim that the dimensional epidemic parameters can be varied independently while keeping the endemic prevalence fixed.

## Proof
The source gives the trace and determinant of the Jacobian at \((1,1)\) as
\[
\operatorname{Tr}_1=-rac{r}{1+B}(q-q_c)(B-B_H),
\]
\[
\det_1=rac{r}{(1+B)X_1}
\left[BqX_1+(1+B)(1-pX_1)ight].
\]
Assume first \(p>p_c\) and \(q>q_c\). Then \(q_c>0\) and \(B_H>0\). At \(B=B_H\),
\[
1+B_H=rac q{q-q_c},\qquad
rac{B_Hq}{1+B_H}=q_c.
\]
Therefore
\[
\det_H
=rac r{X_1}\left[q_cX_1+1-pX_1ight]
=rac r{X_1}(1-p_cX_1).
\]
Using \(X_1=1-(s+1)\widetilde X\) and the definition of \(p_c\),
\[
1-p_cX_1=s\widetilde X-rac{X_1}r,
\]
so
\[
\det_H=rac{rs\widetilde X}{X_1}-1
=rac{(s+1+sr)\widetilde X-1}{X_1}.
\]
Because \(X_1>0\), the condition \(\det_H>0\) is exactly
\[
\widetilde X>rac1{s+1+sr}.
\]
This gives the frequency formula \(\omega_H^2=\det_H\).

It remains to compare the source's two displayed Hopf alternatives. Its first alternative is already
\(p_c<p\le 1/X_1\), \(q>q_c\), together with the same strict lower bound on \(\widetilde X\). In the second alternative \(p>\max\{p_c,1/X_1\}\) and the source additionally writes \(q>q_1\), where
\[
q_1=rac{(1+B)(pX_1-1)}{BX_1}.
\]
At \(B=B_H\), multiplication by the positive quantity \(B_HX_1\) gives
\[
q>q_1
\iff q_cX_1>pX_1-1
\iff 1>p_cX_1
\iff \widetilde X>rac1{s+1+sr}.
\]
Hence the extra \(q_1\) condition in the second branch is exactly the determinant-positivity condition already expressed by the prevalence bound. Splitting at \(p=1/X_1\) is therefore unnecessary, and the union of the two branches is precisely the single criterion in the finding.

For transversality, a planar complex conjugate pair has real part \(\operatorname{Tr}_1/2\). Differentiating the exact trace identity at \(B=B_H\) gives
\[
\left.\partial_B\operatorname{Re}\lambdaight|_{B_H}
=-rac{r(q-q_c)}{2(1+B_H)}
=-rac{r(q-q_c)^2}{2q}<0.
\]

Finally substitute the source's variables \((a,m,n,g,D)\). Directly,
\[
X_1=rac{g+1}{(a+1)(g+1)+aD},
\]
and therefore
\[
rac{rs\widetilde X}{X_1}-1
=rac{(g+1)}arac{1+D}g
rac{ag}{g+1}-1=D.
\]
Thus \(D=\omega_H^2\). The source later multiplies the vector field by \(1+Bx^q\); at the equilibrium this factor is \(1+B_H=n/(a-m+1+n)\), so the rescaled angular frequency is \((1+B_H)\sqrt D=n\sqrt D/(a-m+1+n)\), exactly matching its focus-normal-form formula.

## Verification
Every equality used in the proof follows from the source's equations (18), (19), (21), (30), and (33). Two independent routes give the same positive-frequency condition: direct determinant positivity at \(B_H\), and the source's \(q>q_1\) condition in its high-\(p\) Hopf branch.

As an exact rational stress check, take \(s=1\), \(r=3/2\), \(\widetilde X=1/3\), \(p=3\), and \(q=2\). Then
\[
X_1=rac13,\quad p_c=rac83,\quad q_c=rac13,\quad B_H=rac15,
\quad \omega_H^2=rac12,
\]
and the crossing speed is \(-25/24\). The corresponding reparametrization values \(a=5/3\), \(m=3\), \(n=2\), \(g=3/2\), \(D=1/2\) reproduce \(B_H=1/5\) and \(D=\omega_H^2\). This finite example is only a consistency check; the theorem is proved algebraically for the full stated parameter region.

## Relationship to prior work
Yu, Tang, and Zeng derive the normalized system, the two-case Hopf conditions, and the exact trace/determinant formulas. In their generalized-Hopf reparametrization they display the frequency \(n\sqrt D/(a-m+1+n)\) after introducing the positive factor \(1+Bx^q\) used for focus calculations. They do not state the single-inequality Hopf criterion above, identify \(D\) as the squared frequency before that time rescaling, or state the incidence-exponent independence of the original-time onset frequency at fixed \((s,r,\widetilde X)\).

Earlier SIRS literature with generalized nonlinear incidence establishes Hopf bifurcation and computes normal forms or Lyapunov coefficients, including Alexander--Moghadas (2005) and Hu--Bi--Ma--Ruan (2011). The accessible primary descriptions do not state the present criterion or frequency invariant. Cui--Zhao (2024) treats saddle-node and Bogdanov--Takens bifurcations for the same power-rational incidence family; the 2026 source explicitly identifies its Hopf-codimension problem as left open by that work.

## Limitations
This result is a local linear statement at the positive equilibrium. It does not determine whether a particular Hopf point is ordinary or generalized beyond transversality, nor the criticality, amplitude, stability, or persistence range of periodic orbits. It also does not resolve the source's codimension-six conjecture. Literature searches cannot exclude an equivalent observation hidden in an unindexed or inaccessible older derivation; this is the principal originality risk.

## References
1. P. Yu, W. Tang, and Y. Zeng, “A codimension-5 Hopf bifurcation yielding 5 limit cycles in a SIRS epidemic model with nonlinear incidence rate,” arXiv:2609.38874v1, 2026.
2. Z. Hu, P. Bi, W. Ma, and S. Ruan, “Bifurcations of an SIRS epidemic model with nonlinear incidence rate,” *Discrete and Continuous Dynamical Systems - B* 15 (2011), 93–112. DOI: 10.3934/dcdsb.2011.15.93.
3. M. E. Alexander and S. M. Moghadas, “Bifurcation Analysis of an SIRS Epidemic Model with Generalized Incidence,” *SIAM Journal on Applied Mathematics* 65 (2005), 1794–1816. DOI: 10.1137/040604947.
4. W. Cui and Y. Zhao, “Saddle-node bifurcation and Bogdanov-Takens bifurcation of a SIRS epidemic model with nonlinear incidence rate,” *Journal of Differential Equations* 384 (2024), 252–278. DOI: 10.1016/j.jde.2023.11.030.
