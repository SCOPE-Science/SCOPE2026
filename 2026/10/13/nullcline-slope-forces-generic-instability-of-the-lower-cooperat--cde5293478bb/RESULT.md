# Nullcline slope forces generic instability of the lower cooperative-hunting equilibrium
## Finding
For the discrete Ricker predator-prey model with prey refuge and cooperative hunting,
\[
x_{n+1}=x_n\bigl[(1-b)+b e^{-y_n(1+c y_n)}\bigr]e^{r(1-x_n)},
\]
\[
y_{n+1}=\beta b x_n\bigl(1-e^{-y_n(1+c y_n)}\bigr),
\]
the two positive-equilibrium nullclines are
\[
x=f(y):=
1+\frac1r\log\!\bigl((1-b)+b e^{-y(1+c y)}\bigr)
\]
and
\[
x=g(y):=
\frac{y}{\beta b(1-e^{-y(1+c y)})}.
\]
Set
\[
H(y)=f(y)-g(y).
\]

At every positive equilibrium \(E=(x,y)\), the first Jury quantity has the exact geometric form
\[
\det(I-J(E))=-r y\,H'(y).
\]
This turns the relative slope of the two nullclines directly into a spectral statement.

In the strong-cooperation regime considered by De Silva and Jang,
\[
2c>1,\qquad \beta b<1,
\]
suppose there are exactly two positive equilibria
\[
E_{21}=(f(y_1),y_1),\qquad
E_{22}=(f(y_2),y_2),
\qquad 0<y_1<y_2.
\]
The lower crossing starts from \(H<0\), so
\[
H'(y_1)\ge0.
\]
Consequently, the lower equilibrium cannot be hyperbolically Schur-stable. If the crossing is transverse, then
\[
H'(y_1)>0
\]
and \(J(E_{21})\) has a real eigenvalue strictly larger than \(1\). Thus every transverse lower equilibrium is linearly unstable.

There is also a sharp saddle criterion. If the lower crossing is transverse and
\[
r x_1\le2,
\]
then one eigenvalue lies in \((-1,1)\) and the other in \((1,\infty)\), so \(E_{21}\) is a genuine saddle.

This supplies an analytic classification that the motivating article leaves open after reporting only numerical evidence that the lower equilibrium is either a saddle or a repeller.

## Assumptions and scope
The parameters satisfy
\[
r>0,\qquad \beta>0,\qquad 0<b<1,\qquad c>0.
\]
The accepted theorem concerns the two-positive-equilibrium regime
\[
2c>1,\qquad \beta b<1
\]
and assumes that the model has exactly two positive equilibria, as in Proposition 3.6 and the numerical examples of the source.

A transverse equilibrium means
\[
H'(y_i)\ne0.
\]
The lower equilibrium is proved linearly unstable whenever it is transverse. If
\[
H'(y_1)=0,
\]
the result proves that \(1\) is an eigenvalue, but it does not infer nonlinear instability from that nonhyperbolic case.

The stronger statement that the lower equilibrium is a saddle additionally assumes
\[
r x_1\le2.
\]
No stability claim is made for the upper equilibrium beyond the sign identity for its first Jury quantity.

## Proof
Write
\[
S(y)=e^{-y(1+c y)},
\qquad
D(y)=(1-b)+bS(y).
\]
At a positive equilibrium,
\[
D(y)e^{r(1-x)}=1
\]
and
\[
y=\beta b x(1-S(y)).
\]

The Jacobian is
\[
J(E)=
\begin{pmatrix}
1-rx & -b x e^{r(1-x)}S(y)(1+2cy)\\[2mm]
y/x & \beta b x S(y)(1+2cy)
\end{pmatrix}.
\]
Introduce
\[
A=\beta b xS(y)(1+2cy)
\]
and
\[
B=b y e^{r(1-x)}S(y)(1+2cy).
\]
Then
\[
\operatorname{tr}J=1-rx+A,
\qquad
\det J=(1-rx)A+B.
\]
Therefore
\[
\det(I-J)
=
1-\operatorname{tr}J+\det J
=
rx(1-A)+B.
\]

Now differentiate the predator nullcline. Since
\[
g(y)=\frac{y}{\beta b(1-S(y))},
\]
the equilibrium relation gives
\[
g'(y)=\frac{x}{y}(1-A).
\]
Hence
\[
rx(1-A)=r y g'(y).
\]

Similarly,
\[
f'(y)
=
-\frac{bS(y)(1+2cy)}{rD(y)}.
\]
Using
\[
e^{r(1-x)}=\frac1{D(y)}
\]
at equilibrium gives
\[
B=-r y f'(y).
\]
Combining these identities yields
\[
\det(I-J)
=
r y\bigl(g'(y)-f'(y)\bigr)
=
-r y H'(y).
\]

In the exactly-two-equilibrium regime, \(H(0+)<0\), the first zero is \(y_1\), and \(H\) is positive immediately after a transverse lower crossing. Hence
\[
H'(y_1)>0
\]
for a transverse lower equilibrium. Thus
\[
p_{E_{21}}(1)=\det(I-J(E_{21}))<0.
\]
Because \(p_{E_{21}}(\lambda)\) is a monic real quadratic and tends to \(+\infty\) as \(\lambda\to+\infty\), it has a real root
\[
\lambda_+>1.
\]
So the lower equilibrium is linearly unstable.

For the saddle refinement,
\[
p_E(-1)=1+\operatorname{tr}J+\det J
       =(2-rx)(1+A)+B.
\]
If
\[
rx\le2,
\]
then \(A>0\) and \(B>0\) imply
\[
p_E(-1)>0.
\]
Together with
\[
p_E(1)<0,
\]
the intermediate value theorem gives one eigenvalue in \((-1,1)\), while the other is \(>1\). Thus the lower equilibrium is a saddle.

If the lower zero is nontransverse, then
\[
H'(y_1)=0
\]
and the same identity gives
\[
p_{E_{21}}(1)=0,
\]
so \(1\) is an eigenvalue. This is the stated degenerate boundary of the result.

## Verification
The bundled script `verification/verify.py` reconstructs the two source parameter examples
\[
\beta=2,\qquad b=0.49,\qquad c=3
\]
at
\[
r=1
\]
and
\[
r=3.
\]
It solves \(H(y)=0\) by bisection, rebuilds the Jacobian from the model, and checks numerically that
\[
\det(I-J)=-r y H'(y)
\]
to tight tolerance.

For \(r=1\), it reproduces
\[
E_{21}\approx(0.9947339,0.0104492)
\]
and eigenvalues
\[
0.0106013,\qquad 1.0195174.
\]
For \(r=3\), it reproduces
\[
E_{21}\approx(0.9985180,0.0088588)
\]
and verifies an eigenvalue larger than \(1\), consistent with the source's reported instability.

The numerical replay is not the proof of the theorem. The proof is the exact nullcline-slope identity and the sign argument above.

## Relationship to prior work
De Silva and Jang derive the same Ricker-refuge-cooperation map, identify the two-equilibrium regime, and state that numerical simulations consistently make the lower equilibrium \(E_{21}\) either a saddle or a repeller. They explicitly leave a rigorous classification of \(E_{21}\) as an open problem because the Jury inequalities appear difficult to characterize.

An earlier cooperative-hunting model without prey refuge was analyzed by Chow, Jang, and Wang, who proved that one of two interior steady states is always a saddle. That result concerns a different prey-growth and interaction structure and does not imply the Ricker-plus-refuge calculation above. The 2023 refuge model of Jang and Yousef uses Beverton-Holt prey growth; its two-equilibrium regime is illustrated numerically, but it likewise does not contain the present Ricker nullcline identity.

The new step is the source-specific factorization
\[
\det(I-J(E))=-r y H'(y),
\]
which converts the first Jury condition into the sign of the nullcline crossing and immediately resolves the generic instability of the lower equilibrium in the 2026 model.

## Limitations
The theorem proves generic, transverse instability rather than a complete nonlinear classification of the codimension-one degenerate case
\[
H'(y_1)=0.
\]
At that case the Jacobian has eigenvalue \(1\), and higher-order analysis is required.

When
\[
r x_1>2,
\]
the result still proves a real eigenvalue \(>1\), but it does not determine whether the second eigenvalue lies inside or outside the unit disk. This is why the theorem distinguishes generic instability from the stronger saddle conclusion.

The result concerns local equilibrium stability. It does not determine global basin boundaries, periodic coexistence, or chaotic attractors.

## References
1. T. M. M. De Silva, S. R.-J. Jang, “Persistence, extinction, and chaotic dynamics in a predator-prey system with cooperative hunting and prey refuge,” AIMS Mathematics 11 (2026), 21412–21440. DOI: 10.3934/math.2026868.
2. Y. Chow, S. R.-J. Jang, H.-M. Wang, “Cooperative hunting in a discrete predator-prey system II,” Journal of Biological Dynamics 13 (2019), 247–264. DOI: 10.1080/17513758.2018.1555339.
3. S. R.-J. Jang, A. M. Yousef, “Effects of prey refuge and predator cooperation on a predator-prey system,” Journal of Biological Dynamics 17 (2023), 2242372. DOI: 10.1080/17513758.2023.2242372.
